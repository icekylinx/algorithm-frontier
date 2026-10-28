"""Compact constructive Pauli stabilizer witness, with exact scalar terms.
Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro. Apache-2.0.
The reduction is polynomial; minimization enumerates the effective parity rank.
"""
from dataclasses import dataclass
from fractions import Fraction as F


@dataclass(frozen=True)
class Pauli:
    x: int
    z: int
    sign: int = 0

    @property
    def phase(self):
        return ((self.x & self.z).bit_count()+2*self.sign)%4


def validate(n, clauses):
    if type(n) is not int or n<0:raise ValueError('nonnegative qubit count required')
    out=[]
    for weight,p in clauses:
        if type(weight) not in (int,F) or weight<=0:raise ValueError('positive exact rational weight required')
        if not isinstance(p,Pauli) or type(p.x) is not int or type(p.z) is not int or type(p.sign) is not int:
            raise ValueError('compact Hermitian Pauli required')
        if min(p.x,p.z)<0 or max(p.x,p.z).bit_length()>n or p.sign not in (0,1):
            raise ValueError('Pauli label or sign outside original dimension')
        out.append((F(weight),p))
    return tuple(out)


def commutes(p,q):
    return ((p.x&q.z).bit_count()+(p.z&q.x).bit_count())%2==0


def label(p,n):return p.x|(p.z<<n)


def coordinates(v, basis):
    echelon={}
    for j,row in enumerate(basis):
        mask=1<<j
        while row:
            k=row.bit_length()-1
            if k not in echelon:
                echelon[k]=(row,mask);break
            a,b=echelon[k];row^=a;mask^=b
        else:raise ValueError('independent basis required')
    mask=0
    while v:
        k=v.bit_length()-1
        if k not in echelon:return None
        a,b=echelon[k];v^=a;mask^=b
    return mask


def kernel(rows,width):
    echelon={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k not in echelon:echelon[k]=row;break
            row^=echelon[k]
    result=[]
    for free in range(width):
        if free in echelon:continue
        vector=1<<free
        for k in sorted(echelon):
            if (echelon[k]&vector).bit_count()%2:vector^=1<<k
        result.append(vector)
    return result


def extend(n, initial):
    basis=[]
    for v in initial:
        if coordinates(v,basis) is None:basis.append(v)
    low=(1<<n)-1
    while len(basis)<n:
        constraints=[((v&low)<<n)|(v>>n) for v in basis]
        v=next(v for v in kernel(constraints,2*n) if coordinates(v,basis) is None)
        basis.append(v)
    return tuple(Pauli(v&low,v>>n) for v in basis)


def product(generators,mask):
    x=z=phase=0
    for j,q in enumerate(generators):
        if mask>>j&1:
            phase=(phase+q.phase+2*(z&q.x).bit_count())%4
            x^=q.x;z^=q.z
    return x,z,phase


@dataclass(frozen=True)
class Surrogate:
    n: int
    generators: tuple
    scalar: F
    terms: tuple
    residual: tuple
    pairs: tuple

    def energy(self,assignment):
        if type(assignment) is not int or assignment<0 or assignment.bit_length()>self.n:
            raise ValueError('assignment outside complete stabilizer basis')
        return self.scalar+sum(2*w*((sign+(mask&assignment).bit_count())%2) for w,sign,mask in self.terms)


def reduce_hamiltonian(n,clauses):
    clauses=validate(n,clauses)
    residual=[w for w,p in clauses]
    pairs=[]
    while True:
        pair=next(((i,j) for i in range(len(clauses)) if residual[i]
                   for j in range(i+1,len(clauses)) if residual[j]
                   and not commutes(clauses[i][1],clauses[j][1])),None)
        if pair is None:break
        i,j=pair;amount=min(residual[i],residual[j])
        residual[i]-=amount;residual[j]-=amount;pairs.append((i,j,amount))
    generators=extend(n,[label(p,n) for a,(w,p) in zip(residual,clauses) if a])
    basis=[label(p,n) for p in generators]
    scalar=F(0);terms=[]
    for w,p in clauses:
        mask=coordinates(label(p,n),basis)
        if mask is None:scalar+=w;continue
        x,z,phase=product(generators,mask)
        difference=(p.phase-phase)%4
        if difference%2:raise RuntimeError('commuting Hermitian phase mismatch')
        terms.append((w,difference//2,mask))
    return Surrogate(n,generators,scalar,tuple(terms),tuple(residual),tuple(pairs))


def assignment_for(rows,values):
    echelon={}
    for j,row in enumerate(rows):
        rhs=values>>j&1
        while row:
            k=row.bit_length()-1
            if k not in echelon:echelon[k]=(row,rhs);break
            a,b=echelon[k];row^=a;rhs^=b
        else:raise ValueError('independent parity rows required')
    assignment=0
    for k in sorted(echelon):
        row,rhs=echelon[k]
        if ((row&assignment).bit_count()+rhs)%2:assignment^=1<<k
    return assignment


@dataclass(frozen=True)
class Witness:
    generators: tuple
    energy: F
    parity_rank: int


def minimize(surrogate):
    rows=[]
    for w,sign,mask in surrogate.terms:
        if coordinates(mask,rows) is None:rows.append(mask)
    best=None;best_assignment=0
    for values in range(1<<len(rows)):
        assignment=assignment_for(rows,values)
        energy=surrogate.energy(assignment)
        if best is None or energy<best:best,best_assignment=energy,assignment
    generators=tuple(Pauli(p.x,p.z,p.sign^(best_assignment>>j&1)) for j,p in enumerate(surrogate.generators))
    return Witness(generators,best,len(rows))
