#!/usr/bin/env python3
# Copyright 2026 Yilin Liu. AI contribution identifier: GPT-6 Astra Pro.
# SPDX-License-Identifier: Apache-2.0
"""Exact rational arithmetic for the strongest retained circuit exponent."""

from fractions import Fraction as Q
import json


def rectangular_cost(a, b, c):
    """Literal two-branch full-U curve, with zero boundary."""
    a, b, c = sorted((a, b, c), reverse=True)
    if c*(a+b) <= a*b:
        return a+b
    return (a*b+a*c+b*c)**2/(4*a*b*c)


def main():
    if not __debug__:
        raise SystemExit("Run without -O: this checker uses assertions")
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    a, b = Q(167, 400), Q(233, 400)
    root_upper = Q(286667054264, 10**9)
    large = a + root_upper/400
    target = Q(1719516, 10**6)
    gap = Q(358038466018273, 1379112402223945625000)
    check(a+b == 1)
    check(0 < a < b < 1)
    check((400*a)**2 + (400*b)**2 == 82178)
    check(root_upper > 0 and root_upper**2 > 82178)
    check(large > b > a)
    check(a*(large+b) > large*b)  # Curved branch used by the certificate.
    check(target-rectangular_cost(large, b, a) == gap)
    check(gap > 0)
    # The two transfer shapes differ only by a permutation when a+b=1.
    check(rectangular_cost(root_upper/400+a, b, 1-b)
          == rectangular_cost(1-a, a, root_upper/400+1-b))
    # Simple exact boundaries ensure neither branch was silently swapped.
    check(rectangular_cost(Q(1), Q(1), Q(0)) == 2)
    check(rectangular_cost(Q(1), Q(1), Q(1, 2)) == 2)
    check(rectangular_cost(Q(1), Q(1), Q(1)) == Q(9, 4))
    print(json.dumps({"status": "PASS", "assertions": checks,
                      "shape": [str(large), str(b), str(a)],
                      "root_upper": str(root_upper), "exponent": str(target),
                      "positive_gap": str(gap),
                      "scope": "Exact parameter substitution and positive exponent slack only; does not prove the integral full-U matrix theorem or crossing asymptotic."}, indent=2))


if __name__ == "__main__":
    main()
