# Algorithm Frontier

A source-linked catalogue of deterministic algorithms, exact and approximation schemes, dynamic graph results, and lower-bound records.

[![Curation checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

## Start here

- [Download the overview PDF](overview.pdf) for the visual reading map, headline cards, parameter comparison, review vocabulary, and checkpoint lineage.
- [Contents](CONTENTS.md) for the complete catalogue.
- [Featured results](OVERVIEW.md) for the short reading path.
- [Review registry](reviews/README.md) for proof, algorithm, source, and finite-check review status.
- [Complexity guide](docs/COMPLEXITY.md) for shared parameters and claim boundaries.
- [Maintenance loop](docs/MAINTENANCE_LOOP.md) for the ongoing discovery and re-audit process.

## At a glance

| Record | Contribution | Reading path |
|---|---|---|
| Numeric-target frontier | Exact target decisions, scalar optimization, support geometry, and encoded lower-bound boundaries. | [R/S record](problems/numeric-target-frontier/) |
| Weighted-prefix and sparse-quota frontier | Ordered prefix quotas, laminar completion, sparse overlap, and deterministic ground kernels. | [T/U record](problems/weighted-prefix-quota-frontier/) |
| Faster Subset Sum | Exact indexed witnesses for signed binary inputs with a sub-half exponential time exponent. | [Fast-time record](problems/subset-sum-fast-deterministic/) |
| Low-space Subset Sum | Exact indexed witnesses with a separate explicit writable-space exponent. | [Low-space record](problems/subset-sum-low-space-deterministic/) |
| Graph frontiers | Exact matching and dynamic update/stretch/recourse tradeoffs under their named models. | [Graph records](CONTENTS.md#graph-algorithms-and-matching) |
| Allocation and scheduling | Source-linked approximation schemes, exact endpoints, robustness records, and barriers. | [Allocation and scheduling](CONTENTS.md#allocation-flow-and-polymatroids) |

The landing page is intentionally short. Exact parameter values, assumptions, lower-bound scopes, and proof status live in the result cards, the overview PDF, and the review reports.

## Reading order

| Tier | Role | Where to start |
|---|---|---|
| **A** | Headline frontier records and the newest parameter boundaries. | Numeric-target, weighted-prefix, faster Subset Sum, low-space Subset Sum, matching, and APSP. |
| **B** | Supporting constructions and reusable dynamic, flow, allocation, or scheduling extensions. | The graph, flow, allocation, and scheduling sections in [`CONTENTS.md`](CONTENTS.md). |
| **C** | Lower bounds, barriers, robustness limits, and endpoint records. | The robustness and lower-bound section in [`CONTENTS.md`](CONTENTS.md). |
| **D** | Imported manuscripts, checkpoint archives, manifests, licenses, and historical snapshots. | [`sources/`](sources/) and the linked provenance pages. |

The tier controls reading order and maintenance attention. It does not rank mathematical truth or replace the model and review fields on an individual record.

## Record contract

Each curated problem keeps a compact, auditable contract:

- `README.md` — result card with guarantee, objective/output, time, space, parameters, representation, lower-bound type, review status, and sources;
- `proof.md` — proof map and claim boundaries;
- `verify/` — focused audits or executable-check pointers;
- `sources.md` — exact provenance and attribution;
- `reviews/` — independent proof, algorithm, and source review reports when the record is in the active review queue.

Imported manuscripts stay under `sources/`. Checkpoint increments keep their original filenames and live in separate directories so parent links, archive hashes, review scope, and supersession status remain auditable.

GitHub-facing cards use readable prose. Detailed symbolic formulas remain in the PDF overview and source manuscripts, where the notation can be preserved without making the landing page hard to scan.

## Citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25 (2026). Apache License 2.0.

Cite the relevant problem path and commit, state whether the curated layer changed, and retain the applicable Apache-2.0 and NOTICE files. See [PROTOCOL.md](PROTOCOL.md).
