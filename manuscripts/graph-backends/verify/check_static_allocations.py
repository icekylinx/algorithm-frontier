#!/usr/bin/env python3
"""Finite independent checks for two restored static allocation theorems.

The reference routines explicitly list paths/cycles and may repeatedly scan
the whole graph. They are deliberately ordinary polynomial finite-test
implementations, not implementations or certifications of near-linear
dynamic-tree bounds. Validation recomputes native-record divergences,
row/column margins, selected components, and injection conditions directly.
"""
from __future__ import annotations

from collections import deque
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import random

if not __debug__:
    raise SystemExit("Run mathematical verification without python -O.")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def divergences(n, arcs, values):
    result = [0] * n
    for (u, v), value in zip(arcs, values):
        result[u] += value
        result[v] -= value
    return result


def directed_cycle(n, arcs, values):
    adjacency = [[] for _ in range(n)]
    for edge, ((u, v), value) in enumerate(zip(arcs, values)):
        if value:
            adjacency[u].append((v, edge))
    color, position = [0] * n, {}
    vertices, edges = [], []

    def visit(u):
        color[u] = 1
        position[u] = len(vertices)
        vertices.append(u)
        for v, edge in adjacency[u]:
            if color[v] == 1:
                return edges[position[v]:] + [edge]
            if color[v] == 0:
                edges.append(edge)
                found = visit(v)
                if found is not None:
                    return found
                edges.pop()
        vertices.pop()
        del position[u]
        color[u] = 2
        return None

    for vertex in range(n):
        if color[vertex] == 0:
            found = visit(vertex)
            if found is not None:
                return found
    return None


def trim_explicit(n, arcs, supplied, targets, sinks):
    """Simple monotone directed-cycle cancellation and explicit path trimming."""
    values = list(supplied)
    require(len(arcs) == len(values), "arc/value size")
    require(set(targets) == set(range(n)) - set(sinks), "nonsink targets")
    require(all(type(x) is int and x >= 0 for x in values), "integral flow")
    require(all(type(w) is int and w > 0 for w in targets.values()), "positive targets")
    before = divergences(n, arcs, values)
    require(all(before[v] >= w for v, w in targets.items()), "feasible supplied divergences")
    for edge, (u, _) in enumerate(arcs):
        if u in sinks:
            values[edge] = 0
    clipped = divergences(n, arcs, values)
    require(all(clipped[v] >= before[v] for v in targets), "outgoing sink clipping")
    cycles = 0
    while (cycle := directed_cycle(n, arcs, values)) is not None:
        old_divergence = divergences(n, arcs, values)
        amount = min(values[edge] for edge in cycle)
        require(amount > 0, "positive cycle bottleneck")
        for edge in cycle:
            values[edge] -= amount
        require(divergences(n, arcs, values) == old_divergence, "cycle conservation")
        cycles += 1
    paths = 0
    for start, target in sorted(targets.items()):
        excess = divergences(n, arcs, values)[start] - target
        while excess:
            adjacency = [[] for _ in range(n)]
            for edge, ((u, v), value) in enumerate(zip(arcs, values)):
                if value:
                    adjacency[u].append((v, edge))
            parent = {start: None}
            queue = deque([start])
            finish = None
            while queue:
                u = queue.popleft()
                if u in sinks:
                    finish = u
                    break
                for v, edge in adjacency[u]:
                    if v not in parent:
                        parent[v] = (u, edge)
                        queue.append(v)
            require(finish is not None, "positive supply must reach a sink")
            path = []
            vertex = finish
            while vertex != start:
                vertex, edge = parent[vertex]
                path.append(edge)
            amount = min(excess, min(values[edge] for edge in path))
            for edge in path:
                values[edge] -= amount
            excess -= amount
            paths += 1
    require(cycles + paths <= len(arcs) + len(targets), "permanent-deletion/exhaustion event count")
    return values, cycles, paths


def verify_trim(n, arcs, supplied, targets, sinks):
    result, cycles, paths = trim_explicit(n, arcs, supplied, targets, sinks)
    require(len(result) == len(supplied), "original flow-record count")
    require(all(type(v) is int and 0 <= v <= old for v, old in zip(result, supplied)),
            "integrality and coordinatewise input domination")
    actual = divergences(n, arcs, result)
    require(all(actual[v] == target for v, target in targets.items()),
            "exact original nonsink divergences")
    require(all(result[e] == 0 for e, (u, _) in enumerate(arcs) if u in sinks),
            "all outgoing sink records removed")
    return cycles, paths


def undirected_cycle(rows, bins, allocation):
    adjacency = [[] for _ in range(rows + bins)]
    for (row, bin_), amount in allocation.items():
        if amount:
            edge = (row, bin_)
            adjacency[row].append((rows + bin_, edge))
            adjacency[rows + bin_].append((row, edge))
    color, position = [0] * (rows + bins), {}
    vertices, edges = [], []

    def visit(u, previous):
        color[u] = 1
        position[u] = len(vertices)
        vertices.append(u)
        for v, edge in adjacency[u]:
            if edge == previous:
                continue
            if color[v] == 1:
                return edges[position[v]:] + [edge]
            if color[v] == 0:
                edges.append(edge)
                found = visit(v, edge)
                if found is not None:
                    return found
                edges.pop()
        vertices.pop()
        del position[u]
        color[u] = 2
        return None

    for u in range(rows + bins):
        if color[u] == 0:
            found = visit(u, None)
            if found is not None:
                return found
    return None


def transportation_forest(rows, bins, total, records, tie):
    """Explicit cycle cancellation plus the general-rank child-pair rule."""
    allocation, witness = {}, {}
    for native_id, (row, bin_, amount) in enumerate(records):
        key = (row, bin_)
        allocation[key] = allocation.get(key, 0) + amount
        witness.setdefault(key, native_id)
    cycles = 0
    while (cycle := undirected_cycle(rows, bins, allocation)) is not None:
        require(len(cycle) % 2 == 0, "bipartite support cycle")
        amount = min(allocation[edge] for edge in cycle[::2])
        require(amount > 0, "transportation bottleneck")
        for index, edge in enumerate(cycle):
            allocation[edge] += amount if index % 2 else -amount
        cycles += 1
    adjacency = [[] for _ in range(rows + bins)]
    for (row, bin_), amount in allocation.items():
        if amount:
            adjacency[row].append(rows + bin_)
            adjacency[rows + bin_].append(row)
    parent = {}
    roots = sorted(range(bins), key=lambda b: (b - tie) % max(1, bins))
    for root in roots:
        root += rows
        if root in parent:
            continue
        parent[root] = None
        stack = [root]
        while stack:
            u = stack.pop()
            for v in adjacency[u]:
                if v not in parent:
                    parent[v] = u
                    stack.append(v)
    selected = []
    for row in range(rows):
        neighbors = sorted(v - rows for v in adjacency[row])
        require(len(neighbors) >= 2, "positive weight excludes degree-one rows")
        if len(neighbors) == 2:
            first, second = neighbors
        else:
            children = [v for v in neighbors if rows + v != parent[row]]
            pairs = list(combinations(children, 2))
            first, second = pairs[tie % len(pairs)]
        selected.append((first, second, witness[(row, first)], witness[(row, second)]))
    bin_adjacency = [[] for _ in range(bins)]
    for row, (u, v, _, _) in enumerate(selected):
        bin_adjacency[u].append((v, row))
        bin_adjacency[v].append((u, row))
    seen, assignment = set(), {}
    for root in roots:
        if root in seen:
            continue
        seen.add(root)
        stack = [root]
        while stack:
            u = stack.pop()
            for v, row in bin_adjacency[u]:
                if v not in seen:
                    assignment[row] = v
                    seen.add(v)
                    stack.append(v)
    return allocation, selected, assignment, cycles


def components(adjacency):
    visited = set()
    result = []
    for start in range(len(adjacency)):
        if start in visited:
            continue
        visited.add(start)
        group, stack = [], [start]
        while stack:
            u = stack.pop()
            group.append(u)
            for v in adjacency[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        edges = sum(len(adjacency[u]) for u in group) // 2
        result.append((group, edges))
    return result


def verify_transport(rows, bins, total, weights, records, tie):
    row_before, col_before = [0] * rows, [0] * bins
    for row, bin_, amount in records:
        require(type(amount) is int and amount >= 0, "nonnegative integral input allocation")
        row_before[row] += amount
        col_before[bin_] += amount
    require(row_before == [total] * rows, "input row margins")
    require(all(w > 0 and load <= total - w for w, load in zip(weights, col_before)),
            "strict input column capacities")
    allocation, selected, assignment, cycles = transportation_forest(rows, bins, total, records, tie)
    row_after, col_after = [0] * rows, [0] * bins
    support = [[] for _ in range(rows + bins)]
    for (row, bin_), amount in allocation.items():
        require(type(amount) is int and 0 <= amount <= total, "bounded integral private allocation")
        row_after[row] += amount
        col_after[bin_] += amount
        if amount:
            support[row].append(rows + bin_)
            support[rows + bin_].append(row)
    require(row_after == row_before and col_after == col_before, "both transportation margins preserved")
    require(all(edges == len(group) - 1 for group, edges in components(support)),
            "positive allocation support is a forest")
    require(len(selected) == rows and set(assignment) == set(range(rows)), "every row represented")
    require(len(set(assignment.values())) == rows, "row assignment is injective")
    chosen = [[] for _ in range(bins)]
    for row, (u, v, first_id, second_id) in enumerate(selected):
        require(u != v and records[first_id][:2] == (row, u)
                and records[second_id][:2] == (row, v), "distinct genuine native incidence witnesses")
        require(assignment[row] in (u, v), "assignment follows its selected pair")
        chosen[u].append(v)
        chosen[v].append(u)
    groups = components(chosen)
    require(len(groups) == bins - rows, "exact number of free roots")
    for group, edges in groups:
        require(edges == len(group) - 1, "selected bin graph is a forest")
        require(sum(weights[v] for v in group) < 2 * total, "strict arbitrary-rank component weight")
    initial_rank = max((len({b for rr, b, value in records if rr == r and value})
                        for r in range(rows)), default=0)
    isolated = sum(not neighbors for neighbors in support[rows:])
    return cycles, initial_rank, isolated, max((sum(weights[v] for v in group)
                                               for group, _ in groups), default=0)


def main():
    rng = random.Random(20261024)
    counts = dict(flow_exhaustive=0, flow_seeded=0, flow_cycles=0, flow_paths=0,
                  flow_loops=0, flow_parallel=0, flow_antiparallel=0, flow_sink_outgoing=0,
                  transport_exhaustive=0, transport_seeded=0, transport_cycles=0,
                  rank_above_three=0, isolated_bin_instances=0, maximum_row_rank=0,
                  tight_two_L_minus_two=0)

    def flow_case(n, arcs, flow, targets, sinks, kind):
        cycles, paths = verify_trim(n, arcs, flow, targets, sinks)
        counts[kind] += 1
        counts["flow_cycles"] += cycles
        counts["flow_paths"] += paths
        counts["flow_loops"] += any(u == v and flow[i] for i, (u, v) in enumerate(arcs))
        counts["flow_parallel"] += len(set(arcs)) < len(arcs)
        records = set(arcs)
        counts["flow_antiparallel"] += any(u != v and (v, u) in records for u, v in records)
        counts["flow_sink_outgoing"] += any(u in sinks and flow[i] for i, (u, _) in enumerate(arcs))

    flow_case(0, [], [], {}, set(), "flow_exhaustive")
    native = [(0, 1), (0, 1), (1, 0), (0, 0), (1, 1)]
    for values in product(range(3), repeat=len(native)):
        divergence = divergences(2, native, values)[0]
        for target in range(1, divergence + 1):
            flow_case(2, native, values, {0: target}, {1}, "flow_exhaustive")
    for _ in range(1000):
        n = rng.randrange(2, 11)
        sinks = set(rng.sample(range(n), rng.randrange(1, n + 1)))
        nonsinks = sorted(set(range(n)) - sinks)
        arcs, values = [], []

        def add(u, v, amount):
            existing = [i for i, edge in enumerate(arcs) if edge == (u, v)]
            if existing and rng.randrange(2):
                values[rng.choice(existing)] += amount
            else:
                arcs.append((u, v))
                values.append(amount)

        for start in nonsinks:
            middle = rng.sample([v for v in nonsinks if v != start], rng.randrange(len(nonsinks)))
            path = [start] + middle + [rng.choice(sorted(sinks))]
            amount = rng.randrange(1, 7)
            for u, v in zip(path, path[1:]):
                add(u, v, amount)
        for _ in range(rng.randrange(1, 8)):
            cycle = rng.sample(range(n), rng.randrange(1, n + 1))
            amount = rng.randrange(1, 5)
            for u, v in zip(cycle, cycle[1:] + cycle[:1]):
                add(u, v, amount)
        for _ in range(3):
            add(rng.randrange(n), rng.randrange(n), 0)
        div = divergences(n, arcs, values)
        targets = {v: rng.randrange(1, div[v] + 1) for v in nonsinks}
        flow_case(n, arcs, values, targets, sinks, "flow_seeded")

    def transport_case(rows, bins, total, weights, records, tie, kind):
        cycles, rank, isolated, largest = verify_transport(rows, bins, total, weights, records, tie)
        counts[kind] += 1
        counts["transport_cycles"] += cycles
        counts["rank_above_three"] += rank > 3
        counts["maximum_row_rank"] = max(counts["maximum_row_rank"], rank)
        counts["isolated_bin_instances"] += isolated > 0
        counts["tight_two_L_minus_two"] += total > 1 and largest == 2 * total - 2

    for rows, bins, total in [(0, 0, 1), (0, 3, 2), (1, 3, 2), (1, 4, 4), (2, 3, 3)]:
        for values in product(range(total + 1), repeat=rows * bins):
            if any(sum(values[r * bins:(r + 1) * bins]) != total for r in range(rows)):
                continue
            columns = [sum(values[r * bins + b] for r in range(rows)) for b in range(bins)]
            if any(value >= total for value in columns):
                continue
            records = [(r, b, values[r * bins + b]) for r in range(rows) for b in range(bins)]
            for tie in (0, 3):
                transport_case(rows, bins, total, [total - x for x in columns],
                               records, tie, "transport_exhaustive")
    transport_case(1, 6, 6, [5] * 6, [(0, b, 1) for b in range(6)],
                   2, "transport_exhaustive")
    for _ in range(1500):
        bins, total = rng.randrange(1, 10), rng.randrange(2, 13)
        rows = rng.randrange(min(bins - 1, bins * (total - 1) // total) + 1)
        residual = [total - 1] * bins
        allocation = [[0] * bins for _ in range(rows)]
        for row in range(rows):
            for _ in range(total):
                bin_ = rng.choice([b for b in range(bins) if residual[b]])
                allocation[row][bin_] += 1
                residual[bin_] -= 1
        weights = [rng.randrange(1, remaining + 2) for remaining in residual]
        records = []
        for row in range(rows):
            for bin_, amount in enumerate(allocation[row]):
                if rng.randrange(2):
                    first = rng.randrange(amount + 1)
                    records.extend([(row, bin_, first), (row, bin_, amount - first)])
                else:
                    records.append((row, bin_, amount))
        rng.shuffle(records)
        transport_case(rows, bins, total, weights, records, rng.randrange(100),
                       "transport_seeded")
    require(all(counts[key] > 0 for key in ("flow_cycles", "flow_paths", "flow_loops",
                  "flow_parallel", "flow_antiparallel", "flow_sink_outgoing",
                  "transport_cycles", "rank_above_three", "isolated_bin_instances",
                  "tight_two_L_minus_two")), "required coverage")
    print(json.dumps(dict(status="PASS", counts=counts,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope="Finite integral native-flow and transportation cases; explicit polynomial reference routines and independent output checks, not near-linear dynamic-tree implementations or arbitrary-size theorem certification."),
        sort_keys=True))


if __name__ == "__main__":
    main()
