# Executable outline and proof map for deterministic general matching

**Status:** mathematical algorithm specification for the current research
candidate. Subroutines below have explicit interfaces in the accompanying
notes and named public primitives. This is not executable software or
external verification. The target is exact maximum cardinality on every
undirected general graph.

## 1. One input preparation

Read the input, remove loops, retain one original edge ID for each
distinct nonloop pair, discard isolated vertices, and compact the
remaining graph G. This costs O(n+m) in the stated word-RAM model.
The empty graph returns its empty matching directly.

Optionally apply the exact matching-size kernel: endpoints of a maximal
greedy matching give a cover C; retain every C-C edge and at most |C|+1
outside neighbors per cover vertex. `matching_size_kernel_corollary.md`
proves exact optimum preservation, without knowledge of the optimum.
Every subsequent branch and acceptance check uses this same compact
exact-preserving graph. Original edge IDs remain passive output labels.

For a fixed parameter a, replace every degree-d vertex by an odd path
on 2d-1 vertices and attach its original edges to distinct odd ports.
Write r=|V(G)|, e=|E(G)|, A=2e-r and N=4e-r. The subcubic graph J
satisfies nu(J)=A+nu(G). Lift any greedy matching M to Q of size A+|M|.
The exact decoder and the proof for arbitrary gadget matchings are in
`general_graph_gap_reduction.md`.

## 2. The optimum-gap driver

Maintain an integer U with U>=nu(J)-|Q|. Initialize

    U=floor(r/2)-|M|.

Repeat while U>0:

```text
K <- ceil(U/2)
result <- GapPhase(J, Q, K, a)
if result is SUCCESS with g gains:
    Q <- its represented matching
    U <- U-g
else if result is LOW after i gains:
    Q <- its represented matching
    U <- K-1-i
else:
    suspend this parameter branch
```

LOW has the exact meaning nu(J)<q_start+K. Hence both updates preserve
the integer upper-bound invariant. There are O_a(log(r+2)) phases.
When U=0, materialize Q and decode it into a matching of G. No
perfect-matching decision search or promise is used.

## 3. A gap phase

Set C=a+1, L=ceil(10000CN/K), and
g_*=max(1,floor(K/(100C))). Start with unmatched vertices as singleton
bins, matched pairs in a paired remainder, no rows and no blockers.
All initial integral debts vanish. Top slacks are L-C>0.

Maintain the physical partition, immutable factor-critical records,
top numerical coordinates, and a+1 ledgers with floors C-j. Every
actual integral allocation has a persistent acyclic carrier. At each
settled state the bottom debt is zero, and its canonical assignment
and inverse are implicit point-query oracles.

At a settled state, take the first applicable action:

1. If a physical edge joins two different bins, query that pair.
   First use the deterministic output-sensitive tight-set detector.
   If it returns the inclusion-minimal tight set, contract it with
   its captive rows and save the creation-time witness. Otherwise
   free the two bins using the two-small-tree exchange, expose their
   joining-edge contacts, match along that edge, and remove those
   bins to the paired remainder. This is one gain.
2. Otherwise, if a bin has a contact to the paired remainder and
   cached top slack at least 4C, expand along it: the contacted
   vertex becomes a row and its mate a singleton child bin. Their
   old matching edge is the new row's assigned incidence.
3. Otherwise request a deterministic top priced step. Apply an
   accepted exact circulation and settle its notifications. LOW
   ends the phase with its gap conclusion. An invalid certificate,
   failed prerequisite or exceeded guard suspends the branch.

The g_*-th gain ends the phase immediately. Each other structural
action is followed by the reset transaction below. Pricing alone
does not change the integral ledgers or the physical partition.

## 4. One structural/reset transaction

Retain the pre-event bottom version as a frozen assignment oracle.
Use a sparse forward/inverse overlay for the event's assignment
changes. A pair exchange writes only its two O(L)-volume trees.
Contraction saves captive assignments before their rows disappear.
All assigned-row deletion decisions in this event use this same view.

Apply the exact structural ledger formulas. Top changes are one
old-to-final batch of positive settings, with its old provenance
available through retirement. Compute top residuals by the exact
identity y=s-p+Cw, without summing a large column's implicit entries.
Read old integral values before applying a whole allocation batch;
only then normalize its carrier by signed path pivots.

Advance ticks by one for an expansion or contraction and by L for
a repaired gain. For b_j=B^(a-j), choose the smallest j whose
pre-/post-event tick quotient changes.

For j=1, globally solve the exact integral exchange problem starting
from L on assigned incidences. For j>1, freeze the just-current
normalized parent j-1 for the ENTIRE local projection: all threshold
tests, capacities, locks and final exact-flow/cut recovery read it.

The projection returns an exact flow and, if needed, the full residual
bin set R. Apply all child allocation changes and all deletions,
including exterior load released by removed rows, before normalizing
the child. Preserved coarser ledgers receive their separate preserving
deletions. Fresh deeper ledgers share the final child's persistent
roots. Only after the transaction settles is the new bottom canonical
assignment published.

Historical row incidence lists include zero noncarrier incidences and
physical witnesses. Reused live bin representatives never overwrite
immutable old contraction or carrier records. A changed implicit
assignment does not globally rematerialize the physical matching.

## 5. Numerical calls and safe query consumption

`priced_logarithmic_steps_from_raw_cycles.md` reduces every logarithmic
client to a degree-three integer-priced graph with private port paths.
Choose one COMPLETE numerical route from `numerical_backend_choices.md`,
including its disconnected-component wrapper and the shared lifetime
interface. Every result is a list of real edges and occurrence-forest
paths with a literal traversal-length certificate.

Process a query's representation logs and consume or discard its result
in one transaction. Do not refresh prices between obtaining a path list
and applying it. A complete accepted step uses one common exact dyadic
coefficient on every piece. Individual partial path updates need not be
circulations; the completed list must be. Then service all queued
refreshes and client repairs before the next pricing call.

Signed increments and absolute motion have different counters. Every
dormant exposed real copy remains in coordinate sweeps. Retirement
transfers both counters before invalidating old metadata. Numerical
forests have one mutable history; integral carrier persistence is a
separate worst-case data structure.

## 6. Why the work is small, and what must still be true

The factor-critical proof is `factor_critical_contractions.md`. Exact
ledger/debt/erasure identities are in `ledger_algebra_and_phase_budget.md`.
Persistent normalization and implicit assignments are in
`persistent_integral_ledger_carrier.md`. The deterministic local pair
chain is `deterministic_local_tight_discovery.md`,
`balanced_forest_pair_oracle.md`, and `static_pair_exchange.md`.

`local_exact_projection_from_priced_steps.md` proves that each higher
reset changes only O(P) records and recovers the FULL residual cut.
`deterministic_phase_cost_and_guards.md` proves the complete sum:
structural volume O_a(N), objective-paid pricing, large-jump parent
debt, all reset padding, initialization and first incomplete attempts.
Conditional on the stated numerical interfaces, a phase costs
N^(1+O(1/a)+o_a(1)) with an absolute coefficient in O(1/a).

For one uniform program, interleave these finite parameter branches
with a classical deterministic branch. Charge every instruction,
allocation and final check within its branch. Validate each proposed
matching and perform one independent augmenting-path search before
acceptance, as specified in
`deterministic_uniformization_by_optimality_check.md`.

This proves the candidate fixed-epsilon and uniform envelopes only
if all the named mathematical contracts hold. Independent acceptance
guarantees correct output even if a fast branch fails; it does not
establish the improved running time. The classical branch supplies
termination and a fallback time bound in that case.
