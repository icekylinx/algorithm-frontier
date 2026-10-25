# Problem families

`problems/` is organised by mathematical family. A family groups records that share an input model or a proof interface; it does not imply that two records in the same family have comparable guarantees.

## Subset Sum

Exact signed-binary Subset Sum with indexed witness recovery.

- [Faster deterministic Subset Sum](../problems/subset-sum-fast-deterministic/): time exponent below one half; no separate space claim.
- [Low-space deterministic Subset Sum](../problems/subset-sum-low-space-deterministic/): one-half time exponent with an explicit writable-space exponent.

## Numeric targets and quota systems

Integral target feasibility and scalar optimisation under globally coupled, ordered, laminar, or sparse quota constraints.

- [Numeric-target frontier](../problems/numeric-target-frontier/): R/S target magnitude and support-sensitive records.
- [Weighted-prefix and sparse-quota frontier](../problems/weighted-prefix-quota-frontier/): T/U ordered-prefix, laminar, sparse, and ground-kernel records.

## Dynamic graphs

Update-sensitive graph maintenance, distance oracles, spanners, and connectivity.

- [Dynamic APSP](../problems/apsp-frontier/)
- [Dynamic spanners](../problems/dynamic-spanners/)
- [Incremental SSSP](../problems/incremental-sssp/)
- [Incremental SCC](../problems/incremental-scc/)
- [Dynamic minimum spanning forest](../problems/dynamic-msf/)
- [Decremental strong forest and Gomory--Hu transfer](../problems/decremental-strong-forest/)

## Matching and graph optimisation

Exact matching, degree-constrained subgraphs, and flow primitives used by several allocation records.

- [General-graph matching](../problems/general-matching/)
- [Strong Haxell hypergraph matching](../problems/strong-haxell-matching/)
- [Independent transversal](../problems/independent-transversal/)
- [Degree-constrained subgraphs](../problems/degree-constrained-subgraphs/)
- [Static and threshold min-cost flow](../problems/min-cost-flow/)

## Allocation and matroid systems

Integral allocation with player matroids, recipient polymatroids, item matroid unions, or configuration comparators.

- [Arbitrary-value allocation](../problems/arbitrary-value-allocation-scheme/)
- [Recipient polymatroids](../problems/recipient-polymatroid/)
- [Recipient-matroid configuration](../problems/recipient-matroid-configuration/)
- [Explicit-item matroid union](../problems/item-matroid-union/)
- [One-value exact-factor-two allocation](../problems/one-value-exact-two/)
- [Compulsory two-value exact-factor-two allocation](../problems/two-value-exact-two/)
- [Intrinsic values near factor two](../problems/intrinsic-values-near-two/)
- [Unrelated-value additive allocation](../problems/unrelated-values-additive/)
- [Unrelated values with a joint role](../problems/unrelated-values-joint-role/)
- [Whole-ground allocation and scheduling transfers](../problems/whole-ground-allocation/)
- [Selected splittable concurrent flow](../problems/selected-flow/)

## Robust allocation and flow

Common selections with scenario-adaptive assignments or routings.

- [Robust selected flow](../problems/robust-scenario-flow/)
- [Selected flow with shared setup](../problems/shared-setup-flow/)
- [Robust bounded certificates](../problems/robust-bounded-certificates/)
- [Robust unrelated allocation](../problems/robust-unrelated-allocation/)
- [Robust width-two allocation](../problems/robust-width-two-allocation/)
- [Two-scenario robust allocation hardness](../problems/robust-two-scenario-hardness/)

## Scheduling

Makespan schemes parameterised by machine profiles, job sizes, commitments, buckets, or workload rank.

- [Activated-machine scheduling](../problems/activated-machine-scheduling/)
- [Arbitrary-processing scheduling](../problems/arbitrary-processing-scheduling/)
- [Commitment scheduling](../problems/commitment-scheduling/)
- [Many-size workload scheduling](../problems/many-size-scheduling/)
- [Two-size makespan scheduling](../problems/two-size-scheduling/)
- [Per-machine two-time scheduling](../problems/two-time-scheduling/)
- [Processing-bucket tradeoff](../problems/processing-bucket-tradeoff/)
- [Six-profile three-halves scheduling](../problems/six-profile-three-halves/)

## Lower bounds and barriers

Records whose primary contribution is a query barrier, obstruction, or robustness boundary.

- [Allocation and scheduling oracle barriers](../problems/allocation-lower-bounds/)

## Record contract

Each directory contains a concise `README.md`. A proof map, verification material, and source map are included when the record has reached that review stage. The [review registry](../reviews/README.md) records proof, algorithm, source, and finite-check status. Imported manuscripts remain under `sources/`.

## Incoming draft checkpoint X

The following source files are grouped by family for review. They remain
source-only and carry a draft marker; they are not promoted problem records.

### Matching and graph optimisation

- [Single-failure arborescences and matroid intersection](../sources/checkpoint-x/01_exact_single_failure_arborescences_and_matroid_intersection.md)
- [Valuated matroid intersection](../sources/checkpoint-x/09_valuated_matroid_intersection.md)

### Subset Sum

- [Deterministic Subset Sum increment](../sources/checkpoint-x/02_deterministic_subset_sum_increment.md)

### Dynamic graphs and topological certificates

- [Correlated-fault boundary and persistence sparsifiers](../sources/checkpoint-x/03_correlated_fault_boundary_and_persistence_sparsifiers.md)
- [Coloured graph and vertex-failure certificates](../sources/checkpoint-x/05_colored_graph_and_vertex_failure_certificates.md)

### Allocation and matroid systems

- [Represented matroid failure summaries](../sources/checkpoint-x/04_sharp_represented_matroid_failure_summaries.md)
- [Arbitrary matroid and submodular failure summaries](../sources/checkpoint-x/06_arbitrary_matroid_and_submodular_failure_summaries.md)
- [Represented resource-packing transfer](../sources/checkpoint-x/07_represented_resource_packing_transfer.md)

### Numeric targets and quota systems

- [Boolean linear-optimization compiler](../sources/checkpoint-x/08_boolean_linear_optimization_compiler.md)

The draft payloads have non-promoted review cards: [single-failure preservers](../problems/exact-failure-preservers-x-draft/), [faster Subset Sum increment](../problems/subset-sum-fast-deterministic-x-draft/), [persistent-homology certificates](../problems/persistence-failure-certificates-x-draft/), [graph color-failure certificates](../problems/graph-color-failure-certificates-x-draft/), [matroid failure summaries](../problems/matroid-failure-summaries-x-draft/), [packing and matching summaries](../problems/packing-matching-summaries-x-draft/), and [Boolean linear compiler](../problems/boolean-linear-compiler-x-draft/). These cards remain outside the stable family lists until the three review roles sign off.
