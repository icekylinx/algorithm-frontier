#!/usr/bin/env python3
"""Resume fixed third-lookup contacts from trusted local JSON work products.

Every completed branch and unfinished subdivision frontier is bound to the
kernel, fixed menu and driver bytes. Atomic replacement preserves previous
work after interruption. These local caches are recovery state, not proof-
carrying certificates. The kernel's --all command is an independent replay.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from fractions import Fraction as F
import hashlib
import json
import multiprocessing
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import verify_subset_sum_third_contacts as cert

DRIVER_SHA256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
CACHE_SCHEMA = 1
FIELDS = cert.FIELDS


def require(condition, message):
    if not condition:
        raise ValueError("invalid contact replay state: " + message)


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def fingerprint(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def choice_of(job):
    return dict(zip(FIELDS, job[:7]))


def paths(cache, choice):
    name = fingerprint(choice)
    return (cache / (name + ".complete.json"),
            cache / (name + ".frontier.json"))


def unchanged_sources():
    cert.unchanged_sources()
    require(hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
            == DRIVER_SHA256, "driver bytes changed during replay")


def worker_sources(checker_digest, menu_digest, driver_digest):
    cert.worker_sources(checker_digest, menu_digest)
    require(DRIVER_SHA256 == driver_digest, "spawned worker driver mismatch")
    unchanged_sources()


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
    require(record.get("producer") == "resume_driver", "unknown producer")
    require(record.get("driver_sha256") == DRIVER_SHA256,
            "driver fingerprint mismatch")
    return record


def validate_result(row, choice):
    cert.validate_result(row, choice)


def pack_frontier(pending):
    return [[[list(map(str, interval)) for interval in box], depth]
            for box, depth in pending]


def unpack_frontier(items):
    pending = []
    for box, depth in items:
        require(type(depth) is int and 0 <= depth <= 90, "frontier depth")
        require(len(box) == 4, "frontier dimension")
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
    unchanged_sources()
    choice = choice_of(job)
    completed_path, frontier_path = paths(cache, choice)
    if completed_path.exists():
        record = read_record(completed_path, choice, "complete")
        validate_result(record["result"], choice)
        return record["result"]
    rho, gamma, gamma2, gamma3, tau, target, branch, max_nodes = job
    family = cert.Family(F(rho), None if gamma == "direct" else F(gamma),
                         F(tau), F(target), branch,
                         F(1, 2) if gamma2 == "direct" else F(gamma2), F(gamma3))
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
        gap = max(F(0), max(cert.at(cert.sub(family.d1, family.q), point)
                               for point in cert.corners(box)))
        widths = [(box[i][1] - box[i][0]) * weight
                  for i, weight in enumerate((F(3), F(1), F(2), 2 * gap))]
        axis = max(range(4), key=lambda i: (widths[i], -i))
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
    parser.add_argument("--all", action="store_true", required=True,
                        help="replay every branch in the fixed third-lookup menu")
    parser.add_argument("--cache", type=Path, required=True, help="trusted local recovery directory")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--max-nodes", type=int, default=5_000_000)
    parser.add_argument("--output", type=Path, required=True,
                        help="complete receipt, written only after all branches pass")
    args = parser.parse_args()
    if args.jobs < 1 or args.max_nodes < 1:
        parser.error("positive jobs and node limit required")
    args.cache.mkdir(parents=True, exist_ok=True)
    jobs = [tuple(choice[key] for key in FIELDS) + (args.max_nodes,)
            for choice in cert.EXPECTED_CHOICES]
    results = []
    with ProcessPoolExecutor(max_workers=args.jobs, mp_context=multiprocessing.get_context("spawn"),
                             initializer=worker_sources,
                             initargs=(cert.CHECKER_SHA256, cert.MENU_SHA256, DRIVER_SHA256)) as pool:
        for future in as_completed([pool.submit(verify_cached, job, args.cache) for job in jobs]):
            row = future.result()
            results.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    unchanged_sources()
    for choice in cert.EXPECTED_CHOICES:
        path, _ = paths(args.cache, choice)
        record = read_record(path, choice, "complete")
        validate_result(record["result"], choice)
    provenance = dict(driver_sha256=DRIVER_SHA256, completed_branches=len(cert.EXPECTED_CHOICES),
                      note="Completed branches and unfinished frontiers were retained as trusted local work products; this is not a proof-carrying checkpoint format.")
    receipt = cert.make_receipt(results, provenance)
    cert.write_receipt(args.output, receipt)
    print(json.dumps({key: value for key, value in receipt.items()
                      if key not in {"results", "expected_choices"}}, sort_keys=True))


if __name__ == "__main__":
    main()
