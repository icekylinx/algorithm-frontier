# Allocation with arbitrary recipient polymatroids

This is a supporting allocation record for common intrinsic values and an
arbitrary selected player basis.

| Field | Curated statement |
|---|---|
| **Guarantee** | With `d=4-3/r`, returns value at least `OPT/d`; for positive rational `eta`, the alternative returns at least `OPT/(d+eta)` under its stated assumptions. |
| **Objective and output** | Maximize common intrinsic value subject to recipient polymatroid constraints, a selected player-matroid basis, binary counts, and exact availability; return the integral allocation and its basis. |
| **Time** | `2^(O(r)) poly(H)` for factor `d`; the `d+eta` alternative takes `poly(H) min{2^(O(r)), (r+1)^(O((1+eta^-1) log(r+1)))}.` |
| **Space** | Polynomial binary workspace in the encoded input and paid oracle state; no independent space exponent is promoted. |
| **Parameters** | `r` is the selected player-basis rank; `q` is the player count; `d=4-3/r`; `eta` is positive rational accuracy in the alternative; `H` is complete binary input plus paid primitive work. |
| **Model and representation** | Common intrinsic values, arbitrary integral recipient polymatroids, an arbitrary selected player-matroid basis, binary multiplicities, exact availability, and the optional lambda-availability oracle named by the source. |
| **Lower-bound scope** | No lower bound is claimed by this record. Oracle barriers are kept in the separate allocation lower-bound record. |
| **Review status** | Internal display and model review; proof and algorithm follow-up remains in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Recipient-polymatroid prefix transfer](../../sources/checkpoint-o/general_recipient_polymatroid_prefix_four_transfer.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
