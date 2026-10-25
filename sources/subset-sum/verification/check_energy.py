"""Finite exact checks of the one-canonical energy tensor identity.

These tests compare the pruned rank-three contractions with independent
binary endpoint enumeration. They are not an asymptotic proof or solver.
"""
from itertools import product
from pathlib import Path
import json
import random


def contract(data, matrix, axis, keep):
    result={}
    for key,value in data.items():
        for row,coeffs in enumerate(matrix):
            coeff=coeffs[key[axis]]
            if not coeff:
                continue
            target=key[:axis]+(row,)+key[axis+1:]
            if keep(target):
                result[target]=result.get(target,0)+coeff*value
    return {key:value for key,value in result.items() if value}


def check(n,k,canonical,weights,modulus,values,offset):
    x,y,xp,yp=values
    local=(
        ((x*xp,1),(1,y*yp)),
        ((0,xp),(0,y)),
        ((x,0),(yp,0)),
    )
    determinant=xp*(x*y-1)
    assert determinant
    h=x*xp*y*yp-1
    v=y*(1-xp*yp)
    P=((h,determinant,0),(1,0,0),(0,0,determinant))
    U=((xp,x*xp,x),(y,1,yp))
    V=((0,1),(determinant,v),(1,0))
    for delta,c,b in product(range(3),range(2),range(2)):
        assert determinant*local[delta][c][b]==sum(P[j][delta]*U[c][j]*V[j][b] for j in range(3))
    alphabet=(0,1,-1)
    f={}
    for key in product(range(3),repeat=n):
        delta=tuple(alphabet[j] for j in key)
        if sum(d==1 for d in delta)!=sum(d==-1 for d in delta) or sum(d==-1 for d in delta)>k:
            continue
        numeric=offset+sum(a*d for a,d in zip(weights,delta))
        if numeric and numeric%modulus==0:
            f[key]=1
    transformed=f
    for axis in range(n):
        transformed=contract(transformed,P,axis,lambda key,axis=axis:sum(t==2 for t in key)<=k)
    ahat={b:1 for b in canonical}
    for axis in range(n):
        ahat=contract(ahat,V,axis,lambda key,axis=axis:sum(t==2 for t in key[:axis+1])<=k)
    joined={key:value*ahat.get(key,0) for key,value in transformed.items()}
    for axis in range(n):
        joined=contract(joined,U,axis,lambda key:True)
    binary=tuple(product(range(2),repeat=n))
    for c in binary:
        direct=0
        for b in canonical:
            for bp in binary:
                delta=tuple(a-b for a,b in zip(b,bp))
                if delta.count(1)!=delta.count(-1) or delta.count(-1)>k:
                    continue
                numeric=offset+sum(a*d for a,d in zip(weights,delta))
                if not numeric or numeric%modulus:
                    continue
                contribution=1
                for i,d in enumerate(delta):
                    contribution*=local[alphabet.index(d)][c[i]][b[i]]
                direct+=contribution
        assert joined.get(c,0)==determinant**n*direct
    return len(binary)


rng=random.Random(20261023)
cases=outputs=0
for n in range(1,5):
    binary=tuple(product(range(2),repeat=n))
    canonical={b for b in binary if rng.randrange(3)}
    weights=(1,-2,1,0)[:n]
    for k,modulus,values,offset in product(range(min(n,2)+1),(1,2,5),((2,3,2,4),(3,2,1,2)),(0,3)):
        outputs+=check(n,k,canonical,weights,modulus,values,offset)
        cases+=1
receipt={'status':'PASS','cases':cases,'output_patterns':outputs,
         'scope':'Exact local rank-three identities and pruned contractions versus binary endpoint enumeration, including signed/repeated/zero weights, exact-zero exclusion and boundary offsets.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS:',cases,'energy cases;',outputs,'output comparisons')
