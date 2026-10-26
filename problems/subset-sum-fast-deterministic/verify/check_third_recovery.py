#!/usr/bin/env python3
"""Exercise actual interruption/resume and reject mismatched recovery hashes."""
from __future__ import annotations

import ast
from copy import deepcopy
import hashlib
import json
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction as F
from pathlib import Path
import tempfile

import replay_third_contacts as replay


EXECUTION_CHECKER_SHA256 = "a8cf3c045780ab72ef8f31128be013b561f4bfe8e08cd22a3bd30b6fb521448b"
EXECUTION_RECEIPT_SHA256 = "7a8260c24922e9b46111252a81874fb5751c58e392ec6ebc32436e08c3247bb2"


def check_distribution_normalization(kernel_bytes, receipt):
    """Accept exactly one removed final LF and an unchanged original receipt.

    This validates a byte-preserving mathematical-source transfer. It does
    not claim a fresh contact replay under the distribution's new digest.
    """
    def require(condition, message):
        if not condition:
            raise ValueError("invalid source normalization: " + message)

    require(type(kernel_bytes) is bytes and kernel_bytes.endswith(b"\n")
            and not kernel_bytes.endswith(b"\n\n"), "exact final-LF shape")
    original_kernel = kernel_bytes + b"\n"
    require(hashlib.sha256(original_kernel).hexdigest() == EXECUTION_CHECKER_SHA256,
            "reconstructed execution kernel hash")
    distribution_digest = hashlib.sha256(kernel_bytes).hexdigest()
    require(ast.dump(ast.parse(kernel_bytes), include_attributes=False)
            == ast.dump(ast.parse(original_kernel), include_attributes=False),
            "AST changed")
    require(receipt.get("checker_sha256") == distribution_digest,
            "distribution kernel fingerprint")
    segmented = receipt.get("segmented_replay")
    require(isinstance(segmented, dict), "segmented replay provenance")
    expected = dict(operation="remove_one_trailing_newline",
                    execution_checker_sha256=EXECUTION_CHECKER_SHA256,
                    distribution_checker_sha256=distribution_digest,
                    original_receipt_sha256=EXECUTION_RECEIPT_SHA256)
    require(segmented.get("distribution_normalization") == expected,
            "normalization operation or source fingerprints")
    original_receipt = deepcopy(receipt)
    original_receipt["checker_sha256"] = EXECUTION_CHECKER_SHA256
    del original_receipt["segmented_replay"]["distribution_normalization"]
    original_receipt_bytes = (json.dumps(original_receipt, indent=2) + "\n").encode()
    require(hashlib.sha256(original_receipt_bytes).hexdigest() == EXECUTION_RECEIPT_SHA256,
            "reconstructed execution receipt hash")
    return dict(status="PASS_NORMALIZATION_TRANSFER", branches=len(receipt["results"]),
                execution_checker_sha256=EXECUTION_CHECKER_SHA256,
                distribution_checker_sha256=distribution_digest,
                original_receipt_sha256=EXECUTION_RECEIPT_SHA256,
                scope="Exactly one final LF was removed after the completed segmented replay; every original receipt byte and mathematical branch record is recoverable.")


def check_normalization_fault_rejection(kernel_bytes, receipt):
    """Reject source, operation, digest and result mutations before publication."""
    check_distribution_normalization(kernel_bytes, receipt)
    faults = []
    assert b"TERMS = 32" in kernel_bytes
    faults.append((kernel_bytes.replace(b"TERMS = 32", b"TERMS = 33", 1), deepcopy(receipt)))
    faults.append((kernel_bytes+b"\n", deepcopy(receipt)))
    wrong_digest = deepcopy(receipt)
    wrong_digest["checker_sha256"] = "0"*64
    faults.append((kernel_bytes, wrong_digest))
    wrong_operation = deepcopy(receipt)
    wrong_operation["segmented_replay"]["distribution_normalization"]["operation"] = "rstrip"
    faults.append((kernel_bytes, wrong_operation))
    wrong_result = deepcopy(receipt)
    wrong_result["results"][0]["nodes"] += 2
    faults.append((kernel_bytes, wrong_result))
    rejected = 0
    for mutated_kernel, mutated_receipt in faults:
        try:
            check_distribution_normalization(mutated_kernel, mutated_receipt)
        except ValueError:
            rejected += 1
        else:
            raise AssertionError("a changed normalization input was accepted")
    return rejected


def stable(row):
    return {key: value for key, value in row.items() if key != "seconds"}


def main():
    if not __debug__:
        raise SystemExit("Run mathematical verification without python -O.")
    kernel_bytes = Path(replay.cert.__file__).read_bytes()
    receipt = json.loads(Path(__file__).with_name("third_receipt.json").read_text())
    normalization = check_distribution_normalization(kernel_bytes, receipt)
    rejected_normalizations = check_normalization_fault_rejection(kernel_bytes, receipt)
    jobs = [
        ("3.18", ".728", ".671", ".583", ".44", ".19449", "push", 10000),
        ("3.44", ".721", ".663", ".584", ".50", ".4", "recursive", 10000),
        ("1.3", ".47", ".5", ".5", ".24", ".14310", "recursive", 10000),
    ]
    # A spawned interpreter must load the same exact menu without inherited
    # mutable globals; this is the portability risk the scratch driver had.
    with ProcessPoolExecutor(max_workers=1, mp_context=multiprocessing.get_context("spawn"),
                             initializer=replay.worker_sources,
                             initargs=(replay.cert.CHECKER_SHA256, replay.cert.MENU_SHA256,
                                       replay.DRIVER_SHA256)) as pool:
        spawned = pool.submit(replay.cert.verify_contact, jobs[0]).result()
    assert stable(spawned) == stable(replay.cert.verify_contact(jobs[0]))
    try:
        replay.cert.Family(F(4), F(".1"), F(".5"), F(".3"), "recursive", F(".5"), F(".5"))
    except ValueError as exc:
        assert "first lookup misses" in str(exc)
    else:
        raise AssertionError("a family missing first queries was accepted")
    try:
        replay.cert.make_receipt([spawned])
    except ValueError as exc:
        assert "incomplete menu" in str(exc)
    else:
        raise AssertionError("one contact was promoted to a complete menu receipt")
    resumed, rejected, accepted_leaves = 0, 0, 0
    with tempfile.TemporaryDirectory(prefix="subset-sum-third-recovery-") as directory:
        cache = Path(directory)
        for job in jobs:
            choice = replay.choice_of(job)
            completed, frontier = replay.paths(cache, choice)
            reference = replay.cert.verify_contact(job)
            if reference["nodes"] > 14:
                try:
                    replay.verify_cached(job, cache, checkpoint_nodes=7, stop_after_checkpoints=3)
                except InterruptedError:
                    pass
                else:
                    raise AssertionError("the deliberate interruption did not occur")
                assert not completed.exists() and frontier.exists()
                payload = replay.read_record(frontier, choice, "frontier")
                assert payload["state"]["nodes"] == 14
                assert payload["state"]["pending"]
                for key in ("checker_sha256", "menu_sha256", "driver_sha256"):
                    wrong = dict(payload, **{key: "0" * 64})
                    replay.write_record(frontier, wrong)
                    try:
                        replay.verify_cached(job, cache)
                    except ValueError as exc:
                        assert "fingerprint mismatch" in str(exc)
                        rejected += 1
                    else:
                        raise AssertionError("a mismatched hash was accepted")
                    replay.write_record(frontier, payload)
                # An interrupted atomic write must not replace the last good state.
                frontier.with_suffix(frontier.suffix + ".tmp").write_text('{"truncated":')
                resumed += 1
            result = replay.verify_cached(job, cache, checkpoint_nodes=7)
            assert stable(result) == stable(reference)
            assert stable(replay.verify_cached(job, cache)) == stable(reference)
            assert completed.exists() and not frontier.exists()
            accepted_leaves += result["leaves"]
    print(json.dumps(dict(status="PASS", branches=len(jobs), resumed_branches=resumed,
                          rejected_hashes=rejected, accepted_leaves=accepted_leaves,
                          source_normalization=normalization, rejected_normalizations=rejected_normalizations,
                          spawned_workers=1, rejected_incomplete_receipts=1, rejected_invalid_families=1,
                          scope="Recovery bookkeeping agrees with clean exact branch runs; not a whole-menu or analytic-proof check."),
                     sort_keys=True))


if __name__ == "__main__":
    main()
