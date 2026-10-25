#!/usr/bin/env python3
"""Validate the review registry without evaluating the mathematical claims."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "reviews" / "registry.json"
REQUIRED_RECORD_FIELDS = {
    "id", "path", "tier", "status", "last_reviewed", "proof_review",
    "algorithm_review", "source_review", "finite_checks",
    "formal_verification", "open_issues", "reports",
}
ALLOWED_TIERS = {"A", "B", "C", "D"}
ALLOWED_STATUS = {"reviewed", "conditional", "needs-follow-up", "archival"}
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fail(message: str) -> None:
    print(f"review validation: error: {message}", file=sys.stderr)
    raise SystemExit(1)


def relative_path(value: object, field: str) -> Path:
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        fail(f"{field} must be a relative path")
    path = (ROOT / value).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"{field} escapes the repository: {value}")
    return path


def main() -> int:
    if not REGISTRY.exists():
        fail("reviews/registry.json is missing")
    try:
        payload = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON: {exc}")

    if payload.get("schema_version") != 1:
        fail("schema_version must be 1")
    policy = payload.get("review_policy")
    if not isinstance(policy, dict):
        fail("review_policy must be an object")
    if policy.get("finite_checks_are_formal_verification") is not False:
        fail("finite_checks_are_formal_verification must be false")
    if policy.get("default_formal_verification_status") != "not-claimed":
        fail("default_formal_verification_status must be not-claimed")
    if policy.get("required_roles") != ["proof_review", "algorithm_review", "source_review"]:
        fail("required_roles must list proof_review, algorithm_review, source_review")

    records = payload.get("records")
    if not isinstance(records, list) or not records:
        fail("records must be a non-empty array")
    ids: set[str] = set()
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            fail(f"record {index} must be an object")
        missing = REQUIRED_RECORD_FIELDS - set(record)
        if missing:
            fail(f"record {index} is missing: {', '.join(sorted(missing))}")
        record_id = record["id"]
        if not isinstance(record_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", record_id):
            fail(f"record {index} has invalid id")
        if record_id in ids:
            fail(f"duplicate record id: {record_id}")
        ids.add(record_id)
        if record["tier"] not in ALLOWED_TIERS:
            fail(f"{record_id}: invalid tier")
        if record["status"] not in ALLOWED_STATUS:
            fail(f"{record_id}: invalid status")
        reviewed = record["last_reviewed"]
        if not isinstance(reviewed, str) or not ISO_DATE.fullmatch(reviewed):
            fail(f"{record_id}: last_reviewed must be ISO date")
        try:
            date.fromisoformat(reviewed)
        except ValueError:
            fail(f"{record_id}: invalid last_reviewed date")
        record_path = relative_path(record["path"], f"{record_id}.path")
        if not record_path.exists():
            fail(f"{record_id}: result path does not exist: {record['path']}")
        reports = record["reports"]
        if not isinstance(reports, list) or not reports:
            fail(f"{record_id}: reports must be a non-empty array")
        for role in ("proof_review", "algorithm_review", "source_review"):
            path = relative_path(record[role], f"{record_id}.{role}")
            if not path.exists():
                fail(f"{record_id}: missing {role}: {record[role]}")
            if not str(path.relative_to(ROOT)).startswith("reviews/"):
                fail(f"{record_id}: {role} must live under reviews/")
        for report in reports:
            path = relative_path(report, f"{record_id}.reports[]")
            if not path.exists():
                fail(f"{record_id}: missing report: {report}")
            if not str(path.relative_to(ROOT)).startswith("reviews/"):
                fail(f"{record_id}: reports must live under reviews/")
        if not isinstance(record["finite_checks"], list):
            fail(f"{record_id}: finite_checks must be an array")
        if not isinstance(record["open_issues"], list) or not all(isinstance(x, str) and x.strip() for x in record["open_issues"]):
            fail(f"{record_id}: open_issues must be a non-empty-string array")
        if not isinstance(record["formal_verification"], str):
            fail(f"{record_id}: formal_verification must be a string")

    print(f"review validation: {len(records)} records, {len(ids)} unique ids")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
