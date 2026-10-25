# Recipient-matroid configuration allocation

This is a supporting allocation record whose comparator is a coupled
configuration LP.

| Field | Curated statement |
|---|---|
| **Guarantee** | Factor `4 - 3/r` against the coupled configuration LP, with the stated positive-accuracy alternative under the same recipient-matroid scope. |
| **Objective and output** | Optimize the coupled configuration comparator while selecting a player basis and one service per player-resource pair; return the feasible integral allocation and selected basis. |
| **Time** | Exponential in the selected rank `r`, times polynomial work in the encoded input and the named rank/configuration primitives. The positive-accuracy alternative has a separate source-defined dependence. |
| **Space** | Polynomial binary workspace in the explicit configuration input and paid matroid state; no separate space exponent is claimed. |
| **Parameters** | `r` is the selected player-basis rank; `eta` is the positive accuracy in the alternative; `H` is the complete encoded input plus paid primitive work. |
| **Model and representation** | Arbitrary recipient matroids, one service per player-resource pair, a selected player basis, and the explicit coupled configuration comparator. |
| **Lower-bound scope** | No lower bound is claimed. The configuration comparator is not interchangeable with the arbitrary-polymatroid integer-optimum record. |
| **Review status** | Internal display and model review; proof and algorithm follow-up is tracked in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Recipient-matroid configuration source](../../sources/checkpoint-o/general_resource_prefix_additivity_four_candidate.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
