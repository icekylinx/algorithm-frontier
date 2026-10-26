#!/usr/bin/env python3
"""Check the retained mathematical source behind static Markdown presentation.

Published Markdown uses inline code and standalone equation images. Its source
is recovered before these grouping/macro checks. The low-level checker also
accepts the protected intermediate syntax used by the source normalizer.
Code spans and ordinary fenced code are excluded from math checks. TeX grouping
braces are checked inside math; ordinary parentheses/brackets are not, because
half-open intervals and one-sided delimiters are valid mathematical notation.
This checks document syntax, not mathematical correctness or TeX semantics.

Every canonical Markdown file receives the complete check. No renderer or
third-party package is required.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
BACKTICKS = re.compile(r"`+")
COMMENTS = re.compile(r"<!--.*?-->", re.DOTALL)


def blank(text: str) -> str:
    """Mask an ignored region without moving line numbers."""
    return "".join("\n" if char == "\n" else " " for char in text)


def check_text(text: str, *, controls_only: bool = False) -> list[tuple[int, str]]:
    errors: list[tuple[int, str]] = []

    def error(offset: int, message: str) -> None:
        errors.append((text.count("\n", 0, offset) + 1, message))

    for offset, char in enumerate(text):
        number = ord(char)
        if (number < 32 and char not in "\t\n\r") or 127 <= number <= 159:
            error(offset, f"forbidden control character U+{number:04X}")
    if controls_only:
        return errors

    def check_braces(body: str, start: int) -> None:
        for match in re.finditer(r"\\operatorname\b\*?", body):
            error(start + match.start(),
                  r"unsupported \operatorname macro; use \mathrm{...}")
        for match in re.finditer(r"\\(?:arg|I|T)\b", body):
            error(start + match.start(),
                  f"undefined math command {match[0]!r}; use an explicit operator or \\setminus")
        environments: list[str] = []
        for match in re.finditer(r"\\(begin|end)\{([^}]+)\}|\\tag\b", body):
            if match[1] == "begin":
                environments.append(match[2])
            elif match[1] == "end":
                if environments and environments[-1] == match[2]:
                    environments.pop()
            elif any(name in {"aligned", "split", "gathered", "alignedat"}
                     for name in environments):
                error(start + match.start(),
                      r"\tag belongs outside the inner alignment environment")
        stack: list[int] = []
        index = 0
        while index < len(body):
            char = body[index]
            if char == "\\":
                # An escaped brace is a displayed delimiter, not a TeX group.
                index += 2
                continue
            if char == "%":
                newline = body.find("\n", index)
                index = len(body) if newline < 0 else newline + 1
                continue
            if char == "{":
                stack.append(index)
            elif char == "}":
                if stack:
                    stack.pop()
                else:
                    error(start + index, "unmatched TeX grouping brace '}'")
            index += 1
        for offset in stack:
            error(start + offset, "unclosed TeX grouping brace '{'")

    # Fences are recognized before inline code, including math blocks.
    masked = list(text)
    fence: tuple[str, int, int, str] | None = None
    body_start = 0
    offset = 0
    for line in text.splitlines(keepends=True):
        match = FENCE.match(line.rstrip("\r\n"))
        if fence is None and match:
            marker, info = match.groups()
            if marker[0] != "`" or "`" not in info:
                fence = (marker[0], len(marker), offset, info.strip())
                body_start = offset + len(line)
                masked[offset:offset + len(line)] = blank(line)
        elif fence is not None:
            char, length, _, info = fence
            if (match and match[1][0] == char and len(match[1]) >= length
                    and not match[2].strip()):
                if info == "math":
                    check_braces(text[body_start:offset], body_start)
                fence = None
            masked[offset:offset + len(line)] = blank(line)
        offset += len(line)
    if fence is not None:
        error(fence[2], f"unclosed fenced block ({fence[0] * fence[1]})")

    content = COMMENTS.sub(lambda match: blank(match[0]), "".join(masked))
    index = 0
    opening: tuple[str, str, int, int] | None = None
    while index < len(content):
        if opening is None:
            if content[index] == "`":
                run = BACKTICKS.match(content, index)
                assert run is not None
                # CommonMark closes a code span with the same run length.
                closing = next(
                    (candidate for candidate in BACKTICKS.finditer(content, run.end())
                     if len(candidate[0]) == len(run[0])),
                    None,
                )
                index = closing.end() if closing else run.end()
                continue
            delimiters = (("$$", "$$"), ("$`", "`$"), (r"\(", r"\)"), (r"\[", r"\]"), ("$", "$"))
            found = next((pair for pair in delimiters if content.startswith(pair[0], index)), None)
            if found:
                left, right = found
                if left != "$`":
                    error(index, "use protected $`...`$ inline math or a fenced math block")
                opening = (left, right, index, index + len(left))
                index += len(left)
                continue
            if content.startswith((r"\)", r"\]"), index):
                error(index, f"unmatched math delimiter {content[index:index + 2]!r}")
                index += 2
                continue
            if content[index] == "\\":
                index += 2
                continue
        else:
            left, right, start, body_start = opening
            if content.startswith(right, index):
                body = content[body_start:index]
                check_braces(body, body_start)
                line_start = content.rfind("\n", 0, start) + 1
                if content[line_start:start].lstrip().startswith("|") and "|" in body:
                    error(start, "literal pipe inside table mathematics; use \\lvert, \\rvert, \\mid or \\Vert")
                if left in {"$", "$`"} and "\n" in content[body_start:index]:
                    error(start, "inline mathematics crosses a line; join it or use a display")
                opening = None
                index += len(right)
                continue
            other = next(
                (token for token in (r"\(", r"\)", r"\[", r"\]", "$$", "$")
                 if content.startswith(token, index)),
                None,
            )
            if other:
                error(index, f"math delimiter {other!r} inside {left!r}; expected {right!r}")
                index += len(other)
                continue
            if content[index] == "%":
                newline = content.find("\n", index)
                index = len(content) if newline < 0 else newline + 1
                continue
            if content[index] == "\\":
                index += 2
                continue
        index += 1
    if opening is not None:
        error(opening[2], f"unclosed math delimiter {opening[0]!r}; expected {opening[1]!r}")
    return errors


def main() -> int:
    from math_presentation import restore_markdown
    from normalize_math import normalize_markdown
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="explicit Markdown files or directories")
    args = parser.parse_args()
    roots = args.paths or [ROOT]
    paths: set[Path] = set()
    for path in roots:
        if not path.exists():
            parser.error(f"path does not exist: {path}")
        paths.update(path.rglob("*.md") if path.is_dir() else [path])
    errors: list[str] = []
    full_count = 0
    for path in sorted(paths):
        if any(part in {".git", ".venv", "node_modules", "__pycache__"} for part in path.parts):
            continue
        try:
            relative = path.resolve().relative_to(ROOT)
        except ValueError:
            relative = path
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            errors.append(f"{relative}: cannot read UTF-8: {exc}")
            continue
        full_count += 1
        errors.extend(
            f"{relative}:{line}: {message}"
            for line, message in check_text(normalize_markdown(restore_markdown(text, path.resolve())))
        )
    if errors:
        print("MARKDOWN MATH CHECK FAILED")
        print("\n".join(f"- {message}" for message in errors))
        return 1
    print(f"Markdown math check passed ({full_count} canonical files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
