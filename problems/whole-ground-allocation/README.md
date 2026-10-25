# Whole-ground allocation and scheduling transfers

| Field | Curated statement |
|---|---|
| **Guarantee** | Whole-ground transfers include exact factor two for one-value and compulsory two-value allocation, exact factor three-halves for two-size scheduling, and the fixed-`R` intrinsic-value tradeoff. |
| **Objective and output** | Apply the block-cover conversion to preserve the selected-set/comparator contract of each source theorem. |
| **Time** | For `A>1`, `T_A(q,H)=(2-1/A)^q 2^(O(q log log(q+2)/log(q+2))) poly(H)`. The one-value and two-value rows use `A=27/4`, giving base `50/27`. |
| **Space** | Polynomial in the explicit ground, streamed omission cover, and paid oracle state. |
| **Parameters** | `q` is the explicit nonloop ground; `H` includes all binary data and paid primitive descriptions; `A` is the local corank-gap base; `R>1` and `Gamma(R)` govern the arbitrary intrinsic-value row. |
| **Model and representation** | The row-specific allocation, scheduling, and flow models are retained separately; numerical counts are binary encoded. |
| **Lower-bound scope** | No joint lower bound is claimed for the transfer table. |
| **Scope** | The transfer preserves each row's own comparator and constraints; it does not merge allocation, scheduling, and flow claims into one theorem. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. |
| **Source** | [Global exponential transfer manuscript](../../sources/checkpoint-o/global_exponential_allocation_flow_transfers.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
