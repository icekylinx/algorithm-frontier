"""Independent original-input exact mixed-target / signed scalar checks.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
Numeric count enumeration occurs only in this tiny independent comparator.
"""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product,islice
from math import comb
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
import targets as impl


def physical(rank,x):
    return all(sum(x[e] for e in range(len(x)) if s>>e&1)<=bound for s,bound in enumerate(rank))


def original(rank,rows,relations,targets,scalar,mandatory=False,eligible=None):
    n=len(scalar)
    eligible=(True,)*n if eligible is None else eligible
    answers=[]
    for x in product(*(range(rank[1<<e]+1) if eligible[e] else (0,) for e in range(n))):
        if not physical(rank,x) or (mandatory and sum(x)!=rank[-1]): continue
        good=True
        for row,relation,target in zip(rows,relations,targets):
            value=sum(a*b for a,b in zip(row,x))
            if not {'<=':value<=target,'=':value==target,'>=':value>=target}[relation]: good=False;break
        if good: answers.append((sum((a*b for a,b in zip(scalar,x)),F(0)),x))
    return tuple(answers)


def check_output(data,answer):
    rank,rows,relations,targets,scalar,mandatory,eligible=data
    n=len(scalar)
    assert type(answer) is impl.Answer and len(answer.counts)==n
    assert all(type(x) is int and x>=0 and (eligible[e] or not x) for e,x in enumerate(answer.counts))
    assert physical(rank,answer.counts) and (not mandatory or sum(answer.counts)==rank[-1])
    for row,relation,target in zip(rows,relations,targets):
        value=sum(a*b for a,b in zip(row,answer.counts))
        assert {'<=':value<=target,'=':value==target,'>=':value>=target}[relation]
    assert answer.value==sum((a*b for a,b in zip(scalar,answer.counts)),F(0))


def main():
    rng=random.Random(271110)
    fixtures=[]
    for n in (1,2,3):
        for _ in range(16):
            pools=tuple((rng.randrange(1,1<<n),rng.randrange(1,3)) for _ in range(2))
            rank=tuple(sum(cap for support,cap in pools if s&support) for s in range(1<<n))
            d=rng.randrange(1,4)
            rows=tuple(tuple(rng.randrange(4) for _ in range(n)) for _ in range(d))
            relations=tuple(rng.choice(('<=','=','>=')) for _ in range(d))
            targets=tuple(rng.randrange(4) for _ in range(d))
            scalar=tuple(rng.choice((F(-2),F(0),F(1),F(3,2))) for _ in range(n))
            eligible=tuple(rng.choice((True,True,False)) for _ in range(n))
            for mandatory in (False,True): fixtures.append((rank,rows,relations,targets,scalar,mandatory,eligible))
    # Deterministic overlapping covers, zero targets, absent zero-vector
    # classes and optional/mandatory distinction with genuine signed weights.
    for mandatory in (False,True):
        fixtures.extend((((0,2,2,3),( (2,1),(1,2)),('>=','>='),(2,2),(F(-1),F(2)),mandatory,(True,True)),
                         ((0,2,2,3),((1,0),(0,1)),('=','>='),(0,1),(F(-3),F(2)),mandatory,(True,True)),
                         ((0,1,1,1),((1,1),),('=',),(2,),(F(1),F(-1)),mandatory,(True,True)),
                         ((0,2,2,3),((0,0),),('<=',),(1,),(F(-2),F(3)),mandatory,(True,True))))
    solved=infeasible=chains=inspected=0
    for data in fixtures:
        truth=original(*data)
        model=impl.Targets(*data)
        prepared=model.prepare()
        # Original support sets are reconstructed without the compiler.
        expected=tuple(sorted({tuple(j for j,t in enumerate(data[3]) if t>0 and data[1][j][e])
                               for e in range(model.n) if data[6][e] and
                               all(r=='>=' or row[e]<=t for row,r,t in zip(data[1],data[2],data[3]))}-{()}))
        assert prepared.supports==expected
        for maximize in (False,True):
            answer=model.solve(maximize)
            if not truth:
                assert answer is None
                infeasible+=1
            else:
                assert answer is not None and model.verify(answer)
                check_output(data,answer)
                assert answer.value==(max if maximize else min)(v for v,x in truth)
            solved+=1
        for chain in model.chains():
            assert len(chain.keys)<= (model.n+int(not model.mandatory))*(len(prepared.covers)+1)
            assert len({(e,v) for (e,_),v in zip(chain.keys,chain.columns)})==len(chain.keys)
            vectors=tuple(v for v,_ in chain.classes)
            # Finite independent vector-multiplicity oracle, not compiler DFS.
            expected_profiles=set()
            ranges=tuple(range(min([model.total]+[cap//a for a,cap in zip(v,chain.upper) if a])+1) for v in vectors)
            for h in product(*ranges):
                loads=tuple(sum(v[j]*count for v,count in zip(vectors,h)) for j in range(len(chain.upper)))
                if sum(h)<=model.total and all(lo<=x<=hi for lo,x,hi in zip(chain.lower,loads,chain.upper)):
                    expected_profiles.add(h)
            actual=tuple(model.profile_vectors(chain))
            assert len(actual)==len(set(actual)) and set(actual)==expected_profiles
            inspected+=len(actual)
            chains+=1
    # Exact-support composition / Vandermonde bound, checked with independently
    # enumerated profiles for all subsets of this small vector universe.
    universe=((1,0),(2,0),(0,1),(0,2),(1,1),(1,2),(2,1),(2,2))
    profile_checks=0
    for pick in range(1<<len(universe)):
        vectors=tuple(v for i,v in enumerate(universe) if pick>>i&1)
        caps=(2,2)
        actual=tuple(impl.profiles(vectors,caps,4))
        expected=tuple(h for h in product(range(3),repeat=len(vectors)) if sum(h)<=4 and
                       all(sum(v[j]*count for v,count in zip(vectors,h))<=caps[j] for j in range(2)))
        assert set(actual)==set(expected) and len(actual)==len(expected)
        supports={tuple(i for i,a in enumerate(v) if a) for v in vectors}
        assert len(actual)<=2**sum(caps)*comb(len(supports)+sum(caps),sum(caps))
        profile_checks+=1
    # Common stopping unit, empty intermediate chain layers, zero cover entries,
    # large coefficients and extra mandatory mass all remain sound and complete.
    tied=impl.Targets((0,2,2,3),((3,0),(2,1)),('>=','>='),(2,2),(F(-1),F(5)),True)
    assert tied.solve().counts==(2,1) and tied.solve(True).value==9
    # Zero coefficient coordinates retain signed scalar and mandatory mass;
    # a single binary residual count is not iterated over.
    huge=1<<100
    large=impl.Targets((0,huge,huge,huge),((1,0),),('=',),(1,),(F(7,3),F(-2)),True)
    answer=large.solve()
    assert answer.counts==(1,huge-1) and answer.value==F(7,3)-2*(huge-1)
    automatic=impl.Targets((0,huge),((0,),),('<=',),(0,),(F(-3),),False)
    assert automatic.solve().counts==(huge,) and automatic.solve(True).counts==(0,)
    assert automatic.last_stats=={'chains':0,'profiles':0}
    # Upper/equality mask cannot silently lower an original mandatory total.
    mandatory=impl.Targets((0,1,1,2),((1,0),),('=',),(0,),(0,0),True)
    optional=impl.Targets((0,1,1,2),((1,0),),('=',),(0,),(0,0),False)
    assert mandatory.prepare().rank_loss and mandatory.solve() is None and optional.verify(optional.solve())
    empty=impl.Targets((0,),(),(),(),(),True)
    assert empty.verify(empty.solve()) and empty.solve().counts==()
    zero_rank=impl.Targets((0,0),((1,),),('>=',),(1,),(0,),False)
    assert zero_rank.solve() is None
    # Explicit DFS handles large occupied depth with one all-zero profile.
    assert tuple(islice(impl.profiles(tuple((i+1,) for i in range(1100)),(0,),0),1))==((0,)*1100,)
    # Producer-independent original verifier and forged objective/eligibility.
    model=impl.Targets((0,2,2,3),((1,1),),('>=',),(1,),(F(-1),F(2)),False)
    good=model.solve()
    saved=impl.Targets.chains,impl.Targets.recover,impl.shared.active_vertex
    def unavailable(*a,**kw): raise AssertionError('verifier used producer')
    try:
        impl.Targets.chains=impl.Targets.recover=impl.shared.active_vertex=unavailable
        assert model.verify(good)
    finally: impl.Targets.chains,impl.Targets.recover,impl.shared.active_vertex=saved
    forged=(replace(good,value=good.value+1),replace(good,counts=(3,3)),replace(good,counts=(1.0,0)),replace(good,counts=(-1,2)))
    assert not any(model.verify(a) for a in forged)
    invalid=0
    for thunk in (lambda:impl.Targets((0,2,2,1),(),(),(),(0,0)),
                  lambda:impl.Targets((0,1),((F(1,2),),),('=',),(1,),(0,)),
                  lambda:impl.Targets((0,1),((1,),),('=',),(-1,),(0,)),
                  lambda:impl.Targets((0,1),(),(),(),(0.5,)),
                  lambda:impl.Targets((0,1),(),(),(),(0,),eligible=(1,)),
                  lambda:impl.Targets((0,1),(),(),(),(0,),mandatory=1),
                  lambda:model.solve(1),lambda:tuple(impl.profiles(((0,),),(1,),1))):
        try: thunk()
        except ValueError: invalid+=1
        else: raise AssertionError('invalid data accepted')
    print(f'PASS: {len(fixtures)} original instances; {solved} signed min/max optimizations ({infeasible} infeasible); {chains} cover chains and {inspected} independently enumerated bounded profiles; {profile_checks} vector universes/composition bounds; tied stops/shared capacity/signed zero columns;101-bit rank with exact mandatory total;zero-row greedy and rank-loss gates;deep occupied DFS;producer-disabled verifier;{len(forged)} forged outputs;{invalid} malformed inputs.')


if __name__=='__main__': main()
