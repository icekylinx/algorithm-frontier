#!/usr/bin/env python3
"""Check relative Markdown links in the curated and actively reviewed trees."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {"README.md", "CONTENTS.md", "CONTRIBUTING.md", "PROTOCOL.md", "HISTORY.md"}
ROOT_DIRS = ("docs", "problems", "manuscripts", "reviews", "provenance")
EXTRA_DIRS = ()
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def markdown_files() -> list[Path]:
    files = [ROOT / name for name in ROOT_FILES if (ROOT / name).is_file()]
    for dirname in ROOT_DIRS:
        directory = ROOT / dirname
        if directory.is_dir():
            files.extend(directory.rglob("*.md"))
    for directory in EXTRA_DIRS:
        if directory.is_dir():
            files.extend(directory.rglob("*.md"))
    return sorted(set(files))


def strip_code(text: str) -> str:
    # Code and mathematics are not Markdown links. A coefficient extraction
    # such as [z^r](1+2z)^k must not be read as a relative URL.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"(?<!\\)\$\$.*?(?<!\\)\$\$", "", text, flags=re.DOTALL)
    text = re.sub(r"\\\[.*?\\\]", "", text, flags=re.DOTALL)
    text = re.sub(r"\\\(.*?\\\)", "", text, flags=re.DOTALL)
    return re.sub(r"(?<![\\$])\$(?!\$).*?(?<!\\)\$(?!\$)", "", text)


def target_exists(source: Path, target: str) -> bool:
    target = unquote(target.strip().strip("<>")).split("#", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return True
    if target.startswith("/"):
        candidate = ROOT / target.lstrip("/")
    else:
        candidate = source.parent / target
    candidate = candidate.resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return False
    if candidate.exists():
        return True
    # GitHub resolves a directory link to its README.
    if candidate.is_dir() and (candidate / "README.md").exists():
        return True
    if candidate.suffix == "" and (candidate.with_suffix(".md")).exists():
        return True
    return False


def main() -> int:
    failures: list[str] = []
    files = markdown_files()
    for source in files:
        text = strip_code(source.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip()
            # Titles in Markdown destinations are rare here; discard a quoted title.
            if raw.startswith("<"):
                destination = raw.split(">", 1)[0] + ">"
            else:
                destination = raw.split(None, 1)[0]
            if not target_exists(source, destination):
                failures.append(f"{source.relative_to(ROOT)} -> {destination}")
    if failures:
        print("internal link check: broken relative links:", file=sys.stderr)
        print("\n".join(f"  {item}" for item in failures), file=sys.stderr)
        return 1
    print(f"internal link check: {len(files)} Markdown files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
