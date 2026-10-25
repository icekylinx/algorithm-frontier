#!/usr/bin/env python3
"""Check source-only draft checkpoints without promoting them to result cards.

The curated catalogue has a separate review registry for promoted cards. A
new checkpoint can enter ``sources/`` while its proof and algorithm reviews
are still pending. This check validates the metadata needed to make that state
explicit; it does not inspect or reproduce manuscript contents.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "sources"
STATUS_RE = re.compile(r"\bstatus\s*:\s*draft\b", re.IGNORECASE)
MATURITY_RE = re.compile(r'"(?:status|maturity)"\s*:\s*"draft"', re.IGNORECASE)


def fail(message: str) -> None:
    print(f"draft-source check: error: {message}", file=sys.stderr)
    raise SystemExit(1)


def relative_inside_root(path: Path, label: str) -> Path:
    try:
        path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        fail(f"{label} escapes repository root")
    return path


def listed_payloads(manifest: dict, source_dir: Path) -> list[str]:
    """Return payload names used by the R--U and X manifest shapes."""
    entries = manifest.get("files")
    if entries is None:
        entries = manifest.get("payload")
    if entries is None:
        return []
    if not isinstance(entries, list):
        fail(f"{source_dir.name}: manifest payload/files must be an array")
    names: list[str] = []
    for index, entry in enumerate(entries):
        if isinstance(entry, str):
            name = entry
        elif isinstance(entry, dict):
            name = entry.get("name", entry.get("file"))
        else:
            fail(f"{source_dir.name}: manifest payload entry {index} is not an object or string")
        if not isinstance(name, str) or not name or Path(name).is_absolute():
            fail(f"{source_dir.name}: manifest payload entry {index} has invalid name")
        payload_path = relative_inside_root((source_dir / name).resolve(), f"{source_dir.name} payload")
        if not payload_path.is_file():
            fail(f"{source_dir.name}: manifest payload is missing: {name}")
        names.append(name)
    return names


def check_draft(source_dir: Path) -> None:
    readme = source_dir / "README.md"
    if not readme.is_file():
        fail(f"{source_dir.name}: draft source is missing README.md")
    text = readme.read_text(encoding="utf-8")
    status_readme = source_dir / "README_INCREMENT_X.md"
    status_text = status_readme.read_text(encoding="utf-8") if status_readme.is_file() else ""
    manifest_path = source_dir / "MANIFEST.json"
    manifest: dict = {}
    manifest_text = ""
    if manifest_path.exists():
        manifest_text = manifest_path.read_text(encoding="utf-8")
        try:
            payload = json.loads(manifest_text)
        except json.JSONDecodeError as exc:
            fail(f"{source_dir.name}: invalid MANIFEST.json: {exc}")
        if not isinstance(payload, dict):
            fail(f"{source_dir.name}: MANIFEST.json must contain an object")
        manifest = payload

    # A directory is a draft source only when it opts into the vocabulary.
    # Existing complete checkpoints retain their older manifest shape.
    is_draft = bool(STATUS_RE.search(text) or STATUS_RE.search(status_text) or MATURITY_RE.search(manifest_text))
    if not is_draft:
        return

    marker_text = (text + "\n" + status_text).lower()
    if not (
        "source-only" in marker_text
        or "not promoted" in marker_text
        or "no promoted result" in marker_text
    ):
        fail(f"{source_dir.name}: draft README must state that the payload is source-only/not promoted")
    if manifest:
        checkpoint = manifest.get("checkpoint")
        expected = source_dir.name.removeprefix("checkpoint-").upper()
        if checkpoint is not None and str(checkpoint).upper() != expected:
            fail(f"{source_dir.name}: manifest checkpoint must be {expected!r}")
        declared_status = manifest.get("status", manifest.get("maturity"))
        if declared_status is not None and str(declared_status).lower() != "draft":
            fail(f"{source_dir.name}: manifest status/maturity must be draft")
        listed = listed_payloads(manifest, source_dir)
        if not listed:
            fail(f"{source_dir.name}: draft manifest must list payload files")
    else:
        payload_files = [p for p in source_dir.iterdir() if p.is_file() and p.name != "README.md"]
        if not payload_files:
            fail(f"{source_dir.name}: draft source has no payload files")


def main() -> int:
    if not SOURCE_ROOT.is_dir():
        fail("sources/ is missing")
    checkpoint_dirs = sorted(path for path in SOURCE_ROOT.glob("checkpoint-*") if path.is_dir())
    for source_dir in checkpoint_dirs:
        check_draft(source_dir)
    drafts = []
    for source_dir in checkpoint_dirs:
        readme_text = (source_dir / "README.md").read_text(encoding="utf-8")
        status_text = (source_dir / "README_INCREMENT_X.md").read_text(encoding="utf-8") if (source_dir / "README_INCREMENT_X.md").exists() else ""
        manifest_text = (
            (source_dir / "MANIFEST.json").read_text(encoding="utf-8")
            if (source_dir / "MANIFEST.json").exists()
            else ""
        )
        if STATUS_RE.search(readme_text) or STATUS_RE.search(status_text) or MATURITY_RE.search(manifest_text):
            drafts.append(source_dir.name)
    print(f"draft-source check: {len(checkpoint_dirs)} checkpoint sources, {len(drafts)} draft source(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
