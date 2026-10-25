# Contents

This is the canonical catalogue of the curated result records. Browse by [problem family](docs/FAMILIES.md); the [overview](OVERVIEW.md) gives the short reading path and the [review registry](reviews/README.md) gives claim status.

## Headline records

| Family | Record | Main quantity shown on the card |
|---|---|---|
| Numeric targets | [Numeric-target frontier](problems/numeric-target-frontier/) | Target magnitude, support geometry, and exact/approximate regimes |
| Quota systems | [Weighted-prefix and sparse-quota frontier](problems/weighted-prefix-quota-frontier/) | Prefix, laminar, sparse, and ground-kernel parameters |
| Subset Sum | [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/) | Exact witness time exponent below 0.4964618056 |
| Subset Sum | [Low-space deterministic Subset Sum](problems/subset-sum-low-space-deterministic/) | Time exponent and explicit writable-space exponent |
| Dynamic graphs | [Dynamic APSP](problems/apsp-frontier/) | Update work versus distance stretch |
| Matching | [General-graph matching](problems/general-matching/) | Exact cardinality under the stated backend |

## Incoming draft checkpoint

[Checkpoint X](sources/checkpoint-x/) is an English source-only bundle of
rough research drafts. It is indexed by the families below for review and
future promotion; no theorem in this bundle is a curated result card yet.

| Family hint | Draft source | Curation state |
|---|---|---|
| Matching and graph optimisation | [Single-failure arborescences and matroid intersection](sources/checkpoint-x/01_exact_single_failure_arborescences_and_matroid_intersection.md); [valuated matroid intersection](sources/checkpoint-x/09_valuated_matroid_intersection.md) | Draft; proof, algorithm, and source review pending |
| Subset Sum | [Deterministic Subset Sum increment](sources/checkpoint-x/02_deterministic_subset_sum_increment.md) | Draft; depends on the existing fast-time proof |
| Dynamic graphs and topological certificates | [Correlated-fault boundary and persistence](sources/checkpoint-x/03_correlated_fault_boundary_and_persistence_sparsifiers.md); [coloured graph and vertex-failure certificates](sources/checkpoint-x/05_colored_graph_and_vertex_failure_certificates.md) | Draft; model and scope review pending |
| Allocation and matroid systems | [Represented matroid failure summaries](sources/checkpoint-x/04_sharp_represented_matroid_failure_summaries.md); [arbitrary matroid and submodular summaries](sources/checkpoint-x/06_arbitrary_matroid_and_submodular_failure_summaries.md); [represented resource-packing transfer](sources/checkpoint-x/07_represented_resource_packing_transfer.md) | Draft; representation and comparator review pending |
| Numeric targets and quota systems | [Boolean linear-optimization compiler](sources/checkpoint-x/08_boolean_linear_optimization_compiler.md) | Draft; backend and parameter review pending |

These payloads also have **non-promoted draft cards** for review: [single-failure preservers](problems/exact-failure-preservers-x-draft/), [faster Subset Sum increment](problems/subset-sum-fast-deterministic-x-draft/), [persistent-homology certificates](problems/persistence-failure-certificates-x-draft/), [graph color-failure certificates](problems/graph-color-failure-certificates-x-draft/), [matroid failure summaries](problems/matroid-failure-summaries-x-draft/), [packing and matching summaries](problems/packing-matching-summaries-x-draft/), and [Boolean linear compiler](problems/boolean-linear-compiler-x-draft/). They are deliberately outside the stable family lists below.

## Subset Sum

- [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/)
- [Low-space deterministic Subset Sum](problems/subset-sum-low-space-deterministic/)

## Numeric targets and quota systems

- [Numeric-target frontier](problems/numeric-target-frontier/)
- [Weighted-prefix and sparse-quota frontier](problems/weighted-prefix-quota-frontier/)

## Dynamic graphs

- [Dynamic APSP](problems/apsp-frontier/)
- [Dynamic spanners](problems/dynamic-spanners/)
- [Incremental SSSP](problems/incremental-sssp/)
- [Incremental SCC](problems/incremental-scc/)
- [Dynamic minimum spanning forest](problems/dynamic-msf/)
- [Decremental strong forest and Gomory--Hu transfer](problems/decremental-strong-forest/)

## Matching and graph optimisation

- [General-graph matching](problems/general-matching/)
- [Strong Haxell hypergraph matching](problems/strong-haxell-matching/)
- [Independent transversal](problems/independent-transversal/)
- [Degree-constrained subgraphs](problems/degree-constrained-subgraphs/)
- [Static and threshold min-cost flow](problems/min-cost-flow/)

## Allocation and matroid systems

- [Arbitrary-value allocation](problems/arbitrary-value-allocation-scheme/)
- [Recipient polymatroids](problems/recipient-polymatroid/)
- [Recipient-matroid configuration](problems/recipient-matroid-configuration/)
- [Explicit-item matroid union](problems/item-matroid-union/)
- [One-value exact-factor-two allocation](problems/one-value-exact-two/)
- [Compulsory two-value exact-factor-two allocation](problems/two-value-exact-two/)
- [Intrinsic values near factor two](problems/intrinsic-values-near-two/)
- [Unrelated-value additive allocation](problems/unrelated-values-additive/)
- [Unrelated values with a joint role](problems/unrelated-values-joint-role/)
- [Whole-ground allocation and scheduling transfers](problems/whole-ground-allocation/)
- [Selected splittable concurrent flow](problems/selected-flow/)

## Robust allocation and flow

- [Robust selected flow](problems/robust-scenario-flow/)
- [Selected flow with shared setup](problems/shared-setup-flow/)
- [Robust bounded certificates](problems/robust-bounded-certificates/)
- [Robust unrelated allocation](problems/robust-unrelated-allocation/)
- [Robust width-two allocation](problems/robust-width-two-allocation/)
- [Two-scenario robust allocation hardness](problems/robust-two-scenario-hardness/)

## Scheduling

- [Activated-machine scheduling](problems/activated-machine-scheduling/)
- [Arbitrary-processing scheduling](problems/arbitrary-processing-scheduling/)
- [Commitment scheduling](problems/commitment-scheduling/)
- [Many-size workload scheduling](problems/many-size-scheduling/)
- [Two-size makespan scheduling](problems/two-size-scheduling/)
- [Per-machine two-time scheduling](problems/two-time-scheduling/)
- [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/)
- [Six-profile three-halves scheduling](problems/six-profile-three-halves/)

## Lower bounds and barriers

- [Allocation and scheduling oracle barriers](problems/allocation-lower-bounds/)

## Review and provenance

- [Review registry](reviews/README.md)
- [Complexity conventions](docs/COMPLEXITY.md)
- [Priority and display rules](docs/PRIORITY.md)
- [Repository map](docs/REPOSITORY_MAP.md)
- [Maintenance loop](docs/MAINTENANCE_LOOP.md)
- [History](HISTORY.md)
- [Source manifests](sources/)
