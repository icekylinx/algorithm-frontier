# Many-size workload scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns the source's additive makespan bound for arbitrary-size workloads, retaining both the multiplicative and smaller-job terms. |
| **Objective and output** | Minimize makespan under the mandatory workload totals, the large-unit profile, and the workload-polymatroid contract; output a legal integral schedule. |
| **Time** | The compressed-rank procedure uses an accuracy-dependent exponential factor in the residual rank `k`, multiplied by polynomial work in the complete encoded input. |
| **Space** | Polynomial binary workspace in the encoded instance and paid profile/rounding state; smaller-job counts are not expanded into unit slots. |
| **Parameters** | `D` is the source's profile parameter; `OPT` is the original integer optimum; `u` is the additive smaller-job term; `a` is the largest relevant unit; `lambda_k` is the residual threshold; `k` is the compressed rank; `epsilon` is the accuracy; `H` is complete encoded input plus paid primitive work. |
| **Model and representation** | Many smaller processing sizes, a large-unit profile, and a workload polymatroid with the source's completion and integral-rounding interfaces. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. The proof and algorithm follow-up is tracked in the [scheduling-profile review](../../reviews/backlog/scheduling-profile-records.md). |
| **Source** | [Many-small-sizes workload transfer](../../sources/checkpoint-o/many_small_sizes_workload_makespan_transfer.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
