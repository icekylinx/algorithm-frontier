# Verification and proof scope

## Ready for review: executable exact matching

The [standard-library reference solver](../reference/README.md) returns
an exact maximum matching and original edge IDs. Normal mode uses
$`O(n+m\log(m+2)+\sum_i k_i^3)`$ operations, where $`k_i`$ is the
actual retained vertex count in input component $`i`$. Optional
certificate generation has the same bound, with
$`O(\sum_i k_i^2)`$ additional extraction work. The
[complete certificate-search proof](../reference/certificate-proof.md)
establishes the needed alternating-forest and odd-component invariants
without importing the Gallai–Edmonds decomposition theorem.

The [independent certificate verifier](../reference/verify_certificate.py)
checks native edge IDs, matching feasibility, the cover/kernel conditions
and a Tutte–Berge odd-component upper bound. Its full acceptance proof is
included in the reference documentation. It uses graph scans and comparison
sorting, never imports the blossom solver, and charges long labels and
certificate encoding by their actual size.

```bash
python3 -B problems/general-matching/verify/check_reference.py
python3 -B problems/general-matching/verify/check_certificate_search.py
```

The default suite compares 33,868 simple graphs through six vertices
against an independent subset-DP matching oracle, in both kernel and
full-graph modes: 67,736 certified solves. It also covers 152 native-record
instances and 260 larger seeded or explicit instances in both modes,
29 rejection checks, and three scale/CLI cases. All oracle comparisons
include independent certificate verification. Loops, parallel records,
isolates, mixed integer/string IDs, odd cycles, the Petersen graph and
invalid certificates are included. Randomness selects supplemental test
inputs only. The dedicated certificate-search check compares the actual
production function with deletion-defined exposability on all 33,868 simple
graphs through six vertices and 500 seeded graphs on seven through thirteen
vertices. It checks factor-critical blocks, unique external matched edges,
even alternating paths and tight odd-component counts. Two valid but
nonmaximum input matchings are rejected explicitly. The mathematical
checkers refuse `-O` execution.

This is finite implementation evidence and an independently checkable
optimality output. It does not verify the faster research implementation
or constitute a proof-assistant formalization.

## Ready for review: exact preprocessing

The unconditional reduction in Lemma 3.1 retains at most
$`\binom c2+c^2`$ edges for a computed cover of size $`c`$, with original
edge identifiers and exact matching preservation. Its cutoff $`c`$ is
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
- three examples showing failure at cutoff $`c-1`$.
- all 5,188 mixed-failure cases in its stated through-four-vertex scope,
  with budgets one and two and both fixed edge orders, plus four
  examples showing the mixed-failure cutoff $`c+f`$ is sharp.

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
running-time conclusion remains conditional on the complete deterministic
cycle-search implementation requirements in Section 11.6. In particular,
quoting a static routing or sparsification theorem
does not supply all of its dynamic initialization, repair, notification and
retirement obligations.

The matching-size kernel and classical optimality certificate have their own
proofs. Verifying a returned matching and a Tutte--Berge witness establishes
optimality of that output; it does not certify the advertised fast construction
time. The five outstanding requirements are circulation quality measured
before traversal cancellation, repair and initialization costs for every
operation prefix, complete retirement of edge copies, finite-bit tree
construction, and constants uniform in the growing parameters. The repository
does not yet provide an executable implementation meeting all five. The
polynomial reference solver supplies a usable exact algorithm with its own
bound and leaves those faster requirements unresolved.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
