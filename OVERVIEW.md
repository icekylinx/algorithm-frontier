# Algorithm index

This is the complete algorithm-facing catalog. Every row links to a problem record whose README states the guarantee, objective, complexity, model, lower-bound type, and review status. Parameterizations with different assumptions remain separate.

## Curated frontier

| Problem | Guarantee | Complexity / resource | Main scope |
|---|---|---|---|
| [General-graph maximum matching](problems/general-matching/) | Exact maximum matching | $$O(n+m)+(m_s+1)\exp(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}))$$ | Conditional arbitrary-graph construction |
| [Faster Subset Sum](problems/subset-sum-fast-deterministic/) | Exact witness | $$C+\mathrm{poly}(n,L)2^{En}$$, $$E<0.4964618056$$ | Signed binary integers |
| [Low-space Subset Sum](problems/subset-sum-low-space-deterministic/) | Exact witness | Time $$\mathrm{poly}(n,L)2^{n/2}$$; space $$\mathrm{poly}(n,L)2^{E_Sn}$$ | Separate low-space algorithm |
| [Numeric-target frontier](problems/numeric-target-frontier/) | Exact targets, optimization, support-sensitive bounds | R: $$2^{O((T+1)\log(T+2))}\,\mathrm{poly}(H)$$; S: $$2^{O(T\log(2+Q/T))}\,\mathrm{poly}(H)$$ | Incremental R/S research checkpoints |
| [Selected flow](problems/selected-flow/) | Rate $$(1-\varepsilon)\mathrm{OPT}$$ | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Exact capacities and selected commodities |
| [Arbitrary processing scheduling](problems/arbitrary-processing-scheduling/) | Makespan $$(1+\varepsilon)\mathrm{OPT}$$ | $$2^{O(q/\varepsilon)}\,\mathrm{poly}(H_\varepsilon)$$ | Mandatory jobs |
| [Exact 3/2 scheduling](problems/six-profile-three-halves/) | Makespan at most $$3\mathrm{OPT}/2$$ | $$6^q\,\mathrm{poly}(H)$$ | Six-profile endpoint |
| [Dynamic APSP](problems/apsp-frontier/) | Update/stretch Pareto frontier | Multiple exponential points | Fully dynamic graph |
| [Dynamic spanners](problems/dynamic-spanners/) | 4/5 and 5/6 recourse regimes | $$\exp(O(U^{4/5}h^{1/5}))$$ and $$\exp(O(U^{5/6}h^{1/6}))$$ | Tracked-terminal and full-horizon scopes |
| [Incremental SSSP](problems/incremental-sssp/) | Distances and simple paths | $$O(n+m)+(n+m)\exp(O(U^{4/5}h^{1/5}+\sqrt{U(h+\log(1/\varepsilon))}))$$ | Directed incremental graph |
| [Incremental SCC](problems/incremental-scc/) | Exact component labels | $$(n+m)E(N)^{O(1)}\,\mathrm{poly}(U)$$ | No path/topological witness claim |
| [Strong forest / Gomory--Hu](problems/decremental-strong-forest/) | Decremental transfer | $$O(n+m)+(m+1)E_6(n+m)$$ | Conditional reduction |

## Allocation and resource models

| Problem | Guarantee | Complexity / resource | Main scope |
|---|---|---|---|
| [Degree-constrained subgraphs](problems/degree-constrained-subgraphs/) | Exact degree-constrained output | Matching-backend envelope | f-factor, interval, and cardinality reductions |
| [Min-cost flow](problems/min-cost-flow/) | Exact flow witness | Conditional raw-backend $$E^4$$ term | Static and fixed-threshold clients |
| [Arbitrary-value allocation](problems/arbitrary-value-allocation-scheme/) | Value $$(1-\varepsilon)\mathrm{OPT}$$ | $$\binom{q}{r}\exp(O(r/\varepsilon))\,\mathrm{poly}(H_\varepsilon)$$ | Optional actual basis |
| [Recipient polymatroids](problems/recipient-polymatroid/) | Factor $$4-3/r$$ | $$2^{O(r)}\,\mathrm{poly}(H)$$ | Integral recipient polymatroids |
| [Recipient-matroid configuration](problems/recipient-matroid-configuration/) | Factor $$4-3/r$$ against the coupled configuration LP | $$2^{O(r)}\,\mathrm{poly}(H)$$ or stated rank-quasipolynomial alternative | Coupled recipient configuration |
| [Item matroid union](problems/item-matroid-union/) | Factor $$4-3/r$$ versus integer OPT | $$2^{O(r)}\,\mathrm{poly}(H)$$ or stated rank-quasipolynomial alternative | Explicit-item model |
| [One-value exact-two allocation](problems/one-value-exact-two/) | Exact factor 2 | $$ (27/4)^c\,\mathrm{poly}(H)$$ | One exact budget |
| [Two-value exact-two allocation](problems/two-value-exact-two/) | Exact factor 2 | $$ (27/4)^{h_C}\,\mathrm{poly}(H)$$ | Compulsory two-value allocation |
| [Intrinsic values near two](problems/intrinsic-values-near-two/) | Factor $$2+\eta$$ | $$\Gamma((2+\eta)/\eta)^k\,\mathrm{poly}(H)$$ | Derived-corank condition |
| [Whole-ground allocation](problems/whole-ground-allocation/) | Exact factor 2 and fixed-$$R$$ tradeoffs | $$(2-1/A)^{q+o(q)}\,\mathrm{poly}(H)$$ | Original player matroid and exact budget |
| [Unrelated-value additive allocation](problems/unrelated-values-additive/) | Player-wise additive guarantee | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Player-dependent values |
| [Unrelated values with joint role](problems/unrelated-values-joint-role/) | Factor $$2R/(R-1)$$ | $$\Gamma(R)^q\,\mathrm{poly}(H)$$ | Joint role and setup budget |
| [Selected flow](problems/selected-flow/) | Rate $$(1-\varepsilon)\mathrm{OPT}$$ | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Selected commodities |
| [Robust scenario flow](problems/robust-scenario-flow/) | Same rate in every scenario | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Adaptive routing per scenario |
| [Shared-setup flow](problems/shared-setup-flow/) | Same rate with exact shared budget | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Setup and routing budget |

## Scheduling and profile tradeoffs

| Problem | Guarantee | Complexity / resource | Main scope |
|---|---|---|---|
| [Activated-machine scheduling](problems/activated-machine-scheduling/) | Makespan $$(1+\varepsilon)\mathrm{OPT}$$ | $$2^{O(q/\varepsilon)}\,\mathrm{poly}(H_\varepsilon)$$ | Activated machine basis |
| [Commitment scheduling](problems/commitment-scheduling/) | Stated bottleneck commitment bound | $$2^{O(k)}\,\mathrm{poly}(H)$$ | Commitment parameter |
| [Many-size scheduling](problems/many-size-scheduling/) | Additive makespan bound | $$\Gamma(1/\varepsilon)^k\,\mathrm{poly}(H)$$ | Compressed-rank profile condition |
| [Two-size scheduling](problems/two-size-scheduling/) | Exact 3/2 and 5/3 regimes | $$(27/4)^c\,\mathrm{poly}(H)$$ and $$2^{O(h)}\,\mathrm{poly}(H)$$ | Separate parameters |
| [Per-machine two-time scheduling](problems/two-time-scheduling/) | Exact 3/2 | $$ (50/27)^qE(q)\,\mathrm{poly}(H)$$ | Machine-specific two-time model |
| [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/) | 5/3, 11/7, approach to 3/2 | $$(k+1)^q\,\mathrm{poly}(H+k)$$ | Bucket parameter |
| [Six-profile scheduling](problems/six-profile-three-halves/) | Exact 3/2 | $$6^q\,\mathrm{poly}(H)$$ | Arbitrary profile endpoint |

## Dynamic graph and matching records

| Problem | Guarantee | Complexity / resource | Main scope |
|---|---|---|---|
| [Dynamic MSF](problems/dynamic-msf/) | Worst-case 2/3-style baseline | $$\exp(O(U^{2/3}h^{1/3}))$$ per update | Public pruning framework |
| [Strong Haxell matching](problems/strong-haxell-matching/) | Matching or checkable hitting-set certificate | $$O(|A|+|B|)+p\exp(O(U\log(2+s)/s))$$ | Strong-Haxell model |
| [Independent transversal](problems/independent-transversal/) | Certified transversal or obstruction | $$P\min\{\exp(O(q)),(q+1)^{O(\varepsilon^{-1}\log(2+r/\varepsilon))}\}\,\mathrm{poly}(b_\varepsilon+\log P)$$ | Partitioned graph model |

## Robustness and lower bounds

| Problem | Guarantee or boundary | Complexity / resource | Main scope |
|---|---|---|---|
| [Allocation and scheduling oracle barriers](problems/allocation-lower-bounds/) | Strictly below factor 2 and 3/2 are blocked in stated models | $$\binom{q}{q/2}-1$$ rank queries | Hidden-rank oracle regime |
| [Robust bounded certificates](problems/robust-bounded-certificates/) | Robust unit guarantee under bounded failure certificates | $$A^c\,\mathrm{poly}(H)$$ | Common basis and bounded certificate width |
| [Robust unrelated allocation](problems/robust-unrelated-allocation/) | Additive robust utility | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Common basis and common setup |
| [Robust width-two allocation](problems/robust-width-two-allocation/) | Exact robust positivity gate | $$\varphi^c\,\mathrm{poly}(H)$$ | Width-two minimal obstructions |
| [Two-scenario robust allocation hardness](problems/robust-two-scenario-hardness/) | W[1]-hard exact admission boundary | Corank $$c=k$$ | Explicit two-scenario model |

The complete proof maps and verification pointers remain in each problem record. The [complexity guide](docs/COMPLEXITY.md) defines the shared notation and separates oracle, readable-program, ETH, and implementation claims.
