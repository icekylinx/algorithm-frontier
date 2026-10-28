"""Independent bottleneck-basis and scalar piecewise-envelope comparisons.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'reference'))
from absorption import RankTable,position_commitment,padding_scale


def binary_rank(vectors):
    pivots={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in pivots:v^=pivots[p]
            else:pivots[p]=v;break
    return len(pivots)


def overhead(pairs,d,x):
    return max(a-max(F(0),min(x/d,lo-(1-1/d)*x)) for lo,a in pairs)


def independent_padding(pairs,d):
    if d==1:
        return overhead(pairs,d,max(lo for lo,_ in pairs))
    breaks=sorted({F(0),*(lo for lo,_ in pairs),*(d*lo/(d-1) for lo,_ in pairs)})
    values=[overhead(pairs,d,x) for x in breaks]
    # Each original machine has one affine overhead on each such interval.
    # Every minimum of their upper envelope occurs at an endpoint or crossing.
    for left,right in zip(breaks,breaks[1:]):
        first=(2*left+right)/3;second=(left+2*right)/3
        lines=[]
        for pair in pairs:
            y1=overhead((pair,),d,first);y2=overhead((pair,),d,second)
            slope=(y2-y1)/(second-first)
            lines.append((slope,y1-slope*first))
        for (a,b),(c,e) in combinations(lines,2):
            if a!=c:
                x=(e-b)/(a-c)
                if left<=x<=right:values.append(overhead(pairs,d,x))
    return min(values)


fixtures={(0,)}
for n in range(1,5):
    for columns in product(range(4),repeat=n):
        fixtures.add(tuple(binary_rank(columns[p] for p in range(n) if s>>p&1) for s in range(1<<n)))
    for r in range(n+1):fixtures.add(tuple(min(r,s.bit_count()) for s in range(1<<n)))
counts=dict(matroids=0,commitments=0,original_bases=0,completions=0,padding=0,strict_improvements=0,rejections=0)
for f in sorted(fixtures,key=lambda x:(len(x),x)):
    n=len(f).bit_length()-1;table=RankTable(n,f)
    bases=[s for s in range(1<<n) if s.bit_count()==f[-1] and f[s]==f[-1]]
    for weights in [tuple(F(p,3) for p in range(n)),tuple(F(n-p,2) for p in range(n)),(F(1),)*n]:
        for k in range(f[-1]+1):
            result=position_commitment(table,weights,k)
            removed=sum(1<<p for p in result.committed)
            possible=[s for s in range(1<<n) if s.bit_count()==f[-1]-k and f[s]==s.bit_count()]
            optimum=min(max((weights[p] for p in range(n) if s>>p&1),default=F(0)) for s in possible)
            assert result.bottleneck==optimum and len(result.committed)==f[-1]-k
            assert result.rank.values[-1]==k
            for basis in bases:
                image=sum(1<<i for i,p in enumerate(result.remaining) if basis>>p&1)
                assert result.rank.values[image]==k
                counts['original_bases']+=1
            for s,v in enumerate(result.rank.values):
                if s.bit_count()==k and v==k:
                    combined=removed|sum(1<<p for i,p in enumerate(result.remaining) if s>>i&1)
                    assert combined in bases
                    counts['completions']+=1
            counts['commitments']+=1
    counts['matroids']+=1
pool=[(F(lo,2),F(hi,2)) for lo in range(1,5) for hi in range(lo,6)]
for pairs in [*(tuple([p]) for p in pool),*combinations(pool,2),*combinations(pool[:7],3)]:
    for d in [F(1),F(3,2),F(2),F(3),F(4)]:
        cost,scale=padding_scale(pairs,d)
        maximum=max(a for _,a in pairs);width=max(a-lo for lo,a in pairs)
        assert scale>0 and cost==overhead(pairs,d,scale)==independent_padding(pairs,d)
        simple=maximum-(maximum-width)/d
        assert cost<=simple
        counts['strict_improvements']+=int(cost<simple)
        counts['padding']+=1
# A boundary at which the formerly limiting machine drops out of the active set.
pairs=((F(1,10),F(1)),(F(2),F(2)))
assert padding_scale(pairs,2)==(F(1),F(2))
bad=[lambda:position_commitment(RankTable(1,(0,2)),(1,),0),
     lambda:position_commitment(RankTable(1,(0,1)),(1,),2),
     lambda:position_commitment(RankTable(1,(0,1)),(-1,),0),
     lambda:padding_scale((),2),lambda:padding_scale(((0,1),),2),
     lambda:padding_scale(((1,1),),F(1,2))]
for call in bad:
    try:call()
    except ValueError:counts['rejections']+=1
    else:raise AssertionError('malformed profile accepted')
assert counts['strict_improvements']
print('PASS exact commitment profiles:',counts,'; strict-active-set endpoint')
