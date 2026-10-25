# Recipient-matroid configuration allocation

This is a supporting allocation record whose comparator is a coupled
configuration LP.

| Field | Curated statement |
|---|---|
| **Guarantee** | Factor `4 - 3/r` against the coupled configuration LP, with the stated positive-accuracy alternative under the same recipient-matroid scope. |
| **Objective and output** | Optimize the coupled configuration comparator while selecting a player basis and one service per player-resource pair; return the feasible integral allocation and selected basis. |
| **Time** | `2^(O(r)) poly(H)` for factor `d=4-3/r`; the `d+eta` alternative takes `poly(H) min{2^(O(r)), (r+1)^(O((1+eta^-1) log(r+1)))}.` |
| **Space** | Polynomial binary workspace in the explicit configuration input and paid matroid state; no separate space exponent is claimed. |
| **Parameters** | `r` is the selected player-basis rank; `d=4-3/r`; `eta` is positive rational accuracy in the alternative; `H` is complete encoded input plus paid primitive work. |
| **Model and representation** | Arbitrary recipient matroids, one service per player-resource pair, a selected player basis, and the explicit coupled configuration comparator. |
| **Lower-bound scope** | No lower bound is claimed. The configuration comparator is not interchangeable with the arbitrary-polymatroid integer-optimum record. |
| **Review status** | Internal display and model review; proof and algorithm follow-up is tracked in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Recipient-matroid configuration source](../../sources/checkpoint-o/general_resource_prefix_additivity_four_candidate.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
