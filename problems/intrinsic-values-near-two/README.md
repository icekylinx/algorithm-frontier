# Intrinsic-value allocation near factor two

This is a supporting allocation record for common intrinsic values and a
derived-corank near-two guarantee.

| Field | Curated statement |
|---|---|
| **Guarantee** | Under derived corank `k`, returns value at least `OPT/(2/(1-epsilon))`; choosing `epsilon=eta/(2+eta)` gives factor `2+eta`. Exact factor two is retained only for the proved boundary cases. |
| **Objective and output** | Maximize common intrinsic value subject to the original player-matroid basis, recipient polymatroids by value type, and the exact budget extension when that extension is cited; return the integral allocation and selected basis. |
| **Time** | `Gamma(1/epsilon)^k poly(H)`, where `Gamma(R)=R^R/(R-1)^(R-1)`; the factor `2+eta` substitution uses `epsilon=eta/(2+eta)`. |
| **Space** | Polynomial binary workspace in the encoded input and paid oracle state; no separate space exponent is promoted. |
| **Parameters** | `k` is the derived corank; `0<epsilon<1` is rational accuracy (or `eta>0` with epsilon=eta/(2+eta)); `H` is complete binary input plus paid primitive work. |
| **Model and representation** | Original player-matroid basis, arbitrary integral recipient polymatroids by value type, common intrinsic values, and the exact-budget extension named by the source. |
| **Lower-bound scope** | No lower bound is claimed by this record. Exact factor-two boundary cases are scoped to the source's characterization. |
| **Review status** | Internal display and model review; proof and algorithm follow-up is tracked in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Near-two intrinsic-value source](../../sources/checkpoint-o/general_value_allocation_heavy_cover_near_two.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
