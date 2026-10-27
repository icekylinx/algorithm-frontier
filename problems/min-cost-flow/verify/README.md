# Verification and proof scope

## Ready for review: exact recovery and initialization

Section 11 gives a complete affine-penalty circulation-rounding proof.
Section 12 supplies arbitrary-demand initialization and distinguishes a
static infeasibility certificate from a current NO in an insertion
stream. Its lazy rule waits until every nonzero-demand vertex passes
the necessary incident-capacity test, then creates the artificial arcs
once. Their penalty uses the declared full-stream cost bound and fixed
threshold, so a YES witness has no artificial flow. Initial isolated
demands may become feasible later and are never rejected permanently.

Run from the repository root:

```bash
python3 -B problems/min-cost-flow/verify/check_recovery.py
```

The checker covers 2,437 exact rational recovery cases with loops and
parallel arcs, and 12,243 incremental prefix/threshold cases. The latter
include 5,058 deferred NO states and 1,090 NO-to-YES transitions. Small
flow optima are obtained by independent exhaustive enumeration. The
reference rounder explicitly scans paths; it does not implement or
certify the fast dynamic-tree running time.

## Ready for review: actual-size capacity scaling for exact cuts

The [capacity-bit reduction](../../../manuscripts/graph-backends/published-flow-capacity-scaling.md)
uses a published exact-flow algorithm only on capacities bounded by
each call's actual edge count. An old minimum cut bounds the missing
flow by the number of newly revealed one-bits. Truncating residual
capacities to that bound preserves every minimum-cut value. A distinct
negative-cost return arc converts the call to a bounded integral
circulation, and signed residual projection recovers the native flow.
For Gomory–Hu this gives an alternative route directly through a published
flow theorem; its five-sixths cost is absorbed by the six-sevenths forest
bound. The earlier four-fifths flow construction remains valid.

```bash
python3 -B problems/min-cost-flow/verify/check_capacity_scaling.py
```

The finite suite checks 8,512 input instances and 18,634 bit stages
against independently enumerated cuts. It exercises 26,859 reverse
residual records, 90,375 capped records, 361 zero-bit stages and 3,999
deliberate forward/reverse circulations. It separately enumerates
419,904 circulation assignments on 729 negative-return-edge instances.
Native cases include loops, parallel and opposite arcs, isolated
vertices, zero capacities and capacities longer than a machine word.
The test oracle is an ordinary integral augmenting-path solver; the
published fast flow theorem is an explicitly named external dependency.
Optimized Python execution is refused so assertions cannot be disabled.

## Ready for review: the quantitative numerical client

The proof supplies the exact acceptance argument, finite-bit
potential arithmetic and reductions to the stated numerical graph backend.
The cap in its quantitative bound is the problem's numerical cap `S`;
substituting the graph-family size cap without the stated normalization would
change the claim.

The generic client theorem is instantiated by the local
[quantitative backend construction, Sections 1–7](../../../manuscripts/graph-backends/quantitative-matching-4-5-composition.md),
[raw-lift proof](../../../manuscripts/graph-backends/distance-oracle-raw-lift.md)
and [lifetime construction](../../../manuscripts/graph-backends/numerical-backend-lifetime-and-loops.md).
Their proofs supply raw quality, chronological updates, copy retirement
and finite numerical maintenance with the named deterministic public
algorithms. The numerical client and these constructions form the
mathematical running-time proof. The finite recovery and capacity tests
exercise narrower reductions; no executable implementation of the whole
fast flow algorithm is supplied.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
