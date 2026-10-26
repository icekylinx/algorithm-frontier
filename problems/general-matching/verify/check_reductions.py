#!/usr/bin/env python3
"""Independent finite checks of the elementary matching reductions.

Uses exhaustive matching enumeration/dynamic programming, not the conditional
fast matching backend. All simple graphs through six vertices are checked for
the c-neighbor kernel in both forward and reverse edge order. All graphs
through four vertices are checked for the odd-path degree reduction, including
the decoder inequality for every matching of every resulting gadget.
Mixed native vertex/edge failures of budgets one and two are also checked
on all graphs through four vertices, in both fixed edge orders.

This finite evidence does not prove the general lemmas or Contract R.
Requires only the Python standard library; run with assertions enabled.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations


def matching_number(n: int, edges: list[tuple[int, int]]) -> int:
    adjacency = [0] * n
    for u, v in edges:
        assert u != v
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    @lru_cache(maxsize=None)
    def solve(mask: int) -> int:
        if not mask:
            return 0
        bit = mask & -mask
        u = bit.bit_length() - 1
        rest = mask ^ bit
        best = solve(rest)
        options = adjacency[u] & rest
        while options:
            other = options & -options
            options ^= other
            best = max(best, 1 + solve(rest ^ other))
        return best

    return solve((1 << n) - 1)


def kernel(n: int, edges: list[tuple[int, int]], failure_budget: int = 0) -> list[tuple[int, int]]:
    covered: set[int] = set()
    for u, v in edges:
        if u not in covered and v not in covered:
            covered.update((u, v))
    retained: list[tuple[int, int]] = []
    seen = {u: set() for u in covered}
    for u, v in edges:
        if u in covered and v in covered:
            retained.append((u, v))
        else:
            if u not in covered:
                u, v = v, u
            assert u in covered and v not in covered
            if len(seen[u]) < len(covered) + failure_budget and v not in seen[u]:
                seen[u].add(v)
                retained.append((u, v))
    c = len(covered)
    assert len(retained) <= min(len(edges), c * (c - 1) // 2 + c * (c + failure_budget))
    return retained


def odd_path_reduction(n: int, edges: list[tuple[int, int]]):
    incidences = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(edges):
        incidences[u].append(edge_id)
        incidences[v].append(edge_id)
    ports: dict[tuple[int, int], int] = {}
    gadget: list[tuple[int, int]] = []
    original: dict[int, tuple[int, int]] = {}
    size = offset = 0
    for u, incident in enumerate(incidences):
        d = len(incident)
        if not d:
            continue
        offset += d - 1
        for j, edge_id in enumerate(incident):
            ports[u, edge_id] = size + 2 * j
        gadget.extend((size + j, size + j + 1) for j in range(2 * d - 2))
        size += 2 * d - 1
    for edge_id, (u, v) in enumerate(edges):
        original[len(gadget)] = (u, v)
        gadget.append((ports[u, edge_id], ports[v, edge_id]))
    degrees = [0] * size
    for u, v in gadget:
        degrees[u] += 1
        degrees[v] += 1
    assert max(degrees, default=0) <= 3
    assert size == 4 * len(edges) - sum(bool(x) for x in incidences)
    return size, gadget, original, offset


def all_matchings(n: int, edges: list[tuple[int, int]]):
    incident = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(edges):
        incident[u].append((v, edge_id))
        incident[v].append((u, edge_id))

    def visit(mask: int, chosen: tuple[int, ...]):
        if not mask:
            yield chosen
            return
        bit = mask & -mask
        u = bit.bit_length() - 1
        rest = mask ^ bit
        yield from visit(rest, chosen)
        for v, edge_id in incident[u]:
            if rest & (1 << v):
                yield from visit(rest ^ (1 << v), (*chosen, edge_id))

    yield from visit((1 << n) - 1, ())


def decode(n: int, original_edges: list[tuple[int, int]]):
    incident = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(original_edges):
        incident[u].append((v, edge_id))
        incident[v].append((u, edge_id))
    seen: set[int] = set()
    output: list[tuple[int, int]] = []
    for root in range(n):
        if root in seen or not incident[root]:
            continue
        stack, vertices, component_edges = [root], set(), set()
        while stack:
            u = stack.pop()
            if u in seen:
                continue
            seen.add(u)
            vertices.add(u)
            for v, edge_id in incident[u]:
                component_edges.add(edge_id)
                if v not in seen:
                    stack.append(v)
        if len(component_edges) == len(vertices) - 1:
            output.append(original_edges[min(component_edges)])
    endpoints = [v for edge in output for v in edge]
    assert len(endpoints) == len(set(endpoints))
    return output


def main() -> None:
    assert __debug__, "run without -O"
    kernel_cases = gadget_cases = decoder_cases = mixed_failure_cases = 0
    for n in range(7):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [e for i, e in enumerate(possible) if mask & (1 << i)]
            optimum = matching_number(n, edges)
            for ordered in (edges, edges[::-1]):
                assert matching_number(n, kernel(n, ordered)) == optimum
                kernel_cases += 1
            if n > 4:
                continue
            fault_items = [("vertex", v) for v in range(n)] + [
                ("edge", edge_id) for edge_id in range(len(edges))
            ]
            for budget in (1, 2):
                for ordered in (edges, edges[::-1]):
                    retained = {tuple(sorted(e)) for e in kernel(n, ordered, budget)}
                    for count in range(budget + 1):
                        for faults in combinations(fault_items, count):
                            failed_vertices = {v for kind, v in faults if kind == "vertex"}
                            failed_edges = {e for kind, e in faults if kind == "edge"}
                            surviving = [
                                e for i, e in enumerate(edges)
                                if i not in failed_edges and not failed_vertices.intersection(e)
                            ]
                            surviving_kernel = [e for e in surviving if tuple(sorted(e)) in retained]
                            assert matching_number(n, surviving) == matching_number(n, surviving_kernel)
                            mixed_failure_cases += 1
            size, gadget, cross_edges, offset = odd_path_reduction(n, edges)
            assert matching_number(size, gadget) == offset + optimum
            gadget_cases += 1
            for matching in all_matchings(size, gadget):
                external = [cross_edges[e] for e in matching if e in cross_edges]
                decoded = decode(n, external)
                assert len(decoded) >= len(matching) - offset
                assert len(decoded) <= optimum
                decoder_cases += 1

    for c in (2, 4, 6):
        internal = [(i, i + 1) for i in range(0, c, 2)]
        original = internal + [(u, c + v) for u in range(c) for v in range(c)]
        insufficient = internal + [
            (u, c + v) for u in range(c) for v in range(c - 1)
        ]
        assert matching_number(2 * c, original) == c
        assert matching_number(2 * c, insufficient) == c - 1
        assert matching_number(2 * c, kernel(2 * c, original)) == c

    for c, budget in ((2, 1), (2, 2), (4, 1), (4, 2)):
        internal = [(i, i + 1) for i in range(0, c, 2)]
        original = internal + [(u, c + v) for u in range(c) for v in range(c + budget)]
        insufficient = internal + [(u, c + v) for u in range(c) for v in range(c + budget - 1)]
        failed = set(range(c, c + budget))
        after = lambda es: [e for e in es if not failed.intersection(e)]
        assert matching_number(2 * c + budget, after(original)) == c
        assert matching_number(2 * c + budget, after(insufficient)) == c - 1
        assert matching_number(2 * c + budget, after(kernel(2 * c + budget, original, budget))) == c

    print(f"Kernel: {kernel_cases} ordered graph cases, all graphs through n=6.")
    print(f"Subcubic gadget: {gadget_cases} graphs, all graphs through n=4.")
    print(f"Decoder: all {decoder_cases} gadget matchings; 3 sharp-cutoff examples.")
    print(f"Mixed vertex/edge faults: {mixed_failure_cases} cases; 4 sharp-cutoff examples.")
    print("PASS: finite reductions only; no Contract R or fast-backend claim.")


if __name__ == "__main__":
    main()
