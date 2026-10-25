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
NEW = Fraction(158153814247997, 318927986919134)
D_U = Fraction(58153814247997, 10**14)
G_L = Fraction(131017921157, 10**13)
MU = Fraction(50000000000000, 159463993459567)
D0 = Fraction(1, 50)
EXPECTED_DECIMAL = 0.4958919277538907


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

    # The new ledger states E_new = mu(1 + D_U) = 1/2 - mu*g_L.
    # Check those identities exactly and make sure the displayed gate values
    # are on the claimed side of the fixed constraints.
    for marker in (str(D_U.numerator), str(G_L.numerator), str(MU.numerator)):
        if marker not in source_text:
            fail(f"ledger marker {marker} is missing from the source draft")
    if MU * (1 + D_U) != NEW:
        fail("mu(1 + D_U) does not equal the displayed new exponent")
    if Fraction(1, 2) - MU * G_L != NEW:
        fail("1/2 - mu*g_L does not equal the displayed new exponent")
    if not (3 * MU < 1 and G_L < D0):
        fail("dictionary-fitting inequalities fail")

    print(
        "checkpoint-X rational constant check passed: "
        f"new={NEW.numerator}/{NEW.denominator}={float(NEW):.16f} "
        f"< old={OLD.numerator}/{OLD.denominator}; ledger identities exact"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
