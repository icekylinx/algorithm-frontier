#!/usr/bin/env python3
"""Finite independent checks for exact correlated-failure summaries.

The algorithms use only independence/value access. Verification enumerates
all permitted failures and original prefixes against complete rank/value
tables. These finite checks do not constitute a proof for arbitrary oracles.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
import json
from math import comb
from typing import Callable, Iterator


def bits(mask: int) -> Iterator[int]:
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def greedy_basis(ground: int, independent: Callable[[int], bool]) -> int:
    basis = 0
    for e in bits(ground):
        candidate = basis | (1 << e)
        if independent(candidate):
            basis = candidate
    return basis


def label_union(ground: int, labels: tuple[int, ...]) -> int:
    union = 0
    for e in bits(ground):
        union |= labels[e]
    return union


def surviving(ground: int, labels: tuple[int, ...], failed: int) -> int:
    return sum(1 << e for e in bits(ground) if not labels[e] & failed)


def allowed_failures(labels: tuple[int, ...], h: int) -> Iterator[int]:
    universe = tuple(bits(label_union((1 << len(labels)) - 1, labels)))
    for size in range(min(h, len(universe)) + 1):
        for selected in combinations(universe, size):
            yield sum(1 << label for label in selected)


def failure_witness(
    ground: int, e: int, labels: tuple[int, ...], h: int,
    independent: Callable[[int], bool],
) -> int | None:
    """Return a coloop witness, or None; do not enumerate the label universe."""
    protected = 1 << e

    def search(current: int, remaining: int, failed: int) -> int | None:
        basis = greedy_basis(current & ~protected, independent)
        if independent(basis | protected):
            return failed
        if remaining == 0:
            return None
        candidates = label_union(basis, labels) & ~labels[e]
        for label in bits(candidates):
            bit = 1 << label
            answer = search(surviving(current, labels, bit), remaining - 1,
                            failed | bit)
            if answer is not None:
                return answer
        return None

    return search(ground, h, 0)


def rank_summary(
    labels: tuple[int, ...], h: int, independent: Callable[[int], bool],
) -> tuple[int, dict[int, int]]:
    ground = (1 << len(labels)) - 1
    witnesses: dict[int, int] = {}
    for e in range(len(labels)):
        witness = failure_witness(ground, e, labels, h, independent)
        if witness is None:
            ground &= ~(1 << e)
        else:
            witnesses[e] = witness
    return ground, witnesses


def weighted_one_failure_summary(
    labels: tuple[int, ...], independent: Callable[[int], bool],
) -> int:
    ground = (1 << len(labels)) - 1
    original = greedy_basis(ground, independent)
    retained = original
    for label in bits(label_union(original, labels)):
        retained |= greedy_basis(surviving(ground, labels, 1 << label), independent)
    return retained


def value_witness(
    ground: int, e: int, labels: tuple[int, ...], h: int,
    value: Callable[[int], int],
) -> int | None:
    protected = 1 << e

    def search(current: int, remaining: int, failed: int) -> int | None:
        without = current & ~protected
        if value(current) > value(without):
            return failed
        if remaining == 0:
            return None
        basis = 0
        basis_value = value(0)
        for item in bits(without):
            candidate = basis | (1 << item)
            candidate_value = value(candidate)
            if candidate_value > basis_value:
                basis, basis_value = candidate, candidate_value
        for label in bits(label_union(basis, labels) & ~labels[e]):
            bit = 1 << label
            answer = search(surviving(current, labels, bit), remaining - 1,
                            failed | bit)
            if answer is not None:
                return answer
        return None

    return search(ground, h, 0)


def value_summary(
    labels: tuple[int, ...], h: int, value: Callable[[int], int],
) -> tuple[int, dict[int, int]]:
    ground = (1 << len(labels)) - 1
    witnesses: dict[int, int] = {}
    for e in range(len(labels)):
        witness = value_witness(ground, e, labels, h, value)
        if witness is None:
            ground &= ~(1 << e)
        else:
            witnesses[e] = witness
    return ground, witnesses


def all_matroid_rank_tables(n: int) -> Iterator[tuple[int, ...]]:
    """Enumerate basis families and check the basis-exchange axiom directly."""
    for rank in range(n + 1):
        candidates = [sum(1 << e for e in subset)
                      for subset in combinations(range(n), rank)]
        for selection in range(1, 1 << len(candidates)):
            bases = {candidates[i] for i in bits(selection)}
            valid = True
            for left in bases:
                for right in bases:
                    for e in bits(left & ~right):
                        if not any((left ^ (1 << e) | (1 << f)) in bases
                                   for f in bits(right & ~left)):
                            valid = False
                            break
                    if not valid:
                        break
                if not valid:
                    break
            if valid:
                yield tuple(max((mask & base).bit_count() for base in bases)
                            for mask in range(1 << n))


def verify_rank_case(
    ranks: tuple[int, ...], labels: tuple[int, ...], h: int,
    counts: Counter,
) -> None:
    n = len(labels)
    ground = (1 << n) - 1
    independent = lambda mask: ranks[mask] == mask.bit_count()
    retained, witnesses = rank_summary(labels, h, independent)
    d = max((label.bit_count() for label in labels), default=0)
    assert retained.bit_count() <= ranks[ground] * comb(h + d, d)
    for failed in allowed_failures(labels, h):
        assert ranks[surviving(retained, labels, failed)] == ranks[surviving(ground, labels, failed)]
        counts['rank_failure_comparisons'] += 1
    for e, failed in witnesses.items():
        assert failed.bit_count() <= h and not failed & labels[e]
        alive = surviving(retained, labels, failed)
        assert ranks[alive] == ranks[alive & ~(1 << e)] + 1
        counts['necessity_witnesses'] += 1
    counts['rank_summary_instances'] += 1
    if h == 1:
        weighted = weighted_one_failure_summary(labels, independent)
        assert weighted.bit_count() <= (d + 1) * ranks[ground]
        for failed in allowed_failures(labels, 1):
            alive = surviving(ground, labels, failed)
            basis = greedy_basis(alive, independent)
            assert not basis & ~weighted
            for end in range(n + 1):
                prefix = (1 << end) - 1
                assert ranks[alive & prefix] == ranks[alive & weighted & prefix]
                counts['weighted_prefix_comparisons'] += 1
        counts['weighted_summary_instances'] += 1


def verify_value_case(
    values: tuple[int, ...], labels: tuple[int, ...], h: int,
    counts: Counter,
) -> None:
    ground = (1 << len(labels)) - 1
    retained, witnesses = value_summary(labels, h, values.__getitem__)
    d = max((label.bit_count() for label in labels), default=0)
    assert retained.bit_count() <= (values[ground] - values[0]) * comb(h + d, d)
    for failed in allowed_failures(labels, h):
        assert values[surviving(retained, labels, failed)] == values[surviving(ground, labels, failed)]
        counts['value_failure_comparisons'] += 1
    for e, failed in witnesses.items():
        assert failed.bit_count() <= h and not failed & labels[e]
        alive = surviving(retained, labels, failed)
        assert values[alive] > values[alive & ~(1 << e)]
    counts['value_summary_instances'] += 1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full-labels', action='store_true',
                        help='use every at-most-two-label assignment also at n=4')
    args = parser.parse_args()
    if not __debug__:
        parser.error('run without -O or PYTHONOPTIMIZE; mathematical assertions must be enabled')
    counts: Counter = Counter()
    for n in range(5):
        ranks_list = list(all_matroid_rank_tables(n))
        counts['matroids'] += len(ranks_list)
        choices = (0, 1, 2, 3, 4, 5, 6) if n <= 3 or args.full_labels else (0, 1, 2, 4)
        for labels in product(choices, repeat=n):
            for ranks in ranks_list:
                for h in range(3):
                    verify_rank_case(ranks, labels, h, counts)
                    # Matroid ranks also test the separate value-oracle code.
                    if n <= 3:
                        verify_value_case(tuple(7 + r for r in ranks), labels, h, counts)
    assert counts['matroids'] == 92  # 1 + 2 + 5 + 16 + 68 labelled matroids.

    # An explicit rank-four sparse-paving oracle on eight elements. Its five
    # circuit-hyperplanes have pairwise intersections of size at most two.
    forbidden = {0b00001111, 0b00110011, 0b11000011, 0b00111100, 0b11001100}
    assert all((a & b).bit_count() <= 2 for a, b in combinations(forbidden, 2))
    bases = [m for m in range(256) if m.bit_count() == 4 and m not in forbidden]
    ranks = tuple(max((mask & base).bit_count() for base in bases) for mask in range(256))
    for shift in range(16):
        labels = tuple(((3 * e + shift) % 15) for e in range(8))
        for h in range(3):
            verify_rank_case(ranks, labels, h, counts)

    # Coverage values with nonzero baseline, overlapping features, zero gains,
    # and repeated item contributions, checked by full surviving-set values.
    for n in range(1, 5):
        for serial, features in enumerate(product(range(8), repeat=n)):
            if n == 4 and serial % 17:
                continue
            values = []
            for mask in range(1 << n):
                covered = 0
                for e in bits(mask):
                    covered |= features[e]
                values.append(5 + covered.bit_count())
            for offset in range(4):
                labels = tuple((features[e] + e + offset) % 7 for e in range(n))
                for h in range(3):
                    verify_value_case(tuple(values), labels, h, counts)

    # Exact lower examples: every d-subset is isolated by its h-complement.
    for rank in (1, 2):
        for h in range(3):
            for d in range(3):
                sets = [sum(1 << i for i in own) for own in combinations(range(h + d), d)]
                labels = tuple(sets * rank)
                if len(labels) > 16:
                    continue
                block = len(sets)
                def independent(mask: int) -> bool:
                    return all(((mask >> (i * block)) & ((1 << block) - 1)).bit_count() <= 1
                               for i in range(rank))
                retained, _ = rank_summary(labels, h, independent)
                assert retained == (1 << len(labels)) - 1
                if h == 1:
                    assert weighted_one_failure_summary(labels, independent) == retained
                counts['sharp_lower_examples'] += 1
    print(json.dumps({'status': 'PASS', 'scope': 'Finite oracle, prefix and necessity-witness checks; asymptotic proofs are separate.',
                      'full_labels': args.full_labels, **dict(sorted(counts.items()))}, sort_keys=True))


if __name__ == '__main__':
    main()
