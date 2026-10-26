#!/usr/bin/env python3
"""Finite checks for the linear-selector proof's local transformations.

This checks small published-expander instances and the generic binary-fan
and matching adapters. It does not implement or certify the all-size
published expander theorem or replace the production Beneš selector.
"""
from __future__ import annotations

import argparse
from collections import deque
from functools import lru_cache
import hashlib
from itertools import combinations
import json
from math import isqrt
from pathlib import Path
import random
import sys

REPOSITORY = Path(__file__).resolve().parents[3]
REFERENCE = REPOSITORY / 'problems/general-matching/reference'
sys.path.insert(0, str(REFERENCE))
from matching import maximum_matching  # noqa: E402
from verify_certificate import verify_result  # noqa: E402


def degree_two_network(n, arcs, inputs, outputs):
    indegree, outdegree = [0] * n, [0] * n
    adjacency = [[] for _ in range(n)]
    for u, v in arcs:
        if not 0 <= u < n or not 0 <= v < n:
            raise ValueError('arc endpoint outside the graph')
        outdegree[u] += 1
        indegree[v] += 1
        adjacency[u].append(v)
    for terminals, degree in ((inputs, indegree), (outputs, outdegree)):
        seen = [False] * n
        for v in terminals:
            if not 0 <= v < n or seen[v] or degree[v]:
                raise ValueError('invalid designated source or sink')
            seen[v] = True
    residual = indegree.copy()
    queue = deque(v for v in range(n) if residual[v] == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in adjacency[u]:
            residual[v] -= 1
            if residual[v] == 0:
                queue.append(v)
    if visited != n:
        raise ValueError('the supplied network is not acyclic')

    next_vertex = 0
    new_arcs = []

    def allocate():
        nonlocal next_vertex
        result = next_vertex
        next_vertex += 1
        return result

    def tree(leaves, incoming):
        if leaves == 0:
            return allocate(), []
        terminals = [allocate() for _ in range(leaves)]
        level = terminals.copy()
        while len(level) > 1:
            following = []
            for index in range(0, len(level), 2):
                if index + 1 == len(level):
                    following.append(level[index])
                    continue
                parent = allocate()
                for child in level[index:index + 2]:
                    new_arcs.append((child, parent) if incoming else (parent, child))
                following.append(parent)
            level = following
        return level[0], terminals

    in_roots, out_roots, in_leaves, out_leaves = [], [], [], []
    for p, q in zip(indegree, outdegree):
        ir, il = tree(p, True)
        otr, ol = tree(q, False)
        in_roots.append(ir)
        out_roots.append(otr)
        in_leaves.append(il)
        out_leaves.append(ol)
        new_arcs.append((ir, otr))
    tail, head = [0] * n, [0] * n
    for u, v in arcs:
        new_arcs.append((out_leaves[u][tail[u]], in_leaves[v][head[v]]))
        tail[u] += 1
        head[v] += 1
    return next_vertex, new_arcs, [in_roots[v] for v in inputs], [out_roots[v] for v in outputs]


def terminal_paths(n, arcs, inputs, outputs):
    adjacency = [[] for _ in range(n)]
    for u, v in arcs:
        adjacency[u].append(v)
    targets = set(outputs)
    all_paths = {}
    for start in inputs:
        paths = []
        stack = [(start, 1 << start)]
        while stack:
            u, used = stack.pop()
            if u in targets:
                paths.append((u, used))
            for v in adjacency[u]:
                assert not used & (1 << v)
                stack.append((v, used | (1 << v)))
        all_paths[start] = paths
    return all_paths


def independent_routing_oracle(paths, selected_inputs, selected_outputs):
    targets = sum(1 << v for v in selected_outputs)

    @lru_cache(maxsize=None)
    def choose(index, used, remaining_targets):
        if index == len(selected_inputs):
            return remaining_targets == 0
        for target, mask in paths[selected_inputs[index]]:
            bit = 1 << target
            if remaining_targets & bit and not used & mask:
                if choose(index + 1, used | mask, remaining_targets ^ bit):
                    return True
        return False
    return choose(0, 0, targets)


def selector_graph(n, arcs, selected_inputs, selected_outputs):
    edges = [(2*v, 2*v+1) for v in range(n)]
    edges += [(2*u+1, 2*v) for u, v in arcs]
    next_vertex = 2*n
    for u in selected_inputs:
        edges.append((next_vertex, 2*u))
        next_vertex += 1
    for v in selected_outputs:
        edges.append((2*v+1, next_vertex))
        next_vertex += 1
    return next_vertex, edges


def check_network(n, arcs, counters, *, selected_pairs=None):
    incoming, outgoing = [0] * n, [0] * n
    for u, v in arcs:
        outgoing[u] += 1
        incoming[v] += 1
    inputs = [v for v in range(n) if incoming[v] == 0]
    outputs = [v for v in range(n) if outgoing[v] == 0]
    expanded_n, expanded_arcs, expanded_inputs, expanded_outputs = degree_two_network(n, arcs, inputs, outputs)
    assert expanded_n <= 4 * len(arcs) + 2 * n
    assert len(expanded_arcs) <= 5 * len(arcs) + n
    assert len(expanded_arcs) == len(set(expanded_arcs))
    ins, outs = [0] * expanded_n, [0] * expanded_n
    adjacency = [[] for _ in range(expanded_n)]
    for u, v in expanded_arcs:
        ins[v] += 1
        outs[u] += 1
        adjacency[u].append(v)
    assert all(value <= 2 for value in ins + outs)
    assert all(ins[v] == 0 for v in expanded_inputs)
    assert all(outs[v] == 0 for v in expanded_outputs)
    degree = ins.copy()
    queue = deque(v for v in range(expanded_n) if degree[v] == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in adjacency[u]:
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v)
    assert visited == expanded_n
    paths = terminal_paths(n, arcs, inputs, outputs)
    source_map, target_map = dict(zip(inputs, expanded_inputs)), dict(zip(outputs, expanded_outputs))
    if selected_pairs is None:
        selected_pairs = ((left, right) for t in range(min(len(inputs), len(outputs)) + 1)
                          for left in combinations(inputs, t) for right in combinations(outputs, t))
    for left, right in selected_pairs:
        expected = independent_routing_oracle(paths, tuple(left), tuple(right))
        order, edges = selector_graph(expanded_n, expanded_arcs,
                                      [source_map[v] for v in left], [target_map[v] for v in right])
        assert all(u != v for u, v in edges)
        assert len(edges) == len({tuple(sorted(edge)) for edge in edges})
        degrees = [0] * order
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
        assert all(value <= 3 for value in degrees)
        result = maximum_matching(order, edges, certificate=True)
        assert (2 * result['cardinality'] == order) == expected
        assert verify_result(order, edges, result)['optimality_verified']
        counters['terminal_pairs'] += 1
        counters['infeasible_terminal_pairs'] += not expected
    counters['networks'] += 1
    counters['maximum_adapter_vertices'] = max(counters['maximum_adapter_vertices'], expanded_n)


def expander_checks(counters):
    def maps(q, x, y):
        return ((x, y), (x, (x+y) % q), (x, (x+y+1) % q),
                ((x+y) % q, y), ((x+y+1) % q, y))
    for q in range(1, 33):
        images = [set() for _ in range(5)]
        for x in range(q):
            for y in range(q):
                for i, point in enumerate(maps(q, x, y)):
                    images[i].add(point)
        assert all(len(image) == q*q for image in images)
        counters['permutation_maps'] += 5
    for q in range(1, 5):
        n = q*q
        neighbors = [sum(1 << (u*q+v) for u, v in set(maps(q, x, y)))
                     for x in range(q) for y in range(q)]
        for chosen in range(1 << n):
            remaining = chosen
            covered = 0
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                covered |= neighbors[bit.bit_length()-1]
            size = chosen.bit_count()
            assert 15*n*covered.bit_count() >= size*(16*n-size)
            counters['finite_expansion_sets'] += 1


def rounding_checks(counters):
    cutoff = 1 << 26
    samples = [cutoff + 1]
    for r in range(126, 300):
        samples.extend(3968*r*r + delta for delta in (-1, 0, 1))
    samples += [(1 << exponent) + delta for exponent in range(27, 241, 7) for delta in (-1, 0, 1)]
    for original in samples:
        if original <= cutoff:
            continue
        n = original
        total_vertices = total_edges = total_sizes = 0
        while n > cutoff:
            r = isqrt((n - 1) // 3968) + 1
            assert 3968*(r-1)**2 < n <= 3968*r*r
            m = 3844*r*r
            assert r >= 131 and 64*m < 63*n
            assert 0 <= n-m <= 124*r*r
            total_vertices += 2*n
            total_edges += n + 2*(5*m + 31*(n-m))
            total_sizes += n
            n = m
        width = 1 << (n-1).bit_length()
        depth = width.bit_length()-1
        total_vertices += (2*depth+1)*width if n > 1 else 2
        total_edges += 4*width*depth if n > 1 else 1
        total_sizes += n
        assert total_sizes <= 64*original
        assert total_vertices <= 234*original
        assert total_edges <= 1040*original
        counters['rounding_sequences'] += 1


def main():
    if not __debug__:
        raise SystemExit('Run this mathematical checker without -O or PYTHONOPTIMIZE.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=5, choices=range(6))
    parser.add_argument('--checkpoint', type=Path)
    args = parser.parse_args()
    counters = dict(networks=0, terminal_pairs=0, infeasible_terminal_pairs=0,
                    maximum_adapter_vertices=0, permutation_maps=0,
                    finite_expansion_sets=0, rounding_sequences=0)
    source_hashes = {str(path.relative_to(REPOSITORY)): hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in (Path(__file__).resolve(), REFERENCE/'matching.py', REFERENCE/'verify_certificate.py')}
    for n in range(args.max_n+1):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            arcs = [arc for index, arc in enumerate(possible) if mask & (1 << index)]
            check_network(n, arcs, counters)
        if args.checkpoint:
            args.checkpoint.write_text(json.dumps(dict(status='IN_PROGRESS', completed_order=n,
                                                       source_sha256=source_hashes, counts=counters), indent=2)+'\n')
    generator = random.Random(0x5C0A)
    for index in range(70):
        n = 6 + index % 4
        arcs = [edge for edge in combinations(range(n), 2) if generator.randrange(7) < 2 + index % 3]
        if index % 4 == 0:
            arcs += arcs[:2]
        check_network(n, arcs, counters)
    # Large fan-in/fan-out, with a one-vertex routing bottleneck.
    arcs = [(u, 32) for u in range(32)] + [(32, v) for v in range(33, 65)]
    pairs = [(tuple(range(t)), tuple(range(65-t, 65))) for t in (0, 1, 2, 16, 32)]
    check_network(65, arcs, counters, selected_pairs=pairs)
    rejected = 0
    for arguments in [(2, [(0, 1), (1, 0)], [], []),
                      (2, [(0, 1)], [1], [1]),
                      (2, [(0, 1)], [0], [0]),
                      (2, [(0, 1)], [0, 0], [1])]:
        try:
            degree_two_network(*arguments)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError(arguments)
    counters['rejected_networks'] = rejected
    expander_checks(counters)
    rounding_checks(counters)
    for name, expected in source_hashes.items():
        assert hashlib.sha256((REPOSITORY / name).read_bytes()).hexdigest() == expected
    receipt = dict(status='PASS_SCOPED_FINITE_EVIDENCE', counts=counters,
                   source_sha256=source_hashes,
                   scope='finite published-expander examples, exact size arithmetic, and local binary-fan/matching adapters; not an all-size expander proof or a replacement production selector')
    if args.checkpoint:
        args.checkpoint.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
