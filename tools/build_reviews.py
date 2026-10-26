#!/usr/bin/env python3
"""Publish scoped review readiness from the evidence registry.

Readiness is a human-readable review invitation, not a proof certificate.
Records without an explicit review entry remain pending.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from normalize_math import normalize_markdown

ROOT = Path(__file__).resolve().parents[1]


def status_paragraph(record: dict) -> str:
    review = record['review']
    label = {'ready': 'Ready for review', 'partial': 'Ready for review in the stated scope',
             'pending': 'Review pending'}[review['status']]
    parts = [f"**{label}.** {review['scope']}"]
    if review.get('conditions'):
        parts.append('**Conditions and remaining work.** ' + ' '.join(review['conditions']))
    parts.append('The [verification note](verify/README.md) identifies executable coverage. '
                 'This status does not claim external peer review or proof-assistant verification.')
    return normalize_markdown('\n\n'.join(parts))


def render_registry(data: dict, catalogue: dict) -> str:
    titles = {r['id']: r['title'] for g in catalogue['groups'] for r in g['records']}
    out = [
        '# Review status and verification evidence', '',
        'Readiness applies to the precise scope below. **Ready for review** means '
        'that the stated manuscript package has been checked for its theorem, '
        'proof, computational model and declared dependencies. **Partial readiness** '
        'identifies completed components of a larger family. Other manuscripts '
        'remain available with review pending. None of these labels claims '
        'external peer review or proof-assistant verification.', '',
        'The machine-readable [registry](registry.json) is the source of these '
        'statuses and of each executable check\'s mathematical scope.', '',
        '## Run the checks', '',
        '```sh', 'python3 tools/check_repository.py', '```', '',
        'The default suite checks repository structure and every registered '
        'executable used by the canonical runner. For Subset Sum it validates '
        'the saved full-contact receipt\'s source/menu binding and freshly replays '
        'the rho=1.7 and direct branches. To replay all 44 contact branches:', '',
        '```sh', 'python3 tools/check_repository.py --full-contacts --jobs 4', '```', '',
        'Receipt binding establishes provenance and coverage metadata; only '
        'recomputation re-establishes the inequalities. The full mode is also '
        'available through manual dispatch of the repository workflow. The '
        '[contact evidence note](../problems/subset-sum-fast-deterministic/verify/README.md) '
        'states the analytic coverage argument.', '',
    ]
    for status, heading in [('ready', 'Ready for review'), ('partial', 'Components ready for review')]:
        out += ['## ' + heading, '']
        records = [r for r in data['records'] if r.get('review', {}).get('status') == status]
        if not records:
            out += ['No package has this status yet.', '']
        for record in records:
            review = record['review']
            out += [f"### [{titles[record['id']]}](../{record['path']}/)", '',
                    review['scope'], '']
            if review.get('conditions'):
                out += ['**Conditions and remaining work.** ' + ' '.join(review['conditions']), '']
            out += [f"[Proof](../{record['path']}/proof.md) · "
                    f"[Dependencies](../{record['path']}/sources.md) · "
                    f"[Evidence](../{record['evidence_note']}) · "
                    f"Reviewed {review['date']}", '']
    out += ['## Review pending', '',
            'These families have not yet received a scoped readiness entry in '
            'this registry. Their existing statements retain their own assumptions.', '']
    for record in data['records']:
        if record.get('review', {}).get('status', 'pending') == 'pending':
            out.append(f"- [{titles[record['id']]}](../{record['path']}/)")
    out += ['', '## Executable evidence', '',
            'Each linked program documents its checked identities or finite domain. '
            'The per-result evidence notes and registry distinguish direct evidence '
            'from a shared prerequisite; a passing finite check does not establish '
            'an arbitrary-input asymptotic theorem.', '']
    programs = sorted({check['path'] for record in data['records'] for check in record.get('checks', [])})
    for program in programs:
        out.append(f'- [{program}](../{program})')
    out += ['', '## Maintaining a status', '',
            'Set a readiness scope only after checking the corresponding proof, '
            'algorithm, representation, randomness and source requirements. Name '
            'unresolved backend contracts beside the scope. Update `registry.json`, '
            'then run `python3 tools/build_reviews.py`; this synchronizes these '
            'entries with the reviewed problem cards. A changed theorem or '
            'dependency requires a new scope assessment.', '',
            'See [Contributing](../CONTRIBUTING.md) for the manuscript workflow and '
            '[provenance](../provenance/README.md) for imported source identities.', '']
    return normalize_markdown('\n'.join(out))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'reviews/registry.json').read_text())
    catalogue = json.loads((ROOT / 'catalogue.json').read_text())
    outputs = {'reviews/README.md': render_registry(data, catalogue)}
    for record in data['records']:
        if 'review' not in record:
            continue
        name = record['path'] + '/README.md'
        before = (ROOT / name).read_text()
        pattern = r'(?ms)^\*\*Review status\*\*\n\n.*?(?=^\*\*Source\*\*$)'
        after, replacements = re.subn(pattern, lambda _: '**Review status**\n\n' + status_paragraph(record) + '\n\n', before)
        if replacements != 1:
            raise ValueError(f'{name}: expected exactly one review-status field')
        outputs[name] = after
    stale = []
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_text() != content:
                stale.append(name)
        else:
            path.write_text(content)
    if stale:
        print('stale review surfaces: ' + ', '.join(stale), file=sys.stderr)
        return 1
    count = sum('review' in r for r in data['records'])
    print(f'Review surfaces {"checked" if args.check else "built"}: {count} scoped records')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
