#!/usr/bin/env python3
# Copyright 2026 Yilin Liu. AI contribution identifier: GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Exact finite crossing coefficients and original ordered substitutions.

Expected coefficients are the literal Kronecker crossing tensor; expected
ring values are direct X Y X Y products. No fast matrix scheme is assumed
or implemented. Standard library only, fixed seed, writes no files.
"""

from collections import Counter, defaultdict
from pathlib import Path
import json
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference"))
from integral_crossing import mixed_factors, ordered_evaluation
from schur_modes import partitions


def expand_word_coefficients(factors):
    """Expand ordered words, independently of the ring evaluation routine."""
    coefficients = defaultdict(int)
    for orientation, left, right in factors:
        for (x, a), c in left.items():
            for (v, b), d in right.items():
                y, u = (a, b) if orientation == "row" else (b, a)
                coefficients[x, y, v, u] += c*d
    return {key: value for key, value in coefficients.items() if value}


def matrix_ring(modulus):
    """Independent exact M_2(Z) or M_2(Z/modulus); no producer helpers."""
    def reduce(values):
        return tuple(v % modulus for v in values) if modulus else tuple(values)

    def add(a, b):
        return reduce(x+y for x, y in zip(a, b))

    def mul(a, b):
        a00, a01, a10, a11 = a
        b00, b01, b10, b11 = b
        return reduce((a00*b00+a01*b10, a00*b01+a01*b11,
                       a10*b00+a11*b10, a10*b01+a11*b11))

    def scale(c, a):
        return reduce(c*v for v in a)

    return {"zero": (0, 0, 0, 0), "add": add, "mul": mul, "scale": scale}


def main():
    if not __debug__:
        raise SystemExit("Run without -O: this checker uses assertions")
    counts, orientations = Counter(), Counter()
    rng = random.Random(27102026)

    def check(label, condition):
        assert condition, label
        counts[label] += 1

    for h in range(1, 4):
        for energy in range(1, 4):
            n, m = len(partitions(h)), len(partitions(energy))
            factors = mixed_factors(h, energy)
            orientations.update(term[0] for term in factors)
            actual = expand_word_coefficients(factors)
            expected = {(x, y, x, y): 1 for x in range(n) for y in range(m)}
            check("complete_integer_crossing", actual == expected)
            for x in range(n):
                for y in range(m):
                    for v in range(n):
                        for u in range(m):
                            check("integer_word_coefficient", actual.get((x, y, v, u), 0)
                                  == int(x == v and y == u))
            check("integer_factors", all(type(c) is int for _, left, right in factors
                  for c in tuple(left.values()) + tuple(right.values())))
            check("factor_count_bound", len(factors) <= sum(min(
                sum(len(partitions(energy+s-h+i)) for i in range(2*h+1)),
                sum(len(partitions(energy+h-s-i)) for i in range(2*h+1)))
                for s in range(-energy-h, energy+h+1)))

            # Reversing the column interior would destroy word order. Detect
            # this mutation in the free-word coefficients without random tests.
            wrong = defaultdict(int)
            for orientation, left, right in factors:
                for (x, a), c in left.items():
                    for (v, b), d in right.items():
                        key = (x, a, v, b) if orientation == "row" else (x, v, b, a)
                        wrong[key] += c*d
            if n > 1 and m > 1:
                check("reversed_interior_guard", dict((k, c) for k, c in wrong.items() if c) != expected)

            for modulus in (None, 2, 3, 4, 5, 6, 8, 9):
                ring = matrix_ring(modulus)
                add, mul = ring["add"], ring["mul"]
                for _ in range(4):
                    xs = [tuple(rng.randrange(-3, 4) for _ in range(4)) for _ in range(n)]
                    ys = [tuple(rng.randrange(-3, 4) for _ in range(4)) for _ in range(m)]
                    expected = ring["zero"]
                    for x in xs:
                        for y in ys:
                            expected = add(expected, mul(mul(mul(x, y), x), y))
                    actual = ordered_evaluation(factors, xs, ys, **ring)
                    check("original_ordered_matrix_value", actual == expected)

    # Each location agrees in both orientations, rather than only after the
    # full crossing sum. These smallest cases avoid large dense Schur tables.
    for h, energy in ((1, 1), (1, 2), (2, 1)):
        for location in range(-h-energy, h+energy+1):
            row = mixed_factors(h, energy, "row", location=location)
            column = mixed_factors(h, energy, "column", location=location)
            check("piece_orientation_identity", expand_word_coefficients(row) == expand_word_coefficients(column))

    # Input contracts reject booleans in numerical parameters and invalid
    # locations before attempting any coefficient construction.
    for args, kwargs in [((True, 1), {}), ((1, True), {}), ((0, 1), {}),
                         ((1.0, 1), {}), ((1, -1), {}), ((1, 1, "bad"), {}),
                         ((1, 1), {"location": True}), ((1, 1), {"location": 3})]:
        try:
            mixed_factors(*args, **kwargs)
        except ValueError:
            check("malformed_input", True)
        else:
            raise AssertionError("malformed input accepted")
    check("both_factor_orientations", set(orientations) == {"row", "column"})
    print(json.dumps({"status": "PASS", "assertions": sum(counts.values()),
                      "categories": dict(counts), "factor_orientations": dict(orientations),
                      "scope": "Nine finite normalization-one Schur crossings and exact ordered substitutions; no asymptotic circuit generator or matrix-interface verification."}, indent=2))


if __name__ == "__main__":
    main()
