# Per-machine two-time scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a schedule with makespan at most three-halves of the original integer optimum for the per-machine two-time model. |
| **Objective and output** | Minimize makespan when each machine has its own two positive processing times; output integral bases for both aggregate job polymatroids and decompose them back to original assignments. |
| **Time** | For fixed rational `d >= 2`, let `R_d=(d+1)/(d-1)`, `A_d=Gamma(R_d)`, `B_d=2-1/A_d`, and `E(q)=2^(O(q log log(q+2)/log(q+2)))`. The construction takes `B_d^q E(q) poly(H)` time. Exact endpoints are factor `3/2` at base `50/27`, factor `5/3` at base `7/4`, and factor `7/4` at base `2-(108/3125)^(1/3)`. |
| **Space** | Polynomial binary workspace in the input, profile state, and integral decomposition; binary job counts are not expanded. |
| **Parameters** | `q` is the number of machines; `d` is the fixed tradeoff parameter; `R_d`, `A_d`, `B_d`, and `E(q)` are as above; each machine has at most two positive times `0<u_p<a_p`; `H` is complete encoded input plus paid rank/SFM/LP/intersection/rounding work; original job totals and assignment budget `C` remain mandatory. |
| **Model and representation** | Per-machine two-time processing profiles with integral job polymatroids and the cost-preserving decomposition primitive. This is not a global two-value assumption. |
| **Lower-bound scope** | No lower bound is claimed. The three-halves endpoint is scoped to the per-machine model. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. The proof and algorithm follow-up is tracked in the [scheduling-profile review](../../reviews/backlog/scheduling-profile-records.md). |
| **Source** | [Per-machine two-time construction](../../sources/checkpoint-q/per_machine_two_time_costed_scheduling.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
