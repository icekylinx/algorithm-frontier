# Many-size workload scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | For every rational `0 < eta <= 1`, returns `C_max <= (2 - 1/(3+eta)) OPT + u`; combining with the polynomial two-approximation gives `min{2 OPT, (2 - 1/(3+eta)) OPT + u}`. |
| **Objective and output** | Minimize makespan under the mandatory workload totals, the large-unit profile, and the workload-polymatroid contract; output a legal integral schedule. |
| **Time** | `poly(H) * min{2^(O(h)), (h+1)^(O((1+eta^-1) log(h+1)))}`, where `h` is the aggregate rank of the largest-size job class. |
| **Space** | Polynomial binary workspace in the encoded instance and paid profile/rounding state; smaller-job counts are not expanded into unit slots. |
| **Parameters** | `q` is the machine count; `h` is the aggregate largest-job rank; `a` is the largest positive job size; `u = max{p_j : p_j < a, f_j(P)>0}` (or `0` if none); `eta` is rational accuracy; `OPT` is the integer optimum; `H` includes all binary input and paid rank/SFM/LP/decomposition/rounding work. |
| **Model and representation** | Many smaller processing sizes, a large-unit profile, and a workload polymatroid with the source's completion and integral-rounding interfaces. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. The proof and algorithm follow-up is tracked in the [scheduling-profile review](../../reviews/backlog/scheduling-profile-records.md). |
| **Source** | [Many-small-sizes workload transfer](../../sources/checkpoint-o/many_small_sizes_workload_makespan_transfer.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
