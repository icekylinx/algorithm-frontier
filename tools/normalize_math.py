#!/usr/bin/env python3
"""Normalize maintained Markdown math to the repository's GitHub-safe notation.

Only mathematical spans are changed. Inline code, ordinary code fences and
HTML comments stay byte-for-byte intact. The transformations preserve values
and statements: upright operator names use ``\\mathrm``, transitional display
delimiters become dollar delimiters, and inline math stays on one physical line.
Run without arguments to normalize Markdown and catalogue.json; use --check
to report stale notation without writing any files. Requires only Python.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"(?m)^ {0,3}(`{3,}|~{3,})([^\n]*)(?:\n|$)")
TICKS = re.compile(r"`+")


def normalize_body(body: str) -> str:
    """Use upright text for named operators without defining TeX macros."""
    # Preserve the under/over placement requested by the starred operator form.
    starred = re.compile(r"(?<!\\)\\operatorname\*(?![A-Za-z])\s*\{")
    while (match := starred.search(body)) is not None:
        opening = match.end() - 1
        depth, position = 1, opening + 1
        while position < len(body) and depth:
            if body[position] == "\\":
                position += 2
                continue
            depth += (body[position] == "{") - (body[position] == "}")
            position += 1
        if depth:
            break  # The syntax checker reports the unmatched argument brace.
        name = body[opening + 1:position - 1]
        body = (body[:match.start()] + r"\mathop{\mathrm{" + name +
                r"}}\limits" + body[position:])
    body = re.sub(r"(?<!\\)\\operatorname(?![A-Za-z*])", r"\\mathrm", body)
    # MathJax/LaTeX do not define a standalone \\arg command.
    body = re.sub(r"(?<!\\)\\arg(?![A-Za-z])", r"\\mathrm{arg}\\,", body)
    body = body.replace("−", "-")

    def move_tag(match: re.Match[str]) -> str:
        # A tag belongs to the outer display, not an aligned/split subformula.
        inner = match[2]
        tags = re.findall(r"\\tag\*?\{[^{}]*\}", inner)
        if len(tags) != 1:
            return match[0]
        inner = re.sub(r"[ \t]*\\tag\*?\{[^{}]*\}", "", inner).rstrip()
        return (r"\begin{" + match[1] + "}" + inner + "\n" +
                r"\end{" + match[1] + "}\n" + tags[0])

    body = re.sub(r"\\begin\{(aligned|gathered|split)\}([\s\S]*?)\\end\{\1\}",
                  move_tag, body)
    return body


def normalize_markdown(text: str) -> str:
    """Normalize rendered mathematics while preserving code and comments."""
    output: list[str] = []
    index = 0
    while index < len(text):
        if text.startswith("<!--", index):
            end = text.find("-->", index + 4)
            end = len(text) if end < 0 else end + 3
            output.append(text[index:end])
            index = end
            continue
        if index == 0 or text[index - 1] == "\n":
            fence = FENCE.match(text, index)
            if fence:
                marker, info = fence.groups()
                closing = re.compile(
                    r"(?m)^ {0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}[ \t]*(?:\n|$)"
                ).search(text, fence.end())
                if closing:
                    output.append(text[index:fence.end()])
                    body = text[fence.end():closing.start()]
                    output.append(normalize_body(body) if info.strip() == "math" else body)
                    output.append(closing[0])
                    index = closing.end()
                    continue
        if text[index] == "`":
            ticks = TICKS.match(text, index)
            assert ticks is not None
            closing = next((m for m in TICKS.finditer(text, ticks.end())
                            if len(m[0]) == len(ticks[0])), None)
            end = closing.end() if closing else ticks.end()
            output.append(text[index:end])
            index = end
            continue
        opener = next((token for token in ("$$", "$`", "$", r"\[", r"\(")
                       if text.startswith(token, index)), None)
        if opener:
            closer = {"$$": "$$", "$`": "`$", "$": "$", r"\[": r"\]", r"\(": r"\)"}[opener]
            position = index + len(opener)
            while position < len(text):
                if text.startswith(closer, position):
                    break
                position += 2 if text[position] == "\\" else 1
            if position < len(text):
                body = normalize_body(text[index + len(opener):position])
                if opener in {"$$", r"\["}:
                    if opener == r"\[":
                        # Transitional delimiters may occur next to prose.
                        prefix = "" if not output or output[-1].endswith("\n") else "\n"
                        output.append(prefix + "$$\n" + body.strip() + "\n$$\n")
                    else:
                        output.append("$$" + body + "$$")
                else:
                    # GitHub's inline renderer should never depend on a line join.
                    body = re.sub(r"\s*\n\s*", " ", body)
                    output.append(("$`" + body + "`$") if opener == "$`" else "$" + body + "$")
                index = position + len(closer)
                continue
        if text[index] == "\\":
            output.append(text[index:index + 2])
            index += 2
        else:
            output.append(text[index])
            index += 1
    return "".join(output)


def normalize_catalogue(text: str) -> str:
    def walk(value: object) -> object:
        if isinstance(value, str):
            return normalize_markdown(value)
        if isinstance(value, list):
            return [walk(item) for item in value]
        if isinstance(value, dict):
            return {key: walk(item) for key, item in value.items()}
        return value
    return json.dumps(walk(json.loads(text)), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files/directories or catalogue.json")
    parser.add_argument("--check", action="store_true", help="report required changes without writing")
    args = parser.parse_args()
    paths: set[Path] = set()
    for path in args.paths or [ROOT]:
        if not path.exists():
            parser.error(f"path does not exist: {path}")
        if path.is_dir():
            paths.update(p for p in path.rglob("*.md")
                         if not any(part in {".git", ".venv", "node_modules", "__pycache__"} for part in p.parts))
            catalogue = path / "catalogue.json"
            if catalogue.is_file():
                paths.add(catalogue)
        else:
            paths.add(path)
    changed: list[str] = []
    for path in sorted(paths):
        before = path.read_text(encoding="utf-8")
        after = (normalize_catalogue(before) if path.name == "catalogue.json" else normalize_markdown(before))
        if after != before:
            changed.append(str(path))
            if not args.check:
                path.write_text(after, encoding="utf-8")
    if args.check and changed:
        print("math notation requires normalization:\n" + "\n".join(changed), file=sys.stderr)
        return 1
    print(f"math notation {'checked' if args.check else 'normalized'}: {len(paths)} files; {len(changed)} changes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
