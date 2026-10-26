"""Build or check the two native-TeX ROABP papers in the repository style.

The ordinary --check mode is Python-only. Authoring builds use XeLaTeX
without shell escape and require a separate visual review of every page.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]
FAMILY = 'problems/roabp-affine-pit'
RECEIPT = ROOT / FAMILY / 'verify/native-paper-builds.json'
SOURCE_DATE_EPOCH = 1792972800
PACKAGES = {
    'core': ('manuscripts/general-affine.tex', 'paper.pdf',
             'Complete all-rank fixed-width affine-orbit PIT proof in every characteristic.'),
    'directions': ('manuscripts/direction-grids.tex', 'direction-grids.pdf',
                   'Complete finite direction-grid refinement, using the companion core theorem.'),
}


def sha(body):
    return hashlib.sha256(body).hexdigest()


def bindings(source):
    names = ['manuscripts/paper-style.tex', FAMILY + '/' + source,
             FAMILY + '/verify/build_native_papers.py']
    return {name: sha((ROOT / name).read_bytes()) for name in names}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--paper', choices=tuple(PACKAGES), action='append')
    args = parser.parse_args()
    selected = args.paper or list(PACKAGES)
    receipt = json.loads(RECEIPT.read_text()) if RECEIPT.exists() else {'schema_version': 1, 'papers': {}}
    for key in selected:
        source, output, scope = PACKAGES[key]
        expected = bindings(source)
        target = ROOT / FAMILY / output
        if args.check:
            saved = receipt['papers'].get(key, {})
            assert saved.get('inputs') == expected, (key, 'stale source binding')
            assert target.is_file() and sha(target.read_bytes()) == saved.get('pdf_sha256'), (key, 'artifact')
            assert saved.get('visual_review') == 'passed', (key, 'visual review pending')
            assert not saved.get('layout_warnings'), (key, 'layout warning')
            assert saved.get('pages', 0) > 0, (key, 'missing page count')
            assert saved.get('visual_review_details'), (key, 'missing review scope')
            continue
        file_id = sha(json.dumps(expected, sort_keys=True).encode())[:32]
        trailer = r'\AtBeginDocument{\special{pdf:trailerid [<' + file_id + '><' + file_id + '>]}}'
        with tempfile.TemporaryDirectory(prefix='af-roabp-paper-') as directory:
            temp = Path(directory)
            command = ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
                       '-no-shell-escape', '-jobname=' + key,
                       '-output-directory=' + str(temp),
                       trailer + r'\input{' + FAMILY + '/' + source + '}']
            environment = dict(os.environ, SOURCE_DATE_EPOCH=str(SOURCE_DATE_EPOCH),
                               FORCE_SOURCE_DATE='1', TZ='UTC')
            for _ in range(3):
                result = subprocess.run(command, cwd=ROOT, env=environment,
                                        text=True, capture_output=True)
                if result.returncode:
                    log = ROOT.parent / ('roabp-' + key + '-typeset-error.log')
                    log.write_text(result.stdout + result.stderr)
                    raise RuntimeError(f'{key}: typesetting failed; see {log}')
            log_text = (temp / (key + '.log')).read_text(errors='replace')
            warnings = [line for line in log_text.splitlines()
                        if re.search(r'Overfull|Underfull|Missing character:|undefined references|multiply defined', line)]
            (ROOT.parent / ('roabp-' + key + '-typeset.log')).write_text(log_text)
            body = (temp / (key + '.pdf')).read_bytes()
            assert body.rstrip().endswith(b'%%EOF'), key
            # This dependency is needed only while authoring, never in CI.
            import io
            from pypdf import PdfReader
            reader = PdfReader(io.BytesIO(body))
            assert all('??' not in page.extract_text() for page in reader.pages)
            part = target.with_suffix('.pdf.part')
            part.write_bytes(body)
            part.replace(target)
            receipt['papers'][key] = {
                'scope': scope, 'inputs': expected, 'output': FAMILY + '/' + output,
                'pdf_sha256': sha(body), 'pages': len(reader.pages),
                'engine': 'xelatex', 'source_date_epoch': SOURCE_DATE_EPOCH,
                'layout_warnings': warnings, 'visual_review': 'pending',
            }
            print(f'Built {key}: {len(reader.pages)} pages; {len(warnings)} layout warnings; visual review pending.')
    if args.check:
        print(f'ROABP native paper bindings and visual-review receipts checked: {len(selected)}.')
    else:
        RECEIPT.write_text(json.dumps(receipt, indent=2) + '\n')


if __name__ == '__main__':
    main()
