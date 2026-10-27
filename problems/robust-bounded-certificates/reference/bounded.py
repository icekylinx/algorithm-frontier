"""Certified budgeted unit tests and bounded hereditary gate.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
Exact weighted matroid intersection is polynomial in paid independence work.
Complete rank tables are explicit input; capacities are not expanded.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


def rational(value):
    if type(value) not in (int, F):
        raise ValueError('exact int or Fraction data required')
    return F(value)


def exchange(n, chosen, independent1, independent2):
    outside = tuple(i for i in range(n) if i not in chosen)
    inside = tuple(sorted(chosen))
    sources = tuple(i for i in outside if independent1(chosen | {i}))
    targets = tuple(i for i in outside if independent2(chosen | {i}))
    arcs = tuple((u,v) for u in inside for v in outside
                 if independent1((chosen - {u}) | {v}))
    arcs += tuple((u,v) for u in outside for v in inside
                  if independent2((chosen - {v}) | {u}))
    return sources, targets, arcs


def potentials(n, arcs, costs):
    # All-source shortest distances certify absence of negative directed cycles.
    distance = [F(0)]*n
    for _ in range(max(0,n-1)):
        new = distance.copy()
        for u,v in arcs:
            new[v] = min(new[v], distance[u]+costs[v])
        if new == distance:
            break
        distance = new
    if any(distance[v] > distance[u]+costs[v] for u,v in arcs):
        raise RuntimeError('negative exchange cycle')
    return tuple(distance)


@dataclass(frozen=True)
class IntersectionCertificate:
    chosen: tuple
    potential: tuple
    cut: tuple | None = None  # When present, certifies maximum cardinality too.


def minimum_cost(independent1, independent2, costs, target):
    """Minimum cost at target size, or a maximum-cardinality smaller set.

    Ground is range(len(costs)); predicates must be matroid independence
    oracles. Costs may be signed exact rationals; target is a binary integer.
    """
    costs = tuple(rational(c) for c in costs)
    n = len(costs)
    if type(target) is not int or target < 0:
        raise ValueError('nonnegative integer cardinality required')
    chosen = frozenset()
    cut = None
    while len(chosen) < target:
        sources, targets, arcs = exchange(n,chosen,independent1,independent2)
        signed = tuple(-c if i in chosen else c for i,c in enumerate(costs))
        # Labels compare total vertex cost, then path length, then integer IDs.
        labels = {s: (signed[s],1,(s,)) for s in sources}
        for _ in range(max(0,n-1)):
            new = labels.copy()
            for u,v in arcs:
                if u in labels:
                    value,length,path = labels[u]
                    candidate = (value+signed[v],length+1,path+(v,))
                    if v not in new or candidate < new[v]:
                        new[v] = candidate
            if new == labels:
                break
            labels = new
        reachable_targets = [v for v in targets if v in labels]
        if not reachable_targets:
            cut = tuple(i for i in range(n) if i not in labels)
            break
        _,_,path = min(labels[v] for v in reachable_targets)
        if len(set(path)) != len(path):
            raise RuntimeError('shortest cheapest path is not simple')
        chosen = chosen.symmetric_difference(path)
        if not independent1(chosen) or not independent2(chosen):
            raise RuntimeError('weighted augmentation invariant violated')
    _,_,arcs = exchange(n,chosen,independent1,independent2)
    signed = tuple(-c if i in chosen else c for i,c in enumerate(costs))
    return IntersectionCertificate(tuple(sorted(chosen)),potentials(n,arcs,signed),cut)


def _ids(values, n):
    return (type(values) is tuple and len(set(values)) == len(values)
            and all(type(i) is int and 0 <= i < n for i in values))


def greedy_rank(ground, independent):
    chosen = frozenset()
    for element in ground:
        if independent(chosen | {element}):
            chosen = chosen | {element}
    return len(chosen)


def verify_intersection(independent1, independent2, costs, target, certificate):
    """Search-free fixed-cardinality minimum, plus a rank cut if underfull."""
    try:
        costs = tuple(rational(c) for c in costs)
        n = len(costs)
        if (type(target) is not int or target < 0 or type(certificate) is not IntersectionCertificate
                or not _ids(certificate.chosen,n) or len(certificate.chosen) > target
                or type(certificate.potential) is not tuple or len(certificate.potential) != n):
            return False
        potential = tuple(rational(x) for x in certificate.potential)
        chosen = frozenset(certificate.chosen)
        if not independent1(chosen) or not independent2(chosen):
            return False
        _,_,arcs = exchange(n,chosen,independent1,independent2)
        signed = tuple(-c if i in chosen else c for i,c in enumerate(costs))
        if any(potential[v] > potential[u]+signed[v] for u,v in arcs):
            return False
        if certificate.cut is not None:
            if not _ids(certificate.cut,n):
                return False
            cut = frozenset(certificate.cut)
            if (greedy_rank(sorted(cut),independent1)
                    + greedy_rank((i for i in range(n) if i not in cut),independent2) != len(chosen)):
                return False
        return len(chosen) == target or certificate.cut is not None
    except (ValueError,TypeError,AttributeError,IndexError):
        return False


@dataclass(frozen=True)
class UnitCertificate:
    selected: tuple
    assignment: tuple  # (player, type), one pair per selected player on success.
    intersection: IntersectionCertificate


class UnitScenario:
    """One budget, Boolean-cap resource matroids, and explicit assignment costs.

    costs[player][type] is None for an ineligible pair, otherwise nonnegative.
    Boolean resource predicates accept frozensets of original owner IDs.
    """
    def __init__(self, q, resource_independent, costs, budget):
        self.resource_independent = tuple(resource_independent)
        self.costs = tuple(tuple(None if c is None else rational(c) for c in row) for row in costs)
        self.budget = rational(budget)
        self.q, self.m = q, len(self.resource_independent)
        if (type(q) is not int or q < 0 or len(self.costs) != q
                or any(len(row) != self.m for row in self.costs)
                or self.budget < 0 or any(c is not None and c < 0 for row in self.costs for c in row)
                or any(not callable(test) for test in self.resource_independent)):
            raise ValueError('invalid unit scenario')

    def formulation(self, selected):
        selected = tuple(selected)
        if not _ids(selected,self.q):
            raise ValueError('distinct original player IDs required')
        pairs = tuple((p,j) for p in sorted(selected) for j in range(self.m) if self.costs[p][j] is not None)
        def resource(chosen):
            return all(test(frozenset(pairs[i][0] for i in chosen if pairs[i][1] == j))
                       for j,test in enumerate(self.resource_independent))
        def owner(chosen):
            return len({pairs[i][0] for i in chosen}) == len(chosen)
        return pairs,resource,owner,tuple(self.costs[p][j] for p,j in pairs)

    def optimize(self, selected):
        selected = tuple(sorted(selected))
        pairs,resource,owner,costs = self.formulation(selected)
        certificate = minimum_cost(resource,owner,costs,len(selected))
        return UnitCertificate(selected,tuple(pairs[i] for i in certificate.chosen),certificate)

    def verify(self, certificate):
        """Search-free exact minimum-cost unit test, even for rejection records."""
        try:
            if type(certificate) is not UnitCertificate:
                return False
            pairs,resource,owner,costs = self.formulation(certificate.selected)
            return (type(certificate.assignment) is tuple
                    and verify_intersection(resource,owner,costs,len(certificate.selected),certificate.intersection)
                    and certificate.assignment == tuple(pairs[i] for i in certificate.intersection.chosen))
        except (ValueError,TypeError,AttributeError,IndexError):
            return False

    def affordable(self, certificate):
        return (len(certificate.assignment) == len(certificate.selected)
                and sum((self.costs[p][j] for p,j in certificate.assignment),F(0)) <= self.budget)

    def __call__(self, selected):
        certificate = self.optimize(selected)
        return certificate if self.affordable(certificate) else None


def table_scenario(ranks, costs, budget):
    """Validate explicit original polymatroid rank tables; no unit copies."""
    ranks = tuple(tuple(row) for row in ranks)
    costs = tuple(tuple(row) for row in costs)
    q = len(costs)
    for row in ranks:
        if (len(row) != 1 << q or row[0] != 0
                or any(type(x) is not int or x < 0 for x in row)):
            raise ValueError('normalized nonnegative integer rank table required')
        for a in range(1 << q):
            for b in range(1 << q):
                if a & b == a and row[a] > row[b]:
                    raise ValueError('nonmonotone resource rank')
                if row[a]+row[b] < row[a|b]+row[a&b]:
                    raise ValueError('nonsubmodular resource rank')
    def capped(row):
        return lambda selected: all(sum(1 for p in selected if mask >> p & 1) <= value
                                    for mask,value in enumerate(row))
    return UnitScenario(q,tuple(capped(row) for row in ranks),costs,budget)


@dataclass(frozen=True)
class GateOutcome:
    status: str
    selected: tuple = ()
    witnesses: tuple = ()
    scenario: int | None = None
    certificate: tuple = ()
    nodes: int = 0


def gate(q, rank, rank_oracle, scenarios, width, forced=()):
    """Bounded-certificate common-basis unit extension in original coordinates."""
    if (type(q) is not int or type(rank) is not int or not 0 <= rank <= q
            or type(width) is not int or width < 1):
        raise ValueError('invalid ground, rank or certificate width')
    scenarios = tuple(scenarios)
    if not scenarios or any(not callable(test) for test in scenarios):
        raise ValueError('nonempty exact hereditary scenario list required')
    ground = frozenset(range(q))
    forced = frozenset(forced)
    if any(type(p) is not int or p not in ground for p in forced) or rank_oracle(ground) != rank:
        raise ValueError('invalid forced seed or original rank')
    stack = [ground-forced]
    nodes = 0
    while stack:
        allowed = stack.pop()
        nodes += 1
        if len(allowed) < rank or rank_oracle(allowed) < rank:
            continue
        basis = frozenset()
        for player in sorted(allowed):
            if rank_oracle(basis | {player}) > len(basis):
                basis = basis | {player}
                if len(basis) == rank:
                    break
        witnesses = []
        failed = None
        for omega,test in enumerate(scenarios):
            witness = test(basis)
            if witness is None:
                failed = omega
                break
            witnesses.append(witness)
        if failed is None:
            return GateOutcome('SUCCESS',tuple(sorted(basis)),tuple(witnesses),nodes=nodes)
        test = scenarios[failed]
        certificate = basis
        for player in sorted(basis):
            if test(certificate-{player}) is None:
                certificate = certificate-{player}
        if not certificate:
            raise RuntimeError('scenario empty-set feasibility contract violated')
        if len(certificate) > width:
            return GateOutcome('WIDTH VIOLATION',scenario=failed,
                               certificate=tuple(sorted(certificate)),nodes=nodes)
        if len(allowed) > rank:
            for player in sorted(certificate,reverse=True):
                stack.append(allowed-{player})
    return GateOutcome('INFEASIBLE',nodes=nodes)
