#!/usr/bin/env python3
"""Reject TeX math in GitHub-facing display pages.

Imported manuscripts and detailed proof maps are intentionally excluded: they
preserve source notation. The check applies to the landing pages and curated
problem result cards, where portable code-span notation is the repository
standard.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
paths = [
    ROOT / "README.md",
    ROOT / "OVERVIEW.md",
    ROOT / "CONTENTS.md",
    ROOT / "FORMATTING.md",
    ROOT / "docs/COMPLEXITY.md",
    ROOT / "docs/PRIORITY.md",
    ROOT / "docs/MAINTENANCE_LOOP.md",
]
paths += sorted((ROOT / "problems").glob("*/README.md"))
paths.append(ROOT / "problems/README.md")
errors = []
tex_delimiter = re.compile(r"\$\$|(?<!\$)\$[^$\n]+\$(?!\$)|\\(?:\(|\)|\[|\])|\\begin\{(?:equation|align|gather)")
tex_command = re.compile(r"\\(?:mathrm|operatorname|mathbb|mathbf|mathsf|frac|binom|sqrt|Gamma|varepsilon|epsilon|exp|log|cdot|times)\b")
for path in paths:
    if not path.is_file():
        errors.append(f"missing display page: {path}")
        continue
    text = path.read_text(errors="replace")
    if tex_delimiter.search(text):
        errors.append(f"TeX delimiter in display page: {path}")
    if tex_command.search(text):
        errors.append(f"TeX command in display page: {path}")
if errors:
    print("DISPLAY NOTATION CHECK FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"DISPLAY NOTATION CHECK OK: {len(paths)} display pages")
