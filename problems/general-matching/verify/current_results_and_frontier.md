# Verification note

**Curated source path:** `sources/checkpoint-o/current_checkpoint/current_results_and_frontier.md`

The source audit follows.

# Current result and remaining frontier

**24 October 2026. Research checkpoint; uniform theorem candidate.**

## Current primary conclusion

The smallest current research-proof candidate is

\[
 O(n+m)+(m_s+1)\exp O\!\left(
   (\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}\right).
\]

The complete quantitative assembly is
`quantitative_matching_4_5_composition.md`, using
`sequential_expander_routing_tradeoff.md` and
`linear_parameter_static_sparsifier.md`.
The new structural/work separation is
log Gamma=O((p+r)log U) and
log F=O(U/p+U/r+r^2 log U+(p+r)log U).
The router has an actual virtual root, identity child inclusions,
one flattened physical embedding, explicit token trajectories,
and preprocessing paid once per actual host. Both witness queries
pay their full auxiliary-token volumes. The normalized route-table
and exact correction-circulation interfaces are retained.

The new hierarchy uses the self-contained
`half_matching_entropy_progress.md`, with balanced-cut threshold
at most 1/8 and all repeated matching occurrences retained. It does
not use the source's larger-threshold per-round entropy calculation.
Its cut player, leaf circuits, hierarchy, and query all have explicit
sequential work arguments; a distributed round count is not used as
a sequential algorithm.

The corrected coverage interface is in
`explicit_virtual_cut_balance_wrapper.md`. Weak spectral leaves now
stop removals at beta=1/1000 of their OWN original input, matching
the internal weak-success guarantee. The strong wrapper removes
disjoint current-host cuts until their union first reaches one
quarter, or retains the one final successful hierarchy. It proves
both the required balanced cut and more-than-two-thirds success
coverage. A former bare three-quarter weak leaf was insufficient
after earlier wrapper removals. This correction changes only fixed
constants and does not change the displayed exponent.

An elementary optional incidence-fiber construction is proved in
`hypercube_port_adapter.md`. Its at-most-4m vertices and
O(m log m) edges have conductance phi/O(log m). The corresponding
polynomial-logarithmic root-degree cost is already paid, so it
removes a local explicit-expander-family dependency without changing
the quantitative envelope.
The optional balanced witness in `hypercube_weighted_witness.md`
uses the same elementary cube inequality. It replaces a constant
witness degree multiplier by an explicit O(U) multiplier, and proves
that both query inventories and weighted ambient selection absorb it
in the existing polynomial factors.

`uniform_source_interfaces_for_4_5.md` makes the surviving source
contracts explicit. It uses the conservative log-squared center
count and the aspect-dependent weighted forest inventory; it does
not invoke the old complete KMPG theorem at the new inadmissible K.

The finite-arithmetic tree construction is now explicit in
`an_weighted_finite_bit_adapter.md`. Its exact weighted portals,
static petal metric, midpoint cut tests, and inherited target paths
preserve the retained geometric induction. The separate
`polynomial_bit_stretch_stable_forest_integration.md` proves an
acyclic stored-label bound: only original-edge tree path sums are
exported, so their bit growth is additive per numerical level.
Fixed polynomial dependence on the input bit count consequently
fits the current quantitative envelope.

Rounded parameters p=r=t, K=t^2, log k=ceil(U/t),
t=floor((U/ceil(log_2(U+4)))^(1/5)) pay the full quality term
(U/log k)K log Gamma. The input scope remains arbitrary undirected
general graphs, and the output is an explicit exact matching with
original edge IDs. This remains a research-proof candidate with named
dependencies, not an established public theorem or externally certified
implementation. The verifier protects accepted output; it does not
prove the fast running time.

## The preceding independent 5/6 construction

Here independence concerns the routing and static-provider construction.
The matching ledger, raw numerical backend, and several source interfaces
are shared with the 4/5 assembly.

The preceding independent research candidate is

\[
 O(n+m)+(m_s+1)\exp\!\left(
 O\!\left((\log(m_s+2))^{5/6}
          (\log\log(m_s+4))^{1/6}\right)\right).
\]

It is assembled in `quantitative_matching_5_6_composition.md`.
The new static construction is
`length_free_ambient_static_sparsifier.md`, using
`deterministic_token_routing_by_thresholds.md` and
`deterministic_weighted_path_selection.md`. Its source path oracle
and degree bands are reconstructed in
`separated_static_sparsifier_parameters.md` and
`parameterized_expander_path_and_degree_bands.md`.
The dynamic normalization interface is proved in
`normalized_projected_route_composition.md`.

This construction applies to arbitrary undirected general graphs and
returns an explicit exact maximum matching with original edge IDs.
No perfect-matching, bipartiteness, density, or regularity promise is
used. The existing physical degree reset, flat-tree pools, exact
projection recovery, binary ledger driver, and final independent
matching check remain the specified components.

The output/work separation is retained:
log Gamma=O(q r log U), while
log F=O(U/q+U/r+r^2 log U+q r log U).
The new argument normalizes EACH supplied ambient edge image to a
simple path, then deterministically selects one weighted witness route
from explicit token alternatives. Its ambient congestion is
Gamma(C+Delta), without a path-length multiplier. The guarantee uses
the returned NORMALIZED table, not an unchanged nonsimple input image.
The full path-list work and the correction circulation for the new
route remain charged.

Thus local repair work is Gamma^O(K), while selected recourse remains
a fixed power of rho Gamma poly(U). The full raw-quality term
(U/log k) K log Gamma remains present. Rounded parameters
q=r=t, K=t^2, log k=ceil(U/t),
t=floor((U/ceil(log_2(U+4)))^(1/6)) give the displayed rate.
This route uses the reconstructed CS21 decremental path oracle;
it does not use a sequential interpretation of CHS distributed routing.

This is a research-proof candidate, not an established public algorithm
or an externally certified result. Exact verification protects accepted
output and the classical branch ensures termination; neither proves
the claimed fast time. The latter depends on all named mathematical
source, reconstruction, lifetime, and numerical contracts.

## The preceding 6/7 construction

The independently retained 6/7 envelope, with log-log power 1/7,
is in `conditional_matching_6_7_composition.md`. It separates the same
output and construction-work factors, but retains the literal ambient
input-path-length congestion multiplier and therefore has local work
Gamma^O(K^2). Its source reconstruction and proof remain available.
The new 5/6 construction changes that dependency by a separate token
routing and sparse-selection argument; it does not retroactively
remove a factor from the source theorem.

## The preceding 14/15 construction and retained alternatives

The preceding explicit envelope is supplied by the degree-reset
distance backend in `distance_degree_reset_candidate.md`, the exact
recovery in `near_feasible_rounding_and_exact_projection.md`, and the
complete composition in `quantitative_matching_14_15_composition.md`.
Conditional on the named mathematical component proofs, it proposes
the single-program bound

\[
 O(n+m)+(m_s+1)\exp\!\left(
 O\!\left((\log(m_s+2))^{14/15}
          (\log\log(m_s+4))^{1/5}\right)\right).
\]

The new recursion restores degree three after each selected,
degree-controlled sparsifier. Its accounting separates propagated
selected-edge recourse from more expensive local demand-route work.
The latter is paid locally, not once per recursive level. Stable root
pools, actual resident histories, fixed bit caps and raw traversal
lengths remain explicit parts of the proposed interface.

A cleaner outer parameterization is proved in
`decoupled_numerical_client.md` and
`binary_ledger_hierarchy_and_decoupled_parameters.md`. With
`S=2^s`, it sets `a=s`, uses binary ledger reset periods, and chooses
accuracy from the backend cap `E_*` directly. Its full cost is
`S E_*^4 poly(s)`, giving the same displayed envelope. It needs only
two fixed backend constants in the instruction portfolio. Exact
near-feasible rounding and a final flow/cut pair replace every fresh
static max-flow recovery call, including level-one resets.

The independent Route A envelope remains `167/168` with log-log power
`1/4` in `sharp_log_parameter_portfolio.md`. Its separate metric and
real-edge provenance proofs are retained. The earlier `209/210` and
`335/336` calculations likewise remain separate and readable. All
these statements are research-proof candidates with unrestricted
input scope. Independent final checking protects output correctness
rather than proving the faster running time.

The preceding uniform proof assembly remains
`uniform_general_maximum_matching.md`, built on
`persistent_carrier_general_matching.md` and
`persistent_integral_ledger_carrier.md`. It proposes one uniform
deterministic program for explicit exact maximum-cardinality matching
on arbitrary general graphs in

\[
 O(n+m)+(m_s+1)^{1+o(1)},
\]

with original edge identifiers, where `m_s` counts distinct nonloop
edges. The elementary matching-size kernel gives the corresponding
bound with `m_s` replaced inside the second term by
`min(m_s,nu^2)`. The fixed-parameter theorem remains another useful
formulation: for every prescribed fixed `epsilon>0`, its branch has
time `O(n+m)+O_epsilon((m_s+1)^(1+epsilon))`.

This is a proof assembly importing the specified deterministic OAI
state framework, reconstructed projection/client proofs, and a complete
constructive numerical chain in `numerical_backend_choices.md`.
Both routes now have explicit disconnected-component accounting in
`disconnected_routing_components.md` and
`disconnected_component_backend_wrapper.md`. The literal source
O(m/k) total spanning-forest component count is not used on arbitrary
disconnected inputs.
It is not an external verification of the OAI
manuscript or an implemented running-time benchmark.

Uniformity does not follow merely from the family of fixed-exponent
bounds. The additional argument is an instruction-level interleaving
of one computable parameter family, with an independent deterministic
augmenting-path search checking each proposed matching. A classical
branch ensures termination and bounds actual allocated memory. Every
candidate check is charged inside its branch budget. For every fixed
positive exponent slack, one fixed fast branch eventually meets it;
the same interleaved program therefore has a common `1+o(1)` envelope.

The final check protects the correctness of accepted answers. It does
not prove the fast branches' performance: a hidden error in their
structural or numerical proof would leave only the classical fallback
time justified. The full reasoning is in
`deterministic_uniformization_by_optimality_check.md`.

## What removed the previous exponent bottleneck

The earlier direct composition had structural phase cost

\[
 \widetilde O\left(N+\frac{N^2}{bL}+Nb\right),
\]

and its optimized epoch parameter gave `N sqrt(K)`. Balancing this
against an original-graph blocking warm start gave the `n^(1/3)`
overhead recorded in the previous checkpoint.

The new method represents every actual integral ledger as a
persistent acyclic carrier. It retains zero carrier edges, so a
single long cycle cancellation does not require enumerating every
coordinate that becomes zero. A sparse final-coordinate batch
causes only linearly many tree pivots. A canonical row assignment
is accessed implicitly from the carrier, and small selected trees
exist at every settled state. Each gain therefore pays `O(L)`
up to logarithms, while contractions remain output-sensitive.
The global epoch term disappears.

The distinction from earlier failed private-guide attempts is
substantive: the normalized allocation is the actual integral
ledger that the next projection reads. A separate prescribed
allocation is not retained alongside it.

## Valid obstacles and why they do not refute this construction

| Earlier obstruction | Exact scope | Resolution used here |
|---|---|---|
| Sparse increments can make a private rounded entry negative | Applying updates intended for one vector to a different shadow vector | Apply a whole batch to the actual parent ledger before any normalization |
| Exact positive support can have linear recourse | Explicitly listing all support entries becoming zero/nonzero | Retain zero forest edges and update a long path implicitly |
| Pair-freeing injection may not correspond to any feasible flow basis | Requiring the temporary gain assignment to be the transportation basis | Use a local injection overlay for the immediate gain; publish a new canonical injection only after projection settles |
| Bulk removal of small selected trees creates quadratic top debt | Deleting complete carriers instead of the source gain bins | Remove only the original two gain bins and the source projection peel |
| A carrier reroot may change many assignments | Requiring an explicit update list for the global assignment array | Forward and inverse assignments are persistent point queries |
| Branching can reuse an amortized dynamic-tree potential | Applying mutable splay bounds to arbitrary old-version forks | Use a worst-case dynamic-tree implementation and a persistent RAM simulation |
| A peel can hit many anchored pieces while having zero deficiency | Charging anchored pieces as if each had a distinct free root | No multilevel anchored-core rebuild is used |

The files recording these examples remain useful interface warnings.
They are not lower bounds for maintained general matching and do not
contradict the current representation.

## Remaining frontier after uniformization

1. **Two explicit numerical routes.** The alias reconstruction now
   combines with `constant_degree_steiner_bridge.md`. It moves retained
   edges back to their original endpoints, compresses their connecting
   parent-tree paths, and uses bounded port fibers and per-input-edge
   path pools. It therefore invokes the cover/HRG primitives only at
   degree three and avoids an unexplained high-degree fiber collapse.
   The distance route begins with the local arbitrary-degree
   interfaces and literal squared-degree bounds in
   `distance_backend_general_matching_integration.md`. Its newer
   `distance_degree_reset_candidate.md` restores degree three between
   levels and gives the explicit `14/15` rate. Its expensive
   demand-route work remains local only under the precise retained-edge
   provenance and propagated-recourse arguments stated there.
   Both routes give raw-length, stable-image and edit-accounting
   arguments, including their separate component wrappers. The
   distance wrapper uses registered empty-loop embeddings and native
   core splits, so many formerly internal loops do not cause a k
   factor in recursive edit counts. Neither independently reimplements or externally
   verifies the source primitives. Their shared OAI client remains
   a separate proof dependency.
2. **Numerical implementation and constants.** The proof imports
   full constructive dynamic routing/minimum-ratio reductions.
   An implementation would need those algorithms, exact word
   bounds, and occurrence retirement machinery, not merely a
   callable ratio oracle. The candidate bound says little about
   practical constants. The uniform program proves an asymptotic
   envelope. The explicit rates above still provide no useful
   practical crossover estimate: the fixed constants and eventual
   cutoffs can be enormous. Further asymptotic improvements require
   stronger numerical interfaces or sharper quantitative composition.
3. **Independent scrutiny of the complete proof.** The OAI source is
   model-produced research with varying verification status.
   The present work now gives standalone proofs of factor-critical
   witnesses, ledger algebra, local exact projection, the priced client
   and the full phase-cost/guard sum. It does not establish that all
   source arguments or these reconstructions
   have received external mathematical verification.

The standalone carrier theorem is in
`dynamic_integral_allocation_theorem.md`. Its full persistent interface
versions zero noncarrier incidences as well as the carrier: a deleted
zero incidence can change a Hall obstruction while leaving every
allocation and carrier edge unchanged. This costs only the already
charged sparse topology updates. The new numerical constructions also
use observed pool doubling and cumulative, rather than per-batch,
recourse guards; the latter matches the source's amortized contract.

The primary checkpoint result applies to arbitrary density and
arbitrary general graphs. Regular, bipartite, approximate, maximal,
or communication-only algorithms have not been used as substitutes
for that target.

### A precise boundary for a further greedy improvement

[The ambient bulk-deactivation obstruction](ambient_bulk_deactivation_obstruction.md)
gives a static failure of one attempted ambient-aware repair: cap the
loads of loop-erased ambient routes, then deactivate every selected
native edge whose fixed image crosses a saturated resource. It can
retain \(\Omega(n^2/\gamma)\) selected IDs with threshold
\(\Theta(\gamma(C_0+\Delta))\), although every active native graph is
a tree. The example also has a degree-three ambient representation
with logarithmic-length simple input paths. This is a boundary of
that specific rule, not an impossibility theorem for stronger ambient
selection, a lower bound for general matching, or an asserted
trajectory of the numerical initializer. A successful further
improvement still needs compatible sparse selected support,
ambient congestion, propagated recourse, and cumulative cycle quality.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
