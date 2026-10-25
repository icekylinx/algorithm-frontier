#!/usr/bin/env python3
"""Check authored Markdown for balanced $$ display delimiters."""
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
paths = [root / 'README.md', root / 'OVERVIEW.md', root / 'FORMATTING.md']
paths += list((root / 'problems').rglob('README.md'))
paths += list((root / 'problems').rglob('proof.md'))
paths += list((root / 'problems').rglob('NOTICE.md'))
paths += list((root / 'problems').rglob('sources.md'))
paths += list((root / 'problems').rglob('verify/*.md'))
errors=[]
for p in paths:
    text=p.read_text(errors='replace')
    if text.count('$$') % 2:
        errors.append(f'{p}: unmatched $$ delimiter')
    if '\\operatorname' in text:
        errors.append(f'{p}: unsupported \\operatorname macro; use \\mathrm instead')
    if '\\(' in text or '\\)' in text or '\\[' in text or '\\]' in text:
        errors.append(f'{p}: inline or bracket TeX delimiters are not allowed; use $$ ... $$')
if errors:
    print('LATEX DELIMITER CHECK FAILED')
    print('\n'.join(errors)); sys.exit(1)
print(f'LATEX DELIMITER CHECK OK: {len(paths)} authored files')
