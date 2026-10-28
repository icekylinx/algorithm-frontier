#!/usr/bin/env python3
"""Independent original common-set checks for price and insertion queries.
Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
import price as native


rng=random.Random(6123)
counts={'instances':0,'queries':0,'insertions':0,'infeasible':0,'invalid':0}
for n in range(7):
    sets=tuple(frozenset(s) for r in range(n+1) for s in combinations(range(n),r))
    for trial in range(24):
        blocks1=tuple(rng.randrange(3) for _ in range(n))
        blocks2=tuple(rng.randrange(3) for _ in range(n))
        caps1=tuple(rng.randrange(3) for _ in range(3));caps2=tuple(rng.randrange(3) for _ in range(3))
        def first(s):return all(sum(blocks1[e]==j for e in s)<=caps1[j] for j in range(3))
        def second(s):return all(sum(blocks2[e]==j for e in s)<=caps2[j] for j in range(3))
        active=frozenset(e for e in range(n) if trial%2==0 or rng.randrange(3))
        common=tuple(s for s in sets if first(s) and second(s))
        rank=rng.randrange(n+2)
        costs=tuple(F(rng.randrange(-7,8),rng.randrange(1,5)) for _ in range(n))
        oracle=native.build_price(costs,rank,first,second,active)
        available=tuple(s for s in common if len(s)==rank and s<=active)
        if not available:
            assert oracle is None;counts['infeasible']+=1;continue
        assert oracle.baseline_cost==min(sum((costs[e] for e in s),F(0)) for s in available)
        for e in range(n):
            enlarged=active|{e}
            feasible=tuple(s for s in common if len(s)==rank and s<=enlarged)
            for delta in (F(-100),F(-3,2),F(0),F(7,3),F(100)):
                value,chosen=oracle.query(e,delta)
                actual=min(sum((costs[j] for j in s),F(0))+(delta if e in s else 0) for s in feasible)
                assert value==actual and frozenset(chosen) in feasible and len(chosen)==len(set(chosen))==rank
                assert sum((costs[j] for j in chosen),F(0))+(delta if e in chosen else 0)==actual
                counts['queries']+=1;counts['insertions']+=e not in active
        counts['instances']+=1
# A long exchange cycle exercises positive/negative primary return edges.
for rank in (8,27):
    n=2*rank
    first=lambda s:len({e%rank for e in s})==len(s)
    second=lambda s:len({e if e<rank else (e-rank+1)%rank for e in s})==len(s)
    costs=tuple(F(-1) if e<rank else F(1,rank) for e in range(n))
    oracle=native.build_price(costs,rank,first,second)
    value,chosen=oracle.query(rank,-10**100)
    assert set(chosen)==set(range(rank,n)) and value==1-10**100
# Catalog insertion may have negative gap; baseline is optimal only on active set.
one=lambda s:len(s)<=1
costs=[F(2),F(-10**100),F(7)]
oracle=native.build_price(costs,1,one,one,(0,2))
assert oracle.query(1)==(-10**100,(1,))
# Final state does not need original costs, original predicates or initialization.
costs.clear()
saved=native.weighted.minimum_cost,native.reporting._distances
native.weighted.minimum_cost=native.reporting._distances=lambda *a,**k:(_ for _ in ()).throw(AssertionError('producer disabled'))
assert oracle.query(1)==(-10**100,(1,))
assert oracle.query(0,100)==(7,(2,))
native.weighted.minimum_cost,native.reporting._distances=saved
for args in [((0,),-1,one,one,None),((0,),True,one,one,None),((0.0,),1,one,one,None),((0,),1,one,one,(0,0)),((0,),1,one,one,(1,))]:
    try:native.build_price(*args)
    except ValueError:counts['invalid']+=1
    else:raise AssertionError('invalid original input accepted')
for e,delta in [(True,0),(-1,0),(3,0),(0,0.5)]:
    try:oracle.query(e,delta)
    except ValueError:counts['invalid']+=1
    else:raise AssertionError('invalid price request accepted')
print('PASS original price/catalog:',counts,'; long repairs, negative insertion, binary costs, disabled producers')
