#!/usr/bin/env python3
"""Run the canonical repository validation and executable evidence suite.

The default run validates the saved full-contact receipt's code/menu binding
and recomputes the rho=1.7 and direct continuous branches. Use --full-contacts
to recompute all 44 branches instead. A receipt binding check is provenance,
not an independent replay of the covered inequalities.

All checks use the Python standard library. The finite and numerical checks
have the scopes stated in their scripts and result-card verification notes;
passing this suite does not mechanically prove the asymptotic manuscripts.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Check:
    name: str
    arguments: tuple[str, ...]

    @property
    def command(self) -> list[str]:
        # Do not create bytecode artifacts; assertions remain enabled.
        return [sys.executable, "-B", *self.arguments]


def positive_integer(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def checks(full_contacts: bool, jobs: int) -> list[Check]:
    suite = [
        Check("Canonical problem structure", ("tools/validate_curation.py",)),
        Check("Evidence registry", ("tools/validate_reviews.py",)),
        Check("Scoped review statuses", ("tools/build_reviews.py", "--check")),
        Check("Import provenance and canonical targets", ("tools/check_provenance.py",)),
        Check("Internal links", ("tools/check_internal_links.py",)),
        Check("Result-card schema", ("tools/check_card_schema.py",)),
        Check("Mathematical delimiters", ("tools/check_latex_delimiters.py",)),
        Check("Portable mathematical notation", ("tools/normalize_math.py", "--check")),
        Check("Generated result and proof catalogues", ("tools/build_catalogue.py", "--check")),
        Check(
            "Low-space Subset Sum resource certificate",
            ("problems/subset-sum-low-space-deterministic/verify/check_resources.py",),
        ),
        Check(
            "Low-space Subset Sum structural identities",
            ("problems/subset-sum-low-space-deterministic/verify/check_structural.py",),
        ),
        Check(
            "Low-space Subset Sum range and convolution identities",
            ("problems/subset-sum-low-space-deterministic/verify/check_range_identities.py",),
        ),
        Check(
            "Short-range Subset Sum decisions and indexed witnesses",
            ("problems/subset-sum-low-space-deterministic/verify/check_range_solver.py",),
        ),
        Check(
            "Elementary exact fixed-point convolution",
            ("problems/subset-sum-low-space-deterministic/verify/check_exact_convolution.py",),
        ),
        Check(
            "Fast Subset Sum energy tensor identities",
            ("problems/subset-sum-fast-deterministic/verify/check_energy.py",),
        ),
        Check("Fast Subset Sum scalar composition", ("tools/verify_subset_sum_scalars.py",)),
        Check("Scheduling quotas, buckets and six-profile coverage", ("tools/verify_profile_certificates.py",)),
        Check("Finite two-scenario hardness reduction", ("tools/verify_finite_reductions.py",)),
        Check("Finite sensitivity certificates", ("tools/verify_sensitivity_certificates.py",)),
        Check("Matching kernels and subcubic reduction", ("problems/general-matching/verify/check_reductions.py",)),
        Check("Degree-interval and cardinality reductions", ("problems/degree-constrained-subgraphs/verify/check_reductions.py",)),
        Check("Matroid rank, one-failure weighted and value summaries", ("problems/matroid-failure-summaries/verify/check_summaries.py",)),
        Check("Nonrepresentable weighted-oracle obstruction", ("problems/matroid-failure-summaries/verify/check_weighted_obstruction.py",)),
        Check("Weighted oracle retained-prefix construction", ("problems/matroid-failure-summaries/verify/check_weighted_prefix.py",)),
        Check("Sharp sparse-packing original-context restrictions", ("problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py",)),
        Check("Aggregate laminar lower-row reduction", ("problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py",)),
        Check(
            "Composite-group quotient rounding",
            ("problems/group-metric-constraints/verify/check_quotient_rounding.py",),
        ),
        Check("Non-Fano obstruction", ("tools/verify_non_fano.py",)),
        Check(
            "Full-contact receipt binding and coverage metadata",
            (
                "tools/verify_subset_sum_contacts.py",
                "--check-receipt",
                "problems/subset-sum-fast-deterministic/verify/receipt.json",
            ),
        ),
    ]
    parallelism = ("--jobs", str(jobs))
    if full_contacts:
        suite.append(Check(
            "All 44 continuous contact branches",
            ("tools/verify_subset_sum_contacts.py", "--all", *parallelism),
        ))
    else:
        suite.extend([
            Check(
                "Fresh continuous contact branches at rho=1.7",
                ("tools/verify_subset_sum_contacts.py", "--rho", "1.7", *parallelism),
            ),
            Check(
                "Fresh direct continuous contact branches",
                ("tools/verify_subset_sum_contacts.py", "--branch", "direct", *parallelism),
            ),
        ])
    return suite


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--full-contacts",
        action="store_true",
        help="recompute all 44 continuous contact branches instead of the default selected replay",
    )
    parser.add_argument(
        "--jobs",
        type=positive_integer,
        default=min(4, os.cpu_count() or 1),
        help="parallel workers for continuous contacts (default: at most four available CPUs)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="print the exact commands without executing checks",
    )
    args = parser.parse_args()
    suite = checks(args.full_contacts, args.jobs)
    if args.list:
        for index, check in enumerate(suite, 1):
            print(f"{index:02d}. {check.name}\n    {shlex.join(check.command)}")
        return 0

    if not __debug__:
        parser.error("run without -O or PYTHONOPTIMIZE; mathematical assertions must be enabled")
    environment = os.environ.copy()
    environment["PYTHONOPTIMIZE"] = "0"
    environment["PYTHONUNBUFFERED"] = "1"
    started = time.monotonic()
    print(
        f"Running {len(suite)} canonical checks from {ROOT}\n"
        f"Continuous contacts: {'all 44 branches' if args.full_contacts else 'rho=1.7 and direct branches'}; "
        f"workers: {args.jobs}",
        flush=True,
    )
    for index, check in enumerate(suite, 1):
        print(f"\n[{index}/{len(suite)}] {check.name}", flush=True)
        print(f"$ {shlex.join(check.command)}", flush=True)
        check_started = time.monotonic()
        try:
            result = subprocess.run(check.command, cwd=ROOT, env=environment, check=False)
        except KeyboardInterrupt:
            print(f"\nInterrupted during: {check.name}", file=sys.stderr)
            return 130
        except OSError as error:
            print(f"\nCould not run {check.name}: {error}", file=sys.stderr)
            return 1
        elapsed = time.monotonic() - check_started
        if result.returncode:
            print(
                f"\nFAILED: {check.name} (exit {result.returncode}, {elapsed:.1f}s).\n"
                "Remaining checks were not run.",
                file=sys.stderr,
            )
            return 1
        print(f"PASS: {check.name} ({elapsed:.1f}s)", flush=True)
    print(
        f"\nAll {len(suite)} repository checks passed in {time.monotonic() - started:.1f}s.\n"
        "Each mathematical check retains its documented finite or analytic scope.",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
