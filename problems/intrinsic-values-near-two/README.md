# Intrinsic-value allocation near factor two

This is a supporting allocation record for common intrinsic values and a
derived-corank near-two guarantee.

| Field | Curated statement |
|---|---|
| **Guarantee** | Factor `2 + eta` under the stated derived-corank condition, with exact factor two retained only for the proved boundary cases. |
| **Objective and output** | Maximize common intrinsic value subject to the original player-matroid basis, recipient polymatroids by value type, and the exact budget extension when that extension is cited; return the integral allocation and selected basis. |
| **Time** | The source uses the inverse-accuracy base raised to the derived corank `k`, multiplied by polynomial work in the full encoded input. |
| **Space** | Polynomial binary workspace in the encoded input and paid oracle state; no separate space exponent is promoted. |
| **Parameters** | `k` is the derived corank; `eta` is the additive accuracy in the near-two guarantee; `H` is the complete binary input plus paid primitive work. |
| **Model and representation** | Original player-matroid basis, arbitrary integral recipient polymatroids by value type, common intrinsic values, and the exact-budget extension named by the source. |
| **Lower-bound scope** | No lower bound is claimed by this record. Exact factor-two boundary cases are scoped to the source's characterization. |
| **Review status** | Internal display and model review; proof and algorithm follow-up is tracked in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Near-two intrinsic-value source](../../sources/checkpoint-o/general_value_allocation_heavy_cover_near_two.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
