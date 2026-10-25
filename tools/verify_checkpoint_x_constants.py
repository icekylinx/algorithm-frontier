#!/usr/bin/env python3
"""Check the exact rational arithmetic exposed by the checkpoint-X SS draft.

This is a consistency check for the displayed constants only.  It does not
verify the contact inequalities, circuit compiler, or asymptotic theorem.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/checkpoint-x/02_deterministic_subset_sum_increment.md"
CARD = ROOT / "problems/subset-sum-fast-deterministic-x-draft/README.md"
OLD = Fraction(149809813343531, 301754962128739)
NEW = Fraction(149809813343531, 301825962128739)
EXPECTED_DECIMAL = 0.4963450204447026


def fail(message: str) -> None:
    raise SystemExit(f"checkpoint-X constant check failed: {message}")


def main() -> int:
    if not SOURCE.is_file() or not CARD.is_file():
        fail("draft source or card is missing")
    source_text = SOURCE.read_text(encoding="utf-8")
    card_text = CARD.read_text(encoding="utf-8")
    fraction = rf"{NEW.numerator}\s*/\s*{NEW.denominator}"
    latex_fraction = rf"\\frac\{{{NEW.numerator}\}}\{{{NEW.denominator}\}}"
    if not (re.search(fraction, source_text) or re.search(latex_fraction, source_text)):
        fail("new fraction is missing from the source draft")
    if not re.search(fraction, card_text):
        fail("new fraction is missing from the draft card")
    if not NEW < OLD:
        fail("new exponent is not strictly smaller than the pinned old exponent")
    if abs(float(NEW) - EXPECTED_DECIMAL) > 1e-15:
        fail("decimal expansion does not match the exact new fraction")
    if abs(float(OLD) - 0.496461805587) > 1e-12:
        fail("pinned old decimal sanity check failed")
    print(
        "checkpoint-X rational constant check passed: "
        f"new={NEW.numerator}/{NEW.denominator}={float(NEW):.16f} "
        f"< old={OLD.numerator}/{OLD.denominator}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
