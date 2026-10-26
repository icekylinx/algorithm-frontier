#!/usr/bin/env python3
"""Enforce the readable, table-free problem-card field contract.

Every public problem card uses the same nine standalone labels and full-width
paragraphs. Dense field/refinement tables are deliberately excluded. The index
can still be scanned mechanically.  The check intentionally validates presentation
structure only; mathematical truth remains a review task.
"""
from __future__ import annotations

from pathlib import Path
import re

REQUIRED = (
    "Objective and output",
    "Randomness",
    "Time",
    "Space",
    "Parameters",
    "Model and representation",
    "Lower-bound scope",
    "Review status",
    "Source",
)


def main() -> None:
    errors: list[str] = []
    repo_root = Path(__file__).resolve().parents[1]
    cards = sorted((repo_root / "problems").glob("*/README.md"))
    if not cards:
        raise SystemExit("no problem cards found")
    for path in cards:
        text = path.read_text(encoding="utf-8")
        positions: list[int] = []
        for label in REQUIRED:
            count = len(re.findall(r"\*\*" + re.escape(label) + r"\*\*", text))
            if count == 0:
                errors.append(f"{path}: missing **{label}**")
            elif count > 1:
                errors.append(f"{path}: duplicate **{label}** ({count})")
            else:
                positions.append(text.index(f"**{label}**"))
                if not re.search(r"(?m)^\*\*" + re.escape(label) + r"\*\*$\n\n\S", text):
                    errors.append(f"{path}: **{label}** must introduce a separate paragraph")
        if re.search(r"(?m)^ *\|[ :|\-]+\| *$", text):
            errors.append(f"{path}: use stacked result entries instead of Markdown tables")
        if len(positions) == len(REQUIRED) and positions != sorted(positions):
            errors.append(f"{path}: required fields are out of order")
    if errors:
        raise SystemExit("card schema check failed:\n" + "\n".join(errors))
    print(f"card schema check passed ({len(cards)} cards)")


if __name__ == "__main__":
    main()
