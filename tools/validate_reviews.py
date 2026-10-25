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

    draft_sources = payload.get("draft_sources", [])
    if not isinstance(draft_sources, list):
        fail("draft_sources must be an array when present")
    draft_ids: set[str] = set()
    for index, draft in enumerate(draft_sources):
        if not isinstance(draft, dict):
            fail(f"draft source {index} must be an object")
        for field in ("id", "path", "status", "maturity", "family_hints", "payloads", "review_backlog", "open_actions"):
            if field not in draft:
                fail(f"draft source {index} is missing: {field}")
        draft_id = draft["id"]
        if not isinstance(draft_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", draft_id):
            fail(f"draft source {index} has invalid id")
        if draft_id in draft_ids:
            fail(f"duplicate draft source id: {draft_id}")
        draft_ids.add(draft_id)
        if draft["status"] != "draft":
            fail(f"{draft_id}: status must be draft")
        if not isinstance(draft["maturity"], str) or "source-only" not in draft["maturity"]:
            fail(f"{draft_id}: maturity must state source-only")
        source_dir = relative_path(draft["path"], f"{draft_id}.path")
        if not source_dir.is_dir():
            fail(f"{draft_id}: source path does not exist: {draft['path']}")
        for field in ("family_hints", "payloads", "open_actions"):
            values = draft[field]
            if not isinstance(values, list) or not values or not all(isinstance(x, str) and x.strip() for x in values):
                fail(f"{draft_id}: {field} must be a non-empty-string array")
        for item in draft["payloads"]:
            item_path = relative_path(item, f"{draft_id}.payloads[]")
            if not item_path.is_file():
                fail(f"{draft_id}: missing payload: {item}")
            if source_dir not in item_path.parents:
                fail(f"{draft_id}: payload escapes source directory: {item}")
        backlog = relative_path(draft["review_backlog"], f"{draft_id}.review_backlog")
        if not backlog.is_file() or not str(backlog.relative_to(ROOT)).startswith("reviews/"):
            fail(f"{draft_id}: review_backlog must point to a file under reviews/")

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
        finite_checks = record["finite_checks"]
        if not isinstance(finite_checks, list):
            fail(f"{record_id}: finite_checks must be an array")
        for check in finite_checks:
            check_path = relative_path(check, f"{record_id}.finite_checks[]")
            if not check_path.exists():
                fail(f"{record_id}: missing finite check: {check}")
        if not isinstance(record["open_issues"], list) or not all(isinstance(x, str) and x.strip() for x in record["open_issues"]):
            fail(f"{record_id}: open_issues must be a non-empty-string array")
        if not isinstance(record["formal_verification"], str):
            fail(f"{record_id}: formal_verification must be a string")

    print(f"review validation: {len(records)} records, {len(ids)} unique ids, {len(draft_sources)} draft source(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
