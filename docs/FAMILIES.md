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
