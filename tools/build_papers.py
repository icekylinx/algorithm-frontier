#!/usr/bin/env python3
"""Typeset only explicitly selected complete proof packages in the original style.

The configured papers use the hash-matched original Subset Sum typography.
All other manuscripts remain source-only. A build checks exact mathematical
AST preservation, uses a temporary directory and disables shell escape.
Publication additionally requires visual page review; see docs/MANUSCRIPTS.md.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from build_manuscripts import export
from math_presentation import ROOT, transform

CONFIG = ROOT / 'manuscripts' / 'papers.json'
RECEIPT = ROOT / 'manuscripts' / 'paper-builds.json'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--paper', action='append', help='configured paper ID; default all')
    parser.add_argument('--check', action='store_true', help='Python-only saved-build binding check')
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text())
    selected = set(args.paper or [item['id'] for item in config['papers']])
    known = {item['id'] for item in config['papers']}
    if not selected <= known:
        parser.error('unknown paper ID')
    old = json.loads(RECEIPT.read_text()) if RECEIPT.exists() else {'schema_version': 1, 'papers': {}}
    failures = []
    for item in config['papers']:
        if item['id'] not in selected:
            continue
        inputs = [CONFIG.relative_to(ROOT).as_posix(), config['style'], item['wrapper'],
                  'tools/build_manuscripts.py', 'tools/build_papers.py', 'tools/math_presentation.py',
                  *item['sources']]
        binding = {name: sha(ROOT / name) for name in inputs}
        target = ROOT / item['output']
        if args.check:
            saved = old['papers'].get(item['id'], {})
            if (saved.get('inputs') != binding or not target.exists() or
                    saved.get('pdf_sha256') != sha(target) or
                    saved.get('visual_review') != 'passed' or
                    saved.get('layout_warnings')):
                failures.append(item['id'])
            continue
        with tempfile.TemporaryDirectory(prefix='af-paper-') as directory:
            temp = Path(directory)
            for name in item['sources']:
                path = ROOT / name
                records = []
                source = transform(path.read_text(), path, source=True, records=records)
                (temp / path.with_suffix('.tex').name).write_text(export(
                    source, path, records, paper=True,
                    preserve_section_labels=item.get('heading_numbers') == 'source'))
            command = [config['engine'], '-interaction=nonstopmode', '-halt-on-error',
                       '-no-shell-escape', '-jobname=' + item['id'],
                       '-output-directory=' + str(temp),
                       r'\def\AFGeneratedPath{' + str(temp) + r'}\input{' + item['wrapper'] + '}']
            for _ in range(3):
                environment = dict(os.environ, SOURCE_DATE_EPOCH=str(config['source_date_epoch']),
                                   FORCE_SOURCE_DATE='1', TZ='UTC')
                run = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                                     env=environment)
                if run.returncode:
                    log = ROOT.parent / (item['id'] + '-typeset-error.log')
                    log.write_text(run.stdout + run.stderr)
                    raise RuntimeError(f'{item["id"]}: typesetting failed; {log}')
            logtext = (temp / (item['id'] + '.log')).read_text(errors='replace')
            warnings = [line for line in logtext.splitlines()
                        if any(token in line for token in ('Overfull', 'Missing character:', 'undefined references', 'multiply defined'))]
            source_pdf = temp / (item['id'] + '.pdf')
            shutil.copy2(source_pdf, target)
            log = ROOT.parent / (item['id'] + '-typeset.log')
            log.write_text(logtext)
            old['papers'][item['id']] = {'scope': item['scope'], 'output': item['output'],
                                       'inputs': binding, 'pdf_sha256': sha(target),
                                       'engine': config['engine'],
                                       'source_date_epoch': config['source_date_epoch'],
                                       'layout_warnings': warnings,
                                       'visual_review': 'pending'}
            print(f'Built {item["id"]}: {target.stat().st_size} bytes; {len(warnings)} layout warnings; visual review pending')
    if failures:
        raise SystemExit('Stale paper builds: ' + ', '.join(failures))
    if not args.check:
        RECEIPT.write_text(json.dumps(old, indent=2, ensure_ascii=False) + '\n')
    else:
        print(f'Paper source bindings checked: {len(selected)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
