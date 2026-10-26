#!/usr/bin/env python3
"""Check the deterministic retained-prefix algorithm against full rank tables.

The construction uses independence queries on the retained earlier prefix.
The reference computes canonical acceptance from ranks of the ORIGINAL
earlier prefix, and enumerates every failure set. Exact integer probability
weights additionally test the Bernoulli event on failures above the budget.

The fixture generators are shared with the separate rank-summary and
weighted-obstruction checkers. No algorithm under test is imported from
them. Python's standard library is the only implementation dependency.
"""
from __future__ import annotations

from collections import Counter
from itertools import product
import json

from check_summaries import all_matroid_rank_tables
from check_weighted_obstruction import ITEMS, independent as obstruction_independent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def bits(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def survivors(ground: int, labels: tuple[int, ...], failed: int) -> int:
    return sum(1 << e for e in bits(ground) if not labels[e] & failed)


def prefix_summary(labels, budget, order, independent):
    """Construct only with the retained prefix; count every oracle call."""
    retained = 0
    witnesses = {}
    query_count = node_count = 0

    def query(mask):
        nonlocal query_count
        query_count += 1
        return independent(mask)

    for protected in order:
        protected_bit = 1 << protected

        def search(current, remaining, failed):
            nonlocal node_count
            node_count += 1
            basis = 0
            for e in bits(current):
                candidate = basis | (1 << e)
                if query(candidate):
                    basis = candidate
            if query(basis | protected_bit):
                return failed
            if remaining == 0:
                return None
            branch_labels = 0
            for e in bits(basis):
                branch_labels |= labels[e]
            branch_labels &= ~labels[protected]
            for label in bits(branch_labels):
                label_bit = 1 << label
                answer = search(survivors(current, labels, label_bit),
                                remaining - 1, failed | label_bit)
                if answer is not None:
                    return answer
            return None

        witness = search(retained, budget, 0)
        if witness is not None:
            retained |= protected_bit
            witnesses[protected] = witness
    return retained, witnesses, query_count, node_count


def all_failures(universe: int):
    failed = universe
    while True:
        yield failed
        if failed == 0:
            return
        failed = (failed - 1) & universe


def verify_case(ranks, labels, budget, order, counts):
    size = len(labels)
    ground = (1 << size) - 1
    rank = ranks[ground]
    degree = max((label.bit_count() for label in labels), default=0)
    independent = lambda mask: ranks[mask] == mask.bit_count()
    retained, witnesses, queries, nodes = prefix_summary(
        labels, budget, order, independent,
    )
    if budget and degree:
        numerator = (budget + degree) ** (budget + degree)
        denominator = budget ** budget * degree ** degree
        bound = min(size, rank * numerator // denominator)
    else:
        bound = min(size, rank)
    require(retained.bit_count() <= bound, "Bernoulli retained-size bound")
    tree_bound = sum((degree * rank) ** depth for depth in range(budget + 1))
    require(queries <= size * (bound + 1) * tree_bound,
            "support-sensitive independence-query bound")
    require(nodes <= size * tree_bound, "bounded-depth node count")

    universe = 0
    for label in labels:
        universe |= label
    reference_union = 0
    expected_rank_numerator = event_sum_numerator = 0
    label_count = universe.bit_count()
    for failed in all_failures(universe):
        alive = survivors(ground, labels, failed)
        allowed = failed.bit_count() <= budget
        prefix = canonical_basis = 0
        for e in order:
            previous_rank = ranks[prefix]
            if alive >> e & 1:
                prefix |= 1 << e
            increment = ranks[prefix] - previous_rank
            require(increment in (0, 1), "matroid prefix increment")
            if increment:
                canonical_basis |= 1 << e
            if allowed:
                require(ranks[prefix & retained] == ranks[prefix],
                        "every original surviving prefix rank")
                counts["original_prefix_rank_comparisons"] += 1
            if e in witnesses:
                witness = witnesses[e]
                event = witness & ~failed == 0 and labels[e] & failed == 0
                if event:
                    require(increment == 1, "Bernoulli event forces original rank increment")
                    counts["bernoulli_event_implications"] += 1
        require(canonical_basis.bit_count() == ranks[alive],
                "full original-prefix reference basis rank")
        if allowed:
            reference_union |= canonical_basis
            counts["allowed_failure_queries"] += 1
        if budget and degree:
            weight = budget ** failed.bit_count() * degree ** (
                label_count - failed.bit_count()
            )
            expected_rank_numerator += weight * ranks[alive]

    require(retained == reference_union, "exact canonical-basis union")
    prefix = 0
    for e in order:
        if e in witnesses:
            witness = witnesses[e]
            require(witness.bit_count() <= budget and not witness & labels[e],
                    "allowed necessity witness")
            original_earlier = survivors(prefix, labels, witness)
            require(ranks[original_earlier | (1 << e)] == ranks[original_earlier] + 1,
                    "necessity in the original earlier prefix")
            counts["necessity_witnesses"] += 1
            if budget and degree:
                remaining_labels = label_count - witness.bit_count() - labels[e].bit_count()
                require(remaining_labels >= 0, "disjoint label events")
                event_sum_numerator += (
                    budget ** witness.bit_count()
                    * degree ** labels[e].bit_count()
                    * (budget + degree) ** remaining_labels
                )
        prefix |= 1 << e
    if budget and degree:
        require(event_sum_numerator <= expected_rank_numerator,
                "nonuniform event sum below exact expected rank")
        require(expected_rank_numerator <= rank * (budget + degree) ** label_count,
                "exact expected rank below original rank")
        counts["nonuniform_bernoulli_inequalities"] += 1
    counts["instances"] += 1
    counts["independence_queries"] += queries
    counts["witness_search_nodes"] += nodes
    counts["strict_reductions"] += retained != ground
    return retained


def check_all_small_matroids():
    counts = Counter()
    matroid_count = 0
    for size in range(5):
        # All overlapping lists on three labels through n=3; all lists on
        # two labels at n=4. Every possible budget up to that alphabet is used.
        label_count = 3 if size <= 3 else 2
        for ranks in all_matroid_rank_tables(size):
            matroid_count += 1
            for labels in product(range(1 << label_count), repeat=size):
                for budget in range(label_count + 1):
                    verify_case(ranks, labels, budget, tuple(range(size)), counts)
    require(matroid_count == 92, "all labeled matroids on n<=4")
    counts["labeled_matroids"] = matroid_count
    return dict(counts)


def check_nonrepresentable_fixture():
    counts = Counter()
    size = len(ITEMS)
    ranks = [0] * (1 << size)
    # Rank is computed from all independent subsets by an exhaustive
    # subset recurrence, separately from both greedy and the witness search.
    for mask in range(1, len(ranks)):
        if obstruction_independent(mask):
            ranks[mask] = mask.bit_count()
        else:
            ranks[mask] = max(ranks[mask ^ (1 << e)] for e in bits(mask))
    labels = tuple(1 << (ord(color) - ord("A")) for _, color in ITEMS)
    natural = tuple(range(size))
    orders = set()
    for shift in range(size):
        rotated = natural[shift:] + natural[:shift]
        orders.add(rotated)
        orders.add(tuple(reversed(rotated)))
    for order in sorted(orders):
        for budget in range(5):
            retained = verify_case(ranks, labels, budget, order, counts)
            if order == natural and budget == 2:
                require(retained.bit_count() == 13, "known 13-item sharp-bound obstruction")
    counts["complete_rank_table_entries"] = len(ranks)
    counts["fixed_orders"] = len(orders)
    return dict(counts)


def main():
    require(__debug__, "run without -O; exact verification must stay enabled")
    print(json.dumps({
        "status": "passed",
        "algorithm": "deterministic retained-prefix failure-witness search",
        "small_matroids": check_all_small_matroids(),
        "nonrepresentable_rank_four": check_nonrepresentable_fixture(),
        "scope": "finite matroid checks; integral-submodular corollary proved separately",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
