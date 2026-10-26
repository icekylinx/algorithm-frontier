#!/usr/bin/env python3
"""Portable mathematics for GitHub: code spans and checked-in SVG images.

The displayed page contains no client-side TeX. Inline source is retained in
an escaped code element; display source is retained in a non-rendering comment.
Both representations round-trip to ordinary mathematical Markdown for the
incremental TeX migration. The SVG name depends on its exact normalized source.
This module uses only the Python standard library and does not render images.
"""
from __future__ import annotations

import hashlib
import html
import os
from pathlib import Path
import re
import textwrap

from normalize_math import FENCE, TICKS, normalize_body

ROOT = Path(__file__).resolve().parents[1]
INLINE = '<code class="math">'
DISPLAY = '<!-- math-display: '
IMAGE = re.compile(r'\s*\n[ \t]*!\[Formula\]\([^\n)]+\)(?:\n|$)')


def canonical_tex(tex: str, *, display: bool) -> str:
    tex = normalize_body(tex)
    if display:
        return textwrap.dedent(tex).strip()
    return re.sub(r'\s*\n\s*', ' ', tex).strip()


def equation_key(tex: str) -> str:
    return hashlib.sha256(tex.encode('utf-8')).hexdigest()[:24]


def _code(tex: str) -> str:
    # Entities also prevent a literal table pipe from creating another cell.
    escaped = html.escape(tex, quote=False).replace('|', '&#124;')
    return INLINE + escaped + '</code>'


def transform(text: str, path: Path, *, source: bool = False,
              records: list[dict[str, object]] | None = None,
              root: Path = ROOT) -> str:
    """Present math or restore its source, leaving ordinary code untouched."""
    output: list[str] = []
    index = 0

    def emit_math(body: str, display: bool, position: int, indent: str = '') -> str:
        tex = canonical_tex(body, display=display)
        if records is not None:
            records.append({'path': path.relative_to(root).as_posix(),
                            'line': text.count('\n', 0, position) + 1,
                            'display': display, 'tex': tex,
                            'key': equation_key(tex) if display else None})
        if source:
            return ('$$\n' + '\n'.join(indent + line for line in tex.splitlines()) +
                    '\n' + indent + '$$') if display else '$' + tex + '$'
        if not display:
            return _code(tex)
        key = equation_key(tex)
        if '-->' in tex:
            raise ValueError(f'{path}: a display contains the HTML comment terminator')
        asset = root / 'assets' / 'math' / (key + '.svg')
        relative = os.path.relpath(asset, path.parent).replace(os.sep, '/')
        return (DISPLAY + key + '\n' +
                '\n'.join(indent + line for line in tex.splitlines()) +
                '\n' + indent + '-->\n' + indent +
                '![Formula](' + relative + ')')

    while index < len(text):
        if text.startswith(DISPLAY, index):
            end = text.find('-->', index + len(DISPLAY))
            if end < 0:
                raise ValueError(f'{path}: unterminated display source')
            opening_end = text.find('\n', index, end)
            if opening_end < 0:
                raise ValueError(f'{path}: display source has no body')
            body = text[opening_end + 1:end]
            image = IMAGE.match(text, end + 3)
            if image is None:
                raise ValueError(f'{path}: display source has no generated image')
            line_start = text.rfind('\n', 0, index) + 1
            indent = text[line_start:index]
            if indent.strip():
                indent = ''
            output.append(emit_math(body, True, index, indent))
            if image[0].endswith('\n'):
                output.append('\n')
            index = image.end()
            continue
        if text.startswith('<!--', index):
            end = text.find('-->', index + 4)
            end = len(text) if end < 0 else end + 3
            output.append(text[index:end])
            index = end
            continue
        if text.startswith(INLINE, index):
            end = text.find('</code>', index + len(INLINE))
            if end < 0:
                raise ValueError(f'{path}: unterminated inline mathematical code')
            output.append(emit_math(html.unescape(text[index + len(INLINE):end]), False, index))
            index = end + len('</code>')
            continue
        if index == 0 or text[index - 1] == '\n':
            fence = FENCE.match(text, index)
            if fence:
                marker, info = fence.groups()
                closing = re.compile(
                    r'(?m)^ {0,3}' + re.escape(marker[0]) + '{' + str(len(marker)) +
                    r',}[ \t]*(?:\n|$)').search(text, fence.end())
                if closing:
                    if info.strip() == 'math':
                        indent = re.match(r' *', fence[0])[0]
                        output.append(indent + emit_math(text[fence.end():closing.start()], True, index, indent))
                        if closing[0].endswith('\n'):
                            output.append('\n')
                    else:
                        output.append(text[index:closing.end()])
                    index = closing.end()
                    continue
        if text[index] == '`':
            ticks = TICKS.match(text, index)
            assert ticks is not None
            closing = next((m for m in TICKS.finditer(text, ticks.end())
                            if len(m[0]) == len(ticks[0])), None)
            end = closing.end() if closing else ticks.end()
            output.append(text[index:end])
            index = end
            continue
        opener = next((token for token in ('$$', '$`', '$', r'\[', r'\(')
                       if text.startswith(token, index)), None)
        if opener:
            closer = {'$$': '$$', '$`': '`$', '$': '$', r'\[': r'\]', r'\(': r'\)'}[opener]
            position = index + len(opener)
            while position < len(text):
                if text.startswith(closer, position):
                    break
                position += 2 if text[position] == '\\' else 1
            if position < len(text):
                is_display = opener in {'$$', r'\['}
                line_start = text.rfind('\n', 0, index) + 1
                prefix = text[line_start:index]
                indent = prefix if not prefix.strip() else ''
                lead = '\n\n' if is_display and prefix.strip() else ''
                following = text[position + len(closer):].split('\n', 1)[0]
                tail = '\n\n' if is_display and following.strip() else ''
                output.append(lead + emit_math(text[index + len(opener):position],
                                               is_display, index, indent) + tail)
                index = position + len(closer)
                continue
        if text[index] == '\\':
            output.append(text[index:index + 2])
            index += 2
        else:
            output.append(text[index])
            index += 1
    return ''.join(output)


def present_markdown(text: str, path: Path, *, root: Path = ROOT) -> str:
    return transform(text, path, root=root)


def restore_markdown(text: str, path: Path, *, root: Path = ROOT) -> str:
    return transform(text, path, root=root, source=True)
