#!/usr/bin/env python3
"""Exhaustively replay the displayed seven-element non-Fano example.

This checks the finite arithmetic example only; it is not formal verification
of the surrounding Gaussian or sparsification claims.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/checkpoint-x/38_non_fano_obstruction_to_fixed_amplitude_bound.md"
A = ((1, 0, 0, 1, 1, 0, 1), (0, 1, 0, 1, 0, 1, 1), (0, 0, 1, 0, 1, 1, 1))
WEIGHTS = (6, 5, 3, 5, 5, 5, 6)


def support(vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(i for i, value in enumerate(vector) if value % 3)


def main() -> int:
    if not SOURCE.is_file():
        raise SystemExit("obstruction check failed: source is missing")
    supports = set()
    for coefficients in product(range(3), repeat=3):
        if coefficients == (0, 0, 0):
            continue
        row = tuple(sum(coefficients[i] * A[i][j] for i in range(3)) % 3 for j in range(7))
        supports.add(support(row))
    if len(supports) != 13:
        raise SystemExit(f"obstruction check failed: expected 13 supports, got {len(supports)}")
    valid = []
    for positive in product((0, 1), repeat=7):
        if all(2 * sum(WEIGHTS[i] * positive[i] for i in query) <= sum(WEIGHTS[i] for i in query) for query in supports):
            valid.append(positive)
    if len(valid) != 15:
        raise SystemExit(f"obstruction check failed: expected 15 valid supports, got {len(valid)}")
    probability = Fraction(len(valid), 2**7)
    if probability != Fraction(15, 128) or not probability < Fraction(1, 8):
        raise SystemExit("obstruction check failed: probability identity")
    print("checkpoint-X non-Fano obstruction check passed: 13 row supports, 15/128 < 1/8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
