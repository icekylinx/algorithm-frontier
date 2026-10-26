# Verification and proof scope

## Ready for review: executable exact matching

The [standard-library reference solver](../reference/README.md) returns
an exact maximum matching and original edge IDs. Normal and certificate
modes use `O(n+m log(m+2)+sum_i nu(G_i)^p_i)` operations, where `p_i=5/2`
for a bipartite first kernel and `p_i=3` otherwise. Every originally
bipartite input component receives the improved bound. The
[cover-compression proof](../reference/cover-compression-proof.md) derives
smaller final solve graph while keeping certificates on the original edge
kernel. The [bipartite proof](../reference/bipartite-proof.md) establishes
the nonrecursive Hopcroft–Karp phases, matching-number time bound and
linear vertex-cover certificate. The
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
python3 -B problems/general-matching/verify/check_bipartite.py
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
follow. It also verifies the general matching optimum, the <code class="math">\min\{2c,3\nu\}</code> vertex
cap, the matched-edge bound on certificate contractions and explicit
rejection of an invalid cover. The full solver check includes a connected
420-vertex graph reduced to 40 bipartite solve vertices, with its certificate
independently verified on the 420-vertex first kernel.

The dedicated bipartite check compares all 74,963 graphs with at most four
vertices on each side with an independent matching oracle, plus 300
seeded cases in two side/adjacency orders. It verifies the matching,
minimum cover, phase-count bound and one final failed BFS per call.
Eight rejection checks and six native/branch/long-path cases include
a second-phase path containing 2,400 matching edges. Both public kernel
modes use the unchanged independent certificate verifier; a nonbipartite
original graph with a bipartite first kernel checks the exact dispatch
condition. The standalone checker refuses `python -O`.

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

## Universal mixed-failure compression and certificates

The [complete layered proof](../reference/fault-tolerant-cover-compression.md)
has a [constructor](../reference/failure_kernel.py) and an
[independent universal verifier](../reference/verify_failure_kernel.py).
The verifier checks the neighbor reduction and a matching with an equally
large vertex cover at each residual crossing layer. Acceptance proves
all permitted failure queries simultaneously, without enumerating those
queries or running a matching search.

```sh
python3 problems/general-matching/verify/check_failure_kernel.py
```

The [checker](check_failure_kernel.py) uses independent subset dynamic
programming on 76 exhaustive graphs through four vertices and 48 seeded
larger graphs. It checks all covers, both nontrivial edge orders and
budgets zero through two in the exhaustive domain, including every
charged outside-vertex/crossing-edge failure and every cover subset.
Arbitrary cover-vertex and cover-internal-edge deletions are uncharged.
The completed run covers 3,950 certified kernels, 3,295 maximum layers,
16,451 charged scenarios, 158,734 left-subset ranks and 727,954 general
matching comparisons.

Sixteen star instances attain the two separately scoped vertex bounds.
Two examples use the budget <code class="math">10^{1000}</code> without allocating a budget-sized
universe. Native integer/string IDs, omitted and explicit-null IDs,
26 certificate corruptions, 17 constructor rejections and nine verifier
input rejections are covered. A real constructor/verifier CLI roundtrip
under `python -O` accepts valid output and rejects tampering and loops.
The general theorem covers arbitrary graph attachments through the cover;
its proof follows from the all-left-subset identity and does not require
enumerating those contexts.

## Ready for review: the deterministic four-fifths construction

The main proof assembles the matching reduction, integral-ledger carrier,
local tight discovery, cycle-search hierarchy and final optimality check.
[Theorem 11.6](../proof.md#116-deterministic-cycle-search-realization)
instantiates the five interfaces from their detailed checkpoint proofs:
raw traversal quality, chronological initialization and repair, signed and
absolute retirement, finite-bit original-edge trees, and constants uniform
in the growing parameters. Its table lists suppliers, applicable ranges
and costs; Section 12 proves the resulting four-fifths bound. The named
published source results remain ordinary mathematical dependencies.

The repository's finite checkers execute the polynomial reference package
and local reductions. They do not execute the full fast hierarchy. This
implementation limit does not turn the supplied mathematical construction
into an open premise. End-to-end code and performance validation for the
fast hierarchy remain future work.

Verifying a matching and a Tutte–Berge witness establishes the optimality
of that output, independently of the research hierarchy. It does not
establish a running-time bound. The theoretical portfolio similarly uses
its independent augmenting-path check only for acceptance; the favorable
fast branch is justified by the construction and its first-failure
argument. The [source history](../sources.md#checkpoint-provenance) also
distinguishes the earlier <code class="math">4\nu</code> kernel proof from
the current implementation and tests.

Read the [main proof](../proof.md) with its [source map](../sources.md). Repository checks validate links, mathematical syntax and catalogue coverage; they do not certify the asymptotic theorem. No proof-assistant verification or external peer review is claimed.
