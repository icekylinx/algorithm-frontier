# Unrelated values with a joint role and setup budget

| Field | Curated statement |
|---|---|
| **Guarantee** | For fixed rational `R>1`, returns a legal integral allocation with minimum utility at least `(1-1/R) OPT / 2`; choosing `R=(2+eta)/eta` gives factor `2+eta`. |
| **Objective and output** | Maximize minimum player-dependent utility with optional player selection, one exact assignment/setup budget, and the joint-role selector; output selected players and allocations. |
| **Time** | `B(R)^q * 2^(O(q log log(q+2)/log(q+2))) * poly(H)`, where `B(R)=2-1/Gamma(R)` and `Gamma(R)=R^R/(R-1)^(R-1)`. |
| **Space** | Polynomial in the complete binary input and paid joint-role, rank, LP, and rounding state. |
| **Parameters** | `q` is the nonloop player ground; `R>1` is the rational accuracy parameter; `Gamma(R)` and `B(R)` are as above; `H` includes values, costs, setup fees, ranks, and selector descriptions. |
| **Model and representation** | Player-dependent rational values, integral recipient polymatroids, optional basis selection, one exact budget, and the paid joint-role selector. |
| **Lower-bound scope** | No lower bound is claimed; the factor is an upper bound under the exact selector interface. |
| **Scope** | The factor is whole-ground and does not assume a heavy-support or price-diversity promise. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). |
| **Source** | [Joint-role near-two theorem](../../sources/checkpoint-p/unrelated_values_joint_role_near_two_allocation.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
