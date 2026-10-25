#!/usr/bin/env python3
"""Verify the committed O/P/Q source-file manifest and incremental layout."""
from pathlib import Path
import hashlib, json, sys
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'provenance/checkpoint-files.json').read_text())
errors = []
seen = set()
for item in manifest['files']:
    key = (item['checkpoint'], item['path'])
    seen.add(key)
    p = root / f"sources/checkpoint-{item['checkpoint']}" / item['path']
    if not p.is_file(): errors.append(f"missing {p}"); continue
    data = p.read_bytes()
    if len(data) != item['bytes']: errors.append(f"size changed {p}")
    if hashlib.sha256(data).hexdigest() != item['sha256']: errors.append(f"hash changed {p}")
# A path may occur in multiple checkpoints only for retained checkpoint metadata.
for path in sorted({x[1] for x in seen}):
    owners = {x[0] for x in seen if x[1] == path}
    if len(owners) > 1 and path not in {'README.md','MANIFEST.md','current_checkpoint/README.md'} and not path.startswith('CHECKPOINT_'):
        errors.append(f"non-metadata path duplicated across checkpoints: {path}")
if errors:
    print("INCREMENTAL SOURCE CHECK FAILED")
    print("\n".join(f"- {e}" for e in errors)); sys.exit(1)
print(f"INCREMENTAL SOURCE CHECK OK: {len(manifest['files'])} retained files")
