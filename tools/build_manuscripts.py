#!/usr/bin/env python3
"""Export complete selected proof bodies to TeX without producing draft PDFs.

Pandoc is used only for authoring. --check validates source, generator and
output hashes with Python. Every mathematical AST node is compared with the
source parser before export, so a dropped or changed formula blocks the build.
The generated body fragments deliberately do not invent the missing original
Subset Sum document class, fonts or page geometry.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlsplit

from math_presentation import ROOT, canonical_tex, transform

SOURCES = [
    'problems/general-matching/proof.md',
    'problems/general-matching/reference/certificate-proof.md',
    'problems/general-matching/reference/cover-compression-proof.md',
    'problems/subset-sum-fast-deterministic/proof.md',
    'problems/matroid-failure-summaries/proof.md',
    'problems/matroid-failure-summaries/manuscripts/sharp-represented-matroid-failure-summaries.md',
    'problems/matroid-failure-summaries/manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md',
    'problems/matroid-failure-summaries/manuscripts/weighted-oracle-prefix-fpt-construction.md',
    'problems/matroid-failure-summaries/manuscripts/weighted-oracle-two-failure-obstruction.md',
    'problems/matroid-failure-summaries/manuscripts/two-failure-oracle-prefix-bounds.md',
]
MANIFEST = ROOT / 'manuscripts' / 'tex-exports.json'


def digest(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def walk(node):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from walk(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk(value)


def pandoc(*arguments: str, data: str) -> str:
    return subprocess.run(['pandoc', *arguments], input=data, text=True,
                          capture_output=True, check=True).stdout


def export(source: str, path: Path, expected: list[dict[str, object]]) -> str:
    ast = json.loads(pandoc('--from=markdown+tex_math_dollars+raw_tex', '--to=json', data=source))
    observed = []
    for node in walk(ast):
        if node.get('t') == 'Math':
            kind, tex = node['c']
            display = kind['t'] == 'DisplayMath'
            observed.append((display, canonical_tex(tex, display=display)))
        if node.get('t') in {'Link', 'Image'}:
            target = node['c'][-1][0]
            parsed = urlsplit(target)
            if not parsed.scheme and not target.startswith('#'):
                destination = (path.parent / parsed.path).resolve()
                relative = destination.relative_to(ROOT).as_posix()
                route = 'tree' if destination.is_dir() else 'blob'
                node['c'][-1][0] = ('https://github.com/icekylinx/algorithm-frontier/' +
                                    route + '/main/' + relative +
                                    ('#' + parsed.fragment if parsed.fragment else ''))
        if node.get('t') == 'Str' and node.get('c') == '∎':
            node.clear()
            node.update({'t': 'RawInline', 'c': ['latex', r'\hfill\(\square\)']})
    wanted = [(bool(record['display']), str(record['tex'])) for record in expected]
    if Counter(observed) != Counter(wanted):
        missing = Counter(wanted) - Counter(observed)
        extra = Counter(observed) - Counter(wanted)
        raise ValueError(f'{path}: mathematical conversion mismatch; missing={missing}; extra={extra}')
    return pandoc('--from=json', '--to=latex', '--wrap=none', '--no-highlight',
                  data=json.dumps(ast, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Python-only saved-export checks')
    args = parser.parse_args()
    old = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    generator = digest(Path(__file__).read_bytes())
    version = old.get('pandoc_version') if args.check else subprocess.check_output(
        ['pandoc', '--version'], text=True).splitlines()[0]
    entries = []
    failures = []
    old_entries = {item['source']: item for item in old.get('exports', [])}
    for name in SOURCES:
        path = ROOT / name
        records: list[dict[str, object]] = []
        source = transform(path.read_text(), path, source=True, records=records)
        source_hash = digest(source.encode('utf-8'))
        target = path.with_suffix('.tex')
        if args.check:
            entry = old_entries.get(name, {})
            if (entry.get('source_sha256') != source_hash or not target.exists() or
                    entry.get('tex_sha256') != digest(target.read_bytes()) or
                    entry.get('math_nodes') != len(records)):
                failures.append(name)
            continue
        body = export(source, path, records)
        header = ('% Generated TeX body; no PDF or document-style claim.\n' +
                  '% Maintained source: ' + name + '\n' +
                  '% Recovered-source SHA-256: ' + source_hash + '\n' +
                  '% Rebuild: python3 tools/build_manuscripts.py\n' +
                  '% Common packages: amsmath, amssymb, hyperref, longtable, booktabs, array.\n' +
                  '% Final document preamble must use the recovered original Subset Sum style.\n\n')
        target.write_text(header + body, encoding='utf-8')
        entries.append({'source': name, 'target': target.relative_to(ROOT).as_posix(),
                        'source_sha256': source_hash, 'tex_sha256': digest(target.read_bytes()),
                        'math_nodes': len(records), 'pdf': 'source-only'})
    if args.check:
        if old.get('generator_sha256') != generator or set(old_entries) != set(SOURCES):
            failures.append('export generator or source list')
        if failures:
            print('Stale TeX exports: ' + ', '.join(failures), file=sys.stderr)
            return 1
    else:
        MANIFEST.write_text(json.dumps({'schema_version': 1, 'pandoc_version': version,
                                       'generator_sha256': generator, 'exports': entries},
                                      indent=2, ensure_ascii=False) + '\n')
    print(f'TeX source exports {"checked" if args.check else "built"}: {len(SOURCES)}; no PDFs generated')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
