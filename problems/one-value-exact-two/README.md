# One-value allocation with exact factor two

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns an original player-matroid basis and an integral allocation whose minimum selected utility is at least `OPT/2`. |
| **Objective and output** | Maximize the minimum number of common-value units received by each selected player, subject to one exact assignment-cost budget; output the basis and allocation. |
| **Time** | `(27/4)^c poly(H)`, where `c = q-r` is the player-matroid corank. |
| **Space** | Polynomial in the complete binary input and paid rational-oracle work. |
| **Parameters** | `q` is the nonloop player count; `r >= 1` is the player-matroid rank; `c=q-r`; `v>0` is the common unit value; `C` is the nonnegative assignment-cost budget; `H` includes binary data and paid rank, SFM, LP, and intersection primitives. |
| **Model and representation** | Integral recipient polymatroids and an actual original player-matroid basis; counts and costs are binary encoded. |
| **Lower-bound scope** | No new lower bound is claimed; the factor-two row is an upper bound in the stated oracle model. |
| **Boundary** | The `c=0` fixed-basis case is solvable exactly in polynomial oracle time; rank zero is handled separately. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). |
| **Source** | [Budgeted one-value theorem](../../sources/checkpoint-o/one_value_exact_budget_corank_two_allocation.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
