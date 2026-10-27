#!/usr/bin/env python3
"""Reject recognizable bare math in public prose, not canonical manuscripts.

Showcases use source-bound SVGs; parameters and exact data use literal code.
This lexical guard supplements the manual purpose review. It cannot infer
whether an isolated ordinary word or letter denotes a mathematical variable.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BARE_MATH = re.compile(
    r"\\(?:frac|sqrt|log|varepsilon|lambda|Theta|Gamma|binom|mathcal|mathrm)\b"
    r"|\b(?:O|Theta|Omega|poly|binom|log|sqrt|exp)\s*\("
    r"|\b(?:[A-Za-z]|OPT|FOPT|Gamma|rank|dim)\([^)]*\)"
    r"|[A-Za-z0-9][_^][A-Za-z0-9({]"
    r"|\b[A-Za-z][A-Za-z0-9_]*(?:\([^)]*\))?\s*(?:<=|>=|=|<|>)\s*[A-Za-z0-9({]"
    r"|[≥≤≠∈∉∑∏√⊆ΘΩαβγδεζηθκλμνξρστφχψω²³]"
    r"|(?<![\w./])\d+/\d+(?![\w/]|\.\d)"
    r"|\b(?:nu|epsilon|rho|lambda|kappa)\b"
    r"|&(?:lt|gt|le|ge);"
)


def prose_lines(text: str):
    """Keep visible prose and line numbers, removing source/data containers."""
    for pattern in (r"<!--.*?-->", r"<code\b[^>]*>.*?</code>", r"<pre\b[^>]*>.*?</pre>"):
        text = re.sub(pattern, lambda m: "\n" * m[0].count("\n"), text, flags=re.S)
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None or line.startswith("    ") or line.startswith("\t"):
            continue
        line = re.sub(r"(`+).*?\1", "", line)
        line = re.sub(r"\]\([^)]*\)", "]", line)
        line = re.sub(r"https?://\S+", "", line)
        line = re.sub(r"</?(?:a|em|strong|span|div|p|br|img|table|thead|tbody|tr|td|th|sup|sub|details|summary|h[1-6])(?:\s[^>]*)?/?>", "", line)
        # A linked filename is an identifier, not an algebraic subscript.
        line = re.sub(r"\b[\w./-]+\.(?:py|json|md|tex|pdf|svg|zip)\b", "", line)
        yield number, line


def public_pages():
    pages = set(ROOT.glob("*.md"))
    pages.update((ROOT / "docs").rglob("*.md"))
    pages.update((ROOT / "provenance").rglob("*.md"))
    pages.update((ROOT / "tools").glob("README.md"))
    pages.update((ROOT / "tools").glob("*/README.md"))
    pages.add(ROOT / "reviews/README.md")
    pages.update(p for p in (ROOT / "problems").rglob("*.md")
                 if p.name in {"README.md", "sources.md"})
    return sorted(pages)


def main() -> int:
    failures = []
    pages = public_pages()
    for path in pages:
        for number, line in prose_lines(path.read_text()):
            match = BARE_MATH.search(line)
            if match:
                failures.append(f"{path.relative_to(ROOT)}:{number}: bare mathematical text {match[0]!r}")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"Public mathematics checked: {len(pages)} pages; canonical manuscripts retain their stated exceptions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
