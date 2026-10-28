"""Exact supplied-baseline single-arc-failure arborescence reporting.

Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0

The caller supplies an optimal rooted spanning arborescence. This module does
not compute that baseline. It realizes the manuscript's heavy-light auxiliary
graph and deterministic phased path-reporting construction. Exact Floyd--
Warshall replaces its faster shortest-path implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


@dataclass(frozen=True)
class Arc:
    tail: int
    head: int
    cost: int | Fraction


@dataclass(frozen=True)
class _AuxArc:
    tail: int
    head: int
    length: tuple[Fraction, int]
    label: int | None = None
    removed: int | None = None


def _add(a, b):
    return (a[0] + b[0], a[1] + b[1])


@dataclass(frozen=True)
class _Hub:
    vertex: int
    # Each entry points toward the hub, or away from it, respectively.
    incoming: dict[int, _AuxArc]
    outgoing: dict[int, _AuxArc]


@dataclass(frozen=True)
class _Route:
    source: int
    target: int
    explicit: tuple[_AuxArc, ...] | None
    hub: int | None


@dataclass(frozen=True)
class Oracle:
    """Final reporting records; no original graph or distance matrix is kept."""

    baseline: tuple[int, ...]
    baseline_cost: Fraction
    routes: dict[int, _Route | None]
    hubs: tuple[_Hub, ...]
    support: tuple[int, ...]
    values: dict[int, Fraction | None]
    auxiliary_nodes: int
    auxiliary_arcs: int
    phases: int

    @property
    def record_count(self):
        """Count constant-size records, including copies in different trees."""
        return (len(self.baseline) + len(self.support) + 2 * len(self.routes)
                + len(self.hubs)
                + sum(len(h.incoming) + len(h.outgoing) for h in self.hubs)
                + sum(len(r.explicit) if r is not None and r.explicit is not None
                      else 0 for r in self.routes.values()))

    def _report(self, route):
        if route.explicit is not None:
            return route.explicit
        hub = self.hubs[route.hub]
        prefix, suffix = [], []
        vertex = route.source
        while vertex != hub.vertex:
            arc = hub.incoming[vertex]
            prefix.append(arc)
            vertex = arc.head
        vertex = route.target
        while vertex != hub.vertex:
            arc = hub.outgoing[vertex]
            suffix.append(arc)
            vertex = arc.tail
        return tuple(prefix + suffix[::-1])

    def query(self, failed: int | None = None) -> tuple[int, ...] | None:
        """Return optimum original element IDs, or None when infeasible.

        None means no failure; any unknown original ID has no effect. This
        method traverses stored paths and baseline IDs only.
        """
        if failed not in self.routes:
            return self.baseline
        route = self.routes[failed]
        if route is None:
            return None
        path = self._report(route)
        removed = {a.removed for a in path if a.removed is not None}
        added = tuple(a.label for a in path if a.label is not None)
        return tuple(a for a in self.baseline if a not in removed) + added

    def optimum_cost(self, failed: int | None = None):
        return self.values.get(failed, self.baseline_cost)


def _auxiliary(n, root, arcs, baseline):
    """Build the actual HLD/segment-tree graph, retaining parallel labels."""
    children = [[] for _ in range(n)]
    parent = [-1] * n
    entering = {}
    for i in baseline:
        arc = arcs[i]
        children[arc.tail].append(arc.head)
        parent[arc.head] = arc.tail
        entering[arc.head] = i
    depth = [0] * n
    order = [root]
    for u in order:
        for v in children[u]:
            depth[v] = depth[u] + 1
            order.append(v)
    size = [1] * n
    heavy = [-1] * n
    for u in order[::-1]:
        for v in children[u]:
            size[u] += size[v]
            if heavy[u] == -1 or size[v] > size[heavy[u]]:
                heavy[u] = v
    position, head = [-1] * n, [-1] * n
    pending = [(root, root)]
    cursor = 0
    while pending:
        u, chain = pending.pop()
        head[u] = chain
        if u != root:
            position[u] = cursor
            cursor += 1
        for v in reversed(children[u]):
            if v != heavy[u]:
                pending.append((v, v))
        if heavy[u] != -1:
            pending.append((heavy[u], chain))

    def path_intervals(u, v):
        intervals = []
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            intervals.append((position[head[u]], position[u] + 1))
            u = parent[head[u]]
        if depth[u] > depth[v]:
            u, v = v, u
        if u != v:
            intervals.append((position[u] + 1, position[v] + 1))
        return intervals

    k = n - 1
    nodes = 2 * k
    output = []
    zero = (Fraction(0), 0)
    minus = {arc_id: 2 * i for i, arc_id in enumerate(baseline)}
    plus = {arc_id: node + 1 for arc_id, node in minus.items()}
    leaves, segments = {}, {}

    def segment(lo, hi):
        nonlocal nodes
        node = nodes
        nodes += 1
        if hi - lo == 1:
            leaves[lo] = node
            segments[node] = (lo, hi, None, None)
        else:
            mid = (lo + hi) // 2
            left, right = segment(lo, mid), segment(mid, hi)
            segments[node] = (lo, hi, left, right)
            output.extend((_AuxArc(left, node, zero), _AuxArc(right, node, zero)))
        return node

    segment_root = segment(0, k) if k else None

    def cover(node, lo, hi):
        start, end, left, right = segments[node]
        if lo <= start and end <= hi:
            return [node]
        result = []
        for child in (left, right):
            if child is not None:
                a, b, _, _ = segments[child]
                if lo < b and a < hi:
                    result.extend(cover(child, lo, hi))
        return result

    for v, arc_id in entering.items():
        output.append(_AuxArc(minus[arc_id], plus[arc_id], zero))
        output.append(_AuxArc(plus[arc_id], leaves[position[v]],
                              (-arcs[arc_id].cost, 0), removed=arc_id))
    selected = set(baseline)
    for i, arc in enumerate(arcs):
        if i in selected or arc.head == root or arc.tail == arc.head:
            continue
        for lo, hi in path_intervals(arc.tail, arc.head):
            for node in cover(segment_root, lo, hi):
                output.append(_AuxArc(node, minus[entering[arc.head]],
                                      (arc.cost, 1), label=i))
    return nodes, tuple(output), minus, plus


def _distances(nodes, arcs):
    """Exact lexicographic Floyd--Warshall; no input numeric perturbation."""
    distance = [[None] * nodes for _ in range(nodes)]
    first = [[None] * nodes for _ in range(nodes)]
    last = [[None] * nodes for _ in range(nodes)]
    for u in range(nodes):
        distance[u][u] = (Fraction(0), 0)
    for arc in arcs:
        old = distance[arc.tail][arc.head]
        if old is None or arc.length < old:
            distance[arc.tail][arc.head] = arc.length
            first[arc.tail][arc.head] = last[arc.tail][arc.head] = arc
    for middle in range(nodes):
        for source in range(nodes):
            left = distance[source][middle]
            if left is None:
                continue
            for target in range(nodes):
                right = distance[middle][target]
                if right is not None:
                    candidate = _add(left, right)
                    old = distance[source][target]
                    if old is None or candidate < old:
                        distance[source][target] = candidate
                        first[source][target] = (first[source][middle]
                                                 or first[middle][target])
                        last[source][target] = (last[middle][target]
                                                or last[source][middle])
    if any(distance[u][u] < (0, 0) for u in range(nodes)):
        raise ValueError("negative exchange cycle: supplied baseline is not optimal")
    return distance, first, last


def _path(source, target, first):
    path, visited = [], {source}
    while source != target:
        arc = first[source][target]
        path.append(arc)
        source = arc.head
        if source in visited:
            raise AssertionError("tight arcs contain a zero-length directed cycle")
        visited.add(source)
    return tuple(path)


def _sparsify(nodes, demands, first, last):
    """Store short paths and complete shortest-path trees at greedy hubs."""
    paths = {key: _path(s, t, first)
             for key, (s, t) in demands.items()}
    routes, hubs, phases = {}, [], 0
    remaining = dict(paths)
    while remaining:
        phases += 1
        p = len(remaining)
        # Exact ceil(nodes/sqrt(p)), avoiding floating-point threshold errors.
        threshold = isqrt((nodes * nodes + p - 1) // p)
        if threshold * threshold * p < nodes * nodes:
            threshold += 1
        for key, path in tuple(remaining.items()):
            if len(path) <= threshold:
                s, t = demands[key]
                routes[key] = _Route(s, t, path, None)
                del remaining[key]
        # One phase uses at most ceil(nodes/threshold) hubs. Keep unhit long
        # demands for the next geometrically smaller phase.
        for _ in range((nodes + threshold - 1) // threshold):
            if not remaining:
                break
            counts = [0] * nodes
            for path in remaining.values():
                for vertex in {path[0].tail, *(a.head for a in path)}:
                    counts[vertex] += 1
            hub = max(range(nodes), key=lambda v: (counts[v], -v))
            incoming = {v: first[v][hub] for v in range(nodes)
                        if v != hub and first[v][hub] is not None}
            outgoing_tree = {v: last[hub][v] for v in range(nodes)
                             if v != hub and last[hub][v] is not None}
            index = len(hubs)
            hubs.append(_Hub(hub, incoming, outgoing_tree))
            for key, path in tuple(remaining.items()):
                if hub == path[0].tail or any(a.head == hub for a in path):
                    routes[key] = _Route(*demands[key], None, index)
                    del remaining[key]
    return routes, tuple(hubs), phases


def _graph_input(n, root, arcs):
    """Shared validation for the supplied-baseline and initialized graph APIs."""
    if type(n) is not int or n < 1 or type(root) is not int or not 0 <= root < n:
        raise ValueError("invalid graph size or root")
    checked = []
    for arc in arcs:
        if (not isinstance(arc, Arc) or type(arc.tail) is not int
                or type(arc.head) is not int or not 0 <= arc.tail < n
                or not 0 <= arc.head < n
                or type(arc.cost) not in (int, Fraction) or arc.cost < 0):
            raise ValueError("invalid arc or nonnegative exact cost")
        checked.append(Arc(arc.tail, arc.head, Fraction(arc.cost)))
    return tuple(checked)


def build(n: int, root: int, arcs, baseline) -> Oracle:
    """Build from a promised optimal baseline; IDs are input-list positions.

    Costs are nonnegative integers/Fractions. Loops and arcs entering root
    are validated then ignored. Parallel arcs keep separate original IDs.
    Shape validation is unconditional; optimum baseline supply is a caller
    obligation (negative exchange cycles are defensively rejected).
    """
    arcs = _graph_input(n, root, arcs)
    baseline = tuple(baseline)
    if (len(baseline) != n - 1 or len(set(baseline)) != len(baseline)
            or any(type(i) is not int or not 0 <= i < len(arcs) for i in baseline)):
        raise ValueError("invalid baseline identifiers or size")
    reached, heads = {root}, set()
    for i in baseline:
        arc = arcs[i]
        if arc.head == root or arc.head in heads or arc.tail == arc.head:
            raise ValueError("baseline is not a rooted spanning arborescence")
        heads.add(arc.head)
    for _ in range(n):
        reached.update(arcs[i].head for i in baseline if arcs[i].tail in reached)
    if len(reached) != n:
        raise ValueError("baseline is not root-spanning")
    baseline_cost = sum((arcs[i].cost for i in baseline), Fraction(0))
    nodes, auxiliary, minus, plus = _auxiliary(n, root, arcs, baseline)
    return _finish(baseline, baseline_cost, nodes, auxiliary, minus, plus)


def _finish(baseline, baseline_cost, nodes, auxiliary, minus, plus):
    """Canonical final reporter for either auxiliary or compressed exchanges."""
    distance, first, last = _distances(nodes, auxiliary)
    demands = {i: (plus[i], minus[i]) for i in baseline
               if distance[plus[i]][minus[i]] is not None}
    routes, hubs, phases = _sparsify(nodes, demands, first, last)
    values = {}
    for i in baseline:
        if i not in routes:
            routes[i] = None
            values[i] = None
        else:
            values[i] = baseline_cost + distance[plus[i]][minus[i]][0]
    retained = set(baseline)
    for route in routes.values():
        if route is not None and route.explicit is not None:
            retained.update(a.label for a in route.explicit if a.label is not None)
    for hub in hubs:
        retained.update(a.label for a in (*hub.incoming.values(), *hub.outgoing.values())
                        if a.label is not None)
    return Oracle(baseline, baseline_cost, routes, hubs, tuple(sorted(retained)),
                  values, nodes, len(auxiliary), phases)
