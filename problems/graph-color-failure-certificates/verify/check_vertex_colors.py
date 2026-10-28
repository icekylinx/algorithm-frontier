#!/usr/bin/env python3
"""Independent all-prefix graph checks for the vertex-color backend.
Copyright 2026 icekylinx. Authored by GPT-6 Astra Pro.
SPDX-License-Identifier: Apache-2.0
"""
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'reference'))
from vertex_colors import Edge, build

COUNTS = dict(instances=0, failures=0, prefixes=0, sharp_instances=0, rejections=0)


def components(n, records, colors, failed):
    # Reachability flood fills: independent of elimination and disjoint-set code.
    alive = set(range(n)) - {v for v, c in enumerate(colors) if c in failed}
    adj = {v: set() for v in alive}
    for _, e in records:
        if e.u in alive and e.v in alive:
            adj[e.u].add(e.v)
            adj[e.v].add(e.u)
    parts = set()
    while alive:
        reached, frontier = set(), {min(alive)}
        while frontier:
            v = frontier.pop()
            if v not in reached:
                reached.add(v)
                frontier.update(adj[v] - reached)
        alive -= reached
        parts.add(frozenset(reached))
    return frozenset(parts)


def canonical(n, records, colors, failed):
    accepted = []
    previous = components(n, accepted, colors, failed)
    for record in records:
        current = components(n, accepted + [record], colors, failed)
        if current != previous:
            accepted.append(record)
            previous = current
    return tuple(i for i, _ in accepted)


def check(colors, edges, budget):
    certificate = build(colors, edges, budget)
    COUNTS['instances'] += 1
    assert len(certificate.records) <= certificate.support_bound
    assert len({i for i, _ in certificate.records}) == len(certificate.records)
    assert all(edge == edges[i] for i, edge in certificate.records)
    records = sorted(enumerate(edges), key=lambda pair: (pair[1].weight, pair[0]))
    palette = sorted(set(colors))
    for size in range(min(budget, len(palette)) + 1):
        for failed in combinations(palette, size):
            COUNTS['failures'] += 1
            assert certificate.forest(failed) == canonical(len(colors), records, colors, failed)
            for length in range(len(records) + 1):
                original = records[:length]
                ids = {i for i, _ in original}
                retained = [(i, e) for i, e in certificate.records if i in ids]
                assert components(len(colors), original, colors, failed) == components(
                    len(colors), retained, colors, failed)
                COUNTS['prefixes'] += 1
    return certificate


def main():
    for n in range(4):
        possible = tuple(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [Edge(u, v, Fraction(i % 3 - 1, 2)) for i, (u, v) in enumerate(possible)
                     if mask >> i & 1]
            for colors in product(range(2), repeat=n):
                for budget in range(3):
                    check(colors, edges, budget)
    rng = random.Random(104699)
    for _ in range(110):
        n = rng.randrange(1, 8)
        colors = [rng.randrange(4) for _ in range(n)]
        edges = [Edge(rng.randrange(n), rng.randrange(n), Fraction(rng.randrange(-5, 6), 3))
                 for _ in range(rng.randrange(18))]
        check(colors, edges, rng.randrange(4))
    # Every core edge and every outer/core edge is forced by the standard
    # sharpness example, including the all-colors and no-failure endpoints.
    for n in range(1, 8):
        for h in range(n + 1):
            k = min(h + 1, n)
            edges = [Edge(u, v, 1) for u, v in combinations(range(k), 2)]
            edges += [Edge(u, v, 2) for u in range(k, n) for v in range(k)]
            certificate = check(tuple(range(n)), edges, h)
            assert len(certificate.records) == len(edges) == certificate.support_bound
            COUNTS['sharp_instances'] += 1
    certificate = check([5, 5], [Edge(0, 1, -1)], 10**100)
    assert certificate.forest([10**200]) == (0,)
    bad = [lambda: build([0], [], -1), lambda: build([True], [], 0),
           lambda: build([0], [Edge(0, 1, 0)], 1),
           lambda: build([0], [Edge(0, 0, 0.1)], 1),
           lambda: certificate.forest([5, 5]), lambda: certificate.forest([-1]),
           lambda: build([0, 1], [Edge(0, 1, 0)], 0).forest([0])]
    for call in bad:
        try:
            call()
        except ValueError:
            COUNTS['rejections'] += 1
        else:
            raise AssertionError('invalid input accepted')
    print('PASS vertex-color certificates:', ', '.join(f'{k}={v}' for k, v in COUNTS.items()))


if __name__ == '__main__':
    main()
