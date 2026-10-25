#!/usr/bin/env python3
"""Enforce the compact problem-card field contract.

Every public problem card uses the same eight labels so that the index can be
scanned mechanically.  The check intentionally validates presentation
structure only; mathematical truth remains a review task.
"""
from __future__ import annotations

from pathlib import Path
import re

REQUIRED = (
    "Objective and output",
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
        for label in REQUIRED:
            count = len(re.findall(r"\*\*" + re.escape(label) + r"\*\*", text))
            if count == 0:
                errors.append(f"{path}: missing **{label}**")
            elif count > 1:
                errors.append(f"{path}: duplicate **{label}** ({count})")
    if errors:
        raise SystemExit("card schema check failed:\n" + "\n".join(errors))
    print(f"card schema check passed ({len(cards)} cards)")


if __name__ == "__main__":
    main()
