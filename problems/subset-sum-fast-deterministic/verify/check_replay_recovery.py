#!/usr/bin/env python3
"""Exercise actual interruption/resume and reject mismatched recovery hashes."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile

import replay_contacts as replay


def stable(row):
    return {key: value for key, value in row.items() if key != "seconds"}


def main():
    if not __debug__:
        raise SystemExit("Run mathematical verification without python -O.")
    jobs = [
        ("3.29", ".664", ".56", ".50", ".20538", "push", 10000),
        ("1.7", ".47", ".5", ".40", ".18545", "recursive", 10000),
        ("1.3", ".47", ".5", ".24", ".14310", "recursive", 10000),
    ]
    resumed, rejected, accepted_leaves = 0, 0, 0
    with tempfile.TemporaryDirectory(prefix="subset-sum-recovery-") as directory:
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
                          scope="Recovery bookkeeping agrees with clean exact branch runs; not a whole-menu or analytic-proof check."),
                     sort_keys=True))


if __name__ == "__main__":
    main()
