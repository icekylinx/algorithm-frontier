#!/usr/bin/env python3
"""Finite exact replay of closure-preserving rank rounding over a composite ring.

Domain: every subset of six explicitly represented blocks in Z_6^3, and all
4096 ordered subset pairs. Integer subgroup enumeration is independent of HNF.
Logarithms use certified rational intervals; all final checks are exact.
This is finite evidence, not a proof of the general rounding theorem.
"""
from collections import deque
from fractions import Fraction as F
from itertools import product

MODULUS = 6
BLOCKS = (
    ((2, 0, 0),),
    ((3, 0, 0),),
    ((0, 2, 0),),
    ((0, 3, 0), (0, 0, 2)),
    ((1, 1, 0),),
    ((0, 1, 1),),
)
M = len(BLOCKS)


def subgroup_order(mask):
    generators = [v for e, block in enumerate(BLOCKS) if mask >> e & 1 for v in block]
    found = {(0, 0, 0)}
    queue = deque(found)
    while queue:
        v = queue.popleft()
        for g in generators:
            w = tuple((a + b) % MODULUS for a, b in zip(v, g))
            if w not in found:
                found.add(w)
                queue.append(w)
    return len(found)


def natural_log_interval(u, terms=16):
    assert F(1) <= u <= F(2)
    z = (u - 1) / (u + 1)
    lower = 2 * sum((z ** (2 * j + 1) / (2 * j + 1) for j in range(terms)), F(0))
    tail = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return lower, lower + tail


def binary_log_interval(n):
    exponent = n.bit_length() - 1
    lo, hi = natural_log_interval(F(n, 1 << exponent))
    lo2, hi2 = natural_log_interval(F(2))
    return exponent + lo / hi2, exponent + hi / lo2


def main():
    orders = [subgroup_order(s) for s in range(1 << M)]
    total = orders[-1]
    rank_bound = (total - 1).bit_length()
    denominator = 1
    while denominator < 1024 * rank_bound:
        denominator *= 2
    assert 1024 * rank_bound <= denominator < 2048 * rank_bound

    rounded_by_order = {}
    for order in sorted(set(orders)):
        if order == 1:
            rounded_by_order[order] = F(0)
            continue
        lo, hi = binary_log_interval(order)
        assert hi - lo <= F(1, 1024 * rank_bound)
        value = (lo + hi) / 2
        transformed = value - value * value / (4 * rank_bound)
        numerator = (transformed * denominator).__floor__()
        rounded = 4 * F(numerator, denominator)
        # The transform is monotone and 1-Lipschitz on the relevant interval.
        assert 0 <= lo <= hi <= rank_bound
        lo_phi = lo - lo * lo / (4 * rank_bound)
        hi_phi = hi - hi * hi / (4 * rank_bound)
        assert rounded / 4 - lo_phi <= F(1, 64 * rank_bound)
        assert hi_phi - rounded / 4 <= F(1, 64 * rank_bound)
        rounded_by_order[order] = rounded

    values = [rounded_by_order[o] for o in orders]
    assert values[0] == 0 and values[-1] <= 4 * rank_bound
    for s in range(1 << M):
        for e in range(M):
            t = s | (1 << e)
            delta = values[t] - values[s]
            assert delta >= 0
            assert (delta == 0) == (orders[t] == orders[s])
            assert delta == 0 or delta >= 1
        for t in range(1 << M):
            # Independently confirm integer subgroup submodularity first.
            assert orders[s] * orders[t] >= orders[s | t] * orders[s & t]
            assert values[s] + values[t] >= values[s | t] + values[s & t]
    print(f"Exact quotient-rounding replay passed: {1 << M} subsets, "
          f"{1 << (2 * M)} submodularity pairs, total subgroup order {total}.")


if __name__ == "__main__":
    main()
