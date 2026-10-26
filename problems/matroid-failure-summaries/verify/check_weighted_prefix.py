#!/usr/bin/env python3
"""Check two deterministic prefix algorithms against complete oracle tables.

The constructions branch on ordered bases, or use independence queries on
the retained earlier prefix.
The reference computes canonical acceptance from ranks of the ORIGINAL
earlier prefix, and enumerates every failure set. Exact integer probability
weights additionally test the Bernoulli event on failures above the budget.

The fixture generators are shared with the separate rank-summary and
weighted-obstruction checkers. No algorithm under test is imported from
them. Python's standard library is the only implementation dependency.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import json
from math import comb

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


def ordered_basis_tree(labels, budget, order, independent):
    """Rescan the original input at each bounded-depth basis branch."""
    retained = 0
    query_count = node_count = 0

    def visit(failed, remaining):
        nonlocal retained, query_count, node_count
        node_count += 1
        basis = branch_labels = 0
        for e in order:
            if labels[e] & failed:
                continue
            query_count += 1
            if independent(basis | (1 << e)):
                basis |= 1 << e
                branch_labels |= labels[e]
        retained |= basis
        if remaining:
            for label in bits(branch_labels):
                require(not failed >> label & 1, "each tree branch fails a new label")
                visit(failed | (1 << label), remaining - 1)

    visit(0, budget)
    return retained, query_count, node_count


def ordered_value_tree(labels, budget, order, value):
    """Keep only positive marginal items, caching the empty-set baseline."""
    retained = 0
    baseline = value(0)
    query_count, node_count = 1, 0

    def visit(failed, remaining):
        nonlocal retained, query_count, node_count
        node_count += 1
        basis = branch_labels = 0
        current_value = baseline
        for e in order:
            if labels[e] & failed:
                continue
            query_count += 1
            enlarged = basis | (1 << e)
            enlarged_value = value(enlarged)
            if enlarged_value > current_value:
                basis, current_value = enlarged, enlarged_value
                branch_labels |= labels[e]
        retained |= basis
        if remaining:
            for label in bits(branch_labels):
                require(not failed >> label & 1, "each value branch fails a new label")
                visit(failed | (1 << label), remaining - 1)

    visit(0, budget)
    return retained, query_count, node_count


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


def two_failure_bound(rank: int) -> int:
    if rank <= 1:
        return 3 * rank
    return min(5 * rank, comb(rank + 1, 2) + 3)


def verify_case(ranks, labels, budget, order, counts):
    size = len(labels)
    ground = (1 << size) - 1
    rank = ranks[ground]
    degree = max((label.bit_count() for label in labels), default=0)
    independent = lambda mask: ranks[mask] == mask.bit_count()
    retained, witnesses, queries, nodes = prefix_summary(
        labels, budget, order, independent,
    )
    tree_retained, tree_queries, tree_nodes = ordered_basis_tree(
        labels, budget, order, independent,
    )
    require(tree_retained == retained, "both constructions return the same canonical union")
    original_basis = original_prefix = 0
    for e in order:
        enlarged = original_prefix | (1 << e)
        if ranks[enlarged] > ranks[original_prefix]:
            original_basis |= 1 << e
        original_prefix = enlarged
    require(original_basis.bit_count() == rank, "unfailed canonical basis")
    require(not original_basis & ~retained, "original basis retained")
    require(all(witnesses[e] == 0 for e in bits(original_basis)),
            "original basis has empty failure witnesses")
    if budget and degree:
        numerator = (budget + degree) ** (budget + degree)
        denominator = budget ** budget * degree ** degree
        gamma_bound = rank * numerator // denominator
        # The degree-one choice is the exact optimizer of the stronger
        # parameter-only bound. Otherwise the original Gamma optimizer
        # still gives a strict, certified original-basis improvement.
        failed_weight, alive_weight = budget, degree
        if degree == 1 and budget >= 2:
            failed_weight, alive_weight = budget - 1, 1
        total_weight = failed_weight + alive_weight
        base_numerator = sum(
            alive_weight ** labels[e].bit_count()
            * total_weight ** (degree - labels[e].bit_count())
            for e in bits(original_basis)
        )
        refined_bound = rank + (
            (rank * total_weight ** degree - base_numerator)
            * total_weight ** budget
            // (failed_weight ** budget * alive_weight ** degree)
        )
        bound = min(size, gamma_bound, refined_bound)
        if budget == 1:
            bound = min(bound, (degree + 1) * rank)
        if budget == 2 and degree == 1:
            circuit_bound = min(size, two_failure_bound(rank))
            counts["circuit_bound_improvements"] += circuit_bound < bound
            bound = min(bound, circuit_bound)
        counts["strict_parameter_bound_improvements"] += refined_bound < gamma_bound
        counts["strict_gated_bound_improvements"] += bound < min(size, gamma_bound)
        counts["original_basis_refined_inequalities"] += 1
    else:
        bound = min(size, rank)
    require(retained.bit_count() <= bound, "original-basis refined retained-size bound")
    tree_bound = sum((degree * rank) ** depth for depth in range(budget + 1))
    require(queries <= size * (bound + 1) * tree_bound,
            "support-sensitive independence-query bound")
    require(nodes <= size * tree_bound, "bounded-depth node count")
    require(tree_nodes <= tree_bound and tree_queries <= size * tree_bound,
            "ordered-basis tree oracle and node bounds")

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
            weight = failed_weight ** failed.bit_count() * alive_weight ** (
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
                    failed_weight ** witness.bit_count()
                    * alive_weight ** labels[e].bit_count()
                    * total_weight ** remaining_labels
                )
        prefix |= 1 << e
    if budget and degree:
        require(event_sum_numerator <= expected_rank_numerator,
                "nonuniform event sum below exact expected rank")
        require(expected_rank_numerator <= rank * total_weight ** label_count,
                "exact expected rank below original rank")
        counts["nonuniform_bernoulli_inequalities"] += 1
    counts["instances"] += 1
    counts["independence_queries"] += queries
    counts["witness_search_nodes"] += nodes
    counts["basis_tree_independence_queries"] += tree_queries
    counts["basis_tree_nodes"] += tree_nodes
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


def verify_two_failure_profile(ranks, labels, order, counts):
    """Check the d=1 profile bound, including losses under arbitrary failures."""
    require(all(label.bit_count() <= 1 for label in labels), "disjoint color classes")
    size = len(labels)
    rank = ranks[(1 << size) - 1]
    universe = 0
    for label in labels:
        universe |= label

    def original_greedy(failed):
        earlier = basis = 0
        for e in order:
            if labels[e] & failed:
                continue
            enlarged = earlier | (1 << e)
            if ranks[enlarged] > ranks[earlier]:
                basis |= 1 << e
            earlier = enlarged
        return basis, ranks[earlier]

    base, _ = original_greedy(0)
    multiplicities = Counter()
    losses = {}
    for label in bits(universe):
        basis, surviving_rank = original_greedy(1 << label)
        for e in bits(basis & ~base):
            multiplicities[e] += 1
        losses[label] = rank - surviving_rank
    total_replacements = sum(multiplicities.values())
    unlabelled_base = sum(labels[e] == 0 for e in bits(base))
    require(total_replacements == rank - unlabelled_base - sum(losses.values()),
            "single-failure replacement/loss accounting")
    profile_bound = rank + 2 * total_replacements + sum(
        comb(value - 1, 2) for value in multiplicities.values() if value >= 3
    )
    union = 0
    for failed in all_failures(universe):
        basis, surviving_rank = original_greedy(failed)
        require(surviving_rank <= rank - sum(losses[label] for label in bits(failed)),
                "superadditive rank loss for disjoint color classes")
        counts["rank_loss_inequalities"] += 1
        if failed.bit_count() <= 2:
            union |= basis
    actual = union.bit_count()
    require(actual <= profile_bound, "one-failure-profile support bound")
    require(actual <= rank + 4 * total_replacements, "rank-loss-adjusted five-rank bound")
    require(actual <= two_failure_bound(rank), "circuit-refined universal two-failure bound")
    if max(multiplicities.values(), default=0) <= 2:
        require(actual <= 3 * rank, "bounded replacement-overlap sharp bound")
        counts["multiplicity_at_most_two_cases"] += 1
    counts["instances"] += 1
    counts["rank_drop_instances"] += any(losses.values())
    counts["unlabelled_base_instances"] += unlabelled_base > 0
    counts["loop_instances"] += any(ranks[1 << e] == 0 for e in range(size))
    return actual, profile_bound, tuple(sorted(multiplicities.values()))


def check_small_two_failure_profiles():
    counts = Counter()
    matroid_count = 0
    for size in range(5):
        for ranks in all_matroid_rank_tables(size):
            matroid_count += 1
            for labels in product((0, 1, 2, 4), repeat=size):
                verify_two_failure_profile(ranks, labels, tuple(range(size)), counts)
    require(matroid_count == 92, "profile fixture enumeration")
    counts["labeled_matroids"] = matroid_count
    return dict(counts)


def check_rank_three_line_patterns():
    """Exhaust all point incidences permitted by the quadrangle line lemma."""
    sides = tuple(combinations(range(4), 2))
    stars = tuple(sum(1 << i for i, edge in enumerate(sides) if vertex in edge)
                  for vertex in range(4))
    all_sides = (1 << len(sides)) - 1
    patterns = cases = winning_cases = 0
    for on_lines in range(1 << len(sides)):
        if on_lines != all_sides and any(
            (on_lines & star).bit_count() >= 2 and on_lines != star
            for star in stars
        ):
            continue
        # The all-lines pattern is a loop. Every other permitted pattern
        # is a matching of side-lines or the three-line star of a parallel point.
        patterns += 1
        for own_color in (-1, 0, 1, 2, 3):
            survives = all_sides if own_color == -1 else stars[own_color]
            wins = survives & ~on_lines
            require(not wins or wins.bit_count() >= 2,
                    "first later winner serves at least two failed-pair queries")
            cases += 1
            winning_cases += bool(wins)
    require(patterns == 15 and cases == 75, "complete local incidence enumeration")
    return {"line_membership_patterns": patterns, "color_cases": cases,
            "positive_winner_cases": winning_cases}


def check_circuit_extensions():
    """Enumerate basis families, without assuming the multipartite lemma.

    A circuit C of size m forces every (m-1)-subset of C to be a basis.
    A nonloop extension y can add any nonempty subfamily of the bases
    {y} union (C minus a pair). Every candidate family is independently
    accepted or rejected by the complete basis-exchange axiom.
    """
    counts = Counter()
    expected_valid = {2: 1, 3: 4, 4: 14, 5: 51}
    for size in range(2, 6):
        circuit = (1 << size) - 1
        new_bit = 1 << size
        rank = size - 1
        pairs = tuple(combinations(range(size), 2))
        mandatory = {circuit ^ (1 << e) for e in range(size)}
        optional = tuple((circuit ^ (1 << a) ^ (1 << b)) | new_bit
                         for a, b in pairs)
        valid_count = 0
        for selection in range(1, 1 << len(optional)):
            counts["candidate_basis_families"] += 1
            bases = mandatory | {optional[i] for i in bits(selection)}
            valid = True
            exchange_checks = 0
            for left in bases:
                for right in bases:
                    for e in bits(left & ~right):
                        exchange_checks += 1
                        if not any((left ^ (1 << e) | (1 << f)) in bases
                                   for f in bits(right & ~left)):
                            valid = False
                            break
                    if not valid:
                        break
                if not valid:
                    break
            if not valid:
                continue
            counts["valid_basis_exchange_conditions"] += exchange_checks
            valid_count += 1
            ranks = tuple(max((mask & base).bit_count() for base in bases)
                          for mask in range(1 << (size + 1)))
            counts["complete_rank_table_entries"] += len(ranks)
            require(ranks[circuit] == ranks[circuit | new_bit] == rank,
                    "circuit and spanning extension ranks")
            require(ranks[new_bit] == 1, "nonloop extension")
            require(all(ranks[mask] == mask.bit_count()
                        for mask in range(circuit)), "all proper circuit subsets independent")

            wins = set()
            for a, b in pairs:
                surviving = circuit ^ (1 << a) ^ (1 << b)
                if ranks[surviving | new_bit] > ranks[surviving]:
                    wins.add((a, b))
            nonedge_classes = tuple(frozenset(
                b for b in range(size)
                if a == b or tuple(sorted((a, b))) not in wins
            ) for a in range(size))
            require(all(nonedge_classes[a] == nonedge_classes[b]
                        for a in range(size) for b in nonedge_classes[a]),
                    "rank-derived nonedges form equivalence classes")
            require(len(set(nonedge_classes)) >= 2,
                    "nonloop extension gives at least two parts")
            require(len(wins) >= size - 1, "nonloop circuit extension wins enough pairs")
            for own_color in range(-1, size):
                surviving_wins = {pair for pair in wins if own_color not in pair}
                require(not surviving_wins or len(surviving_wins) >= size - 2,
                        "first later winner serves at least rank minus one queries")
                if own_color == -1:
                    require(len(surviving_wins) >= size - 1,
                            "outside-color extension wins at least rank queries")
                counts["own_color_cases"] += 1
                counts["positive_winner_cases"] += bool(surviving_wins)
        require(valid_count == expected_valid[size], "complete circuit-extension enumeration")
        counts["valid_extensions"] += valid_count
    return dict(counts)


def check_few_label_coarsenings(ranks, original_labels, orders):
    """Check all maps of four colors into three colors or the unlabelled core."""
    counts = Counter()
    size = len(original_labels)
    rank = ranks[(1 << size) - 1]
    for mapping in product((0, 1, 2, 4), repeat=4):
        labels = tuple(mapping[label.bit_length() - 1] for label in original_labels)
        universe = 0
        for label in labels:
            universe |= label
        for order in orders:
            def original_basis(failed):
                earlier = basis = 0
                for e in order:
                    if labels[e] & failed:
                        continue
                    enlarged = earlier | (1 << e)
                    if ranks[enlarged] > ranks[earlier]:
                        basis |= 1 << e
                    earlier = enlarged
                return basis

            certificate = 0
            for label in bits(universe):
                certificate |= original_basis(universe ^ (1 << label))
            if universe.bit_count() <= 2:
                certificate |= original_basis(universe)
            require(certificate.bit_count() <= 3 * rank, "few-label basis-union size")
            for failed in all_failures(universe):
                if failed.bit_count() <= 2:
                    require(not original_basis(failed) & ~certificate,
                            "few-label union contains every canonical surviving basis")
                    counts["failure_queries"] += 1
            counts["instances"] += 1
    return dict(counts)


def check_nonrepresentable_fixture():
    counts = Counter()
    profile_counts = Counter()
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
        actual, profile_bound, multiplicities = verify_two_failure_profile(
            ranks, labels, order, profile_counts,
        )
        if order == natural:
            require(actual == profile_bound == 13 and multiplicities == (1, 3),
                    "exact one-failure-profile certificate for the obstruction")
        for budget in range(5):
            retained = verify_case(ranks, labels, budget, order, counts)
            if order == natural and budget == 2:
                require(retained.bit_count() == 13, "known 13-item sharp-bound obstruction")
    counts["complete_rank_table_entries"] = len(ranks)
    counts["fixed_orders"] = len(orders)
    return {**counts, "two_failure_profile": dict(profile_counts),
            "few_label_coarsenings": check_few_label_coarsenings(ranks, labels, sorted(orders))}


def verify_value_tree_case(values, labels, budget, order, counts):
    """Reference every original prefix value, never a compressed greedy state."""
    size = len(labels)
    ground = (1 << size) - 1
    value_range = values[ground] - values[0]
    degree = max((label.bit_count() for label in labels), default=0)
    retained, queries, nodes = ordered_value_tree(labels, budget, order, values.__getitem__)
    universe = 0
    for label in labels:
        universe |= label
    reference = 0
    original_marginals = {}
    for failed in all_failures(universe):
        if failed.bit_count() > budget:
            continue
        prefix = 0
        for e in order:
            enlarged = prefix if labels[e] & failed else prefix | (1 << e)
            marginal = values[enlarged] - values[prefix]
            if marginal > 0:
                reference |= 1 << e
                if failed == 0:
                    original_marginals[e] = marginal
            require(values[enlarged & retained] == values[enlarged],
                    "every original surviving prefix value")
            counts["original_prefix_value_comparisons"] += 1
            prefix = enlarged
        counts["allowed_failure_queries"] += 1
    require(reference == retained, "exact union of original positive-marginal items")
    require(sum(original_marginals.values()) == value_range,
            "original positive marginals telescope")
    tree_bound = sum((degree * value_range) ** depth for depth in range(budget + 1))
    require(nodes <= tree_bound and queries <= 1 + size * tree_bound,
            "cached-baseline value-tree oracle bound")

    if budget and degree:
        gamma_bound = value_range * (budget + degree) ** (budget + degree) // (
            budget ** budget * degree ** degree
        )
        failed_weight, alive_weight = budget, degree
        if degree == 1 and budget >= 2:
            failed_weight, alive_weight = budget - 1, 1
        total_weight = failed_weight + alive_weight
        base_numerator = sum(
            marginal * alive_weight ** labels[e].bit_count()
            * total_weight ** (degree - labels[e].bit_count())
            for e, marginal in original_marginals.items()
        )
        refined_bound = len(original_marginals) + (
            (value_range * total_weight ** degree - base_numerator)
            * total_weight ** budget
            // (failed_weight ** budget * alive_weight ** degree)
        )
        bound = min(size, gamma_bound, refined_bound)
        if budget == 1:
            bound = min(bound, (degree + 1) * value_range)
        counts["weighted_original_marginal_inequalities"] += 1
    else:
        bound = len(original_marginals)
    require(retained.bit_count() <= bound, "integral-submodular retained-size bound")
    counts["instances"] += 1
    counts["value_queries"] += queries
    counts["basis_tree_nodes"] += nodes
    counts["nonzero_baseline_instances"] += values[0] != 0
    counts["zero_range_instances"] += value_range == 0
    counts["marginal_above_one_instances"] += max(original_marginals.values(), default=0) > 1


def check_integral_submodular_trees():
    counts = Counter()
    # Scaled matroid ranks include noncoverage functions. Every two-label
    # list, every budget through two, and both order directions are checked.
    for size in range(4):
        for ranks in all_matroid_rank_tables(size):
            values = tuple(-5 + 2 * rank for rank in ranks)
            counts["scaled_matroid_value_tables"] += 1
            for labels in product(range(4), repeat=size):
                for budget in range(3):
                    for order in {tuple(range(size)), tuple(reversed(range(size)))}:
                        verify_value_tree_case(values, labels, budget, order, counts)

    # Weighted coverage adds overlapping features, unequal positive jumps,
    # duplicate items, zero increments, and positive/negative baselines.
    # All feature assignments through n=3 and a fixed n=4 slice are used.
    for size in range(5):
        for serial, features in enumerate(product(range(8), repeat=size)):
            if size == 4 and serial % 17:
                continue
            baseline = 7 if serial % 2 else -3
            values = []
            for mask in range(1 << size):
                covered = 0
                for e in bits(mask):
                    covered |= features[e]
                values.append(baseline + sum(bit + 1 for bit in bits(covered)))
            # Validate the declared oracle class on its complete table.
            for left in range(1 << size):
                for right in range(1 << size):
                    require(values[left] + values[right]
                            >= values[left & right] + values[left | right],
                            "coverage table submodularity")
                    if left & ~right == 0:
                        require(values[left] <= values[right], "coverage table monotonicity")
            counts["weighted_coverage_value_tables"] += 1
            for offset in range(4):
                labels = tuple((features[e] + e + offset) % 8 for e in range(size))
                order = tuple(range(size)) if offset % 2 else tuple(reversed(range(size)))
                for budget in range(4):
                    verify_value_tree_case(tuple(values), labels, budget, order, counts)
    return dict(counts)


def main():
    require(__debug__, "run without -O; exact verification must stay enabled")
    print(json.dumps({
        "status": "passed",
        "algorithm": "ordered-basis tree and retained-prefix failure-witness search",
        "small_matroids": check_all_small_matroids(),
        "small_two_failure_profiles": check_small_two_failure_profiles(),
        "rank_three_local_incidence": check_rank_three_line_patterns(),
        "circuit_extension_basis_enumeration": check_circuit_extensions(),
        "nonrepresentable_rank_four": check_nonrepresentable_fixture(),
        "integral_submodular_value_tree": check_integral_submodular_trees(),
        "scope": "finite independence/value-oracle checks; general bounds have separate proofs",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
