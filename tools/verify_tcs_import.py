#!/usr/bin/env python3
"""Verify the selective November TCS import, never a mathematical certificate.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
Original archive replay is optional; publishing original archives is forbidden.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'provenance/imports/tcs-research-20261102.json'


def safe(name):
    path = PurePosixPath(name)
    assert str(path) == name and not path.is_absolute() and '..' not in path.parts
    return path


def digest(body):
    return hashlib.sha256(body).hexdigest()


def main():
    data = json.loads(MANIFEST.read_text())
    assert data['schema_version'] == 1
    selected = {'triangular-low-rank-counting', 'sparse-low-rank-counting',
                'subset-sum-exact-counting'}
    support = {'partial-transpose-circuits'}
    assert set(data['selected_results']) == selected
    assert set(data['supporting_results']) == support
    assert data['attribution'] == ['icekylinx', 'GPT-6 Astra Pro']
    members = {row['member']: row for row in data['members']}
    assert len(members) == len(data['members']) == 161
    mapped = {}
    targets = set()
    for row in data['transformations']:
        assert row['source_sha256'] == members[row['source_member']]['sha256']
        target = safe(row['target'])
        assert target.parts[:2] in {
            *{('problems', name) for name in selected},
            ('manuscripts', 'partial-transpose-circuits')}, target
        assert (ROOT / target).is_file(), target
        assert row['transformation'].strip()
        mapped.setdefault(row['source_member'], set()).add(str(target))
        targets.add(str(target))
    for name, row in members.items():
        assert safe(name).parts[0] == 'tcs_research_checkpoint'
        assert isinstance(row['bytes'], int) and row['bytes'] >= 0
        assert re.fullmatch('[0-9a-f]{64}', row['sha256'])
        assert set(row['canonical_targets']) == mapped.get(name, set())
        assert row['reason'].strip()
        if row['canonical_targets']:
            assert row['disposition'] == 'integrated'
        else:
            assert row['disposition'].startswith('excluded-')
    assert data['counts'] == dict(
        source_members=161, source_bytes=sum(x['bytes'] for x in members.values()),
        integrated_members=len(mapped), excluded_members=161-len(mapped),
        canonical_targets=len(targets))
    assert len(mapped) == 25 and len(targets) == 26
    assert (ROOT / safe(data['summary'])).is_file()
    catalogue = json.loads((ROOT / 'catalogue.json').read_text())
    main_ids = {r['id'] for g in catalogue['groups'] for r in g['records']}
    support_ids = {r['id'] for r in catalogue['supporting_results']}
    assert selected <= main_ids and support <= support_ids
    assert not (support & main_ids)
    for identifier in selected:
        for name in ('README.md', 'proof.md', 'sources.md', 'verify/README.md'):
            text = (ROOT / 'problems' / identifier / name).read_text()
            assert 'icekylinx' in text and 'GPT-6 Astra Pro' in text
            assert not re.search('[\u4e00-\u9fff]', text), (identifier, name)
    # Check the publication boundary against tracked files, not ignored inputs.
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    forbidden = ('.zip', '.tar', '.tar.gz', '.tgz', '.7z', '.rar')
    assert not [n for n in tracked if n.lower().endswith(forbidden)], 'original archive tracked'
    assert not [n for n in tracked if n.startswith('.local/')], 'local input tracked'
    assert not (ROOT / 'tcs_research_checkpoint').exists(), 'duplicate extracted source tree'
    assert not (ROOT / 'verification/fock/fock_audit_source').exists(), 'duplicate primitive snapshot'
    assert len(data['external_primary_sources']) == 6
    for row in data['external_primary_sources']:
        assert re.fullmatch('[0-9a-f]{64}', row['sha256']) and row['bytes'] > 0
        assert '4eaee87548250b2682affda7d05d947c05554bae' in row['url']
    archive = data['archive']
    path = ROOT / safe(archive['local_directory']) / safe(archive['filename'])
    if not path.exists():
        path = ROOT / safe(archive['filename'])  # Earlier input location.
    replayed = 0
    if path.exists():
        payload = path.read_bytes()
        assert len(payload) == archive['bytes'] and digest(payload) == archive['sha256']
        with zipfile.ZipFile(path) as source:
            files = [x for x in source.infolist() if not x.is_dir()]
            assert len(files) == len(members)
            assert {x.filename for x in files} == set(members)
            for info in files:
                raw = source.read(info)
                assert len(raw) == members[info.filename]['bytes']
                assert digest(raw) == members[info.filename]['sha256']
                replayed += 1
            supplied = json.loads(source.read('tcs_research_checkpoint/MANIFEST.json'))['files']
            assert {x['path'] for x in supplied} == {
                n.removeprefix('tcs_research_checkpoint/') for n in members
                if n != 'tcs_research_checkpoint/MANIFEST.json'}
            for row in supplied:
                saved = members['tcs_research_checkpoint/' + row['path']]
                assert all(row[k] == saved[k] for k in ('bytes', 'sha256'))
    print(f'PASS TCS import: {len(members)} members, {len(mapped)} selected sources, '
          f'{len(targets)} adapted targets; {replayed} original members replayed; '
          'no original archives tracked; provenance only')


if __name__ == '__main__':
    main()
