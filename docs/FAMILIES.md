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

The complete X source tree is grouped below by mathematical family. Every item is source-only and retains a draft marker; no payload is a stable result card.

### Exact sensitivity, flow, and matching

- [01 — single-failure arborescences and matroid intersection](../sources/checkpoint-x/01_exact_single_failure_arborescences_and_matroid_intersection.md)
- [09 — valuated matroid intersection](../sources/checkpoint-x/09_valuated_matroid_intersection.md)
- [10 — exact minimum-cost flow and vertex-disjoint paths](../sources/checkpoint-x/10_exact_min_cost_flow_and_vertex_disjoint_paths.md)
- [12 — linear single-fault matching](../sources/checkpoint-x/12_linear_single_fault_general_matching.md)
- [13 — linear unweighted two-matroid certificate](../sources/checkpoint-x/13_linear_unweighted_two_matroid_certificate.md)
- [14 — nonnegative sensitivity compiler](../sources/checkpoint-x/14_general_nonnegative_sensitivity_compiler.md)
- [16 — one-element price sensitivity](../sources/checkpoint-x/16_compact_one_element_price_sensitivity.md)

### Subset Sum

- [02 — deterministic Subset Sum increment](../sources/checkpoint-x/02_deterministic_subset_sum_increment.md)

### Correlated spectral, regression, and seminorm summaries

- [03 — persistent boundary certificates](../sources/checkpoint-x/03_correlated_fault_boundary_and_persistence_sparsifiers.md)
- [11 — spectral and Lewis-weight summaries](../sources/checkpoint-x/11_correlated_failure_spectral_and_regression_summaries.md)
- [15 — weak convex regression](../sources/checkpoint-x/15_weak_convex_regression_under_correlated_failures.md)
- [17 — label-vector spectral lifts](../sources/checkpoint-x/17_label_vector_spectral_and_norm_lifts.md)
- [18 — correlated vertex/edge spectral graphs](../sources/checkpoint-x/18_correlated_vertex_and_edge_failure_spectral_graphs.md)
- [19 — graded incidence and simplicial spectra](../sources/checkpoint-x/19_graded_incidence_and_simplicial_spectral_sparsification.md)
- [26 — seminorms under correlated failures](../sources/checkpoint-x/26_arbitrary_seminorms_under_correlated_failures.md)

### Matroid, packing, cuts, and whole blocks

- [04 — represented matroid failure summaries](../sources/checkpoint-x/04_sharp_represented_matroid_failure_summaries.md)
- [05 — colored graph and vertex-failure certificates](../sources/checkpoint-x/05_colored_graph_and_vertex_failure_certificates.md)
- [06 — arbitrary matroid and submodular summaries](../sources/checkpoint-x/06_arbitrary_matroid_and_submodular_failure_summaries.md)
- [07 — represented resource-packing transfer](../sources/checkpoint-x/07_represented_resource_packing_transfer.md)
- [27 — adaptive quotient resparsification](../sources/checkpoint-x/27_adaptive_quotient_resparsification.md)
- [28 — exact label cuts and matroid quotients](../sources/checkpoint-x/28_exact_label_cut_and_matroid_quotient_sparsification.md)
- [29 — exact whole blocks and hyperedges](../sources/checkpoint-x/29_exact_label_whole_blocks_and_hyperedges.md)

### Boolean linear compiler

- [08 — Boolean linear-optimization compiler](../sources/checkpoint-x/08_boolean_linear_optimization_compiler.md)

### Group, affine, metric, quotient-rank, and obstruction boundaries

- [20 — arbitrary-group Cayley sparsification](../sources/checkpoint-x/20_arbitrary_group_cayley_sparsification.md)
- [30 — whole subgroup constraints](../sources/checkpoint-x/30_optimal_whole_subgroup_constraints.md)
- [31 — affine constraints over finite groups](../sources/checkpoint-x/31_affine_constraints_over_arbitrary_finite_groups.md)
- [32 — transitive metrics and group alignment](../sources/checkpoint-x/32_transitive_metrics_and_group_alignment.md)
- [33 — exact separation for compact codes](../sources/checkpoint-x/33_exact_separation_for_compact_codes.md)
- [35 — rational quotient ranks](../sources/checkpoint-x/35_rational_quotient_ranks_from_weak_oracles.md)
- [36 — affine modular blocks](../sources/checkpoint-x/36_affine_modular_blocks_and_sharp_modulus_dependence.md)
- [37 — few-orbit Hilbert metrics](../sources/checkpoint-x/37_hilbert_metric_sums_with_few_orbits.md)
- [38 — non-Fano obstruction](../sources/checkpoint-x/38_non_fano_obstruction_to_fixed_amplitude_bound.md)

### Quantum, Pauli, qudit, and stabilizer blocks

- [21 — arbitrary-locality Pauli sparsification](../sources/checkpoint-x/21_arbitrary_locality_pauli_sparsification.md)
- [22 — prime-qudit checks](../sources/checkpoint-x/22_arbitrary_locality_prime_qudit_checks.md)
- [23 — stabilizer block sparsification](../sources/checkpoint-x/23_arbitrary_locality_stabilizer_block_sparsification.md)
- [24 — arbitrary-dimension Weyl checks](../sources/checkpoint-x/24_arbitrary_dimension_weyl_checks.md)
- [25 — commuting surrogates and stabilizer witnesses](../sources/checkpoint-x/25_commuting_surrogates_and_stabilizer_energy_witnesses.md)
- [34 — arbitrary-dimension whole stabilizer blocks](../sources/checkpoint-x/34_arbitrary_dimension_whole_stabilizer_blocks.md)

The corresponding non-promoted cards are listed in [`CONTENTS.md`](../CONTENTS.md). New family-level review handles are [exact sensitivity, flow, and matching](../problems/exact-flow-sensitivity-x-draft/), [correlated spectral/regression summaries](../problems/correlated-spectral-regression-x-draft/), [finite-group and metric constraints](../problems/group-metric-constraints-x-draft/), [quantum and stabilizer blocks](../problems/quantum-stabilizer-x-draft/), [label/block cuts](../problems/label-block-cut-x-draft/), and [exact-separation boundaries](../problems/obstruction-boundaries-x-draft/). The [review backlog](../reviews/backlog/checkpoint-x-drafts.md) records the proof, algorithm, and source gates.
