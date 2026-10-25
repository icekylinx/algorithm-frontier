#!/usr/bin/env python3
"""Verify legacy checkpoint manifests and available increment-only checkpoint layouts."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check_bytes(path: Path, expected_bytes: int, expected_sha: str) -> None:
    if not path.is_file():
        errors.append(f"missing {path}")
        return
    data = path.read_bytes()
    if len(data) != expected_bytes:
        errors.append(f"size changed {path}: {len(data)} != {expected_bytes}")
    digest = hashlib.sha256(data).hexdigest()
    if digest != expected_sha:
        errors.append(f"hash changed {path}: {digest} != {expected_sha}")


# The original O/P/Q manifest remains the authoritative byte map for the
# complete baseline and the two earlier increments.
legacy = json.loads((ROOT / "provenance/checkpoint-files.json").read_text())
seen = set()
for item in legacy["files"]:
    checkpoint = item["checkpoint"].lower()
    path = item["path"]
    key = (checkpoint, path)
    seen.add(key)
    check_bytes(ROOT / f"sources/checkpoint-{checkpoint}" / path, item["bytes"], item["sha256"])

# Increment manifests are optional independently so a future push can land
# one verified checkpoint at a time. If present, each manifest is fully checked.
specs = {
    "r": {"parent_checkpoint": "Q", "parent_sha256": "8ff7b58aafa78cf67747fcd58433f98d8968a11d03ee61c3041497b3b7fc96e5"},
    "s": {"parent_checkpoint": "R", "parent_archive": "deterministic_related_problems_increment_20261025_R.zip", "parent_sha256": "c5a0cacff1e0ab9283da4e6214d7f80ced7fc46cc3b15e5700dc9098bf7e3bf4"},
    "t": {"parent_checkpoint": "S", "parent_archive": "deterministic_related_problems_increment_20261025_S.zip", "parent_sha256": "0aa96b8c60ff9f866df6cc1cfbae1764a9d016e0351eb1944be343b1d41912ed"},
    "u": {"parent_checkpoint": "T", "parent_archive": "deterministic_related_problems_increment_20261025_T.zip", "parent_sha256": "ce5d4260f803c4872e9065ebba8c0c5275087412e78d180dd2c384556f02b0e0"},
}
for checkpoint, expected in specs.items():
    directory = ROOT / f"sources/checkpoint-{checkpoint}"
    manifest_path = directory / "MANIFEST.json"
    if not manifest_path.is_file():
        continue
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("checkpoint", "").lower() != checkpoint:
        errors.append(f"wrong checkpoint label in {manifest_path}")
    if checkpoint == "r":
        if manifest.get("parent_checkpoint", "").upper() != expected["parent_checkpoint"]:
            errors.append(f"wrong parent checkpoint for R: {manifest.get('parent_checkpoint')}")
    else:
        parent = manifest.get("parent_archive") or manifest.get("parent", {}).get("filename")
        if parent != expected["parent_archive"]:
            errors.append(f"wrong parent archive for {checkpoint.upper()}: {parent}")
        if checkpoint == "s" and manifest.get("scope") != "increment_only_since_R":
            errors.append("S manifest does not declare increment_only_since_R")
        if checkpoint in {"t", "u"} and not manifest.get("scope", "").startswith("Increment only"):
            errors.append(f"{checkpoint.upper()} manifest is not increment-only")
    parent_hash = manifest.get("parent_sha256") or manifest.get("parent", {}).get("sha256")
    if parent_hash != expected["parent_sha256"]:
        errors.append(f"wrong parent archive hash for {checkpoint.upper()}")
    listed = manifest.get("files") or manifest.get("payload", [])
    declared = manifest.get("research_files")
    if declared is not None and declared != len(listed):
        errors.append(f"{checkpoint.upper()} file count does not match MANIFEST.json")
    for item in listed:
        name = item.get("name", item.get("file"))
        check_bytes(directory / name, item["bytes"], item["sha256"])

# A path may occur in multiple legacy checkpoints only for retained metadata.
for path in sorted({path for _, path in seen}):
    owners = {checkpoint for checkpoint, candidate in seen if candidate == path}
    if len(owners) > 1 and path not in {"README.md", "MANIFEST.md", "current_checkpoint/README.md"} and not path.startswith("CHECKPOINT_"):
        errors.append(f"non-metadata path duplicated across legacy checkpoints: {path}")

if errors:
    print("INCREMENTAL SOURCE CHECK FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

legacy_count = len(legacy["files"])
counts = []
for checkpoint in ("r", "s", "t", "u"):
    path = ROOT / f"sources/checkpoint-{checkpoint}/MANIFEST.json"
    if path.is_file():
        m=json.loads(path.read_text()); counts.append(f"{checkpoint.upper()} {len(m.get('files') or m.get('payload', []))}")
print(f"INCREMENTAL SOURCE CHECK OK: {legacy_count} legacy files" + (" + " + " + ".join(counts) if counts else ""))
