# Deterministic Exact General Matching: Corrected 4/5 Checkpoint

**24 October 2026. Revised English mathematical checkpoint.**

This is a correctness revision of the earlier 4/5 archive, with additional
mathematical frontier results. The earlier archive is retained unchanged.
The principal candidate exponent remains 4/5; the revision does not claim
a new smaller matching exponent.

## Result and exact scope

The current research candidate is one deterministic program returning
an explicit exact maximum-cardinality matching on every undirected
general graph, with original edge identifiers, in time
\[
 \boxed{O(n+m)+(m_s+1)\exp O\!\left(
   (\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}\right).}        \tag{1}
\]
Here n,m count the original vertices and listed edges; m_s counts
distinct nonloop edges after one shared cleanup. Disconnected, dense,
nonbipartite, odd-order, and no-perfect-matching inputs are included.
No expansion, regularity, or density promise is imposed on the input.

The preceding independent checkpoint had logarithmic-overhead exponent
5/6 and log-log exponent 1/6. Equation (1) improves these to 4/5 and
1/5. These are exponents INSIDE the subpolynomial overhead, not a claim
of m^(4/5) time or an approximate matching.
The two assemblies share their matching-ledger and raw-backend
interfaces. Independence here refers to the different expander-routing
and static-provider constructions, not to every component of the
end-to-end matching proof.

**Status: research-proof candidate.** The new provider interfaces
have explicit constructions and proofs in this archive and were
independently reread during this research session. This is not an
established public theorem, external certification, or implemented
runtime benchmark. The complete time claim depends on the cited
public-source and reconstructed mathematical components.

Every proposed matching is checked by an exact deterministic
augmenting-path search. A classical exact branch receives a fixed
positive share of instructions. These safeguards protect accepted
output and termination; they do not prove the improved time.
Faster completion requires the favorable branch's mathematical proofs.

An optional exact kernel replaces m_s throughout the second term by
min(m_s,O(nu(G)^2)). Every worker and every candidate check then runs
on that compact kernel, and only the winning output is mapped back.

## Baselines checked

[public_baselines.md](public_baselines.md) records the primary sources
and a fresh search through 24 October 2026. The strongest unrestricted
deterministic exact sequential bound verified in that search includes
Goldberg--Karzanov's
\[
 O\!\left(m\sqrt n\,\frac{\log(n^2/m)}{\log n}\right)
\]
on its nontrivial input range, with ordinary input cleanup separate.
The search did not locate a published unrestricted deterministic exact
algorithm with (1). This is a search finding, not a nonexistence proof.

The OpenAI starting manuscript is
[Almost-Linear-Time Maximum-Cardinality Matching in General Graphs](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026).
Its official directory retains the historical word Sparse, but its
theorem covers arbitrary simple undirected graphs. The statement is
randomized: near-linear instructions on every random path and success
probability at least 2/3. That is not a deterministic success theorem.
[oai_baseline_and_imports.md](oai_baseline_and_imports.md) separates
the source framework, imported deterministic lemmas, and replacements.

Approximation, streaming passes, regular-graph results, bipartite
algorithms, and communication rounds do not replace the present target.

## The new mathematical improvement

For master logarithmic size U and h=Theta(log(U+4)), the older
independent 5/6 route has structural quality log Gamma=O(qrh).
The new sequential router and static construction have
\[
 \log\Gamma=O((p+r)h),\qquad
 \log F=O(U/p+U/r+r^2h+(p+r)h).                              \tag{2}
\]
F is construction work only. Gamma governs selected support,
congestion, explicit paths, and selected-edge recourse.

The proof is assembled in
[sequential_expander_routing_tradeoff.md](sequential_expander_routing_tradeoff.md)
and [linear_parameter_static_sparsifier.md](linear_parameter_static_sparsifier.md).
This is an explicit sequential reconstruction, not a conversion of
a distributed round bound by multiplying by the edge count.

## What this revision corrects

[explicit_virtual_cut_balance_wrapper.md](explicit_virtual_cut_balance_wrapper.md)
repairs a success-coverage boundary. A weak leaf retaining only three
quarters of its own host was insufficient after the enclosing wrapper
had already removed almost one quarter of its original host: the product
could be only 9/16, below the required 2/3.

Every weak success now retains at least 1-beta of its CURRENT input,
with fixed beta=1/1000. The strong wrapper removes disjoint weak cuts
until their union first reaches one quarter, or keeps one weak success.
At a cut exit the union is below 5/8, so complementation loses less
than 5/3 in sparsity. At a success exit more than 3/4 remains, and
(1-beta) times 3/4 is greater than 2/3. The proof counts a fixed
O(1/beta) number of weak calls and retains only the final successful
embedding. Exact root coverage uses a first-removal argument in the
promised physical expander. These changes affect fixed constants only.

[hypercube_port_adapter.md](hypercube_port_adapter.md) gives an optional
fully elementary incidence-fiber construction. It uses at most 4m
vertices and O(m log m) edges, with conductance phi/O(log m). The
already paid polynomial-logarithmic root-degree factors absorb the
change. A separate explicit constant-degree expander family is therefore
unnecessary for that local adapter.

[hypercube_weighted_witness.md](hypercube_weighted_witness.md)
also replaces the balanced weighted-witness family by a cube with
carefully rounded port groups. Its degree multiplier is O(U) and
inverse conductance O(U). The note explicitly recomputes both query
volumes and the weighted ambient load; it does not silently retain
the former constant degree multiplier. These fixed polynomial factors
preserve the same candidate envelope.

[uniform_source_interfaces_for_4_5.md](uniform_source_interfaces_for_4_5.md)
records the conservative center count, length-aspect-dependent forest
count, occurrence-weighted path inventory, and actual deterministic
source interfaces. In particular, the old complete KMPG theorem is NOT
invoked at the new growing repair depth. Its restricted parameter range
is replaced only by the independently specified repair construction.

[deterministic_symbolic_shortest_path_ties.md](deterministic_symbolic_shortest_path_ties.md)
gives an optional exact implementation of consistent shortest-path
ties. Canonical persistent signatures avoid both random perturbations
and one-bit-per-edge integer arithmetic. The bound is per source or
per actually explored truncated search, on a declared common length
grid; it is not an all-pairs or dynamic shortest-path claim.

[an_weighted_finite_bit_adapter.md](an_weighted_finite_bit_adapter.md)
supplies a finite-bit implementation of the retained low-stretch-tree
geometry. It uses explicit weighted portals, one static directed metric
for each petal, exact dyadic midpoint tests, and a separate assignment
of the working target and the recursive child's prescribed target.
It omits short-edge contractions and pays a fixed polynomial in the
input length bit count. Temporary portal coordinates are removed before
exporting an original-edge spanning tree.

[polynomial_bit_stretch_stable_forest_integration.md](polynomial_bit_stretch_stable_forest_integration.md)
then proves that this weaker, bit-dependent stretch is sufficient here.
An exported core length is a sum of only O(log^2 n) original-tree path
lengths. Its bit bound is independent of both the low-stretch factor
and the number of weighted forest calls. This yields the declared
O(Ut) stored-label bound before substituting the fixed polynomial
tree cost, so the numerical guard has no recursive bit-length
self-reference. Importance weights and reciprocal ordering use
integer arithmetic or one explicit dyadic grid.

[fresh_general_matching_client_interfaces.md](fresh_general_matching_client_interfaces.md)
reconstructs the other end of the chain: arbitrary optimum gap,
current-injection augmenting prefixes, frozen whole-batch ledger
updates, exact flow/cut recovery, and late recursive update credit.
It treats the complete raw backend as a stated hypothesis and keeps
the verifier separate from its performance obligations.

### Hierarchy and cuts

[virtual_expander_hierarchy_reconstruction.md](virtual_expander_hierarchy_reconstruction.md)
exports a virtual root on exactly the physical host vertices.
Children are literal induced subgraphs of the VIRTUAL root, and one
explicit map embeds that root in the physical host. Interior vertices
of embedding paths are not silently added to terminal sets.

[sequential_short_path_matching.md](sequential_short_path_matching.md)
and [sequential_fresh_cut_matching_adapter.md](sequential_fresh_cut_matching_adapter.md)
use explicit bounded-depth BFS, full-host fresh calls, summable
failure-cut budgets, and exact covering. Every returned cut is an
actual cut of its stated host; unmatched leftovers are accounted for.
Exact rational spectral elimination replaces exponential coarse-cut
enumeration.

A newly found source-proof issue is repaired explicitly in
[half_matching_entropy_progress.md](half_matching_entropy_progress.md).
With only half the smaller cut side matched, the original larger
cut threshold does not imply the printed per-round entropy increase.
The new construction uses threshold at most 1/8. It proves good mass
at least 5N/64 and entropy gain at least 5N/1024 per continuing round.
An executable 512 ceil(log_2(N+2)) cap follows. All repeated matching
occurrences remain distinct multigraph edges; deduplicating them
would invalidate the mass bound. The preceding 5/6 route uses full
matchings through a different source chain and is unaffected.

### Polynomial local procedures and explicit query paths

[polynomial_energy_cut_player.md](polynomial_energy_cut_player.md)
uses finite even moments and conditional expectations for the energy
cut. [sequential_leaf_routing_and_chs_work.md](sequential_leaf_routing_and_chs_work.md)
constructs short leaf matching paths with exact walk moments and
conditional expectations, then compiles bitonic circuit layers.
Both have fixed polynomial local work, including their arithmetic.

[conditional_full_router_from_shufflers.md](conditional_full_router_from_shufflers.md)
proves a direct scatter, meet, reverse, and exact-destination recursion.
It keeps real and dummy token paths explicitly. Its work is
n times the endpoint-load bound, including 2L dummies per vertex.
It does not assume a sparse-token-only query bound or reuse a global
best-leaf load parameter.

The final hierarchy is retained FIRST; shufflers and leaf circuits
are built afterward for its actual nodes. At one depth the virtual
host edge sets are disjoint. Union their primitive path families,
sum over depths, and apply the one root map once. This gives quality
phi^{-O(1)}log^{O(p)}n, with a fixed inverse-conductance power.
An already flattened embedding factor is not multiplied per level.

The actual branching parameter is
2^max(5,ceil(log_2(n+2)/p)). Leaves stop at a fixed polynomial in
that parameter and log n. This supplies all integer-routing guards
without padding small graphs or importing the source's distributed
epsilon restriction. Temporary matrix integers can exceed the
numerical backend label cap; their full multiword work belongs in F.

### Static normalized-route composition

Both witness directions pay the router's FULL query volume.
Forward load is O(phi^{-1}) on demand-band ports. Reverse load is
ceil(rho) on a weight-rho witness, whose total volume satisfies
sum m_W ceil(rho) <= O(m_J/phi). Expensive preprocessing is paid once
per actual host, never once per unit of load.

There are two distinct loop erasures: token routes in their immediate
host, and each input ambient edge image in its immediate ambient graph.
All use native lifetime IDs. Different aliases with equal eventual
physical images are not identified.

The output includes the normalized table Pi'. Sparse deterministic
weighted selection gives ambient congestion Gamma(C+Delta) without
an input-path-length multiplier. Full route-list work remains charged.
[normalized_projected_route_composition.md](normalized_projected_route_composition.md)
and [normalized_route_cycle_comparison.md](normalized_route_cycle_comparison.md)
preserve central IDs, actual route dependencies, exact correction
circulations e-R(e), and the raw numerical lift.

## Complete time balance

[quantitative_matching_4_5_composition.md](quantitative_matching_4_5_composition.md)
sets
\[
 t=\Theta((U/h)^{1/5}),\quad p=r=t,\quad K=t^2,\quad
 x=\lceil U/t\rceil,\quad k=2^x,\quad d=O(t).                 \tag{3}
\]
It pays construction work, repair work, propagated recourse, and
FULL recursive quality separately. In particular,
\[
 \log F=O(U/t+t^2h),\quad
 K\log\Gamma=O(t^3h),\quad
 d\log P=O(U/t+t^2h),\quad
 dK\log\Gamma=O(t^4h)\leq O(U/t).                            \tag{4}
\]
The last term is essential. Local quality is not substituted for
full-depth quality.

Stored length/gradient labels use O(Ut) bits. Larger local preprocessing
integers are charged separately. Constant-index caps, late initial
update credit, degree-reset fibers, raw occurrence pools, exact
near-feasible projection, and the binary-ledger matching client all
retain explicit work accounting. The final client cost is
S E_*^4 poly(log S), with log E_*=O((log S)^(4/5)(loglog S)^(1/5)).

## Additional results and the next exponent targets

The new frontier notes distinguish useful lemmas from complete matching
improvements.

* [Nonuniform fractional path selection](nonuniform_fractional_path_selection.md)
  extends deterministic sparse selection to arbitrary supplied rational
  path masses. Its positive arithmetic avoids constructing a huge common
  denominator merely to normalize a commodity's path probabilities.
* [Initial-route projection](initial_route_projection_updates.md) shows
  that local anchor-route scans can fit the existing work budget. Its
  projected endpoints undergo multi-origin relocations, so it does not
  inherit a native-split theorem automatically.
* [Central greedy support](central_greedy_recoursing_under_splits.md)
  has a small central-ID recourse bound under genuine splits. Its
  short-path existence does not supply fast route reporting or the
  required ambient congestion.
  [Congestion-capped greedy support](congested_greedy_support_and_dynamic_boundary.md)
  adds a positive static native-congestion lemma and a conditional
  split-recourse bound, but its unchanged support violates the needed
  additive ambient bound by a polynomial factor. The counterexample
  keeps both selected and immediate ambient maximum degrees at three
  and survives complete loop erasure.
  [The first-touched provenance example](projected_central_provenance_congestion_obstruction.md)
  realizes the same obstruction through legal native splits and
  prefix--own-central-edge--suffix images. Its initial table is a
  permitted table, not an asserted output of the current initializer.
  [Bulk ambient deactivation](ambient_bulk_deactivation_obstruction.md)
  tests a more direct repair: stop using every selected edge whose
  fixed image crosses a saturated ambient resource. An exact static
  example forces Omega(n^2/gamma) retained IDs at threshold
  Theta(gamma(C0+Delta)), even after loop erasure and with degree-three
  ambient graphs. This rules out that particular repair rule.
* [Recursive cycle quality](recursive_cycle_quality_obstruction.md)
  and [literal logarithmic client states](logarithmic_client_quality_obstruction.md)
  give explicit failures of an additive replacement for the present
  independent route-quality product. They do not rule out algorithms
  exploiting their actual route choices, reachable states, or a more
  powerful joint optimization. The latter note also proves a useful
  shortest-path bypass when the ordinary gradient is a vertex potential.
  [The actual-client limits](potential_bypass_limits_in_matching_clients.md)
  show why this useful special case is not automatic: a strong ordinary
  cycle is already present at literal exchange-client initialization.
* [Shared fractional path records](hhl_shared_path_dag_and_conditional_tradeoff.md)
  and [short-path extraction](compressed_fractional_path_extraction.md)
  supply representation adapters. The low-step flow provider's quantitative
  and arithmetic premises remain separate. Literal intermediate source
  problems are isolated in
  [the sequence and parameter note](hht_literal_sequence_and_parameter_boundary.md);
  none is imported by the current 4/5 construction.
* [Weighted spanner packing](weighted_spanner_packing_width_boundary.md)
  gives a positive aggregate-cost and deterministic selection calculation,
  but identifies the missing bound on an individual response's ambient
  load and on the union of its selected supports. It is an interface
  boundary, not an iteration lower bound.
  [The Chuzhoy--Parter comparison](chuzhoy_parter_2026_interface_boundary.md)
  checks a recent deterministic dynamic low-congestion spanner against
  the actual path, split, notification, and quantitative requirements.
  Its stated interface does not supply a replacement for the current
  ambient-route module.

[post_four_fifths_quantitative_targets.md](post_four_fifths_quantitative_targets.md)
calculates precise CONDITIONAL 3/4 and 2/3 targets. They require stronger
local quality or work interfaces and are not further matching bounds.
The current parameter-rebalancing, virtual-merge, and repair-window
obstructions identify why deleting a charged factor without a new
algorithmic argument would be invalid.

## What remains open and how to read the archive

[linear_router_backend_balance.md](linear_router_backend_balance.md)
proves that rebalancing the current charged expressions, even with
different parameters at different levels, cannot improve the 4/5
power or its 1/5 logarithm. This is an optimization boundary for the
stated proof envelope, not an algorithmic lower bound.

Further work is targeting the routing/preprocessing tradeoff,
propagated repair recourse, and accumulation of raw quality.
No smaller exponent is claimed by this checkpoint.

For a short reading order, start with this README, the full 4/5
composition, the sequential routing provider, the static provider,
and the entropy repair. Their links lead to component proofs.
Older 5/6, 6/7, and other assemblies are retained as separately scoped
alternatives; the smallest current result is stated here and in
[current_results_and_frontier.md](current_results_and_frontier.md).

The archive contains English mathematical notes only. It contains
no Lean, PDF, executable tests, experimental logs, or claim of formal
verification. Checkpoint container checks are not mathematical proof.
