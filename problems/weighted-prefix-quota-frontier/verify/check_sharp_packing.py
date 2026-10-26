#!/usr/bin/env python3
"""Check sharp sparse-packing restrictions against exhaustive finite contexts.

The reduction uses only an independence oracle, implemented here by explicit
independent-set families. The exhaustive reference enumerates every original
feasible set and every possible single replacement; it does not reuse the
failure-summary proof to decide feasibility. The suite includes every labeled
matroid on four elements, overlapping packing labels, equal-profit and
arbitrary-profit ordered reductions, the capacity-sensitive saturated-row
budget, and the exact forcing family.

This is finite evidence, not a proof of the asymptotic theorem. Only the
Python standard library is used. The deterministic JSON report is written
to stdout; the checker modifies no files.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from math import comb


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def bits(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def four_element_matroids() -> list[frozenset[int]]:
    """Enumerate set families and check the hereditary/augmentation axioms."""
    output = []
    subsets = tuple(range(16))
    for encoded in range(1, 1 << 16, 2):  # The empty set must be independent.
        independent = frozenset(s for s in subsets if encoded >> s & 1)
        if any(
            s ^ (1 << e) not in independent
            for s in independent for e in bits(s)
        ):
            continue
        if any(
            not any(a | (1 << e) in independent for e in bits(b & ~a))
            for a in independent for b in independent
            if a.bit_count() < b.bit_count()
        ):
            continue
        output.append(independent)
    return output


def greedy_basis(ground: int, independent) -> int:
    basis = 0
    for e in bits(ground):
        if independent(basis | (1 << e)):
            basis |= 1 << e
    return basis


def sharp_summary(ground: int, labels: tuple[int, ...], budget: int, independent):
    """Direct witness search, without the optional return-input size gate."""
    current = ground
    nodes = 0
    for protected in tuple(bits(ground)):
        protected_bit = 1 << protected

        def witness(others: int, remaining: int):
            nonlocal nodes
            nodes += 1
            basis = greedy_basis(others, independent)
            if independent(basis | protected_bit):
                return 0
            if remaining == 0:
                return None
            branch_labels = 0
            for e in bits(basis):
                branch_labels |= labels[e]
            branch_labels &= ~labels[protected]
            for label in bits(branch_labels):
                label_bit = 1 << label
                surviving = sum(
                    1 << e for e in bits(others) if not labels[e] & label_bit
                )
                answer = witness(surviving, remaining - 1)
                if answer is not None:
                    return answer | label_bit
            return None

        if witness(current & ~protected_bit, budget) is None:
            current &= ~protected_bit
    return current, nodes


def weighted_prefix_summary(ground, labels, budget, profits, independent):
    """One ordered pass; witness searches use only retained earlier items."""
    retained = nodes = 0
    for protected in sorted(bits(ground), key=lambda e: (-profits[e], e)):
        protected_bit = 1 << protected

        def witness(earlier, remaining):
            nonlocal nodes
            nodes += 1
            basis = greedy_basis(earlier, independent)
            if independent(basis | protected_bit):
                return True
            if remaining == 0:
                return False
            branch_labels = 0
            for e in bits(basis):
                branch_labels |= labels[e]
            branch_labels &= ~labels[protected]
            for label in bits(branch_labels):
                surviving = sum(
                    1 << e for e in bits(earlier) if not labels[e] & (1 << label)
                )
                if witness(surviving, remaining - 1):
                    return True
            return False

        if witness(retained, budget):
            retained |= protected_bit
    return retained, nodes


def bernoulli_bound(rank, budget, degree):
    if not budget or not degree:
        return rank
    return rank * (budget + degree) ** (budget + degree) // (
        budget ** budget * degree ** degree
    )


def packing_feasible(mask: int, labels: tuple[int, ...], capacities: tuple[int, ...]):
    return all(
        sum(bool(labels[e] >> row & 1) for e in bits(mask)) <= capacity
        for row, capacity in enumerate(capacities)
    )


def check_oracle_restrictions() -> dict[str, int]:
    matroids = four_element_matroids()
    require(len(matroids) == 68, f"four-element matroid count: {len(matroids)}")
    profit_profiles = ((0, 0, 0, 0), (-2, 3, -2, 3), (-7, 1, 5, -3))
    instance_count = context_count = replacement_count = search_nodes = 0
    strict_reductions = capacity_improvements = 0
    weighted_nodes = weighted_replacements = weighted_reductions = 0
    # Every 2-row incidence pattern is included, so supports may overlap or
    # coincide, and individual items can have zero, one, or two labels.
    for independent_family in matroids:
        for original_labels in product(range(4), repeat=4):
            for capacities in product((1, 2), repeat=2):
                # Cardinality two exhausts both saturated-label and truncation
                # behavior on this four-item family. Larger tight examples are
                # checked separately below.
                def independent(mask):
                    return mask.bit_count() <= 2 and mask in independent_family

                eligible = sum(1 << e for e in range(4) if independent(1 << e))
                rank = greedy_basis(eligible, independent).bit_count()
                if rank == 0:
                    continue
                active_rows = sum(
                    1 << j for j, capacity in enumerate(capacities)
                    if capacity < rank
                )
                labels = tuple(value & active_rows for value in original_labels)
                degree = max(labels[e].bit_count() for e in bits(eligible))
                loads = sorted((
                    sum((Fraction(1, capacities[j]) for j in bits(labels[e])),
                        Fraction(0))
                    for e in bits(eligible)
                ), reverse=True)
                budget = int(sum(loads[:rank - 1], Fraction(0)))
                budget = min(budget, active_rows.bit_count())
                require(budget <= degree * (rank - 1), "capacity budget bound")
                if budget < degree * (rank - 1):
                    capacity_improvements += 1
                feasible = tuple(
                    mask for mask in range(16)
                    if mask & ~eligible == 0 and independent(mask)
                    and packing_feasible(mask, original_labels, capacities)
                )
                for context in feasible:
                    if context.bit_count() <= rank - 1:
                        saturated = sum(
                            sum(bool(labels[e] >> j & 1) for e in bits(context))
                            == capacities[j]
                            for j in bits(active_rows)
                        )
                        require(saturated <= budget, "saturated-row load certificate")
                for profits in profit_profiles:
                    instance_count += 1
                    retained = rank_sum = 0
                    for value in sorted(set(profits)):
                        group = sum(
                            1 << e for e in bits(eligible) if profits[e] == value
                        )
                        rank_sum += greedy_basis(group, independent).bit_count()
                        summary, nodes = sharp_summary(group, labels, budget, independent)
                        retained |= summary
                        search_nodes += nodes
                    require(
                        retained.bit_count() <= rank_sum * comb(budget + degree, degree),
                        "binomial retained-size bound",
                    )
                    if retained != eligible:
                        strict_reductions += 1
                    weighted_retained, nodes = weighted_prefix_summary(
                        eligible, labels, budget, profits, independent,
                    )
                    weighted_nodes += nodes
                    weighted_reductions += weighted_retained != eligible
                    require(
                        weighted_retained.bit_count() <= bernoulli_bound(rank, budget, degree),
                        "arbitrary-profit Bernoulli retained-size bound",
                    )
                    for selected in feasible:
                        context_count += 1
                        for protected in bits(selected):
                            replacement_count += 1
                            context = selected ^ (1 << protected)
                            require(any(
                                profits[e] == profits[protected]
                                and independent(context | (1 << e))
                                and packing_feasible(
                                    context | (1 << e), original_labels, capacities
                                )
                                for e in bits(retained & ~context)
                            ), "original-context, equal-profit replacement")
                            weighted_replacements += 1
                            require(any(
                                profits[e] >= profits[protected]
                                and independent(context | (1 << e))
                                and packing_feasible(
                                    context | (1 << e), original_labels, capacities
                                )
                                for e in bits(weighted_retained & ~context)
                            ), "original-context, no-worse-profit replacement")
                    for cardinality in range(rank + 1):
                        original_values = [
                            sum(profits[e] for e in bits(s))
                            for s in feasible if s.bit_count() == cardinality
                        ]
                        retained_values = [
                            sum(profits[e] for e in bits(s))
                            for s in feasible
                            if s.bit_count() == cardinality and s & ~retained == 0
                        ]
                        require(
                            (max(original_values) if original_values else None)
                            == (max(retained_values) if retained_values else None),
                            "fixed-cardinality optimum preservation",
                        )
                        weighted_values = [
                            sum(profits[e] for e in bits(s))
                            for s in feasible
                            if s.bit_count() == cardinality and s & ~weighted_retained == 0
                        ]
                        require(
                            (max(original_values) if original_values else None)
                            == (max(weighted_values) if weighted_values else None),
                            "arbitrary-profit fixed-cardinality optimum preservation",
                        )
    return {
        "all_labeled_matroids_on_four_elements": len(matroids),
        "packing_and_profit_instances": instance_count,
        "original_feasible_sets": context_count,
        "single_replacement_requirements": replacement_count,
        "witness_search_nodes": search_nodes,
        "strict_ground_reductions": strict_reductions,
        "capacity_budget_improvements": capacity_improvements,
        "arbitrary_profit_replacement_requirements": weighted_replacements,
        "arbitrary_profit_witness_search_nodes": weighted_nodes,
        "arbitrary_profit_strict_reductions": weighted_reductions,
    }


def check_capacity_and_weighted_endpoint() -> dict[str, int]:
    """Exercise nontrivial higher capacities and the one-failure cost endpoint."""
    cases = (
        ((1, 1, 2, 2, 4, 4), (2, 2, 2), 4),
        ((1, 1, 1, 2, 2, 2, 4, 4), (3, 3, 3), 4),
        ((3, 3, 5, 5, 6, 6), (2, 2, 2), 4),
        ((1, 2, 4, 8, 1, 2, 4, 8), (3, 3, 3, 3), 4),
    )
    inequalities = replacements = weighted_replacements = strict_improvements = 0
    for labels, capacities, rank in cases:
        size = len(labels)
        ground = (1 << size) - 1
        degree = max(value.bit_count() for value in labels)
        loads = sorted((sum((Fraction(1, capacities[j]) for j in bits(label)),
                            Fraction(0)) for label in labels), reverse=True)
        budget = min(len(capacities), int(sum(loads[:rank - 1], Fraction(0))))
        require(budget < degree * (rank - 1), "targeted capacity improvement")
        strict_improvements += 1

        def independent(mask):
            return mask.bit_count() <= rank

        feasible = tuple(
            mask for mask in range(1 << size)
            if independent(mask) and packing_feasible(mask, labels, capacities)
        )
        summary, _ = sharp_summary(ground, labels, budget, independent)
        require(summary.bit_count() <= rank * comb(budget + degree, degree),
                "capacity-sensitive summary size")
        for selected in feasible:
            if selected.bit_count() <= rank - 1:
                saturated = sum(
                    sum(bool(labels[e] >> j & 1) for e in bits(selected)) == capacity
                    for j, capacity in enumerate(capacities)
                )
                require(saturated <= budget, "higher-capacity saturated-row bound")
                inequalities += 1
            for protected in bits(selected):
                context = selected ^ (1 << protected)
                require(any(
                    independent(context | (1 << e))
                    and packing_feasible(context | (1 << e), labels, capacities)
                    for e in bits(summary & ~context)
                ), "higher-capacity original-context replacement")
                replacements += 1

        if budget <= 1:
            profits = tuple(3 * e - size for e in range(size))
            order = sorted(range(size), key=lambda e: (-profits[e], e))

            def ordered_basis(pool):
                basis = 0
                for e in order:
                    if pool >> e & 1 and independent(basis | (1 << e)):
                        basis |= 1 << e
                return basis

            baseline = ordered_basis(ground)
            touched = 0
            for e in bits(baseline):
                touched |= labels[e]
            retained = baseline
            for label in bits(touched):
                survivors = sum(1 << e for e in range(size)
                                if not labels[e] >> label & 1)
                retained |= ordered_basis(survivors)
            require(retained.bit_count() <= (degree + 1) * rank,
                    "one-failure weighted endpoint size")
            for selected in feasible:
                for protected in bits(selected):
                    context = selected ^ (1 << protected)
                    require(any(
                        profits[e] >= profits[protected]
                        and independent(context | (1 << e))
                        and packing_feasible(context | (1 << e), labels, capacities)
                        for e in bits(retained & ~context)
                    ), "one-failure no-worse-profit replacement")
                    weighted_replacements += 1
    return {
        "higher_capacity_instances": len(cases),
        "strict_budget_improvements": strict_improvements,
        "saturated_row_inequalities": inequalities,
        "unweighted_replacement_requirements": replacements,
        "arbitrary_profit_one_failure_replacements": weighted_replacements,
    }


def check_forcing_family() -> dict[str, int]:
    instances = forced_items = candidate_replacements = 0
    for rank in range(1, 5):
        for degree in range(1, 4):
            rows = rank * degree
            supports = tuple(
                sum(1 << j for j in chosen)
                for chosen in combinations(range(rows), degree)
            )
            items = tuple((group, support) for group in range(rank) for support in supports)
            require(len(items) == rank * comb(rank * degree, degree), "forcing size")
            instances += 1
            for protected, (group, support) in enumerate(items):
                remaining = [j for j in range(rows) if not support >> j & 1]
                context = []
                for index, other_group in enumerate(g for g in range(rank) if g != group):
                    block = sum(1 << j for j in remaining[index * degree:(index + 1) * degree])
                    context.append((other_group, block))
                require(len({g for g, _ in context}) == rank - 1, "context resource")
                occupied = 0
                for _, block in context:
                    require(not occupied & block, "context packing")
                    occupied |= block
                valid = []
                used_groups = {g for g, _ in context}
                for candidate, (candidate_group, candidate_support) in enumerate(items):
                    candidate_replacements += 1
                    if candidate_group not in used_groups and not candidate_support & occupied:
                        valid.append(candidate)
                require(valid == [protected], "each original item is forced")
                forced_items += 1
    return {
        "parameter_pairs": instances,
        "forced_original_items": forced_items,
        "candidate_replacement_checks": candidate_replacements,
    }


def main() -> None:
    require(__debug__, "run with assertions enabled")
    print(json.dumps({
        "status": "passed",
        "scope": "finite oracle restrictions, equal/no-worse-profit replacements, and forcing examples",
        "oracle_restrictions": check_oracle_restrictions(),
        "capacity_and_weighted_endpoint": check_capacity_and_weighted_endpoint(),
        "forcing_family": check_forcing_family(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
