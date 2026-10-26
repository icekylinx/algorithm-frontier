#!/usr/bin/env python3
"""Exhaustive finite checks for the two-scenario k-SUM reduction.

The script checks the exact arithmetic equivalence used by the hardness card
on all small integer instances.  It is a regression check for the reduction,
not a proof of W[1]-hardness.
"""
from __future__ import annotations

from itertools import combinations, product
import json


def check_two_scenario_reduction() -> dict[str, int]:
    instances = omitted_sets = comparisons = 0
    for q in range(2, 8):
        for a in product(range(4), repeat=q):
            instances += 1
            total = sum(a)
            L = total + 1
            for k in range(1, q):
                r = q - k
                for omitted in combinations(range(q), k):
                    D = set(omitted)
                    B = [i for i in range(q) if i not in D]
                    # Construct each selected-set cost independently from the
                    # original two scenarios, once for all target values.
                    cost1 = sum(a[i] for i in B)
                    cost2 = sum(L - a[i] for i in B)
                    omitted_sum = sum(a[i] for i in D)
                    omitted_sets += 1
                    for target in range(total + 1):
                        C1 = total - target
                        C2 = r * L - total + target
                        positive = (
                            cost1 <= C1
                            and cost2 <= C2
                        )
                        comparisons += 1
                        if positive != (omitted_sum == target):
                            raise AssertionError(
                                f"reduction mismatch q={q}, a={a}, k={k}, T={target}, D={omitted}"
                            )
    return {"integer_instances": instances, "omitted_sets": omitted_sets,
            "target_comparisons": comparisons}


def main() -> None:
    counts = check_two_scenario_reduction()
    print(json.dumps({"status": "PASS", "counts": counts,
        "scope": "All q=2,...,7, entries 0,...,3, nontrivial omitted sets, and targets 0,...,sum(a); finite arithmetic equivalence, not a hardness proof."}, indent=2))


if __name__ == "__main__":
    main()
