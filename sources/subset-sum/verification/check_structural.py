#!/usr/bin/env python3
"""Focused exact checks for ownership, linear covers and elementary layouts."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

if not __debug__:
    raise SystemExit('Run with assertions enabled.')

counts={}
def count(name,n=1): counts[name]=counts.get(name,0)+n
def choose(n,k): return comb(n,k) if 0<=k<=n else 0
def canonical(weights):
    out={}
    for x in range(1<<len(weights)):
        w=sum(v for i,v in enumerate(weights) if (x>>i)&1)
        out.setdefault(w,x)
    return list(out.values())
def trace(s,h,canon,a,u,v):
    allmask=(1<<a)-1
    return sum(((x^s)&(allmask^h)).bit_count()==u and
               ((x^s)&h).bit_count()==h.bit_count()-v for x in canon)
def cover_case(weights,b,u,v):
    a=len(weights); canon=canonical(weights); N=len(canon)
    j=b+u-v; Q=comb(a-b,u)*comb(b,v)
    owners=[h for h in range(1<<a) if h.bit_count()==b]
    values={(s,h):trace(s,h,canon,a,u,v) for s in range(1<<a) for h in owners}
    nj={s:sum((x^s).bit_count()==j for x in canon) for s in range(1<<a)}
    for s in range(1<<a):
        assert sum(values[s,h] for h in owners)*comb(a,j)==nj[s]*Q*len(owners)
        assert all(0<=values[s,h]<=Q for h in owners)
        count('association_pattern_checks')
    # Every fixed-owner trace is a lower bound on the actual distinct signed image.
    for s in range(1<<a):
        for h in owners:
            image={sum((-w if ((s^h)>>i)&1 else w)
                       for i,w in enumerate(weights) if (r>>i)&1)
                   for r in range(1<<a)
                   if (r&(((1<<a)-1)^h)).bit_count()==u and (r&h).bit_count()==v}
            assert len(image)>=values[s,h]
            count('actual_image_checks')
    C0=2*(a+1); M=F(N*Q,C0*comb(a,j)); L=Q.bit_length()
    eligible={s for s in range(1<<a) if C0*nj[s]>=N}
    if not eligible:return
    U=set(eligible); selected=[]
    while U:
        hs=owners
        for i in range(a):
            children=[[h for h in hs if (h>>i)&1==bit] for bit in (0,1)]
            children=[c for c in children if c]
            hs=max(children,key=lambda c:F(sum(values[s,h] for s in U for h in c),len(c)))
        assert len(hs)==1
        h=hs[0]
        assert sum(values[s,h] for s in U)>=M*len(U)
        ell=max(range(L),key=lambda ell:(1<<ell)*sum(values[s,h]>=1<<ell for s in U))
        rem={s for s in U if values[s,h]>=1<<ell}
        assert (1<<ell)*len(rem)>=M*len(U)/L
        selected.append((h,ell)); U-=rem
    harmonic=sum((F(1,i) for i in range(1,len(eligible)+1)),F())
    weight=sum((F(1,1<<ell) for h,ell in selected),F())
    assert weight<=L*harmonic/M
    for ell in range(L):
        k=sum(e==ell for _,e in selected)
        assert F(k*Q,1<<ell)<=Q*L*harmonic/M
    count('weighted_owner_cover_cases')
    count('weighted_owner_pairs',len(selected))

for weights in ([0,0,0,0],[-3,-1,1,3],[1,1,2,2],[1,2,4,8],[-2,0,2,3,7]):
    a=len(weights)
    for b in range(a+1):
        for u in range(a-b+1):
            for v in range(b+1):
                cover_case(weights,b,u,v)

# Prefix completion kernel, including empty and infeasible completions.
a=6; full=(1<<a)-1
for b,u,v in [(1,1,0),(2,1,1),(4,0,2),(5,1,3)]:
    j=b+u-v
    owners=[h for h in range(1<<a) if h.bit_count()==b]
    for depth in range(a+1):
        prefixmask=(1<<depth)-1; W=full^prefixmask
        for prefix in range(1<<depth):
            F1=prefix; F0=prefixmask^prefix
            for Y in range(1<<a):
                z1=(Y&F1).bit_count(); zw=(Y&W).bit_count()
                predicted=0
                if Y.bit_count()==j:
                    predicted=choose(zw,b-v-z1)*choose(W.bit_count()-zw,b-F1.bit_count()-(b-v-z1))
                actual=sum((h&prefixmask)==prefix and
                           (Y&(full^h)).bit_count()==u and
                           (Y&h).bit_count()==b-v for h in owners)
                assert predicted==actual
                count('prefix_completion_checks')

# Every nonempty subset of F_2^3: exact prefix-conditional linear cover.
for Gbits in range(1,1<<8):
    c=3; N=1<<c; G={x for x in range(N) if (Gbits>>x)&1}
    H={0}
    while True:
        U={x for x in range(N) if not any((x^h) in G for h in H)}
        if not U:break
        prefix=0
        for depth in range(1,c+1):
            mask=(1<<depth)-1
            totals=[]
            for p in (prefix,prefix|(1<<(depth-1))):
                buckets=[sum((x&mask)==a for x in U) for a in range(1<<depth)]
                totals.append((sum(buckets[a]*buckets[a^p] for a in range(1<<depth)),p))
            _,prefix=min(totals)
        newU=U&{x^prefix for x in U}
        assert len(newU)*N<=len(U)**2
        assert prefix not in H
        H=H|{h^prefix for h in H}
        count('linear_cover_doublings')
    assert len(H)<=min(N,F(2*(1+c)*N,len(G)))
    count('linear_cover_sets')

# Construct balanced q=4 layouts by recursive cyclic halves for every support.
def balanced_split(coords,R,q):
    if q==1:return [coords]
    target=sum(x in R for x in coords)//2; half=len(coords)//2
    for shift in range(len(coords)):
        left=coords[shift:]+coords[:shift]; left=left[:half]
        if sum(x in R for x in left)==target:
            leftset=set(left); right=[x for x in coords if x not in leftset]
            return balanced_split(left,R,q//2)+balanced_split(right,R,q//2)
    raise AssertionError('cyclic split missing')
for b in range(4,13):
    for mask in range(1<<b):
        R={i for i in range(b) if (mask>>i)&1}
        yes=sorted(R); no=[i for i in range(b) if i not in R]
        T=set(yes[:len(yes)%4]+no[:len(no)%4])
        assert len(T)<=6
        coords=[i for i in range(b) if i not in T]
        if not coords: continue
        parts=balanced_split(coords,R,4)
        assert len(parts)==4 and len({len(p) for p in parts})==1
        assert len({sum(i in R for i in p) for p in parts})==1
        assert set().union(*(set(p) for p in parts))==set(coords)
        count('cyclic_layout_supports')

# Rational entropy enclosures and active parameter inequalities.
Lminus=2*sum((F(1,(2*j+1)*3**(2*j+1)) for j in range(20)),F())
Lplus=Lminus+F(2,41*3**41)*F(9,8)
def entropy(p,n=256):
    z=abs(1-2*p)
    S=sum((z**(2*j)/((2*j)*(2*j-1)) for j in range(1,n+1)),F())
    tail=z**(2*n+2)/((2*n+2)*(2*n+1)*(1-z*z))
    return 1-(S+tail)/Lminus,1-S/Lplus
hpL,hpU=entropy(F(1,20)); h56L,h56U=entropy(F(14,25),32)
assert hpL>F(28639695,10**8) and hpU<F(28639696,10**8)
assert 1-h56L<F(11,1000)
assert Lplus<F(52,75) and Lminus>F(56,81)
assert hpU-F(3,20)<F(7,50)
assert (2*F(1,15)/(F(1,2)+F(1,15)))*(F(7,50)/F(1,20))==F(56,85)
assert F(9,64)*F(56,85)==F(63,680)
assert F(63,680)/F(1,2)<F(1,2)
assert (2+F(3,4)*F(56,85))*F(1,20)==F(53,425)<1
assert F(9)*F(7,50)**2/(32*F(1,20)*F(9,10)**2)==F(49,360)<F(3,8)
assert F(2)*F(3,50)**2/F(52,75)==F(27,2600)>F(17,2000)
rho=F(9,10); p=F(1,20); z=F(1,15)
assert rho*2*z*(1-hpL-p)<F(8,100)<1-rho
assert rho*(2*z*(1-p)-p)==F(69,1000)<1-rho
assert rho*(hpU+F(3,4)*F(11,1000))<F(265185,10**6)
assert F(3,4)*rho*(F(1,2)+z)==F(153,400)
assert F(3,2)*rho+2*rho*F(17,2000)==F(13653,10000)
count('rational_parameter_checks',17)
receipt={'status':'PASS','counts':counts,'entropy_h_005_enclosure':['.28639695','.28639696'],
         'runtime_scope':'Small exhaustive combinatorial checks and exact rational certificates; no previous profile replay.'}
Path(__file__).with_name('structural_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
