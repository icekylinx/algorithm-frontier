#!/usr/bin/env python3
"""Check that every mapped retained import has an existing canonical target.

Archive hashes identify imported bytes. They intentionally do not freeze
current mathematical manuscripts after authorized editing.
"""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]

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
    if errors:
        print("PROVENANCE CHECK FAILED\n"+"\n".join("- "+e for e in errors));return 1
    print(f"Canonical provenance checked: {len(records)} original paths accounted for");return 0
if __name__=="__main__":sys.exit(main())
