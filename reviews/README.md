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

### [Resource-constrained packing summaries](../problems/packing-matching-summaries/)

The complete exterior/product-feature packing transfer, including signed fixed costs, multiple label-failure systems, private padding, full original resource rank, arbitrary later extension backgrounds, multigraph matching specializations and explicit rational/finite-field construction accounting. The shipped rational backend realizes the dimension gate and weighted lifted basis, with an independent subset/context checker.

**Dependencies and scope.** The original optional resource matroid must be explicitly represented. Later extensions may be unrepresented but must restrict to that original resource; the implementation constructs a restriction and does not solve arbitrary extension queries. The executable uses exact rational arithmetic only. Explicit finite-field extensions retain their separate mathematical proof and are not implemented by this backend. Fixed costs and permanent input IDs cannot be changed by a query. Finite context enumeration tests the implementation, while the original-flat and annihilating-functional proof establishes all-extension quantifiers. This internal review does not certify historical priority or formal verification.

[Proof](../problems/packing-matching-summaries/proof.md) · [Dependencies](../problems/packing-matching-summaries/sources.md) · [Evidence](../problems/packing-matching-summaries/verify/README.md) · Reviewed 2026-10-27

### [Boolean linear optimization compiler](../problems/boolean-linear-compiler/)

The complete signed interval-disjunction proof, bounded-slack interpolation, signed radix packing and indexed-witness/optimization transfer. Each halving emits at most two intervals with at most the original row support many integer values; all exceptional and binary-input cases are explicit. Includes fixed-cardinality layers, modal-coefficient subtraction, signed parity overlap and the resulting smaller slack budget, with exact preservation of the original cardinality and optimization witnesses.

**Dependencies and scope.** The Subset Sum backend is supplied with its stated indexed-witness time contract; a space bound requires that same backend. The compiler and finite checks do not establish the backend circuit or continuous-contact proofs. The cardinality refinement counts the original explicitly listed variables. Its strongest slack bound does not assert a universal improvement to every disjunction-product parameter.

[Proof](../problems/boolean-linear-compiler/proof.md) · [Dependencies](../problems/boolean-linear-compiler/sources.md) · [Evidence](../problems/boolean-linear-compiler/verify/README.md) · Reviewed 2026-10-26

### [Exact-separation and non-Fano boundaries](../problems/obstruction-boundaries/)

Both canonical obstruction theorems: exact compact-code membership is coNP-complete through the weighted Max-Cut reduction, including sparse certificates for binary-encoded unused dimensions; and the precise non-Fano fixed-amplitude counterexample with its direct-sum product. The exact reference constructs the reduction, verifies original-input dense or sparse violations without search, recovers violating cuts and separates by streamed enumeration of used coordinates.

**Dependencies and scope.** The Max-Cut primary source uses positive integer weights and a non-strict target; the reduction explicitly shifts that target to its strict-cut threshold. Construction and certificate verification charge actual rational and coordinate bit lengths. The reference separator is exponential in used coordinates. No polynomial exact separator, approximate-separation hardness, Gaussian-amplitude counterexample or general sparsifier construction is claimed. Independent internal proof review and finite executable evidence do not assert external peer review or proof-assistant verification.

[Proof](../problems/obstruction-boundaries/proof.md) · [Dependencies](../problems/obstruction-boundaries/sources.md) · [Evidence](../problems/obstruction-boundaries/verify/README.md) · Reviewed 2026-10-27

### [Recipient-matroid configuration](../problems/recipient-matroid-configuration/)

The complete recipient-matroid configuration-comparator theorem: universal simultaneous reservations, every ordered-prefix rank-additivity invariant, current eager release, retained-prefix exchanges, sharp rank-cover coefficient, exact and positive-slack rank bounds, fractional fat-service reduction and target-grid search. The shipped resource-state backend realizes completion, current freedom tests and safe prefix exchanges.

**Dependencies and scope.** One service per player-resource pair with common intrinsic nonnegative values. Local families are downward closed; their exact or certified rational approximation oracle and all matroid union/rank work are paid. The executable component implements the resource side only. Player eligibility, earliest whole-layer retention, bundle feasibility/minimality and normalization are caller obligations; the complete player-layer allocator and fat-service union engine are not shipped. The proof uses separate recipient-matroid columns and does not automatically extend to aggregate polymatroids. Finite represented examples support the symbolic all-matroid argument; no external peer review or formal verification is claimed.

[Proof](../problems/recipient-matroid-configuration/proof.md) · [Dependencies](../problems/recipient-matroid-configuration/sources.md) · [Evidence](../problems/recipient-matroid-configuration/verify/README.md) · Reviewed 2026-10-27

### [Explicit-item matroid union](../problems/item-matroid-union/)

The complete explicit-item player-basis theorem and configuration-comparator upgrade: fat-item union and duality, rank-sensitive exact and positive-slack current-blocker bounds, recovery by dual-basis extension, fractional union domination and rational-grid target search. The inner player-eligibility, earliest-circuit exchange, refresh and signature arguments were inspected in the shared current-blocker proof.

**Dependencies and scope.** The original player matroid is supplied by an independence oracle. Polynomial matroid-union/partition and bipartite matching remain named, paid algorithmic dependencies; no unit-cost derived union oracle is assumed. The configuration LP is a proof comparator and is neither supplied nor enumerated by the algorithm. No guarantee against the unrestricted original compact LP is asserted. The new finite checker supports rank and recovery identities; it is not the polynomial union algorithm or a complete allocation implementation. The finite-rank factor tends to four, so no fixed improvement below four is claimed.

[Proof](../problems/item-matroid-union/proof.md) · [Dependencies](../problems/item-matroid-union/sources.md) · [Evidence](../problems/item-matroid-union/verify/README.md) · Reviewed 2026-10-27

### [Intrinsic two-value allocation](../problems/two-value-exact-two/)

The complete compulsory-player two-intrinsic-value arbitrary-assignment-cost theorem: polynomial affordable heavy-recipient parameter, attaining minimum original heavy completion, adaptive residual small-count region and protected pair, exact integral quota recovery, one-unit/pure-heavy/high-target boundaries, one-sided value-grid search and matching strict-below-two recipient-oracle threshold.

**Dependencies and scope.** All players are compulsory, values are intrinsic to disjoint heavy/light types and there is one exact nonnegative assignment-cost budget. Original heavy pairs remain available after every forced light omission; an attaining exact completion is required. Paid exact rank/SFM/LP and weighted matroid/integral polymatroid intersection retain their explicitly proved interfaces. The large-target branch uses the fixed compulsory set and cost-preserving additive rounding; no optional-player all-target LP is inferred. Shared reference evidence realizes weighted unit coverage, adaptive prefix recursion and native scalar setup flow. It does not implement the full two-value allocation LP/quota/rounding pipeline. Mathematical completeness is distinct from that software scope. The strict-below-two lower bound is deterministic hidden-set rank-oracle complexity for the same affordable-heavy parameter with zero costs. It does not imply ordinary explicit-eligibility hardness or an optimal exponential base.

[Proof](../problems/two-value-exact-two/proof.md) · [Dependencies](../problems/two-value-exact-two/sources.md) · [Evidence](../problems/two-value-exact-two/verify/README.md) · Reviewed 2026-10-27

### [Unrelated-value additive allocation](../problems/unrelated-values-additive/)

The complete exact-budget unrelated-value additive theorem against the fractional optimum on an actual fixed-family selected set: nonnegative original service support separation, full-accuracy weighted omission, uniform denominator recovery and original fixed-set reoptimization, disposal/complement-prefix integral rounding with one exact cost objective, and fixed-accuracy whole-ground conversion.

**Dependencies and scope.** The original fixed-cardinality restriction selector and paid exact rational LP, rank/SFM and integral polymatroid intersection primitives remain mathematical dependencies. The fractional comparator relaxes resource counts, never mixes selected bases. Prefix rounding preserves one scalar assignment cost and loses the stated original largest unit per player. It supplies no positive multiplicative factor without controlling that additive term and does not preserve several independent cost budgets. Shared executable evidence realizes weighted selection, rational recovery and global cover primitives; no native general unrelated-value allocation or rounding solver is claimed. Positive-cost coordinates exceeding the whole budget remain in the fractional model unless a zero-budget exact mask applies. The sharp global expression uses fixed rational accuracy; binary-variable accuracy retains the stated rational upper-envelope implementation.

[Proof](../problems/unrelated-values-additive/proof.md) · [Dependencies](../problems/unrelated-values-additive/sources.md) · [Evidence](../problems/unrelated-values-additive/verify/README.md) · Reviewed 2026-10-27

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

### [Prefix, laminar and sparse quotas](../problems/weighted-prefix-quota-frontier/)

The sharp sparse-packing FPT restriction with improved basis-tree preprocessing, arbitrary signed-profit ordered extension, capacity-sensitive failure budget, exact original-context lower construction, and aggregate laminar reduction to at most `B` lower rows. Exact dominant-weight completion with all signed zero-coordinate costs, a binary count-rank oracle, the one-positive-weight polynomial endpoint, the self-contained `10/9` quadratic leading exponent, the named universal-set `5/9` refinement, projected coloring identities and histogram-sensitive enumeration. The compatible-cut extension and the two-positive-weight oracle/encoded-program lower-bound models are proved separately.

**Dependencies and scope.** The general resource calls retain exact integral-polymatroid optimization and submodular-minimization dependencies named in sources.md. The `5/9` leading coefficient specifically uses Naor-Schulman-Srinivasan Theorem 7 and its locally explicit indexing guarantee; the elementary `10/9` alternative supplies a local coloring proof. Finite checkers isolate the stated mechanisms and do not implement all of these optimization algorithms. The compatible-cut one-weight polynomial endpoint requires a prescribed or forced total numeric mass. Original resource totals, all numeric constraints and signed costs remain intact. Oracle query lower bounds and ETH claims for readable rank programs are separate models.

[Proof](../problems/weighted-prefix-quota-frontier/proof.md) · [Dependencies](../problems/weighted-prefix-quota-frontier/sources.md) · [Evidence](../problems/weighted-prefix-quota-frontier/verify/README.md) · Reviewed 2026-10-26

### [Single-failure optimum preservers](../problems/exact-failure-preservers/)

The ordinary two-matroid replacement-cycle value identity and minimum-hop literal update, and the executable supplied-optimum-baseline rooted directed arborescence realization: heavy-light/segment-tree exchange transitions, exact lexicographic dense shortest paths, deterministic phased short-path/hub-tree records, original-arc support, optimum ID reporting and infeasibility flags.

**Dependencies and scope.** The reusable backend assumes a supplied optimum rooted spanning arborescence. Its validation and negative-cycle rejection do not substitute for the separate baseline-supply contract; independent small fixtures obtain baselines by exhaustive enumeration. The reference uses `O(M+A^3)` arithmetic preprocessing with `A=4(n-1)-1` auxiliary vertices, retaining `O(n^(3/2))` final records and `O(n)` reporting; it does not implement the manuscript’s faster preprocessing. Rational bit lengths are charged separately. This review does not cover the valuated extension, rank-drop client, or lower-bound transfers. Those retain their linked mathematical statements and dependencies. Finite checks and internal independent code review are not proof-assistant verification or external peer review.

[Proof](../problems/exact-failure-preservers/proof.md) · [Dependencies](../problems/exact-failure-preservers/sources.md) · [Evidence](../problems/exact-failure-preservers/verify/README.md) · Reviewed 2026-10-27

### [Flow, matching and price sensitivity](../problems/exact-flow-sensitivity/)

The exact nonnegative rational unit-flow and internally vertex-disjoint path components: fixed-value and minimum-cost maximum queries, residual replacement, support-sensitive original-record preservers, compact reports and simple-input support specializations. The native path wrapper proves unit-gate deletion semantics, original-ID recovery and zero-cost-cycle-safe packing output. Both local realizations prove their own polynomial preprocessing and bit-cost contracts. The independent original-input certificate component proves signed-cost reduced-cost optimality, maximum-value and infeasibility cuts, and a binary-input cost-blind general-balance constructor.

**Dependencies and scope.** Parallel original records are supported under the support-sensitive bound; the uniform flow-value-dependent support exponent additionally requires a simple original digraph. Queries are independent single-record deletions, not cumulative updates. The native path wrapper requires simple directed input and one independent original-arc or internal-vertex failure. Terminal deletions and simultaneous failures are excluded. Its full packing output uses linear record work. The references use exact fractions and Python hash tables, with operation and bit-cost conventions explicit. They do not implement the faster research preprocessing. Signed/general-balance minimum-cost initialization, general-matching, matroid and price clients are outside this reviewed component scope. Independent certificates scan the full surviving original graph, with separately charged production and verification; these costs do not inherit the compact oracle query bound. The general-balance constructor ignores costs.

[Proof](../problems/exact-flow-sensitivity/proof.md) · [Dependencies](../problems/exact-flow-sensitivity/sources.md) · [Evidence](../problems/exact-flow-sensitivity/verify/README.md) · Reviewed 2026-10-27

### [Colored and vertex-failure graph certificates](../problems/graph-color-failure-certificates/)

The complete sharp componentwise single-vertex-color theorem: activation and symmetric-matrix rank proofs, all surviving ordered-prefix connectivity partitions, exact canonical minimum spanning forests, sharp core-clique/outer-star examples and deterministic polynomial construction. The rational backend and its independent graph-reachability checker have a separate implementation review.

**Dependencies and scope.** Input is an undirected multigraph with one color per vertex, signed rational weights and fixed original-ID tie breaking. All allowed color failures are covered; recosting after preprocessing is not. The backend uses static rational elimination and scans retained records at query time. Mixed edge colors, overlapping lists, symmetric-cubic refinements and the exchange-reporting dynamic-MSF acceleration remain separate mathematical variants outside this bounded readiness audit. The retained-edge bound is separate from elimination workspace and rational bit costs. Finite checks and internal review do not constitute external peer review, formal certification or exhaustive literature-priority verification.

[Proof](../problems/graph-color-failure-certificates/proof.md) · [Dependencies](../problems/graph-color-failure-certificates/sources.md) · [Evidence](../problems/graph-color-failure-certificates/verify/README.md) · Reviewed 2026-10-27

### [Persistent-homology failure certificates](../problems/persistence-failure-certificates/)

Complete actual-feature-rank construction for represented failure lifts and the vertex-label persistence specialization with no extra top-simplex labels. Includes the degree-bounded evaluation module, canonical column pivots, nonzero shifts, shared original boundary-row compression, streamed column generation, surviving prefix spans and naturality, with exact arithmetic and storage ledgers.

**Dependencies and scope.** The reviewed persistence construction keeps the full lower skeleton and one supplied order over the stated field. Additional top labels retain the separate general incidence theorem. Top-degree homology, integral torsion, dynamic labels and a common solution for unrelated filtration/cost orders are not asserted. Executable checks use rationals and supplied prime fields. The general finite-field extension and rational bit analysis are explicit mathematical components. Finite span checks supplement the naturality proof; they are not proof-assistant verification.

[Proof](../problems/persistence-failure-certificates/proof.md) · [Dependencies](../problems/persistence-failure-certificates/sources.md) · [Evidence](../problems/persistence-failure-certificates/verify/README.md) · Reviewed 2026-10-26

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

The deterministic Pauli stabilizer-basis surrogate and witness theorem (main Theorem 5 and witness Theorem 1), including exact affine-parity enumeration, and the prime-dimensional individual-check witness reduction (witness Corollary 2). Pairwise operator comparisons, complete-basis pinching, exact basis-energy equality and compact tableau output are explicit.

**Dependencies and scope.** The polynomial-time reduction produces a classical objective; exact minimization still uses `2^d poly(L)` enumeration for Pauli labels or `p^n poly(L)` for prime-dimensional checks, with polynomial workspace. This is not a polynomial-time ground-state optimizer. This review uses compact symplectic/stabilizer linear algebra and does not certify the separate whole-block sparsification, adaptive quotient, correlated-failure or joint lower-bound dependency chains. The shared finite quotient-rounding checker is not evidence for quantum operator inequalities; those are proved symbolically.

[Proof](../problems/quantum-stabilizer/proof.md) · [Dependencies](../problems/quantum-stabilizer/sources.md) · [Evidence](../problems/quantum-stabilizer/verify/README.md) · Reviewed 2026-10-27

### [One-value allocation](../problems/one-value-exact-two/)

The main exact factor-two theorem with one assignment-cost budget, the exact prescribed-basis endpoint and the stated strict-below-two oracle boundary. The one-unit gate now has a direct Boolean-cap augmentation proof, an exact assignment-pair matroid construction and binary-size accounting; the main proof supplies nonnegative separation, weighted omission, no-loss quota recovery and target search.

**Dependencies and scope.** Exact submodular minimization, rational LP with separation, and weighted matroid or integral-polymatroid intersection remain paid polynomial primitives. The gate proof identifies their original finite grounds and does not expand binary capacities into unit copies. The separate shared-setup, general integer-factor and whole-ground conversion results are outside this bounded main-theorem audit. Finite gate checks do not implement the full allocator or certify the unbounded runtime theorem.

[Proof](../problems/one-value-exact-two/proof.md) · [Dependencies](../problems/one-value-exact-two/sources.md) · [Evidence](../problems/one-value-exact-two/verify/README.md) · Reviewed 2026-10-27

### [Independent transversals](../problems/independent-transversal/)

The complete elementary certifying fallback: induced-star current-blocker invariants, strict earlier-star zero-blocker cascades, positive-composition signature bound, exact total-domination/constellation output and independent original-input verification. The derived public procedure has a new local executable realization and separately charged exponential-in-class-count work.

**Dependencies and scope.** The elementary procedure is credited to Graf and Haxell, arXiv:1811.02687v2, Definition 3 and Section 2. It requires no claw or slack promise. Within-class edges are removed exactly as in the source convention. A domination constellation is not a certificate that no independent transversal exists. The verifier checks the precise elementary alternative and no stronger infeasibility claim. The faster current-blocker layer theorem and its input-linear layer primitives remain outside this bounded review scope. Python hash-table operations and optional observer costs are separately charged; no fast-layer implementation or formal verification is claimed.

[Proof](../problems/independent-transversal/proof.md) · [Dependencies](../problems/independent-transversal/sources.md) · [Evidence](../problems/independent-transversal/verify/README.md) · Reviewed 2026-10-27

## Review pending

These families have not yet received a scoped readiness entry in this registry. Their existing statements retain their own assumptions.

- [Numeric targets and support patterns](../problems/numeric-target-frontier/)
- [Arbitrary-value allocation scheme](../problems/arbitrary-value-allocation-scheme/)
- [Recipient polymatroids](../problems/recipient-polymatroid/)
- [Intrinsic values near factor two](../problems/intrinsic-values-near-two/)
- [Unrelated values with a joint role](../problems/unrelated-values-joint-role/)
- [Robust unrelated allocation](../problems/robust-unrelated-allocation/)
- [Activated-machine scheduling](../problems/activated-machine-scheduling/)
- [Six-profile scheduling](../problems/six-profile-three-halves/)
- [Many-size workload scheduling](../problems/many-size-scheduling/)
- [Commitment scheduling](../problems/commitment-scheduling/)

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
- [problems/allocation-lower-bounds/verify/check_barriers.py](../problems/allocation-lower-bounds/verify/check_barriers.py)
- [problems/arbitrary-processing-scheduling/verify/check_profiles.py](../problems/arbitrary-processing-scheduling/verify/check_profiles.py)
- [problems/boolean-linear-compiler/verify/check_cardinality_compiler.py](../problems/boolean-linear-compiler/verify/check_cardinality_compiler.py)
- [problems/boolean-linear-compiler/verify/check_interval_compiler.py](../problems/boolean-linear-compiler/verify/check_interval_compiler.py)
- [problems/correlated-spectral-regression/verify/check_importance_regression.py](../problems/correlated-spectral-regression/verify/check_importance_regression.py)
- [problems/degree-constrained-subgraphs/verify/check_linear_selector.py](../problems/degree-constrained-subgraphs/verify/check_linear_selector.py)
- [problems/degree-constrained-subgraphs/verify/check_reductions.py](../problems/degree-constrained-subgraphs/verify/check_reductions.py)
- [problems/degree-constrained-subgraphs/verify/check_reference.py](../problems/degree-constrained-subgraphs/verify/check_reference.py)
- [problems/exact-failure-preservers/verify/check_arborescence_reporting.py](../problems/exact-failure-preservers/verify/check_arborescence_reporting.py)
- [problems/exact-flow-sensitivity/verify/check_flow_certificates.py](../problems/exact-flow-sensitivity/verify/check_flow_certificates.py)
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
- [problems/graph-color-failure-certificates/verify/check_vertex_colors.py](../problems/graph-color-failure-certificates/verify/check_vertex_colors.py)
- [problems/group-metric-constraints/verify/check_coset_compiler.py](../problems/group-metric-constraints/verify/check_coset_compiler.py)
- [problems/group-metric-constraints/verify/check_quotient_rounding.py](../problems/group-metric-constraints/verify/check_quotient_rounding.py)
- [problems/incremental-scc/verify/check_label_history.py](../problems/incremental-scc/verify/check_label_history.py)
- [problems/incremental-sssp/verify/check_path_reporting.py](../problems/incremental-sssp/verify/check_path_reporting.py)
- [problems/independent-transversal/verify/check_elementary.py](../problems/independent-transversal/verify/check_elementary.py)
- [problems/item-matroid-union/verify/check_union_reduction.py](../problems/item-matroid-union/verify/check_union_reduction.py)
- [problems/label-block-cut/verify/check_whole_blocks.py](../problems/label-block-cut/verify/check_whole_blocks.py)
- [problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py](../problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py)
- [problems/matroid-failure-summaries/verify/check_rank_two_prefix.py](../problems/matroid-failure-summaries/verify/check_rank_two_prefix.py)
- [problems/matroid-failure-summaries/verify/check_single_replacement.py](../problems/matroid-failure-summaries/verify/check_single_replacement.py)
- [problems/matroid-failure-summaries/verify/check_summaries.py](../problems/matroid-failure-summaries/verify/check_summaries.py)
- [problems/matroid-failure-summaries/verify/check_weighted_obstruction.py](../problems/matroid-failure-summaries/verify/check_weighted_obstruction.py)
- [problems/matroid-failure-summaries/verify/check_weighted_prefix.py](../problems/matroid-failure-summaries/verify/check_weighted_prefix.py)
- [problems/min-cost-flow/verify/check_capacity_scaling.py](../problems/min-cost-flow/verify/check_capacity_scaling.py)
- [problems/min-cost-flow/verify/check_recovery.py](../problems/min-cost-flow/verify/check_recovery.py)
- [problems/obstruction-boundaries/verify/check_compact_body.py](../problems/obstruction-boundaries/verify/check_compact_body.py)
- [problems/one-value-exact-two/verify/check_one_unit_gate.py](../problems/one-value-exact-two/verify/check_one_unit_gate.py)
- [problems/packing-matching-summaries/verify/check_product_summary.py](../problems/packing-matching-summaries/verify/check_product_summary.py)
- [problems/persistence-failure-certificates/verify/check_feature_construction.py](../problems/persistence-failure-certificates/verify/check_feature_construction.py)
- [problems/processing-bucket-tradeoff/verify/check_buckets.py](../problems/processing-bucket-tradeoff/verify/check_buckets.py)
- [problems/recipient-matroid-configuration/verify/check_reservations.py](../problems/recipient-matroid-configuration/verify/check_reservations.py)
- [problems/roabp-affine-pit/verify/all_rank_affine_orbit.py](../problems/roabp-affine-pit/verify/all_rank_affine_orbit.py)
- [problems/roabp-affine-pit/verify/build_native_papers.py](../problems/roabp-affine-pit/verify/build_native_papers.py)
- [problems/roabp-affine-pit/verify/check_artin_reset.py](../problems/roabp-affine-pit/verify/check_artin_reset.py)
- [problems/roabp-affine-pit/verify/check_palette_sharpness.py](../problems/roabp-affine-pit/verify/check_palette_sharpness.py)
- [problems/roabp-affine-pit/verify/check_quadratic_hasse.py](../problems/roabp-affine-pit/verify/check_quadratic_hasse.py)
- [problems/roabp-affine-pit/verify/check_source_bindings.py](../problems/roabp-affine-pit/verify/check_source_bindings.py)
- [problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py](../problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py)
- [problems/robust-bounded-certificates/verify/check_bounded.py](../problems/robust-bounded-certificates/verify/check_bounded.py)
- [problems/robust-scenario-flow/verify/check_scenarios.py](../problems/robust-scenario-flow/verify/check_scenarios.py)
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
- [problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py](../problems/weighted-prefix-quota-frontier/verify/check_laminar_recovery.py)
- [problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py](../problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py)
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
