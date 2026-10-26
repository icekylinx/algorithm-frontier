# Verification and proof scope

## Ready for review: executable exact matching

The [standard-library reference solver](../reference/README.md) returns
an exact maximum matching and original edge IDs. Normal mode uses
<code class="math">O(n+m\log(m+2)+\sum_i\nu(G_i)^3)</code> operations, where <code class="math">G_i</code>
ranges over nonempty normalized input components. Optional certificate
generation has the same bound. The
[cover-compression proof](../reference/cover-compression-proof.md) derives
the smaller blossom graph while keeping certificates on the original edge
kernel. The
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
python3 -B problems/general-matching/verify/check_cover_compression.py
```

The default suite compares 33,868 simple graphs through six vertices
against an independent subset-DP matching oracle, in both kernel and
full-graph modes: 67,736 certified solves. It also covers 152 native-record
instances and 260 larger seeded or explicit instances in both modes,
29 rejection checks, and four scale/CLI cases. All oracle comparisons
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

The dedicated compression check invokes the actual implementation on
68,236 covers, checks 70,578 possible maximum-crossing right endpoint sets
and 2,882,175 cover-subset ranks by independent subset dynamic programming.
Its exhaustive scope is all simple graphs through six vertices in both
fixed edge orders; 500 seeded graphs on seven through thirteen vertices
follow. It also verifies the general matching optimum, the <code class="math">2c</code> vertex
cap, the matched-edge bound on certificate contractions and explicit
rejection of an invalid cover. The full solver check includes a connected
420-vertex graph reduced to 40 blossom vertices, with its certificate
independently verified on the 420-vertex first kernel.

This is finite implementation evidence and an independently checkable
optimality output. It does not verify the faster research implementation
or constitute a proof-assistant formalization.

## Ready for review: exact preprocessing

The unconditional reduction in Lemma 3.1 retains at most
<code class="math">\binom c2+c^2</code> edges for a computed cover of size <code class="math">c</code>, with original
edge identifiers and exact matching preservation. Its cutoff <code class="math">c</code> is
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
- three examples showing failure at cutoff <code class="math">c-1</code>.
- all 5,188 mixed-failure cases in its stated through-four-vertex scope,
  with budgets one and two and both fixed edge orders, plus four
  examples showing the mixed-failure cutoff <code class="math">c+f</code> is sharp.

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
