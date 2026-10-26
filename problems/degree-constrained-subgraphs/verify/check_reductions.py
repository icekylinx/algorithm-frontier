#!/usr/bin/env python3
"""Finite, independent checks of the sparse degree-factor reductions.

Local selector gadgets are checked by bipartite augmenting paths. Hub/parity
and cardinality gadgets are checked by exhaustive degree-state search on the
actual augmented multigraph and compared with enumerated original edge sets.
No conditional matching backend is called. Requires the standard library.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product


def permutation_network(s: int):
    next_position = 0
    arcs: list[tuple[int, int]] = []

    def allocate(count: int):
        nonlocal next_position
        block = list(range(next_position, next_position + count))
        next_position += count
        return block

    def build(size: int):
        if size == 1:
            only = allocate(1)
            return only, only
        inputs, outputs = allocate(size), allocate(size)
        upper_in, upper_out = build(size // 2)
        lower_in, lower_out = build(size // 2)
        for i in range(size // 2):
            for port in inputs[2 * i:2 * i + 2]:
                arcs.extend(((port, upper_in[i]), (port, lower_in[i])))
            for port in outputs[2 * i:2 * i + 2]:
                arcs.extend(((upper_out[i], port), (lower_out[i], port)))
        return inputs, outputs

    inputs, outputs = build(s)
    indegree, outdegree = [0] * next_position, [0] * next_position
    for u, v in arcs:
        outdegree[u] += 1
        indegree[v] += 1
    assert max(indegree) <= 2 and max(outdegree) <= 2
    assert all(indegree[u] == 0 for u in inputs)
    assert all(outdegree[u] == 0 for u in outputs)
    return next_position, arcs, inputs, outputs


def selector_has_perfect_matching(network, input_mask: int, output_mask: int):
    size, arcs, inputs, outputs = network
    chosen = [u for i, u in enumerate(inputs) if input_mask & (1 << i)]
    sinks = [u for i, u in enumerate(outputs) if output_mask & (1 << i)]
    # Left: position-out endpoints and actual attached ports.
    # Right: position-in endpoints and selected degree-one sinks.
    adjacency = [[u] for u in range(size)]
    for u, v in arcs:
        adjacency[u].append(v)
    for j, u in enumerate(sinks):
        adjacency[u].append(size + j)
    adjacency.extend([[u] for u in chosen])
    if len(adjacency) != size + len(sinks):
        return False
    matched = [-1] * (size + len(sinks))

    def augment(u: int, seen: set[int]):
        for v in adjacency[u]:
            if v in seen:
                continue
            seen.add(v)
            if matched[v] < 0 or augment(matched[v], seen):
                matched[v] = u
                return True
        return False

    return all(augment(u, set()) for u in range(len(adjacency)))


def factor_exists(n: int, edges: list[tuple[int, int]], degrees: list[int]):
    """Exact edge-subset search, independent of the matching reductions."""
    suffix = [[0] * n for _ in range(len(edges) + 1)]
    for i in range(len(edges) - 1, -1, -1):
        suffix[i] = suffix[i + 1].copy()
        u, v = edges[i]
        suffix[i][u] += 1
        suffix[i][v] += 1

    @lru_cache(maxsize=None)
    def visit(i: int, remaining: tuple[int, ...]):
        if any(x < 0 or x > suffix[i][v] for v, x in enumerate(remaining)):
            return False
        if i == len(edges):
            return all(x == 0 for x in remaining)
        if visit(i + 1, remaining):
            return True
        u, v = edges[i]
        reduced = list(remaining)
        reduced[u] -= 1
        reduced[v] -= 1
        return visit(i + 1, tuple(reduced))

    return visit(0, tuple(degrees))


def interval_to_factor(n, edges, lower, upper):
    """Construct the literal dummy-edge and triangle multigraph."""
    hub = n
    deficit = sum(f - g for g, f in zip(lower, upper))
    target = deficit + ((sum(upper) - deficit) % 2)
    augmented = list(edges)
    degrees = [*upper, target]
    for v, (g, f) in enumerate(zip(lower, upper)):
        augmented.extend([(v, hub)] * (f - g))
    for _ in range(target // 2):
        p = len(degrees)
        q = p + 1
        degrees.extend((1, 1))
        augmented.extend(((hub, p), (p, q), (q, hub)))
    return len(degrees), augmented, degrees


def cardinality_to_factor(n, edges, lower, upper, low, high):
    if low > high:
        return None
    deficit = sum(f - g for g, f in zip(lower, upper))
    total = sum(upper)
    hub_low, hub_high = max(0, total - 2 * high), min(deficit, total - 2 * low)
    if hub_low > hub_high:
        return None
    augmented = list(edges)
    for v, (g, f) in enumerate(zip(lower, upper)):
        augmented.extend([(v, n)] * (f - g))
    return interval_to_factor(
        n + 1, augmented, [*upper, hub_low], [*upper, hub_high]
    )


def original_subsets(n, edges):
    output = []
    for mask in range(1 << len(edges)):
        degrees = [0] * n
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                degrees[u] += 1
                degrees[v] += 1
        output.append((mask.bit_count(), degrees))
    return output


def main():
    assert __debug__, "run without -O"
    selector_cases = interval_cases = cardinality_cases = 0
    for s in (1, 2, 4):
        network = permutation_network(s)
        for left in range(1 << s):
            for right in range(1 << s):
                assert selector_has_perfect_matching(network, left, right) == (
                    left.bit_count() == right.bit_count()
                )
                selector_cases += 1
    network = permutation_network(8)
    for left in range(1 << 8):
        for count in range(9):
            right = (1 << count) - 1
            assert selector_has_perfect_matching(network, left, right) == (
                left.bit_count() == count
            )
            selector_cases += 1

    graphs = []
    for n in range(4):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            graphs.append((n, [e for i, e in enumerate(possible) if mask & (1 << i)]))
    # Explicit parallel records are distinct selectable edges.
    graphs.extend(((2, [(0, 1), (0, 1)]), (3, [(0, 1), (0, 1), (1, 2)])))
    for n, edges in graphs:
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        options = [[(g, f) for f in range(d + 1) for g in range(f + 1)] for d in degree]
        subsets = original_subsets(n, edges)
        for intervals in product(*options):
            lower = [g for g, _ in intervals]
            upper = [f for _, f in intervals]
            feasible_sizes = {
                size for size, values in subsets
                if all(g <= d <= f for g, d, f in zip(lower, values, upper))
            }
            assert factor_exists(*interval_to_factor(n, edges, lower, upper)) == bool(feasible_sizes)
            interval_cases += 1
            for low in range(len(edges) + 1):
                for high in range(low, len(edges) + 1):
                    gadget = cardinality_to_factor(n, edges, lower, upper, low, high)
                    actual = gadget is not None and factor_exists(*gadget)
                    assert actual == any(low <= size <= high for size in feasible_sizes)
                    cardinality_cases += 1

    print(f"Sparse selector: {selector_cases} attachment/output cases.")
    print(f"Hub/parity: {interval_cases} interval-degree multigraph cases.")
    print(f"Prescribed/ranged cardinality: {cardinality_cases} exact reductions.")
    print("PASS: finite gadget evidence; no fast-matching-backend claim.")


if __name__ == "__main__":
    main()
