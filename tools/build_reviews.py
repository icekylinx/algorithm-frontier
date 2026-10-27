#!/usr/bin/env python3
"""Publish scoped review readiness from the evidence registry.

Readiness is a human-readable review invitation, not a proof certificate.
Records without an explicit review entry remain pending.
"""
from __future__ import annotations

import argparse
import json
from os.path import relpath
from pathlib import Path
import re
import sys
from normalize_math import normalize_markdown
from math_presentation import present_markdown

ROOT = Path(__file__).resolve().parents[1]


def status_paragraph(record: dict, evidence_link: str = 'verify/README.md') -> str:
    review = record['review']
    label = {'ready': 'Ready for review', 'partial': 'Ready for review in the stated scope',
             'pending': 'Review pending'}[review['status']]
    parts = [f"**{label}.** {review['scope']}"]
    if review.get('conditions'):
        parts.append('**Dependencies and scope.** ' + ' '.join(review['conditions']))
    parts.append(f'The [verification note]({evidence_link}) identifies executable coverage. '
                 'This status does not claim external peer review or proof-assistant verification.')
    return normalize_markdown('\n\n'.join(parts))


def render_registry(data: dict, catalogue: dict) -> str:
    titles = {r['id']: r['title'] for g in catalogue['groups'] for r in g['records']}
    titles.update({r['id']: r['title'] for r in catalogue.get('supporting_results', [])})
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
        'the two-level and third-lookup receipts\' source/menu bindings, checks '
        'both scalar ledgers and the recovery paths, and freshly replays '
        'the `rho=1.7` and direct two-level branches. To cleanly replay all '
        '62 two-level and 16 third-lookup branches:', '',
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
                out += ['**Dependencies and scope.** ' + ' '.join(review['conditions']), '']
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
    supporting = data.get('supporting_records', [])
    out += ['', '## Supporting manuscripts', '',
            'These independent results have their own review scopes. A completed '
            'static theorem does not certify a separate dynamic application.', '']
    for record in supporting:
        review = record.get('review')
        if review is None or review['status'] == 'pending':
            continue
        label = 'Ready for review' if review['status'] == 'ready' else 'Components ready for review'
        out += [f"### [{titles[record['id']]}](../{record['path']})", '',
                f"**{label}.** {review['scope']}", '']
        if review.get('conditions'):
            out += ['**Dependencies and scope.** ' + ' '.join(review['conditions']), '']
        out += [f"[Manuscript](../{record['path']}) · "
                f"[Evidence](../{record['evidence_note']}) · Reviewed {review['date']}", '']
    pending_support = [r for r in supporting if r.get('review', {}).get('status', 'pending') == 'pending']
    if pending_support:
        out += ['### Supporting review pending', '']
        out += [f"- [{titles[r['id']]}](../{r['path']})" for r in pending_support]
    out += ['', '## Executable evidence', '',
            'Each linked program documents its checked identities or finite domain. '
            'The per-result evidence notes and registry distinguish direct evidence '
            'from a shared prerequisite; a passing finite check does not establish '
            'an arbitrary-input asymptotic theorem.', '']
    programs = sorted({check['path'] for record in data['records'] + supporting for check in record.get('checks', [])})
    for program in programs:
        out.append(f'- [{program}](../{program})')
    out += ['', '## Maintaining a status', '',
            'Set a readiness scope only after checking the corresponding proof, '
            'algorithm, representation, randomness and source requirements. Name '
            'proved local realizations, external theorems and genuinely unresolved '
            'assumptions separately. Executable coverage is a distinct field of '
            'evidence. Update `registry.json`, '
            'then run `python3 tools/build_reviews.py`; this synchronizes these '
            'entries with the reviewed problem cards and supporting manuscripts. A changed theorem or '
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
    for record in data.get('supporting_records', []):
        if 'review' not in record:
            continue
        name = record['path']
        path = ROOT / name
        before = path.read_text()
        evidence_link = relpath(ROOT / record['evidence_note'], path.parent)
        block = ('<!-- review-status:start -->\n' + status_paragraph(record, evidence_link)
                 + '\n<!-- review-status:end -->')
        pattern = r'(?ms)^<!-- review-status:start -->\n.*?^<!-- review-status:end -->'
        if '<!-- review-status:start -->' in before:
            after, replacements = re.subn(pattern, lambda _: block, before)
            if replacements != 1:
                raise ValueError(f'{name}: expected one supporting review block')
        else:
            heading, separator, rest = before.partition('\n')
            if not separator or not heading.startswith('# '):
                raise ValueError(f'{name}: missing manuscript heading')
            after = heading + '\n\n' + block + '\n' + rest
        outputs[name] = after
    stale = []
    for name, content in outputs.items():
        path = ROOT / name
        content = present_markdown(content, path)
        if args.check:
            if not path.is_file() or path.read_text() != content:
                stale.append(name)
        else:
            path.write_text(content)
    if stale:
        print('stale review surfaces: ' + ', '.join(stale), file=sys.stderr)
        return 1
    count = sum('review' in r for r in data['records'] + data.get('supporting_records', []))
    print(f'Review surfaces {"checked" if args.check else "built"}: {count} scoped records')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
