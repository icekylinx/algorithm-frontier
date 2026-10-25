# Six-profile exact three-halves scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a schedule with makespan at most one and one-half times the original integer optimum. |
| **Objective and output** | Minimize makespan for arbitrary unrelated processing profiles with mandatory original job totals and the exact assignment-budget accounting; output an integral schedule. |
| **Time** | Enumerates six target profiles per physical machine, giving an exponential factor in the machine count multiplied by polynomial work in the full encoded input. The base six is a construction bound, not an optimality claim. |
| **Space** | Polynomial binary workspace in the input, profile state, and integral-decomposition output. |
| **Parameters** | `q` is the number of physical machines; `H` includes all binary data and paid profile/oracle work; `T` is the target makespan used by the profile LP; mandatory job totals and the exact assignment budget remain part of the instance. |
| **Model and representation** | Arbitrary processing profiles, integral recipient polymatroids, mandatory original totals, and the cost-preserving rounding interface stated by the source. |
| **Lower-bound scope** | No lower bound is claimed; the six-profile base is not asserted to be optimal. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. The proof and algorithm follow-up is tracked in the [scheduling-profile review](../../reviews/backlog/scheduling-profile-records.md). |
| **Source** | [Six-profile three-halves construction](../../sources/checkpoint-q/arbitrary_processing_six_profile_three_halves.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
