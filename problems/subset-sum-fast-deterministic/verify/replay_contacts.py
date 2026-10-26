#!/usr/bin/env python3
"""Resume a complete contact replay from trusted local JSON work products.

The acceptance kernel remains tools/verify_subset_sum_contacts.py. This
orchestrator saves the binary-subdivision frontier and completed branch
results, binding both to the kernel, menu and (for frontiers) driver bytes.
It is recovery bookkeeping, not a proof-carrying certificate verifier.
The kernel's ordinary --all command remains an independent clean replay.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import verify_subset_sum_contacts as cert

DRIVER_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
CACHE_SCHEMA = 1
FIELDS = ("rho", "gamma", "gamma2", "tau", "target", "branch")


def require(condition, message):
    if not condition:
        raise ValueError("invalid contact replay state: " + message)


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def fingerprint(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def choice_of(job):
    return dict(zip(FIELDS, job[:6]))


def paths(cache, choice):
    name = fingerprint(choice)
    return (cache / (name + ".complete.json"),
            cache / (name + ".frontier.json"))


def unchanged_sources():
    require(hashlib.sha256(Path(cert.__file__).read_bytes()).hexdigest()
            == cert.CHECKER_SHA256, "kernel bytes changed during replay")
    require(hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
            == DRIVER_SHA256, "driver bytes changed during replay")
    # CONTACTS is immutable for this process. Check the on-disk menu too,
    # without importing or executing a changed source file.
    require(hashlib.sha256((ROOT / "tools/verify_subset_sum_scalars.py").read_bytes()).hexdigest()
            == SCALAR_SOURCE_SHA256, "scalar/menu source changed during replay")


SCALAR_SOURCE_SHA256 = hashlib.sha256(
    (ROOT / "tools/verify_subset_sum_scalars.py").read_bytes()).hexdigest()


def write_record(path, payload):
    """Atomic replacement makes an interrupted write harmless."""
    record = dict(payload, payload_sha256=fingerprint(payload))
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(record, indent=2) + "\n")
    temporary.replace(path)


def base_record(choice, kind):
    return dict(cache_schema=CACHE_SCHEMA, kind=kind, choice=choice,
                checker_sha256=cert.CHECKER_SHA256,
                menu_sha256=cert.MENU_SHA256,
                producer="resume_driver", driver_sha256=DRIVER_SHA256)


def read_record(path, choice, kind):
    record = json.loads(path.read_text())
    checksum = record.pop("payload_sha256", None)
    require(checksum == fingerprint(record), "damaged JSON work product")
    require(record.get("cache_schema") == CACHE_SCHEMA, "cache schema")
    require(record.get("kind") == kind and record.get("choice") == choice,
            "wrong branch or record kind")
    require(record.get("checker_sha256") == cert.CHECKER_SHA256,
            "kernel fingerprint mismatch")
    require(record.get("menu_sha256") == cert.MENU_SHA256,
            "menu fingerprint mismatch")
    producer = record.get("producer")
    require(producer in {"kernel_main", "resume_driver"}, "unknown producer")
    if producer == "resume_driver":
        require(record.get("driver_sha256") == DRIVER_SHA256,
                "driver fingerprint mismatch")
    else:
        require(kind == "complete" and record.get("driver_sha256") is None,
                "only completed kernel results may be imported")
    return record


def validate_result(row, choice):
    require({key: row.get(key) for key in FIELDS} == choice, "result choice")
    leaves, empty, nodes, depth = (row.get(k) for k in ("leaves", "empty", "nodes", "depth"))
    require(all(type(x) is int and x >= 0 for x in (leaves, empty, nodes, depth)),
            "result counts")
    require(nodes == 2 * (leaves + empty) - 1, "incomplete subdivision")
    methods = row.get("methods", {})
    allowed = ({"old", "closed", "continuous"} if choice["branch"] == "recursive"
               else {choice["branch"]})
    require(set(methods) <= allowed and all(type(n) is int and n > 0 for n in methods.values())
            and sum(methods.values()) == leaves, "accepted-leaf method counts")
    maximum = F(row["maximum"])
    if leaves:
        margin = F(row["minimum_margin"])
        require(0 <= maximum <= F(choice["target"]) and margin >= 0
                and maximum + margin == F(choice["target"]), "acceptance margin")
    else:
        require(empty > 0 and maximum == 0 and row["minimum_margin"] is None,
                "empty-domain result")


def pack_frontier(pending):
    return [[[list(map(str, interval)) for interval in box], depth]
            for box, depth in pending]


def unpack_frontier(items):
    pending = []
    for box, depth in items:
        require(type(depth) is int and 0 <= depth <= 90, "frontier depth")
        require(len(box) == 3, "frontier dimension")
        decoded = tuple(tuple(F(x) for x in interval) for interval in box)
        require(all(len(interval) == 2 and interval[0] <= interval[1]
                    for interval in decoded), "frontier interval")
        pending.append((decoded, depth))
    return pending


def verify_cached(job, cache, checkpoint_nodes=1000, stop_after_checkpoints=None):
    """Use the kernel's exact operations; retain each unfinished frontier.

    stop_after_checkpoints is used only by the recovery regression check.
    The normal CLI never sets it.
    """
    choice = choice_of(job)
    completed_path, frontier_path = paths(cache, choice)
    if completed_path.exists():
        record = read_record(completed_path, choice, "complete")
        validate_result(record["result"], choice)
        return record["result"]
    rho, gamma, gamma2, tau, target, branch, max_nodes = job
    family = cert.Family(F(rho), None if gamma == "direct" else F(gamma),
                         F(tau), F(target), branch,
                         F(1, 2) if gamma2 == "direct" else F(gamma2))
    resumed = frontier_path.exists()
    if resumed:
        record = read_record(frontier_path, choice, "frontier")
        state = record["state"]
        pending = unpack_frontier(state["pending"])
        nodes, leaves, empty, depthmax = (state[k] for k in ("nodes", "leaves", "empty", "depth"))
        require(all(type(x) is int and x >= 0 for x in (nodes, leaves, empty, depthmax)),
                "frontier counts")
        methods = Counter(state["methods"])
        require(all(type(n) is int and n > 0 for n in methods.values())
                and sum(methods.values()) == leaves, "frontier method counts")
        largest = F(state["maximum"])
        margin = None if state["minimum_margin"] is None else F(state["minimum_margin"])
        prior_seconds = float(state["seconds"])
        require(nodes == 2 * (leaves + empty) + len(pending) - 1,
                "frontier does not account for the complete binary tree")
        require(0 <= largest <= family.target and prior_seconds >= 0,
                "frontier maximum or elapsed time")
        require((not leaves and margin is None) or
                (leaves and margin is not None and margin >= 0
                 and largest + margin == family.target), "frontier acceptance margin")
    else:
        pending = [(family.initial(), 0)]
        nodes = leaves = empty = depthmax = 0
        methods, largest, margin, prior_seconds = Counter(), F(0), None, 0.0
    started = time.monotonic()
    last_nodes, last_time, checkpoints = nodes - checkpoint_nodes, started, 0

    def save_frontier():
        unchanged_sources()
        require(nodes == 2 * (leaves + empty) + len(pending) - 1,
                "internal frontier accounting")
        state = dict(pending=pack_frontier(pending), nodes=nodes, leaves=leaves,
                     empty=empty, depth=depthmax, methods=dict(methods),
                     maximum=str(largest), minimum_margin=None if margin is None else str(margin),
                     seconds=prior_seconds + time.monotonic() - started)
        write_record(frontier_path, dict(base_record(choice, "frontier"), state=state))

    while pending:
        if nodes - last_nodes >= checkpoint_nodes or time.monotonic() - last_time >= 20:
            save_frontier()
            checkpoints += 1
            last_nodes, last_time = nodes, time.monotonic()
            if stop_after_checkpoints is not None and checkpoints >= stop_after_checkpoints:
                raise InterruptedError("deliberate recovery-check interruption")
        original, depth = pending.pop()
        nodes += 1
        if nodes > max_nodes:
            raise RuntimeError("node limit reached: " + str(choice))
        box = family.tighten(original)
        if box is None:
            empty += 1
            continue
        proposal = family.propose(box)
        floating, _ = family.bound(box, proposal, False)
        if floating <= float(family.target) + 1e-12:
            upper, method = family.bound(box, proposal, True)
            if upper <= cert.LD * family.target:
                leaves += 1
                methods[method] += 1
                largest = max(largest, upper / cert.LD)
                difference = family.target - upper / cert.LD
                margin = difference if margin is None else min(margin, difference)
                depthmax = max(depthmax, depth)
                continue
        widths = [(box[i][1] - box[i][0]) * weight
                  for i, weight in enumerate((3, 1, 2))]
        axis = max(range(3), key=lambda i: (widths[i], -i))
        if widths[axis] == 0 or depth >= 90:
            raise RuntimeError("unresolved box: " + str((choice, box, floating)))
        mid = (box[axis][0] + box[axis][1]) / 2
        left, right = list(box), list(box)
        left[axis], right[axis] = (box[axis][0], mid), (mid, box[axis][1])
        pending.append((tuple(right), depth + 1))
        pending.append((tuple(left), depth + 1))

    row = dict(choice, leaves=leaves, empty=empty, nodes=nodes, depth=depthmax,
               maximum=str(largest), minimum_margin=None if margin is None else str(margin),
               methods=dict(methods), seconds=round(prior_seconds + time.monotonic() - started, 3))
    validate_result(row, choice)
    unchanged_sources()
    write_record(completed_path, dict(base_record(choice, "complete"), result=row,
                                     resumed_frontier=resumed))
    if frontier_path.exists():
        frontier_path.unlink()
    return row


def main():
    if not __debug__:
        raise SystemExit("Run mathematical verification without python -O.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True, help="trusted local recovery directory")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--max-nodes", type=int, default=5_000_000)
    parser.add_argument("--output", type=Path, required=True, help="complete receipt, written only after success")
    args = parser.parse_args()
    if args.jobs < 1 or args.max_nodes < 1:
        parser.error("positive jobs and node limit required")
    args.cache.mkdir(parents=True, exist_ok=True)
    jobs = [tuple(choice[k] for k in FIELDS) + (args.max_nodes,)
            for choice in cert.EXPECTED_CHOICES]
    results = []
    with ProcessPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(verify_cached, job, args.cache) for job in jobs]
        for future in as_completed(futures):
            row = future.result()
            results.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    unchanged_sources()
    require(len(results) == len(cert.EXPECTED_CHOICES), "incomplete final menu")
    provenance = Counter()
    for choice in cert.EXPECTED_CHOICES:
        path, _ = paths(args.cache, choice)
        record = read_record(path, choice, "complete")
        provenance[record["producer"]] += 1
    summary = dict(receipt_schema=2, status="PASS", complete_X02_contact_menu=True,
                   checker_sha256=cert.CHECKER_SHA256, menu_sha256=cert.MENU_SHA256,
                   expected_branch_count=len(cert.EXPECTED_CHOICES), expected_choices=cert.EXPECTED_CHOICES,
                   branches=len(results), leaves=sum(r["leaves"] for r in results),
                   arithmetic="exact rationals; integer interval atanh logarithms",
                   scope="continuous profile inequalities conditional on the analytic circuit and trace lemmas",
                   segmented_replay=dict(driver_sha256=DRIVER_SHA256, producers=dict(provenance),
                       note="Completed branches and unfinished frontiers were retained as trusted local work products; this is not a proof-carrying checkpoint format."),
                   results=sorted(results, key=lambda r: (F(r["rho"]), r["gamma"], F(r["tau"]), r["branch"])))
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(json.dumps(summary, indent=2) + "\n")
    temporary.replace(args.output)
    cert.check_receipt(args.output)


if __name__ == "__main__":
    main()
