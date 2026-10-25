# Algorithm Frontier

**Attribution:** Yilin Liu · **AI contribution identifier:** GPT-6 Astra Pro
**License:** Apache License 2.0
**Citation:** [`PROTOCOL.md`](PROTOCOL.md) · [`CITATION.cff`](CITATION.cff)

Algorithm Frontier presents exact algorithms, approximation schemes, dynamic
graph algorithms, and their proof and verification records. Each problem has a
compact README, a proof map, and several verification entries. The complete
mathematical source is linked from the problem directory.

## Main results

| Problem | Main guarantee | Complexity or resource bound | Scope |
|---|---|---|---|
| [Deterministic general-graph maximum matching](problems/general-matching/) | Exact maximum-cardinality matching | $$O(n+m)+(m_s+1)\exp(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}))$$ | Conditional backend contract; arbitrary undirected graphs |
| [Faster deterministic Subset Sum](problems/subset-sum-fast-deterministic/) | Exact indexed witness | $$C+\mathrm{poly}(n,L)2^{En}$$, $$E<0.4964618056$$ | Arbitrary signed binary integers |
| [Deterministic low-space Subset Sum](problems/subset-sum-low-space-deterministic/) | Exact indexed witness | Time $$\mathrm{poly}(n,L)2^{n/2}$$; space $$\mathrm{poly}(n,L)2^{E_Sn}$$, $$E_S<0.1826163578$$ | Same input model; separate algorithm |
| [Selected splittable flow](problems/selected-flow/) | Rate at least $$(1-\varepsilon)\mathrm{OPT}$$ | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Exact routing capacities and selection constraints |
| [Static and threshold min-cost flow](problems/min-cost-flow/) | Exact flow and witness recovery | Conditional raw-backend bound with the stated $$E^4$$ numerical term | Static and fixed-threshold clients |
| [Arbitrary-value allocation](problems/arbitrary-value-allocation-scheme/) | Value at least $$(1-\varepsilon)\mathrm{OPT}$$ | $$\binom{q}{r}\exp(O(r/\varepsilon))\,\mathrm{poly}(H_\varepsilon)$$ | Optional player basis and exact shared budget |
| [Recipient-polymatroid allocation](problems/recipient-polymatroid/) | Factor $$4-3/r$$ versus integer OPT | $$2^{O(r)}\,\mathrm{poly}(H)$$ | Integral recipient polymatroids |
| [Arbitrary processing-time scheduling](problems/arbitrary-processing-scheduling/) | Makespan at most $$(1+\varepsilon)\mathrm{OPT}$$ | $$2^{O(q/\varepsilon)}\,\mathrm{poly}(H_\varepsilon)$$ | Mandatory jobs and exact budget |
| [Exact 3/2 scheduling](problems/six-profile-three-halves/) | Makespan at most $$3\mathrm{OPT}/2$$ | $$6^q\,\mathrm{poly}(H)$$ | Six-profile endpoint |
| [Dynamic APSP](problems/apsp-frontier/) | Pareto update/stretch tradeoffs | Multiple exponential update/stretch points | Fully dynamic graph model |
| [Dynamic spanners](problems/dynamic-spanners/) | 4/5 and 5/6 recourse regimes | Stretch/work $$\exp(O(U^{4/5}h^{1/5}))$$ and $$\exp(O(U^{5/6}h^{1/6}))$$ | Tracked-terminal and full-horizon scopes |
| [Incremental SSSP](problems/incremental-sssp/) | Distance estimates and simple-path reporting | $$O(n+m)+(n+m)\exp(O(U^{4/5}h^{1/5}+\sqrt{U(h+\log(1/\varepsilon))}))$$ | Incremental directed graphs |
| [Incremental SCC](problems/incremental-scc/) | Exact component labels | $$ (n+m)E(N)^{O(1)}\,\mathrm{poly}(U)$$ with the stated subpolynomial backend | Incremental directed graphs |
| [Strong forest and Gomory-Hu transfer](problems/decremental-strong-forest/) | Decremental forest transfer | $$O(n+m)+(m+1)E_6(n+m)$$ | Conditional reduction contract |
| [Strong Haxell matching](problems/strong-haxell-matching/) | Matching or checkable hitting-set certificate | $$O(|A|+|B|)+p\exp(O(U\log(2+s)/s))$$ | Strong-Haxell model |

The [full algorithm index](OVERVIEW.md) lists the remaining allocation,
scheduling, flow, dynamic graph, and lower-bound modules.

## Problem record format

Each problem directory contains:

- `README.md`: guarantee, complexity, space, model, and status table;
- `proof.md`: concise proof map with the complete source link;
- `verify/`: audit notes, source comparisons, or executable-check pointers;
- `sources.md`: exact provenance paths.

The authored curation layer uses `$$ ... $$` for displayed mathematics. Original
source files are preserved under `sources/` and retain their own notation and
license boundaries.

## Citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25
> (2026). Apache License 2.0.

Preserve the attribution, cite the problem path and commit, indicate changes,
and retain the applicable Apache-2.0 and NOTICE files. See [`PROTOCOL.md`](PROTOCOL.md).
