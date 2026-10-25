# Algorithm Frontier

A source-linked catalogue of deterministic algorithms, exact and approximation schemes, dynamic graph results, and lower-bound records.

[![Curation checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

## Start here

- [Contents](CONTENTS.md) — canonical, complete map of the catalogue.
- [Featured results](OVERVIEW.md) — the short reading path and current headline records.
- [Complexity guide](docs/COMPLEXITY.md) — shared parameters, models, and display rules.
- [Priority tiers](docs/PRIORITY.md) — how results are surfaced and maintained.
- [Repository map](docs/REPOSITORY_MAP.md) — where curated records, sources, and checkpoints live.
- [Maintenance loop](docs/MAINTENANCE_LOOP.md) — the repeatable discovery and review process.

## Featured results

| Family | Guarantee | Complexity or resource bound | Scope |
|---|---|---|---|
| [General-graph matching](problems/general-matching/) | Exact maximum-cardinality matching | `O(n + m) + (m_s + 1) exp(O((log(m_s + 2))^(4/5) * (log log(m_s + 4))^(1/5)))` | Conditional backend contract |
| [Faster Subset Sum](problems/subset-sum-fast-deterministic/) | Exact indexed witness | `C + poly(n, L) * 2^(E n)`, `E < 0.4964618056` | Signed binary integers |
| [Low-space Subset Sum](problems/subset-sum-low-space-deterministic/) | Exact indexed witness | Time `poly(n, L) * 2^(n/2)`; space `poly(n, L) * 2^(E_S n)` | Separate algorithm |
| [Selected flow](problems/selected-flow/) | Rate at least `(1 - eps) OPT` | `Gamma(1/eps)^c * poly(H)` | Exact capacities and selection constraints |
| [Arbitrary processing scheduling](problems/arbitrary-processing-scheduling/) | Makespan at most `(1 + eps) OPT` | `2^(O(q/eps) * poly(H_eps))` | Mandatory jobs and exact budget |
| [Exact 3/2 scheduling](problems/six-profile-three-halves/) | Makespan at most `3 OPT / 2` | `6^q * poly(H)` | Six-profile endpoint |
| [Dynamic APSP](problems/apsp-frontier/) | Pareto update/stretch tradeoffs | Multiple exponential update/stretch points | Fully dynamic graph |
| [Dynamic spanners](problems/dynamic-spanners/) | 4/5 and 5/6 recourse regimes | `exp(O(U^(4/5) / h^(1/5)))` and `exp(O(U^(5/6) / h^(1/6)))` | Tracked-terminal and full-horizon scopes |
| [Incremental SSSP](problems/incremental-sssp/) | Distance estimates and simple paths | `O(n + m) + (n + m) exp(O(U^(4/5) / h^(1/5) + sqrt(U) * (h + log(1/eps))))` | Incremental directed graphs |
| [Numeric-target frontier](problems/numeric-target-frontier/) | Exact target decisions, optimization, and support-sensitive bounds | R: `2^(O((T + 1) log(T + 2)) * poly(H))`; S: `2^(O(T log(2 + Q/T)) * poly(H))` | Incremental R/S checkpoints |
| [Weighted-prefix and sparse-quota frontier](problems/weighted-prefix-quota-frontier/) | Exact ordered, laminar, and sparse-quota results with deterministic kernel reductions | T/U: from `2^O(B)` and `2^O(B log(B + 2))` to sparse `2^O(Delta B0 log(Delta B0 B + 2))` | Incremental T/U checkpoints |

## Record layout

Each curated problem keeps a compact, auditable contract:

- `README.md` — display-first guarantee, objective, complexity, model, and status;
- `proof.md` — proof map and claim boundaries;
- `verify/` — focused audits or executable-check pointers;
- `sources.md` — exact provenance and attribution.

Imported manuscripts stay under `sources/`. Checkpoint increments keep their original filenames and live in separate directories so parent links, archive hashes, and supersession status remain auditable.

GitHub-facing curation pages use plain-text complexity in code spans. Original TeX and long mathematical derivations remain in source manuscripts or checkpoint records, where notation can be preserved without making the index hard to scan.

## Citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25 (2026). Apache License 2.0.

Cite the relevant problem path and commit, state whether the curated layer was changed, and retain the applicable Apache-2.0 and NOTICE files. See [PROTOCOL.md](PROTOCOL.md).
