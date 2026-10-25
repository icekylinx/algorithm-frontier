# Contents

This is the canonical map of the repository. The short reading path is [`OVERVIEW.md`](OVERVIEW.md); this page keeps the full catalogue visible and gives each family a stable entry point.

## Headline records

| Record | Role | Displayed complexity or boundary |
|---|---|---|
| [Numeric-target frontier](problems/numeric-target-frontier/) | Tier A: newest R/S incremental family | R: `2^(O((T + 1) log(T + 2)) * poly(H))`; S: `2^(O(T log(2 + Q/T)) * poly(H))` |
| [Weighted-prefix and sparse-quota frontier](problems/weighted-prefix-quota-frontier/) | Tier A: newest T/U extension | T/U: `2^O(B)`, `2^O(B log(B + 2))`, `2^O(B^2)`, and sparse `2^O(Delta B0 log(Delta B0 B + 2))` |
| [Faster Subset Sum](problems/subset-sum-fast-deterministic/) | Tier A: exact exponential-time record | `C + poly(n, L) * 2^(E n)`, `E < 0.4964618056` |
| [Low-space Subset Sum](problems/subset-sum-low-space-deterministic/) | Tier A: explicit space-sensitive record | Time `poly(n, L) * 2^(n/2)`; space `poly(n, L) * 2^(E_S n)` |
| [General-graph matching](problems/general-matching/) | Tier A: exact matching backend composition | Conditional fast backend; see record for full bound |
| [Dynamic APSP](problems/apsp-frontier/) | Tier A: update/stretch frontier | Multiple Pareto points |

## Graph algorithms and matching

| Record | Role |
|---|---|
| [General matching](problems/general-matching/) | Exact arbitrary-graph matching with a conditional backend |
| [Dynamic APSP](problems/apsp-frontier/) | Fully dynamic all-pairs shortest paths tradeoffs |
| [Dynamic spanners](problems/dynamic-spanners/) | Dynamic spanner recourse regimes |
| [Incremental SSSP](problems/incremental-sssp/) | Incremental directed single-source shortest paths |
| [Incremental SCC](problems/incremental-scc/) | Incremental strongly connected components |
| [Dynamic MSF](problems/dynamic-msf/) | Dynamic minimum spanning forest baseline |
| [Decremental strong forest](problems/decremental-strong-forest/) | Decremental strong-forest and Gomory–Hu transfer |
| [Strong Haxell matching](problems/strong-haxell-matching/) | Matching or checkable hitting-set certificate |
| [Independent transversal](problems/independent-transversal/) | Certified transversal or obstruction |

## Allocation, flow, and polymatroids

| Record | Role |
|---|---|
| [Selected flow](problems/selected-flow/) | Selected splittable concurrent flow |
| [Robust scenario flow](problems/robust-scenario-flow/) | Scenario-wise robust routing |
| [Shared-setup flow](problems/shared-setup-flow/) | Flow with an exact shared setup budget |
| [Min-cost flow](problems/min-cost-flow/) | Exact flow witness and backend transfer |
| [Degree-constrained subgraphs](problems/degree-constrained-subgraphs/) | f-factor, interval, and cardinality reductions |
| [Arbitrary-value allocation](problems/arbitrary-value-allocation-scheme/) | Optional actual-basis allocation scheme |
| [Recipient polymatroids](problems/recipient-polymatroid/) | Integral recipient polymatroid approximation |
| [Recipient-matroid configuration](problems/recipient-matroid-configuration/) | Coupled recipient configuration model |
| [Item matroid union](problems/item-matroid-union/) | Explicit-item matroid-union model |
| [One-value exact-two allocation](problems/one-value-exact-two/) | One-value exact-two endpoint |
| [Two-value exact-two allocation](problems/two-value-exact-two/) | Compulsory two-value endpoint |
| [Intrinsic values near two](problems/intrinsic-values-near-two/) | Derived-corank approximation near factor two |
| [Whole-ground allocation](problems/whole-ground-allocation/) | Whole-ground and fixed-`R` tradeoffs |
| [Unrelated-value additive allocation](problems/unrelated-values-additive/) | Player-wise additive guarantee |
| [Unrelated values with joint role](problems/unrelated-values-joint-role/) | Joint role and setup budget |

## Scheduling and profile tradeoffs

| Record | Role |
|---|---|
| [Activated-machine scheduling](problems/activated-machine-scheduling/) | Activated-machine profile basis |
| [Arbitrary-processing scheduling](problems/arbitrary-processing-scheduling/) | Mandatory-job processing profile |
| [Commitment scheduling](problems/commitment-scheduling/) | Bottleneck commitment bound |
| [Many-size scheduling](problems/many-size-scheduling/) | Compressed-rank many-size profile |
| [Two-size scheduling](problems/two-size-scheduling/) | Two-size exact endpoint and tradeoff |
| [Per-machine two-time scheduling](problems/two-time-scheduling/) | Machine-specific two-time model |
| [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/) | Bucket-dependent approximation endpoints |
| [Six-profile scheduling](problems/six-profile-three-halves/) | Exact 3/2 profile endpoint |

## Subset Sum and numeric targets

| Record | Role |
|---|---|
| [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/) | Fast exact signed-binary witness |
| [Low-space deterministic Subset Sum](problems/subset-sum-low-space-deterministic/) | Exact witness with a separate space bound |
| [Numeric-target frontier](problems/numeric-target-frontier/) | R/S target and support-sensitive checkpoint family |
| [Weighted-prefix and sparse-quota frontier](problems/weighted-prefix-quota-frontier/) | T/U ordered, laminar, sparse, and deterministic-kernel checkpoint family |

## Robustness and lower bounds

| Record | Role |
|---|---|
| [Allocation lower bounds](problems/allocation-lower-bounds/) | Hidden-rank oracle barriers |
| [Robust bounded certificates](problems/robust-bounded-certificates/) | Bounded failure-certificate robustness |
| [Robust unrelated allocation](problems/robust-unrelated-allocation/) | Additive robust utility |
| [Robust width-two allocation](problems/robust-width-two-allocation/) | Width-two positivity gate |
| [Two-scenario robust allocation hardness](problems/robust-two-scenario-hardness/) | Explicit two-scenario hardness boundary |

## Source and review surfaces

- [`docs/COMPLEXITY.md`](docs/COMPLEXITY.md) — shared parameters and portable display notation.
- [`docs/PRIORITY.md`](docs/PRIORITY.md) — presentation and maintenance tiers.
- [`docs/MAINTENANCE_LOOP.md`](docs/MAINTENANCE_LOOP.md) — incremental discovery and review workflow.
- [`docs/REPOSITORY_MAP.md`](docs/REPOSITORY_MAP.md) — source, provenance, and tool layout.
- [`HISTORY.md`](HISTORY.md) — append-only public curation log.
- [`MAINTENANCE.md`](MAINTENANCE.md) — release policy and required checks.

GitHub-facing pages use plain-text complexity inside code spans. Imported manuscripts and checkpoint payloads preserve their original notation under `sources/`.
