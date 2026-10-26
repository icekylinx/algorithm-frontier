#!/usr/bin/env python3
"""Check exact result coverage and executable-evidence paths in the registry."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]

def main():
    data=json.loads((ROOT/"reviews/registry.json").read_text());errors=[]
    if data.get("schema_version")!=2:errors.append("expected registry schema 2")
    actual={p.parent.name for p in (ROOT/"problems").glob("*/README.md")}
    records=data.get("records",[]);ids=[r["id"] for r in records]
    if len(ids)!=len(set(ids)):errors.append("duplicate result records")
    if set(ids)!=actual:errors.append(f"coverage mismatch: missing={sorted(actual-set(ids))}, extra={sorted(set(ids)-actual)}")
    for r in records:
        if r["path"]!="problems/"+r["id"]:errors.append(f"incorrect canonical path for {r['id']}")
        if r.get("formal_verification")!="not-claimed":errors.append(f"unsupported formal-verification label: {r['id']}")
        if not (ROOT/r["evidence_note"]).is_file():errors.append(f"missing evidence note: {r['evidence_note']}")
        for check in r.get("checks",[]):
            p=ROOT/check["path"]
            if not p.is_file() or p.suffix!=".py":errors.append(f"missing executable evidence: {r['id']} -> {check['path']}")
            if not check.get("scope"):errors.append(f"missing finite scope: {r['id']}")
    if errors:
        print("EVIDENCE REGISTRY CHECK FAILED\n"+"\n".join("- "+e for e in errors));return 1
    print(f"Evidence registry checked: {len(records)} result records");return 0
if __name__=="__main__":sys.exit(main())
