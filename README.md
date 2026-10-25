# Algorithm Frontier

A source-linked index of deterministic algorithms, exact and approximation schemes, dynamic graph results, and lower-bound records.

[![Curation checks](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml/badge.svg)](https://github.com/icekylinx/algorithm-frontier/actions/workflows/curation.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

## Start here

- [Complete algorithm index](OVERVIEW.md)
- [Complexity guide and notation](docs/COMPLEXITY.md)
- [Repository map](docs/REPOSITORY_MAP.md)
- [Curation protocol](PROTOCOL.md)
- [Maintenance policy](MAINTENANCE.md)

## Featured results

| Family | Guarantee | Complexity or resource bound | Scope |
|---|---|---|---|
| [General-graph matching](problems/general-matching/) | Exact maximum-cardinality matching | $$O(n+m)+(m_s+1)\exp(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}))$$ | Conditional backend contract |
| [Faster Subset Sum](problems/subset-sum-fast-deterministic/) | Exact indexed witness | $$C+\mathrm{poly}(n,L)2^{En}$$, $$E<0.4964618056$$ | Signed binary integers |
| [Low-space Subset Sum](problems/subset-sum-low-space-deterministic/) | Exact indexed witness | Time $$\mathrm{poly}(n,L)2^{n/2}$$; space $$\mathrm{poly}(n,L)2^{E_Sn}$$ | Separate algorithm |
| [Selected flow](problems/selected-flow/) | Rate at least $$(1-\varepsilon)\mathrm{OPT}$$ | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Exact capacities and selection constraints |
| [Arbitrary processing scheduling](problems/arbitrary-processing-scheduling/) | Makespan at most $$(1+\varepsilon)\mathrm{OPT}$$ | $$2^{O(q/\varepsilon)}\,\mathrm{poly}(H_\varepsilon)$$ | Mandatory jobs and exact budget |
| [Exact 3/2 scheduling](problems/six-profile-three-halves/) | Makespan at most $$3\mathrm{OPT}/2$$ | $$6^q\,\mathrm{poly}(H)$$ | Six-profile endpoint |
| [Dynamic APSP](problems/apsp-frontier/) | Pareto update/stretch tradeoffs | Multiple exponential update/stretch points | Fully dynamic graph |
| [Dynamic spanners](problems/dynamic-spanners/) | 4/5 and 5/6 recourse regimes | $$\exp(O(U^{4/5}h^{1/5}))$$ and $$\exp(O(U^{5/6}h^{1/6}))$$ | Tracked-terminal and full-horizon scopes |
| [Incremental SSSP](problems/incremental-sssp/) | Distance estimates and simple paths | $$O(n+m)+(n+m)\exp(O(U^{4/5}h^{1/5}+\sqrt{U(h+\log(1/\varepsilon))}))$$ | Incremental directed graphs |
| [Numeric-target frontier](problems/numeric-target-frontier/) | Exact target decisions, optimization, and support-sensitive bounds | From $$2^{O((T+1)\log(T+2))}\,\mathrm{poly}(H)$$ to $$2^{O(T\log(2+Q/T))}\,\mathrm{poly}(H)$$ | R/S incremental research checkpoints |

## Record layout

Each curated problem keeps the same compact contract:

- `README.md` — guarantee, complexity, model, and status;
- `proof.md` — proof map and source links;
- `verify/` — audit notes or executable-check pointers;
- `sources.md` — exact provenance and attribution.

Imported manuscripts remain under `sources/`. Checkpoint increments are kept in their own directories so that parent links, hashes, and supersession status remain auditable.

## Citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25 (2026). Apache License 2.0.

Cite the relevant problem path and commit, state whether the curated layer was changed, and retain the applicable Apache-2.0 and NOTICE files. See [PROTOCOL.md](PROTOCOL.md).
