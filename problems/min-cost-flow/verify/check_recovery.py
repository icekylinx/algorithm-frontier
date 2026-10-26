#!/usr/bin/env python3
"""Exact finite checks of rounding and incremental artificial initialization.

The reference rounder uses explicit paths and Fraction arithmetic; it is not
the claimed fast dynamic-tree implementation. The stream checks enumerate
all integral feasible flows on their small graphs. No raw-cycle backend is
used or certified by this script. Requires only the Python standard library.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from math import ceil, floor


def divergence(n, edges, values):
    result = [Fraction(0) for _ in range(n)]
    for (u, v), value in zip(edges, values):
        result[u] -= value
        result[v] += value
    return tuple(result)


def penalty(values, capacities, costs, weight):
    return sum(
        c * x + weight * max(0, -x, x - u)
        for x, u, c in zip(values, capacities, costs)
    )


def fractional_cycle(n, edges, values):
    forest = [[] for _ in range(n)]
    for edge_id, ((u, v), value) in enumerate(zip(edges, values)):
        if value.denominator == 1:
            continue
        if u == v:
            return [(edge_id, 1)]
        # Find the forest path from v back to u.
        stack = [(v, -1, [])]
        while stack:
            here, parent, path = stack.pop()
            if here == u:
                return [(edge_id, 1), *path]
            for there, old_id, sign in forest[here]:
                if there != parent:
                    stack.append((there, here, [*path, (old_id, sign)]))
        forest[u].append((v, edge_id, 1))
        forest[v].append((u, edge_id, -1))
    return None


def round_flow(n, edges, initial, capacities, costs, weight):
    values = list(map(Fraction, initial))
    original_divergence = divergence(n, edges, values)
    assert all(x.denominator == 1 for x in original_divergence)
    boxes = [(floor(x), ceil(x)) for x in values]
    initial_penalty = penalty(values, capacities, costs, weight)
    steps = 0
    while any(x.denominator != 1 for x in values):
        cycle = fractional_cycle(n, edges, values)
        assert cycle, "fractional forest contradicts integral divergence"
        slopes = [
            c + (-weight if x < 0 else weight if x > u else 0)
            for x, u, c in zip(values, capacities, costs)
        ]
        if sum(sign * slopes[e] for e, sign in cycle) > 0:
            cycle = [(e, -sign) for e, sign in cycle]
        step = min(
            boxes[e][1] - values[e] if sign > 0 else values[e] - boxes[e][0]
            for e, sign in cycle
        )
        assert step > 0
        previous = penalty(values, capacities, costs, weight)
        fractional_before = sum(x.denominator != 1 for x in values)
        for e, sign in cycle:
            values[e] += sign * step
        assert sum(x.denominator != 1 for x in values) < fractional_before
        assert divergence(n, edges, values) == original_divergence
        assert penalty(values, capacities, costs, weight) <= previous
        assert all(lo <= x <= hi for x, (lo, hi) in zip(values, boxes))
        steps += 1
    assert steps <= len(edges)
    assert penalty(values, capacities, costs, weight) <= initial_penalty
    return values


def minimum_cost(n, edges, capacities, costs, demand):
    best = None
    for values in product(*(range(u + 1) for u in capacities)):
        if divergence(n, edges, values) == tuple(demand):
            cost = sum(c * x for c, x in zip(costs, values))
            best = cost if best is None else min(best, cost)
    return best


def main():
    if not __debug__:
        raise SystemExit("This checker requires assertions; run Python without -O.")
    delta = Fraction(1, 1024)
    graphs = [
        (1, [(0, 0)], [1], [(1,)]),
        (1, [(0, 0)], [0], [(1,)]),
        (2, [(0, 1), (1, 0)], [1, 1], [(1, 1)]),
        (2, [(0, 1), (0, 1)], [1, 1], [(1, -1)]),
        (3, [(0, 1), (1, 2), (2, 0)], [1, 1, 1], [(1, 1, 1)]),
        (3, [(0, 1), (1, 2), (2, 0), (0, 1), (1, 1)], [1] * 5,
         [(1, 1, 1, 0, 0), (1, 0, 0, -1, 0), (0, 0, 0, 0, 1), (1, 1, 1, 0, 1)]),
    ]
    rounding_cases = 0
    for n, edges, capacities, directions in graphs:
        m = len(edges)
        cost_vectors = [
            [1] * m, [-1] * m, [(-1) ** i for i in range(m)],
            [(-1) ** i * (i + 1) for i in range(m)],
        ]
        for base in product(*(range(u + 1) for u in capacities)):
            for direction in directions:
                assert divergence(n, edges, direction) == (0,) * n
                for alpha in (-delta, delta, Fraction(1, 2), 1 - delta, 1 + delta):
                    values = [Fraction(x) + alpha * d for x, d in zip(base, direction)]
                    violation = sum(max(0, -x, x - u) for x, u in zip(values, capacities))
                    if violation >= Fraction(1, 4):
                        continue
                    for costs in cost_vectors:
                        b0 = sum(abs(c) * (u + 1) for c, u in zip(costs, capacities))
                        # Check close integral thresholds on both sides of zero.
                        f0 = floor(sum(c * x for c, x in zip(costs, values)))
                        for threshold in (f0, f0 + 1):
                            weight = 2 * b0 + 2 * abs(threshold) + 10
                            if penalty(values, capacities, costs, weight) >= threshold + Fraction(1, 4):
                                continue
                            result = round_flow(n, edges, values, capacities, costs, weight)
                            assert all(0 <= x <= u for x, u in zip(result, capacities))
                            assert sum(c * x for c, x in zip(costs, result)) <= threshold
                            rounding_cases += 1

    n = 3
    possible = [(u, v) for u in range(n) for v in range(n) if u != v]
    stream_cases = preliminary_no = newly_feasible = 0
    demand_vectors = [d for d in product((-1, 0, 1), repeat=n) if sum(d) == 0]
    for length in range(4):
        for stream in permutations(possible, length):
            costs = [1 if u < v else -1 for u, v in stream]
            b_star = len(possible)  # A full-stream bound, fixed before the run.
            for demand in demand_vectors:
                for threshold in (-1, 0, 1):
                    last_answer = False
                    initialized = False
                    for end in range(length + 1):
                        edges, current_costs = list(stream[:end]), costs[:end]
                        capacities = [1] * end
                        optimum = minimum_cost(n, edges, capacities, current_costs, demand)
                        expected = optimum is not None and optimum <= threshold
                        incident = [0] * n
                        for u, v in edges:
                            incident[u] += 1
                            incident[v] += 1
                        ready = all(abs(d) <= incident[v] for v, d in enumerate(demand))
                        if not ready:
                            assert not initialized and not expected
                            actual = False
                            preliminary_no += 1
                        else:
                            initialized = True
                            augmented = list(edges)
                            aug_caps, aug_costs = capacities.copy(), current_costs.copy()
                            penalty_cost = 2 * b_star + abs(threshold) + 1
                            artificial_count = 0
                            for v, value in enumerate(demand):
                                if value:
                                    augmented.append((n, v) if value > 0 else (v, n))
                                    aug_caps.append(abs(value))
                                    aug_costs.append(penalty_cost)
                                    artificial_count += 1
                            assert artificial_count <= 2 * len(edges)
                            padded = minimum_cost(n + 1, augmented, aug_caps, aug_costs, (*demand, 0))
                            assert padded is not None
                            actual = padded <= threshold
                        assert actual == expected
                        if end and actual and not last_answer:
                            newly_feasible += 1
                        assert not last_answer or actual
                        last_answer = actual
                        stream_cases += 1

    print(f"Affine-penalty recovery: {rounding_cases} exact rational cases, including loops and parallel arcs.")
    print(f"Incremental initialization: {stream_cases} prefix/threshold cases; {preliminary_no} deferred NO states.")
    print(f"Feasibility transitions retained: {newly_feasible} NO-to-YES prefixes.")
    print("PASS: finite recovery/initialization checks; no raw-backend certification.")


if __name__ == "__main__":
    main()
