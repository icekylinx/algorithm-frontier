# Verification and proof scope

## Ready for review: exact preprocessing

The unconditional reduction in Lemma 3.1 retains at most
$\binom c2+c^2$ edges for a computed cover of size $c$, with original
edge identifiers and exact matching preservation. Its cutoff $c$ is
sharp for arbitrary local neighbor choices. Corollary 3.1a applies the
same reduction componentwise. Lemma 3.2 gives the exact subcubic
odd-path gadget and a decoder for every matching, not only an optimum.

Run the independent finite checker from the repository root:

```bash
python3 -B problems/general-matching/verify/check_reductions.py
```

It uses exhaustive matching enumeration and dynamic programming to check:

- all 33,868 simple graphs through six vertices, in two fixed edge orders;
- all 76 simple graphs through four vertices after the subcubic reduction;
- the decoder inequality for all 42,721 matchings of those gadget graphs;
- three examples showing failure at cutoff $c-1$.
- all 5,188 mixed-failure cases in its stated through-four-vertex scope,
  with budgets one and two and both fixed edge orders, plus four
  examples showing the mixed-failure cutoff $c+f$ is sharp.

The [mixed-failure theorem](../../../manuscripts/graph-backends/matching-size-kernel-corollary.md#4-one-kernel-for-mixed-vertex-and-edge-failures)
is also ready for review. It concerns native edge/vertex deletions in a
fixed simple graph and one kernel that works simultaneously for every
allowed failure pair. It does not cover arbitrary correlated labels or
justify discarding parallel representatives before record-level faults.

The counts describe finite evidence. The displayed proofs establish the
general reduction statements; this script does not execute the fast backend.

## Conditional: the fast matching composition

The main proof assembles the matching reduction, integral-ledger carrier,
local tight discovery, graph hierarchy and final optimality check. The numerical
running-time conclusion remains conditional on the complete **Contract R** in
Section 11.6. In particular, quoting a static routing or sparsification theorem
does not supply all of its dynamic initialization, repair, notification and
retirement obligations.

The matching-size kernel and classical optimality certificate have their own
proofs. Verifying a returned matching and a Tutte--Berge witness establishes
optimality of that output; it does not certify the advertised fast construction
time. No end-to-end implementation or executable proof of Contract R is
included. Contract R's five clauses cover raw geometric comparison,
chronological recourse and initialization, occurrence retirement, finite-bit
tree realization, and uniform executable cap constants. All five remain
premises; passing the reduction checks removes none of them.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
