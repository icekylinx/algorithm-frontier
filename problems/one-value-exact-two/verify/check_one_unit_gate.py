#!/usr/bin/env python3
"""Finite Boolean-cap/gate checks, not a general matroid intersection solver.

Attribution: Yilin Liu and GPT-6 Astra Pro.
"""
from itertools import product
from fractions import Fraction
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def ranks(q):
    """Uniform integer polymatroids and weighted coverage ranks."""
    values = [tuple(0 for _ in range(1 << q))]
    values += [tuple(int(bool(s & (1 << active))) for s in range(1 << q))
               for active in range(q)]
    for capacity in range(1, 4):
        for total in range(capacity, capacity * q + 1):
            values.append(tuple(min(capacity * s.bit_count(), total) for s in range(1 << q)))
    for offset in range(q + 1):
        masks = [((1 << p) | (1 << ((p + offset) % q))) for p in range(q)]
        table = []
        for subset in range(1 << q):
            union = 0
            for p in range(q):
                if subset >> p & 1:
                    union |= masks[p]
            table.append(sum(1 + j % 2 for j in range(q) if union >> j & 1))
        values.append(tuple(table))
    return sorted(set(values))


def independent(rank, subset):
    return all((subset & s).bit_count() <= rank[s] for s in range(len(rank)))


def main():
    counts = dict(boolean_caps=0, augmentation_pairs=0, gate_instances=0,
                  assignments=0, pair_subsets=0, exact_budget_comparisons=0)
    for q in range(1, 5):
        all_ranks = ranks(q)
        for rank in all_ranks:
            sets = [s for s in range(1 << q) if independent(rank, s)]
            for smaller in sets:
                for larger in sets:
                    if smaller.bit_count() >= larger.bit_count():
                        continue
                    require(any(independent(rank, smaller | (1 << p))
                                for p in range(q) if (larger & ~smaller) >> p & 1),
                            'Boolean cap violates augmentation')
                    counts['augmentation_pairs'] += 1
            counts['boolean_caps'] += 1
        # Every listed player rank is a genuine rank-one-per-block matroid,
        # or a uniform matroid. Resource ranks permit larger binary capacities.
        player_families = [lambda s, r=r: s.bit_count() <= r for r in range(1, q + 1)]
        player_families += [lambda s: all(sum(bool(s >> p & 1) for p in range(q)
                                            if p % 2 == block) <= 1 for block in (0, 1))]
        for index, first in enumerate(all_ranks):
            second = all_ranks[(3 * index + 1) % len(all_ranks)]
            resources = [first, second]
            costs = [[Fraction((p + 2 * j + index) % 5, 1 + (p + j) % 3)
                      for j in range(2)] for p in range(q)]
            for player_ok in player_families:
                rank_m = max(s.bit_count() for s in range(1 << q) if player_ok(s))
                best_direct = None
                # Original allocations with zero or one retained unit per player.
                for choice in product(range(3), repeat=q):
                    chosen = sum(1 << p for p in range(q) if choice[p])
                    counts['assignments'] += 1
                    if chosen.bit_count() != rank_m or not player_ok(chosen):
                        continue
                    recipients = [sum(1 << p for p in range(q) if choice[p] == j + 1)
                                  for j in range(2)]
                    if not all(independent(resources[j], recipients[j]) for j in range(2)):
                        continue
                    cost = sum((costs[p][choice[p]-1] for p in range(q) if choice[p]), Fraction())
                    best_direct = cost if best_direct is None else min(best_direct, cost)
                pairs = [(p, j) for p in range(q) for j in range(2) if resources[j][1 << p] >= 1]
                best_pairs = None
                for mask in range(1 << len(pairs)):
                    counts['pair_subsets'] += 1
                    selected = [pairs[i] for i in range(len(pairs)) if mask >> i & 1]
                    if len(selected) != rank_m or len({p for p, _ in selected}) != rank_m:
                        continue
                    projected = sum(1 << p for p, _ in selected)
                    if not player_ok(projected):
                        continue
                    if not all(independent(resources[j], sum(1 << p for p, t in selected if t == j))
                               for j in range(2)):
                        continue
                    cost = sum((costs[p][j] for p, j in selected), Fraction())
                    best_pairs = cost if best_pairs is None else min(best_pairs, cost)
                require(best_pairs == best_direct, 'pair gate differs from original allocation optimum')
                for budget in [Fraction(0), Fraction(1, 3), Fraction(1), Fraction(9)] + (
                        [] if best_direct is None else [best_direct, best_direct - Fraction(1, 6)]):
                    if budget < 0:
                        continue
                    require((best_pairs is not None and best_pairs <= budget) ==
                            (best_direct is not None and best_direct <= budget), 'budget gate mismatch')
                    counts['exact_budget_comparisons'] += 1
                counts['gate_instances'] += 1
    print(json.dumps({'status': 'PASS', **counts}, indent=2))
    print('Scope: finite Boolean-cap augmentation and exact-cost one-unit pair gates; paid general primitives remain separate.')


if __name__ == '__main__':
    main()
