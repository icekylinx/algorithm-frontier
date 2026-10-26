#!/usr/bin/env python3
"""Replay finite signed-interval and minimum-hop exchange certificates.

The interval test compares the rounding catalogue against every Boolean
assignment in an explicit signed family. The exchange test compares compressed
cycles with exhaustive optimal replacements in every subgraph of K_3,3 under
five fixed integer cost profiles, including complete cost ties.

These are independent finite checks of two local mechanisms. They do not
verify an asymptotic running time, a Subset Sum backend, or the exchange theorem
for arbitrary matroids. All arithmetic is exact and uses only the standard
library. The JSON report is deterministic and no files are modified.
"""
from __future__ import annotations

from itertools import permutations, product
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ceil_log2(value: int) -> int:
    require(value > 0, "logarithm input must be positive")
    return (value - 1).bit_length()


def short_intervals(
    coefficients: tuple[int, ...], lower: int, upper: int
) -> list[tuple[tuple[int, ...], int, int]]:
    """Implement the signed shrinking catalogue with a fixed support bound."""
    support = sum(value != 0 for value in coefficients)
    require(support > 0 and lower <= upper, "invalid nonzero interval row")
    output = []
    while True:
        if upper - lower <= 5 * support:
            output.append((coefficients, lower, upper))
            return output
        if lower % 2:
            output.append((coefficients, lower, lower))
            lower += 1
            continue
        if upper % 2:
            output.append((coefficients, upper, upper))
            upper -= 1
            continue
        output.append((coefficients, lower, lower + 3 * support))
        output.append((coefficients, upper - 2 * support, upper))
        # Python // is floor division also for negative coefficients.
        coefficients = tuple(value // 2 for value in coefficients)
        lower = (lower + 2 * support) // 2
        upper = (upper - 2 * support) // 2


def check_signed_intervals() -> dict[str, int]:
    assignments = tuple(product((0, 1), repeat=3))
    row_count = interval_count = assignment_count = 0
    for coefficients in product(range(-3, 4), repeat=3):
        support = sum(value != 0 for value in coefficients)
        if support == 0:
            continue
        row_count += 1
        for lower in range(-10, 11):
            for upper in range(lower, 11):
                interval_count += 1
                catalogue = short_intervals(coefficients, lower, upper)
                width = upper - lower
                require(
                    len(catalogue) <= 4 * ceil_log2(width + 1) + 1,
                    f"catalogue size: {coefficients}, [{lower},{upper}]",
                )
                maximum_values = min(width + 1, 5 * support + 1)
                require(
                    all(0 <= end - start < maximum_values
                        for _, start, end in catalogue),
                    f"catalogue width: {coefficients}, [{lower},{upper}]",
                )
                for assignment in assignments:
                    assignment_count += 1
                    original_sum = sum(a * x for a, x in zip(coefficients, assignment))
                    original_answer = lower <= original_sum <= upper
                    catalogue_answer = any(
                        start <= sum(a * x for a, x in zip(row, assignment)) <= end
                        for row, start, end in catalogue
                    )
                    require(
                        original_answer == catalogue_answer,
                        f"catalogue equivalence: {coefficients}, "
                        f"[{lower},{upper}], assignment={assignment}",
                    )

    # Independent subset-sum closure checks the slack list, including width zero.
    for width in range(1025):
        count = ceil_log2(width + 1)
        coins = (
            [1 << power for power in range(count - 1)]
            + [width - ((1 << (count - 1)) - 1)]
            if count else []
        )
        require(len(coins) == count, f"slack variable count: {width}")
        require(all(value > 0 for value in coins), f"slack positivity: {width}")
        reachable = {0}
        for value in coins:
            reachable |= {total + value for total in reachable}
        require(reachable == set(range(width + 1)), f"slack coverage: {width}")

    return {
        "nonzero_signed_rows": row_count,
        "row_intervals": interval_count,
        "assignment_interval_comparisons": assignment_count,
        "slack_widths_checked": 1025,
    }


EDGES = tuple((left, right) for left in range(3) for right in range(3))


def elements(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(len(EDGES)) if mask >> index & 1)


def partition_independent(mask: int, side: int) -> bool:
    vertices = [EDGES[index][side] for index in elements(mask)]
    return len(vertices) == len(set(vertices))


def common_independent(mask: int) -> bool:
    return partition_independent(mask, 0) and partition_independent(mask, 1)


def cost(mask: int, weights: tuple[int, ...]) -> int:
    return sum(weights[index] for index in elements(mask))


def compressed_arcs(
    graph: int, basis: int, weights: tuple[int, ...]
) -> dict[tuple[int, int], tuple[int, int]]:
    """Keep the least-cost original outside label for each ordered base pair."""
    arcs: dict[tuple[int, int], tuple[int, int]] = {}
    for outside in elements(graph & ~basis):
        left_exchanges = [
            removed for removed in elements(basis)
            if partition_independent((basis ^ (1 << removed)) | (1 << outside), 0)
        ]
        right_exchanges = [
            removed for removed in elements(basis)
            if partition_independent((basis ^ (1 << removed)) | (1 << outside), 1)
        ]
        for left in left_exchanges:
            for right in right_exchanges:
                candidate = (weights[outside] - weights[left], outside)
                if (left, right) not in arcs or candidate < arcs[left, right]:
                    arcs[left, right] = candidate
    return arcs


def cycles_through(
    failure: int, basis: int, arcs: dict[tuple[int, int], tuple[int, int]]
) -> list[tuple[int, int, tuple[int, ...], tuple[int, ...]]]:
    """Enumerate all simple directed cycles, based at the failed element."""
    others = tuple(element for element in elements(basis) if element != failure)
    cycles = []
    for hops in range(1, len(others) + 2):
        for suffix in permutations(others, hops - 1):
            vertices = (failure,) + suffix
            pairs = tuple(zip(vertices, vertices[1:] + vertices[:1]))
            if all(pair in arcs for pair in pairs):
                labels = tuple(arcs[pair][1] for pair in pairs)
                delta = sum(arcs[pair][0] for pair in pairs)
                cycles.append((delta, hops, labels, vertices))
    return cycles


def check_minimum_hop_repairs() -> dict[str, int]:
    profiles = (
        (0,) * 9,
        tuple(range(-4, 5)),
        tuple(4 - index for index in range(9)),
        tuple(((5 * index + 2) % 11) - 5 for index in range(9)),
        tuple(-3 if left == right else (left + right) % 3 for left, right in EDGES),
    )
    all_matchings = [
        mask for mask in range(1 << len(EDGES)) if common_independent(mask)
    ]
    rank_cases = failure_cases = repairs = infeasible = simple_cycles = 0
    for graph in range(1 << len(EDGES)):
        feasible = [mask for mask in all_matchings if mask & ~graph == 0]
        by_rank = {
            rank: [mask for mask in feasible if mask.bit_count() == rank]
            for rank in range(1, 4)
        }
        for weights in profiles:
            for rank, bases in by_rank.items():
                if not bases:
                    continue
                rank_cases += 1
                basis = min(bases, key=lambda mask: (cost(mask, weights), mask))
                baseline_cost = cost(basis, weights)
                arcs = compressed_arcs(graph, basis, weights)
                for failure in elements(basis):
                    failure_cases += 1
                    alternatives = [mask for mask in bases if not (mask >> failure & 1)]
                    cycles = cycles_through(failure, basis, arcs)
                    simple_cycles += len(cycles)
                    require(
                        all(cycle[0] >= 0 for cycle in cycles),
                        f"negative compressed cycle: graph={graph}, "
                        f"weights={weights}, rank={rank}, failure={failure}",
                    )
                    require(
                        bool(alternatives) == bool(cycles),
                        f"replacement/cycle existence mismatch: graph={graph}, "
                        f"weights={weights}, rank={rank}, failure={failure}",
                    )
                    if not alternatives:
                        infeasible += 1
                        continue

                    repairs += 1
                    delta, hops, labels, vertices = min(cycles)
                    require(
                        len(set(labels)) == hops,
                        f"minimum-hop cycle repeats an original label: {labels}",
                    )
                    removed = sum(1 << vertex for vertex in vertices)
                    added = sum(1 << label for label in labels)
                    repaired = (basis & ~removed) | added
                    require(
                        repaired & ~graph == 0
                        and not (repaired >> failure & 1)
                        and repaired.bit_count() == rank
                        and common_independent(repaired),
                        f"literal toggle is infeasible: graph={graph}, basis={basis}, "
                        f"cycle={(delta, hops, labels, vertices)}",
                    )
                    optimum = min(cost(mask, weights) for mask in alternatives)
                    require(
                        cost(repaired, weights) == baseline_cost + delta == optimum,
                        f"repair is not an exact optimum: graph={graph}, "
                        f"weights={weights}, rank={rank}, failure={failure}",
                    )

    return {
        "unweighted_graphs": 1 << len(EDGES),
        "integer_cost_profiles": len(profiles),
        "feasible_fixed_rank_cases": rank_cases,
        "single_failure_queries": failure_cases,
        "feasible_exact_repairs": repairs,
        "infeasible_queries": infeasible,
        "simple_compressed_cycles_checked": simple_cycles,
    }


def main() -> None:
    report = {
        "scope": "finite signed interval and bipartite partition-matroid certificates",
        "signed_intervals": check_signed_intervals(),
        "minimum_hop_repairs": check_minimum_hop_repairs(),
        "status": "passed",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
