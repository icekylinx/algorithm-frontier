# Decremental strong forest and Gomory-Hu transfer

This is a conditional dynamic-graph transfer record, presented separately
from the fully dynamic APSP and spanner frontiers.

| Field | Curated statement |
|---|---|
| **Guarantee** | A strong decremental forest construction substituted into an exact deterministic Gomory-Hu reduction under the source's metric, forest, and fixed-parameter contracts. |
| **Objective and output** | Maintain the decremental strong-forest interface and use it to output the exact Gomory-Hu cut-tree representation named by the reduction. |
| **Time** | For a fixed-vertex, bounded-degree native graph, total decremental work is `O(n+m) + (m+1) exp(O(U^(6/7) h^(1/7)))`; the exact Gomory--Hu reduction is charged separately. This is total decremental work, not a worst-case per-deletion claim. |
| **Space** | Polynomial in the maintained graph, forest certificates, and reduction state; no independent space exponent is claimed. |
| **Parameters** | `n` is the vertex count; `m` is the lifetime edge inventory; `k` is the fixed reduction parameter; `U` is the master logarithmic scale; `h` is the iterated logarithmic scale used by the forest envelope. |
| **Model and representation** | Fixed native vertex set, bounded-degree decremental metric/forest model, fixed-`k` Gomory--Hu reduction, and the external backend assumptions in the source. |
| **Lower-bound scope** | No lower bound is claimed. The page does not claim an independently implemented near-linear Gomory-Hu data structure. |
| **Review status** | Conditional dynamic-graph research. The [dynamic-graph review](../../reviews/headline/dynamic-graph-frontier.md) tracks proof, algorithm, source, and finite-check boundaries; finite audits are not formal verification. |
| **Source** | [Strong forest and Gomory-Hu source](../../sources/checkpoint-o/six_sevenths_strong_forest_and_gomory_hu_checkpoint.md), the [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
