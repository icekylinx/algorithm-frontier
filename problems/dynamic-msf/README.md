# Dynamic minimum spanning forest baseline

| Field | Curated statement |
|---|---|
| **Guarantee** | Maintains an exact minimum spanning forest in a fully dynamic weighted graph under the stated deterministic reduction. |
| **Objective and output** | Preserve the minimum spanning forest after each settled update; the source charges the update certificate and the forest reconstruction separately. |
| **Update time** | Worst-case work per update is exponential in the two-thirds power of the logarithmic master parameter times the one-third power of its iterated logarithm. This is a derived public baseline, not a claim that one source states the complete composition alone. |
| **Space** | Actual weighted-edge inventory, hierarchy certificates, retired records, and pruning state; no master-cap padding is materialized. |
| **Parameters** | `n` is the vertex count; `m` is the current edge count; `N` bounds lifetime edge records; `U` is log of `N` plus a constant; `h` is log of `U` plus a constant. |
| **Model and representation** | Deterministic fully dynamic weighted multigraph, with the public decomposition, pruning, contraction, and child-forest certificate interfaces named by the source. |
| **Lower-bound scope** | No lower bound is claimed. The displayed point is a baseline and should not be advertised as an improvement over the cited public reduction. |
| **Review status** | Conditional research record; source and backend boundaries remain explicit in the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). Finite audits are not formal verification. |
| **Source** | [Public two-thirds MSF baseline](../../sources/checkpoint-o/dynamic_msf_public_two_thirds_baseline.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
