# Review status and verification evidence

Readiness applies to the precise scope below. **Ready for review** means that the stated manuscript package has been checked for its theorem, proof, computational model and declared dependencies. **Partial readiness** identifies completed components of a larger family. Other manuscripts remain available with review pending. None of these labels claims external peer review or proof-assistant verification.

The machine-readable [registry](registry.json) is the source of these statuses and of each executable check's mathematical scope.

## Run the checks

```sh
python3 tools/check_repository.py
```

The default suite checks repository structure and every registered executable used by the canonical runner. For Subset Sum it validates the saved full-contact receipt's source/menu binding and freshly replays the rho=1.7 and direct branches. To replay the complete contact menu:

```sh
python3 tools/check_repository.py --full-contacts --jobs 4
```

Receipt binding establishes provenance and coverage metadata; only recomputation re-establishes the inequalities. The full mode is also available through manual dispatch of the repository workflow. The [contact evidence note](../problems/subset-sum-fast-deterministic/verify/README.md) states the analytic coverage argument.

## Ready for review

### [Degree-constrained subgraphs](../problems/degree-constrained-subgraphs/)

Theorem 1.1: unconditional sparse deterministic reductions for prescribed degrees, degree intervals, and exact or ranged cardinality, with both extension and decoding directions. Cardinality feasibility uses one exact matching call.

**Conditions and remaining work.** The displayed fast running time requires the faster conditional general-matching implementation. Any correct exact maximum-matching solver, including the standard-library reference solver, suffices for the unconditional reduction theorem.

[Proof](../problems/degree-constrained-subgraphs/proof.md) · [Dependencies](../problems/degree-constrained-subgraphs/sources.md) · [Evidence](../problems/degree-constrained-subgraphs/verify/README.md) · Reviewed 2026-10-26

### [Matroid and submodular failure summaries](../problems/matroid-failure-summaries/)

Main Theorems 1–6: represented prefix lift; sharp oracle-rank and integral-value constructions; sharp one-failure endpoint; explicit weighted obstruction; faster canonical-basis tree and original-basis size refinement; exact low-rank two-failure maxima and minimality of the 13-item example. Includes the sharp singleton-replacement bound r+2t, its failed-contracted-item proof, and the profile-sensitive construction with N(1+ell_0+binom(t+1,2)) queries.

**Conditions and remaining work.** Oracle results require the specified independence or value oracle and retain original items rather than encoding an arbitrary oracle. The best general weighted-oracle size remains open outside the proved low-rank cases. Finite programs support the written proofs and are not proof-assistant verification.

[Proof](../problems/matroid-failure-summaries/proof.md) · [Dependencies](../problems/matroid-failure-summaries/sources.md) · [Evidence](../problems/matroid-failure-summaries/verify/README.md) · Reviewed 2026-10-26

## Components ready for review

### [Faster deterministic Subset Sum](../problems/subset-sum-fast-deterministic/)

Part II parameter composition: the generalized second lookup, its exact 62-branch replay and 44-branch compatibility, the finite-volume cone lemma and compiler allowance, the continuous reflected-profile envelope, and all nine outer cost rates. The scalar tuple was independently recalculated.

**Conditions and remaining work.** The arbitrary-input signed-circuit compiler and witness reduction remain mathematical manuscript proofs; the numerical certificates do not formalize them. The deterministic startup constant is finite and input-independent but has no practical numerical bound.

[Proof](../problems/subset-sum-fast-deterministic/proof.md) · [Dependencies](../problems/subset-sum-fast-deterministic/sources.md) · [Evidence](../problems/subset-sum-fast-deterministic/verify/README.md) · Reviewed 2026-10-26

### [Low-space deterministic Subset Sum](../problems/subset-sum-low-space-deterministic/)

The two-short-range theorem, including signed-input normalization, nested residue streams, indexed witnesses, and the self-contained exact Boolean convolution lemma. The general low-space ledger now explicitly charges the one-bit deficiency-proxy loss.

**Conditions and remaining work.** The stronger n/6 space exponent requires the supplied three-block partition and its two short normalized ranges. The general 0.18261635770550353-space theorem is a separate algorithm; finite range tests do not verify its full storage schedule.

[Proof](../problems/subset-sum-low-space-deterministic/proof.md) · [Dependencies](../problems/subset-sum-low-space-deterministic/sources.md) · [Evidence](../problems/subset-sum-low-space-deterministic/verify/README.md) · Reviewed 2026-10-26

### [Prefix, laminar and sparse quotas](../problems/weighted-prefix-quota-frontier/)

The sharp sparse-packing FPT restriction with improved basis-tree preprocessing, arbitrary signed-profit ordered extension, capacity-sensitive failure budget, exact original-context lower construction, and aggregate laminar reduction to at most B lower rows.

**Conditions and remaining work.** The smaller sparse ground uses explicit FPT preprocessing; it is distinct from the uniform polynomial sunflower tradeoff. These checks do not verify the family’s general valuated completion, universal-coloring construction or lower-bound literature. Original oracles and weights remain available after restriction.

[Proof](../problems/weighted-prefix-quota-frontier/proof.md) · [Dependencies](../problems/weighted-prefix-quota-frontier/sources.md) · [Evidence](../problems/weighted-prefix-quota-frontier/verify/README.md) · Reviewed 2026-10-26

### [Deterministic general-graph maximum matching](../problems/general-matching/)

The executable cubic solver with optimality certificates and its independent verifier; the self-contained quadratic certificate-extraction proof; the unconditional sharp c-neighbor and mixed-failure kernels, componentwise composition, and subcubic reduction with its decoder. The cover-side alternating exchange further reduces the default solver, including certificates, to O(n+m log(m+2)+sum_i nu(G_i)^3), while retaining the original independent certificate format.

**Conditions and remaining work.** The four-fifths research running time still requires the cycle-search implementation and named published prerequisites in sources.md. The executable solver has its separately proved cubic bound. The mixed-failure kernel assumes a fixed simple graph; discarded parallel records and correlated labels are outside its scope.

[Proof](../problems/general-matching/proof.md) · [Dependencies](../problems/general-matching/sources.md) · [Evidence](../problems/general-matching/verify/README.md) · Reviewed 2026-10-26

### [Static and threshold min-cost flow](../problems/min-cost-flow/)

The exact affine integral-recovery proof and reference checks; artificial-edge penalties, fixed-threshold accounting, and initialization that safely defers currently infeasible prefixes.

**Conditions and remaining work.** The faster numerical client still needs deterministic cycle search, dynamic flow maintenance and edge retirement with the stated lifetime and bit bounds. A NO answer at an early insertion prefix is not permanent infeasibility.

[Proof](../problems/min-cost-flow/proof.md) · [Dependencies](../problems/min-cost-flow/sources.md) · [Evidence](../problems/min-cost-flow/verify/README.md) · Reviewed 2026-10-26

### [Incremental strongly connected components](../problems/incremental-scc/)

The small-to-large persistent label history, historical equality queries, and first-coalescence queries in O(1+log log(n+2)) time via a binary search on the shared suffix.

**Conditions and remaining work.** The history layer assumes correct monotone component merges and permanently retired label identities. The faster SCC update algorithm still requires the cycle-search, exact flow and edge-retirement operations listed in sources.md.

[Proof](../problems/incremental-scc/proof.md) · [Dependencies](../problems/incremental-scc/sources.md) · [Evidence](../problems/incremental-scc/verify/README.md) · Reviewed 2026-10-26

### [Incremental directed SSSP](../problems/incremental-sssp/)

The clipped-tree intersection and loop-removal reporting construction, including zero-length edges; the nonnegative-integer perturbation reduction and its accuracy/bit accounting.

**Conditions and remaining work.** The fast distance-maintenance theorem still requires the explicitly stated detector, cycle-search and edge-retirement data structures. The finite path tests do not validate their update time.

[Proof](../problems/incremental-sssp/proof.md) · [Dependencies](../problems/incremental-sssp/sources.md) · [Evidence](../problems/incremental-sssp/verify/README.md) · Reviewed 2026-10-26

### [Fully dynamic APSP](../problems/apsp-frontier/)

The five explicit parameter substitutions and the nonnegative-integer distance adapter, including exact zero answers, transformed length range, and the required uniform stretch bound.

**Conditions and remaining work.** The positive-distance hierarchy remains an explicit prerequisite. For the general parameter family, the zero-length extension additionally needs t^4 h=o(U); t^2 h=o(U) alone is insufficient. Only numerical distance output is claimed.

[Proof](../problems/apsp-frontier/proof.md) · [Dependencies](../problems/apsp-frontier/sources.md) · [Evidence](../problems/apsp-frontier/verify/README.md) · Reviewed 2026-10-26

### [Dynamic spanners](../problems/dynamic-spanners/)

The separate zero-edge class, dyadic positive-weight wrapper, and their initialization, update and recourse accounting for both displayed regimes.

**Conditions and remaining work.** The underlying unweighted hierarchy and forest algorithms remain explicit prerequisites. Output guarantees apply after each complete external update and retain the provider’s adaptive-history requirements.

[Proof](../problems/dynamic-spanners/proof.md) · [Dependencies](../problems/dynamic-spanners/sources.md) · [Evidence](../problems/dynamic-spanners/verify/README.md) · Reviewed 2026-10-26

### [Dynamic minimum spanning forest](../problems/dynamic-msf/)

The formal weighted MSF certificate and pruning substitution: local exchange/contraction proofs, literal connectivity adapter, finite pruning horizons, deterministic decomposition parameters and the NSW recursive cost calculation.

**Conditions and remaining work.** This is a derived public baseline using Chuzhoy–Gao–Li–Nanongkai–Peng–Saranurak Corollary 6.1, Meierhans–Probst Gutenberg–Saranurak Theorem 6.4, and Nanongkai–Saranurak–Wulff-Nilsen Theorem 7.1 and Section 9. It is not an executable implementation or a consequence of the research matching router.

[Proof](../problems/dynamic-msf/proof.md) · [Dependencies](../problems/dynamic-msf/sources.md) · [Evidence](../problems/dynamic-msf/verify/README.md) · Reviewed 2026-10-26

### [Strong forests and Gomory–Hu trees](../problems/decremental-strong-forest/)

The nonnegative-integer flat-forest adapter and zero-capacity Gomory–Hu preprocessing, with native-forest and cut-tree input costs stated separately.

**Conditions and remaining work.** The faster forest and exact-flow constructions retain the data-structure assumptions in sources.md. The local reductions do not supply those implementations or an additional simple-path reporting interface.

[Proof](../problems/decremental-strong-forest/proof.md) · [Dependencies](../problems/decremental-strong-forest/sources.md) · [Evidence](../problems/decremental-strong-forest/verify/README.md) · Reviewed 2026-10-26

## Review pending

These families have not yet received a scoped readiness entry in this registry. Their existing statements retain their own assumptions.

- [Numeric targets and support patterns](../problems/numeric-target-frontier/)
- [Single-failure optimum preservers](../problems/exact-failure-preservers/)
- [Flow, matching and price sensitivity](../problems/exact-flow-sensitivity/)
- [Colored and vertex-failure graph certificates](../problems/graph-color-failure-certificates/)
- [Resource-constrained packing summaries](../problems/packing-matching-summaries/)
- [Persistent-homology failure certificates](../problems/persistence-failure-certificates/)
- [Boolean linear optimization compiler](../problems/boolean-linear-compiler/)
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
- [Hypergraph matching and expander routing](../problems/strong-haxell-matching/)
- [Independent transversals](../problems/independent-transversal/)
- [Allocation and scheduling barriers](../problems/allocation-lower-bounds/)

## Executable evidence

Each linked program documents its checked identities or finite domain. The per-result evidence notes and registry distinguish direct evidence from a shared prerequisite; a passing finite check does not establish an arbitrary-input asymptotic theorem.

- [problems/degree-constrained-subgraphs/verify/check_reductions.py](../problems/degree-constrained-subgraphs/verify/check_reductions.py)
- [problems/general-matching/verify/check_certificate_search.py](../problems/general-matching/verify/check_certificate_search.py)
- [problems/general-matching/verify/check_cover_compression.py](../problems/general-matching/verify/check_cover_compression.py)
- [problems/general-matching/verify/check_reductions.py](../problems/general-matching/verify/check_reductions.py)
- [problems/general-matching/verify/check_reference.py](../problems/general-matching/verify/check_reference.py)
- [problems/group-metric-constraints/verify/check_quotient_rounding.py](../problems/group-metric-constraints/verify/check_quotient_rounding.py)
- [problems/incremental-scc/verify/check_label_history.py](../problems/incremental-scc/verify/check_label_history.py)
- [problems/incremental-sssp/verify/check_path_reporting.py](../problems/incremental-sssp/verify/check_path_reporting.py)
- [problems/matroid-failure-summaries/verify/check_single_replacement.py](../problems/matroid-failure-summaries/verify/check_single_replacement.py)
- [problems/matroid-failure-summaries/verify/check_summaries.py](../problems/matroid-failure-summaries/verify/check_summaries.py)
- [problems/matroid-failure-summaries/verify/check_weighted_obstruction.py](../problems/matroid-failure-summaries/verify/check_weighted_obstruction.py)
- [problems/matroid-failure-summaries/verify/check_weighted_prefix.py](../problems/matroid-failure-summaries/verify/check_weighted_prefix.py)
- [problems/min-cost-flow/verify/check_recovery.py](../problems/min-cost-flow/verify/check_recovery.py)
- [problems/subset-sum-fast-deterministic/verify/check_energy.py](../problems/subset-sum-fast-deterministic/verify/check_energy.py)
- [problems/subset-sum-fast-deterministic/verify/check_replay_recovery.py](../problems/subset-sum-fast-deterministic/verify/check_replay_recovery.py)
- [problems/subset-sum-low-space-deterministic/verify/check_exact_convolution.py](../problems/subset-sum-low-space-deterministic/verify/check_exact_convolution.py)
- [problems/subset-sum-low-space-deterministic/verify/check_range_identities.py](../problems/subset-sum-low-space-deterministic/verify/check_range_identities.py)
- [problems/subset-sum-low-space-deterministic/verify/check_range_solver.py](../problems/subset-sum-low-space-deterministic/verify/check_range_solver.py)
- [problems/subset-sum-low-space-deterministic/verify/check_resources.py](../problems/subset-sum-low-space-deterministic/verify/check_resources.py)
- [problems/subset-sum-low-space-deterministic/verify/check_structural.py](../problems/subset-sum-low-space-deterministic/verify/check_structural.py)
- [problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py](../problems/weighted-prefix-quota-frontier/verify/check_laminar_reduction.py)
- [problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py](../problems/weighted-prefix-quota-frontier/verify/check_sharp_packing.py)
- [tools/verify_finite_reductions.py](../tools/verify_finite_reductions.py)
- [tools/verify_non_fano.py](../tools/verify_non_fano.py)
- [tools/verify_profile_certificates.py](../tools/verify_profile_certificates.py)
- [tools/verify_sensitivity_certificates.py](../tools/verify_sensitivity_certificates.py)
- [tools/verify_subset_sum_contacts.py](../tools/verify_subset_sum_contacts.py)
- [tools/verify_subset_sum_scalars.py](../tools/verify_subset_sum_scalars.py)

## Maintaining a status

Set a readiness scope only after checking the corresponding proof, algorithm, representation, randomness and source requirements. Name required data structures or unproved implementation steps beside the scope. Update `registry.json`, then run `python3 tools/build_reviews.py`; this synchronizes these entries with the reviewed problem cards. A changed theorem or dependency requires a new scope assessment.

See [Contributing](../CONTRIBUTING.md) for the manuscript workflow and [provenance](../provenance/README.md) for imported source identities.
