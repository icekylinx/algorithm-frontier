# Review status and verification evidence

Readiness applies to the precise scope below. **Ready for review** means that the stated manuscript package has been checked for its theorem, proof, computational model and declared dependencies. **Partial readiness** identifies completed components of a larger family. Other manuscripts remain available with review pending. None of these labels claims external peer review or proof-assistant verification.

The machine-readable [registry](registry.json) is the source of these statuses and of each executable check's mathematical scope.

## Run the checks

```sh
python3 tools/check_repository.py
```

The default suite checks repository structure and every registered executable used by the canonical runner. For Subset Sum it validates the two-level and third-lookup receipts' source/menu bindings, checks both scalar ledgers and the recovery paths, and freshly replays the rho=1.7 and direct two-level branches. To cleanly replay all 62 two-level and 16 third-lookup branches:

```sh
python3 tools/check_repository.py --full-contacts --jobs 4
```

Receipt binding establishes provenance and coverage metadata; only recomputation re-establishes the inequalities. The full mode is also available through manual dispatch of the repository workflow. The [contact evidence note](../problems/subset-sum-fast-deterministic/verify/README.md) states the analytic coverage argument.

## Ready for review

### [Faster deterministic Subset Sum](../problems/subset-sum-fast-deterministic/)

The complete uniform deterministic integer Subset Sum and indexed-witness construction in Parts I–III: signed circuit compilation, finite exact seed search, trace aggregation, all inherited reductions, the preserved two-level result and the third-lookup extension. The final-source 62-branch and 16-branch evidence, finite contact-cone lemma, exact reflected envelope and all nine outer cost rates are separately accounted for.

**Dependencies and scope.** The finite input-independent startup constant has no practical numerical bound. Mathematical compiler proofs and exact continuous certificates have different scopes; neither is described as proof-assistant formalization or as a practical implementation of the compiled algorithm. The historical 18-contact presentation retains its explicitly stated numerical evidence boundary. The current 62-plus-16-branch theorem uses its own complete contact evidence and does not depend on that historical receipt.

[Proof](../problems/subset-sum-fast-deterministic/proof.md) · [Dependencies](../problems/subset-sum-fast-deterministic/sources.md) · [Evidence](../problems/subset-sum-fast-deterministic/verify/README.md) · Reviewed 2026-10-26

### [Low-space deterministic Subset Sum](../problems/subset-sum-low-space-deterministic/)

The complete general low-space theorem with writable-space exponent 0.18261635770550353, including the storage schedule, indexed witnesses and the one-bit deficiency-proxy charge. The separate two-short-range theorem includes signed normalization, nested residue streams and self-contained exact Boolean convolution.

**Dependencies and scope.** The stronger n/6-space result requires the supplied three-block partition and two short normalized ranges. The general theorem has no such input restriction. Executable finite checks cover their named identities and resource ledgers; they are not a full implementation or formalization of either asymptotic construction.

[Proof](../problems/subset-sum-low-space-deterministic/proof.md) · [Dependencies](../problems/subset-sum-low-space-deterministic/sources.md) · [Evidence](../problems/subset-sum-low-space-deterministic/verify/README.md) · Reviewed 2026-10-26

### [Deterministic general-graph maximum matching](../problems/general-matching/)

The complete deterministic four-fifths research theorem, including the cycle-search realization, raw quality and gradient lifting, chronological work, stable retirement, finite-bit realization and uniform search. The separate executable package includes exact matching, independent optimality certificates, the refined 3nu vertex count for the earlier compression, nonrecursive bipartite phases, and universal mixed-failure kernels with all-cover-subset and context preservation. Layer matching/vertex-cover witnesses certify every permitted failure query without enumeration.

**Dependencies and scope.** Named published deterministic primitives are explicit proof dependencies; the local realization theorem discharges the abstract cycle-search contract. The shipped reference implementation has a separate polynomial bound and does not implement the entire fast research construction. Failure kernels concern a fixed simple graph and native edge/vertex faults; arbitrary cover deletions and attached cover contexts are proved separately. Correlated failure labels and native parallel records are different models. The O(nu f) positive-budget vertex order is credited to the published 2022 result. Readiness is a mathematical review invitation, not proof-assistant verification.

[Proof](../problems/general-matching/proof.md) · [Dependencies](../problems/general-matching/sources.md) · [Evidence](../problems/general-matching/verify/README.md) · Reviewed 2026-10-26

### [Degree-constrained subgraphs](../problems/degree-constrained-subgraphs/)

The complete sparse reductions for prescribed degrees, degree intervals and exact/ranged cardinality, with extension, native decoding and the fast matching substitution. The shipped native-record solver handles feasibility, minimum and maximum cardinality. Its independent verifier checks YES witnesses and local or matching-based NO/optimality certificates without a matching search. The separate linear-size selector imports the precise Gabber–Galil expansion inequality and proves deterministic network enumeration, degree conversion and matching adaptation.

**Dependencies and scope.** The reference implementation has its own polynomial bounds and shares the proved deterministic reduction builder with the verifier. Input is a loopless multigraph with capacity one per explicit record. Binary multiplicities and arbitrary edge-weight optimization are outside this implementation. The current executable retains its Beneš selector. The linear-size theoretical variant has explicit but large constants and does not claim a linear-time routing algorithm.

[Proof](../problems/degree-constrained-subgraphs/proof.md) · [Dependencies](../problems/degree-constrained-subgraphs/sources.md) · [Evidence](../problems/degree-constrained-subgraphs/verify/README.md) · Reviewed 2026-10-26

### [Static and threshold min-cost flow](../problems/min-cost-flow/)

The complete static and insertion-only fixed-threshold moving-box log-barrier construction, instantiated with the locally realized raw-cycle search, numerical lifetime and retirement rules. Includes affine integral recovery, artificial-edge penalties and prefix-safe deferred initialization. The published-flow capacity-bit adapter is a separately proved alternative for exact max-flow calls.

**Dependencies and scope.** The numerical cap, polynomial adaptive-history horizon and full-flow output charge remain part of the theorem. The incremental result is a fixed-threshold guarantee, not a fresh optimal flow after every update. An infeasible early prefix does not imply permanent infeasibility. The alternative capacity-bit route uses van den Brand et al., arXiv:2407.10830v1, Theorem 6.17, with polynomial capacity relative to each actual call size. Its published algorithm is an external proof dependency; local finite adapter checks do not execute it.

[Proof](../problems/min-cost-flow/proof.md) · [Dependencies](../problems/min-cost-flow/sources.md) · [Evidence](../problems/min-cost-flow/verify/README.md) · Reviewed 2026-10-26

### [Incremental strongly connected components](../problems/incremental-scc/)

The complete incremental SCC label theorem with the raw-cycle-to-frozen-detector realization, nonzero-base handling and retirement rules. The label-history extension proves historical equality and O(1+log log(n+2)) first-coalescence queries using permanently retired identities.

**Dependencies and scope.** The theorem gives exact component labels under the stated insertion model and adaptive-history bounds. It does not include dynamic topological-order maintenance or within-component path output. The executable history checks cover that layer separately.

[Proof](../problems/incremental-scc/proof.md) · [Dependencies](../problems/incremental-scc/sources.md) · [Evidence](../problems/incremental-scc/verify/README.md) · Reviewed 2026-10-26

### [Incremental directed SSSP](../problems/incremental-sssp/)

The complete frozen-detector incremental SSSP construction, its realized numerical interface, the simple-path reporting argument and nonnegative-integer perturbation adapter. Includes exact zero distances, clipped-tree intersections, loop removal and accuracy/bit accounting.

**Dependencies and scope.** The input, accuracy and polynomial numerical-range promises remain explicit. Reporting a path with k edges costs (k+1) poly(U). Finite path tests support the reporting lemmas and do not measure the asymptotic detector update time.

[Proof](../problems/incremental-sssp/proof.md) · [Dependencies](../problems/incremental-sssp/sources.md) · [Evidence](../problems/incremental-sssp/verify/README.md) · Reviewed 2026-10-26

### [Fully dynamic APSP](../problems/apsp-frontier/)

The constructed fully dynamic metric hierarchy, full time/stretch curve and all five explicit parameter points, including the same-stretch 23/28 versus 6/7 comparison. The nonnegative-integer adapter supplies exact zero answers and transformed-range accounting.

**Dependencies and scope.** The tradeoff is amortized and reports numerical distances. Its general family assumes t tends to infinity and t^2 h=o(U); extending that family to zero lengths additionally needs t^4 h=o(U) and a uniform stretch bound. The five displayed points satisfy the stronger conditions.

[Proof](../problems/apsp-frontier/proof.md) · [Dependencies](../problems/apsp-frontier/sources.md) · [Evidence](../problems/apsp-frontier/verify/README.md) · Reviewed 2026-10-26

### [Dynamic spanners](../problems/dynamic-spanners/)

The complete tracked-terminal four-fifths and full-horizon five-sixths constructions, including the destructive-support realization, hierarchy and strong-forest substitutions. The zero-edge class and dyadic positive-weight wrapper charge initialization, all updates and settled output recourse.

**Dependencies and scope.** The two recourse guarantees have different scopes and are retained separately. Output is measured after a complete external update, with the stated adaptive-history and numerical-range restrictions. The underlying proofs are available even though a full executable implementation is not supplied.

[Proof](../problems/dynamic-spanners/proof.md) · [Dependencies](../problems/dynamic-spanners/sources.md) · [Evidence](../problems/dynamic-spanners/verify/README.md) · Reviewed 2026-10-26

### [Dynamic minimum spanning forest](../problems/dynamic-msf/)

The full deterministic weighted MSF public-baseline composition: local exchange/contraction proofs, connectivity adapter, finite pruning horizons, decomposition parameters and recursive worst-case cost.

**Dependencies and scope.** The external theorems are Chuzhoy–Gao–Li–Nanongkai–Peng–Saranurak Corollary 6.1, Meierhans–Probst Gutenberg–Saranurak Theorem 6.4, and Nanongkai–Saranurak–Wulff-Nilsen Theorem 7.1 and Section 9. This is a derived public result; a full executable implementation is not supplied.

[Proof](../problems/dynamic-msf/proof.md) · [Dependencies](../problems/dynamic-msf/sources.md) · [Evidence](../problems/dynamic-msf/verify/README.md) · Reviewed 2026-10-26

### [Strong forests and Gomory–Hu trees](../problems/decremental-strong-forest/)

The complete accepted no-reset Steiner-pool strong-forest construction, with fixed pools, native identities, ghost ownership and chronological work. The six-sevenths cut-tree composition includes the locally realized fixed-k adapter and exact-flow chain. Nonnegative flat-forest and zero-capacity adapters, native input costs and actual-call inventory are explicit. The published-flow capacity-bit construction gives an additional route.

**Dependencies and scope.** The structural expansion, bounded-degree and numerical-range hypotheses remain part of the theorem. Forest routing outputs walks under its stated interface; a simple-path reporting contract is not added. The optional older ported-forest candidate is distinct from the completed no-reset construction. The alternative flow route invokes van den Brand et al., arXiv:2407.10830v1, Theorem 6.17. The earlier four-fifths local flow theorem already had its own proof chain and is not reclassified as an open assumption.

[Proof](../problems/decremental-strong-forest/proof.md) · [Dependencies](../problems/decremental-strong-forest/sources.md) · [Evidence](../problems/decremental-strong-forest/verify/README.md) · Reviewed 2026-10-26

### [Matroid and submodular failure summaries](../problems/matroid-failure-summaries/)

Main Theorems 1–8 and the actual-rank represented construction: represented prefix lift; sharp oracle-rank and integral-value constructions; one-failure endpoint; weighted obstruction; canonical-basis tree and original-basis size refinement; exact low-rank two-failure maxima; singleton replacement profiles; fixed rank-loss contraction and all-prefix identities. The new rank-two exact-union algorithm has optimal Theta(N+h^2) queries in its stated range, sharp r+Th support for T<=2 after contraction, actual-residual-rank terminals and an arbitrary-rank all-label-budget endpoint.

**Dependencies and scope.** Oracle results require the specified independence or value oracle and retain original items rather than encoding an arbitrary oracle. The best general weighted-oracle size remains open outside the proved low-rank cases. Finite programs support the written proofs and are not proof-assistant verification. The rank-loss contraction in this review uses one label per item and a fixed total order. The query ledger charges the original oracle separately from explicit query-set representation; a changed cost order may require another contraction. The rank-two query lower bound requires the exact canonical union and N>=h+3; arbitrary valid supersets are outside that hardness claim. Oracle calls, ordinary work and query-set encoding are separate. The actual-rank linear construction uses explicit fields; its reference supports rationals and supplied primes, with general extension-field and bit costs proved separately.

[Proof](../problems/matroid-failure-summaries/proof.md) · [Dependencies](../problems/matroid-failure-summaries/sources.md) · [Evidence](../problems/matroid-failure-summaries/verify/README.md) · Reviewed 2026-10-26

### [Boolean linear optimization compiler](../problems/boolean-linear-compiler/)

The complete signed interval-disjunction proof, bounded-slack interpolation, signed radix packing and indexed-witness/optimization transfer. Each halving emits at most two intervals with at most the original row support many integer values; all exceptional and binary-input cases are explicit. Includes fixed-cardinality layers, modal-coefficient subtraction, signed parity overlap and the resulting smaller slack budget, with exact preservation of the original cardinality and optimization witnesses.

**Dependencies and scope.** The Subset Sum backend is supplied with its stated indexed-witness time contract; a space bound requires that same backend. The compiler and finite checks do not establish the backend circuit or continuous-contact proofs. The cardinality refinement counts the original explicitly listed variables. Its strongest slack bound does not assert a universal improvement to every disjunction-product parameter.

[Proof](../problems/boolean-linear-compiler/proof.md) · [Dependencies](../problems/boolean-linear-compiler/sources.md) · [Evidence](../problems/boolean-linear-compiler/verify/README.md) · Reviewed 2026-10-26

### [Hypergraph matching and expander routing](../problems/strong-haxell-matching/)

The explicit certifying hypergraph-matching algorithm, including build/growth/collapse and weighted finite-prefix termination; the public explicit-algorithm weighted reanalysis; certified disjoint-path routing and spanning-expander packing. The destructive-support extractor, exact-size auxiliary graph and route/conductance accounting are explicitly instantiated. The retained rank-sensitive layer count, its separate root factor and the fixed-right-rank polynomial-strength consequence are included; explicit incidence input is not replaced by an implicit graph-edge count.

**Dependencies and scope.** The hitting, expansion, density, load and input-size promises remain part of their respective theorems. The companion’s separate conditional observation about the public approximate-extension algorithm is not used by these results and retains its stated assumption. Manuscript readiness does not claim a full executable implementation.

[Proof](../problems/strong-haxell-matching/proof.md) · [Dependencies](../problems/strong-haxell-matching/sources.md) · [Evidence](../problems/strong-haxell-matching/verify/README.md) · Reviewed 2026-10-26

### [Self-concordant cone sparsification](../problems/conic-barrier-sparsification/)

The cone-order sparsification theorem and its boundary-sum proof have been checked against the imported geometric statements. The manuscript separates existence, dual/face/lift consequences, and a conditional randomized separation-oracle construction.

**Dependencies and scope.** Reis--Rothvoss Lemma 18 and Theorems 7 and 22 are essential published inputs; the directional barrier inequality and duality are standard cited results. The two supplied research-session audits identified no substantive proof gap. They are not external peer review or formal verification. No general Turing bit-complexity bound, deterministic construction, or exhaustive historical-priority claim is made.

[Proof](../problems/conic-barrier-sparsification/proof.md) · [Dependencies](../problems/conic-barrier-sparsification/sources.md) · [Evidence](../problems/conic-barrier-sparsification/verify/README.md) · Reviewed 2026-10-26

### [Deterministic PIT for fixed-width affine ROABP orbits](../problems/roabp-affine-pit/)

The complete general fixed-width affine-orbit PIT proof and direction-grid refinement have separate exact-source internal reconstructions, including a fresh-context review of the weighted Artin induction. Arbitrary local ranks, unrestricted local entry degrees and every characteristic are covered.

**Dependencies and scope.** The promise is one unknown-order ROABP under an invertible affine map, with a known scalar total-degree bound; small base fields require extension-field oracle access. The polynomial query exponent depends on width; no FPT, unbounded-width polynomial-time, singular-projection or orbit-closure claim is made. The generic Hasse pivot criterion is standard and attributed. Internal model-assisted review, finite tests and presentation checks are not external peer review, proof-assistant verification or priority certification.

[Proof](../problems/roabp-affine-pit/proof.md) · [Dependencies](../problems/roabp-affine-pit/sources.md) · [Evidence](../problems/roabp-affine-pit/verify/README.md) · Reviewed 2026-10-27

## Components ready for review

### [Prefix, laminar and sparse quotas](../problems/weighted-prefix-quota-frontier/)

The sharp sparse-packing FPT restriction with improved basis-tree preprocessing, arbitrary signed-profit ordered extension, capacity-sensitive failure budget, exact original-context lower construction, and aggregate laminar reduction to at most B lower rows. Exact dominant-weight completion with all signed zero-coordinate costs, a binary count-rank oracle, the one-positive-weight polynomial endpoint, the self-contained 10/9 quadratic leading exponent, the named universal-set 5/9 refinement, projected coloring identities and histogram-sensitive enumeration. The compatible-cut extension and the two-positive-weight oracle/encoded-program lower-bound models are proved separately.

**Dependencies and scope.** The general resource calls retain exact integral-polymatroid optimization and submodular-minimization dependencies named in sources.md. The 5/9 leading coefficient specifically uses Naor-Schulman-Srinivasan Theorem 7 and its locally explicit indexing guarantee; the elementary 10/9 alternative supplies a local coloring proof. Finite checkers isolate the stated mechanisms and do not implement all of these optimization algorithms. The compatible-cut one-weight polynomial endpoint requires a prescribed or forced total numeric mass. Original resource totals, all numeric constraints and signed costs remain intact. Oracle query lower bounds and ETH claims for readable rank programs are separate models.

[Proof](../problems/weighted-prefix-quota-frontier/proof.md) · [Dependencies](../problems/weighted-prefix-quota-frontier/sources.md) · [Evidence](../problems/weighted-prefix-quota-frontier/verify/README.md) · Reviewed 2026-10-26

### [Persistent-homology failure certificates](../problems/persistence-failure-certificates/)

Complete actual-feature-rank construction for represented failure lifts and the vertex-label persistence specialization with no extra top-simplex labels. Includes the degree-bounded evaluation module, canonical column pivots, nonzero shifts, shared original boundary-row compression, streamed column generation, surviving prefix spans and naturality, with exact arithmetic and storage ledgers.

**Dependencies and scope.** The reviewed persistence construction keeps the full lower skeleton and one supplied order over the stated field. Additional top labels retain the separate general incidence theorem. Top-degree homology, integral torsion, dynamic labels and a common solution for unrelated filtration/cost orders are not asserted. Executable checks use rationals and supplied prime fields. The general finite-field extension and rational bit analysis are explicit mathematical components. Finite span checks supplement the naturality proof; they are not proof-assistant verification.

[Proof](../problems/persistence-failure-certificates/proof.md) · [Dependencies](../problems/persistence-failure-certificates/sources.md) · [Evidence](../problems/persistence-failure-certificates/verify/README.md) · Reviewed 2026-10-26

## Review pending

These families have not yet received a scoped readiness entry in this registry. Their existing statements retain their own assumptions.

- [Numeric targets and support patterns](../problems/numeric-target-frontier/)
- [Single-failure optimum preservers](../problems/exact-failure-preservers/)
- [Flow, matching and price sensitivity](../problems/exact-flow-sensitivity/)
- [Colored and vertex-failure graph certificates](../problems/graph-color-failure-certificates/)
- [Resource-constrained packing summaries](../problems/packing-matching-summaries/)
- [Correlated spectral, regression and seminorm summaries](../problems/correlated-spectral-regression/)
- [Label and whole-block cut sparsification](../problems/label-block-cut/)
- [Finite groups, affine constraints and metrics](../problems/group-metric-constraints/)
- [Pauli, qudit and stabilizer blocks](../problems/quantum-stabilizer/)
- [Exact-separation and non-Fano boundaries](../problems/obstruction-boundaries/)
- [Arbitrary-value allocation scheme](../problems/arbitrary-value-allocation-scheme/)
- [Recipient polymatroids](../problems/recipient-polymatroid/)
- [Recipient-matroid configuration](../problems/recipient-matroid-configuration/)
- [Explicit-item matroid union](../problems/item-matroid-union/)
- [One-value allocation](../problems/one-value-exact-two/)
- [Intrinsic two-value allocation](../problems/two-value-exact-two/)
- [Intrinsic values near factor two](../problems/intrinsic-values-near-two/)
- [Unrelated-value additive allocation](../problems/unrelated-values-additive/)
- [Unrelated values with a joint role](../problems/unrelated-values-joint-role/)
- [Whole-ground selection and transfers](../problems/whole-ground-allocation/)
- [Selected concurrent flow](../problems/selected-flow/)
- [Flow with shared setup budget](../problems/shared-setup-flow/)
- [Robust selected flow](../problems/robust-scenario-flow/)
- [Robust unrelated allocation](../problems/robust-unrelated-allocation/)
- [Robust bounded-width certificates](../problems/robust-bounded-certificates/)
- [Width-two robust unit allocation](../problems/robust-width-two-allocation/)
- [Two-scenario hardness](../problems/robust-two-scenario-hardness/)
- [Arbitrary-processing scheme](../problems/arbitrary-processing-scheduling/)
- [Activated-machine scheduling](../problems/activated-machine-scheduling/)
- [Six-profile scheduling](../problems/six-profile-three-halves/)
- [Processing-bucket tradeoff](../problems/processing-bucket-tradeoff/)
- [Two-size scheduling](../problems/two-size-scheduling/)
- [Per-machine two-time scheduling](../problems/two-time-scheduling/)
- [Many-size workload scheduling](../problems/many-size-scheduling/)
- [Commitment scheduling](../problems/commitment-scheduling/)
- [Independent transversals](../problems/independent-transversal/)
- [Allocation and scheduling barriers](../problems/allocation-lower-bounds/)

## Supporting manuscripts

These independent results have their own review scopes. A completed static theorem does not certify a separate dynamic application.

### [Exact demand trimming without a flow oracle](../manuscripts/graph-backends/exact-demand-flow-trimming.md)

**Ready for review.** Complete coordinatewise subflow construction, selected directed forest, cycle cancellation, source excess removal and near-linear operation ledger. Includes sink-outgoing preprocessing, native arc identities and finite-bit arithmetic.

**Dependencies and scope.** The deterministic dynamic-forest interface is a named published data-structure dependency. A supplied feasible flow and strictly positive nonsink targets are part of the input model.

[Manuscript](../manuscripts/graph-backends/exact-demand-flow-trimming.md) · [Evidence](../manuscripts/graph-backends/verify/README.md) · Reviewed 2026-10-26

### [Static selected-pair forests below twice the row total](../manuscripts/graph-backends/static-transportation-support-balancing.md)

**Ready for review.** Complete arbitrary-row-rank static selected-pair forest theorem, private transportation-cycle cancellation, strict component bound below twice the row total and construction of a new physical row-covering injection.

**Dependencies and scope.** The old injection may change. The near-linear operation bound uses named dynamic-tree operations; dynamically maintaining the private support is a separate problem.

[Manuscript](../manuscripts/graph-backends/static-transportation-support-balancing.md) · [Evidence](../manuscripts/graph-backends/verify/README.md) · Reviewed 2026-10-26

### [Near-linear confluent rounding and mass-sensitive tails](../manuscripts/graph-backends/static-confluent-rounding-and-tail-bounds.md)

**Ready for review.** Complete near-linear simulation and Parts B–D simultaneous completed-sink moment and tail bounds, including the budget proportional to actual demand. Part E proves the scoped local warm-start lemma.

**Dependencies and scope.** The precise published base-2 Conflt operations and deterministic dynamic-tree interface are identified. Reopening completed sinks needs separate dynamic replenishment accounting and is not used by the completed main matching theorem.

[Manuscript](../manuscripts/graph-backends/static-confluent-rounding-and-tail-bounds.md) · [Evidence](../manuscripts/graph-backends/verify/README.md) · Reviewed 2026-10-26

### [Canonical odd crowns and exact matching-value preservation](../manuscripts/graph-backends/low-state-odd-crown.md)

**Ready for review.** Complete canonical contact-rank/min-cut characterization, exact physical matching offset, the numerical LOW consequence and the explicit retained-mass counterexample. Independent small-instance checks validate the structural identities.

**Dependencies and scope.** The input state supplies constructive factor-critical witnesses. Ordinary bipartite matching suffices; the named published almost-linear flow theorem is an optional faster construction. A bound on the remaining optimum gap does not bound the entire retained graph.

[Manuscript](../manuscripts/graph-backends/low-state-odd-crown.md) · [Evidence](../manuscripts/graph-backends/verify/README.md) · Reviewed 2026-10-26

### [Exact interval-rank palette support bounds](../problems/roabp-affine-pit/manuscripts/palette-sharpness.md)

**Ready for review.** The general palette lower construction and original-field degree-two actual-curve lift have complete internal proofs, matching the separately proved concentration threshold. The uniform active-endpoint subcase retains its sharper exact threshold.

**Dependencies and scope.** Interval preservation concerns physical matrix words; the augmented scalar interval is excluded when the scalar vanishes on the initial curve. The examples survive one SV pair, so the result is not a PIT or generator lower bound. Internal review and finite identities do not constitute external peer review or formal verification.

[Manuscript](../problems/roabp-affine-pit/manuscripts/palette-sharpness.md) · [Evidence](../problems/roabp-affine-pit/verify/README.md) · Reviewed 2026-10-27

### [Quadratic local Hasse digit-degree obstruction](../problems/roabp-affine-pit/manuscripts/quadratic-hasse-obstruction.md)

**Ready for review.** The binomial determinant formula and original-field actual-curve construction have a complete symbolic proof and a separate internal reconstruction. The first ordinary homogeneous component has digit degree exactly w²−1.

**Dependencies and scope.** Width w≥2 and prime characteristic p>w²+w−2; the construction uses n=p coordinates and scalar total degree 2p(w−1). The curve is the ordinary moment curve, whose p-th coordinate has zero derivative. This is not a counterexample to a derivative-separating-curve theorem. Every physical interval preserves full rank. The endpoint-augmented scalar interval does not. One SV pair detects the example, so no PIT or generator lower bound is asserted. The audit is internal model-assisted reconstruction, not external peer review, formal certification or priority determination.

[Manuscript](../problems/roabp-affine-pit/manuscripts/quadratic-hasse-obstruction.md) · [Evidence](../problems/roabp-affine-pit/verify/README.md) · Reviewed 2026-10-27

### Supporting review pending

- [Grouped choices under resource deletions](../manuscripts/graph-backends/decremental-choice-recourse-lemma.md)
- [Nonuniform sparse route rounding](../manuscripts/graph-backends/nonuniform-fractional-path-selection.md)
- [Short path inventories from a shared DAG](../manuscripts/graph-backends/compressed-fractional-path-extraction.md)
- [Bounded-width lazy path client](../manuscripts/graph-backends/bounded-interface-witness-pattern-updates.md)
- [Forest-support numerical client](../manuscripts/graph-backends/complete-unrestricted-forest-one-sided-client.md)
- [Feedback-edge numerical client](../manuscripts/graph-backends/feedback-edge-one-sided-client.md)
- [Weak-Haxell certifying matching](../manuscripts/matching-and-routing/weak-haxell-current-blocker-growth.md)
- [Sparse-separator corank refinement](../manuscripts/allocation-and-scheduling/attained-set-sparse-separator-gap.md)
- [Whole-ground robust allocation barrier](../manuscripts/allocation-and-scheduling/robust-unit-allocation-whole-ground-oracle-barrier.md)
- [Implicit minimal-bundle transversals](../manuscripts/matching-and-routing/implicit-minimal-bundle-transversal-oracle.md)
- [Global free pool at the critical quota](../manuscripts/allocation-and-scheduling/critical-unit-quota-global-free-pool.md)
- [Jointly independent layer owners](../manuscripts/allocation-and-scheduling/joint-owner-sharp-quality-addendum.md)
- [Explicit laminar reservation interface](../manuscripts/allocation-and-scheduling/laminar-resource-current-blocker-reservations.md)
- [Persistent path-hitting certificates](../manuscripts/graph-backends/fixed-hitting-certificates-under-graph-updates.md)
- [Fixed-potential tight-DAG repairs](../manuscripts/graph-backends/fixed-potential-tight-dag-repair-lemma.md)
- [Slack-only directed matching reduction](../manuscripts/graph-backends/slack-only-one-sided-matching-client.md)
- [Residual-capacity configuration comparator](../manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md)
- [Fractional optimization of residual configuration relaxations](../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md)

## Executable evidence

Each linked program documents its checked identities or finite domain. The per-result evidence notes and registry distinguish direct evidence from a shared prerequisite; a passing finite check does not establish an arbitrary-input asymptotic theorem.

- [manuscripts/graph-backends/verify/check_odd_crown.py](../manuscripts/graph-backends/verify/check_odd_crown.py)
- [manuscripts/graph-backends/verify/check_static_allocations.py](../manuscripts/graph-backends/verify/check_static_allocations.py)
- [problems/boolean-linear-compiler/verify/check_cardinality_compiler.py](../problems/boolean-linear-compiler/verify/check_cardinality_compiler.py)
- [problems/boolean-linear-compiler/verify/check_interval_compiler.py](../problems/boolean-linear-compiler/verify/check_interval_compiler.py)
- [problems/degree-constrained-subgraphs/verify/check_linear_selector.py](../problems/degree-constrained-subgraphs/verify/check_linear_selector.py)
- [problems/degree-constrained-subgraphs/verify/check_reductions.py](../problems/degree-constrained-subgraphs/verify/check_reductions.py)
- [problems/degree-constrained-subgraphs/verify/check_reference.py](../problems/degree-constrained-subgraphs/verify/check_reference.py)
- [problems/general-matching/verify/check_bipartite.py](../problems/general-matching/verify/check_bipartite.py)
- [problems/general-matching/verify/check_certificate_search.py](../problems/general-matching/verify/check_certificate_search.py)
- [problems/general-matching/verify/check_cover_compression.py](../problems/general-matching/verify/check_cover_compression.py)
- [problems/general-matching/verify/check_failure_kernel.py](../problems/general-matching/verify/check_failure_kernel.py)
- [problems/general-matching/verify/check_reductions.py](../problems/general-matching/verify/check_reductions.py)
- [problems/general-matching/verify/check_reference.py](../problems/general-matching/verify/check_reference.py)
- [problems/group-metric-constraints/verify/check_quotient_rounding.py](../problems/group-metric-constraints/verify/check_quotient_rounding.py)
- [problems/incremental-scc/verify/check_label_history.py](../problems/incremental-scc/verify/check_label_history.py)
- [problems/incremental-sssp/verify/check_path_reporting.py](../problems/incremental-sssp/verify/check_path_reporting.py)
- [problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py](../problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py)
- [problems/matroid-failure-summaries/verify/check_rank_two_prefix.py](../problems/matroid-failure-summaries/verify/check_rank_two_prefix.py)
- [problems/matroid-failure-summaries/verify/check_single_replacement.py](../problems/matroid-failure-summaries/verify/check_single_replacement.py)
- [problems/matroid-failure-summaries/verify/check_summaries.py](../problems/matroid-failure-summaries/verify/check_summaries.py)
- [problems/matroid-failure-summaries/verify/check_weighted_obstruction.py](../problems/matroid-failure-summaries/verify/check_weighted_obstruction.py)
- [problems/matroid-failure-summaries/verify/check_weighted_prefix.py](../problems/matroid-failure-summaries/verify/check_weighted_prefix.py)
- [problems/min-cost-flow/verify/check_capacity_scaling.py](../problems/min-cost-flow/verify/check_capacity_scaling.py)
- [problems/min-cost-flow/verify/check_recovery.py](../problems/min-cost-flow/verify/check_recovery.py)
- [problems/persistence-failure-certificates/verify/check_feature_construction.py](../problems/persistence-failure-certificates/verify/check_feature_construction.py)
- [problems/roabp-affine-pit/verify/all_rank_affine_orbit.py](../problems/roabp-affine-pit/verify/all_rank_affine_orbit.py)
- [problems/roabp-affine-pit/verify/build_native_papers.py](../problems/roabp-affine-pit/verify/build_native_papers.py)
- [problems/roabp-affine-pit/verify/check_artin_reset.py](../problems/roabp-affine-pit/verify/check_artin_reset.py)
- [problems/roabp-affine-pit/verify/check_palette_sharpness.py](../problems/roabp-affine-pit/verify/check_palette_sharpness.py)
- [problems/roabp-affine-pit/verify/check_quadratic_hasse.py](../problems/roabp-affine-pit/verify/check_quadratic_hasse.py)
- [problems/roabp-affine-pit/verify/check_source_bindings.py](../problems/roabp-affine-pit/verify/check_source_bindings.py)
- [problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py](../problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py)
- [problems/subset-sum-fast-deterministic/verify/check_energy.py](../problems/subset-sum-fast-deterministic/verify/check_energy.py)
- [problems/subset-sum-fast-deterministic/verify/check_headline_ledger.py](../problems/subset-sum-fast-deterministic/verify/check_headline_ledger.py)
- [problems/subset-sum-fast-deterministic/verify/check_replay_recovery.py](../problems/subset-sum-fast-deterministic/verify/check_replay_recovery.py)
- [problems/subset-sum-fast-deterministic/verify/check_third_recovery.py](../problems/subset-sum-fast-deterministic/verify/check_third_recovery.py)
- [problems/subset-sum-low-space-deterministic/verify/check_exact_convolution.py](../problems/subset-sum-low-space-deterministic/verify/check_exact_convolution.py)
- [problems/subset-sum-low-space-deterministic/verify/check_range_identities.py](../problems/subset-sum-low-space-deterministic/verify/check_range_identities.py)
- [problems/subset-sum-low-space-deterministic/verify/check_range_solver.py](../problems/subset-sum-low-space-deterministic/verify/check_range_solver.py)
- [problems/subset-sum-low-space-deterministic/verify/check_resources.py](../problems/subset-sum-low-space-deterministic/verify/check_resources.py)
- [problems/subset-sum-low-space-deterministic/verify/check_structural.py](../problems/subset-sum-low-space-deterministic/verify/check_structural.py)
- [problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py](../problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py)
- [problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py](../problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py)
- [problems/weighted-prefix-quota-frontier/verify/check_quota_extensions.py](../problems/weighted-prefix-quota-frontier/verify/check_quota_extensions.py)
- [problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py](../problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py)
- [problems/weighted-prefix-quota-frontier/verify/check_two_weight_lower.py](../problems/weighted-prefix-quota-frontier/verify/check_two_weight_lower.py)
- [tools/verify_finite_reductions.py](../tools/verify_finite_reductions.py)
- [tools/verify_non_fano.py](../tools/verify_non_fano.py)
- [tools/verify_profile_certificates.py](../tools/verify_profile_certificates.py)
- [tools/verify_sensitivity_certificates.py](../tools/verify_sensitivity_certificates.py)
- [tools/verify_subset_sum_contacts.py](../tools/verify_subset_sum_contacts.py)
- [tools/verify_subset_sum_scalars.py](../tools/verify_subset_sum_scalars.py)
- [tools/verify_subset_sum_third_contacts.py](../tools/verify_subset_sum_third_contacts.py)

## Maintaining a status

Set a readiness scope only after checking the corresponding proof, algorithm, representation, randomness and source requirements. Name proved local realizations, external theorems and genuinely unresolved assumptions separately. Executable coverage is a distinct field of evidence. Update `registry.json`, then run `python3 tools/build_reviews.py`; this synchronizes these entries with the reviewed problem cards and supporting manuscripts. A changed theorem or dependency requires a new scope assessment.

See [Contributing](../CONTRIBUTING.md) for the manuscript workflow and [provenance](../provenance/README.md) for imported source identities.
