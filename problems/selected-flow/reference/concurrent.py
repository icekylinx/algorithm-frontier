"""Exact selected concurrent flow baseline. Attribution: Yilin Liu and GPT-6 Astra Pro.

Apache-2.0. No third-party packages. Bland simplex is not a polynomial-time
LP implementation; explicit selection enumeration is not the corank scheme.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


def rational(x):
    if type(x) not in (int, F):
        raise ValueError('use exact int or Fraction data')
    return F(x)


def simplex(a, b, c):
    """Max c*x, A*x <= b, x >= 0; requires b >= 0. Returns x, y."""
    n, m = len(c), len(b)
    if len(a) != m or any(len(row) != n for row in a):
        raise ValueError('LP dimensions')
    a = [[rational(x) for x in row] for row in a]
    b, c = [rational(x) for x in b], [rational(x) for x in c]
    if any(x < 0 for x in b):
        raise ValueError('origin must be feasible')
    tab = [row + [F(i == j) for j in range(m)] + [b[i]]
           for i, row in enumerate(a)]
    obj = [-x for x in c] + [F(0)] * (m + 1)
    basis = list(range(n, n + m))
    while True:
        entering = next((j for j in range(n + m) if obj[j] < 0), None)
        if entering is None:
            break
        candidates = [i for i in range(m) if tab[i][entering] > 0]
        if not candidates:
            raise ValueError('unbounded LP')
        leaving = min(candidates, key=lambda i: (tab[i][-1] / tab[i][entering], basis[i]))
        pivot = tab[leaving][entering]
        tab[leaving] = [x / pivot for x in tab[leaving]]
        for i in range(m):
            if i != leaving:
                mult = tab[i][entering]
                tab[i] = [x - mult*y for x, y in zip(tab[i], tab[leaving])]
        mult = obj[entering]
        obj = [x - mult*y for x, y in zip(obj, tab[leaving])]
        basis[leaving] = entering
    x = [F(0)] * n
    for i, j in enumerate(basis):
        if j < n:
            x[j] = tab[i][-1]
    return tuple(x), tuple(obj[n:n+m])


def verify_lp(a, b, c, x, y):
    """Search-free exact primal/dual optimality check."""
    try:
        if len(x) != len(c) or len(y) != len(b) or len(a) != len(b):
            return False
        if any(len(row) != len(c) for row in a):
            return False
        for value in [*b, *c, *x, *y, *(v for row in a for v in row)]:
            rational(value)
        dot = lambda u, v: sum((s*t for s, t in zip(u, v)), F(0))
        return (all(v >= 0 for v in (*x, *y))
                and all(dot(row, x) <= rhs for row, rhs in zip(a, b))
                and all(sum(y[i]*a[i][j] for i in range(len(b))) >= c[j]
                        for j in range(len(c)))
                and dot(c, x) == dot(b, y))
    except (ValueError, TypeError):
        return False


@dataclass(frozen=True)
class Network:
    vertices: int
    edges: tuple  # (tail, head, capacity), physical edge IDs are positions
    commodities: tuple  # (source, target, positive demand scale)
    undirected: bool = False

    def __post_init__(self):
        if type(self.vertices) is not int or self.vertices < 1 or type(self.undirected) is not bool:
            raise ValueError('network dimensions')
        edges, commodities = tuple(self.edges), tuple(self.commodities)
        for records, positive in ((edges, False), (commodities, True)):
            for u, v, value in records:
                if (type(u) is not int or type(v) is not int or not 0 <= u < self.vertices
                        or not 0 <= v < self.vertices or u == v):
                    raise ValueError('distinct valid endpoints required')
                value = rational(value)
                if value < 0 or (positive and value == 0):
                    raise ValueError('invalid capacity or demand')
        object.__setattr__(self, 'edges', tuple((u,v,rational(w)) for u,v,w in edges))
        object.__setattr__(self, 'commodities', tuple((u,v,rational(w)) for u,v,w in commodities))

    def arcs(self):
        return tuple((u,v,e) for e,(u,v,_) in enumerate(self.edges) for u,v in
                     (((u,v),(v,u)) if self.undirected else ((u,v),)))


def formulation(net, selected, budgets=(), setup=None):
    """Budget: (q by directed-arc charge matrix, cap).

    Optional setup: (q fees, q by directed-arc charges, shared cap).
    Returns A,b,c for rate first, then selected-commodity arc coordinates.
    None means this set's setup alone is unaffordable.
    """
    q, arcs = len(net.commodities), net.arcs()
    selected = tuple(selected)
    if not selected or any(type(i) is not int or not 0 <= i < q for i in selected) or len(set(selected)) != len(selected):
        raise ValueError('nonempty distinct selected commodity IDs required')
    rows = []
    for charges, cap in budgets:
        charges = tuple(tuple(rational(w) for w in row) for row in charges)
        cap = rational(cap)
        if len(charges) != q or any(len(row) != len(arcs) for row in charges) or cap < 0 or any(w < 0 for row in charges for w in row):
            raise ValueError('invalid routing budget')
        rows.append((charges, cap))
    residual = None
    if setup is not None:
        fees, charges, cap = setup
        fees = tuple(rational(w) for w in fees)
        charges = tuple(tuple(rational(w) for w in row) for row in charges)
        cap = rational(cap)
        if len(fees) != q or any(w < 0 for w in fees) or cap < 0 or len(charges) != q or any(len(row) != len(arcs) for row in charges) or any(w < 0 for row in charges for w in row):
            raise ValueError('invalid shared budget')
        residual = cap - sum(fees[i] for i in selected)
        if residual >= 0:
            rows.append((charges, residual))
    if residual is not None and residual < 0:
        return None
    n = 1 + len(selected)*len(arcs)
    a, b = [], []
    def add(row, rhs):
        a.append(tuple(row)); b.append(F(rhs))
    for k, i in enumerate(selected):
        s, t, demand = net.commodities[i]
        for v in range(net.vertices):
            row = [F(0)]*n
            row[0] = -demand*((v == s)-(v == t))
            for j,(u,w,_) in enumerate(arcs):
                row[1+k*len(arcs)+j] = F((u == v)-(w == v))
            add(row, 0); add([-x for x in row], 0)
    for e,(_,_,cap) in enumerate(net.edges):
        row = [F(0)] + [F(physical == e) for _ in selected for _,_,physical in arcs]
        add(row, cap)
    for charges, cap in rows:
        add([F(0)] + [charges[i][j] for i in selected for j in range(len(arcs))], cap)
    upper = sum((cap for _,_,cap in net.edges), F(0)) / min(net.commodities[i][2] for i in selected)
    add([F(1)] + [F(0)]*(n-1), upper)
    return tuple(a), tuple(b), (F(1),) + (F(0),)*(n-1)


@dataclass(frozen=True)
class Certificate:
    selected: tuple
    primal: tuple
    dual: tuple

    @property
    def rate(self):
        return self.primal[0]


def optimize_fixed(net, selected, budgets=(), setup=None):
    selected = tuple(selected)
    lp = formulation(net, selected, budgets, setup)
    if lp is None:
        return None
    x, y = simplex(*lp)
    return Certificate(selected, x, y)


def verify_fixed(net, certificate, budgets=(), setup=None):
    try:
        lp = formulation(net, certificate.selected, budgets, setup)
        return lp is not None and verify_lp(*lp, certificate.primal, certificate.dual)
    except (ValueError, TypeError, AttributeError, IndexError):
        return False


def optimize_selected(net, rank, permitted=lambda selected: True, budgets=(), setup=None):
    """Exact enumeration baseline; None means no affordable permitted set.

    permitted is a paid fixed-family predicate. Certifies fixed-set optimality;
    global optimality also relies on exhaustive enumeration and that predicate.
    """
    if type(rank) is not int or not 1 <= rank <= len(net.commodities):
        raise ValueError('rank must be between one and commodity count')
    budgets = tuple(budgets)
    best = None
    for selected in combinations(range(len(net.commodities)), rank):
        if permitted(selected):
            candidate = optimize_fixed(net, selected, budgets, setup)
            if candidate is not None and (best is None or candidate.rate > best.rate):
                best = candidate
    return best

@dataclass(frozen=True)
class PackingRow:
    lengths: tuple
    multipliers: tuple
    potentials: tuple
    coefficients: tuple
    capacity: F


def separate(net, rates, budgets=()):
    """Return a globally valid strictly violated nonnegative row, or None.

    This executes the normalized Farkas LP from proof Sections 3--4. None
    means membership; it is not a reconstructed routing witness.
    """
    rates = tuple(rational(z) for z in rates)
    q, v, e = len(net.commodities), net.vertices, len(net.edges)
    if len(rates) != q or any(z < 0 for z in rates):
        raise ValueError('invalid service vector')
    budgets = tuple((tuple(tuple(rational(x) for x in row) for row in charges),rational(cap)) for charges,cap in budgets)
    # Reuse only input validation, not optimization or the fixed-set matrix.
    if q:
        formulation(net,(0,),budgets)
    elif budgets:
        raise ValueError('budgeted separator needs a commodity')
    arcs, s = net.arcs(), len(budgets)
    offset = e+s
    n = offset+2*q*v
    def pos(i,u): return offset+2*(i*v+u)
    def potential(row,i,u,mult):
        row[pos(i,u)] += mult; row[pos(i,u)+1] -= mult
    a,b = [],[]
    for i,(source,target,_) in enumerate(net.commodities):
        for j,(u,w,physical) in enumerate(arcs):
            row = [F(0)]*n
            potential(row,i,u,1); potential(row,i,w,-1)
            row[physical] -= 1
            for h,(charges,_) in enumerate(budgets): row[e+h] -= charges[i][j]
            a.append(row); b.append(F(0))
        row = [F(0)]*n
        potential(row,i,source,-1); potential(row,i,target,1)
        a.append(row); b.append(F(0))
    a.append([F(1)]*n); b.append(F(1))
    c = [-cap for _,_,cap in net.edges]+[-cap for _,cap in budgets]+[F(0)]*(2*q*v)
    for i,(source,target,demand) in enumerate(net.commodities):
        potential(c,i,source,demand*rates[i]); potential(c,i,target,-demand*rates[i])
    x,_ = simplex(a,b,c)
    if sum(ci*xi for ci,xi in zip(c,x)) == 0:
        return None
    potentials = tuple(tuple(x[pos(i,u)]-x[pos(i,u)+1] for u in range(v)) for i in range(q))
    coefficients = tuple(demand*(potentials[i][source]-potentials[i][target]) for i,(source,target,demand) in enumerate(net.commodities))
    capacity = sum(net.edges[j][2]*x[j] for j in range(e))+sum(cap*x[e+h] for h,(_,cap) in enumerate(budgets))
    return PackingRow(tuple(x[:e]),tuple(x[e:offset]),potentials,coefficients,capacity)
