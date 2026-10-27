#!/usr/bin/env python3
"""Finite exact checks of union ranks, basis recovery and fractional domination.
Attribution: Yilin Liu and GPT-6 Astra Pro. SPDX-License-Identifier: Apache-2.0
This enumerates small matroids, not the polynomial union algorithm.
"""
from fractions import Fraction
from itertools import combinations, product


def subsets(ground):
    ground = tuple(ground)
    return tuple(frozenset(c) for k in range(len(ground) + 1) for c in combinations(ground, k))


def binary_independent(vectors, subset):
    span = {0}
    for p in subset:
        if vectors[p] in span:
            return False
        span |= {v ^ vectors[p] for v in tuple(span)}
    return True


def main():
    totals = dict(matroid_pairs=0, rank_identities=0, recovery_extensions=0,
                  fractional_points=0, fractional_constraints=0)
    for q in range(1, 4):
        ground = frozenset(range(q))
        sets = subsets(ground)
        families = set()
        for vectors in product(range(4), repeat=q):
            families.add(frozenset(s for s in sets if binary_independent(vectors, s)))
        families.add(frozenset(sets))  # Include full rank when q exceeds dimension.
        ordered = sorted(families, key=lambda family: tuple(s in family for s in sets))
        for original in ordered:
            r = max(map(len, original))
            bases = tuple(s for s in sets if s in original and len(s) == r)
            dual_bases = tuple(ground - b for b in bases)
            dual = frozenset(s for s in sets if any(s <= b for b in dual_bases))
            for fat in ordered:
                totals['matroid_pairs'] += 1
                union = frozenset(d | f for d in dual for f in fat if not d & f)
                rank = max(map(len, union))
                ubases = tuple(s for s in sets if s in union and len(s) == rank)
                assert q - rank <= r
                for a in sets:
                    lhs = max(len(i & a) for i in union)
                    rhs = min(len(a - y) + max(len(i & y) for i in dual)
                              + max(len(i & y) for i in fat) for y in subsets(a))
                    assert lhs == rhs
                    totals['rank_identities'] += 1
                for b in ubases:
                    small = ground - b
                    for d in subsets(b):
                        f = b - d
                        if d not in dual or f not in fat:
                            continue
                        for extension in dual_bases:
                            if d <= extension:
                                recovered = ground - extension
                                assert recovered in bases and recovered <= small | f
                                totals['recovery_extensions'] += 1
                # An exact mixture of two dual bases and one fat independent set.
                # Scaling f down enforces f<=x, including zero coordinates. The
                # union inequalities are then checked against independently
                # enumerated union ranks, with all nontrivial rational sums exact.
                for first in dual_bases:
                    second = dual_bases[-1]
                    d = [Fraction(int(p in first), 3) + Fraction(2 * int(p in second), 3)
                         for p in range(q)]
                    x = [1 - value for value in d]
                    for fset in sets:
                        if fset not in fat:
                            continue
                        scale = min((x[p] for p in fset), default=Fraction(1))
                        f = [scale if p in fset else Fraction(0) for p in range(q)]
                        z = [d[p] + f[p] for p in range(q)]
                        h = [x[p] - f[p] for p in range(q)]
                        assert all(0 <= z[p] <= 1 and h[p] == 1-z[p] for p in range(q))
                        for a in sets:
                            assert sum(z[p] for p in a) <= max(len(i & a) for i in union)
                            totals['fractional_constraints'] += 1
                        totals['fractional_points'] += 1
    print('PASS matroid union reduction:', ', '.join(f'{k}={v}' for k, v in totals.items()))


if __name__ == '__main__':
    main()
