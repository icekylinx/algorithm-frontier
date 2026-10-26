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

## Conditional: the quantitative numerical client

The proof supplies the exact acceptance argument, finite-bit
potential arithmetic and reductions to the stated numerical graph backend.
The cap in its quantitative bound is the problem's numerical cap **S**;
substituting the graph-family size cap without the stated normalization would
change the claim.

Raw-cycle quality, chronological updates, copy retirement and the
finite numerical maintenance interface remain named premises of the
composition. The local recovery and artificial initialization proofs do
not discharge those backend requirements. Exact feasibility and optimality of a
returned flow are separate from a fast construction-time proof. No executable
implementation of the whole backend or flow algorithm is supplied.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
