#!/usr/bin/env python3
"""Independent finite checks for the support-sized signed interval compiler.

Direct Boolean evaluation is the reference.  The integration suite independently
enumerates every assignment to each packed Subset Sum instance, then projects
its indexed solutions to the original variables.  It does not run or validate an
exponential-time backend, or establish an asymptotic bound by experimentation.
All arithmetic is exact, the seed is fixed, and only the standard library is used.
"""
from __future__ import annotations

from itertools import product
import json
from math import prod
import random


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def ceil_log2(value: int) -> int:
    require(value > 0, "logarithm requires a positive integer")
    return (value - 1).bit_length()


def subset_sums(row: tuple[int, ...]) -> list[int]:
    values = [0]
    for coefficient in row:
        values += [value + coefficient for value in values]
    return values


def short_intervals(row: tuple[int, ...], lower: int, upper: int):
    """Return exact interval tests and a trace; zero rows are preprocessed."""
    support = sum(coefficient != 0 for coefficient in row)
    if lower > upper:
        return [], []
    if not support:
        return ([(row, 0, 0)] if lower <= 0 <= upper else []), []
    output = []
    trace = []
    while True:
        if upper - lower + 1 <= support:
            output.append((row, lower, upper))
            return output, trace
        odd = sum(coefficient % 2 for coefficient in row)
        child_lower = -((-lower) // 2)
        child_upper = (upper - odd) // 2
        boundaries = []
        boundary_upper = min(upper, 2 * child_lower + odd - 2)
        if lower <= boundary_upper:
            boundaries.append((row, lower, boundary_upper))
        boundary_lower = max(lower, 2 * child_upper + 2)
        if boundary_lower <= upper:
            boundaries.append((row, boundary_lower, upper))
        output.extend(boundaries)
        trace.append((row, lower, upper, odd, child_lower, child_upper, boundaries))
        if child_lower > child_upper:
            return output, trace
        row = tuple(coefficient // 2 for coefficient in row)
        lower, upper = child_lower, child_upper


def check_row(row: tuple[int, ...], lower: int, upper: int, counts: dict[str, int]):
    catalogue, trace = short_intervals(row, lower, upper)
    counts["row_intervals"] += 1
    original = subset_sums(row)
    accepted = [False] * len(original)
    for emitted, start, end in catalogue:
        for mask, total in enumerate(subset_sums(emitted)):
            accepted[mask] |= start <= total <= end
    require(accepted == [lower <= total <= upper for total in original],
            f"interval equivalence: {row}, [{lower},{upper}]")
    counts["assignment_comparisons"] += len(original)
    support = sum(coefficient != 0 for coefficient in row)
    if not support or lower > upper:
        counts["preprocessed_zero_or_empty_rows"] += 1
        return
    maximum_values = min(upper - lower + 1, support)
    require(all(1 <= end - start + 1 <= maximum_values
                for _, start, end in catalogue), "emitted width bound")
    require(len(catalogue) <= 2 * ceil_log2(upper - lower + 1) + 1,
            "catalogue count bound")
    require(len(trace) <= ceil_log2(upper - lower + 1), "halving depth bound")
    counts["maximum_halving_depth"] = max(counts["maximum_halving_depth"], len(trace))
    for current, start, end, odd, child_lower, child_upper, boundaries in trace:
        counts["halving_frames"] += 1
        require(all(1 <= right - left + 1 <= odd
                    for _, left, right in boundaries), "parity-sensitive boundary width")
        if not odd:
            require(not boundaries, "even row emits no boundary")
            counts["all_even_frames"] += 1
        if child_lower > child_upper:
            counts["empty_child_frames"] += 1
        else:
            require(child_upper - child_lower <= (end - start) // 2,
                    "child width contracts")
        if len(boundaries) == 2 and boundaries[1][1] <= boundaries[0][2]:
            counts["overlapping_boundary_frames"] += 1
        rounded = tuple(coefficient // 2 for coefficient in current)
        for old_value, new_value in zip(subset_sums(current), subset_sums(rounded)):
            counts["local_rounding_comparisons"] += 1
            delta = old_value - 2 * new_value
            require(0 <= delta <= odd, "signed floor remainder")
            child_accepts = child_lower <= new_value <= child_upper
            boundary_accepts = any(left <= old_value <= right for _, left, right in boundaries)
            require((start <= old_value <= end) == (child_accepts or boundary_accepts),
                    "one-level exact disjunction")


def check_catalogues() -> dict[str, int]:
    counts = {key: 0 for key in (
        "coefficient_rows", "row_intervals", "assignment_comparisons",
        "preprocessed_zero_or_empty_rows", "halving_frames", "all_even_frames",
        "empty_child_frames", "overlapping_boundary_frames",
        "local_rounding_comparisons", "maximum_halving_depth",
    )}
    for dimension in range(4):
        for row in product(range(-4, 5), repeat=dimension):
            counts["coefficient_rows"] += 1
            minimum = sum(min(coefficient, 0) for coefficient in row) - 2
            maximum = sum(max(coefficient, 0) for coefficient in row) + 2
            for lower in range(minimum, maximum + 1):
                for upper in range(lower, maximum + 1):
                    check_row(row, lower, upper, counts)
    fixtures = [
        ((0, 0), 1, 2), ((0, 0), -2, 2), ((3, 3), 1, 3),
        ((-3, -3), -5, -3), ((2, -4, 6), -1, 8), ((1, -1), 4, 3),
        ((-1, -1, -1), -(1 << 300), (1 << 300) + 1),
        ((1 << 513, -(1 << 512), (1 << 257) + 1), -(1 << 513), 1 << 514),
    ]
    rng = random.Random(20261026)
    for _ in range(400):
        row = tuple(rng.randrange(-100, 101) for _ in range(4))
        lower, upper = sorted((rng.randrange(-400, 401), rng.randrange(-400, 401)))
        fixtures.append((row, lower, upper))
    for row, lower, upper in fixtures:
        check_row(row, lower, upper, counts)
    counts["additional_fixtures"] = len(fixtures)
    require(all(counts[key] > 0 for key in (
        "preprocessed_zero_or_empty_rows", "all_even_frames", "empty_child_frames",
        "overlapping_boundary_frames")), "edge-case coverage")
    return counts


def slack_weights(width: int) -> tuple[int, ...]:
    count = ceil_log2(width + 1)
    if not count:
        return ()
    return tuple(1 << bit for bit in range(count - 1)) + (width - ((1 << (count - 1)) - 1),)


def check_slack() -> dict[str, int]:
    assignments = 0
    for width in range(1025):
        coins = slack_weights(width)
        values = subset_sums(coins)
        require(set(values) == set(range(width + 1)), "independent slack subset sums")
        require(len(coins) == ceil_log2(width + 1), "slack bit count")
        assignments += len(values)
    return {"widths": 1025, "slack_assignments": assignments}


def compiled_solutions(n, intervals, equalities, budgets, counts):
    catalogues = []
    q_values = []
    active_budgets = []
    for (row, lower, upper), budget in zip(intervals, budgets):
        if lower > upper:
            return set()
        support = sum(coefficient != 0 for coefficient in row)
        if not support:
            if not lower <= 0 <= upper:
                return set()
            continue
        catalogue, _ = short_intervals(row, lower, upper)
        q = ceil_log2(min(upper - lower + 1, support))
        require(0 <= budget <= q, "row slack budget")
        q_values.append(q)
        active_budgets.append(budget)
        catalogues.append(catalogue)
    choices = []
    for catalogue, budget in zip(catalogues, active_budgets):
        chunks = []
        for row, lower, upper in catalogue:
            for start in range(lower, upper + 1, 1 << budget):
                chunks.append((row, start, min(upper, start + (1 << budget) - 1)))
        choices.append(chunks)
    maximum_branches = prod(len(catalogue) for catalogue in catalogues) * (
        1 << (sum(q_values) - sum(active_budgets)))
    answers = set()
    branches = 0
    for chosen in product(*choices):
        branches += 1
        equations = [(list(row), target) for row, target in equalities]
        variable_count = n
        for row, lower, upper in chosen:
            coins = slack_weights(upper - lower)
            coefficients = list(row) + [0] * (variable_count - n) + list(coins)
            variable_count += len(coins)
            equations.append((coefficients, upper))
        equations = [(tuple(row + [0] * (variable_count - len(row))), target)
                     for row, target in equations]
        require(variable_count <= n + sum(budgets), "compiled variable budget")
        radix = 1 + max((sum(map(abs, row)) + abs(target) for row, target in equations), default=0)
        packed_row = tuple(sum(row[index] * radix ** j for j, (row, _) in enumerate(equations))
                           for index in range(variable_count))
        packed_target = sum(target * radix ** j for j, (_, target) in enumerate(equations))
        original_equation_values = [(subset_sums(row), target) for row, target in equations]
        for mask, value in enumerate(subset_sums(packed_row)):
            counts["packed_assignment_comparisons"] += 1
            packed_accepts = value == packed_target
            require(packed_accepts == all(values[mask] == target
                                          for values, target in original_equation_values),
                    "signed radix equivalence")
            if packed_accepts:
                answers.add(mask & ((1 << n) - 1))
        counts["packed_instances"] += 1
    require(branches <= maximum_branches, "total branch upper bound")
    return answers


def check_compilation() -> dict[str, int]:
    counts = {key: 0 for key in (
        "systems", "budget_profiles", "packed_instances", "packed_assignment_comparisons",
        "original_assignment_comparisons", "optimization_comparisons",
    )}
    rng = random.Random(20261027)
    cases = [
        (0, [], []), (0, [((), -1, 1)], []), (0, [((), 1, 2)], []),
        (2, [((3, 3), 1, 3), ((-3, 2), -2, 1)], []),
        (3, [((1, 1, 1), 0, 2)], [((0, 0, 0), 1)]),
        (3, [((0, 0, 0), 0, 0), ((2, -1, 3), 1, 1)], [((1, 0, -1), 0)]),
        (3, [((1, -1, 2), 4, 3)], []),
    ]
    for index in range(300):
        n = rng.randrange(1, 5)
        intervals = []
        for _ in range(rng.randrange(3)):
            row = tuple(rng.randrange(-5, 6) for _ in range(n))
            lower, upper = sorted((rng.randrange(-8, 9), rng.randrange(-8, 9)))
            intervals.append((row, lower, upper))
        equalities = []
        for _ in range(rng.randrange(3)):
            row = tuple(rng.randrange(-4, 5) for _ in range(n))
            target = rng.randrange(-6, 7)
            if index % 3 == 0:
                target = subset_sums(row)[rng.randrange(1 << n)]
            equalities.append((row, target))
        cases.append((n, intervals, equalities))
    for n, intervals, equalities in cases:
        counts["systems"] += 1
        original = {mask for mask in range(1 << n)
                    if all(lower <= subset_sums(row)[mask] <= upper for row, lower, upper in intervals)
                    and all(subset_sums(row)[mask] == target for row, target in equalities)}
        objective = tuple(rng.randrange(-5, 6) for _ in range(n))
        objective_values = subset_sums(objective)
        budget_ranges = []
        for row, lower, upper in intervals:
            support = sum(coefficient != 0 for coefficient in row)
            q = ceil_log2(min(upper - lower + 1, support)) if support and lower <= upper else 0
            budget_ranges.append(range(q + 1))
        for budgets in product(*budget_ranges):
            counts["budget_profiles"] += 1
            actual = compiled_solutions(n, intervals, equalities, budgets, counts)
            require(actual == original, "complete compiled system solution projection")
            counts["original_assignment_comparisons"] += 1 << n
            require(min((objective_values[mask] for mask in actual), default=None)
                    == min((objective_values[mask] for mask in original), default=None),
                    "signed objective optimum on indexed solutions")
            counts["optimization_comparisons"] += 1
    return counts


def main() -> None:
    require(__debug__, "run without -O: this is a verification program")
    print(json.dumps({
        "scope": "support-sized signed interval catalogues, slack and exact signed radix compilation",
        "catalogues": check_catalogues(),
        "slack": check_slack(),
        "compilation": check_compilation(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
