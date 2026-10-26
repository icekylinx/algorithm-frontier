#!/usr/bin/env python3
"""Build or verify portable Markdown formulas and their standalone SVG assets.

Normal verification is Python-only and checks exact source/image bindings.
Rendering new or changed formulas needs the pinned optional Node renderer:
  npm ci --prefix tools/math-renderer
  python3 tools/build_math_assets.py
No network, JavaScript, font, or math renderer is needed to read the pages.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

from math_presentation import ROOT, transform

ASSETS = ROOT / 'assets' / 'math'
MANIFEST = ASSETS / 'manifest.json'
RENDERER = ROOT / 'tools' / 'math-renderer' / 'render.cjs'


def digest(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob('*.md')
                  if not any(part in {'.git', '.venv', 'node_modules', '__pycache__'}
                             for part in p.parts))


def validate_svg(path: Path, tex: str) -> None:
    """Reject external assets, executable elements and clipped/missing canvases."""
    root = ET.fromstring(path.read_bytes())
    ns = '{http://www.w3.org/2000/svg}'
    if root.tag != ns + 'svg':
        raise ValueError(f'{path}: not an SVG image')
    title = root.find(ns + 'title')
    if title is None or title.text != tex:
        raise ValueError(f'{path}: accessible source title does not match the formula')
    viewbox = [float(x) for x in root.attrib.get('viewBox', '').split()]
    if len(viewbox) != 4 or viewbox[2] <= 0 or viewbox[3] <= 0:
        raise ValueError(f'{path}: invalid viewBox')
    if not list(root.iter(ns + 'path')) and not list(root.iter(ns + 'text')):
        raise ValueError(f'{path}: no visible mathematical glyphs')
    for element in root.iter():
        if element.tag.split('}')[-1] in {'script', 'foreignObject', 'iframe', 'image'}:
            raise ValueError(f'{path}: unexpected executable or external element')
        for key, value in element.attrib.items():
            local = key.split('}')[-1]
            if local.lower().startswith('on'):
                raise ValueError(f'{path}: event attribute')
            if local == 'href' and not value.startswith('#'):
                raise ValueError(f'{path}: external glyph reference')
            if 'url(' in value.lower() or 'data-mjx-error' in local:
                raise ValueError(f'{path}: unresolved renderer content')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify saved files without Node or writes')
    parser.add_argument('--force-render', action='store_true', help='regenerate every required SVG')
    args = parser.parse_args()
    if args.check and args.force_render:
        parser.error('--check and --force-render are incompatible')
    records: list[dict[str, object]] = []
    changes: dict[Path, str] = {}
    files = markdown_files()
    for path in files:
        before = path.read_text(encoding='utf-8')
        after = transform(before, path, records=records)
        if before != after:
            changes[path] = after
    equations: dict[str, str] = {}
    for item in records:
        if item['display']:
            key, tex = str(item['key']), str(item['tex'])
            if key in equations and equations[key] != tex:
                raise ValueError('truncated source hash collision')
            equations[key] = tex
    old = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    renderer = {'name': 'MathJax', 'version': '3.2.2',
                'source_sha256': digest(RENDERER.read_bytes())}
    stale_renderer = old.get('renderer') != renderer
    pending = []
    for key, tex in sorted(equations.items()):
        path = ASSETS / (key + '.svg')
        record = old.get('equations', {}).get(key, {})
        if (args.force_render or stale_renderer or not path.exists() or
                record.get('svg_sha256') != digest(path.read_bytes())):
            pending.append({'key': key, 'tex': tex})
    if args.check and (changes or pending):
        for path in changes:
            print('nonportable mathematics: ' + str(path.relative_to(ROOT)), file=sys.stderr)
        if pending:
            print(f'{len(pending)} missing or stale equation images; run tools/build_math_assets.py', file=sys.stderr)
        return 1
    if pending:
        with tempfile.TemporaryDirectory(prefix='af-math-render-') as directory:
            request = Path(directory) / 'request.json'
            request.write_text(json.dumps(pending, ensure_ascii=False), encoding='utf-8')
            subprocess.run(['node', str(RENDERER), str(request), str(ASSETS)], check=True)
    manifest = {'schema_version': 1, 'renderer': renderer, 'equations': {}}
    for key, tex in sorted(equations.items()):
        path = ASSETS / (key + '.svg')
        validate_svg(path, tex)
        manifest['equations'][key] = {'tex_sha256': digest(tex.encode('utf-8')),
                                      'svg_sha256': digest(path.read_bytes())}
    rendered_manifest = json.dumps(manifest, indent=2, ensure_ascii=False) + '\n'
    if args.check:
        if not MANIFEST.exists() or MANIFEST.read_text() != rendered_manifest:
            print('equation manifest is stale; run tools/build_math_assets.py', file=sys.stderr)
            return 1
    else:
        ASSETS.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(rendered_manifest, encoding='utf-8')
        for path, content in changes.items():
            path.write_text(content, encoding='utf-8')
    inline = sum(not bool(item['display']) for item in records)
    displays = len(records) - inline
    print(f'Portable mathematics: {len(files)} pages, {inline} inline code formulas, '
          f'{displays} displays, {len(equations)} unique bound SVGs; '
          f'{len(changes)} pages {"need changes" if args.check else "updated"}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
