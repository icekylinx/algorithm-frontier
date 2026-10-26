#!/usr/bin/env python3
"""Verify exact rank-two prefix summaries and their oracle-query charging.

The tested construction sees only independence answers.  The reference
enumerates all failures and identifies greedy items from original-prefix
rank increments.  Bit masks are a finite-verification representation, not
an assertion of constant-time operations on arbitrarily long masks.
"""

import argparse
import json
import random
import sys
from itertools import combinations, permutations

from check_summaries import all_matroid_rank_tables
from check_rank_loss_contraction import label_patterns


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def all_failures(labels, order):
    universe = 0
    for e in order:
        universe |= labels[e]
    failed = universe
    while True:
        yield failed
        if not failed:
            return
        failed = (failed - 1) & universe


def reference_basis(rank, labels, order, failed):
    prefix = basis = old = 0
    for e in order:
        if labels[e] & failed:
            continue
        prefix |= 1 << e
        new = rank(prefix)
        require(new - old in (0, 1), 'matroid prefix rank increment')
        if new > old:
            basis |= 1 << e
        old = new
    return basis


def construct(labels, order, independent, budget, rank_one=False):
    """Return exact H, item witnesses, and actual independence-query counts."""
    counts = dict(singleton=0, classify=0, append=0, dependent=0)

    def ask(mask, phase):
        result = independent(mask)
        if phase == 'scan':
            counts['append' if result else 'dependent'] += 1
        else:
            counts[phase] += 1
        return result

    nonloops = [e for e in order if ask(1 << e, 'singleton')]
    universe = 0
    for e in nonloops:
        universe |= labels[e]
    k = min(budget, universe.bit_count())
    first = []
    seen = 0
    for e in nonloops:
        label = labels[e]
        if label and seen & label:
            continue
        first.append(e)
        seen |= label
        if not label or len(first) == k + 1:
            break

    retained = sum(1 << e for e in first)
    witnesses = {}
    earlier = 0
    first_failures = {}
    for e in first:
        first_failures[e] = earlier
        witnesses[e] = earlier
        earlier |= labels[e]
    if rank_one or not first:
        counts.update(k=k, first=len(first), classes=0,
                      queries=sum(counts.values()), candidate_items=len(first))
        return retained, witnesses, counts

    representatives = []
    class_of = {}
    for e in first:
        for index, rep in enumerate(representatives):
            if not ask((1 << rep) | (1 << e), 'classify'):
                class_of[e] = index
                break
        else:
            class_of[e] = len(representatives)
            representatives.append(e)

    lists = [[] for _ in representatives]
    seen = [0 for _ in representatives]
    closed = [False for _ in representatives]
    for e in nonloops:
        dependent_here = 0
        for index, rep in enumerate(representatives):
            if closed[index] or labels[e] & seen[index] or e == rep:
                continue
            if ask((1 << rep) | (1 << e), 'scan'):
                lists[index].append(e)
                seen[index] |= labels[e]
                if not labels[e] or len(lists[index]) == k + 1:
                    closed[index] = True
            else:
                dependent_here += 1
        require(dependent_here <= 1, 'at most one failed class comparison per item')

    position = {e: i for i, e in enumerate(order)}
    for a in first:
        failed = first_failures[a]
        for e in lists[class_of[a]]:
            if (position[a] < position[e] and failed.bit_count() <= k
                    and not failed & (labels[a] | labels[e])):
                retained |= 1 << e
                witnesses.setdefault(e, failed)
            failed |= labels[e]

    queries = sum(counts.values())
    counts.update(k=k, first=len(first), classes=len(representatives),
                  queries=queries,
                  candidate_items=len(first) + sum(map(len, lists)))
    require(counts['singleton'] == len(order), 'one singleton query per ground item')
    require(counts['classify'] <= len(first) * (len(first) - 1) // 2,
            'classification query bound')
    require(counts['append'] <= len(representatives) * (k + 1), 'successful scan bound')
    require(counts['dependent'] <= len(order), 'dependent scan bound')
    require(queries <= 2 * len(order) + k * (k + 1) // 2 + (k + 1) ** 2,
            'total query bound')
    return retained, witnesses, counts


def construct_all_labels(labels, order, independent):
    """The all-label-budget endpoint at arbitrary rank, using no rank oracle."""
    unlabelled = retained = 0
    states = {}
    principal = propagated = 0
    for e in order:
        bit = 1 << e
        label = labels[e]
        principal += 1
        if label:
            if label not in states:
                states[label] = unlabelled
            if independent(states[label] | bit):
                states[label] |= bit
                retained |= bit
        elif independent(unlabelled | bit):
            unlabelled |= bit
            retained |= bit
            for active_label, basis in states.items():
                propagated += 1
                if independent(basis | bit):
                    states[active_label] |= bit
    require(principal == len(order), 'one principal test per input item')
    require(propagated <= unlabelled.bit_count() * len(states),
            'all-label endpoint propagated-query bound')
    return retained, dict(principal=principal, propagated=propagated,
                          queries=principal + propagated,
                          unlabelled_rank=unlabelled.bit_count())


def verify_case(rank, labels, order, counts):
    ground = sum(1 << e for e in order)
    r = rank(ground)
    require(r <= 2, 'rank-two input promise')
    independent = lambda subset: rank(subset) == subset.bit_count()
    answers = {failed: reference_basis(rank, labels, order, failed)
               for failed in all_failures(labels, order)}
    universe = 0
    for e in order:
        universe |= labels[e]
    budgets = list(range(universe.bit_count() + 1)) + [10 ** 100]
    counts['instances'] += 1
    for h in budgets:
        expected = 0
        for failed, basis in answers.items():
            if failed.bit_count() <= h:
                expected |= basis
        observed, witnesses, stats = construct(labels, order, independent, h)
        require(observed == expected, 'exact original-prefix canonical union')
        require(set(witnesses) == set(bits(observed)), 'one stored witness per output')
        for e, failed in witnesses.items():
            require(failed.bit_count() <= h, 'witness respects original budget')
            require(not labels[e] & failed, 'witness protects retained item')
            require(reference_basis(rank, labels, order, failed) >> e & 1,
                    'witness checked against original full-prefix ranks')
            counts['witnesses'] += 1
        require(observed.bit_count() <= min(len(order), 2 * (stats['k'] + 1)),
                'sharp rank-two retained-size bound')
        for failed in answers:
            if failed.bit_count() > h:
                continue
            full = restricted = 0
            for e in order:
                if labels[e] & failed:
                    continue
                full |= 1 << e
                if observed >> e & 1:
                    restricted |= 1 << e
                require(rank(full) == rank(restricted), 'all original surviving prefix ranks')
                counts['prefix_comparisons'] += 1
        if r <= 1:
            rank_one, _, rank_one_stats = construct(labels, order, independent, h, True)
            require(rank_one == expected, 'rank-one direct scan')
            require(rank_one_stats['queries'] == len(order), 'rank-one linear query bound')
            require(rank_one.bit_count() <= rank_one_stats['k'] + 1,
                    'sharp rank-one support')
            counts['rank_one_cases'] += 1
        counts['budget_instances'] += 1
        counts['queries'] += stats['queries']
        counts['quadratic_candidates'] += stats['candidate_items']
    all_label_result, all_label_stats = construct_all_labels(labels, order, independent)
    full_union = 0
    for basis in answers.values():
        full_union |= basis
    require(all_label_result == full_union, 'all-label-budget endpoint exact union')
    require(all_label_stats['queries'] <= len(order) + r * universe.bit_count(),
            'all-label-budget endpoint oracle cap')
    counts['all_label_queries'] += all_label_stats['queries']


def fresh_counts():
    return {name: 0 for name in ('matroids', 'instances', 'budget_instances',
            'prefix_comparisons', 'witnesses', 'queries', 'rank_one_cases',
            'quadratic_candidates', 'all_label_queries')}


def check_small(max_n):
    counts = fresh_counts()
    for n in range(max_n + 1):
        orders = list(permutations(range(n)))
        patterns = list(label_patterns(n))
        for table in all_matroid_rank_tables(n):
            if table[-1] > 2:
                continue
            counts['matroids'] += 1
            rank = lambda mask, table=table: table[mask]
            for labels in patterns:
                for order in orders:
                    verify_case(rank, labels, order, counts)
        print(json.dumps({'checkpoint_n': n, 'instances': counts['instances']}),
              file=sys.stderr, flush=True)
    return counts


def partition_rank(classes, subset):
    return min(2, len({classes[e] for e in bits(subset) if classes[e] is not None}))


def check_larger():
    counts = fresh_counts()
    rng = random.Random(20261026)
    for _ in range(240):
        n = rng.randrange(5, 19)
        classes = tuple(rng.choice((None, 0, 1, 2, 3, 4)) for _ in range(n))
        labels = tuple(rng.choice((0, 1, 2, 4, 8, 16)) for _ in range(n))
        order = list(range(n))
        rng.shuffle(order)
        verify_case(lambda mask, classes=classes: partition_rank(classes, mask),
                    labels, tuple(order), counts)
        counts['matroids'] += 1
    # Long classes with repeated labels, a late unlabelled item, and many loops.
    for k in range(1, 6):
        classes = (None,) * (2 * k) + (0,) * (3 * k) + (1,) * (3 * k) + (2, 1)
        labels = tuple(1 << (i % 5) for i in range(len(classes) - 2)) + (0, 0)
        for order in (tuple(range(len(classes))), tuple(reversed(range(len(classes))))):
            verify_case(lambda mask, classes=classes: partition_rank(classes, mask),
                        labels, order, counts)
        counts['matroids'] += 1
    # Exact size 2(h+1); only inspect the target budget to avoid large failure tables.
    for h in range(9):
        classes = (0,) * (h + 1) + (1,) * (h + 1)
        labels = tuple(1 << i for i in range(len(classes)))
        order = tuple(range(len(classes)))
        rank = lambda mask, classes=classes: partition_rank(classes, mask)
        result, witnesses, _ = construct(labels, order,
                                         lambda mask: rank(mask) == mask.bit_count(), h)
        require(result.bit_count() == 2 * (h + 1), 'sharp support attained')
        for e, failed in witnesses.items():
            require(failed.bit_count() <= h and reference_basis(rank, labels, order, failed) >> e & 1,
                    'tight-family witness')
        counts['matroids'] += 1
    return counts


def check_lower_bound():
    counts = dict(instances=0, pair_variants=0, loop_variants=0,
                  oracle_answer_comparisons=0)
    for h in range(4):
        for p in range(3):
            core = h + 3
            n = p + core
            classes = (None,) * p + tuple(range(core))
            labels = tuple(1 << i for i in range(n))
            order = tuple(range(n))
            base_rank = lambda mask, classes=classes: partition_rank(classes, mask)
            base_h, _, _ = construct(labels, order,
                                     lambda mask: base_rank(mask) == mask.bit_count(), h)
            last = n - 1
            require(not base_h >> last & 1, 'last core item absent in uniform base')
            for i, j in combinations(range(p, n - 1), 2):
                changed = list(classes)
                changed[j] = changed[i]
                variant_rank = lambda mask, changed=tuple(changed): partition_rank(changed, mask)
                variant_h, _, _ = construct(labels, order,
                        lambda mask: variant_rank(mask) == mask.bit_count(), h)
                require(variant_h >> last & 1, 'hidden parallel pair makes last item necessary')
                differences = []
                for subset in range(1 << n):
                    if ((base_rank(subset) == subset.bit_count()) !=
                            (variant_rank(subset) == subset.bit_count())):
                        differences.append(subset)
                    counts['oracle_answer_comparisons'] += 1
                require(differences == [(1 << i) | (1 << j)],
                        'pair variants differ on exactly one oracle query')
                counts['pair_variants'] += 1
            for u in range(p):
                changed = list(classes)
                changed[u] = classes[p]
                variant_rank = lambda mask, changed=tuple(changed): partition_rank(changed, mask)
                variant_h, _, _ = construct(labels, order,
                        lambda mask: variant_rank(mask) == mask.bit_count(), h)
                require(variant_h >> u & 1 and not base_h >> u & 1,
                        'loop variant changes exact summary')
                for subset in range(1 << n):
                    changed_answer = ((base_rank(subset) == subset.bit_count()) !=
                                      (variant_rank(subset) == subset.bit_count()))
                    expected_change = (subset == 1 << u or
                        (subset.bit_count() == 2 and subset >> u & 1 and
                         bool(subset & sum(1 << e for e in range(p + 1, n)))))
                    require(changed_answer == expected_change,
                            'loop distinguishing queries have private support')
                    counts['oracle_answer_comparisons'] += 1
                counts['loop_variants'] += 1
            counts['instances'] += 1
    return counts


def check_all_labels_higher_rank():
    from check_rank_loss_contraction import binary_rank
    from check_weighted_obstruction import ITEMS, independent as nonrepresentable_independent

    counts = dict(instances=0, queries=0, failure_instances=0)
    rng = random.Random(20261027)
    instances = []
    for _ in range(90):
        n = rng.randrange(5, 13)
        r = rng.randrange(3, 7)
        vectors = tuple(rng.randrange(1 << r) for _ in range(n))
        rank = lambda mask, vectors=vectors: binary_rank(vectors, mask)
        independent = lambda mask, rank=rank: rank(mask) == mask.bit_count()
        labels = tuple(rng.choice((0, 1, 2, 4, 8)) for _ in range(n))
        order = list(range(n))
        rng.shuffle(order)
        instances.append((independent, rank, labels, tuple(order)))
    n = len(ITEMS)
    table = []
    for mask in range(1 << n):
        basis = 0
        for e in bits(mask):
            if nonrepresentable_independent(basis | (1 << e)):
                basis |= 1 << e
        table.append(basis.bit_count())
    rank = lambda mask: table[mask]
    original_labels = tuple(1 << 'ABCD'.index(item[1]) for item in ITEMS)
    for _ in range(12):
        labels = tuple(0 if rng.randrange(3) == 0 else label for label in original_labels)
        order = list(range(n))
        rng.shuffle(order)
        instances.append((nonrepresentable_independent, rank, labels, tuple(order)))
    for independent, rank, labels, order in instances:
        expected = 0
        for failed in all_failures(labels, order):
            expected |= reference_basis(rank, labels, order, failed)
            counts['failure_instances'] += 1
        observed, stats = construct_all_labels(labels, order, independent)
        require(observed == expected, 'arbitrary-rank all-label endpoint')
        counts['instances'] += 1
        counts['queries'] += stats['queries']
    return counts


if __name__ == '__main__':
    require(__debug__, 'run without -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true',
                        help='all rank-at-most-two matroids through four items')
    args = parser.parse_args()
    print(json.dumps({'small': check_small(4 if args.full else 3),
                      'larger': check_larger(),
                      'lower_bound': check_lower_bound(),
                      'all_labels_higher_rank': check_all_labels_higher_rank()},
                     indent=2, sort_keys=True))
