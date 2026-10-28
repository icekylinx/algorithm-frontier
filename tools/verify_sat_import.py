#!/usr/bin/env python3
"""Check selective SAT source identities and optional original ZIP replay.

Attribution: icekylinx and GPT-6 Astra Pro. Apache-2.0.
This checks provenance and publication scope, not mathematical correctness.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def safe_path(name):
    path = PurePosixPath(name)
    assert not path.is_absolute() and '..' not in path.parts and str(path) == name
    return path


def main():
    record = json.loads((ROOT / 'provenance/imports/sat-research.json').read_text())
    assert record['schema_version'] == 1
    selected = {'noncommutative-crossing', 'ordered-subset-contraction'}
    assert set(record['selected_results']) == selected
    members = {item['member']: item for item in record['members']}
    assert len(members) == len(record['members']) == 1069
    mappings = {}
    targets = set()
    for item in record['transformations']:
        source = members[item['source']]
        assert source['sha256'] == item['source_sha256']
        target = safe_path(item['target'])
        assert len(target.parts) >= 3 and target.parts[0] == 'problems'
        assert target.parts[1] in selected and (ROOT / target).is_file()
        assert item['transform'].strip()
        mappings.setdefault(item['source'], set()).add(str(target))
        targets.add(str(target))
    for name, item in members.items():
        safe_path(name)
        assert re.fullmatch('[0-9a-f]{64}', item['sha256'])
        assert isinstance(item['bytes'], int) and item['bytes'] >= 0
        assert set(item['canonical_targets']) == mappings.get(name, set())
        if item['canonical_targets']:
            assert item['disposition'] == 'integrated'
        else:
            assert item['disposition'].startswith('excluded-')
        assert item['reason'].strip()
    assert record['counts'] == dict(
        source_members=1069, source_bytes=sum(x['bytes'] for x in members.values()),
        integrated_members=len(mappings), excluded_members=1069-len(mappings),
        canonical_targets=len(targets))
    assert len(mappings) == 22 and len(targets) == 20
    assert (ROOT / safe_path(record['summary'])).is_file()
    catalogue = json.loads((ROOT / 'catalogue.json').read_text())
    main_ids = {x['id'] for g in catalogue['groups'] for x in g['records']}
    support_ids = {x['id'] for x in catalogue['supporting_results']}
    assert selected <= main_ids
    assert not ({'sat-counting', 'modular-permanent'} & main_ids)
    for item in record['repository_cleanup']:
        path = ROOT / safe_path(item['path'])
        if item['action'] == 'internal-proof-dependency-only':
            assert path.is_file() and item['id'] not in support_ids
        else:
            assert item['action'] == 'removed-obsolete-candidate' and not path.exists()
            assert (ROOT / safe_path(item['retained_target'])).is_file()
    replayed = 0
    archive = record['archive']
    path = ROOT / safe_path(archive['filename'])
    if path.exists():
        payload = path.read_bytes()
        assert len(payload) == archive['bytes']
        assert hashlib.sha256(payload).hexdigest() == archive['sha256']
        with zipfile.ZipFile(path) as source:
            assert len(source.namelist()) == len(members)
            assert set(source.namelist()) == set(members)
            for name, item in members.items():
                original = source.read(name)
                assert len(original) == item['bytes']
                assert hashlib.sha256(original).hexdigest() == item['sha256']
                replayed += 1
            supplied = json.loads(source.read('MANIFEST.json'))['files']
            assert {x['path'] for x in supplied} == set(members) - {'MANIFEST.json'}
            for item in supplied:
                assert all(item[k] == members[item['path']][k] for k in ('bytes', 'sha256'))
    print(f'PASS SAT import: {len(members)} original members, {len(mappings)} selected, '
          f'{len(targets)} adapted targets, {replayed} local original members replayed; '
          'provenance only, no mathematical certification')


if __name__ == '__main__':
    main()
