#!/usr/bin/env python3
"""Exact arithmetic checks for promoted constants in the public cards.

The checks are intentionally small and auditable: they use only Python's
``fractions.Fraction`` and do not attempt to prove any theorem.  A failure
means that a displayed constant, decimal, or finite bucket identity has
become inconsistent with the curated record.
"""
from __future__ import annotations

from fractions import Fraction
from math import isclose


def assert_close(name: str, value: Fraction, decimal: str, tol: str = "1e-15") -> None:
    expected = float(decimal)
    if not isclose(float(value), expected, rel_tol=0.0, abs_tol=float(tol)):
        raise AssertionError(f"{name}: {value} != {decimal}")


def check_subset_sum_constants() -> None:
    fast = Fraction(149809813343531, 301754962128739)
    assert_close("fast Subset Sum exponent", fast, "0.4964618056", "1e-10")
    low_space = Fraction(18261635770550353, 10**17)
    assert_close("low-space exponent", low_space, "0.18261635770550353", "1e-18")
    # The older rational is a valid weaker upper bound, not an equality.
    if not low_space < Fraction(137, 750):
        raise AssertionError("low-space exponent must improve 137/750")


def check_bucket_curve() -> None:
    # The processing-bucket construction has gamma_k decreasing to 3/2.
    values = []
    for k in range(1, 32):
        gamma = Fraction(3 * (2**k) - 1, (2 ** (k + 1)) - 1)
        values.append(gamma)
        if not Fraction(3, 2) < gamma <= Fraction(2, 1):
            raise AssertionError(f"invalid bucket factor at k={k}: {gamma}")
    if any(values[i + 1] >= values[i] for i in range(len(values) - 1)):
        raise AssertionError("bucket factors must strictly decrease")
    if values[-1] - Fraction(3, 2) >= Fraction(1, 2**30):
        raise AssertionError("bucket curve does not approach 3/2 at the checked depth")


def check_activation_curve() -> None:
    # Activated profiles use the same gamma_k curve, with one inactive label.
    for k in range(1, 16):
        gamma = Fraction(3 * (2**k) - 1, (2 ** (k + 1)) - 1)
        if gamma <= Fraction(3, 2):
            raise AssertionError(f"activation factor crossed 3/2 at k={k}")


def main() -> None:
    check_subset_sum_constants()
    check_bucket_curve()
    check_activation_curve()
    print("rational certificate checks passed")


if __name__ == "__main__":
    main()
