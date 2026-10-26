#!/usr/bin/env python3
"""Finite oracle checks of bipartite matching and linear optimality certificates.

The matching oracle independently enumerates possibilities for a remaining
vertex.  It uses no augmenting paths, layers, vertex covers, or compression.
All bipartite graphs with at most four vertices on each side are checked.
Larger native-record and long-path cases use the separate certificate
verifier, whose matching and odd-component checks do not call this solver.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import sys
from functools import lru_cache
from pathlib import Path

REFERENCE = Path(__file__).resolve().parents[1] / "reference"
sys.path.insert(0, str(REFERENCE))
from matching import (  # noqa: E402
    _bipartite_barrier, _bipartition, _hopcroft_karp, maximum_matching,
)
from verify_certificate import verify_result  # noqa: E402


def oracle(n: int, edges: list[tuple[int, int]]) -> int:
    adjacency = [0] * n
    for u, v in edges:
        if u != v:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u

    @lru_cache(maxsize=None)
    def solve(mask: int) -> int:
        if not mask:
            return 0
        bit = mask & -mask
        u = bit.bit_length() - 1
        rest = mask ^ bit
        result = solve(rest)
        choices = adjacency[u] & rest
        while choices:
            next_bit = choices & -choices
            choices ^= next_bit
            result = max(result, 1 + solve(rest ^ next_bit))
        return result
    return solve((1 << n) - 1)


def check(n: int, edges: list[tuple[int, int]], left: list[bool]) -> tuple[int, int]:
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    assert _bipartition(adjacency) is not None
    statistics: dict[str, int] = {}
    mate = _hopcroft_karp(adjacency, left, statistics=statistics)
    expected = oracle(n, edges)
    assert sum(u < v for u, v in enumerate(mate)) == expected
    for u, v in enumerate(mate):
        assert v == -1 or (v in adjacency[u] and mate[v] == u and left[u] != left[v])
    barrier = _bipartite_barrier(adjacency, mate, left)
    removed = set(barrier)
    assert len(removed) == len(barrier) == expected
    assert all(u in removed or v in removed for u, v in edges)
    # Every surviving vertex is a singleton odd component, giving the same
    # certificate equality used by the independent public verifier.
    assert 2 * expected == n - (n - len(barrier)) + len(barrier)
    phases = statistics.get("hopcroft_karp_phases", 0)
    assert statistics["hopcroft_karp_calls"] == 1
    assert statistics["hopcroft_karp_bfs"] == phases + 1
    assert statistics.get("hopcroft_karp_augmentations", 0) == expected
    bound = 2 * math.isqrt(expected)
    if math.isqrt(expected) ** 2 != expected:
        bound += 2
    assert phases <= bound if expected else phases == 0
    return phases, expected


def rejection_checks() -> int:
    cases = [
        (_hopcroft_karp, ([[1], [0]], [True])),
        (_hopcroft_karp, ([[1], [0]], [True, True])),
        (_bipartite_barrier, ([[1], [0]], [-1, -1], [True, False])),
        (_bipartite_barrier, ([[1], [0]], [1, -1], [True, False])),
        (_bipartite_barrier, ([[1], [0]], [2, 0], [True, False])),
        (_bipartite_barrier, ([[1], [0]], [1, 0], [True, True])),
        (_bipartite_barrier, ([[1], [0]], [1], [True, False])),
    ]
    for function, arguments in cases:
        try:
            function(*arguments)
        except RuntimeError:
            pass
        else:
            raise AssertionError((function.__name__, arguments))
    assert _bipartition([[1, 2], [0, 2], [0, 1]]) is None
    return len(cases) + 1


def large_and_native_cases() -> int:
    # The first phase greedily leaves the last left and last right vertices
    # free.  Its only augmenting path then has 2*depth+1 graph edges.  The
    # explicit stack must work well beyond Python's recursion limit.
    depth = 2400
    side = depth + 1
    edges = [(u, side + u) for u in range(depth)]
    edges += [(u, side + u + 1) for u in range(depth)]
    edges.append((depth, side))
    adjacency = [[] for _ in range(2 * side)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    statistics: dict[str, int] = {}
    mate = _hopcroft_karp(adjacency, [True] * side + [False] * side,
                          statistics=statistics)
    assert sum(u < v for u, v in enumerate(mate)) == side
    assert statistics["hopcroft_karp_phases"] == 2
    assert statistics["hopcroft_karp_bfs"] == 3
    result = maximum_matching(2 * side, edges, use_kernel=False, certificate=True)
    assert result["cardinality"] == side
    assert result["statistics"]["blossom_vertices"] == 0
    assert verify_result(2 * side, edges, result)["optimality_verified"]

    # A nonbipartite original graph may have a bipartite retained H.  The
    # classification is on H, whose certificate transfers to the original.
    native = [(0, 1), (2, 3), (1, 2)]
    native += [(u, 4 + 4 * u + j) for u in range(4) for j in range(4)]
    native += [(0, 20), (1, 20)]
    result = maximum_matching(23, native, certificate=True)
    assert result["cardinality"] == 4
    assert result["statistics"]["bipartite_components"] == 1
    assert result["statistics"]["blossom_vertices"] == 0
    assert verify_result(23, native, result)["optimality_verified"]
    full = maximum_matching(23, native, use_kernel=False, certificate=True)
    assert full["statistics"]["bipartite_components"] == 0
    assert full["statistics"]["blossom_vertices"] > 0
    assert verify_result(23, native, full)["optimality_verified"]

    records = [(0, 0), (1, 0), (0, 1), (1, 2), (3, 2), (2, 3), (5, 5)]
    labels = ["loop", 1, "1", -2, "last", "parallel", 10 ** 80]
    for use_kernel in (True, False):
        answer = maximum_matching(8, records, labels, use_kernel=use_kernel, certificate=True)
        assert answer["cardinality"] == oracle(8, records) == 2
        assert answer["statistics"]["blossom_vertices"] == 0
        assert verify_result(8, records, answer, labels)["optimality_verified"]
        assert all(edge["input_index"] in (1, 3, 4) for edge in answer["matching"])
        plain = maximum_matching(8, records, labels, use_kernel=use_kernel)
        assert answer["matching"] == plain["matching"]
    return 6


def main() -> None:
    if not __debug__:
        raise SystemExit("Run this mathematical checker without -O or PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-side", type=int, default=4, choices=range(5))
    parser.add_argument("--random-cases", type=int, default=300)
    parser.add_argument("--checkpoint", type=Path)
    args = parser.parse_args()
    if args.random_cases < 0:
        parser.error("--random-cases must be nonnegative")
    receipt = {
        "status": "IN_PROGRESS",
        "scope": "finite matching oracle and independent certificate checks",
        "source_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (Path(__file__).resolve(), REFERENCE / "matching.py",
                         REFERENCE / "verify_certificate.py")
        },
        "max_side": args.max_side,
        "random_cases": args.random_cases,
        "completed_families": [],
        "exhaustive_graphs": 0,
        "max_successful_phases": 0,
    }

    def save() -> None:
        if args.checkpoint:
            args.checkpoint.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    for a in range(args.max_side + 1):
        for b in range(args.max_side + 1):
            possible = [(u, a + v) for u in range(a) for v in range(b)]
            left = [True] * a + [False] * b
            for mask in range(1 << len(possible)):
                edges = [edge for bit, edge in enumerate(possible) if mask & (1 << bit)]
                phases, _ = check(a + b, edges, left)
                receipt["max_successful_phases"] = max(receipt["max_successful_phases"], phases)
                receipt["exhaustive_graphs"] += 1
            receipt["completed_families"].append([a, b])
            save()

    generator = random.Random(0xB1A7)
    for index in range(args.random_cases):
        a, b = 1 + index % 6, 1 + (index // 6) % 6
        edges = [(u, a + v) for u in range(a) for v in range(b)
                 if generator.randrange(10) <= index % 10]
        generator.shuffle(edges)
        phases, expected = check(a + b, edges, [True] * a + [False] * b)
        receipt["max_successful_phases"] = max(receipt["max_successful_phases"], phases)
        # Reverse both vertex order and side names to exercise deterministic
        # root/adjacency choices distinct from the exhaustive natural order.
        reversed_edges = [(a + b - 1 - v, a + b - 1 - u) for u, v in reversed(edges)]
        _, reversed_expected = check(a + b, reversed_edges, [True] * b + [False] * a)
        assert expected == reversed_expected
        for use_kernel in (True, False):
            answer = maximum_matching(a + b + 2, edges, use_kernel=use_kernel, certificate=True)
            assert answer["cardinality"] == expected
            assert answer["statistics"]["blossom_vertices"] == 0
            assert answer["statistics"]["certificate_searches"] == 0
            assert verify_result(a + b + 2, edges, answer)["optimality_verified"]
    receipt["rejection_checks"] = rejection_checks()
    receipt["large_and_native_cases"] = large_and_native_cases()
    receipt["status"] = "PASS"
    save()
    print(f"PASS: {receipt['exhaustive_graphs']} exhaustive bipartite graphs; {args.random_cases} seeded cases in two orders")
    print(f"PASS: {receipt['rejection_checks']} rejection checks; {receipt['large_and_native_cases']} long-path/native/branch cases")
    print(f"Maximum observed successful phases: {receipt['max_successful_phases']}; every call includes one final failed BFS")
    print("Scope: finite evidence for matching, phase accounting, and linear cover certificates; no fast research-backend claim.")


if __name__ == "__main__":
    main()
