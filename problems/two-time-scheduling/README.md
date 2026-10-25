# Per-machine two-time scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a schedule with makespan at most three-halves of the original integer optimum for the per-machine two-time model. |
| **Objective and output** | Minimize makespan when each machine has its own two positive processing times; output integral bases for both aggregate job polymatroids and decompose them back to original assignments. |
| **Time** | The fixed-dimension construction uses the source's `(50/27)^q E(q)` profile factor, multiplied by polynomial work in the complete encoded input. The function `E(q)` and its rounding regime stay source-defined. |
| **Space** | Polynomial binary workspace in the input, profile state, and integral decomposition; binary job counts are not expanded. |
| **Parameters** | `q` is the number of machines; `E(q)` is the source's fixed-dimension profile factor; the two positive processing times are machine-specific; `H` is complete encoded input plus paid oracle and rounding work; original job totals and the assignment budget remain mandatory. |
| **Model and representation** | Per-machine two-time processing profiles with integral job polymatroids and the cost-preserving decomposition primitive. This is not a global two-value assumption. |
| **Lower-bound scope** | No lower bound is claimed. The three-halves endpoint is scoped to the per-machine model. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. The proof and algorithm follow-up is tracked in the [scheduling-profile review](../../reviews/backlog/scheduling-profile-records.md). |
| **Source** | [Per-machine two-time construction](../../sources/checkpoint-q/per_machine_two_time_costed_scheduling.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
