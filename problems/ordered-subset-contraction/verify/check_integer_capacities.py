#!/usr/bin/env python3
# Copyright 2026 Yilin Liu and GPT-6 Astra Pro
# SPDX-License-Identifier: Apache-2.0
"""Exact finite certificates for integer subset-capacity envelopes.

This checks the maxima of the stated cost functions on finite integer
profiles. It does not prove optimality of matrix multiplication or circuits.
"""

from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json


@lru_cache(maxsize=None)
def upper_u(a, b, c):
    a, b, c = sorted(map(F, (a, b, c)), reverse=True)
    if c * (a + b) <= a * b:
        return a + b
    return (a*b + a*c + b*c)**2 / (4*a*b*c)


def square_envelope(a, b, c, omega):
    a, b, c = sorted(map(F, (a, b, c)), reverse=True)
    return a + b + (omega - 2)*c


def profiles(h):
    h1, h2, h3 = h
    for g in range(min(h) + 1):
        for a in range(min(h1-g, h2-g) + 1):
            for b in range(min(h1-g-a, h3-g) + 1):
                for c in range(min(h2-g-a, h3-g-b) + 1):
                    yield g, a, b, c


def predicted(h, support, characteristic_two=False):
    if 2*max(h) > sum(h):
        return F(max(h))
    e = (F(h[0]+h[1]-h[2], 2),
         F(h[0]+h[2]-h[1], 2),
         F(h[1]+h[2]-h[0], 2))
    parity = sum(h) % 2
    if not parity:
        return support(*e)
    lower = tuple(value-F(1, 2) for value in e)
    if not characteristic_two:
        return 1 + support(*lower)
    maximum_index = max(range(3), key=lambda i: lower[i])
    chosen = support(*(value+int(maximum_index == j)
                       for j, value in enumerate(lower)))
    return chosen


def run():
    counts = Counter()
    profile_count = 0
    maximum_capacity = 8
    omegas = (F(2), F(9, 4), F(5, 2), F(3))
    maxima = {}

    def check(condition, category):
        counts[category] += 1
        assert condition, category

    for h in product(range(maximum_capacity + 1), repeat=3):
        integer_profiles = tuple(profiles(h))
        profile_count += len(integer_profiles)
        actual = max([F(max(h))] + [g+upper_u(a, b, c)
                                    for g, a, b, c in integer_profiles])
        actual_two = max([F(max(h))] + [upper_u(a, b, c)
                                        for g, a, b, c in integer_profiles if g == 0])
        check(actual == predicted(h, upper_u), "full_u_integer_envelope")
        check(actual_two == predicted(h, upper_u, True), "characteristic_two_envelope")
        reduced = max([F(max(h))] + [g+upper_u(a, b, c)
                                     for g, a, b, c in integer_profiles if g <= 1])
        check(actual == reduced, "g_zero_or_one_suffices")
        check(actual_two <= actual, "characteristic_two_never_worse")
        maxima[h] = (actual, actual_two)
        for omega in omegas:
            support = lambda a, b, c, omega=omega: square_envelope(a, b, c, omega)
            observed = max([F(max(h))] + [g+support(a, b, c)
                                         for g, a, b, c in integer_profiles])
            check(observed == predicted(h, support), "square_tiling_integer_envelope")

    for q in range(maximum_capacity + 1):
        m, parity = divmod(q, 2)
        expected = F(9*m, 4) + parity
        check(maxima[q, q, q][0] == expected, "equal_size_closed_formula")
        expected_two = upper_u(m+1, m, m) if parity else F(9*m, 4)
        check(maxima[q, q, q][1] == expected_two, "equal_size_characteristic_two_formula")
        if parity:
            check(expected-expected_two == F(m, 4*(m+1)), "equal_size_exact_saving")

    table = []
    for k in range(2, 3*maximum_capacity + 1):
        h = ((k+2)//3, (k+1)//3, k//3)
        actual, actual_two = maxima[h]
        table.append({"degree": k, "block_lengths": h,
                      "integer_envelope": str(actual),
                      "characteristic_two_envelope": str(actual_two),
                      "continuous_envelope": str(predicted(h, upper_u)
                                                 if sum(h) % 2 == 0
                                                 else upper_u(F(h[0]+h[1]-h[2], 2),
                                                              F(h[0]+h[2]-h[1], 2),
                                                              F(h[1]+h[2]-h[0], 2)))})
    return {
        "status": "PASS", "assertions": sum(counts.values()),
        "categories": dict(counts),
        "capacity_range": {"minimum": 0, "maximum": maximum_capacity,
                           "ordered_triples": (maximum_capacity+1)**3},
        "profile_assignments_enumerated": profile_count,
        "square_exponents": [str(value) for value in omegas],
        "balanced_degree_table": table,
        "scope": "Exact rational finite maxima of specified U and square-tiling certificates, with input-table cost included. No matrix-multiplication or arithmetic-circuit lower bound; no numerical proof of the general theorem.",
    }


if __name__ == "__main__":
    report = run()
    report["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    destination = Path(__file__).resolve().parents[1] / "results" / "integer_capacity_profile_checks.json"
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "assertions": report["assertions"],
                      "profile_assignments_enumerated": report["profile_assignments_enumerated"]}))
