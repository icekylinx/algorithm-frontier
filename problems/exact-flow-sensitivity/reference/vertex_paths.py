"""Compact exact single-failure oracles for internally disjoint paths.

Input is a simple directed graph with nonnegative exact rational costs.
Native arc IDs are input positions. Queries independently delete one arc
or one nonterminal vertex. Only retained records survive preprocessing.

Attribution: icekylinx and GPT-6 Astra Pro.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from unit_flow import Arc, MaximumFlowOracle, fixed_flow


@dataclass(frozen=True)
class Path:
    vertices: tuple[int, ...]
    arc_ids: tuple[int, ...]


@dataclass(frozen=True)
class Packing:
    value: int
    cost: Fraction
    paths: tuple[Path, ...]


def _split(n, arcs, source, target):
    if (type(n) is not int or n < 2 or type(source) is not int
            or type(target) is not int or not 0 <= source < n
            or not 0 <= target < n or source == target):
        raise ValueError("distinct in-range integer terminals required")
    native = []
    pairs = set()
    for arc in arcs:
        if (not isinstance(arc, Arc) or type(arc.tail) is not int
                or type(arc.head) is not int or not 0 <= arc.tail < n
                or not 0 <= arc.head < n or arc.tail == arc.head):
            raise ValueError("invalid loopless original arc")
        if type(arc.cost) not in (int, Fraction) or arc.cost < 0:
            raise ValueError("costs must be exact nonnegative rationals")
        pair = (arc.tail, arc.head)
        if pair in pairs:
            raise ValueError("parallel originals are outside this simple-graph contract")
        pairs.add(pair)
        native.append(Arc(arc.tail, arc.head, Fraction(arc.cost)))
    split = []
    origins = {}
    for index, arc in enumerate(native):
        # Such arcs belong to no simple source-to-target path. Their deletion
        # is accepted as an irrelevant original failure after preprocessing.
        if arc.head == source or arc.tail == target:
            continue
        origins[len(split)] = index
        split.append(Arc(2 * arc.tail + (arc.tail != source),
                         2 * arc.head, arc.cost))
    gates = {}
    for vertex in range(n):
        if vertex not in (source, target):
            gates[len(split)] = vertex
            split.append(Arc(2 * vertex, 2 * vertex + 1, Fraction(0)))
    return tuple(native), tuple(split), origins, gates


class _FixedPackingOracle:
    """Internal adapter of a computed and validated unit-flow oracle."""

    def __init__(self, n, source, target, native, flow, origins, gates):
        self.n, self.source, self.target = n, source, target
        self.original_count = len(native)
        self.value = flow.value
        self._flow = flow
        self._origin = {i: origins[i] for i in flow.retained if i in origins}
        self.retained = {original: native[original] for original in self._origin.values()}
        # Only failures on this baseline require a nontrivial flow query.
        self._arc_failure = {origins[i]: i for i in flow.baseline if i in origins}
        self._vertex_failure = {gates[i]: i for i in flow.baseline if i in gates}

    def _failure(self, failed_arc, failed_vertex):
        if failed_arc is not None and failed_vertex is not None:
            raise ValueError("supply at most one arc or internal-vertex failure")
        if failed_arc is not None:
            if type(failed_arc) is not int or not 0 <= failed_arc < self.original_count:
                raise ValueError("failure must be an original arc ID")
            return self._arc_failure.get(failed_arc)
        if failed_vertex is not None:
            if (type(failed_vertex) is not int or not 0 <= failed_vertex < self.n
                    or failed_vertex in (self.source, self.target)):
                raise ValueError("failure must be an internal vertex")
            return self._vertex_failure.get(failed_vertex)
        return None

    def cost(self, *, failed_arc=None, failed_vertex=None):
        """Return the exact optimum cost or None for infeasibility."""
        return self._flow.cost(self._failure(failed_arc, failed_vertex))

    def query(self, *, failed_arc=None, failed_vertex=None):
        """Return native simple paths, or None at an infeasible fixed value."""
        failure = self._failure(failed_arc, failed_vertex)
        support = self._flow.flow(failure)
        if support is None:
            return None
        used = [self._origin[i] for i in support if i in self._origin]
        following = {}
        starts = []
        for index in used:
            arc = self.retained[index]
            if arc.tail == self.source:
                starts.append(index)
            else:
                if arc.tail in following:
                    raise RuntimeError("split flow violates an internal unit gate")
                following[arc.tail] = index
        if len(starts) != self.value:
            raise RuntimeError("split flow has the wrong source value")
        paths = []
        occupied = set()
        total = Fraction(0)
        for first in starts:
            vertices = [self.source]
            indices = []
            index = first
            while True:
                arc = self.retained[index]
                indices.append(index)
                vertices.append(arc.head)
                total += arc.cost
                if arc.head == self.target:
                    break
                if arc.head in occupied or arc.head == self.source:
                    raise RuntimeError("split flow does not give internally disjoint simple paths")
                occupied.add(arc.head)
                if arc.head not in following:
                    raise RuntimeError("split flow violates conservation")
                index = following[arc.head]
            paths.append(Path(tuple(vertices), tuple(indices)))
        optimum = self._flow.cost(failure)
        # Minimum-cost flows may contain zero-cost circulations after repair.
        # Discard those components; nonnegative optimality makes them free.
        if total != optimum:
            raise RuntimeError("discarded circulation has nonzero cost")
        return Packing(self.value, total, tuple(paths))


def fixed_paths(n: int, arcs, source: int, target: int, value: int):
    """Build an exact fixed-cardinality path oracle, or None if infeasible.

    Zero is permitted. The public input graph is simple; repeated ordered
    endpoint pairs, loops, floats, booleans and negative costs are rejected.
    """
    if type(value) is not int or value < 0:
        raise ValueError("value must be a nonnegative integer")
    native, split, origins, gates = _split(n, arcs, source, target)
    flow = fixed_flow(2 * n, split, 2 * source, 2 * target, value)
    if flow is None:
        return None
    return _FixedPackingOracle(n, source, target, native, flow, origins, gates)


class MaximumPathsOracle:
    """Minimum-cost maximum packing after one independent native failure."""

    def __init__(self, n: int, arcs, source: int, target: int):
        native, split, origins, gates = _split(n, arcs, source, target)
        flow = MaximumFlowOracle(2 * n, split, 2 * source, 2 * target)
        self.upper = _FixedPackingOracle(n, source, target, native,
                                         flow.upper, origins, gates)
        self.lower = (None if flow.lower is None else
                      _FixedPackingOracle(n, source, target, native,
                                          flow.lower, origins, gates))
        self.retained = dict(self.upper.retained)
        if self.lower is not None:
            self.retained.update(self.lower.retained)

    def query(self, *, failed_arc=None, failed_vertex=None):
        """Return a native maximum-cardinality, minimum-cost Packing."""
        selected = self.upper
        if selected.cost(failed_arc=failed_arc, failed_vertex=failed_vertex) is None:
            selected = self.lower
        if selected is None:
            raise RuntimeError("one native failure lost more than one path")
        return selected.query(failed_arc=failed_arc, failed_vertex=failed_vertex)
