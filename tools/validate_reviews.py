#!/usr/bin/env python3
"""Check exact result coverage and executable-evidence paths in the registry."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]

def main():
    data=json.loads((ROOT/"reviews/registry.json").read_text());errors=[]
    if data.get("schema_version")!=3:errors.append("expected registry schema 3")
    actual={p.parent.name for p in (ROOT/"problems").glob("*/README.md")}
    records=data.get("records",[]);ids=[r["id"] for r in records]
    if len(ids)!=len(set(ids)):errors.append("duplicate result records")
    if set(ids)!=actual:errors.append(f"coverage mismatch: missing={sorted(actual-set(ids))}, extra={sorted(set(ids)-actual)}")
    for r in records:
        if r["path"]!="problems/"+r["id"]:errors.append(f"incorrect canonical path for {r['id']}")
        if r.get("formal_verification")!="not-claimed":errors.append(f"unsupported formal-verification label: {r['id']}")
        if not (ROOT/r["evidence_note"]).is_file():errors.append(f"missing evidence note: {r['evidence_note']}")
        review=r.get("review")
        if review is not None:
            if set(review)!={"status","scope","date","conditions"}:
                errors.append(f"invalid review fields: {r['id']}")
            if review.get("status") not in {"pending","partial","ready"}:
                errors.append(f"invalid review status: {r['id']}")
            if not review.get("scope") or not review.get("date"):
                errors.append(f"missing review scope/date: {r['id']}")
            if not isinstance(review.get("conditions"),list) or any(not isinstance(c,str) or not c.strip() for c in review.get("conditions",[])):
                errors.append(f"invalid review conditions: {r['id']}")
        for check in r.get("checks",[]):
            p=ROOT/check["path"]
            if not p.is_file() or p.suffix!=".py":errors.append(f"missing executable evidence: {r['id']} -> {check['path']}")
            if not check.get("scope"):errors.append(f"missing finite scope: {r['id']}")
    if errors:
        print("EVIDENCE REGISTRY CHECK FAILED\n"+"\n".join("- "+e for e in errors));return 1
    print(f"Evidence registry checked: {len(records)} result records");return 0
if __name__=="__main__":sys.exit(main())
