#!/usr/bin/env python3
"""Check source identities, canonical targets and optional local ZIP replay.

Attribution: Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
Source hashes identify imported bytes, not immutable current mathematical text.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import zipfile

ROOT=Path(__file__).resolve().parents[3]
manifest=json.loads((ROOT/'provenance/imports/integer-factorization.json').read_text())
assert manifest['schema_version']==1
archives={r['filename']:r for r in manifest['archives']}
assert len(archives)==2 and len(manifest['members'])==31
seen=set();targets=set();replayed=0
for row in manifest['members']:
    key=row['archive'],row['member']
    assert key not in seen;seen.add(key)
    assert row['archive'] in archives and re.fullmatch('[0-9a-f]{64}',row['sha256'])
    member=PurePosixPath(row['member'])
    assert not member.is_absolute() and '..' not in member.parts
    if row.get('disposition')=='excluded-route':
        assert row['canonical_target'] is None
        continue
    assert row.get('disposition')=='integrated'
    target=PurePosixPath(row['canonical_target'])
    assert not target.is_absolute() and '..' not in target.parts
    path=ROOT/target
    assert path.is_file(),path
    text=path.read_text()
    assert row['sha256'] in text,(row['member'],'source identity omitted')
    assert not re.search('[\u4e00-\u9fff]',text),(path,'non-English result')
    assert 'Yilin Liu' in text and 'GPT-6 Astra Pro' in text
    targets.add(row['canonical_target'])
assert len(targets)==18
assert sum(r['disposition']=='excluded-route' for r in manifest['members'])==12
assert manifest['counts']=={'source_archives':2,'source_members':31,'retained_members':19,'excluded_members':12,'canonical_targets':18}
for name,row in archives.items():
    path=ROOT/name
    if not path.exists():continue  # Binary source archives are not shipped in CI.
    data=path.read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
    expected={r['member']:r for r in manifest['members'] if r['archive']==name}
    with zipfile.ZipFile(path) as z:
        assert set(z.namelist())==set(expected)
        for member,original in expected.items():
            payload=z.read(member)
            assert len(payload)==original['bytes']
            assert hashlib.sha256(payload).hexdigest()==original['sha256']
            replayed+=1
print('PASS factoring import:',len(archives),'archives,',len(seen),'members,',len(targets),'retained canonical targets; 12 excluded members;',replayed,'local original members replayed; no mathematical validation')
