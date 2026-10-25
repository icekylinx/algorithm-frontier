# Algorithm index

The table below is the algorithm-facing index. Each row links to a problem
record whose README states the exact model, guarantee, complexity, and proof
status. Parameterizations with different assumptions remain separate.

| Problem | Guarantee | Complexity / resource | Main scope |
|---|---|---|---|
| [General-graph maximum matching](problems/general-matching/) | Exact maximum matching | $$O(n+m)+(m_s+1)\exp(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}))$$ | Conditional arbitrary-graph construction |
| [Degree-constrained subgraphs](problems/degree-constrained-subgraphs/) | Exact degree-constrained output | Matching-backend envelope | f-factor, interval, and cardinality reductions |
| [Selected flow](problems/selected-flow/) | Rate $$(1-\varepsilon)\mathrm{OPT}$$ | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Exact capacities and selected commodities |
| [Robust scenario flow](problems/robust-scenario-flow/) | Same rate in every scenario | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Adaptive routing per scenario |
| [Shared-setup flow](problems/shared-setup-flow/) | Same rate with exact shared budget | $$\Gamma(1/\varepsilon)^c\,\mathrm{poly}(H)$$ | Setup and routing budget |
| [Static/threshold min-cost flow](problems/min-cost-flow/) | Exact flow witness | Conditional raw-backend $$E^4$$ term | Static and fixed-threshold clients |
| [One-value allocation](problems/one-value-exact-two/) | Exact factor 2 | $$(27/4)^c\,\mathrm{poly}(H)$$ | One exact budget |
| [Recipient polymatroids](problems/recipient-polymatroid/) | Factor $$4-3/r$$ | $$2^{O(r)}\,\mathrm{poly}(H)$$ | Versus integer OPT |
| [Arbitrary-value allocation](problems/arbitrary-value-allocation-scheme/) | Value $$(1-\varepsilon)\mathrm{OPT}$$ | $$\binom{q}{r}\exp(O(r/\varepsilon))\,\mathrm{poly}(H_\varepsilon)$$ | Optional actual basis |
| [Arbitrary processing scheduling](problems/arbitrary-processing-scheduling/) | Makespan $$(1+\varepsilon)\mathrm{OPT}$$ | $$2^{O(q/\varepsilon)}\,\mathrm{poly}(H_\varepsilon)$$ | Mandatory jobs |
| [Two-size scheduling](problems/two-size-scheduling/) | Exact 3/2 and 5/3 regimes | $$(27/4)^c\,\mathrm{poly}(H)$$ and $$2^{O(h)}\,\mathrm{poly}(H)$$ | Different parameters, both retained |
| [Six-profile scheduling](problems/six-profile-three-halves/) | Exact 3/2 | $$6^q\,\mathrm{poly}(H)$$ | Arbitrary profile endpoint |
| [Processing-bucket tradeoff](problems/processing-bucket-tradeoff/) | 5/3, 11/7, approach to 3/2 | $$(k+1)^q\,\mathrm{poly}(H+k)$$ | Bucket parameter k |
| [Dynamic APSP](problems/apsp-frontier/) | Update/stretch Pareto frontier | Multiple exponential points | Fully dynamic graph |
| [Dynamic spanners](problems/dynamic-spanners/) | 4/5 and 5/6 recourse scopes | Stretch/work $$\exp(O(U^{4/5}h^{1/5}))$$ and $$\exp(O(U^{5/6}h^{1/6}))$$; low-recourse output $$ (n+D)\exp(O(U^{5/6}h^{1/6}))$$ | Different recourse definitions |
| [Incremental SSSP](problems/incremental-sssp/) | Distances and simple paths | $$O(n+m)+(n+m)\exp(O(U^{4/5}h^{1/5}+\sqrt{U(h+\log(1/\varepsilon))}))$$ | Directed incremental graph |
| [Incremental SCC](problems/incremental-scc/) | Exact component labels | $$ (n+m)E(N)^{O(1)}\,\mathrm{poly}(U)$$, where $$E(N)=\exp(O(U^{4/5}(\log U)^{1/5}))$$ | No path/topological witness claim |
| [Strong forest / Gomory-Hu](problems/decremental-strong-forest/) | Decremental transfer | $$O(n+m)+(m+1)E_6(n+m)$$ | Conditional reduction |
| [Dynamic MSF](problems/dynamic-msf/) | Worst-case 2/3-style baseline | $$\exp(O(U^{2/3}h^{1/3}))$$ per update | Public pruning framework |
| [Strong Haxell matching](problems/strong-haxell-matching/) | Matching or checkable hitting-set certificate | $$O(|A|+|B|)+p\exp(O(U\log(2+s)/s))$$ | Hypergraph model |
| [Independent transversal](problems/independent-transversal/) | Certified transversal or obstruction | $$P\min\{\exp(O(q)),(q+1)^{O(\varepsilon^{-1}\log(2+r/\varepsilon))}\}\,\mathrm{poly}(b_\varepsilon+\log P)$$ | Partitioned graph model |
| [Faster Subset Sum](problems/subset-sum-fast-deterministic/) | Exact witness | $$C+\mathrm{poly}(n,L)2^{En}$$, $$E<0.4964618056$$ | Signed binary integers |
| [Low-space Subset Sum](problems/subset-sum-low-space-deterministic/) | Exact witness | Time $$\mathrm{poly}(n,L)2^{n/2}$$; space $$\mathrm{poly}(n,L)2^{E_Sn}$$ | Separate low-space algorithm |

Lower bounds and negative results are grouped in [allocation-lower-bounds](problems/allocation-lower-bounds/), [robust-two-scenario-hardness](problems/robust-two-scenario-hardness/), and the negative sections of the relevant problem records.

The complete proof maps and verification pointers are intentionally separate
from this index so that the algorithmic results remain easy to scan.
