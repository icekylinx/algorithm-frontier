# Incremental strongly connected components

| Field | Curated statement |
|---|---|
| **Guarantee** | Exact strongly connected component labels after every settled directed-edge insertion. |
| **Objective and output** | Maintain one explicit component label per original vertex. The record does not include a topological ordering of the quotient or a path witness. |
| **Update time** | Total work is linear in the vertex and inserted-edge inventory, multiplied by a fixed power of the raw backend factor and a polynomial in the logarithmic master parameter. The candidate backend has the four-fifths hierarchy exponent shown in the source. |
| **Space** | Polynomial in the maintained graph, label inventory, and raw-backend state; the client does not expand binary caps into unit arrays. |
| **Parameters** | `n` is the original vertex count; `m` bounds inserted edge records; `N` is the power-of-two master cap; `U` is its logarithmic scale. Parallel edges and self-loops are allowed. |
| **Model and representation** | Conditional incremental directed graph client using the named raw minimum-ratio-cycle interface, explicit endpoint retargeting, edge retirement, and exact component-label updates. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Conditional research record. The [backlog review](../../reviews/backlog/legacy-result-cards.md) tracks the next proof, algorithm, and source audit; the [review registry](../../reviews/README.md) records its status. |
| **Source** | [Log-barrier incremental SCC source](../../sources/checkpoint-o/log_barrier_incremental_scc.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
