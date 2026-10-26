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


def without_file_identifiers(pdf: bytes) -> bytes | None:
    """Compare all PDF bytes except the two nonvisual trailer identifiers.

    Accept only the exact cross-reference-stream form emitted by our engine;
    an unexpected or duplicated field requires a fresh visual review.
    """
    pattern = rb'(/Type/XRef/ID\[)<[0-9a-f]{32}><[0-9a-f]{32}>(\])'
    normalized, count = re.subn(pattern, rb'\1<' + b'0' * 32 + rb'><' + b'0' * 32 + rb'>\2', pdf)
    return normalized if count == 1 else None


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
        previous = old['papers'].get(item['id'], {})
        if args.check:
            saved = old['papers'].get(item['id'], {})
            if (saved.get('inputs') != binding or not target.exists() or
                    saved.get('pdf_sha256') != sha(target) or
                    saved.get('visual_review') != 'passed' or
                    saved.get('layout_warnings')):
                failures.append(item['id'])
            continue
        previous_pdf = target.read_bytes() if target.exists() else None
        previous_binding_valid = (previous_pdf is not None and
                                  previous.get('pdf_sha256') == hashlib.sha256(previous_pdf).hexdigest())
        with tempfile.TemporaryDirectory(prefix='af-paper-') as directory:
            temp = Path(directory)
            for name in item['sources']:
                path = ROOT / name
                records = []
                source = transform(path.read_text(), path, source=True, records=records)
                (temp / path.with_suffix('.tex').name).write_text(export(
                    source, path, records, paper=True,
                    preserve_section_labels=item.get('heading_numbers') == 'source'))
            # The documented dvipdfmx first-page special fixes the two file IDs.
            # See https://tug.org/dvipdfmx/doc/dvipdfmx/dvipdfmx.pdf, "Custom File Identifiers".
            file_id = hashlib.sha256(json.dumps(binding, sort_keys=True).encode()).hexdigest()[:32]
            trailer = (r'\AtBeginDocument{\special{pdf:trailerid [<' + file_id
                       + '><' + file_id + '>]}}')
            command = [config['engine'], '-interaction=nonstopmode', '-halt-on-error',
                       '-no-shell-escape', '-jobname=' + item['id'],
                       '-output-directory=' + str(temp),
                       r'\def\AFGeneratedPath{' + str(temp) + '}' + trailer
                       + r'\input{' + item['wrapper'] + '}']
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
            pdf_digest = sha(target)
            exact_bytes = previous.get('pdf_sha256') == pdf_digest
            prior_content = without_file_identifiers(previous_pdf) if previous_binding_valid else None
            current_content = without_file_identifiers(target.read_bytes())
            identifiers_only = prior_content is not None and prior_content == current_content
            same_reviewed_pdf = (previous_binding_valid and (exact_bytes or identifiers_only)
                                 and previous.get('visual_review') == 'passed' and not warnings)
            old['papers'][item['id']] = {'scope': item['scope'], 'output': item['output'],
                                       'inputs': binding, 'pdf_sha256': sha(target),
                                       'engine': config['engine'],
                                       'source_date_epoch': config['source_date_epoch'],
                                       'layout_warnings': warnings,
                                       'visual_review': 'passed' if same_reviewed_pdf else 'pending'}
            if same_reviewed_pdf:
                old['papers'][item['id']]['visual_review_details'] = previous.get('visual_review_details', {})
                old['papers'][item['id']]['visual_review_basis'] = (
                    'PDF bytes are identical to the previously visually reviewed artifact.' if exact_bytes else
                    'Only the two 16-byte PDF trailer file identifiers changed; every other byte is identical to the previously visually reviewed artifact.')
                old['papers'][item['id']]['previous_reviewed_pdf_sha256'] = previous['pdf_sha256']
            status = 'retained by exact PDF comparison' if same_reviewed_pdf else 'pending'
            print(f'Built {item["id"]}: {target.stat().st_size} bytes; {len(warnings)} layout warnings; visual review {status}')
    if failures:
        raise SystemExit('Stale paper builds: ' + ', '.join(failures))
    if not args.check:
        RECEIPT.write_text(json.dumps(old, indent=2, ensure_ascii=False) + '\n')
    else:
        print(f'Paper source bindings checked: {len(selected)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
