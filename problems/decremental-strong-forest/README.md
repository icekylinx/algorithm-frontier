# Decremental strong forest and Gomory-Hu transfer

This is a conditional dynamic-graph transfer record, presented separately
from the fully dynamic APSP and spanner frontiers.

| Field | Result |
|---|---|
| **Guarantee** | A strong decremental forest construction substituted into an exact deterministic Gomory-Hu reduction under the source's metric, forest, and fixed-parameter contracts. |
| **Objective and output** | Maintain the decremental strong-forest interface and use it to output the exact Gomory-Hu cut-tree representation named by the reduction. |
| **Time** | Both the native decremental forest and the exact Gomory–Hu application have total work $O(n+m)+(m+1)E_{6/7}$ under their stated interfaces, where $E_{6/7}=\exp(O(U^{6/7}h^{1/7}))$. |
| **Space** | Polynomial in the maintained graph, forest certificates, and reduction state; no independent space exponent is claimed. |
| **Parameters** | $n$ is the vertex count; $m$ is the lifetime edge inventory; $k$ is the fixed reduction parameter; $U$ is the master logarithmic scale; $h$ is the iterated logarithmic scale used by the forest envelope. |
| **Model and representation** | The forest uses a fixed bounded-degree native graph. The Gomory–Hu application accepts arbitrary-degree undirected multigraphs with positive polynomial-range integer nonloop capacities and uses the fixed-parameter reduction and named forest/flow interfaces. |
| **Lower-bound scope** | No lower bound is claimed. The page does not claim an independently implemented near-linear Gomory-Hu data structure. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md). |

## Exact cut-tree output

The returned tree uses the original vertices. For every pair, the minimum edge weight along its tree path equals the exact minimum-cut value. Disconnected component trees are joined by zero-weight edges; graph loops do not affect cuts.

The reduction charges actual-size degree expansion, finite-precision multiplicative weights, the skeleton, fixed-$k$ guide families, contractions, and all flow calls. Their $5/6$ and $4/5$ overhead scales are absorbed by the stated $6/7$ factor. This is an application of the complete strong-forest contract, including occurrence and retirement accounting.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
