#!/usr/bin/env python3
"""Validate canonical problem structure; this is not a mathematical verifier."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]

def main():
    errors=[]
    for name in ("PROTOCOL.md","CITATION.cff","CONTRIBUTING.md","CONTENTS.md","catalogue.json"):
        if not (ROOT/name).is_file():errors.append(f"missing {name}")
    cards=sorted((ROOT/"problems").glob("*/README.md"))
    for card in cards:
        directory=card.parent
        if "draft" in directory.name:errors.append(f"obsolete draft directory: {directory.name}")
        for name in ("README.md","proof.md","sources.md","verify/README.md"):
            path=directory/name
            if not path.is_file():
                errors.append(f"missing {path.relative_to(ROOT)}")
                continue
            text=path.read_text(encoding="utf-8")
            if name!="verify/README.md":
                for marker in ("Yilin Liu","GPT-6 Astra Pro"):
                    if marker not in text:errors.append(f"{path.relative_to(ROOT)}: missing {marker}")
            if name=="proof.md":
                if text.startswith("# Proof map") or "display-first map" in text:
                    errors.append(f"proof-map placeholder: {path.relative_to(ROOT)}")
                if len(text.split())<350:errors.append(f"main proof unexpectedly short: {path.relative_to(ROOT)}")
        if directory.name.startswith("subset-sum-") and not (directory/"NOTICE.md").is_file():
            errors.append(f"missing import notice in {directory.name}")
    if (ROOT/"overview.pdf").exists():errors.append("obsolete generated overview.pdf is present")
    if (ROOT/"sources").exists():errors.append("unconsolidated checkpoint source tree is present")
    if errors:
        print("CANONICAL STRUCTURE CHECK FAILED\n"+"\n".join("- "+e for e in errors));return 1
    print(f"Canonical structure checked: {len(cards)} substantive problem records");return 0
if __name__=="__main__":sys.exit(main())
