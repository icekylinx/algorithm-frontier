#!/usr/bin/env python3
"""Original-input failure/prefix checks for the general incidence constructor.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import importlib.util
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
import incidence as backend


def rank(rows,modulus=None):
    a=[[F(x) if modulus is None else int(x)%modulus for x in row] for row in rows]
    if not a:return 0
    out=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(out,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[out],a[pivot]=a[pivot],a[out]
        factor=1/a[out][j] if modulus is None else pow(a[out][j],-1,modulus)
        a[out]=[x*factor if modulus is None else x*factor%modulus for x in a[out]]
        for i in range(out+1,len(a)):
            z=a[i][j]
            a[i]=[x-z*y if modulus is None else (x-z*y)%modulus for x,y in zip(a[i],a[out])]
        out+=1
        if out==len(a):break
    return out


counts={'matrices':0,'prefixes':0,'simplicial':0,'invalid':0}
def compare(rows,rl,cl,h,order,modulus=None):
    result=backend.incidence_summary(rows,rl,cl,h,modulus,order)
    kept=set(result['retained'])
    assert len(kept)==result['rank']<=min(len(cl),result['formal_rows'])
    assert result['original_rank']==rank(rows,modulus)
    labels=sorted(set().union(*cl,*rl))
    for size in range(min(h,len(labels))+1):
        for failed in combinations(labels,size):
            surviving=[]
            for e in order:
                if set(cl[e]).isdisjoint(failed):surviving.append(e)
                full=[[row[j] for j in surviving] for row in rows]
                small=[[row[j] for j in surviving if j in kept] for row in rows]
                assert rank(full,modulus)==rank(small,modulus),(rows,failed,e,result)
                counts['prefixes']+=1
    counts['matrices']+=1
    return result


rng=random.Random(6107)
for modulus in (None,7):
    for trial in range(160):
        m=rng.randrange(5);n=rng.randrange(7)
        rl=[set(i for i in range(3) if rng.randrange(2)) for _ in range(m)]
        cl=[set(i for i in range(3) if rng.randrange(2)) for _ in range(n)]
        rows=[[rng.choice((-2,-1,0,1,2)) if rl[i]<=cl[e] else 0 for e in range(n)] for i in range(m)]
        order=list(range(n));rng.shuffle(order)
        compare(rows,rl,cl,trial%4,order,modulus)
# Each field's zero incidence is checked after reduction.
compare([[7,0],[0,1]],[{0},set()],[set(),{1}],2,[1,0],7)
# Shared row labels need not be bounded by the incidence increment.
common=set(range(70))
result=compare([[1,1,1]],[common],[common|{70},common|{71},common|{72}],1,[2,0,1])
assert result['increment']==1 and len(result['retained'])==2
# Huge binary failure budget must never create a degree-sized iterator.
result=backend.incidence_summary([[1,1,1]],[set()],[{0},{1},{2}],10**100)
assert len(result['retained'])==3 and result['candidates']<30
# Original dependent-row labels must not be attached to linear combinations.
compare([[1,0,1],[0,1,1],[1,1,2]],[{0},set(),set()],[{0},{1},{0,1}],1,[0,1,2])
for modulus in (None,7):
    simplices=list(combinations(range(5),3))
    for trial in range(25):
        selected=[s for s in simplices if rng.randrange(2)]
        vl=[{j for j in range(3) if rng.randrange(3)==0} for _ in range(5)]
        tl=[{j for j in range(3) if rng.randrange(3)==0} for _ in selected]
        order=list(range(len(selected)));rng.shuffle(order)
        result=backend.labeled_persistence_summary(5,selected,vl,tl,1,modulus,order)
        # Independently derive original oriented boundary and all label sets.
        faces=sorted(set(face for s in selected for face in combinations(s,2)))
        rows=[]
        for face in faces:
            row=[]
            for s in selected:
                value=0
                for j in range(3):
                    if s[:j]+s[j+1:]==face:value=(-1)**j
                row.append(value)
            rows.append(row)
        rl=[set().union(*(vl[v] for v in f)) for f in faces]
        cl=[set(tl[e]).union(*(vl[v] for v in s)) for e,s in enumerate(selected)]
        checked=compare(rows,rl,cl,1,order,modulus)
        assert result['retained']==checked['retained']
        counts['simplicial']+=1
# Sharp general coefficient: each failure isolates one independent cone.
from math import comb
for p,a,b,h in [(1,1,0,1),(1,0,1,2),(1,1,1,1),(2,1,0,1),(2,0,1,1),(2,1,1,1)]:
    t=p+2
    subsets=list(combinations(range(a+b+h),a+b))
    vl=[set() for _ in range(t)]+[set(s[:a]) for s in subsets]
    tops=[];extra=[]
    for j,labels in enumerate(subsets):
        for base in combinations(range(t),p):
            tops.append(tuple(base)+(t+j,));extra.append(set(labels[a:]))
    result=backend.labeled_persistence_summary(t+len(subsets),tops,vl,extra,h)
    assert len(result['retained'])==len(tops)==len(subsets)*comb(t,p)
    assert result['original_rank']==comb(t,p)+(len(subsets)-1)*comb(t-1,p-1)
    counts['simplicial']+=1
for args in [([[1]],[{0}],[set()],1),([[1,2]],[set()],[set()],1),([[1]],[set()],[set()],-1),([[1]],[set()],[set()],True),([[1]],[],[set()],1),([[1]],[set()],[{'x'}],1)]:
    try:backend.incidence_summary(*args)
    except ValueError:counts['invalid']+=1
    else:raise AssertionError('invalid incidence accepted')
print('PASS original incidence/persistence:',counts,'; huge binary degree, shared labels, exact original rows')
