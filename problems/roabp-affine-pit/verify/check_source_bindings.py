"""Check exact imported source identities and reversible publication edits.

This verifies provenance, not mathematical correctness or external review.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]


def digest(body):
    return hashlib.sha256(body).hexdigest()


def main():
    manifest = json.loads((ROOT / 'provenance/imports/roabp-affine-pit.json').read_text())
    seen = set()
    for entry in manifest['records']:
        name = entry['canonical_path']
        assert name not in seen, name
        seen.add(name)
        path = ROOT / name
        assert path.is_file(), name
        body = path.read_bytes()
        assert digest(body) == entry['canonical_sha256'], name
        assert len(body) == entry['canonical_bytes'], name
        text = body.decode()
        for edit in reversed(entry.get('editorial_changes', [])):
            assert text.count(edit['new_text']) == 1, name
            text = text.replace(edit['new_text'], edit['old_text'], 1)
        original = text.encode()
        assert digest(original) == entry['original_sha256'], name
        assert len(original) == entry['original_bytes'], name
    print(f'ROABP import bindings: {len(seen)} sources; all exact identities and editorial reversals passed.')


if __name__ == '__main__':
    main()
