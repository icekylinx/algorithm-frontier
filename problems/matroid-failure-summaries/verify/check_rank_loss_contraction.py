#!/usr/bin/env python3
"""Verify a fixed rank-loss contraction against original subset ranks.

The construction uses only independence queries.  The reference computes
canonical greedy membership by original prefix rank differences, enumerates
all failures, and verifies contraction/deletion and prefix rank equalities.
"""
from itertools import combinations, permutations
import argparse
import json
import random
import sys

from check_summaries import all_matroid_rank_tables
from check_weighted_obstruction import ITEMS, independent as obstruction_independent


def require(condition,message):
    if not condition:
        raise AssertionError(message)


def bits(mask):
    while mask:
        bit=mask & -mask
        yield bit.bit_length()-1
        mask^=bit


def survivors(ground,labels,failed):
    return sum(1<<e for e in bits(ground) if not labels[e]&failed)


def union_labels(ground,labels):
    result=0
    for e in bits(ground): result |= labels[e]
    return result


def failure_sets(labels):
    universe=union_labels((1<<len(labels))-1,labels)
    subset=universe
    while True:
        yield subset
        if not subset: return
        subset=(subset-1)&universe


def label_patterns(n):
    """Every one-label partition up to renaming, plus an unlabelled class."""
    def visit(prefix,largest):
        if len(prefix)==n:
            yield tuple(0 if c==0 else 1<<(c-1) for c in prefix)
            return
        for c in range(largest+2):
            yield from visit(prefix+(c,),max(largest,c))
    yield from visit((),0)


def construct(labels,order,independent):
    queries=0
    def ask(mask):
        nonlocal queries
        queries+=1
        return independent(mask)
    def greedy(failed):
        result=0
        for e in order:
            if labels[e]&failed: continue
            if ask(result|(1<<e)): result |= 1<<e
        return result
    original=greedy(0)
    labelled=union_labels(original,labels)
    q_zero=sum(1<<e for e in bits(original) if not labels[e])
    contracted=q_zero
    blocks={}
    replacements={}
    losses={}
    for ell in bits(labelled):
        label=1<<ell
        survivor_basis=greedy(label)
        replacements[label]=survivor_basis & ~original
        losses[label]=original.bit_count()-survivor_basis.bit_count()
        extension=0
        for e in order:
            if original>>e&1 and labels[e]==label:
                if ask(survivor_basis|extension|(1<<e)):
                    extension|=1<<e
        require(extension.bit_count()==losses[label],'extension size equals single-failure loss')
        blocks[label]=extension
        contracted|=extension
    total=sum(mask.bit_count() for mask in replacements.values())
    require(total==original.bit_count()-q_zero.bit_count()-sum(losses.values()),'replacement identity')
    require(contracted.bit_count()==original.bit_count()-total,'contracted rank')
    require(queries<=len(labels)*(1+labelled.bit_count())+original.bit_count(),'construction query cap')
    return original,contracted,blocks,total,queries


def canonical_from_ranks(ground,order,rank):
    accepted=prefix=0
    current=rank(0)
    for e in order:
        if not ground>>e&1: continue
        prefix|=1<<e
        new=rank(prefix)
        require(new-current in (0,1),'matroid rank increment')
        if new>current: accepted|=1<<e
        current=new
    return accepted


def contracted_tree(labels,order,contracted,rank,budget):
    rank_q=contracted.bit_count()
    minor_order=tuple(e for e in order if not contracted>>e&1)
    universe=union_labels(sum(1<<e for e in minor_order),labels)
    budget=min(budget,universe.bit_count())
    retained=0
    queries=nodes=0
    if rank((1<<len(labels))-1)==rank_q:
        return 0,0,0
    def visit(failed,left):
        nonlocal retained,queries,nodes
        basis=0
        nodes+=1
        for e in minor_order:
            if labels[e]&failed: continue
            queries+=1
            if rank(contracted|basis|(1<<e))==rank_q+basis.bit_count()+1:
                basis|=1<<e
        retained|=basis
        if left:
            for ell in bits(union_labels(basis,labels)):
                visit(failed|(1<<ell),left-1)
    visit(0,budget)
    return retained,queries,nodes


def verify_case(rank,labels,order,counts,all_subsets=True,rng=None):
    n=len(labels);ground=(1<<n)-1
    r=rank(ground)
    independent=lambda x:rank(x)==x.bit_count()
    b0,q,blocks,total,queries=construct(labels,order,independent)
    counts['instances']+=1
    counts['construction_queries']+=queries
    counts['rank_zero_minor']+=total==0
    counts['rank_one_minor']+=total==1
    counts['strict_rank_reductions']+=total<r
    require(independent(q),'contracted set independent')
    require(rank(ground)-q.bit_count()==total,'minor rank is T')
    references={}
    for failed in failure_sets(labels):
        live=survivors(ground,labels,failed)
        q_live=q&live;q_failed=q&~live
        basis=canonical_from_ranks(live,order,rank)
        require(q_live&~basis==0,'surviving contracted items remain canonical')
        require(rank(live|q_failed)==rank(live)+q_failed.bit_count(),'joint failed-block independence')
        minor_live=live&~q
        rank_minor=lambda subset:rank(subset|q)-q.bit_count()
        minor_basis=canonical_from_ranks(minor_live,order,rank_minor)
        require(basis==(q_live|minor_basis),'canonical contraction decomposition')
        references[failed]=basis
        counts['failure_instances']+=1
        prefix=0
        for e in order:
            prefix|=1<<e
            p_live=prefix&live
            require(rank(p_live)==(p_live&q).bit_count()+rank_minor(p_live&~q),
                    'every original prefix rank reconstructed exactly')
            counts['prefix_comparisons']+=1
        if all_subsets:
            subsets=[]
            subset=minor_live
            while True:
                subsets.append(subset)
                if not subset:break
                subset=(subset-1)&minor_live
        else:
            subsets=[0,minor_live]
            subsets += [rng.getrandbits(n)&minor_live for _ in range(40)]
        for subset in subsets:
            require(rank_minor(subset)==rank(subset|q_live)-q_live.bit_count(),
                    'fixed contraction equals surviving contraction after failure')
            counts['contraction_rank_comparisons']+=1
        outside=basis&~b0
        bound=sum((canonical_from_ranks(survivors(ground,labels,1<<ell),order,rank)&~b0).bit_count()
                  for ell in bits(failed))
        require(outside.bit_count()<=bound<=total,'surviving replacement count bounded by T')
        residual_sum=0
        for ell in bits(union_labels(live,labels)):
            one_more=canonical_from_ranks(survivors(live,labels,1<<ell),order,rank)
            residual_sum+=(one_more&~basis).bit_count()
        require(residual_sum<=total,'residual replacement total never increases')
    label_count=union_labels(ground,labels).bit_count()
    for h in range(label_count+1):
        expected=0
        for failed,basis in references.items():
            if failed.bit_count()<=h: expected|=basis
        minor_h,minor_queries,nodes=contracted_tree(labels,order,q,rank,h)
        require(q|minor_h==expected,'full prefix union via fixed contraction')
        minor_n=n-q.bit_count()
        require(minor_queries<=minor_n*sum(total**i for i in range(h+1)), 'minor query cap')
        if total==0:
            require(expected==b0,'T=0 unchanged union at every budget')
        if total==1:
            require(expected.bit_count()<=r+h,'sharp T=1 support bound')
        counts['budget_instances']+=1
        counts['minor_independence_queries']+=minor_queries
    huge,_,_=contracted_tree(labels,order,q,rank,10**100)
    require(q|huge==references_union(references),'binary-large h clips to occurring labels')
    counts['huge_budget_instances']+=1


def references_union(references):
    result=0
    for basis in references.values():result|=basis
    return result


def fresh_counts():
    return {key:0 for key in ('matroids','instances','construction_queries','rank_zero_minor','rank_one_minor',
        'strict_rank_reductions','failure_instances','prefix_comparisons','contraction_rank_comparisons',
        'budget_instances','minor_independence_queries','huge_budget_instances')}


def check_small(max_n=3):
    counts=fresh_counts()
    for n in range(max_n+1):
        pats=list(label_patterns(n));orders=list(permutations(range(n)))
        for table in all_matroid_rank_tables(n):
            counts['matroids']+=1
            for labels in pats:
                for order in orders:
                    verify_case(lambda subset,table=table:table[subset],labels,order,counts)
        print(json.dumps({'checkpoint_n':n,'instances':counts['instances']}),file=sys.stderr,flush=True)
    return counts


def binary_rank(vectors,subset):
    pivots={}
    for e in bits(subset):
        value=vectors[e]
        while value:
            high=value.bit_length()-1
            if high in pivots:value^=pivots[high]
            else:
                pivots[high]=value
                break
    return len(pivots)


def check_larger():
    counts=fresh_counts();rng=random.Random(20261101)
    for _ in range(180):
        n=rng.randrange(5,11);r=rng.randrange(1,6)
        vectors=[rng.randrange(1<<r) for _ in range(n)]
        labels=tuple(rng.choice((0,1,2,4,8)) for _ in range(n))
        order=list(range(n));rng.shuffle(order)
        rank=lambda subset,vectors=vectors:binary_rank(vectors,subset)
        verify_case(rank,labels,tuple(order),counts,False,rng)
        counts['matroids']+=1
    # Explicit T=1 tight examples with unlabelled coloops and a colored parallel chain.
    for coloop_count in range(5):
        for chain_length in range(2,9):
            vectors=[1<<j for j in range(coloop_count)]+[1<<coloop_count]*chain_length
            labels=(0,)*coloop_count+tuple(1<<j for j in range(chain_length))
            rank=lambda subset,vectors=vectors:binary_rank(vectors,subset)
            order=tuple(range(len(vectors)))
            verify_case(rank,labels,order,counts,False,rng)
            b0,q,_,total,_=construct(labels,order,lambda x:rank(x)==x.bit_count())
            require(total==1,'tight family has T=1')
            for h in range(chain_length):
                minor,_,_=contracted_tree(labels,order,q,rank,h)
                require((q|minor).bit_count()==coloop_count+1+h,'T=1 bound attained')
            counts['matroids']+=1
    # A nonrepresentable obstruction plus colored private components and unlabelled coloops.
    n0=len(ITEMS)
    old_rank=[]
    for subset in range(1<<n0):
        best=0
        for e in bits(subset):
            if obstruction_independent(best|(1<<e)):best|=1<<e
        old_rank.append(best.bit_count())
    base_labels=tuple(1<<('ABCD'.index(item[1])) for item in ITEMS)
    for private_count in range(5):
        labels=base_labels+tuple(1<<j for j in range(private_count) for _ in range(2))+(0,0)
        def rank(subset,private_count=private_count):
            value=old_rank[subset&((1<<n0)-1)]
            for j in range(private_count):
                value+=bool(subset&((3<<(n0+2*j))))
            value+=(subset>>(n0+2*private_count)).bit_count()
            return value
        for _ in range(3):
            order=list(range(len(labels)));rng.shuffle(order)
            verify_case(rank,labels,tuple(order),counts,False,rng)
        counts['matroids']+=1
    return counts


if __name__=='__main__':
    require(__debug__,'run without -O')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full',action='store_true',
                        help='enumerate every four-item matroid, label partition and order')
    args=parser.parse_args()
    small=check_small(4 if args.full else 3)
    larger=check_larger()
    print(json.dumps({'small':small,'larger':larger},indent=2,sort_keys=True))
