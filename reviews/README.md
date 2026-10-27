# Review status and verification evidence

Readiness applies to the precise scope below. **Ready for review** means that the stated manuscript package has been checked for its theorem, proof, computational model and declared dependencies. **Partial readiness** identifies completed components of a larger family. Other manuscripts remain available with review pending. None of these labels claims external peer review or proof-assistant verification.

The machine-readable [registry](registry.json) is the source of these statuses and of each executable check's mathematical scope.

## Run the checks

```sh
python3 tools/check_repository.py
```

The default suite checks repository structure and every registered executable used by the canonical runner. For Subset Sum it validates the two-level and third-lookup receipts' source/menu bindings, checks both scalar ledgers and the recovery paths, and freshly replays the `rho=1.7` and direct two-level branches. To cleanly replay all 62 two-level and 16 third-lookup branches:

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

**Dependencies and scope.** The stronger `n/6`-space result requires the supplied three-block partition and two short normalized ranges. The general theorem has no such input restriction. Executable finite checks cover their named identities and resource ledgers; they are not a full implementation or formalization of either asymptotic construction.

[Proof](../problems/subset-sum-low-space-deterministic/proof.md) · [Dependencies](../problems/subset-sum-low-space-deterministic/sources.md) · [Evidence](../problems/subset-sum-low-space-deterministic/verify/README.md) · Reviewed 2026-10-26

### [Deterministic general-graph maximum matching](../problems/general-matching/)

The complete deterministic four-fifths research theorem, including the cycle-search realization, raw quality and gradient lifting, chronological work, stable retirement, finite-bit realization and uniform search. The separate executable package includes exact matching, independent optimality certificates, the refined `3nu` vertex count for the earlier compression, nonrecursive bipartite phases, and universal mixed-failure kernels with all-cover-subset and context preservation. Layer matching/vertex-cover witnesses certify every permitted failure query without enumeration.

**Dependencies and scope.** Named published deterministic primitives are explicit proof dependencies; the local realization theorem discharges the abstract cycle-search contract. The shipped reference implementation has a separate polynomial bound and does not implement the entire fast research construction. Failure kernels concern a fixed simple graph and native edge/vertex faults; arbitrary cover deletions and attached cover contexts are proved separately. Correlated failure labels and native parallel records are different models. The `O(nu f)` positive-budget vertex order is credited to the published 2022 result. Readiness is a mathematical review invitation, not proof-assistant verification.

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

The complete incremental SCC label theorem with the raw-cycle-to-frozen-detector realization, nonzero-base handling and retirement rules. The label-history extension proves historical equality and `O(1+log log(n+2))` first-coalescence queries using permanently retired identities.

**Dependencies and scope.** The theorem gives exact component labels under the stated insertion model and adaptive-history bounds. It does not include dynamic topological-order maintenance or within-component path output. The executable history checks cover that layer separately.

[Proof](../problems/incremental-scc/proof.md) · [Dependencies](../problems/incremental-scc/sources.md) · [Evidence](../problems/incremental-scc/verify/README.md) · Reviewed 2026-10-26

### [Incremental directed SSSP](../problems/incremental-sssp/)

The complete frozen-detector incremental SSSP construction, its realized numerical interface, the simple-path reporting argument and nonnegative-integer perturbation adapter. Includes exact zero distances, clipped-tree intersections, loop removal and accuracy/bit accounting.

**Dependencies and scope.** The input, accuracy and polynomial numerical-range promises remain explicit. Reporting a path with `k` edges costs `(k+1) poly(U)`. Finite path tests support the reporting lemmas and do not measure the asymptotic detector update time.

[Proof](../problems/incremental-sssp/proof.md) · [Dependencies](../problems/incremental-sssp/sources.md) · [Evidence](../problems/incremental-sssp/verify/README.md) · Reviewed 2026-10-26

### [Fully dynamic APSP](../problems/apsp-frontier/)

The constructed fully dynamic metric hierarchy, full time/stretch curve and all five explicit parameter points, including the same-stretch `23/28` versus `6/7` comparison. The nonnegative-integer adapter supplies exact zero answers and transformed-range accounting.

**Dependencies and scope.** The tradeoff is amortized and reports numerical distances. Its general family assumes `t` tends to infinity and `t^2 h=o(U)`; extending that family to zero lengths additionally needs `t^4 h=o(U)` and a uniform stretch bound. The five displayed points satisfy the stronger conditions.

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

The complete accepted no-reset Steiner-pool strong-forest construction, with fixed pools, native identities, ghost ownership and chronological work. The six-sevenths cut-tree composition includes the locally realized fixed-`k` adapter and exact-flow chain. Nonnegative flat-forest and zero-capacity adapters, native input costs and actual-call inventory are explicit. The published-flow capacity-bit construction gives an additional route.

**Dependencies and scope.** The structural expansion, bounded-degree and numerical-range hypotheses remain part of the theorem. Forest routing outputs walks under its stated interface; a simple-path reporting contract is not added. The optional older ported-forest candidate is distinct from the completed no-reset construction. The alternative flow route invokes van den Brand et al., arXiv:2407.10830v1, Theorem 6.17. The earlier four-fifths local flow theorem already had its own proof chain and is not reclassified as an open assumption.

[Proof](../problems/decremental-strong-forest/proof.md) · [Dependencies](../problems/decremental-strong-forest/sources.md) · [Evidence](../problems/decremental-strong-forest/verify/README.md) · Reviewed 2026-10-26

### [Matroid and submodular failure summaries](../problems/matroid-failure-summaries/)

Main Theorems 1–8 and the actual-rank represented construction: represented prefix lift; sharp oracle-rank and integral-value constructions; one-failure endpoint; weighted obstruction; canonical-basis tree and original-basis size refinement; exact low-rank two-failure maxima; singleton replacement profiles; fixed rank-loss contraction and all-prefix identities. The new rank-two exact-union algorithm has optimal `Theta(N+h^2)` queries in its stated range, sharp `r+Th` support for `T<=2` after contraction, actual-residual-rank terminals and an arbitrary-rank all-label-budget endpoint.

**Dependencies and scope.** Oracle results require the specified independence or value oracle and retain original items rather than encoding an arbitrary oracle. The best general weighted-oracle size remains open outside the proved low-rank cases. Finite programs support the written proofs and are not proof-assistant verification. The rank-loss contraction in this review uses one label per item and a fixed total order. The query ledger charges the original oracle separately from explicit query-set representation; a changed cost order may require another contraction. The rank-two query lower bound requires the exact canonical union and `N>=h+3`; arbitrary valid supersets are outside that hardness claim. Oracle calls, ordinary work and query-set encoding are separate. The actual-rank linear construction uses explicit fields; its reference supports rationals and supplied primes, with general extension-field and bit costs proved separately.

[Proof](../problems/matroid-failure-summaries/proof.md) · [Dependencies](../problems/matroid-failure-summaries/sources.md) · [Evidence](../problems/matroid-failure-summaries/verify/README.md) · Reviewed 2026-10-26

### [Colored and vertex-failure graph certificates](../problems/graph-color-failure-certificates/)

Complete canonical graph family: sharp componentwise singleton vertex-color activation theorem; overlapping vertex lists with actual symmetric-matrix rank saving; mixed vertex/extra-edge lists and singleton mixed symmetric-cubic dependencies; all surviving fixed-order prefix connectivity partitions and exact canonical minimum spanning forests with signed rational weights/permanent IDs; ordinary sharp and all stated leading-order simple/multigraph lower examples; completed-batch one-failure replacement lists, exact indexed values, and the published dynamic-MSF composition. Native references compute actual evaluation spans without formal monomial enumeration and exercise genuine original-ID exchange reporting with separately charged exact reference updates.

**Dependencies and scope.** One original undirected multigraph, one shared color-failure palette, overlapping vertex/edge lists, signed rational edge weights and one fixed permanent-ID tie-broken order are retained. Prefix and canonical-forest guarantees hold after all allowed failures; arbitrary recosting, metric distances or a second unrelated order are not included. The mixed/list backend computes polynomial-size actual evaluation-module rowspaces on component vertices or endpoint/edge positions. Both-direction row maps preserve the full formal activation-matrix dependencies. Vertex-mode ranks are componentwise actual vertex-feature ranks; mixed feature-rank metadata is not the vertex Vandermonde rank used by the separate cubic formula. No uncomputed global actual rank is asserted. Native arithmetic is rational or over a caller-supplied sufficiently large prime field. Primality validation and field-extension software are not supplied. The rational construction alone realizes deterministic polynomial preprocessing; all coordinate, elimination, sorting and original rational-bit costs are charged. Retained-edge support is distinct from arithmetic workspace and full forest-report cost. HDT JACM2001 Theorem 8 and Section5.1, together with its original page724 problem definition, realize the exchange-reporting dynamic-MSF interface. The global forest changes name their entering/leaving original edges; parallel-pair priority queues use constant-many simple-graph updates. The shipped ReferenceMSF instead scans original records and recomputes exact Kruskal per update, with its own polynomial scan/hash/set ledger. No polylogarithmic dynamic implementation is claimed. The one-failure wrapper collects only completed deletion batches, sorts replacement lists and the retained union, and charges those sorts. Compact indexed difference/value lookup is separate from raw original-color binary search and materializing a full forest. Replacement support is bounded by destroyed baseline incidence, with no intermediate-forest accumulation. Support lower bounds concern original retained subgraphs in their stated simple-graph or multigraph asymptotic regimes; they do not lower-bound arbitrary encodings or prove optimality of all mixed instances. The color-list model is publicly credited. Quantitative comparisons to uninspected journal refinements, exhaustive historical priority, external peer review and proof-assistant verification are outside this readiness scope.

[Proof](../problems/graph-color-failure-certificates/proof.md) · [Dependencies](../problems/graph-color-failure-certificates/sources.md) · [Evidence](../problems/graph-color-failure-certificates/verify/README.md) · Reviewed 2026-10-27

### [Resource-constrained packing summaries](../problems/packing-matching-summaries/)

The complete exterior/product-feature packing transfer, including signed fixed costs, multiple label-failure systems, private padding, full original resource rank, arbitrary later extension backgrounds, multigraph matching specializations and explicit rational/finite-field construction accounting. The shipped rational backend realizes the dimension gate and weighted lifted basis, with an independent subset/context checker.

**Dependencies and scope.** The original optional resource matroid must be explicitly represented. Later extensions may be unrepresented but must restrict to that original resource; the implementation constructs a restriction and does not solve arbitrary extension queries. The executable uses exact rational arithmetic only. Explicit finite-field extensions retain their separate mathematical proof and are not implemented by this backend. Fixed costs and permanent input IDs cannot be changed by a query. Finite context enumeration tests the implementation, while the original-flat and annihilating-functional proof establishes all-extension quantifiers. This internal review does not certify historical priority or formal verification.

[Proof](../problems/packing-matching-summaries/proof.md) · [Dependencies](../problems/packing-matching-summaries/sources.md) · [Evidence](../problems/packing-matching-summaries/verify/README.md) · Reviewed 2026-10-27

### [Persistent-homology failure certificates](../problems/persistence-failure-certificates/)

The full exact persistence family: general row/column incidence-label construction, additional top-simplex labels, surviving prefix spans and canonical signed-cost boundary bases with rank drops, natural lower-homology persistence and compatible relative/zigzag identifications, sharp one-color exterior envelope and its complete-complex lower construction, actual-feature-rank refinement and labeled-cone asymptotic lower bound. The native general-incidence backend preserves original row labels while generating row-specific evaluation modules and merging actual lifted row spaces. The previous feature-rank companion completes degree-bounded closure, shared row compression, streamed contractions and exact representation costs.

**Dependencies and scope.** The full original lower skeleton is retained, with one supplied original top-column order and one chosen coefficient field. Independent filtration and cost orders require separate summaries. Top-degree homology, integral torsion, homotopy type, dynamic update bounds and optimizing unknown worst failures are not claimed. Executable arithmetic is rational or over a caller-supplied prime field large enough for the explicit nonzero label points. Finite-field extensions and scalar descent are proved mathematical components, not an implemented extension constructor. The general-incidence adapter materializes the original boundary and charges polynomial dense storage and exact elimination separately; the vertex-only adapter retains its streamed resource contract. The exact one-color envelope and asymptotic general coefficient are original-top-cell restriction lower bounds with the full lower skeleton fixed. Historical comparison and publication-priority claims are not certified by this internal proof review. Finite original-input checks supplement the arbitrary-size proofs and are neither external peer review nor proof-assistant verification.

[Proof](../problems/persistence-failure-certificates/proof.md) · [Dependencies](../problems/persistence-failure-certificates/sources.md) · [Evidence](../problems/persistence-failure-certificates/verify/README.md) · Reviewed 2026-10-27

### [Boolean linear optimization compiler](../problems/boolean-linear-compiler/)

The complete signed interval-disjunction proof, bounded-slack interpolation, signed radix packing and indexed-witness/optimization transfer. Each halving emits at most two intervals with at most the original row support many integer values; all exceptional and binary-input cases are explicit. Includes fixed-cardinality layers, modal-coefficient subtraction, signed parity overlap and the resulting smaller slack budget, with exact preservation of the original cardinality and optimization witnesses.

**Dependencies and scope.** The Subset Sum backend is supplied with its stated indexed-witness time contract; a space bound requires that same backend. The compiler and finite checks do not establish the backend circuit or continuous-contact proofs. The cardinality refinement counts the original explicitly listed variables. Its strongest slack bound does not assert a universal improvement to every disjunction-product parameter.

[Proof](../problems/boolean-linear-compiler/proof.md) · [Dependencies](../problems/boolean-linear-compiler/sources.md) · [Evidence](../problems/boolean-linear-compiler/verify/README.md) · Reviewed 2026-10-26

### [Exact-separation and non-Fano boundaries](../problems/obstruction-boundaries/)

Both canonical obstruction theorems: exact compact-code membership is coNP-complete through the weighted Max-Cut reduction, including sparse certificates for binary-encoded unused dimensions; and the precise non-Fano fixed-amplitude counterexample with its direct-sum product. The exact reference constructs the reduction, verifies original-input dense or sparse violations without search, recovers violating cuts and separates by streamed enumeration of used coordinates.

**Dependencies and scope.** The Max-Cut primary source uses positive integer weights and a non-strict target; the reduction explicitly shifts that target to its strict-cut threshold. Construction and certificate verification charge actual rational and coordinate bit lengths. The reference separator is exponential in used coordinates. No polynomial exact separator, approximate-separation hardness, Gaussian-amplitude counterexample or general sparsifier construction is claimed. Independent internal proof review and finite executable evidence do not assert external peer review or proof-assistant verification.

[Proof](../problems/obstruction-boundaries/proof.md) · [Dependencies](../problems/obstruction-boundaries/sources.md) · [Evidence](../problems/obstruction-boundaries/verify/README.md) · Reviewed 2026-10-27

### [Arbitrary-value allocation scheme](../problems/arbitrary-value-allocation-scheme/)

The complete arbitrary-value optional-player approximation scheme with a genuine original player basis, recipient polymatroids, eligibility, optional unused capacity, arbitrary nonnegative player/type values, setup fees and one shared exact setup/assignment budget: integer-target capping, occupied profiles and both state-count envelopes, original joint LP feasibility, cost-preserving disposal/complement-prefix rounding, full requested accuracy and one-sided original-grid optimization. Includes a native complete-table implementation and independent original-input/output verification with separately charged finite LP costs.

**Dependencies and scope.** The mathematical time envelopes charge named polynomial exact rank/SFM, LP and weighted polymatroid-intersection primitives. The complete-table reference streams LP active systems after exact fixed-coordinate substitution, with an additional `binom(R,D)` factor for actual remaining rows and free dimension `D<=m*q`; it does not implement those fast primitive costs. Complete rank-table input, augmented disposal tables, rational arithmetic and the full binary accuracy encoding are charged. The approximation comparator is original integer optimum, not the capped fractional relaxation or a fractional selected basis. Original type capacities remain shared across all players and bins; one actual scalar cost objective preserves the single shared setup and assignment budget. Several independent exact budgets and extra coupling constraints between types are outside this scope. Internal proof review, exact finite original-input comparisons and producer-independent output verification are not proof-assistant formalization or external peer review. The cited ICALP 2025 rounding paper is a public antecedent, not a black-box proof of this full profile model.

[Proof](../problems/arbitrary-value-allocation-scheme/proof.md) · [Dependencies](../problems/arbitrary-value-allocation-scheme/sources.md) · [Evidence](../problems/arbitrary-value-allocation-scheme/verify/README.md) · Reviewed 2026-10-27

### [Recipient polymatroids](../problems/recipient-polymatroid/)

Complete canonical integer allocation and binary representation family, together with all linked fractional companions: natural ranks and whole-owner contraction, original-box integral comparator recovery and distinct records, large-unit dual-union completion, prefix additivity and current release/exchange/rank charging, exact and positive-slack signatures and quota endpoint; residual-capacity configuration comparator, dependent-reserve basis replacement, exact full and support-restricted subset-cut equivalence and fat preservation; scaled recipient-matroid component fractional loss; count-box signed convex pricing, strict cost grids, explicit-row and implicit-aggregate weak fractional optimizers with uniform finite-system interior balls and primal extraction; full and bounded-support XP runtime distinctions; and fractional-only player-dependent profits. Aggregate and full residual configuration gaps remain separate from integer-comparator guarantees. Native count and fractional references exercise original input interfaces with separately charged table, finite generation, storage and Bland pivot costs.

**Dependencies and scope.** The integer allocation theorem and residual/scaled comparator transfers use common intrinsic nonnegative values, independent integral recipient polymatroids, unused capacity and an original selected player basis. Arbitrary type-symmetric downward-closed local families require the supplied certified availability oracle. This is a declared input-model primitive; the fractional pricing implementation does not supply a general local oracle or add original assignment budgets. The fractional optimizer requires local integer coordinate boxes, with quotas at most original singleton ranks. It retains every original player-base and aggregate-resource constraint even with a restricted residual-cut family. Its output is fractional configuration mass, not an actual integer allocation or a fractionally mixed basis substituted into the integer comparator proof. The player-dependent-value extension applies only to fractional optimization. All mathematical allocation and weak-optimizer constructions pay for the exact rank/SFM, integral intersection/decomposition, rational LP, greedy support and ellipsoid operations they use. Support-restricted fractional optimization is XP in the support/rank parameter, while the full cut family is singly exponential in the total original player count. It is not a rank-FPT or rank-quasipolynomial fractional optimizer. The native outer implementation uses actual normalized homogeneous Farkas column/aggregate-vertex generation with exact canonical Bland certificates. At zero margin its LP dual supplies a finite primal directly. Local signed convex pricing uses binary segments, nonpositive-prefix shifting, profit scaling and exact strict-cost grids. The number of generated objects and Bland pivots can be enormous, and all generated columns/vertices are stored; these finite costs and full rational accuracy encoding are explicit and separate from the fast mathematical ellipsoid time and workspace. No numerical unit list is constructed. Scaled matroid types remain separate supplied components; merging equal-value types can weaken the configuration comparator. The full residual relaxation itself has an exact integrality gap of two, and the unstrengthened aggregate gap approaches selected rank. Neither is a computational hardness claim against integer optimum or a below-two algorithm. The small-quota positive-growth boundary is unchanged. Full player-layer integer-allocation software, a fast ellipsoid implementation and arbitrary local-availability oracle implementations are not supplied by these references. Independent mathematical review, original-input finite evidence and producer-independent verification do not constitute proof-assistant formalization, external peer review or an exhaustive publication-priority claim.

[Proof](../problems/recipient-polymatroid/proof.md) · [Dependencies](../problems/recipient-polymatroid/sources.md) · [Evidence](../problems/recipient-polymatroid/verify/README.md) · Reviewed 2026-10-27

### [Recipient-matroid configuration](../problems/recipient-matroid-configuration/)

The complete recipient-matroid configuration-comparator theorem: universal simultaneous reservations, every ordered-prefix rank-additivity invariant, current eager release, retained-prefix exchanges, sharp rank-cover coefficient, exact and positive-slack rank bounds, fractional fat-service reduction and target-grid search. The shipped resource-state backend realizes completion, current freedom tests and safe prefix exchanges.

**Dependencies and scope.** One service per player-resource pair with common intrinsic nonnegative values. Local families are downward closed; their exact or certified rational approximation oracle and all matroid union/rank work are paid. The executable component implements the resource side only. Player eligibility, earliest whole-layer retention, bundle feasibility/minimality and normalization are caller obligations; the complete player-layer allocator and fat-service union engine are not shipped. The proof uses separate recipient-matroid columns and does not automatically extend to aggregate polymatroids. Finite represented examples support the symbolic all-matroid argument; no external peer review or formal verification is claimed.

[Proof](../problems/recipient-matroid-configuration/proof.md) · [Dependencies](../problems/recipient-matroid-configuration/sources.md) · [Evidence](../problems/recipient-matroid-configuration/verify/README.md) · Reviewed 2026-10-27

### [Explicit-item matroid union](../problems/item-matroid-union/)

The complete explicit-item player-basis theorem and configuration-comparator upgrade: fat-item union and duality, rank-sensitive exact and positive-slack current-blocker bounds, recovery by dual-basis extension, fractional union domination and rational-grid target search. The inner player-eligibility, earliest-circuit exchange, refresh and signature arguments were inspected in the shared current-blocker proof.

**Dependencies and scope.** The original player matroid is supplied by an independence oracle. Polynomial matroid-union/partition and bipartite matching remain named, paid algorithmic dependencies; no unit-cost derived union oracle is assumed. The configuration LP is a proof comparator and is neither supplied nor enumerated by the algorithm. No guarantee against the unrestricted original compact LP is asserted. The new finite checker supports rank and recovery identities; it is not the polynomial union algorithm or a complete allocation implementation. The finite-rank factor tends to four, so no fixed improvement below four is claimed.

[Proof](../problems/item-matroid-union/proof.md) · [Dependencies](../problems/item-matroid-union/sources.md) · [Evidence](../problems/item-matroid-union/verify/README.md) · Reviewed 2026-10-27

### [One-value allocation](../problems/one-value-exact-two/)

The full one-value allocation family: the main exact factor-two theorem with arbitrary nonnegative assignment costs, the shared setup-and-assignment budget companion, every fixed integer approximation factor `d>=2`, corank weighted omission and streamed whole-ground conversion, exact prescribed-original-basis optimization, the direct Boolean-cap/assignment-pair one-unit gate and the inherited strict-below-two recipient-value-oracle boundary. The audit covers original loop deletion and free disposal, nonnegative projected separation, attained minimum-setup restriction and protected original full witness under adaptive residual budgets, exact maximum-total cost-minimizing quota recovery and nonmonotone one-sided integer optimization. The native complete-table client implements actual original-basis allocation through a direct capped-service primal/dual separator, exact dominant scalar recovery, canonical weighted pair intersection, omission and rational containment covers.

**Dependencies and scope.** There is one common positive value, one original player matroid, optional original-basis selection, arbitrary integral recipient polymatroids with unused capacity allowed, nonnegative setup and assignment costs, and one exact combined scalar budget. An unaffordable setup basis is zero-service infeasibility, distinct from zero optimum; the rank-zero output has no finite minimum utility. Prescribed-basis optimization remains an exact polynomial-oracle endpoint rather than an approximation claim. The sharp corank and fixed-integer whole-ground bounds charge the stated polynomial exact rank/SFM, rational LP and weighted matroid/polymatroid-intersection primitives. The native backend reuses exact Bland simplex with a separately charged potentially exponential finite basis bound and polynomial explicit-table/binary workspace. Its rational covers attain the sharp `d=2` and `d=3` endpoints; for other or varying binary d they use the certified rational envelope `3*(d+1)/(d-1)`, distinct from the proved sharp fixed-d algebraic comparison construction. No numerical capacity, quota or setup/assignment budget is expanded into unit copies. The strict-below-two obstruction is a deterministic recipient-value-oracle approximation boundary for the included zero-cost optional-basis subclass. It does not prove exponential bases optimal, apply to prescribed-basis exact optimization, or establish explicit-recipient-list hardness. Finite original-input checks support the complete manuscript arguments; proof-assistant formalization, external peer review and exhaustive publication-priority claims are not made.

[Proof](../problems/one-value-exact-two/proof.md) · [Dependencies](../problems/one-value-exact-two/sources.md) · [Evidence](../problems/one-value-exact-two/verify/README.md) · Reviewed 2026-10-27

### [Intrinsic two-value allocation](../problems/two-value-exact-two/)

The complete compulsory-player two-intrinsic-value arbitrary-assignment-cost theorem: polynomial affordable heavy-recipient parameter, attaining minimum original heavy completion, adaptive residual small-count region and protected pair, exact integral quota recovery, one-unit/pure-heavy/high-target boundaries, one-sided value-grid search and matching strict-below-two recipient-oracle threshold.

**Dependencies and scope.** All players are compulsory, values are intrinsic to disjoint heavy/light types and there is one exact nonnegative assignment-cost budget. Original heavy pairs remain available after every forced light omission; an attaining exact completion is required. Paid exact rank/SFM/LP and weighted matroid/integral polymatroid intersection retain their explicitly proved interfaces. The large-target branch uses the fixed compulsory set and cost-preserving additive rounding; no optional-player all-target LP is inferred. Shared reference evidence realizes weighted unit coverage, adaptive prefix recursion and native scalar setup flow. It does not implement the full two-value allocation LP/quota/rounding pipeline. Mathematical completeness is distinct from that software scope. The strict-below-two lower bound is deterministic hidden-set rank-oracle complexity for the same affordable-heavy parameter with zero costs. It does not imply ordinary explicit-eligibility hardness or an optimal exponential base.

[Proof](../problems/two-value-exact-two/proof.md) · [Dependencies](../problems/two-value-exact-two/sources.md) · [Evidence](../problems/two-value-exact-two/verify/README.md) · Reviewed 2026-10-27

### [Intrinsic values near factor two](../problems/intrinsic-values-near-two/)

The complete canonical intrinsic family: compulsory and arbitrary-original-player near-two theorems with exact threshold parameters; Boolean/dual-union rank identities, spanning and completion preserving a specified light basis; original light-resource fractional realization and joint lower rounding; full-accuracy fixed-family optimization; the published fallback and explicit dummy-dual transfer; exact-half XP/zero-corank/quantified-margin endpoints and their unresolved general-FPT boundary; and the aligned refined-parameter-zero deterministic oracle obstruction. Native reference executes actual prefix selection, certified union/heavy completion and original light recovery with separately charged finite LP basis cost.

**Dependencies and scope.** Values are common intrinsic values, original recipient polymatroids are independent, units may be unused, and no assignment/setup budget or coupled local type constraint is included. Original and derived loop restrictions preserve original resources; original player corank alone is not substituted for derived corank. Exact rank/SFM, LP, integral intersection and binary workload decomposition remain paid mathematical primitives. The external fixed-positive-slack fallback is Bamas et al., arXiv:2307.08453v1, Theorem 4 with its Definition 7 full-base model; the optional-player dummy M* transfer has been checked explicitly. The native backend accepts complete original rank tables and executes actual weighted prefix/rational search. Its original fractional realization and joint rounding stream active LP systems with a separate potentially exponential finite bound and polynomial rational workspace; no numeric resource expansion occurs. The default software does not implement the public fallback, although an original-feasible callback can be supplied and retained by actual value. Exact-half XP, zero-corank and quantified-margin statements use the half-optimum threshold. Unquantified strict light slack does not yield unrestricted exact-half FPT. The refined-zero lower bound concerns strictly-better-than-two deterministic black-box algorithms, not exact two, the unrefined heavy rank or explicit-table hardness.

[Proof](../problems/intrinsic-values-near-two/proof.md) · [Dependencies](../problems/intrinsic-values-near-two/sources.md) · [Evidence](../problems/intrinsic-values-near-two/verify/README.md) · Reviewed 2026-10-27

### [Unrelated-value additive allocation](../problems/unrelated-values-additive/)

The complete exact-budget unrelated-value additive theorem against the fractional optimum on an actual fixed-family selected set: nonnegative original service support separation, full-accuracy weighted omission, uniform denominator recovery and original fixed-set reoptimization, disposal/complement-prefix integral rounding with one exact cost objective, and fixed-accuracy whole-ground conversion.

**Dependencies and scope.** The original fixed-cardinality restriction selector and paid exact rational LP, rank/SFM and integral polymatroid intersection primitives remain mathematical dependencies. The fractional comparator relaxes resource counts, never mixes selected bases. Prefix rounding preserves one scalar assignment cost and loses the stated original largest unit per player. It supplies no positive multiplicative factor without controlling that additive term and does not preserve several independent cost budgets. Shared executable evidence realizes weighted selection, rational recovery and global cover primitives; no native general unrelated-value allocation or rounding solver is claimed. Positive-cost coordinates exceeding the whole budget remain in the fractional model unless a zero-budget exact mask applies. The sharp global expression uses fixed rational accuracy; binary-variable accuracy retains the stated rational upper-envelope implementation.

[Proof](../problems/unrelated-values-additive/proof.md) · [Dependencies](../problems/unrelated-values-additive/sources.md) · [Evidence](../problems/unrelated-values-additive/verify/README.md) · Reviewed 2026-10-27

### [Unrelated values with a joint role](../problems/unrelated-values-joint-role/)

Complete canonical family: unrelated player-type values with genuinely shared original recipient resources; exact scalar assignment budget; optional original player matroid and persistent zero-service dual dummy for one combined selected-player setup/assignment budget; fixed positive-accuracy near-two corank-plus-support and streamed whole-ground guarantees; arbitrary-value exact-two role endpoint; compulsory two-value exact quota and fixed-integer-factor tradeoffs; all target-search, count-floor, model-boundary and inherited below-two oracle statements. Native reference executes actual shared-resource LPs, first-crossing omission, block covers, signed-cost prefix recovery, exact-two role enumeration and compulsory quota target gates, with separately charged local finite LP cost.

**Dependencies and scope.** Original values, assignment costs and setup fees are nonnegative; recipient polymatroids are independent; unused units are allowed; exactly one combined scalar budget is preserved. Each original type has one shared rank system across all owner roles, and masks precede rounding. The zero-service M* dummy remains available at every omission node, including light owners. Its signed objective is internal affine setup accounting. Recovery optimizes one signed cost on the bounded integral prefix face after removing the budget halfspace, then extracts an original basis from dummy-free owners before discarding original nonnegative-cost assignments. The full mathematical fast time and polynomial workspace use paid polynomial exact rank/SFM, LP, matroid/polymatroid-intersection and streamed-cover primitives. The complete-table reference instead enumerates active LP bases and temporarily stores distinct projected support vertices, with potentially exponential local time and memory. Numerical resource counts remain binary. Exact Gamma power comparisons outside the safe rational 3R envelope have an explicit reference cost; the safe varying-accuracy branch avoids those huge powers. Compulsory two-value refinements do not extend to optional selection by a value-changing dummy. The native quota target routine loops every heavy cardinality and does not implement the mathematical affordable-support cap `nu_C`. A restricted near support budget counts original corank plus promised selected heavy recipients at the exact stated threshold. Below-two lower bounds concern arbitrary rank-value oracles through the intrinsic subclasses; no optimal base at exact factor two is asserted. Multiple independent exact assignment budgets, arbitrary negative original costs and a common robust fractional-dummy rounding are outside this theorem. Finite verification is not proof-assistant formalization or external peer review.

[Proof](../problems/unrelated-values-joint-role/proof.md) · [Dependencies](../problems/unrelated-values-joint-role/sources.md) · [Evidence](../problems/unrelated-values-joint-role/verify/README.md) · Reviewed 2026-10-27

### [Whole-ground selection and transfers](../problems/whole-ground-allocation/)

The complete whole-ground transfer family and all six shared components: actual weighted first-crossing omission with full unfinished/failed work accounting; attaining adaptive residual budgets; streamed logarithmic-block covers and corank-profile refinement; fixed-family rational comparator recovery; exact integer-quota endpoints/tradeoffs; every main allocation, scheduling and flow transfer; and the stated balanced deterministic rank-oracle barriers. Reference implements actual prefix recursion, block streaming, rational search, certified selectors and native fixed/adaptive flow gaps.

**Dependencies and scope.** Paid restriction/completion selectors, valid polynomial-bit separators, exact LP/SFM/intersection/decomposition and actual model-specific recovery remain stated mathematical primitives. Adaptive rows require the same original protected witness; local strict violation alone cannot certify that premise. The supplied rational-base reference implements exact block comparisons. Sharp algebraic Gamma global displays require fixed rational tradeoffs; varying binary inputs retain the supplied rational upper-envelope option and its encoding cost. The native flow integration executes real omission and exact witness recovery, but uses the canonical finite Bland simplex with separately charged potentially exponential LP cost. The code does not implement every allocation/scheduling recovery or arbitrary algebraic-number input. All selected sets and original ranks, mandatory totals, scalar budgets and comparators retain their own models. Heavy/light types must be intrinsically disjoint in that transfer; omitted light candidates keep original heavy options. Balanced lower bounds are deterministic black-box rank-oracle statements for strictly better factors, not explicit-input hardness or optimality of the threshold base.

[Proof](../problems/whole-ground-allocation/proof.md) · [Dependencies](../problems/whole-ground-allocation/sources.md) · [Evidence](../problems/whole-ground-allocation/verify/README.md) · Reviewed 2026-10-27

### [Selected concurrent flow](../problems/selected-flow/)

The complete selected concurrent-flow theorem with exact fixed-cardinality selection and nonnegative routing budgets: finite normalized Farkas separation, weighted first-crossing omission, zero-optimum handling, exact rational comparator recovery and fixed-accuracy whole-ground conversion. The exact reference adds fixed-set primal/dual certificates, physical undirected-capacity handling and native enumeration.

**Dependencies and scope.** Exact polynomial rational LP, Farkas duality and the specified paid selection oracle remain mathematical dependencies. The whole-ground sharp base is stated for fixed rational accuracy. Splittable rational flow is required; integral or unsplittable multicommodity routing is outside the model. The shipped reference uses finite Bland simplex and explicit selected-set enumeration with separate potentially exponential running times. It supplies exact fixed-set certificates and normalized separation, but not the omission recursion or rational target search. A fixed-set certificate proves that set optimal; global optimality of the enumeration baseline additionally depends on the fixed permitted-family predicate and complete enumeration.

[Proof](../problems/selected-flow/proof.md) · [Dependencies](../problems/selected-flow/sources.md) · [Evidence](../problems/selected-flow/verify/README.md) · Reviewed 2026-10-27

### [Flow with shared setup budget](../problems/shared-setup-flow/)

The complete selected-flow theorem with one shared commodity-setup and routing budget, including attained minimum-setup restriction optimization, the protected-witness invariant under adaptive residual budgets, exact Farkas separation, rational reoptimization and fixed-accuracy whole-ground conversion. The reference recomputes the actual set residual and supplies exact primal/dual certificates.

**Dependencies and scope.** Exact polynomial rational LP, Farkas duality and the specified paid selection oracle remain mathematical dependencies. The whole-ground sharp base is stated for fixed rational accuracy. Splittable rational flow is required; integral or unsplittable multicommodity routing is outside the model. The shipped reference uses finite Bland simplex and explicit selected-set enumeration with separate potentially exponential running times. It supplies exact fixed-set certificates and normalized separation, but not the omission recursion or rational target search. The minimum-setup restriction oracle must attain its minimum on the actual returned set. An existence-only selector or separately minimized unrelated setup objectives is insufficient. Fixed routing-only budgets remain allowed.

[Proof](../problems/shared-setup-flow/proof.md) · [Dependencies](../problems/shared-setup-flow/sources.md) · [Evidence](../problems/shared-setup-flow/verify/README.md) · Reviewed 2026-10-27

### [Robust selected flow](../problems/robust-scenario-flow/)

The complete adaptive explicit-scenario selected-flow theorem, including scenario-tagged nonnegative Farkas separation, original-coordinate weighted omission, fixed-family rational comparator recovery and fixed-accuracy whole-ground conversion; the parameter-preserving exact-admission Hitting Set reduction including its forest and nonconstant-gap scope. Exact reference supplies common-set certificates, separately scaled adaptive routings and scenario separation.

**Dependencies and scope.** Exact polynomial rational LP, Farkas duality and the paid fixed-family restriction selector remain theorem dependencies. The sharp whole-ground base requires fixed rational accuracy. Scenario list and routing-budget rows are explicit and charged. Selection is common, routing is adaptive and splittable. No implicit uncertainty, oblivious or unsplittable routing guarantee. Reference uses potentially exponential finite Bland simplex and original selected-set enumeration, not the omission recursion or rational target search. Search-free certificates prove fixed-set optimality; global optimality additionally relies on enumeration and the fixed-family predicate. W[2] hardness uses the source fact recorded by Jansen 2017 and the assumption FPT differs from W[2]. It concerns exact admission with arbitrary explicit scenarios, supplies no constant approximation gap and no single-edge-failure-only lower bound.

[Proof](../problems/robust-scenario-flow/proof.md) · [Dependencies](../problems/robust-scenario-flow/sources.md) · [Evidence](../problems/robust-scenario-flow/verify/README.md) · Reviewed 2026-10-27

### [Robust unrelated allocation](../problems/robust-unrelated-allocation/)

Complete canonical actual-common-basis fractional-comparator theorem with arbitrary scenario/player-specific values, recipient polymatroids and assignment costs; one common setup vector and exact scenario scalar budgets; attained minimum-setup restriction selection; intersected scenario nonnegative separation; same-basis protected witnesses through changing residual budgets; weighted prefix and streamed whole-ground time; full-accuracy original fixed-basis rational reoptimization; independent exact-budget scenario rounding; and role/dummy/common-setup boundary constructions. Native reference exercises this actual pipeline with original inputs and explicitly separate finite LP cost.

**Dependencies and scope.** The scenario list is explicit and nonempty. One actual original player-matroid basis is selected before the scenario; only assignments adapt. FOPT relaxes resource counts on one common actual basis and does not mix or change bases by scenario. Original counts may be unused and all original costs are nonnegative. The setup vector is identical in every scenario. Each current residual budget subtracts the cost of the same attaining minimum-setup basis. Arbitrary scenario-specific setup vectors, one common integer assignment or a common heavy/light role mask require additional arguments and are not included. The guarantee retains the scenario/player-specific largest-unit additive loss, including zero when it dominates. It does not provide an unrestricted positive multiplicative guarantee on zero/one robust instances or round a shared fractional dummy into one common integer selection. The fast mathematical bounds charge exact polynomial rank/SFM, LP, weighted intersection and streamed-cover primitives. The complete-table reference enumerates active LP systems and temporarily stores projected support vertices, with potentially exponential local time and memory separate from those bounds. It never expands binary resource units; original labels including loops are retained in software. Rank zero has an explicit empty-basis convention, outside the nontrivial positive-rank theorem. Independent original-input finite checks and code/manuscript reviews do not constitute proof-assistant formalization, external peer review or an exhaustive publication-priority search.

[Proof](../problems/robust-unrelated-allocation/proof.md) · [Dependencies](../problems/robust-unrelated-allocation/sources.md) · [Evidence](../problems/robust-unrelated-allocation/verify/README.md) · Reviewed 2026-10-27

### [Robust bounded-width certificates](../problems/robust-bounded-certificates/)

The complete bounded-certificate robust factor-d theorem: exact original budgeted unit tests and minimal failures, guarded common-basis extension, all-input forced-seed/node bounds, scenario-intersection support separation, exact integral high-quota recovery, one-sided target search and streamed global conversion. New reference realizes polynomial weighted matroid intersection with optimality/cut certificates, native budgeted unit scenarios and the bounded local gate.

**Dependencies and scope.** Original matroid/rank and Boolean-cap independence oracles must satisfy their declared contracts. The native complete-table adapter validates integral polymatroid tables and charges their full explicit encoding; no rank-only time bound is inferred by constructing those tables. Weighted augmentation and exchange-cycle optimality use Barasz et al., arXiv:2407.03229v2, Definition 2.2, Algorithm 2 and Lemma 2.5. Exact rational LP, submodular minimization and integral polymatroid intersection remain named paid mathematical dependencies for higher quotas. The software implements weighted intersection, exact unit tests/rejection certificates and bounded local extension, including actual integration with the Fibonacci client. It does not implement higher-quota LPs/recovery, integer target search or the streamed global wrapper. Width violation is a separate structural outcome and never failed extension. Scenario allocations are adaptive, one budget per allocation is exact, and binary capacities are not expanded. Sharp global bases retain fixed tradeoff parameters; binary-variable tradeoffs retain the stated rational upper-envelope option.

[Proof](../problems/robust-bounded-certificates/proof.md) · [Dependencies](../problems/robust-bounded-certificates/sources.md) · [Evidence](../problems/robust-bounded-certificates/verify/README.md) · Reviewed 2026-10-27

### [Width-two robust unit allocation](../problems/robust-width-two-allocation/)

The complete width-two robust theorem: exact unit gate and Boolean optimization, original dual-rank forced omissions, polynomial matching intersection/completion, Fibonacci all-input accounting and guarded outcomes, plus the Section 8 higher-quota factor-d composition and both fixed-tradeoff whole-ground conversions. The precise unchanged positive-quota packing/recovery chain has been checked against the complete bounded-certificate theorem.

**Dependencies and scope.** Original rank and exact hereditary scenario unit tests retain their paid model contracts. General budgeted unit tests now have the certified weighted bounded-certificate realization, directly compatible with the Fibonacci client. The unit gate changes only the one-time exact positivity cost; fixed original bases/ranks/scenario data, saved small-target witnesses, larger-quota separator and integral scenario recovery remain identical to BW. Local costs add, and global conversion is applied separately, proving the maximum base. The sharper global expressions require fixed tradeoff parameters. Each quota comparison uses a fixed rational power, and the unit gate uses exact quadratic arithmetic; no arbitrary real-number oracle is assumed. The width-two software implements the local unit gate and polynomial matching terminal; higher-quota LPs/recovery, target search and the streamed wrapper remain separate complete mathematical algorithms, not implemented features. Width violation remains a third structural outcome.

[Proof](../problems/robust-width-two-allocation/proof.md) · [Dependencies](../problems/robust-width-two-allocation/sources.md) · [Evidence](../problems/robust-width-two-allocation/verify/README.md) · Reviewed 2026-10-27

### [Two-scenario hardness](../problems/robust-two-scenario-hardness/)

The complete deterministic corank-parameterized finite-factor obstruction for optional common-basis selection under two exact scenario budgets, including positive-service equivalence to bounded nonnegative `k`-SUM, the always-feasible zero solution, binary encoding and parameter preservation.

**Dependencies and scope.** Uses the deterministic `W[1]`-hardness direction of Abboud, Lewi and Williams, Losing Weight by Gaining Edges, Definition 1.1, Theorem 1.3 and Section 4, and the assumption `FPT` differs from `W[1]`. The bounded nonnegative source avoids the separate randomized arbitrary-range reduction. The conclusion requires integer service, exact budgets and an optional common basis. It does not cover randomized algorithms, fractional service or relaxed budgets, and supplies no ETH or whole-ground exponential lower bound. Finite reduction checks do not certify the external hardness theorem.

[Proof](../problems/robust-two-scenario-hardness/proof.md) · [Dependencies](../problems/robust-two-scenario-hardness/sources.md) · [Evidence](../problems/robust-two-scenario-hardness/verify/README.md) · Reviewed 2026-10-27

### [Arbitrary-processing scheme](../problems/arbitrary-processing-scheduling/)

The complete exact-budget arbitrary-processing Theorem PS: original mandatory job-polymatroid bases, arbitrary nonnegative rational pair times/costs, exact bin boundaries, sparse occupied-bin grouping, load-pruned profile streaming with both composition and partition count bounds, one joint minimum-cost upper-prefix recovery, zero feasibility and one-sided grid optimization. The separate common-type-size slot-surplus Theorem S is also audited, including the fixed full-machine workload dual, binary scaled decomposition, guarded compressed count recursion, large-corank enumeration for polynomial space and the supplied-surplus-budget target search. The reference implements the PS profile and shared joint recovery semantics with explicit-table solver costs.

**Dependencies and scope.** The main approximation scheme uses the stated paid exact rank/SFM, rational LP and integral polymatroid-intersection primitives; its accuracy encoding and occupied-bin polynomial-space ledger remain explicit. The shipped reference shares canonical LP-vertex and numeric count enumeration, whose costs and potentially exponential vertex storage are charged separately from the fast theorem. The slot-surplus companion has common positive type sizes and no assignment budget. Its stronger bound retains the slot-surplus promise at OPT and the additive largest-smaller-job term, alongside the unconditional additive-largest-job fallback. That distinct compressed-slot algorithm is mathematically proved but not implemented by the profile reference. Finite reference tests, complete mathematical proofs, formal verification, external review and publication priority are distinct; the latter three are not claimed.

[Proof](../problems/arbitrary-processing-scheduling/proof.md) · [Dependencies](../problems/arbitrary-processing-scheduling/sources.md) · [Evidence](../problems/arbitrary-processing-scheduling/verify/README.md) · Reviewed 2026-10-27

### [Activated-machine scheduling](../problems/activated-machine-scheduling/)

The complete activated-basis Theorem AS: genuine fixed-cardinality activation bases, original mandatory job-polymatroid totals after eligibility/activation masks, one exact combined nonnegative setup-and-assignment budget, exact global/zero feasibility, active-rank profile enumeration for the approximation scheme, bucket curve and exact three-halves six-profile endpoint, one joint minimum-cost integer recovery and nonmonotone one-sided grid optimization. The fixed-cardinality polynomial-membership extension has the same proved enumeration interface. The complete-table reference realizes activation restriction, binary greedy feasibility and all three local profile clients with their inherited solver costs separate.

**Dependencies and scope.** The original theorem uses the stated paid exact matroid/rank/SFM, rational LP and integral polymatroid-intersection primitives. The reference streams actual bases and profiles and checks original totals before compressing to active coordinates, but its canonical positive-target solver retains explicitly charged LP-vertex and numeric count enumeration and potentially exponential vertex storage. The shared budget is one scalar setup-plus-assignment row; independent affordable pieces or a minimum-setup basis do not replace the joint capacity/cost test. Rank-zero and empty-job cases retain the actual activation requirement. Helper preconditions for genuine bases and already-masked ranks are documented and checked. Finite executable evidence, complete mathematical proof, formal verification, external review and publication priority remain distinct; formal verification, external peer review and exhaustive publication priority are not claimed.

[Proof](../problems/activated-machine-scheduling/proof.md) · [Dependencies](../problems/activated-machine-scheduling/sources.md) · [Evidence](../problems/activated-machine-scheduling/verify/README.md) · Reviewed 2026-10-27

### [Six-profile scheduling](../problems/six-profile-three-halves/)

The complete exact three-halves arbitrary-processing Theorem SX with mandatory original job-polymatroid bases and one exact assignment budget: six exact disjoint profiles, exhaustive one/two-big-unit coverage, original-total LPs, one joint prefix/partition integer cost recovery, zero processing, original-grid target search and complete streamed profile/time-space accounting. The reusable direct SixBackend lives with the activation adapter but implements the original SX model without activation.

**Dependencies and scope.** The theorem's polynomial per-profile exact LP/SFM and integral-intersection primitives remain explicitly paid. The reusable complete-table reference has separately charged canonical LP-vertex and numeric integer enumeration, including potentially exponential vertex storage; that implementation boundary is not an unresolved mathematical interface. The theorem permits arbitrary nonnegative machine/type times and one scalar assignment budget. No optimality of base six, general multiple-budget extension, exhaustive publication priority, proof-assistant formalization or external peer review is claimed.

[Proof](../problems/six-profile-three-halves/proof.md) · [Dependencies](../problems/six-profile-three-halves/sources.md) · [Evidence](../problems/six-profile-three-halves/verify/README.md) · Reviewed 2026-10-27

### [Processing-bucket tradeoff](../problems/processing-bucket-tradeoff/)

The complete arbitrary-time bucket-label Theorem AB and its depth/accuracy tradeoff: exact open-left/closed-right masks, full-target label witness, mandatory original bases and exact one-budget joint recovery, upper-prefix machine bounds, zero processing and one-sided grid optimization, complete depth-dependent enumeration accounting and optimality of the stated contiguous one-big-group analysis template. The reference bucket client instantiates the shared general-processing joint plan solver with separate finite solver costs.

**Dependencies and scope.** The theorem uses paid exact rank/SFM, rational LP and integral polymatroid-intersection primitives. The reference shares the canonical general-processing/two-time LP and numeric count baseline, preserving its explicit enumeration and vertex-storage costs rather than claiming the fast per-label implementation. Depth is charged numerically in the stated H+k bounds; no polynomial-in-log-depth claim is made, and no finite depth attains exact three-halves by this one-big-group construction. Template optimality is not a general scheduling lower bound. Finite executable evidence is not proof-assistant verification or external peer review; exhaustive publication priority is not claimed.

[Proof](../problems/processing-bucket-tradeoff/proof.md) · [Dependencies](../problems/processing-bucket-tradeoff/sources.md) · [Evidence](../problems/processing-bucket-tradeoff/verify/README.md) · Reviewed 2026-10-27

### [Two-size scheduling](../problems/two-size-scheduling/)

The complete two-common-positive-size scheduling family: Theorem D's exact three-halves corank approximation, its Boolean-rank-failure and empty-class branches, original full-machine box/dual reconstruction, guarded omission-batch node bound and strict-below-three-halves value-oracle obstruction; the distinct five-thirds large-unit-rank theorem, its private-slack residual-rank refinement and their explicitly promised fine-small-job variants; and the fixed-integer-d corank/whole-ground quota curve. The complete-table reference client realizes the hard-target corank construction and reuses the canonical two-time high-target LP baseline with separate implementation costs.

**Dependencies and scope.** All original mandatory bases, binary numerical encodings and paid exact rank/SFM, integral optimization/decomposition and additive rounding primitives retain their stated models. The distinct rank-based unit-core theorem uses the complete normalized-prefix and bounded-signature proof; a missing local-search implementation does not make that mathematical result conditional. The reference uses complete rank tables and actual guarded batch recursion. Its shared high-target solver has explicitly charged vertex and integer-count enumeration costs; it is not an implementation of the fast whole-ground wrapper or the large-unit-rank/private-slack local search. Fine-small-job and private-slack optimization promises remain explicit, and no uniform near-five-thirds rank-quasipolynomial result is inferred. The matching threshold obstruction concerns arbitrary value-oracle job polymatroids, not explicit restricted-assignment hardness or optimality of the exponential base. Finite executable tests, external review, formal verification and publication priority remain distinct.

[Proof](../problems/two-size-scheduling/proof.md) · [Dependencies](../problems/two-size-scheduling/sources.md) · [Evidence](../problems/two-size-scheduling/verify/README.md) · Reviewed 2026-10-27

### [Per-machine two-time scheduling](../problems/two-time-scheduling/)

The complete fixed-integer-d heterogeneous two-positive-processing-times-per-machine Theorem HT: original mandatory job-polymatroid bases, nonnegative rational times including zero, one exact assignment budget, exact small-quota gates, heterogeneous scaled support separators, protected omission recursion, joint minimum-cost integral recovery, streamed global conversion and one-sided rational-grid optimization. The complete-table reference realization has its own explicitly charged vertex, role and integer-count enumeration bound.

**Dependencies and scope.** The fast mathematical algorithm uses the explicitly paid exact rank/SFM, rational LP and integral polymatroid-intersection primitives. The reference backend implements semantic interfaces on complete rank tables by enumeration; it does not realize the fast theorem's time or polynomial workspace. The sharp base is for fixed integer `d>=2` and one scalar assignment budget. Finite executable tests have their stated scope; proof-assistant formalization, external peer review and publication priority are not claimed.

[Proof](../problems/two-time-scheduling/proof.md) · [Dependencies](../problems/two-time-scheduling/sources.md) · [Evidence](../problems/two-time-scheduling/verify/README.md) · Reviewed 2026-10-27

### [Many-size workload scheduling](../problems/many-size-scheduling/)

The complete many-common-size workload theorem: original mandatory integral job-polymatroid bases, binary workload aggregation, full-physical-machine box dual, large integer quota and rank-dependent unit-core transfer, scaled original-type decomposition, per-machine upper-prefix rounding with explicit largest-smaller-job additive term, exact one-size/easy/rank-loss branches and one-sided original-grid optimization with the public fallback. The linked private-slack exact finite-rank refinement is audited through its player-only contraction, engineered exact quota, private insertion, attained cap threshold and capped-comparator optimization. The native complete-table reference implements aggregation, binary scaled decomposition, upper rounding, original equal-largest-type recovery and both target/search variants, with weak-basis and active-system enumeration costs separate.

**Dependencies and scope.** The guarantees retain the explicit additive largest-smaller-job term; a purely multiplicative near-five-thirds consequence needs the stated size-gap condition. This common-type-size transfer has no arbitrary assignment-cost budget. The private refinement compares against the larger of the original optimum and its own attained cap threshold; cap failure is not original infeasibility. The fast theorem uses the proved normalized rank-search and paid exact rank/SFM, integral decomposition/intersection and rounding primitives. The native reference instead enumerates weak selected bases and streams exact mandatory-base LP active systems, with explicit finite time costs and polynomial rational workspace in its complete-table/binary encoding. Generic intrinsic LP primitives are reused; optional allocation, disposal and lower-rounding interfaces are not transferred into this mandatory scheduling model. Binary counts, artificial workload multipliers and accuracy/rank/divisor encodings remain binary; no numerical unit expansion occurs. Finite reference evidence, complete asymptotic proof, proof-assistant formalization, external review and publication priority are distinct; the latter three are not claimed.

[Proof](../problems/many-size-scheduling/proof.md) · [Dependencies](../problems/many-size-scheduling/sources.md) · [Evidence](../problems/many-size-scheduling/verify/README.md) · Reviewed 2026-10-27

### [Commitment scheduling](../problems/commitment-scheduling/)

All three canonical commitment manuscripts: original-optimum homogeneous-largest workload and exact two-size bottleneck commitments; full-marginal machine contraction with actual dominated residual bases, order-independent closures and the all-budget greedy profile; and local eligibility/collision padding including exact scalar optimization, its correct grid and approximation scope. The native modules realize both main original-optimum clients, safe absorption and lifting, position contractions and local structural certificates on original complete rank tables.

**Dependencies and scope.** The mathematical bounds pay for rank/SFM, integral decomposition/intersection, LP and the normalized-prefix unit search. Native clients instead stream residual original subsets and exact LP active systems with separately charged finite time and polynomial binary workspace. No capacity or artificial workload multiplier is expanded into individual jobs. All models use common positive type sizes and no assignment/setup budget. Commitment bottlenecks are explicit load terms, with no implicit bound by original optimum; private-cap and original-optimum comparisons remain distinct. Exact two-size recovery admits noninteger size ratios and incurs no smaller-job additive loss. The complete heterogeneous-large padding allocator and specialized public two-size approximation are not implemented. Scalar optimization is only for the stated padding certificate, and full-marginal closure optimality applies only to its absorption rule. No external peer review or proof-assistant verification is claimed.

[Proof](../problems/commitment-scheduling/proof.md) · [Dependencies](../problems/commitment-scheduling/sources.md) · [Evidence](../problems/commitment-scheduling/verify/README.md) · Reviewed 2026-10-27

### [Hypergraph matching and expander routing](../problems/strong-haxell-matching/)

The explicit certifying hypergraph-matching algorithm, including build/growth/collapse and weighted finite-prefix termination; the public explicit-algorithm weighted reanalysis; certified disjoint-path routing and spanning-expander packing. The destructive-support extractor, exact-size auxiliary graph and route/conductance accounting are explicitly instantiated. The retained rank-sensitive layer count, its separate root factor and the fixed-right-rank polynomial-strength consequence are included; explicit incidence input is not replaced by an implicit graph-edge count.

**Dependencies and scope.** The hitting, expansion, density, load and input-size promises remain part of their respective theorems. The companion’s separate conditional observation about the public approximate-extension algorithm is not used by these results and retains its stated assumption. Manuscript readiness does not claim a full executable implementation.

[Proof](../problems/strong-haxell-matching/proof.md) · [Dependencies](../problems/strong-haxell-matching/sources.md) · [Evidence](../problems/strong-haxell-matching/verify/README.md) · Reviewed 2026-10-26

### [Allocation and scheduling barriers](../problems/allocation-lower-bounds/)

The deterministic rank/corank oracle barriers below factor two for allocation and below three halves for scheduling; the refined-parameter-zero barrier at threshold `OPT/(2+eta)`; the aggregate configuration gap approaching the selection rank and full-residual gap exactly two. The greedy residual-capacity identity and both explicit component decompositions have direct local proofs.

**Dependencies and scope.** The lower bounds use arbitrary integral recipient or job polymatroids in the full value-oracle model. They do not assert randomized lower bounds or NP/ETH hardness for explicit restricted-assignment inputs. The refined compulsory parameter is zero while its unrefined heavy-cover rank grows with the ground. The four-unit promise/two-unit output problem is separate and is not settled by these examples. Finite checks support the constructions, not the unbounded transcript argument.

[Proof](../problems/allocation-lower-bounds/proof.md) · [Dependencies](../problems/allocation-lower-bounds/sources.md) · [Evidence](../problems/allocation-lower-bounds/verify/README.md) · Reviewed 2026-10-27

### [Self-concordant cone sparsification](../problems/conic-barrier-sparsification/)

The cone-order sparsification theorem and its boundary-sum proof have been checked against the imported geometric statements. The manuscript separates existence, dual/face/lift consequences, and a conditional randomized separation-oracle construction.

**Dependencies and scope.** Reis--Rothvoss Lemma 18 and Theorems 7 and 22 are essential published inputs; the directional barrier inequality and duality are standard cited results. The two supplied research-session audits identified no substantive proof gap. They are not external peer review or formal verification. No general Turing bit-complexity bound, deterministic construction, or exhaustive historical-priority claim is made.

[Proof](../problems/conic-barrier-sparsification/proof.md) · [Dependencies](../problems/conic-barrier-sparsification/sources.md) · [Evidence](../problems/conic-barrier-sparsification/verify/README.md) · Reviewed 2026-10-26

### [Deterministic PIT for fixed-width affine ROABP orbits](../problems/roabp-affine-pit/)

The complete general fixed-width affine-orbit PIT proof and direction-grid refinement have separate exact-source internal reconstructions, including a fresh-context review of the weighted Artin induction. Arbitrary local ranks, unrestricted local entry degrees and every characteristic are covered.

**Dependencies and scope.** The promise is one unknown-order ROABP under an invertible affine map, with a known scalar total-degree bound; small base fields require extension-field oracle access. The polynomial query exponent depends on width; no FPT, unbounded-width polynomial-time, singular-projection or orbit-closure claim is made. The generic Hasse pivot criterion is standard and attributed. Internal model-assisted review, finite tests and presentation checks are not external peer review, proof-assistant verification or priority certification.

[Proof](../problems/roabp-affine-pit/proof.md) · [Dependencies](../problems/roabp-affine-pit/sources.md) · [Evidence](../problems/roabp-affine-pit/verify/README.md) · Reviewed 2026-10-27

## Components ready for review

### [Numeric targets and support patterns](../problems/numeric-target-frontier/)

The complete central BC budget-classification proof, including its original-support and total-target upper dependencies and calibrated bounded-error hidden-matroid query lower bound; the complete UP useful-prefix/interval construction; the complete CC mixed-target chain representation and direct bounded coefficient-profile recovery/counts. Includes a native CC exact mixed-target signed-scalar solver with original eligibility, optional versus mandatory mass, polynomial copied-ground representation, streamed occupied profiles, exact shared-resource recovery and producer-independent original verification.

**Dependencies and scope.** The executable implements CC covering-row permutations, retaining its explicit factorial cover factor; it does not implement the stronger mixed-support UP interval compiler. Generic streamed exact LP recovery has a separately charged `binom(M,D)` active-system factor for actual remaining rows and free dimension. The fast mathematical bounds pay named polynomial SFM/weighted-intersection primitives. Complete original-table input, all rational work and binary ranks/targets are charged; no copied-ground subset table or resource-unit list is expanded. This partial review does not cover the seven approximation schemes and constants, every fixed-dimensional/single-objective/support-geometric refinement, all encoded ETH families or nonlinear/global/mandatory/robust compositions. Those retain their linked mathematical statements and dependencies; no whole-family readiness is claimed. The BC lower bound is worst-case under parameter upper budgets in the rank-oracle model, including its stated bounded-error scope. It is not an exact-pair or representation-independent hardness statement. Finite exact checks and internal proof review are not proof-assistant formalization, external peer review or an exhaustive priority audit.

[Proof](../problems/numeric-target-frontier/proof.md) · [Dependencies](../problems/numeric-target-frontier/sources.md) · [Evidence](../problems/numeric-target-frontier/verify/README.md) · Reviewed 2026-10-27

### [Prefix, laminar and sparse quotas](../problems/weighted-prefix-quota-frontier/)

The complete one-common-order exact mixed-prefix companion: common nonnegative integer weights, optional independent vectors or original-total mandatory bases, arbitrary signed rational scalar optimization, original eligibility and quota dominance, safe upper masks, shared active/passive copying and capped lower credit, a single charged marked prefix, actual support colors, colored-partition profile counting, exact resource/partition recovery, all-input traversal and uniform binary workspace. The associated sparse-paving oracle-query and separately encoded deterministic-ETH lower constructions and discrepancy scope boundary are audited. Native complete-table software now implements actual original-input one-order profiles and signed optimization. The prior scope is retained: sharp sparse-packing FPT restriction with improved basis-tree preprocessing, arbitrary signed-profit ordered extension, capacity-sensitive failure budget, exact original-context lower construction, aggregate laminar lower-row reduction, exact dominant-weight completion including signed zero-coordinate costs, binary count-rank recovery, one-positive-weight polynomial endpoint, elementary `10/9` and named universal-set `5/9` refinements, projected coloring and histogram-sensitive recovery; compatible cuts and two-positive-weight oracle/encoded-program boundaries remain separately proved. Also includes the complete bounded two-order/common-weight and common-order/variable-family companions: simultaneous independent marks, reversed-order and original-support refinements, streamed covering-family stopping chains with only `s+1` copied layers, actual collapsed-vector classes and their alphabet-and-cuts count, exact original signed recovery and all-input binary workspace. The joint target/family query lower grid and separately calibrated readable-program ETH, including optional scalar versus mandatory-feasibility distinctions, are audited. Native TwoOrders and Families share the original-subset resource recovery with Prefix.

**Dependencies and scope.** The prefix native scope comprises one common-weight order, two common-weight orders, and variable nonnegative integer weight families on one common order. Every client retains one original global integral polymatroid, one signed scalar, original mandatory total or explicit optional disposal, actual real zero-column costs and original eligibility. Shared copied resource recovery uses original subset rows, without a copied-ground rank table or resource-unit expansion. Arbitrary combined order/family geometry and the broader sparse-hash, kernel and laminar-coloring dependency chains remain outside this added bounded audit; the family retains partial readiness. The mathematical prefix theorems charge paid polynomial exact integral-polymatroid optimization. The native clients reuse canonical exact Bland simplex with a separately charged potentially exponential basis factor and polynomial complete-table/binary workspace. Original Prefix API and its 956-solve checker remain unchanged. TwoOrders charges one common capped magnitude per copied unit; Families charges its collapsed-vector `l1` mass and streams covering-family permutations with at most `p+1` layers, without enumerating all family subsets. The parameter time depends on the largest numeric target, while workspace is polynomial in numeric bit length. The retained laminar `5/9` coefficient specifically imports Naor-Schulman-Srinivasan Theorem 7 and its local indexing guarantee; the elementary `10/9` alternative has its local proof. Compatible-cut one-weight polynomial optimization requires prescribed or forced total numeric mass. General resource calls retain the named SFM and integral-polymatroid primitives. Oracle-query, encoded-rank-program ETH and explicit represented-resource models remain distinct. Finite checks and independent internal review are not proof-assistant verification, external peer review or exhaustive priority claims.

[Proof](../problems/weighted-prefix-quota-frontier/proof.md) · [Dependencies](../problems/weighted-prefix-quota-frontier/sources.md) · [Evidence](../problems/weighted-prefix-quota-frontier/verify/README.md) · Reviewed 2026-10-27

### [Single-failure optimum preservers](../problems/exact-failure-preservers/)

The complete ordinary fixed-rank signed-cost two-matroid and initialized rooted-arborescence reporting scope, extended to ordinary minimum-cost maximum-cardinality reporting through two consecutive ranks; and the complete fixed-rank valuated companion proof, with a native independently certified supplied-common-baseline price interface and compact value/path reporting. Covers local-to-global and initial matroids, joint convex decomposition, valued matching and cycle identity, minimum-hop literal update, signed shortest paths, phased reporting, original-ID infeasibility and actual rational/temporary versus retained-record costs.

**Dependencies and scope.** Ordinary maximum-cardinality initialization uses the canonical certified polynomial weighted-intersection primitive and separately initializes the next lower rank. The valued software requires a supplied common finite basis, certifies optimality through original split-price exchange inequalities and rejects a nonoptimal basis; it does not implement native valuated baseline search. The classical mathematical initializer and effective-domain initialization remain separately paid, as specified by Iwamasa–Takazawa v3 Lemma 7. Valid ordinary matroids and valid fixed-rank minimization-convention valuated matroids are oracle-model assumptions. Independent tiny valuation tables check their exchange axioms in full, but native baseline certificates verify optimality conditional on those axioms. Value callbacks use exact binary rational values and None outside the domain. No smaller-rank valuation or cross-rank objective is inferred. Valued baseline verification/compression uses `O(Nk)` evaluations and `O(Nk^2+k^3)` additional arithmetic; original answer bit lengths are charged. Original-ground price certificates, initialization certificates, exchange tables and callbacks are discarded before returning compact reporters. Separately retained price evidence is outside the `O(k^(3/2))` reporting-record bound. The graph wrapper still does not implement the optimized arborescence preprocessing. Lower-bound transfers, simultaneous failures and later-changing costs or valuations remain outside this review. Exact finite checks, internal proof audit and independent certificate verification are not external peer review or proof-assistant formalization.

[Proof](../problems/exact-failure-preservers/proof.md) · [Dependencies](../problems/exact-failure-preservers/sources.md) · [Evidence](../problems/exact-failure-preservers/verify/README.md) · Reviewed 2026-10-27

### [Flow, matching and price sensitivity](../problems/exact-flow-sensitivity/)

The exact nonnegative rational unit-flow and internally vertex-disjoint path components: fixed-value and minimum-cost maximum queries, residual replacement, support-sensitive original-record preservers, compact reports and simple-input support specializations. The native path wrapper proves unit-gate deletion semantics, original-ID recovery and zero-cost-cycle-safe packing output. Both local realizations prove their own polynomial preprocessing and bit-cost contracts. The independent original-input certificate component proves signed-cost reduced-cost optimality, maximum-value and infeasibility cuts, and a binary-input cost-blind general-balance constructor. The signed unit-flow realization completes native minimum-cost initialization for arbitrary integral balances, negative cycles and loops, and compact fixed-balance and maximum-value deletion reporting with deterministic decoding. The complete ordinary fixed-rank price-change and supplied-catalog insertion identity, minimum-hop literal recovery and all-pairs reporting alternative are audited and implemented with native certified ordinary initialization.

**Dependencies and scope.** Parallel original records are supported under the support-sensitive bound; the uniform flow-value-dependent support exponent additionally requires a simple original digraph. Queries are independent single-record deletions, not cumulative updates. The native path wrapper requires simple directed input and one independent original-arc or internal-vertex failure. Terminal deletions and simultaneous failures are excluded. Its full packing output uses linear record work. The original nonnegative flow references use exact fractions and Python hash tables. Signed-flow and ordinary price reporters use deterministic dense decoding. All charge actual rational bit work and polynomial preprocessing separately from faster research bounds. General-matching and unweighted matroid support companions, specialized arborescence price machinery and valuated price software remain outside this reviewed component scope. Independent certificates scan the full surviving original graph, with separately charged production and verification; these costs do not inherit the compact oracle query bound. The general-balance constructor ignores costs. The separate signed optimizer initializes its own optimum; final signed reporting bounds use actual baseline support including negative cycles, not flow value. The native price backend handles ordinary matroid independence oracles, one independent cost increment or one inactive supplied-catalog insertion, and a prescribed common rank. It realizes the stated `O(N+r^2)` record alternative with `O(r)` output work, not the stronger pair-preserver record bound. It does not implement valuated prices, arbitrary uncatalogued arborescence insertion or an insertion-induced rank increase.

[Proof](../problems/exact-flow-sensitivity/proof.md) · [Dependencies](../problems/exact-flow-sensitivity/sources.md) · [Evidence](../problems/exact-flow-sensitivity/verify/README.md) · Reviewed 2026-10-27

### [Correlated spectral, regression and seminorm summaries](../problems/correlated-spectral-regression/)

The exact rational arbitrary-rank PSD importance core with possibly singular fixed background, deletion monotonicity and effective-dimension accounting, sharper one-label-failure maxima, supplied-pool estimator with separate deterministic mass and probabilistic domination contracts, conservative preflight gates, exact fixed-scenario all-vector embedding checks, and the supplied-response unconstrained ridge realization. Mathematical review includes the weak convex-regression bilinear lemma with its convexity, attainment and nonnegative-penalty hypotheses.

**Dependencies and scope.** The reference does not generate random pools, sample a sparse summary or implement matrix-exponential derandomization. Supplied-pool certificates prove exact score/mass accounting; coverage and simultaneous domination remain separate probability events in the mathematical theorem. Nontrivial planner modes return `weights=None`. The ridge solver implements unconstrained quadratic objectives. General convex constrained/penalized minimization, RIP/coherence codes, graded incidence software, Lewis weights and whole-seminorm backends are outside this implementation and scoped readiness. Their mathematical claims remain separately stated with primary dependencies. Fixed-scenario embedding checks prove PSD inequalities for all real vectors in that scenario, without asserting all-failure sampling success. Exact rational bit lengths and explicit input/certificate matrix dimensions are charged. No external peer review or proof-assistant verification is claimed.

[Proof](../problems/correlated-spectral-regression/proof.md) · [Dependencies](../problems/correlated-spectral-regression/sources.md) · [Evidence](../problems/correlated-spectral-regression/verify/README.md) · Reviewed 2026-10-27

### [Label and whole-block cut sparsification](../problems/label-block-cut/)

The exact rational whole-block incidence-label compiler and decoder, original-row rank compression, common item scalar, original-ID whole-block rank and subspace-query interfaces, uniform full-input dimension gate, and mathematical composition with Quanrud quotient sparsification and the integer-rank adaptive restriction/error/probability/bit ledger.

**Dependencies and scope.** The deterministic reference retains the original input and, in `LIFT` mode, its complete compiled blocks. It is not a sampled sparse summary and implements neither the published quotient sampler nor adaptive resparsification. Those remain completed mathematical constructions through the identified published backend. This review does not cover finite-field extension software, the rational subgroup-rank client, quantum stabilizer algebra or support lower-bound reductions. Their mathematical statements and primary dependencies remain separately recorded. Exact rational bit work is charged; `FULL_INPUT` returns before monomial enumeration or polynomial multiplication when positive-rank formal dimension is at least item count. Finite executable checks are not proof-assistant verification or external peer review.

[Proof](../problems/label-block-cut/proof.md) · [Dependencies](../problems/label-block-cut/sources.md) · [Evidence](../problems/label-block-cut/verify/README.md) · Reviewed 2026-10-27

### [Finite groups, affine constraints and metrics](../problems/group-metric-constraints/)

The exact whole-coset algebraic compiler on validated explicit finite-group tables: generated subgroups, one common implicit wreath product, whole original-item membership and reweighting identities, empty/whole predicates, and exact original-query coefficient verification with optional total weight. The established subgroup construction is credited and the local implementation has explicit table, generator, rational-bit and hash-operation costs.

**Dependencies and scope.** The original multiplication table is explicit. The construction supports nonabelian groups, nonnormal subgroups and inconsistent cosets; it does not claim polynomial time in a compact group presentation. This is an algebraic compiler and verifier, not a sparse coefficient sampler. Gaussian subgroup support, Cayley spectral constructions, compact modular rationalization and metric extensions remain outside this bounded review. Original item IDs and whole predicates are retained. The item-independent query embedding is not assumed to be a homomorphism. Finite group/permutation checks support the symbolic identities and are not formal or external peer review.

[Proof](../problems/group-metric-constraints/proof.md) · [Dependencies](../problems/group-metric-constraints/sources.md) · [Evidence](../problems/group-metric-constraints/verify/README.md) · Reviewed 2026-10-27

### [Pauli, qudit and stabilizer blocks](../problems/quantum-stabilizer/)

The deterministic Pauli stabilizer-basis surrogate and witness theorem (main Theorem 5 and witness Theorem 1), including exact affine-parity enumeration, and the prime-dimensional individual-check witness reduction (witness Corollary 2). Pairwise operator comparisons, complete-basis pinching, exact basis-energy equality and compact tableau output are explicit. The native Pauli backend realizes original-weight balanced peeling, phase-aware maximal isotropic extension, exact original scalar/parity compilation and effective-rank enumeration. Independent verification uses a separate local multiplication table and checks complete original-input tableau energy without importing producer algebra.

**Dependencies and scope.** The polynomial-time reduction produces a classical objective; exact minimization still uses `2^d poly(L)` enumeration for Pauli labels or `p^n poly(L)` for prime-dimensional checks, with polynomial workspace. This is not a polynomial-time ground-state optimizer. This review uses compact symplectic/stabilizer linear algebra and does not certify the separate whole-block sparsification, adaptive quotient, correlated-failure or joint lower-bound dependency chains. The shared finite quotient-rounding checker is not evidence for quantum operator inequalities; those are proved symbolically. The executable implements Pauli witnesses only. Native minimization finds the optimum within its constructed basis using `2^d` enumeration and polynomial space; it does not optimize over every stabilizer basis. The verifier checks actual original energy, not global optimality or an arbitrary supplied approximation claim. Prime-dimensional Weyl witness construction remains a proved but unimplemented software interface.

[Proof](../problems/quantum-stabilizer/proof.md) · [Dependencies](../problems/quantum-stabilizer/sources.md) · [Evidence](../problems/quantum-stabilizer/verify/README.md) · Reviewed 2026-10-27

### [Independent transversals](../problems/independent-transversal/)

The complete elementary certifying fallback: induced-star current-blocker invariants, strict earlier-star zero-blocker cascades, positive-composition signature bound, exact total-domination/constellation output and independent original-input verification. The derived public procedure has a new local executable realization and separately charged exponential-in-class-count work.

**Dependencies and scope.** The elementary procedure is credited to Graf and Haxell, arXiv:1811.02687v2, Definition 3 and Section 2. It requires no claw or slack promise. Within-class edges are removed exactly as in the source convention. A domination constellation is not a certificate that no independent transversal exists. The verifier checks the precise elementary alternative and no stronger infeasibility claim. The faster current-blocker layer theorem and its input-linear layer primitives remain outside this bounded review scope. Python hash-table operations and optional observer costs are separately charged; no fast-layer implementation or formal verification is claimed.

[Proof](../problems/independent-transversal/proof.md) · [Dependencies](../problems/independent-transversal/sources.md) · [Evidence](../problems/independent-transversal/verify/README.md) · Reviewed 2026-10-27

## Review pending

These families have not yet received a scoped readiness entry in this registry. Their existing statements retain their own assumptions.


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

**Ready for review.** The binomial determinant formula and original-field actual-curve construction have a complete symbolic proof and a separate internal reconstruction. The first ordinary homogeneous component has digit degree exactly `w^2-1`.

**Dependencies and scope.** Width `w>=2` and prime characteristic `p>w^2+w-2`; the construction uses `n=p` coordinates and scalar total degree `2p(w-1)`. The curve is the ordinary moment curve, whose `p`-th coordinate has zero derivative. This is not a counterexample to a derivative-separating-curve theorem. Every physical interval preserves full rank. The endpoint-augmented scalar interval does not. One SV pair detects the example, so no PIT or generator lower bound is asserted. The audit is internal model-assisted reconstruction, not external peer review, formal certification or priority determination.

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
- [problems/activated-machine-scheduling/verify/check_activation.py](../problems/activated-machine-scheduling/verify/check_activation.py)
- [problems/activated-machine-scheduling/verify/check_six_profiles.py](../problems/activated-machine-scheduling/verify/check_six_profiles.py)
- [problems/allocation-lower-bounds/verify/check_barriers.py](../problems/allocation-lower-bounds/verify/check_barriers.py)
- [problems/arbitrary-processing-scheduling/verify/check_profiles.py](../problems/arbitrary-processing-scheduling/verify/check_profiles.py)
- [problems/arbitrary-value-allocation-scheme/verify/check_scheme.py](../problems/arbitrary-value-allocation-scheme/verify/check_scheme.py)
- [problems/boolean-linear-compiler/verify/check_cardinality_compiler.py](../problems/boolean-linear-compiler/verify/check_cardinality_compiler.py)
- [problems/boolean-linear-compiler/verify/check_interval_compiler.py](../problems/boolean-linear-compiler/verify/check_interval_compiler.py)
- [problems/commitment-scheduling/verify/check_absorption.py](../problems/commitment-scheduling/verify/check_absorption.py)
- [problems/commitment-scheduling/verify/check_commitment_client.py](../problems/commitment-scheduling/verify/check_commitment_client.py)
- [problems/commitment-scheduling/verify/check_commitment_profiles.py](../problems/commitment-scheduling/verify/check_commitment_profiles.py)
- [problems/correlated-spectral-regression/verify/check_importance_regression.py](../problems/correlated-spectral-regression/verify/check_importance_regression.py)
- [problems/degree-constrained-subgraphs/verify/check_linear_selector.py](../problems/degree-constrained-subgraphs/verify/check_linear_selector.py)
- [problems/degree-constrained-subgraphs/verify/check_reductions.py](../problems/degree-constrained-subgraphs/verify/check_reductions.py)
- [problems/degree-constrained-subgraphs/verify/check_reference.py](../problems/degree-constrained-subgraphs/verify/check_reference.py)
- [problems/exact-failure-preservers/verify/check_arborescence_reporting.py](../problems/exact-failure-preservers/verify/check_arborescence_reporting.py)
- [problems/exact-failure-preservers/verify/check_matroid_reporting.py](../problems/exact-failure-preservers/verify/check_matroid_reporting.py)
- [problems/exact-failure-preservers/verify/check_valuated_rank_drop.py](../problems/exact-failure-preservers/verify/check_valuated_rank_drop.py)
- [problems/exact-flow-sensitivity/verify/check_flow_certificates.py](../problems/exact-flow-sensitivity/verify/check_flow_certificates.py)
- [problems/exact-flow-sensitivity/verify/check_price.py](../problems/exact-flow-sensitivity/verify/check_price.py)
- [problems/exact-flow-sensitivity/verify/check_signed_flow.py](../problems/exact-flow-sensitivity/verify/check_signed_flow.py)
- [problems/exact-flow-sensitivity/verify/check_unit_flow.py](../problems/exact-flow-sensitivity/verify/check_unit_flow.py)
- [problems/exact-flow-sensitivity/verify/check_vertex_paths.py](../problems/exact-flow-sensitivity/verify/check_vertex_paths.py)
- [problems/general-matching/verify/check_bipartite.py](../problems/general-matching/verify/check_bipartite.py)
- [problems/general-matching/verify/check_certificate_search.py](../problems/general-matching/verify/check_certificate_search.py)
- [problems/general-matching/verify/check_cover_compression.py](../problems/general-matching/verify/check_cover_compression.py)
- [problems/general-matching/verify/check_failure_kernel.py](../problems/general-matching/verify/check_failure_kernel.py)
- [problems/general-matching/verify/check_failure_query.py](../problems/general-matching/verify/check_failure_query.py)
- [problems/general-matching/verify/check_failure_query_certificate.py](../problems/general-matching/verify/check_failure_query_certificate.py)
- [problems/general-matching/verify/check_reductions.py](../problems/general-matching/verify/check_reductions.py)
- [problems/general-matching/verify/check_reference.py](../problems/general-matching/verify/check_reference.py)
- [problems/graph-color-failure-certificates/verify/check_list_colors.py](../problems/graph-color-failure-certificates/verify/check_list_colors.py)
- [problems/graph-color-failure-certificates/verify/check_vertex_colors.py](../problems/graph-color-failure-certificates/verify/check_vertex_colors.py)
- [problems/group-metric-constraints/verify/check_coset_compiler.py](../problems/group-metric-constraints/verify/check_coset_compiler.py)
- [problems/group-metric-constraints/verify/check_quotient_rounding.py](../problems/group-metric-constraints/verify/check_quotient_rounding.py)
- [problems/incremental-scc/verify/check_label_history.py](../problems/incremental-scc/verify/check_label_history.py)
- [problems/incremental-sssp/verify/check_path_reporting.py](../problems/incremental-sssp/verify/check_path_reporting.py)
- [problems/independent-transversal/verify/check_elementary.py](../problems/independent-transversal/verify/check_elementary.py)
- [problems/intrinsic-values-near-two/verify/check_intrinsic.py](../problems/intrinsic-values-near-two/verify/check_intrinsic.py)
- [problems/item-matroid-union/verify/check_union_reduction.py](../problems/item-matroid-union/verify/check_union_reduction.py)
- [problems/label-block-cut/verify/check_whole_blocks.py](../problems/label-block-cut/verify/check_whole_blocks.py)
- [problems/many-size-scheduling/verify/check_workload.py](../problems/many-size-scheduling/verify/check_workload.py)
- [problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py](../problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py)
- [problems/matroid-failure-summaries/verify/check_rank_two_prefix.py](../problems/matroid-failure-summaries/verify/check_rank_two_prefix.py)
- [problems/matroid-failure-summaries/verify/check_single_replacement.py](../problems/matroid-failure-summaries/verify/check_single_replacement.py)
- [problems/matroid-failure-summaries/verify/check_summaries.py](../problems/matroid-failure-summaries/verify/check_summaries.py)
- [problems/matroid-failure-summaries/verify/check_weighted_obstruction.py](../problems/matroid-failure-summaries/verify/check_weighted_obstruction.py)
- [problems/matroid-failure-summaries/verify/check_weighted_prefix.py](../problems/matroid-failure-summaries/verify/check_weighted_prefix.py)
- [problems/min-cost-flow/verify/check_capacity_scaling.py](../problems/min-cost-flow/verify/check_capacity_scaling.py)
- [problems/min-cost-flow/verify/check_recovery.py](../problems/min-cost-flow/verify/check_recovery.py)
- [problems/numeric-target-frontier/verify/check_targets.py](../problems/numeric-target-frontier/verify/check_targets.py)
- [problems/obstruction-boundaries/verify/check_compact_body.py](../problems/obstruction-boundaries/verify/check_compact_body.py)
- [problems/one-value-exact-two/verify/check_one_unit_gate.py](../problems/one-value-exact-two/verify/check_one_unit_gate.py)
- [problems/one-value-exact-two/verify/check_one_value.py](../problems/one-value-exact-two/verify/check_one_value.py)
- [problems/packing-matching-summaries/verify/check_product_summary.py](../problems/packing-matching-summaries/verify/check_product_summary.py)
- [problems/persistence-failure-certificates/verify/check_feature_construction.py](../problems/persistence-failure-certificates/verify/check_feature_construction.py)
- [problems/persistence-failure-certificates/verify/check_incidence.py](../problems/persistence-failure-certificates/verify/check_incidence.py)
- [problems/processing-bucket-tradeoff/verify/check_buckets.py](../problems/processing-bucket-tradeoff/verify/check_buckets.py)
- [problems/quantum-stabilizer/verify/check_witness.py](../problems/quantum-stabilizer/verify/check_witness.py)
- [problems/recipient-matroid-configuration/verify/check_reservations.py](../problems/recipient-matroid-configuration/verify/check_reservations.py)
- [problems/recipient-polymatroid/verify/check_counts.py](../problems/recipient-polymatroid/verify/check_counts.py)
- [problems/recipient-polymatroid/verify/check_fractional.py](../problems/recipient-polymatroid/verify/check_fractional.py)
- [problems/roabp-affine-pit/verify/all_rank_affine_orbit.py](../problems/roabp-affine-pit/verify/all_rank_affine_orbit.py)
- [problems/roabp-affine-pit/verify/build_native_papers.py](../problems/roabp-affine-pit/verify/build_native_papers.py)
- [problems/roabp-affine-pit/verify/check_artin_reset.py](../problems/roabp-affine-pit/verify/check_artin_reset.py)
- [problems/roabp-affine-pit/verify/check_palette_sharpness.py](../problems/roabp-affine-pit/verify/check_palette_sharpness.py)
- [problems/roabp-affine-pit/verify/check_quadratic_hasse.py](../problems/roabp-affine-pit/verify/check_quadratic_hasse.py)
- [problems/roabp-affine-pit/verify/check_source_bindings.py](../problems/roabp-affine-pit/verify/check_source_bindings.py)
- [problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py](../problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py)
- [problems/robust-bounded-certificates/verify/check_bounded.py](../problems/robust-bounded-certificates/verify/check_bounded.py)
- [problems/robust-scenario-flow/verify/check_scenarios.py](../problems/robust-scenario-flow/verify/check_scenarios.py)
- [problems/robust-unrelated-allocation/verify/check_robust.py](../problems/robust-unrelated-allocation/verify/check_robust.py)
- [problems/robust-width-two-allocation/verify/check_width_two.py](../problems/robust-width-two-allocation/verify/check_width_two.py)
- [problems/selected-flow/verify/check_concurrent.py](../problems/selected-flow/verify/check_concurrent.py)
- [problems/subset-sum-fast-deterministic/verify/check_energy.py](../problems/subset-sum-fast-deterministic/verify/check_energy.py)
- [problems/subset-sum-fast-deterministic/verify/check_headline_ledger.py](../problems/subset-sum-fast-deterministic/verify/check_headline_ledger.py)
- [problems/subset-sum-fast-deterministic/verify/check_replay_recovery.py](../problems/subset-sum-fast-deterministic/verify/check_replay_recovery.py)
- [problems/subset-sum-fast-deterministic/verify/check_third_recovery.py](../problems/subset-sum-fast-deterministic/verify/check_third_recovery.py)
- [problems/subset-sum-low-space-deterministic/verify/check_exact_convolution.py](../problems/subset-sum-low-space-deterministic/verify/check_exact_convolution.py)
- [problems/subset-sum-low-space-deterministic/verify/check_range_identities.py](../problems/subset-sum-low-space-deterministic/verify/check_range_identities.py)
- [problems/subset-sum-low-space-deterministic/verify/check_range_solver.py](../problems/subset-sum-low-space-deterministic/verify/check_range_solver.py)
- [problems/subset-sum-low-space-deterministic/verify/check_resources.py](../problems/subset-sum-low-space-deterministic/verify/check_resources.py)
- [problems/subset-sum-low-space-deterministic/verify/check_structural.py](../problems/subset-sum-low-space-deterministic/verify/check_structural.py)
- [problems/two-size-scheduling/verify/check_corank.py](../problems/two-size-scheduling/verify/check_corank.py)
- [problems/two-time-scheduling/verify/check_scheduling.py](../problems/two-time-scheduling/verify/check_scheduling.py)
- [problems/unrelated-values-joint-role/verify/check_joint.py](../problems/unrelated-values-joint-role/verify/check_joint.py)
- [problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py](../problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py)
- [problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py](../problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py)
- [problems/weighted-prefix-quota-frontier/verify/check_orders_families.py](../problems/weighted-prefix-quota-frontier/verify/check_orders_families.py)
- [problems/weighted-prefix-quota-frontier/verify/check_prefix.py](../problems/weighted-prefix-quota-frontier/verify/check_prefix.py)
- [problems/weighted-prefix-quota-frontier/verify/check_quota_extensions.py](../problems/weighted-prefix-quota-frontier/verify/check_quota_extensions.py)
- [problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py](../problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py)
- [problems/weighted-prefix-quota-frontier/verify/check_two_weight_lower.py](../problems/weighted-prefix-quota-frontier/verify/check_two_weight_lower.py)
- [problems/whole-ground-allocation/verify/check_selection.py](../problems/whole-ground-allocation/verify/check_selection.py)
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
