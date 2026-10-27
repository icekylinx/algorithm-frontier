"""Original subset inequalities and all-order closure checks.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from itertools import product
from pathlib import Path
from fractions import Fraction as F
from dataclasses import replace
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
from absorption import Absorption,RankTable,eligibility


def base_vectors(table):
    n=len(table).bit_length()-1
    return tuple(x for x in product(*(range(table[1<<p]+1) for p in range(n)))
                 if sum(x)==table[-1] and all(sum(x[p] for p in range(n) if s>>p&1)<=v
                                             for s,v in enumerate(table)))


def schedules(tables):
    n=len(tables[0]).bit_length()-1
    return tuple(tuple(tuple(column[p] for column in columns) for p in range(n))
                 for columns in product(*(base_vectors(f) for f in tables)))


def load(rows,sizes):
    return max((sum(v*s for v,s in zip(row,sizes)) for row in rows),default=F(0))


def terminals(tables,sizes,threshold):
    n=len(tables[0]).bit_length()-1
    seen={0};todo=[0];ends=set()
    while todo:
        mask=todo.pop();nexts=[]
        for p in range(n):
            if not mask>>p&1:
                marginal=sum(s*(f[mask|1<<p]-f[mask]) for f,s in zip(tables,sizes))
                if marginal<=threshold:nexts.append(mask|1<<p)
        if not nexts:ends.add(mask)
        for nxt in nexts:
            if nxt not in seen:seen.add(nxt);todo.append(nxt)
    return ends,len(seen)


fixtures=[]
for n in range(1,4):
    for caps in product(range(3),repeat=n):
        total=sum(caps)
        for rank in sorted({0,total//2,total}):
            first=tuple(min(rank,sum(c for p,c in enumerate(caps) if s>>p&1)) for s in range(1<<n))
            second=tuple(min(1,s.bit_count()) for s in range(1<<n))
            fixtures.append(((first,second),(F(3,2),F(1,3)),(0,)))
fixtures.extend([
    (((0,1,1,1),(0,1,1,1)),(F(1),F(3)),(0,1)),
    (((0,2,0,2),(0,0,1,1)),(F(5,3),F(7,3)),(0,1)),
    (((0,1,1,1,1,1,1,1),(0,0,1,1,1,1,1,1),(0,1,1,2,1,2,2,2)),
     (F(3),F(4),F(1)),(0,1)),
])
fixtures.append((((0,),),(F(1),),(0,)))
counts=dict(instances=0,closures=0,reachable_sets=0,budgets=0,dominated=0,lifts=0,rejections=0,collision=0,boolean_ranks=0)
for tables,sizes,large in fixtures:
    original=schedules(tables)
    engine=Absorption(tuple(RankTable(len(f).bit_length()-1,f) for f in tables),sizes,large)
    n=engine.n
    data=eligibility(engine)
    possible_collisions=[]
    for rows in original:
        for row in rows:
            sizes_here=sorted(size for j,size in enumerate(sizes) if j in large for _ in range(row[j]))
            if len(sizes_here)>1:possible_collisions.append(sum(sizes_here[:2]))
    assert data.collision==min(possible_collisions,default=None)
    for mask,rank in enumerate(data.large_recipients.values):
        optimum=0
        # Native feasible large assignments may leave capacity unused.
        for rows in original:
            supported=sum(1<<p for p,row in enumerate(rows) if mask>>p&1 and sum(row[j] for j in large)>0)
            optimum=max(optimum,supported.bit_count())
        assert rank==optimum
        counts['boolean_ranks']+=1
    if data.large_recipients.values[-1]<engine.residual[0]:assert data.collision is not None
    counts['collision']+=1
    thresholds={F(0)}
    for mask in range(1<<n):
        for p in range(n):
            if not mask>>p&1:
                thresholds.add(sum(s*(f[mask|1<<p]-f[mask]) for f,s in zip(tables,sizes)))
    thresholds=sorted(thresholds)
    closures={}
    for threshold in thresholds:
        closure=engine.closure(threshold)
        ends,visited=terminals(tables,sizes,threshold)
        removed=sum(1<<p for p in closure.removed)
        assert ends=={removed}
        assert load(closure.committed,sizes)<=threshold
        expected=tuple(tuple(f[removed|sum(1<<p for i,p in enumerate(closure.remaining) if s>>i&1)]-f[removed]
                             for s in range(1<<len(closure.remaining))) for f in tables)
        assert tuple(f.values for f in closure.ranks)==expected
        residual=schedules(expected)
        assert min(load(rows,sizes) for rows in residual)<=min(load(rows,sizes) for rows in original)
        for rows in original:
            h=engine.dominated(closure,rows)
            assert h in residual
            assert all(v<=rows[p][j] for i,p in enumerate(closure.remaining) for j,v in enumerate(h[i]))
            counts['dominated']+=1
        for rows in residual:
            lifted=engine.lift(closure,rows)
            assert lifted in original
            assert load(lifted,sizes)<=max(threshold,load(rows,sizes))
            counts['lifts']+=1
        closures[threshold]=closure
        counts['closures']+=1;counts['reachable_sets']+=visited
    for budget in range(engine.residual[0]+2):
        result=engine.for_budget(budget)
        expected=min(t for t,c in closures.items() if c.residual_large<=budget)
        assert result==closures[expected]
        counts['budgets']+=1
    counts['instances']+=1
# Decreasing raw marginals require extending a bottleneck plateau.
plateau=Absorption((RankTable(2,(0,2,2,2)),),(1,),(0,))
assert plateau.loads==(2,0) and plateau.for_budget(1).removed==(0,1)
zero=Absorption((RankTable(2,(0,0,2,2)),),(1,),(0,))
assert zero.for_budget(2).removed==(0,)
# Huge encoded capacities do not become loops or explicit job-copy arrays.
huge=10**100
big=Absorption((RankTable(2,(0,huge,huge,huge)),),(F(1,3),),(0,))
assert big.for_budget(huge-1).residual_large==0
assert eligibility(big).collision==F(2,3)
c=big.closure(0)
assert big.dominated(c,((huge,),(0,)))==((huge,),(0,))
assert big.lift(big.for_budget(0),())==((huge,),(0,))
bad=[lambda:big.closure(-1),lambda:big.for_budget(-1),lambda:big.for_budget(True),
     lambda:big.dominated(c,((huge,),(huge,))),
     lambda:big.lift(replace(c,residual_large=0),((huge,),(0,))),
     lambda:Absorption((RankTable(1,(0,1)),),(0,),(0,)),
     lambda:Absorption((RankTable(1,(0,1)),),(1,),(1,))]
for call in bad:
    try:call()
    except ValueError:counts['rejections']+=1
    else:raise AssertionError('malformed or forged input accepted')
print('PASS original-machine absorption:',counts,'; plateau, zero and100-digit guards')
