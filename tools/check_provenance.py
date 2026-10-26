#!/usr/bin/env python3
"""Check that every mapped retained import has an existing canonical target.

Archive hashes identify imported bytes. They intentionally do not freeze
current mathematical manuscripts after authorized editing.
"""
from pathlib import Path, PurePosixPath
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]

def check_recovery(errors):
    """Validate metadata bindings; original ZIP bytes are not shipped in CI."""
    data=json.loads((ROOT/'provenance/checkpoint-recovery.json').read_text())
    originals=json.loads((ROOT/'provenance/archive-manifest.json').read_text())['archives']
    known={row['sha256'] for row in originals}
    known.add(json.loads((ROOT/'provenance/imports/checkpoint-x.json').read_text())['source_archive']['sha256'])
    archives=data['archives']; ids={row['id'] for row in archives}
    if len(ids)!=len(archives):errors.append('duplicate recovery archive identifier')
    if {row['sha256'] for row in archives}!=known:
        errors.append('recovery archive hashes disagree with original manifests')
    notes=data['notes']; names={row['name'] for row in notes}; contents=set()
    if len(names)!=len(notes):errors.append('duplicate recovered source basename')
    for row in notes:
        for field in ('canonical_targets','related_targets'):
            for target in row.get(field,[]):
                if not (ROOT/target.split('#',1)[0]).is_file():
                    errors.append(f"missing recovery {field}: {row['name']} -> {target}")
        for version in row['original_versions']:
            digest=version['sha256'];contents.add(digest)
            if not re.fullmatch('[0-9a-f]{64}',digest) or version['bytes']<0:
                errors.append(f"invalid original source identity: {row['name']}")
            if not version['locations']:errors.append(f"unlocated original source: {row['name']}")
            for location in version['locations']:
                path=PurePosixPath(location['path'])
                if location['archive'] not in ids or path.is_absolute() or '..' in path.parts or path.name!=row['name']:
                    errors.append(f"invalid archive member: {row['name']}")
        if row.get('disposition')=='restored-complete-proof':
            restoration=row.get('restoration',{})
            target=restoration.get('target')
            digest=restoration.get('source_sha256')
            if (target not in row.get('canonical_targets',[]) or
                    digest not in {v['sha256'] for v in row['original_versions']} or
                    not restoration.get('date') or not restoration.get('scope')):
                errors.append(f"incomplete proof restoration binding: {row['name']}")
            elif not (ROOT/target).is_file() or digest not in (ROOT/target).read_text():
                errors.append(f"restored manuscript omits original source identity: {row['name']}")
    counts={'archives':len(archives),'extracted_files':sum(row['extracted_files'] for row in archives),
            'markdown_basenames':len(names),'distinct_markdown_contents':len(contents)}
    if counts!=data['counts']:errors.append('checkpoint recovery counts disagree with inventory')
    print(f"Checkpoint recovery metadata: {len(archives)} archives, {len(names)} source basenames; original ZIP replay is separate")

def main():
    data=json.loads((ROOT/"provenance/canonical-map.json").read_text())
    records=data["records"]
    errors=[];seen=set()
    for r in records:
        old=r["original_path"]
        if old in seen:errors.append(f"duplicate original path: {old}")
        seen.add(old)
        if r["disposition"] not in {"integrated","moved","removed"}:errors.append(f"invalid disposition: {old}")
        target=r.get("canonical_path")
        if r["disposition"]!="removed" and not target:errors.append(f"retained source has no target: {old}")
        if target and not (ROOT/target.split("#",1)[0]).exists():errors.append(f"missing target: {old} -> {target}")
    for path in ("provenance/imports/subset-sum/licenses/LICENSE","provenance/imports/subset-sum/licenses/NOTICE",
                 "provenance/imports/subset-sum/licenses/AUTHORS.md","provenance/matching.md"):
        if not (ROOT/path).is_file():errors.append(f"missing import boundary: {path}")
    for old,target in data.get("retired_canonical_paths",{}).items():
        if (ROOT/old).exists():errors.append(f"duplicate retired manuscript remains: {old}")
        if not (ROOT/target.split("#",1)[0]).is_file():errors.append(f"missing integration destination: {old} -> {target}")
    check_recovery(errors)
    if errors:
        print("PROVENANCE CHECK FAILED\n"+"\n".join("- "+e for e in errors));return 1
    print(f"Canonical provenance checked: {len(records)} original paths accounted for");return 0
if __name__=="__main__":sys.exit(main())
