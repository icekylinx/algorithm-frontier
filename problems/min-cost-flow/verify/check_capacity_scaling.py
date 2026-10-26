#!/usr/bin/env python3
"""Finite evidence for the actual-size capacity-bit scaling reduction.

The bounded-capacity oracle is an elementary integral augmenting-path solver
here, not the published fast solver. Independent exhaustive cut enumeration
checks every scale, every truncation, and the final maximum flow. Separate
circulation enumeration checks the negative return-edge reduction.
"""
from __future__ import annotations

import argparse
from collections import deque
from itertools import product
import json
from pathlib import Path
import random


def cut_oracle(n: int, edges, capacities, source=0, sink=None):
    sink = n - 1 if sink is None else sink
    middle = [v for v in range(n) if v not in (source, sink)]
    best = sum(capacities) + 1
    best_side = None
    for mask in range(1 << len(middle)):
        side = {source} | {v for bit, v in enumerate(middle) if mask >> bit & 1}
        value = sum(capacity for (u, v), capacity in zip(edges, capacities)
                    if u in side and v not in side)
        if value < best:
            best, best_side = value, side
    return best, best_side


def flow_value(n, edges, capacities, flow, source=0, sink=None):
    sink = n - 1 if sink is None else sink
    balance = [0] * n
    assert len(flow) == len(edges) == len(capacities)
    for (u, v), capacity, value in zip(edges, capacities, flow):
        assert type(value) is int and 0 <= value <= capacity
        balance[u] += value
        balance[v] -= value
    value = balance[source]
    assert value >= 0 and balance[sink] == -value
    assert all(balance[v] == 0 for v in range(n) if v not in (source, sink))
    return value


def integral_oracle(n, edges, capacities, source, sink):
    """Ordinary BFS augmentations, used only to instantiate the test oracle."""
    adjacency = [[] for _ in range(n)]
    locations = []
    for (u, v), capacity in zip(edges, capacities):
        if u == v or capacity == 0:
            locations.append(None)
            continue
        locations.append((u, len(adjacency[u])))
        forward = [v, len(adjacency[v]), capacity]
        reverse = [u, len(adjacency[u]), 0]
        adjacency[u].append(forward)
        adjacency[v].append(reverse)
    while True:
        parent = [None] * n
        parent[source] = (-1, -1)
        queue = deque([source])
        while queue and parent[sink] is None:
            u = queue.popleft()
            for index, (v, _, capacity) in enumerate(adjacency[u]):
                if capacity and parent[v] is None:
                    parent[v] = (u, index)
                    queue.append(v)
        if parent[sink] is None:
            break
        amount = sum(capacities) + 1
        v = sink
        while v != source:
            u, index = parent[v]
            amount = min(amount, adjacency[u][index][2])
            v = u
        v = sink
        while v != source:
            u, index = parent[v]
            arc = adjacency[u][index]
            arc[2] -= amount
            adjacency[v][arc[1]][2] += amount
            v = u
    return [0 if location is None else capacity - adjacency[location[0]][location[1]][2]
            for location, capacity in zip(locations, capacities)]


def scale_and_check(n, native_edges, native_capacities, counters, source=0, sink=None):
    sink = n - 1 if sink is None else sink
    keep = [i for i, ((u, v), capacity) in enumerate(zip(native_edges, native_capacities))
            if u != v and capacity > 0]
    edges = [native_edges[i] for i in keep]
    capacities = [native_capacities[i] for i in keep]
    order = len(edges)
    width = max(capacities, default=0).bit_length()
    current = [0] * order
    flow = [0] * order
    value = 0
    for position in range(width - 1, -1, -1):
        old_opt, old_cut = cut_oracle(n, edges, current, source, sink)
        assert value == old_opt
        bits = [(capacity >> position) & 1 for capacity in capacities]
        newly_one = sum(bits)
        current = [2 * old + bit for old, bit in zip(current, bits)]
        flow = [2 * old for old in flow]
        doubled_value = flow_value(n, edges, current, flow, source, sink)
        assert doubled_value == 2 * value
        next_opt, _ = cut_oracle(n, edges, current, source, sink)
        assert 0 <= next_opt - doubled_value <= newly_one <= order
        old_cut_new = sum(capacity for (u, v), capacity in zip(edges, current)
                          if u in old_cut and v not in old_cut)
        assert old_cut_new <= doubled_value + newly_one
        residual_edges, residual_caps, origins = [], [], []
        for index, ((u, v), capacity, sent) in enumerate(zip(edges, current, flow)):
            if capacity > sent:
                residual_edges.append((u, v))
                residual_caps.append(capacity - sent)
                origins.append((index, 1))
            if sent:
                residual_edges.append((v, u))
                residual_caps.append(sent)
                origins.append((index, -1))
        counters['stages'] += 1
        counters['reverse_records'] += sum(sign == -1 for _, sign in origins)
        residual_opt, _ = cut_oracle(n, residual_edges, residual_caps, source, sink)
        assert residual_opt == next_opt - doubled_value
        if newly_one:
            assert newly_one <= len(residual_edges) <= 2 * order
            bounded = [min(capacity, newly_one) for capacity in residual_caps]
            bounded_opt, _ = cut_oracle(n, residual_edges, bounded, source, sink)
            assert bounded_opt == residual_opt
            counters['truncated_records'] += sum(a != b for a, b in zip(residual_caps, bounded))
            # Compress vertices for the actual oracle call; no global-size padding.
            vertices = sorted({source, sink} | {v for edge in residual_edges for v in edge})
            inverse = {vertex: index for index, vertex in enumerate(vertices)}
            local_edges = [(inverse[u], inverse[v]) for u, v in residual_edges]
            local_flow = integral_oracle(len(vertices), local_edges, bounded,
                                         inverse[source], inverse[sink])
            extra = flow_value(len(vertices), local_edges, bounded, local_flow,
                               inverse[source], inverse[sink])
            assert extra == bounded_opt <= newly_one <= len(local_edges)
            assert max(bounded) <= len(local_edges)
            # A correct oracle may return extra circulation on the two
            # residual records of one original arc.  Exercise that lift too.
            forward_of = {index: record for record, (index, sign) in enumerate(origins) if sign == 1}
            for record, (index, sign) in enumerate(origins):
                other = forward_of.get(index)
                if sign == -1 and other is not None and min(
                        bounded[record] - local_flow[record], bounded[other] - local_flow[other]) > 0:
                    local_flow[record] += 1
                    local_flow[other] += 1
                    assert flow_value(len(vertices), local_edges, bounded, local_flow,
                                      inverse[source], inverse[sink]) == extra
                    counters['paired_direction_circulations'] += 1
                    break
            # Add one negative-cost return arc: this is a feasible circulation.
            circulation_edges = local_edges + [(inverse[sink], inverse[source])]
            circulation = local_flow + [extra]
            balances = [0] * len(vertices)
            for (u, v), sent in zip(circulation_edges, circulation):
                balances[u] += sent
                balances[v] -= sent
            assert not any(balances) and extra <= newly_one
            for (index, sign), sent in zip(origins, local_flow):
                flow[index] += sign * sent
            counters['oracle_calls'] += 1
        else:
            assert residual_opt == 0
            counters['zero_bit_stages'] += 1
        value = flow_value(n, edges, current, flow, source, sink)
        assert value == next_opt
    native_flow = [0] * len(native_edges)
    for index, sent in zip(keep, flow):
        native_flow[index] = sent
    assert flow_value(n, native_edges, native_capacities, native_flow, source, sink) == value
    assert cut_oracle(n, native_edges, native_capacities, source, sink)[0] == value
    residual_adjacency = [[] for _ in range(n)]
    for (u, v), capacity, sent in zip(native_edges, native_capacities, native_flow):
        if capacity > sent:
            residual_adjacency[u].append(v)
        if sent:
            residual_adjacency[v].append(u)
    reachable = {source}
    pending = [source]
    while pending:
        for vertex in residual_adjacency[pending.pop()]:
            if vertex not in reachable:
                reachable.add(vertex)
                pending.append(vertex)
    assert sink not in reachable
    assert sum(capacity for (u, v), capacity in zip(native_edges, native_capacities)
               if u in reachable and v not in reachable) == value
    counters['instances'] += 1
    return value


def return_edge_cases():
    edges = [(u, v) for u in range(3) for v in range(3) if u != v]
    cases = enumerated = 0
    for capacities in product(range(3), repeat=len(edges)):
        expected, _ = cut_oracle(3, edges, capacities)
        # A cap equal to the max-flow upper bound preserves the exact reduction.
        return_capacity = sum(capacities)
        all_edges = edges + [(2, 0)]
        best_cost = 0
        for circulation in product(*(range(capacity + 1) for capacity in (*capacities, return_capacity))):
            enumerated += 1
            balance = [0] * 3
            for (u, v), sent in zip(all_edges, circulation):
                balance[u] += sent
                balance[v] -= sent
            if not any(balance):
                best_cost = min(best_cost, -circulation[-1])
        assert -best_cost == expected
        cases += 1
    return cases, enumerated


def main():
    if not __debug__:
        raise SystemExit('Run this mathematical checker without -O or PYTHONOPTIMIZE.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path)
    args = parser.parse_args()
    counters = {key: 0 for key in ('instances', 'stages', 'oracle_calls', 'reverse_records',
                                  'truncated_records', 'zero_bit_stages',
                                  'paired_direction_circulations')}
    def checkpoint(phase):
        if args.checkpoint:
            args.checkpoint.write_text(json.dumps({'status': phase, **counters}, indent=2) + '\n')
    for n in (2, 3):
        edges = [(u, v) for u in range(n) for v in range(n) if u != v]
        for capacities in product(range(4), repeat=len(edges)):
            scale_and_check(n, edges, capacities, counters)
    checkpoint('small_capacity_cases_complete')
    n = 4
    edges = [(u, v) for u in range(n) for v in range(n) if u != v]
    for capacities in product(range(2), repeat=len(edges)):
        scale_and_check(n, edges, capacities, counters)
    checkpoint('all_binary_four_vertex_cases_complete')
    randomizer = random.Random(0xCA9AC17)
    for index in range(300):
        n = 3 + index % 6
        records = [(randomizer.randrange(n), randomizer.randrange(n))
                   for _ in range(index % 37)]
        bits = (1, 2, 5, 17, 83)[index % 5]
        capacities = [randomizer.getrandbits(bits) for _ in records]
        source, sink = randomizer.sample(range(n), 2)
        scale_and_check(n, records, capacities, counters, source, sink)
    explicit = [
        (5, [], []),
        (5, [(0, 4), (0, 4), (4, 0), (2, 2)], [0, 0, 0, 1 << 200]),
        (7, [(0, 1), (0, 1), (1, 6), (6, 1), (3, 3)],
         [(1 << 120) + 5, 13, (1 << 120) + 11, 2, 99]),
        (4, [(0, 1), (1, 2), (2, 3), (0, 2), (1, 3), (2, 1)],
         [1024, 3, 1024, 1023, 1023, 17]),
    ]
    for n, records, capacities in explicit:
        scale_and_check(n, records, capacities, counters)
    checkpoint('scaling_complete')
    cases, enumerated = return_edge_cases()
    counters['return_edge_instances'] = cases
    counters['circulation_assignments'] = enumerated
    assert all(counters[key] for key in ('reverse_records', 'truncated_records',
                                        'zero_bit_stages', 'paired_direction_circulations'))
    checkpoint('PASS')
    print('PASS:', json.dumps(counters, sort_keys=True))
    print('Scope: exact finite capacity-scaling, truncation and return-edge reductions; not the published fast flow implementation.')


if __name__ == '__main__':
    main()
