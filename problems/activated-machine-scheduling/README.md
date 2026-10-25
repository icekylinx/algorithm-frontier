# Activated-machine scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a legal schedule with makespan at most `(1 + epsilon)` times the original integer optimum, or detects global infeasibility. |
| **Objective and output** | Minimize maximum machine load while keeping every original job total mandatory and preserving the exact assignment/setup budget. Output is an integer assignment of all original job units. |
| **Time** | Exponential in the number of physical machines divided by the supplied accuracy, times polynomial work in the full binary input and accuracy encoding. |
| **Space** | Polynomial in the full binary input, including the complete rational accuracy encoding. No job identity or binary count is expanded into unit slots. |
| **Parameters** | `q` is the machine count; `epsilon` is rational accuracy; `H_epsilon` includes all input bits, rank interfaces, and the full encoding of epsilon; `n_j` are mandatory original type totals. |
| **Model and representation** | Machine-dependent processing times, integral job polymatroids, an activated actual machine basis, and the initialization/assignment-cost contract in the source. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [Activated-machine scheduling source](../../sources/checkpoint-q/activated_machine_profile_scheduling.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
