#!/usr/bin/env python3
"""Exhaustive finite checks for the two-scenario k-SUM reduction.

The script checks the exact arithmetic equivalence used by the hardness card
on all small integer instances.  It is a regression check for the reduction,
not a proof of W[1]-hardness.
"""
from __future__ import annotations

from itertools import combinations, product


def check_two_scenario_reduction() -> None:
    for q in range(2, 8):
        for a in product(range(4), repeat=q):
            total = sum(a)
            L = total + 1
            for k in range(1, q):
                r = q - k
                for target in range(total + 1):
                    C1 = total - target
                    C2 = r * L - total + target
                    for omitted in combinations(range(q), k):
                        D = set(omitted)
                        B = [i for i in range(q) if i not in D]
                        positive = (
                            sum(a[i] for i in B) <= C1
                            and sum(L - a[i] for i in B) <= C2
                        )
                        if positive != (sum(a[i] for i in D) == target):
                            raise AssertionError(
                                f"reduction mismatch q={q}, a={a}, k={k}, T={target}, D={omitted}"
                            )


def main() -> None:
    check_two_scenario_reduction()
    print("finite reduction checks passed")


if __name__ == "__main__":
    main()
