# Compulsory two-value allocation with exact factor two

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns an integral allocation giving every compulsory player utility at least `OPT/2`, while preserving the assignment budget exactly. |
| **Objective and output** | Maximize the minimum utility when every player is compulsory and unit values are `u` or `a` with `0<u<a`; output all recipient count vectors. |
| **Time** | `(27/4)^(h_C) poly(H)`, where `h_C` is the maximum number of distinct large-unit recipients affordable under the exact budget. |
| **Space** | Polynomial in the complete encoded instance and paid matroid/intersection state. |
| **Parameters** | `q` is the compulsory-player count; `h_C` is the budget-aware large-recipient rank; `0<u<a` are the two intrinsic values; `C` is the assignment-cost budget; `H` includes all binary data and paid oracle work. |
| **Model and representation** | Integral recipient polymatroids with two value classes, compulsory players, and binary counts; one exact budget is preserved. |
| **Lower-bound scope** | The corresponding strict-below-two recipient-oracle barrier is scoped to the named oracle model; no explicit-input hardness claim is added here. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. |
| **Source** | [Two-value exact-two theorem](../../sources/checkpoint-o/two_value_arbitrary_cost_exact_two_allocation.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
