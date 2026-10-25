#!/usr/bin/env python3
"""Check the curation contract; this is a structural check, not a proof checker."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
problems = ROOT / "problems"
errors = []
if not (ROOT / "PROTOCOL.md").is_file(): errors.append("missing PROTOCOL.md")
if not (ROOT / "CITATION.cff").is_file(): errors.append("missing CITATION.cff")
for d in sorted(p for p in problems.iterdir() if p.is_dir() and p.name != "__pycache__"):
    for name in ("README.md", "proof.md", "sources.md"):
        if not (d / name).is_file(): errors.append(f"{d}: missing {name}")
    verifies = list((d / "verify").glob("*")) if (d / "verify").is_dir() else []
    if len(verifies) < 2: errors.append(f"{d}: fewer than two verify files")
    for name in ("README.md", "proof.md", "sources.md"):
        p = d / name
        if p.is_file():
            text = p.read_text(errors="replace")
            for marker in ("Yilin Liu", "GPT-6 Astra Pro"):
                if marker not in text: errors.append(f"{p}: missing {marker}")
if errors:
    print("CURATION CHECK FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"CURATION CHECK OK: {len([p for p in problems.iterdir() if p.is_dir()])} problem directories")
