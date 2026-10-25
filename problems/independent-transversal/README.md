# Independent transversal with a certifying obstruction

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns an independent transversal, or a domination/constellation certificate satisfying the stated partition-relative claw bound. |
| **Objective and output** | Find one vertex in each class with no selected edge, or return a domination/constellation obstruction. |
| **Time** | `P * min{exp(O(q)), (q+1)^(O(epsilon^-1 log(2+r/epsilon)))} * poly(b_epsilon + log P)`. |
| **Space** | Polynomial in the explicit graph, partition, and streamed blocker state. |
| **Parameters** | `q` is the number of nonempty vertex classes; `r >= 2` is the partition-relative claw parameter; `epsilon` is rational slack; `P = |V| + |E| + q + 2`; `b_epsilon` is the encoding length of `epsilon`. |
| **Model and representation** | A finite loopless graph whose vertices are partitioned into `q` classes. The obstruction contains a nonempty class set, a totally dominating set, and an induced constellation. |
| **Lower-bound scope** | No lower bound is claimed; the obstruction is a certifying output boundary. |
| **Scope** | A certificate does not by itself prove that no independent transversal exists; the guarantee is unconditional for the stated input model. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [matching-certificate review](../../reviews/backlog/matching-certificate-records.md). |
| **Source** | [Current-blocker growth theorem](../../sources/checkpoint-o/independent_transversal_current_blocker_growth.md) and its verification paths. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
