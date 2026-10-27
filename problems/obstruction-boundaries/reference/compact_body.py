"""Exact Max-Cut reduction and independently checkable compact-body violations.

The exhaustive separator is exponential in the number of used coordinates.
Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product


def exact(x):
    return type(x) in (int,F)


@dataclass(frozen=True)
class Body:
    dimension: int
    checks: tuple
    weights: tuple
    point: tuple
    accuracy: F = F(1,4)

    def __post_init__(self):
        rows=tuple(tuple(row) for row in self.checks)
        weights,point=tuple(self.weights),tuple(self.point)
        n=self.dimension
        if type(n) is not int or n<0:
            raise ValueError('nonnegative integer dimension required')
        if len(rows)!=len(weights) or len(rows)!=len(point):
            raise ValueError('item dimensions differ')
        if any(any(type(v) is not int or not 0<=v<n for v in row) or len(set(row))!=len(row) for row in rows):
            raise ValueError('checks require distinct original variable IDs')
        if (any(not exact(w) or w<=0 for w in weights) or any(not exact(z) for z in point)
                or not exact(self.accuracy) or not 0<self.accuracy<=F(1,2)):
            raise ValueError('exact weights, point and accuracy required')
        object.__setattr__(self,'checks',rows)
        object.__setattr__(self,'weights',tuple(map(F,weights)))
        object.__setattr__(self,'point',tuple(map(F,point)))
        object.__setattr__(self,'accuracy',F(self.accuracy))


def evaluate(body,assignment):
    assignment=tuple(assignment)
    if (len(assignment)!=body.dimension or any(type(v) is not int or v not in (0,1) for v in assignment)):
        raise ValueError('original binary assignment required')
    value,weight=F(0),F(0)
    for row,w,z in zip(body.checks,body.weights,body.point):
        if sum(assignment[v] for v in row)%2:
            value+=w*z; weight+=w
    return value,weight


@dataclass(frozen=True)
class QueryViolation:
    assignment: tuple[int,...]


@dataclass(frozen=True)
class SparseQueryViolation:
    ones: tuple[int,...]


@dataclass(frozen=True)
class CubeViolation:
    coordinate: int


def verify_violation(body,witness):
    """Search-free exact nonmembership check; no Max-Cut call."""
    try:
        if type(body) is not Body:
            return False
        if type(witness) is CubeViolation:
            i=witness.coordinate
            return type(i) is int and 0<=i<len(body.point) and abs(body.point[i])>1
        if type(witness) is SparseQueryViolation:
            ones=witness.ones
            if (type(ones) is not tuple or any(type(v) is not int or not 0<=v<body.dimension for v in ones)
                    or len(set(ones))!=len(ones)):
                return False
            chosen=set(ones)
            value,weight=F(0),F(0)
            for row,w,z in zip(body.checks,body.weights,body.point):
                if sum(v in chosen for v in row)%2:
                    value+=w*z; weight+=w
            return abs(value)>body.accuracy*weight
        if type(witness) is QueryViolation and type(witness.assignment) is tuple:
            value,weight=evaluate(body,witness.assignment)
            return abs(value)>body.accuracy*weight
        return False
    except (ValueError,TypeError,AttributeError,IndexError):
        return False


def separate(body):
    """Exhaustively return a violated cube/query constraint, or None.

    Exact and polynomial-space, exponential in the number of used variables.
    """
    if type(body) is not Body:
        raise ValueError('validated Body required')
    for i,z in enumerate(body.point):
        if abs(z)>1:
            return CubeViolation(i)
    active=tuple(sorted({v for row in body.checks for v in row}))
    if not active:
        return None
    for bits in product((0,1),repeat=len(active)):
        witness=SparseQueryViolation(tuple(v for v,bit in zip(active,bits) if bit))
        if verify_violation(body,witness):
            return witness
    return None


def reduce_maxcut(n,edges,threshold):
    """Construct z in Q_(1/4) iff maximum nonnegative integer cut <= threshold.

    Parallel edge records remain separate items; zero terms are omitted.
    Even empty/all-zero graphs and negative thresholds are handled exactly.
    """
    if type(n) is not int or n<0 or type(threshold) is not int:
        raise ValueError('integer graph size and threshold required')
    edges=tuple(tuple(edge) for edge in edges)
    degree=[0]*n
    for edge in edges:
        if len(edge)!=3:
            raise ValueError('edge is (u,v,integer weight)')
        u,v,w=edge
        if (type(u) is not int or type(v) is not int or not 0<=u<n or not 0<=v<n
                or u==v or type(w) is not int or w<0):
            raise ValueError('invalid loopless weighted edge')
        degree[u]+=w; degree[v]+=w
    maximum=max(degree,default=0)
    signed=[((u,v),F(w)) for u,v,w in edges]
    signed.extend((row,-F(maximum,2)) for v in range(n) for row in ((v,),(v,n)))
    signed.append(((n,),F(maximum*n,2)-threshold))
    signed=[(row,c) for row,c in signed if c]
    return Body(n+1,tuple(row for row,_ in signed),tuple(4*abs(c) for _,c in signed),
                tuple(F(1,2) if c>0 else F(0) for _,c in signed))


def recover_cut(n,edges,threshold,witness):
    """Translate a checked reduction query back to an original cut > threshold."""
    body=reduce_maxcut(n,edges,threshold)
    if not verify_violation(body,witness):
        raise ValueError('valid reduction witness required')
    if type(witness) is QueryViolation and witness.assignment[-1]==1:
        return tuple(v for v,bit in enumerate(witness.assignment[:-1]) if bit)
    if type(witness) is SparseQueryViolation and n in witness.ones:
        return tuple(sorted(v for v in witness.ones if v!=n))
    raise ValueError('homogenizing-one query witness required')
