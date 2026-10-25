# Algorithm Frontier

A source-linked catalogue of deterministic algorithms, exact and approximation schemes, dynamic graph results, and lower-bound records.

[![Curation checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml) [![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

## Start here

- [Overview PDF](overview.pdf) — compact problem statements, parameters, and complexity bounds.
- [Problem families](docs/FAMILIES.md) — the primary index.
- [Contents](CONTENTS.md) — every curated record.
- [Review registry](reviews/README.md) — proof, algorithm, source, and finite-check status.
- [Complexity conventions](docs/COMPLEXITY.md) — shared parameter names and claim boundaries.

## Catalogue at a glance

| Family | Representative records | Main comparison axis |
|---|---|---|
| **Subset Sum** | [Faster](problems/subset-sum-fast-deterministic/), [low-space](problems/subset-sum-low-space-deterministic/) | Exact witness time and writable space |
| **Numeric targets and quotas** | [Numeric-target](problems/numeric-target-frontier/), [weighted-prefix](problems/weighted-prefix-quota-frontier/) | Target, support, order, and quota geometry |
| **Dynamic graphs** | [APSP](problems/apsp-frontier/), [spanners](problems/dynamic-spanners/), [SSSP](problems/incremental-sssp/) | Update work, stretch, recourse, and query time |
| **Matching and graph optimisation** | [Matching](problems/general-matching/), [degree constraints](problems/degree-constrained-subgraphs/), [min-cost flow](problems/min-cost-flow/) | Exact objective and backend assumptions |
| **Allocation and matroids** | [Recipient polymatroids](problems/recipient-polymatroid/), [item matroid union](problems/item-matroid-union/) | Comparator, rank, value model, and accuracy |
| **Robust allocation and flow** | [Robust flow](problems/robust-scenario-flow/), [bounded certificates](problems/robust-bounded-certificates/) | Scenario coupling and certificate width |
| **Scheduling** | [Many-size](problems/many-size-scheduling/), [two-size](problems/two-size-scheduling/), [six-profile](problems/six-profile-three-halves/) | Makespan factor and profile/rank parameter |
| **Lower bounds** | [Oracle barriers](problems/allocation-lower-bounds/) | Query model, obstruction, and scope |

The family index is deliberately separate from the review status: records in one family can have different proof or source maturity.

## Record contract

Each curated result exposes its guarantee before the supporting detail. A card states the problem and output, model, time, space, parameter definitions, comparator or lower-bound scope, and review status. Proof maps and exact source maps are linked from the card; imported manuscripts remain under `sources/`.

The maintenance loop is documented in [`docs/MAINTENANCE_LOOP.md`](docs/MAINTENANCE_LOOP.md). It has no scheduled job: a new checkpoint or an active review pass reopens the queue, and every change is checked before it reaches `main`.

## Citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25 (2026). Apache License 2.0.

Cite the relevant problem path and commit, state whether the curated layer changed, and retain the applicable Apache-2.0 and NOTICE files. See [PROTOCOL.md](PROTOCOL.md).
