# Two constructive numerical routes for the general-matching candidate

**Research proof assembly, 24 October 2026.** The matching construction
needs one deterministic numerical backend with the interface below.
This note identifies two ways to supply it and the exact external
dependencies of each. Neither route is an implementation or an external
verification of the cited algorithms. The new arguments are mathematical
components of the present candidate.

**Disconnected inputs are accounted for explicitly.** A spanning forest
cannot have O(m/k) components on every graph. The primary route uses
`disconnected_routing_components.md`; the distance route uses
`disconnected_component_backend_wrapper.md`. These notes retain local
small-component information while proving the size of the actual
recursive input. The distance repair additionally requires constructive
empty-loop embeddings and native vertex splits. The impossible literal
total-component bound is not imported for arbitrary graphs.

The quantitative extensions of Route A are given separately in
`growing_depth_aspect_exploration.md`,
`hrg_routing_from_rounded_covers.md`, and
`master_hierarchy_209_210_exploration.md`. The newer metric variant in
`local_length_aspect_preservation.md` keeps length bits linear in
`log S` while charging gradient precision separately. Its conservative
composition is `quantitative_matching_167_168_composition.md`.
The constant-tuple choice in `sharp_log_parameter_portfolio.md` has
common backend factor
`exp(O((log S)^(167/168)(log log S)^(1/4)))`, and the same envelope
for matching overhead after a sufficiently large fixed outer constant.
Actual local initialization, restarts, occurrence records and finite-word
arithmetic remain charged. The parallel-edge map is constructed explicitly
in `snc_provenance_from_vertex_maps.md`.

These extensions reconstruct the parameterized HRG loops and tree family;
they do not substitute new parameters into the specialized constant-depth
corollary. Route B now has a separate growing-depth extension in
`distance_degree_reset_candidate.md`. It inserts degree-three port
fibers after selected degree control and separates local work from
propagated recourse. Its common factor is
`exp(O((log S)^(14/15)(log log S)^(1/5)))`.
The full conservative composition is
`quantitative_matching_14_15_composition.md`; the cleaner outer
parameterization is in `decoupled_numerical_client.md` and
`binary_ledger_hierarchy_and_decoupled_parameters.md`.
The remainder of this note also preserves the earlier constant-depth
interfaces as separate alternatives.

The preceding 6/7 Route B refinement reconstructs the static routing primitive
with separate OUTPUT and WORK parameters. Its proof is in
`separated_static_sparsifier_parameters.md` and
`parameterized_expander_path_and_degree_bands.md`. Combined with the
explicit clock and degree potential in
`amortized_static_base_distance_sparsifier.md`, it gives the research
candidate envelope
`exp(O((log S)^(6/7)(log log S)^(1/7)))`.
The complete quantitative composition is
`conditional_matching_6_7_composition.md`. It keeps the literal
ambient-input-path-length congestion factor, uses actual-size
initialization, and charges raw quality separately. It does not
substitute a larger repair depth into the older KMPG theorem.

The independent 5/6 refinement supplies a NEW normalized-route static
primitive in `length_free_ambient_static_sparsifier.md`. It uses
`deterministic_token_routing_by_thresholds.md` and
`deterministic_weighted_path_selection.md` to remove the ambient
path-length congestion multiplier after explicit input normalization.
`normalized_projected_route_composition.md` proves its compatibility
with the touched-set layers and exact correction circulations.
Local work becomes Gamma^O(K), and complete quality accumulation is
still charged. The complete research composition is
`quantitative_matching_5_6_composition.md`, with envelope
`exp(O((log S)^(5/6)(log log S)^(1/6)))`.
It does not import the separately investigated CHS hierarchy.

The current 4/5 refinement is a separately reconstructed sequential
router, in `sequential_expander_routing_tradeoff.md`, and its static
composition in `linear_parameter_static_sparsifier.md`. It has
log Gamma=O((p+r)log U), with local construction work
log F=O(U/p+U/r+r^2 log U+(p+r)log U).
The virtual hierarchy, polynomial local procedures, direct query
induction, and repaired half-matching entropy lemma are explicit
dependencies, not a distributed-round shortcut. The full composition
is `quantitative_matching_4_5_composition.md`, with envelope
`exp(O((log S)^(4/5)(log log S)^(1/5)))` and the same arbitrary
general-graph exact matching scope. All claims remain research
proof candidates; exact output verification does not certify time.

## 1. The common interface

For a fully dynamic degree-three graph of nominal size M, with positive
integral lengths and integral gradients of polynomial magnitude at a
fixed outer parameter, maintain an explicit forest of occurrences.
Every occurrence has a fixed physical vertex image during its lifetime;
every nonnull occurrence edge has a current physical edge ID and endpoint
correspondence. Null edges project to an empty physical walk.

A query returns a circulation as a short list of oriented physical edges
and occurrence-forest paths. Its denominator is a computable upper bound
on the sum of lengths of ALL physical traversals, before cancellation.
The numerator is its exact physical gradient. The approximation is to
the best gradient-to-norm circulation ratio. Representation insertions,
removals, and changes are explicit, and old records are retired before
their physical metadata becomes invalid.

For every sufficiently small fixed eta>0, the needed budgets are

* initialization at most M^(1+O(eta)+o(1));
* amortized input-edit and query work at most M^(O(eta)+o(1));
* occurrence multiplicity at most M^(O(eta)+o(1));
* raw ratio loss and output-piece count at most M^(O(eta)+o(1)).

The absolute constants in these exponents are independent of the outer
parameter. Choosing eta sufficiently smaller than 1/a meets the OAI
client's explicit margins. A value-only ratio oracle, a net-length
certificate, or a changing-image forest would not provide this interface.

## 2. Route A: degree-three routing and a geometric Steiner bridge

The relevant source is Chen, Kyng, Liu, Meierhans and Probst Gutenberg,
*Almost-Linear Time Algorithms for Incremental Graphs: Cycle Detection,
SCCs, s-t Shortest Path, and Minimum-Cost Flow*, arXiv:2311.18295v1:

<https://arxiv.org/abs/2311.18295v1>.

The new reconstruction uses its sparse neighborhood covers and
hierarchical routing construction only on their stated constant-degree
inputs. Theorem 4.1, Theorem 4.5, Definitions 4.28--4.30 and Lemma 4.32
are used at this scope. The dynamic spanner is Theorem 5.13.

The construction has three parts.

1. `portal_alias_api_reconstruction.md` supplies legal spanner updates
   for decreasing portal-leg lengths and retained crossing off-edges.
   The aliases have immutable scalar lengths and fixed origin labels;
   promotion shortens their valid physical lifts. The master degree,
   membership lifetime and update counts are proved explicitly.
2. `constant_degree_steiner_bridge.md` coalesces aliases of an original
   off-edge into one edge at its original endpoints. A compressed
   Steiner forest of the current parent tree routes all portal legs.
   This geometric graph has degree at most the degree of the particular
   routing-tree instance, which is subpolynomial for degree-three input.
3. A computably bounded port tree at each geometric anchor makes the
   recursive graph degree three. Long geometric paths are copied at
   INPUT-edge lifetimes and reused across child occurrence edits.
   Consequently no local piece-size factor multiplies recursive forest
   edit volume. Full retired null fibers are omitted from the physical
   export, so historical parent lifetimes do not accumulate congestion.

Positive null connector lengths are handled by scaling both real lengths
and gradients, then dividing BOTH the returned numerator and raw
denominator by that scale. The capacity factor is included in an
enlarged subpolynomial A. With k=M^eta and constant depth D=O(1/eta),
the proof has occurrence factor A^O(D), output length k A^O(D), and
work k^O(1) A^O(D). The precise local and initialization charges are
in the bridge and the general backend note.

This route therefore does not infer an arbitrary-degree vertex-occurrence
bound merely by collapsing a binary degree reduction. That would be an
insufficient argument: many split vertices could map to one physical
vertex. The geometric placement and per-input-edge pools are the
additional proof components used here.

The earlier `constant_depth_deterministic_backend.md` gives the general
constant-depth composition and raw-cycle repairs. Its original import of
the full constructive Theorems 3.3 and 3.4 is retained as a historical
alternative. For the reconstructed route, use the alias and Steiner
notes at that interface instead. This is a replacement proof of the
needed scoped interface, not a claim that the source states this exact
Steiner construction.

The arbitrary-forest portal decomposition counts only active pieces
and portals in the recursive graph. Zero-portal components remain
parent metadata and local fundamental-cycle candidates. The objective
of this tree-cycle subproblem is explicitly scoped to cycles T+e with
connected endpoints in T; the HRG comparison supplies such a candidate
for the original general-cycle problem.

## 3. Route B: an explicitly degree-sensitive distance sparsifier

The second chain is described in
`distance_backend_general_matching_integration.md`, supported by
`constant_depth_distance_oracle_backend.md` and
`distance_oracle_raw_lift.md`. Retained-edge gradients, direct
vertex pools and executable degree caps are proved in the integration
note itself; an older full-depth theorem-dependent calculation is not
needed by this conservative route.

The disconnected-component wrapper is a required part of this route.
Small initial components use whole low-stretch trees with a common
actual root in every forest. Logical local pivots and every initial
singleton edge path are included in the path-preservation family.
Positive core loops retain their input identities and empty metric
embeddings, while their cycle information is served locally. A native
core split can expose many former loops without generating that many
recursive edge edits. Actual child vertices are created at first
retained nonloop incidence and remain counted, even when isolated,
until the instance is disposed.

Its sources are:

* Kyng, Meierhans and Probst Gutenberg, *A Dynamic Shortest Paths
  Toolbox: Low-Congestion Vertex Sparsifiers and Their Applications*,
  arXiv:2311.06402v1, Theorem 3.1, Lemmas 3.5 and 3.21, and Algorithms
  2--5: <https://arxiv.org/abs/2311.06402v1>.
* Kyng, Meierhans, Probst Gutenberg and Sulser, *A Simpler and Faster
  Min-Cost Flow Solver via Min-Ratio Cycles from Distance Oracles*,
  arXiv:2609.23852v1, Lemma 4.1 and the Section 3 cycle dichotomies:
  <https://arxiv.org/abs/2609.23852v1>.

These local interfaces explicitly permit an arbitrary intermediate
maximum degree Delta. Use the conservative factor Delta^2 A, not a
sharper degree dependence from a later displayed hierarchy theorem.
At fixed depth choose a sufficiently large fixed spanner parameter;
the accumulated degree exponent is then arbitrarily small.

The lift uses copies of actual parent forest components. Each physical
vertex occurs in at most one component of each parent forest, giving
a direct vertex count that includes isolated and dormant occurrences.
A common observed capacity for all root pools is doubled when needed.
This handles new root identifications without guessing a hidden
asymptotic congestion constant or copying a whole component at each
root event.

The exact executable degree bounds, cumulative recourse guards and
restart periods are in the integration note. Recourse is checked over
the full prefix of each local instance, matching the amortized source
guarantee. A legitimate concentrated update is not rejected merely for
exceeding a per-update average. The period is at most n/k as required
by the source, rather than incorrectly using m/k on a high-degree input.

Frozen potentials are corrected on retained positive spanner edges
before contracting zero alias links. A loop uses its simple fundamental
cycle, and a selected short abstract circulation is decomposed into
simple cycles BEFORE it is lifted. These steps prove a literal-length
certificate; they do not rely on cancellation of a long implicit
physical walk. The local crude cycle-extraction loss is charged once,
at the first level selecting a local candidate, rather than at every
recursive level.

This route avoids the 2023 routing bridge. Its top-level numerical
dependency chain is different, but both routes may use overlapping
lower-level distance or spanner primitives. It also shares the outer
OAI client and the matching-side carrier construction with Route A;
agreement between the routes does not independently prove those shared
modules. The two component wrappers give the corresponding general-input
accounting within these explicitly constructive interfaces.

## 4. Common exact-flow and matching-side dependencies

The earlier local projection and first integral-level reset use exact
deterministic maximum flow on explicitly represented local networks.
The public primitive is van den Brand et al., *A Deterministic
Almost-Linear Time Algorithm for Minimum-Cost Flow*, arXiv:2309.16629v1,
Theorem 1.1 and its integral rounding construction:

<https://arxiv.org/abs/2309.16629v1>.

For capacities large relative to a small local network, use the binary
capacity-scaling argument in OAI Section 2: after doubling an old
maximum flow, the next optimal augmentation is at most the number of
arcs. Residual capacities may be truncated at that value. All digit
rounds and identifier translations are charged. This import solves
the directed auxiliary flow problem, not general matching by itself.

The new `near_feasible_rounding_and_exact_projection.md` replaces
these static-flow calls by the same priced client, cost-nonincreasing
cycle rounding, and ordinary residual searches. It proves both local
and all-expanded recovery. Every returned flow is exactly feasible
and paired with a checked cut. The fast-time proof still requires the
complete priced-step and raw-cycle contracts. This replacement removes
the older `17/18` static-flow overhead from the `14/15` composition.

Both numerical routes compose with:

* the OAI row/bin framework, with explicit reconstructed proofs in
  `factor_critical_contractions.md`, `ledger_algebra_and_phase_budget.md`,
  `local_exact_projection_from_priced_steps.md`,
  `priced_logarithmic_steps_from_raw_cycles.md`, and
  `deterministic_phase_cost_and_guards.md`;
* the actual integral-ledger carrier and frozen assignment transaction;
* the output-sensitive tight-set detector and local pair exchange;
* the exact odd-path optimum offset and general optimum-gap driver.

The matching side is stated in
`persistent_carrier_general_matching.md`. Its new allocation component
has a separate formulation in `dynamic_integral_allocation_theorem.md`.
The final common program is in `uniform_general_maximum_matching.md`.

The common finite lifetime and real-loop interface is
`numerical_backend_lifetime_and_loops.md`. The exact terminal cycle
routine is `small_graph_ratio_solver.md`; it uses rational separation
and negative-cycle detection with polynomial bit costs.

## 5. What the two routes establish, and what they do not

Either complete numerical chain is sufficient for the proposed
fixed-parameter phase bound N^(1+O(1/a)+o_a(1)). The structural proof
removes the previous epoch cost, and the exact gap driver gives arbitrary
general maximum matching. Independent final optimality checking and
instruction interleaving turn the computable family into the candidate
uniform bound

    O(n+m) + (m_s+1)^(1+o(1)).

The second route is useful because a problem specific to one numerical
construction need not invalidate both. It does not certify the shared
OAI dependencies or replace a full implementation. The explicit
convergence rates above still have unspecified fixed constants and
eventual thresholds. The final verifier certifies an accepted matching's
optimality. It does not certify the fast-time analysis.
