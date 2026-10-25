# Explicit-item matroid-union allocation

This is a supporting allocation record for explicit items and a matroid-union
resource construction.

| Field | Curated statement |
|---|---|
| **Guarantee** | Factor `4 - 3/r` against integer optimum in the explicit-item model, with the stated positive-accuracy rank-quasipolynomial alternative and configuration-LP addendum. |
| **Objective and output** | Maximize intrinsic item value while selecting a feasible player-matroid basis and matroid-union resource set; return the original-item allocation and basis. |
| **Time** | Exponential in the selected rank `r`, times polynomial work in the encoded input and named matroid primitives. The rank-quasipolynomial alternative has its own source-defined dependence. |
| **Space** | Polynomial binary workspace in the explicit input and paid matroid state; no separate space exponent is claimed. |
| **Parameters** | `r` is the selected player-basis rank; `eta` is the positive accuracy in the alternative guarantee; `H` is the complete encoded input plus paid primitive work. |
| **Model and representation** | Explicit items with arbitrary intrinsic values, a player matroid, the matroid-union resource construction, and the source's original-basis recovery interface. |
| **Lower-bound scope** | No lower bound is claimed. The configuration-LP addendum is a separate comparator and is not an explicit-input hardness statement. |
| **Review status** | Internal display and model review; proof and algorithm follow-up is tracked in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Matroid-union allocation source](../../sources/checkpoint-o/matroid_union_fat_resource_allocation.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
