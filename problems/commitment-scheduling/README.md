# Scheduling by bottleneck commitments

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns the source's bottleneck-commitment makespan bound, comparing the committed-machine profile with the residual rank-search guarantee. |
| **Objective and output** | Minimize makespan while committing a computable set of large-job machines, then output a complete integral schedule whose original job bases remain valid. |
| **Time** | Exponential in the selected residual rank `k`, times polynomial oracle and submodular-optimization work. The commitment profile is computed before trial makespans. |
| **Space** | Polynomial in the full binary input and the residual rank-search state. |
| **Parameters** | `q` is the machine count; `a` is the largest positive job size; `h` is the aggregate largest-job rank; `k` is the residual rank after commitment; `lambda_k` is the computable singleton workload threshold; `u` bounds smaller-job exposure. |
| **Model and representation** | Integral job polymatroids with binary ranks, value-oracle and submodular-minimization operations, a unit-box commitment matroid, and zero extension on committed coordinates. |
| **Lower-bound scope** | No lower bound is claimed. The record does not claim an unconditional improvement when the commitment term dominates. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [Bottleneck commitment source](../../sources/checkpoint-o/scheduling_bottleneck_commitment_rank_reduction.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
