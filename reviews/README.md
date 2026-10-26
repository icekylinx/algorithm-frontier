# Review status and verification evidence

Readiness applies to the precise scope below. **Ready for review** means that the stated manuscript package has been checked for its theorem, proof, computational model and declared dependencies. **Partial readiness** identifies completed components of a larger family. Other manuscripts remain available with review pending. None of these labels claims external peer review or proof-assistant verification.

The machine-readable [registry](registry.json) is the source of these statuses and of each executable check's mathematical scope.

## Run the checks

```sh
python3 tools/check_repository.py
```

The default suite checks repository structure and every registered executable used by the canonical runner. For Subset Sum it validates the saved full-contact receipt's source/menu binding and freshly replays the rho=1.7 and direct branches. To replay all 44 contact branches:

```sh
python3 tools/check_repository.py --full-contacts --jobs 4
```

Receipt binding establishes provenance and coverage metadata; only recomputation re-establishes the inequalities. The full mode is also available through manual dispatch of the repository workflow. The [contact evidence note](../problems/subset-sum-fast-deterministic/verify/README.md) states the analytic coverage argument.

## Ready for review

### [Degree-constrained subgraphs](../problems/degree-constrained-subgraphs/)

Theorem 1.1: unconditional sparse deterministic reductions for prescribed degrees, degree intervals, and exact or ranged cardinality, with both extension and decoding directions. Cardinality feasibility uses one exact matching call.

**Conditions and remaining work.** The displayed fast running time requires the conditional general-matching backend, including Contract R. Any correct exact maximum-matching solver suffices for the unconditional reduction theorem.

[Proof](../problems/degree-constrained-subgraphs/proof.md) · [Dependencies](../problems/degree-constrained-subgraphs/sources.md) · [Evidence](../problems/degree-constrained-subgraphs/verify/README.md) · Reviewed 2026-10-26

### [Matroid and submodular failure summaries](../problems/matroid-failure-summaries/)

Main Theorems 1–5: represented prefix lift; sharp oracle-rank and integral-value constructions; sharp one-failure weighted endpoint; explicit weighted obstruction; deterministic arbitrary-budget prefix construction. The two-stage rank construction has linear input dependence for fixed parameters.

**Conditions and remaining work.** Oracle results require the stated independence or value oracle; they bound retained original items, not an encoding of an arbitrary oracle. The exact general weighted-oracle optimum size beyond one failure is not determined. Finite programs complement the written proofs and do not constitute formal verification.

[Proof](../problems/matroid-failure-summaries/proof.md) · [Dependencies](../problems/matroid-failure-summaries/sources.md) · [Evidence](../problems/matroid-failure-summaries/verify/README.md) · Reviewed 2026-10-26

## Components ready for review

### [Faster deterministic Subset Sum](../problems/subset-sum-fast-deterministic/)

The refined parameter and compiler-allowance update in Part II, Sections 6–7: the retyped initial difference-table bound, exact reflected-profile budget, and all nine outer cost rates. The new scalar tuple was independently recalculated against the existing compiler lemmas.

**Conditions and remaining work.** The arbitrary-input signed-circuit compiler and witness reduction remain mathematical manuscript proofs; the numerical certificates do not formalize them. The deterministic startup constant is finite and input-independent but has no practical numerical bound.

[Proof](../problems/subset-sum-fast-deterministic/proof.md) · [Dependencies](../problems/subset-sum-fast-deterministic/sources.md) · [Evidence](../problems/subset-sum-fast-deterministic/verify/README.md) · Reviewed 2026-10-26

### [Low-space deterministic Subset Sum](../problems/subset-sum-low-space-deterministic/)

The two-short-range theorem, including signed-input normalization, nested residue streams, indexed witnesses, and the self-contained exact Boolean convolution lemma. The general low-space ledger now explicitly charges the one-bit deficiency-proxy loss.

**Conditions and remaining work.** The stronger n/6 space exponent requires the supplied three-block partition and its two short normalized ranges. The general 0.18261635770550353-space theorem is a separate algorithm; finite range tests do not verify its full storage schedule.

[Proof](../problems/subset-sum-low-space-deterministic/proof.md) · [Dependencies](../problems/subset-sum-low-space-deterministic/sources.md) · [Evidence](../problems/subset-sum-low-space-deterministic/verify/README.md) · Reviewed 2026-10-26

### [Prefix, laminar and sparse quotas](../problems/weighted-prefix-quota-frontier/)

The sharp sparse-packing FPT restriction, arbitrary signed-profit ordered extension, capacity-sensitive failure budget, exact original-context lower construction, and the aggregate laminar reduction to at most B lower rows.

**Conditions and remaining work.** The smaller sparse ground uses explicit FPT preprocessing; it is distinct from the uniform polynomial sunflower tradeoff. These checks do not verify the family’s general valuated completion, universal-coloring construction or lower-bound literature. Original oracles and weights remain available after restriction.

[Proof](../problems/weighted-prefix-quota-frontier/proof.md) · [Dependencies](../problems/weighted-prefix-quota-frontier/sources.md) · [Evidence](../problems/weighted-prefix-quota-frontier/verify/README.md) · Reviewed 2026-10-26

### [Deterministic general-graph maximum matching](../problems/general-matching/)

The unconditional input reductions in Section 3: the sharp c-neighbor kernel, componentwise composition, the native mixed-failure kernel in the companion, and the subcubic reduction with its decoder.

**Conditions and remaining work.** The four-fifths running-time theorem remains conditional on Contract R and the deterministic primitives listed in sources.md. The mixed-failure kernel assumes a fixed simple graph; discarded parallel records and correlated labels are outside its scope.

[Proof](../problems/general-matching/proof.md) · [Dependencies](../problems/general-matching/sources.md) · [Evidence](../problems/general-matching/verify/README.md) · Reviewed 2026-10-26

## Review pending

These families have not yet received a scoped readiness entry in this registry. Their existing statements retain their own assumptions.

- [Numeric targets and support patterns](../problems/numeric-target-frontier/)
- [Static and threshold min-cost flow](../problems/min-cost-flow/)
- [Incremental strongly connected components](../problems/incremental-scc/)
- [Incremental directed SSSP](../problems/incremental-sssp/)
- [Fully dynamic APSP](../problems/apsp-frontier/)
- [Dynamic spanners](../problems/dynamic-spanners/)
- [Dynamic minimum spanning forest](../problems/dynamic-msf/)
- [Strong forests and Gomory–Hu trees](../problems/decremental-strong-forest/)
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
- [problems/general-matching/verify/check_reductions.py](../problems/general-matching/verify/check_reductions.py)
- [problems/group-metric-constraints/verify/check_quotient_rounding.py](../problems/group-metric-constraints/verify/check_quotient_rounding.py)
- [problems/matroid-failure-summaries/verify/check_summaries.py](../problems/matroid-failure-summaries/verify/check_summaries.py)
- [problems/matroid-failure-summaries/verify/check_weighted_obstruction.py](../problems/matroid-failure-summaries/verify/check_weighted_obstruction.py)
- [problems/matroid-failure-summaries/verify/check_weighted_prefix.py](../problems/matroid-failure-summaries/verify/check_weighted_prefix.py)
- [problems/subset-sum-fast-deterministic/verify/check_energy.py](../problems/subset-sum-fast-deterministic/verify/check_energy.py)
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

Set a readiness scope only after checking the corresponding proof, algorithm, representation, randomness and source requirements. Name unresolved backend contracts beside the scope. Update `registry.json`, then run `python3 tools/build_reviews.py`; this synchronizes these entries with the reviewed problem cards. A changed theorem or dependency requires a new scope assessment.

See [Contributing](../CONTRIBUTING.md) for the manuscript workflow and [provenance](../provenance/README.md) for imported source identities.
