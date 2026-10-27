"""Independent original common-set / fixed-rank valuation comparisons.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
No baseline, potential, compression or path helper enters the tiny oracles.
"""
from dataclasses import replace
from fractions import Fraction as F
from itertools import combinations,permutations
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
import matroid_reporting as ordinary
import valuated_reporting as native


def allsets(n):
    return tuple(frozenset(c) for k in range(n+1) for c in combinations(range(n),k))


def valuation_table(matrix,n):
    k=len(matrix)
    values={}
    for basis in combinations(range(n),k):
        candidates=tuple(sum((matrix[row][e] for row,e in enumerate(order)),F(0))
                         for order in permutations(basis) if all(matrix[row][e] is not None for row,e in enumerate(order)))
        if candidates: values[frozenset(basis)]=min(candidates)
    return values


def axiom(table):
    checks=0
    for a,va in table.items():
        for b,vb in table.items():
            for e in a-b:
                assert any(a-{e}|{f} in table and b-{f}|{e} in table and
                           va+vb>=table[a-{e}|{f}]+table[b-{f}|{e}] for f in b-a)
                checks+=1
    return checks


def main():
    rng=random.Random(280910)
    tables=pairs=queries=failed_queries=nonoptimal=axioms=certificates=hubs=0
    # Deterministic nonlinear assignment valuations: no linear element cost
    # can give different totals on complementary pairs with the same union.
    fixture=valuation_table(((0,0,5,5),(5,5,0,0)),4)
    assert fixture[frozenset((0,1))]+fixture[frozenset((2,3))] != fixture[frozenset((0,2))]+fixture[frozenset((1,3))]
    instances=[(4,2,fixture,valuation_table(((0,4,0,4),(4,0,4,0)),4))]
    for n in range(1,7):
        for k in range(min(3,n)+1):
            for _ in range(4):
                matrices=tuple(tuple(tuple(None if rng.randrange(7)==0 else F(rng.randrange(-6,8),rng.choice((1,2,3)))
                                          for e in range(n)) for row in range(k)) for i in range(2))
                first,second=(valuation_table(matrix,n) for matrix in matrices)
                if first and second: instances.append((n,k,first,second))
    for n,k,first,second in instances:
        axioms+=axiom(first)+axiom(second)
        tables+=2
        common=tuple(b for b in first if b in second)
        if not common: continue
        optimum=min(first[b]+second[b] for b in common)
        best=tuple(b for b in common if first[b]+second[b]==optimum)
        # All optimal supplied baselines are checked, including zero/signed ties.
        for chosen in best:
            baseline=tuple(sorted(chosen))
            certificate=native.certify(n,k,first.get,second.get,baseline)
            assert native.verify_optimality(n,k,first.get,second.get,certificate)
            assert certificate.value==optimum
            shifted=replace(certificate,prices=tuple(p+F(17,3) for p in certificate.prices))
            assert native.verify_optimality(n,k,first.get,second.get,shifted)
            reporter=native.build(n,k,first.get,second.get,baseline)
            assert reporter.query()==baseline and reporter.optimum_cost()==optimum
            for failed in range(n):
                available=tuple(b for b in common if failed not in b)
                answer=reporter.query(failed)
                if not available:
                    assert answer is None and reporter.optimum_cost(failed) is None
                    failed_queries+=1
                else:
                    assert answer is not None and len(answer)==len(set(answer))==k and failed not in answer
                    b=frozenset(answer)
                    value=min(first[c]+second[c] for c in available)
                    assert b in first and b in second and first[b]+second[b]==value==reporter.optimum_cost(failed)
                    assert set(answer)<=set(reporter.support)
                queries+=1
            hubs+=sum(r is not None and r.hub is not None for r in reporter.routes.values())
            certificates+=1
        for chosen in common:
            if first[chosen]+second[chosen]==optimum: continue
            try: native.certify(n,k,first.get,second.get,tuple(sorted(chosen)))
            except ValueError: nonoptimal+=1
            else: raise AssertionError('nonoptimal common baseline accepted')
        pairs+=1
    # Full zero-valued effective domains create many tied supplied baselines.
    zero={frozenset(c):F(0) for c in combinations(range(5),2)}
    for chosen in zero:
        reporter=native.build(5,2,zero.get,zero.get,tuple(sorted(chosen)))
        for failed in range(5):
            answer=reporter.query(failed)
            assert len(answer)==2 and len(set(answer))==2 and failed not in answer
            queries+=1
    # Long original partition domains force the entire cycle on failure,
    # exercising valued hub reports with signed rational valuation increments.
    long_queries=long_hubs=0
    for k in (8,25):
        n=2*k
        def first_value(chosen):
            if len(chosen)!=k or len({e % k for e in chosen})!=k: return None
            return sum((F(-1) if e<k else F(1,k) for e in chosen),F(0))
        def second_value(chosen):
            groups={e if e<k else (e-k+1) % k for e in chosen}
            return F(0) if len(chosen)==len(groups)==k else None
        reporter=native.build(n,k,first_value,second_value,tuple(range(k)))
        cert=native.certify(n,k,first_value,second_value,tuple(range(k)))
        assert native.verify_optimality(n,k,first_value,second_value,cert)
        for failed in range(k):
            assert set(reporter.query(failed))==set(range(k,n))
            assert reporter.optimum_cost(failed)==1
            long_queries+=1
            long_hubs+=reporter.routes[failed].hub is not None
    assert long_hubs>0
    # Independent ordinary max-cardinality / min-cost truth, with rank drops.
    max_instances=max_queries=rank_drops=0
    for n in range(6):
        sets=allsets(n)
        for _ in range(14):
            blocks1=tuple(rng.randrange(3) for e in range(n))
            blocks2=tuple(rng.randrange(3) for e in range(n))
            caps1=tuple(rng.randrange(3) for _ in range(3))
            caps2=tuple(rng.randrange(3) for _ in range(3))
            first=lambda x:all(sum(blocks1[e]==b for e in x)<=caps1[b] for b in range(3))
            second=lambda x:all(sum(blocks2[e]==b for e in x)<=caps2[b] for b in range(3))
            costs=tuple(F(rng.randrange(-5,7),rng.choice((1,2,3))) for e in range(n))
            common=tuple(b for b in sets if first(b) and second(b))
            original_rank=max(map(len,common))
            reporter=ordinary.build_maximum(costs,first,second)
            for failed in (None,*range(n)):
                available=tuple(b for b in common if failed not in b)
                rank=max(map(len,available))
                optimum=min(sum((costs[e] for e in b),F(0)) for b in available if len(b)==rank)
                answer=reporter.query(failed)
                assert frozenset(answer) in available and len(answer)==rank==reporter.rank_after(failed)
                assert sum((costs[e] for e in answer),F(0))==optimum==reporter.optimum_cost(failed)
                assert set(answer)<=set(reporter.support)
                max_queries+=1
                rank_drops+=rank<original_rank
            max_instances+=1
    # Forced rank drop with a nontrivial signed/rational lower-rank optimum.
    costs=(F(5),F(-7,3),F(2))
    first=lambda x:len(x)<=2
    second=lambda x:len(x)<=2 and not {1,2}<=set(x)
    reporter=ordinary.build_maximum(costs,first,second)
    assert reporter.rank==2 and reporter.rank_after(0)==1 and reporter.query(0)==(1,)
    assert reporter.optimum_cost(0)==F(-7,3)
    # Original certificate verification is independent of every producer.
    n,k,first,second=instances[0]
    common=tuple(b for b in first if b in second)
    chosen=min(common,key=lambda b:first[b]+second[b])
    certificate=native.certify(n,k,first.get,second.get,tuple(sorted(chosen)))
    saved=native._certify,native._candidates,native.build
    def unavailable(*args,**kw): raise AssertionError('producer used')
    try:
        native._certify=native._candidates=native.build=unavailable
        assert native.verify_optimality(n,k,first.get,second.get,certificate)
    finally: native._certify,native._candidates,native.build=saved
    # A tight first-valuation exchange makes an upward outside-price forgery fail.
    forged_prices=list(certificate.prices)
    outside=next(e for e in range(n) if e not in chosen)
    forged_prices[outside]+=100
    forged=(replace(certificate,value=certificate.value+1),replace(certificate,prices=tuple(forged_prices)),
            replace(certificate,baseline=(0,0)),replace(certificate,prices=(0.0,)*n))
    assert not any(native.verify_optimality(n,k,first.get,second.get,c) for c in forged)
    # Large original ground is preprocessing-only; rank-small final objects and
    # all queries work after every original callback/producer is unavailable.
    n=1024
    enabled=True
    calls=0
    def value(chosen):
        nonlocal calls
        if not enabled: raise AssertionError('valuation called during query')
        calls+=1
        return sum((F(e) for e in chosen),F(0)) if len(chosen)==2 else None
    valued=native.build(n,2,value,value,(0,1))
    ordinary_max=ordinary.build_maximum(tuple(range(n)),lambda x:len(x)<=2,lambda x:len(x)<=2)
    assert valued.support==(0,1,2) and valued.record_count<50
    assert ordinary_max.record_count<100
    previous=calls
    enabled=False
    for failed in (None,0,1,2,n-1):
        assert valued.query(failed) is not None and valued.optimum_cost(failed) is not None
        assert ordinary_max.query(failed) is not None and ordinary_max.rank_after(failed)==2
    assert calls==previous
    # Rank zero keeps both valuation constants and no cross-rank interpretation.
    empty=lambda chosen:F(-11,7) if not chosen else None
    reporter=native.build(4,0,empty,empty,())
    assert reporter.query(0)==() and reporter.optimum_cost(0)==F(-22,7)
    invalid=0
    for thunk in (lambda:native.build(2,1,lambda x:None,lambda x:None,(0,)),
                  lambda:native.build(2,1,lambda x:1.0,lambda x:0,(0,)),
                  lambda:native.build(2,1,lambda x:0,lambda x:0,(0,0)),
                  lambda:native.build(2,1,lambda x:0,lambda x:0,(True,)),
                  lambda:native.build(2,3,lambda x:0,lambda x:0,(0,1,2)),
                  lambda:ordinary.build_maximum((1.0,),lambda x:True,lambda x:True)):
        try: thunk()
        except ValueError: invalid+=1
        else: raise AssertionError('invalid input accepted')
    print(f'PASS: {tables} independently axiom-checked valuation tables/{axioms} exchange axioms; '
          f'{pairs} common-domain pairs/{certificates} certified optimal baselines; {queries} exact valued failure queries '
          f'({failed_queries} infeasible); {nonoptimal} nonoptimal baselines rejected; {hubs} tiny hub reports; '
          f'{long_queries} long valued queries/{long_hubs} hub reports; '
          f'{max_instances} ordinary max-cardinality instances/{max_queries} queries/{rank_drops} rank drops; '
          f'signed fallback fixture; producer-independent certificate; {len(forged)} forged prices/values; '
          f'1024-ground retained/query isolation; fixed-rank zero constants; {invalid} malformed inputs.')


if __name__=='__main__': main()
