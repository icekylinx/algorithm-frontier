#!/usr/bin/env python3
"""Independent finite checks of the production vertex-cover compression.

Compare the actual kernel and compression functions to a subset-DP matching
oracle.  All small right endpoint bases and all left subsets are checked,
including preservation of the general-graph matching number.  Also test the
matched-edge bound on contractions in the actual certificate search.
"""
from __future__ import annotations

import argparse
import random
import sys
from functools import lru_cache
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from matching import _blossom, _compress_cover, _failed_search_forest, _kernel  # noqa: E402


def oracle(n: int, edges: list[tuple[int, int]]):
    adjacency = [0] * n
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    @lru_cache(maxsize=None)
    def solve(mask: int) -> int:
        if not mask:
            return 0
        bit = mask & -mask
        u = bit.bit_length() - 1
        rest = mask ^ bit
        answer = solve(rest)
        available = adjacency[u] & rest
        while available:
            other = available & -available
            available ^= other
            answer = max(answer, 1 + solve(rest ^ other))
        return answer
    return solve


def check_graph(n: int, edges: list[tuple[int, int]], *, all_bases: bool) -> tuple[int, int]:
    full = (1 << n) - 1
    original_opt = oracle(n, edges)(full)
    index_of = [-1] * n
    records = [(u, v, index) for index, (u, v) in enumerate(edges)]
    compact, adjacency, kept, cover_vertices = _kernel(list(range(n)), records, index_of, True)
    c = len(cover_vertices)
    assert c <= 2 * original_opt
    cover = [False] * n
    covered = [False] * len(compact)
    for u in cover_vertices:
        cover[u] = True
        covered[index_of[u]] = True
    kernel = [(u, v) for u, v, _ in kept]
    assert oracle(n, kernel)(full) == original_opt
    assert len(kernel) <= min(len(edges), c * (c - 1) // 2 + c * c)
    solve_vertices, solve_adjacency = _compress_cover(adjacency, covered)
    assert len(solve_vertices) == len(set(solve_vertices)) <= min(2 * c, 3 * original_opt)
    retained_vertices = {compact[index] for index in solve_vertices}
    assert set(cover_vertices) <= retained_vertices
    chosen = retained_vertices - set(cover_vertices)
    compressed = [(compact[solve_vertices[u]], compact[solve_vertices[v]])
                  for u, neighbors in enumerate(solve_adjacency) for v in neighbors if u < v]
    assert {frozenset(edge) for edge in compressed} == {
        frozenset((u, v)) for u, v in kernel if u in retained_vertices and v in retained_vertices}
    assert oracle(n, compressed)(full) == original_opt

    left = cover_vertices
    outside = [u for u in range(n) if not cover[u]]
    left_mask = sum(1 << u for u in left)
    outside_mask = full ^ left_mask
    crossing = [(u, v) for u, v in kernel if cover[u] != cover[v]]
    cross_oracle = oracle(n, crossing)
    original_cross = oracle(n, [(u, v) for u, v in edges if cover[u] != cover[v]])
    rank = cross_oracle(full)
    assert len(chosen) == rank <= c
    assert cross_oracle(left_mask | sum(1 << v for v in chosen)) == rank
    right_sets = [tuple(sorted(chosen))]
    if all_bases:
        right_sets = [candidate for candidate in combinations(outside, rank)
                      if cross_oracle(left_mask | sum(1 << v for v in candidate)) == rank]
    tested_bases = tested_subsets = 0
    for right_set in right_sets:
        right_mask = sum(1 << v for v in right_set)
        tested_bases += 1
        subset = left_mask
        while True:
            old_rank = original_cross(subset | outside_mask)
            assert old_rank == cross_oracle(subset | outside_mask)
            assert old_rank == cross_oracle(subset | right_mask), (n, edges, right_set, subset)
            tested_subsets += 1
            if subset == 0:
                break
            subset = (subset - 1) & left_mask

    # Compute on the small J, then certify on the original H, as in the API.
    small_mate = _blossom(solve_adjacency)
    assert sum(u < v for u, v in enumerate(small_mate)) == original_opt
    mate = [-1] * len(compact)
    for u, v in enumerate(small_mate):
        if v != -1:
            mate[solve_vertices[u]] = solve_vertices[v]
    statistics = {"certificate_searches": 0, "blossom_contractions": 0}
    _failed_search_forest(adjacency, mate, statistics)
    assert statistics["blossom_contractions"] <= original_opt
    return tested_bases, tested_subsets


def main() -> None:
    if not __debug__:
        raise SystemExit("Run this mathematical checker without -O or PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=6, choices=range(7))
    parser.add_argument("--random-cases", type=int, default=500)
    args = parser.parse_args()
    if args.random_cases < 0:
        parser.error("--random-cases must be nonnegative")
    graphs = covers = bases = subsets = 0
    for n in range(args.max_n + 1):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [edge for bit, edge in enumerate(possible) if mask & (1 << bit)]
            for order in (edges, list(reversed(edges))):
                b, s = check_graph(n, order, all_bases=True)
                covers += 1
                bases += b
                subsets += s
            graphs += 1
    randomizer = random.Random(0xC0A3E55)
    for index in range(args.random_cases):
        n = 7 + index % 7
        probability = (index % 9 + 1) / 10
        edges = [edge for edge in combinations(range(n), 2) if randomizer.random() < probability]
        randomizer.shuffle(edges)
        b, s = check_graph(n, edges, all_bases=False)
        covers += 1
        bases += b
        subsets += s
    try:
        _compress_cover([[1], [0]], [False, False])
    except RuntimeError as error:
        assert "vertex cover" in str(error)
    else:
        raise AssertionError("compression accepted a set that is not a vertex cover")
    print(f"PASS: {graphs} exhaustive graphs in both edge orders; {args.random_cases} seeded graphs")
    print(f"PASS: {covers} covers, {bases} right bases, {subsets} left-subset rank comparisons")
    print("PASS: general matching, min(2c,3nu) vertex cap, matched-edge contraction bound, and invalid-cover rejection")
    print("Scope: production cover compression and its certificate-cost bound; no fast research-backend claim.")


if __name__ == "__main__":
    main()
