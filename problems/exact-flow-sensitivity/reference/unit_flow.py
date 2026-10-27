"""Exact unit-flow single-deletion preservers with compact path reports.

Standard library only. Arc IDs are positions in the supplied arc tuple. Costs
must be integers or fractions.Fraction values; floating point is rejected.
The polynomial preprocessing here does not implement the manuscript's faster
all-source shortest-path and incidence-heap construction.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


@dataclass(frozen=True)
class Arc:
    tail: int
    head: int
    cost: Fraction


@dataclass(frozen=True)
class Residual:
    tail: int
    head: int
    cost: Fraction
    tie: int
    original: int
    sign: int


def _shortest(n: int, arcs: tuple[Residual, ...], source: int):
    """Bellman--Ford on (cost, tie, hops), with strict relaxations.

    The last coordinate excludes zero-cost parent cycles. Negative cycles
    reachable from source are rejected, including a negative tie coordinate.
    """
    distances = [None] * n
    parents = [None] * n
    distances[source] = (Fraction(0), 0, 0)
    for _ in range(n - 1):
        changed = False
        for arc in arcs:
            distance = distances[arc.tail]
            if distance is None:
                continue
            candidate = (distance[0] + arc.cost,
                         distance[1] + arc.tie, distance[2] + 1)
            if distances[arc.head] is None or candidate < distances[arc.head]:
                distances[arc.head] = candidate
                parents[arc.head] = arc
                changed = True
        if not changed:
            break
    for arc in arcs:
        distance = distances[arc.tail]
        if distance is not None:
            candidate = (distance[0] + arc.cost,
                         distance[1] + arc.tie, distance[2] + 1)
            if distances[arc.head] is None or candidate < distances[arc.head]:
                raise ValueError("negative residual cycle")
    return distances, parents


def _path(parents, source: int, target: int) -> tuple[Residual, ...]:
    backwards = []
    vertex = target
    while vertex != source:
        arc = parents[vertex]
        if arc is None:
            raise ValueError("unreachable path")
        backwards.append(arc)
        vertex = arc.tail
        if len(backwards) >= len(parents):
            raise ValueError("cyclic predecessor chain")
    return tuple(reversed(backwards))


class CompactPaths:
    """Phased short paths and hub trees for supplied residual demands.

    Input cycles must have nonnegative cost and every arc must have tie=1.
    Stored state contains only selected lists, trees, and demand descriptors;
    it drops the graph and all-pairs preprocessing tables on return.
    """

    def __init__(self, n: int, arcs: tuple[Residual, ...], demands):
        if n < 1 or any(a.tie != 1 for a in arcs):
            raise ValueError("positive-hop residual representation required")
        self.n = n
        self.descriptors = {}
        self.hubs = []
        all_sources = [_shortest(n, arcs, source) for source in range(n)]
        pending = {}
        for key, (source, target) in demands.items():
            distance, parents = all_sources[source]
            if distance[target] is None:
                self.descriptors[key] = None
            else:
                pending[key] = (source, target, _path(parents, source, target))
        self.phase_counts = []
        while pending:
            count = len(pending)
            # Smallest integer L with L*sqrt(count) >= n; no floating point.
            quotient = (n * n + count - 1) // count
            length = isqrt(quotient - 1) + 1
            long = {}
            for key, (source, target, path) in pending.items():
                if len(path) <= length:
                    self.descriptors[key] = ("short", path)
                else:
                    vertices = {source, *(arc.head for arc in path)}
                    long[key] = (source, target, vertices)
            initial_long = len(long)
            selections = 0
            for _ in range((n + length - 1) // length):
                if not long:
                    break
                coverage = [0] * n
                for _, _, vertices in long.values():
                    for vertex in vertices:
                        coverage[vertex] += 1
                hub = max(range(n), key=lambda v: (coverage[v], -v))
                hit = [key for key, (_, _, vertices) in long.items()
                       if hub in vertices]
                if not hit:
                    raise RuntimeError("greedy hitting made no progress")
                reversed_arcs = tuple(Residual(a.head, a.tail, a.cost, 1,
                                               a.original, a.sign) for a in arcs)
                _, incoming_reversed = _shortest(n, reversed_arcs, hub)
                incoming = tuple(None if a is None else Residual(
                    a.head, a.tail, a.cost, 1, a.original, a.sign)
                    for a in incoming_reversed)
                outgoing = tuple(all_sources[hub][1])
                index = len(self.hubs)
                self.hubs.append((hub, incoming, outgoing))
                for key in hit:
                    source, target, _ = long.pop(key)
                    self.descriptors[key] = ("hub", index, source, target)
                selections += 1
            self.phase_counts.append((count, length, initial_long, selections,
                                      len(long)))
            pending = {key: pending[key] for key in long}

    def report(self, key) -> tuple[Residual, ...] | None:
        descriptor = self.descriptors[key]
        if descriptor is None:
            return None
        if descriptor[0] == "short":
            return descriptor[1]
        _, index, source, target = descriptor
        hub, incoming, outgoing = self.hubs[index]
        prefix = []
        vertex = source
        while vertex != hub:
            arc = incoming[vertex]
            if arc is None or len(prefix) >= self.n:
                raise RuntimeError("invalid incoming tree")
            prefix.append(arc)
            vertex = arc.head
        return tuple(prefix) + _path(outgoing, hub, target)

    def retained_residuals(self):
        for descriptor in self.descriptors.values():
            if descriptor is not None and descriptor[0] == "short":
                yield from descriptor[1]
        for _, incoming, outgoing in self.hubs:
            yield from (arc for arc in incoming if arc is not None)
            yield from (arc for arc in outgoing if arc is not None)

    def record_count(self) -> int:
        """Descriptors, list entries and both full vertex-pointer arrays."""
        return (len(self.descriptors) + 2 * self.n * len(self.hubs)
                + sum(len(d[1]) for d in self.descriptors.values()
                      if d is not None and d[0] == "short"))


def _residual(arcs, support, signed_count=False):
    return tuple(Residual(a.head if i in support else a.tail,
                          a.tail if i in support else a.head,
                          -a.cost if i in support else a.cost,
                          (-1 if i in support else 1) if signed_count else 1,
                          i, -1 if i in support else 1)
                 for i, a in enumerate(arcs))


def _validate(n, arcs, source, target):
    if (type(n) is not int or n < 2 or type(source) is not int
            or type(target) is not int or not 0 <= source < n or not 0 <= target < n):
        raise ValueError("invalid graph or terminals")
    if source == target:
        raise ValueError("terminals must differ")
    output = []
    for arc in arcs:
        if (type(arc.tail) is not int or type(arc.head) is not int
                or not 0 <= arc.tail < n or not 0 <= arc.head < n
                or arc.tail == arc.head):
            raise ValueError("invalid loopless arc")
        if type(arc.cost) not in (int, Fraction) or arc.cost < 0:
            raise ValueError("costs must be exact nonnegative rationals")
        output.append(Arc(arc.tail, arc.head, Fraction(arc.cost)))
    return tuple(output)


def _augmentations(n, arcs, source, target):
    support = set()
    yield frozenset(support)
    while True:
        residual = _residual(arcs, support, signed_count=True)
        distances, parents = _shortest(n, residual, source)
        if distances[target] is None:
            return
        for arc in _path(parents, source, target):
            if arc.sign == 1:
                support.add(arc.original)
            else:
                support.remove(arc.original)
        yield frozenset(support)


@dataclass(frozen=True)
class Change:
    cost: Fraction
    removed: tuple[int, ...]
    added: tuple[int, ...]


class _FixedFlowOracle:
    """Independent single-record deletion queries at one fixed flow value."""

    def __init__(self, n, arcs, value, support):
        self.n = n
        self.original_count = len(arcs)
        self.value = value
        self.baseline = tuple(sorted(support))
        self.baseline_cost = sum((arcs[i].cost for i in support), Fraction(0))
        residual = _residual(arcs, support)
        self.paths = CompactPaths(n, residual,
                                  {i: (arcs[i].tail, arcs[i].head) for i in support})
        retained = set(support)
        retained.update(a.original for a in self.paths.retained_residuals())
        self.retained = {i: arcs[i] for i in sorted(retained)}
        self.costs = {}
        for i in support:
            path = self.paths.report(i)
            self.costs[i] = (None if path is None else self.baseline_cost
                             - arcs[i].cost + sum((a.cost for a in path), Fraction(0)))

    def _check_failure(self, failed):
        if failed is not None and (type(failed) is not int
                                   or not 0 <= failed < self.original_count):
            raise ValueError("failure must name one original record or None")

    def cost(self, failed: int | None = None) -> Fraction | None:
        self._check_failure(failed)
        return self.costs.get(failed, self.baseline_cost)

    def difference(self, failed: int | None = None) -> Change | None:
        self._check_failure(failed)
        if failed not in self.costs:
            return Change(self.baseline_cost, (), ())
        if self.costs[failed] is None:
            return None
        path = self.paths.report(failed)
        removed = (failed,) + tuple(a.original for a in path if a.sign == -1)
        added = tuple(a.original for a in path if a.sign == 1)
        return Change(self.costs[failed], removed, added)

    def flow(self, failed: int | None = None) -> tuple[int, ...] | None:
        change = self.difference(failed)
        if change is None:
            return None
        removed = set(change.removed)
        return tuple(i for i in self.baseline if i not in removed) + change.added


def fixed_flow(n: int, arcs, source: int, target: int, value: int):
    """Return a compact oracle, or None when the original value is infeasible."""
    arcs = _validate(n, arcs, source, target)
    if type(value) is not int or value < 0:
        raise ValueError("value must be a nonnegative integer")
    for achieved, support in enumerate(_augmentations(n, arcs, source, target)):
        if achieved == value:
            return _FixedFlowOracle(n, arcs, value, support)
    return None


class MaximumFlowOracle:
    """Minimum-cost maximum flow after an independent single-arc deletion."""

    def __init__(self, n: int, arcs, source: int, target: int):
        arcs = _validate(n, arcs, source, target)
        previous = None
        for value, support in enumerate(_augmentations(n, arcs, source, target)):
            if value:
                previous = current
            current = support
        self.upper = _FixedFlowOracle(n, arcs, value, current)
        self.lower = (None if value == 0 else
                      _FixedFlowOracle(n, arcs, value - 1, previous))

    def query(self, failed: int | None = None):
        oracle = self.upper if self.upper.cost(failed) is not None else self.lower
        if oracle is None:
            raise RuntimeError("one unit-capacity deletion lost two flow units")
        return oracle.value, oracle.cost(failed), oracle.flow(failed)
