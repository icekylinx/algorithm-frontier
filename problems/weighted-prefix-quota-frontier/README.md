# Prefix, laminar and sparse quotas

Exact algorithms for structured quota systems and deterministic reductions that retain original items.

| Field | Result |
|---|---|
| **Objective and output** | Decide mixed numeric quotas and recover an exact signed-scalar optimum; kernel rows instead return a smaller original ground with a replacement guarantee. |
| **Time** | One order $2^{O(B)}$; two orders $2^{O(B\log(B+2))}$; $p$ shared weight families $2^{O(pB\log(p+2))}$; common-weight laminar quotas $2^{O(B^2)}$, all times $\operatorname{poly}(H)$. Sparse and support-sensitive refinements appear below. |
| **Space** | Uniform polynomial binary workspace. Enumerated profiles and universal colorings are streamed. |
| **Parameters** | $B$ bounds finite targets; $B_0\le B$ is the distinguished root cap; $\Delta$ bounds positive nonroot incidences; $C$ counts distinct support patterns; $H$ is the full encoded input with paid oracle work. Kernel parameters are solution size $k$ and the specified frequency or additional matroid count. |
| **Model and representation** | One global normalized monotone integral polymatroid with exact rank access. Prefix rows share the stated coordinate orders and weight vectors. Sparse rows require every zero-root coordinate to be zero in every numeric row. Mandatory bases retain their original total; zero-weight coordinates retain their actual scalar costs. |
| **Lower-bound scope** | Oracle-query and readable-program ETH bounds are stated separately. Frequency-one disjoint weighted equalities already require $2^{\Omega(B\log(B+2))}$ queries. Row-dependent weights have a separate W[2] boundary. The laminar upper and lower exponents are not claimed to coincide. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Formal theorems and quadratic laminar proof](proof.md), [complete companion and reference index](sources.md). |

## Exact algorithm bounds

All rows include $\operatorname{poly}(H)$.

| Quota geometry | Time |
|---|---|
| One common order | $2^{O(B)}$ |
| Two common orders | $2^{O(B\log(B+2))}$ |
| One order, $C$ actual supports | $2^{O(\sqrt{B\min\{C,B\}})}$ |
| Two orders, $C$ actual supports | $2^{O(\min\{\sqrt{BC},B\log(2+\min\{C/B,B\})\})}$ |
| $p$ shared weight families | $2^{O(pB\log(p+2))}$ |
| Common-weight laminar family with root cap $B$ | $2^{4B^2+O(B\log(B+1))}$ |
| Root cap $B_0$, maximum target $B$, frequency $\Delta$ | $2^{O((\Delta+1)B_0\log((\Delta+1)B_0(B+2)+2))}$; in particular $2^{O(\Delta B\log(\Delta B+2))}$ for $\Delta\ge1$ |

## Deterministic ground reductions

These constructions are polynomial in the explicit input. The retained original resource oracle and weights remain part of the output model.

| Resource and constraints | Retained size |
|---|---|
| One item matroid and frequency-$\delta$ sparse packing | $k\delta![k(\delta(k-1)+1)]^\delta=O_\delta(k^{2\delta+1})$ |
| The same packing with distinct item supports | The leading multiplicity factor $k$ is unnecessary: $O_\delta(k^{2\delta})$ |
| One arbitrary and $d$ additional coverable matroids | $k\,d![k(1+\sum_i g_i)]^d$, for the stated closure-class bounds $g_i$ |
| One arbitrary and $d$ explicitly represented transversal matroids | $O_d(k^{2d+1})$ |
| Graph matching with one matroid on edges | $O(k^4)$ for simple graphs; $O(k^5)$ with parallel edges |
| Sparse numeric quotas and valuated completion | Parameter-bounded positive capacity with all original zero-coordinate completion and signed costs retained |

Each reduction preserves replacements against feasible contexts in the original instance. A small retained ground is not a parameter-only bit encoding of an arbitrary oracle.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
