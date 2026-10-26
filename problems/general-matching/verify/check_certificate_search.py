#!/usr/bin/env python3
"""Independent finite checks of the simultaneous failed-forest certificate.

The actual production search is compared to deletion-defined exposability
using subset dynamic programming and, for n<=9, explicit simple alternating
paths.  Terminal block/matching invariants are also checked.  This does not
run a copied search algorithm or certify the separate fast research theorem.
"""
from __future__ import annotations

import argparse
import random
import sys
from functools import lru_cache
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from matching import _blossom, _failed_search_forest  # noqa: E402


def independent_oracle(adjacency: list[list[int]]):
    masks = [sum(1 << v for v in neighbors) for neighbors in adjacency]

    @lru_cache(maxsize=None)
    def solve(available: int) -> int:
        if not available:
            return 0
        bit = available & -available
        u = bit.bit_length() - 1
        rest = available ^ bit
        answer = solve(rest)
        candidates = masks[u] & rest
        while candidates:
            other = candidates & -candidates
            candidates ^= other
            answer = max(answer, 1 + solve(rest ^ other))
        return answer
    return solve


def even_endpoints(adjacency: list[list[int]], mate: list[int]) -> set[int]:
    reached: set[int] = set()
    seen: set[tuple[int, int, bool]] = set()

    def visit(u: int, visited: int, even: bool) -> None:
        state = (u, visited, even)
        if state in seen:
            return
        seen.add(state)
        if even:
            reached.add(u)
            candidates = [v for v in adjacency[u] if mate[u] != v]
        else:
            candidates = [] if mate[u] == -1 else [mate[u]]
        for v in candidates:
            if not visited & (1 << v):
                visit(v, visited | (1 << v), not even)

    for root, partner in enumerate(mate):
        if partner == -1:
            visit(root, 1 << root, True)
    return reached


def check_graph(n: int, edges: list[tuple[int, int]]) -> int:
    adjacency: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    mate = _blossom(adjacency)
    old_mate = mate.copy()
    oracle = independent_oracle(adjacency)
    full = (1 << n) - 1
    optimum = oracle(full)
    assert sum(u < v for u, v in enumerate(mate)) == optimum
    expected = {v for v in range(n) if oracle(full ^ (1 << v)) == optimum}
    statistics = {"certificate_searches": 0, "blossom_contractions": 0}
    outer, base, parent = _failed_search_forest(adjacency, mate, statistics)
    assert mate == old_mate
    reached = {v for v in range(n) if outer[v]}
    assert reached == expected, (n, edges, mate, reached, expected)
    if n <= 9:
        assert reached == even_endpoints(adjacency, mate)
    inner = {v for v in range(n) if not outer[v] and parent[v] != -1}
    assert inner == {v for u in reached for v in adjacency[u]} - reached
    blocks = {base[v] for v in reached}
    free = sum(partner == -1 for partner in mate)
    assert len(blocks) == len(inner) + free
    assert {base[mate[v]] for v in inner} == {block for block in blocks if mate[block] != -1}
    unreached = set(range(n)) - reached - inner
    assert all(mate[v] in unreached for v in unreached)
    for u in reached:
        for v in adjacency[u]:
            if outer[v]:
                assert base[u] == base[v]
    for representative in blocks:
        block = {v for v in reached if base[v] == representative}
        assert len(block) % 2 == 1
        mask = sum(1 << v for v in block)
        for vertex in block:
            assert oracle(mask ^ (1 << vertex)) == (len(block) - 1) // 2
        leaving = [(v, mate[v]) for v in block if mate[v] != -1 and mate[v] not in block]
        if mate[representative] == -1:
            assert not leaving
            assert sum(mate[v] == -1 for v in block) == 1
        else:
            assert leaving == [(representative, mate[representative])]
            assert mate[representative] in inner
    remaining = set(range(n)) - inner
    odd = 0
    while remaining:
        stack = [remaining.pop()]
        order = 0
        while stack:
            u = stack.pop()
            order += 1
            for v in adjacency[u]:
                if v in remaining:
                    remaining.remove(v)
                    stack.append(v)
        odd += order % 2
    assert odd == len(blocks)
    assert 2 * optimum == n - odd + len(inner)
    assert statistics["certificate_searches"] == 1
    return statistics["blossom_contractions"]


def rejection_checks() -> int:
    cases = [
        ([[1], [0]], [-1, -1]),
        ([[1], [0, 2], [1, 3], [2]], [-1, 2, 1, -1]),
    ]
    for adjacency, mate in cases:
        try:
            _failed_search_forest(adjacency, mate)
        except RuntimeError as error:
            assert "augmenting path" in str(error)
        else:
            raise AssertionError("nonmaximum matching passed exhausted-search extraction")
    return len(cases)


def main() -> None:
    if not __debug__:
        raise SystemExit("Run this mathematical checker without -O or PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=6, choices=range(7))
    parser.add_argument("--random-cases", type=int, default=500)
    args = parser.parse_args()
    if args.random_cases < 0:
        parser.error("--random-cases must be nonnegative")
    graphs = contractions = 0
    for n in range(args.max_n + 1):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [edge for bit, edge in enumerate(possible) if mask & (1 << bit)]
            contractions += check_graph(n, edges)
            graphs += 1
    randomizer = random.Random(0xCE471F1C)
    for index in range(args.random_cases):
        n = 7 + index % 7
        probability = (index % 9 + 1) / 10
        edges = [edge for edge in combinations(range(n), 2) if randomizer.random() < probability]
        randomizer.shuffle(edges)
        contractions += check_graph(n, edges)
    rejected = rejection_checks()
    print(f"PASS: {graphs} exhaustive graphs and {args.random_cases} seeded graphs")
    print(f"PASS: deletion-defined exposability, even alternating paths, factor-critical blocks, and tight barriers")
    print(f"Coverage: {contractions} contractions; {rejected} nonmaximum-input rejections")
    print("Scope: the production quadratic certificate search; no fast research-backend claim.")


if __name__ == "__main__":
    main()
