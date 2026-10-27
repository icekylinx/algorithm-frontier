#!/usr/bin/env python3
"""Run the canonical repository validation and executable evidence suite.

The default run validates both contact receipts' code/menu bindings,
checks the third-lookup recovery path and recomputes the rho=1.7 and direct
two-level branches. Use --full-contacts to recompute all 62 two-level and
16 third-level branches instead. A receipt binding check is provenance,
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
        Check("Mathematical source formatting regressions", ("tools/check_math_formatting.py",)),
        Check("Static mathematical presentation regressions", ("tools/check_math_presentation.py",)),
        Check("Public prose mathematics uses SVG or literal code", ("tools/check_public_math.py",)),
        Check("Formula images and exact source bindings", ("tools/build_math_assets.py", "--check")),
        Check("Reviewed PDF source and artifact bindings", ("tools/build_papers.py", "--check")),
        Check("Selected TeX source exports", ("tools/build_manuscripts.py", "--check")),
        Check("Generated result and proof catalogues", ("tools/build_catalogue.py", "--check")),
        Check("ROABP exact source identities and publication edits", ("problems/roabp-affine-pit/verify/check_source_bindings.py",)),
        Check("ROABP native paper and visual-review bindings", ("problems/roabp-affine-pit/verify/build_native_papers.py", "--check")),
        Check("ROABP exact generator arithmetic and traversal semantics", ("problems/roabp-affine-pit/verify/all_rank_affine_orbit.py", "--self-check")),
        Check("Rank-one/full ROABP exact generator and separating-curve arithmetic", ("problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py", "--self-check")),
        Check("Exact interval-rank palette sharpness constructions", ("problems/roabp-affine-pit/verify/check_palette_sharpness.py",)),
        Check("Artin-ring reset and source-restart identities", ("problems/roabp-affine-pit/verify/check_artin_reset.py",)),
        Check("Quadratic Hasse obstruction determinant and residual identities", ("problems/roabp-affine-pit/verify/check_quadratic_hasse.py",)),
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
        Check("Preserved two-level Subset Sum scalar composition", ("tools/verify_subset_sum_scalars.py", "--base-two-level")),
        Check("Subset Sum theorem and headline ledger synchronization", ("problems/subset-sum-fast-deterministic/verify/check_headline_ledger.py",)),
        Check("Third-lookup contact receipt binding and coverage", ("tools/verify_subset_sum_third_contacts.py", "--receipt", "problems/subset-sum-fast-deterministic/verify/third_receipt.json")),
        Check("Third-lookup exact recovery and invalid-input rejection", ("problems/subset-sum-fast-deterministic/verify/check_third_recovery.py",)),
        Check("Exact contact replay checkpoint recovery", ("problems/subset-sum-fast-deterministic/verify/check_replay_recovery.py",)),
        Check("Scheduling quotas, buckets and six-profile coverage", ("tools/verify_profile_certificates.py",)),
        Check("Finite two-scenario hardness reduction", ("tools/verify_finite_reductions.py",)),
        Check("Allocation oracle barriers and residual configuration gaps", ("problems/allocation-lower-bounds/verify/check_barriers.py",)),
        Check("Finite sensitivity certificates", ("tools/verify_sensitivity_certificates.py",)),
        Check('Independent signed-flow certificates and binary-balance feasibility', ('problems/exact-flow-sensitivity/verify/check_flow_certificates.py',)),
        Check('Exact concurrent flow, shared setup and normalized Farkas separation', ('problems/selected-flow/verify/check_concurrent.py',)),
        Check('Recipient reservations and safe ordered-prefix exchanges', ('problems/recipient-matroid-configuration/verify/check_reservations.py',)),
        Check('Matroid union ranks and fractional recovery identities', ('problems/item-matroid-union/verify/check_union_reduction.py',)),
        Check('Exact product-feature packing summaries and original contexts', ('problems/packing-matching-summaries/verify/check_product_summary.py',)),
        Check('Sharp vertex-color failure activation certificates', ('problems/graph-color-failure-certificates/verify/check_vertex_colors.py',)),
        Check('robust-scenario-flow', ('problems/robust-scenario-flow/verify/check_scenarios.py',)),
        Check('robust-width-two-allocation', ('problems/robust-width-two-allocation/verify/check_width_two.py',)),
        Check('two-time-scheduling', ('problems/two-time-scheduling/verify/check_scheduling.py',)),
        Check('exact-failure-preservers', ('problems/exact-failure-preservers/verify/check_arborescence_reporting.py',)),
        Check('independent-transversal', ('problems/independent-transversal/verify/check_elementary.py',)),
        Check('robust-bounded-certificates', ('problems/robust-bounded-certificates/verify/check_bounded.py',)),
        Check('two-size-scheduling', ('problems/two-size-scheduling/verify/check_corank.py',)),
        Check('label-block-cut', ('problems/label-block-cut/verify/check_whole_blocks.py',)),
        Check('group-metric-constraints', ('problems/group-metric-constraints/verify/check_coset_compiler.py',)),
        Check("Exact unit-flow failure repair and compact reporting", ("problems/exact-flow-sensitivity/verify/check_unit_flow.py",)),
        Check("Native internally disjoint paths after one failure", ("problems/exact-flow-sensitivity/verify/check_vertex_paths.py",)),
        Check("Boolean-cap matroids and exact one-unit assignment gates", ("problems/one-value-exact-two/verify/check_one_unit_gate.py",)),
        Check("Matching kernels and subcubic reduction", ("problems/general-matching/verify/check_reductions.py",)),
        Check("Exact matching solver and independent certificates", ("problems/general-matching/verify/check_reference.py",)),
        Check("Simultaneous failed-search matching certificates", ("problems/general-matching/verify/check_certificate_search.py",)),
        Check("Matching cover compression and left-subset preservation", ("problems/general-matching/verify/check_cover_compression.py",)),
        Check("Degree-interval and cardinality reductions", ("problems/degree-constrained-subgraphs/verify/check_reductions.py",)),
        Check("Integral flow recovery and safe prefix initialization", ("problems/min-cost-flow/verify/check_recovery.py",)),
        Check("Persistent component labels and first coalescence", ("problems/incremental-scc/verify/check_label_history.py",)),
        Check("Clipped-tree intersections and simple-path reporting", ("problems/incremental-sssp/verify/check_path_reporting.py",)),
        Check("Matroid rank, one-failure weighted and value summaries", ("problems/matroid-failure-summaries/verify/check_summaries.py",)),
        Check("Nonrepresentable weighted-oracle obstruction", ("problems/matroid-failure-summaries/verify/check_weighted_obstruction.py",)),
        Check("Weighted oracle canonical-prefix construction", ("problems/matroid-failure-summaries/verify/check_weighted_prefix.py",)),
        Check("Sharp singleton-replacement prefix summaries", ("problems/matroid-failure-summaries/verify/check_single_replacement.py",)),
        Check("Sharp sparse-packing original-context restrictions", ("problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py",)),
        Check("Aggregate laminar lower-row reduction", ("problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py",)),
        Check(
            "Composite-group quotient rounding",
            ("problems/group-metric-constraints/verify/check_quotient_rounding.py",),
        ),
        Check('Bipartite phase matching and independent cover certificates', ('problems/general-matching/verify/check_bipartite.py',)),
        Check('Native degree constraints and certified cardinality optimization', ('problems/degree-constrained-subgraphs/verify/check_reference.py',)),
        Check('Capacity-bit scaling for the published exact-flow theorem', ('problems/min-cost-flow/verify/check_capacity_scaling.py',)),
        Check('Laminar dominant-weight recovery and binary rank oracles', ('problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py',)),
        Check('Two-positive-weight oracle and encoded-program boundary', ('problems/weighted-prefix-quota-frontier/verify/check_two_weight_lower.py',)),
        Check('Projected quota catalogues and compatible-cut orientation', ('problems/weighted-prefix-quota-frontier/verify/check_quota_extensions.py',)),
        Check('Signed support-sized interval and slack compilation', ('problems/boolean-linear-compiler/verify/check_interval_compiler.py',)),
        Check('Original-cardinality and modal interval compilation', ('problems/boolean-linear-compiler/verify/check_cardinality_compiler.py',)),
        Check('Fixed rank-loss contraction and all-prefix identities', ('problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py',)),
        Check('Optimal rank-two oracle summaries and exact-output lower bounds', ('problems/matroid-failure-summaries/verify/check_rank_two_prefix.py',)),
        Check('Actual-feature-rank modules and streamed persistence contractions', ('problems/persistence-failure-certificates/verify/check_feature_construction.py',)),
        Check('Universal mixed-failure matching kernels and independent certificates', ('problems/general-matching/verify/check_failure_kernel.py',)),
        Check('Native mixed-failure matching queries and certificate lifting', ('problems/general-matching/verify/check_failure_query.py',)),
        Check('Independent composite matching-query certificates', ('problems/general-matching/verify/check_failure_query_certificate.py',)),
        Check('Linear-size selector degree conversion and matching adapter', ('problems/degree-constrained-subgraphs/verify/check_linear_selector.py',)),
        Check('Canonical contact-rank crowns and physical optimum offsets', ('manuscripts/graph-backends/verify/check_odd_crown.py',)),
        Check('Exact demand trimming and arbitrary-rank support forests', ('manuscripts/graph-backends/verify/check_static_allocations.py',)),
        Check('whole-ground-allocation exact reference', ('problems/whole-ground-allocation/verify/check_selection.py',)),
        Check('arbitrary-processing-scheduling exact reference', ('problems/arbitrary-processing-scheduling/verify/check_profiles.py',)),
        Check('processing-bucket-tradeoff exact reference', ('problems/processing-bucket-tradeoff/verify/check_buckets.py',)),
        Check('correlated-spectral-regression exact reference', ('problems/correlated-spectral-regression/verify/check_importance_regression.py',)),
        Check('obstruction-boundaries exact reference', ('problems/obstruction-boundaries/verify/check_compact_body.py',)),
        Check('activated-machine-scheduling check_activation', ('problems/activated-machine-scheduling/verify/check_activation.py',)),
        Check('activated-machine-scheduling check_six_profiles', ('problems/activated-machine-scheduling/verify/check_six_profiles.py',)),
        Check('exact-failure-preservers check_matroid_reporting', ('problems/exact-failure-preservers/verify/check_matroid_reporting.py',)),
        Check('recipient-polymatroid check_counts', ('problems/recipient-polymatroid/verify/check_counts.py',)),
        Check('intrinsic-values-near-two check_intrinsic', ('problems/intrinsic-values-near-two/verify/check_intrinsic.py',)),
        Check('arbitrary-value-allocation-scheme check_scheme', ('problems/arbitrary-value-allocation-scheme/verify/check_scheme.py',)),
        Check('many-size-scheduling check_workload', ('problems/many-size-scheduling/verify/check_workload.py',)),
        Check('unrelated-values-joint-role check_joint', ('problems/unrelated-values-joint-role/verify/check_joint.py',)),
        Check('robust-unrelated-allocation check_robust', ('problems/robust-unrelated-allocation/verify/check_robust.py',)),
        Check('commitment-scheduling check_absorption', ('problems/commitment-scheduling/verify/check_absorption.py',)),
        Check('commitment-scheduling check_commitment_profiles', ('problems/commitment-scheduling/verify/check_commitment_profiles.py',)),
        Check('commitment-scheduling check_commitment_client', ('problems/commitment-scheduling/verify/check_commitment_client.py',)),
        Check('numeric-target-frontier check_targets', ('problems/numeric-target-frontier/verify/check_targets.py',)),
        Check('recipient-polymatroid check_fractional', ('problems/recipient-polymatroid/verify/check_fractional.py',)),
        Check('one-value-exact-two check_one_value', ('problems/one-value-exact-two/verify/check_one_value.py',)),
        Check('exact-flow-sensitivity check_signed_flow', ('problems/exact-flow-sensitivity/verify/check_signed_flow.py',)),
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
            "All 62 continuous contact branches",
            ("tools/verify_subset_sum_contacts.py", "--all", *parallelism),
        ))
        suite.append(Check(
            "All 16 third-lookup continuous contact branches",
            ("tools/verify_subset_sum_third_contacts.py", "--all", *parallelism),
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
        help="recompute all 62 two-level and 16 third-lookup branches instead of the default selected replay",
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
        f"Continuous contacts: {'all 62 + 16 branches' if args.full_contacts else 'rho=1.7 and direct branches, plus third-lookup recovery'}; "
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
