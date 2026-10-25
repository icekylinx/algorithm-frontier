# Arbitrary processing-time scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a legal schedule with makespan at most `(1 + epsilon)` times the original integer optimum, or detects infeasibility even without a load bound. |
| **Objective and output** | Minimize maximum load while preserving every original type total and the exact assignment-cost budget; output an integer schedule. |
| **Time** | Exponential in the physical machine count divided by the accuracy, times polynomial work in the full binary input and accuracy encoding. |
| **Space** | Polynomial in the complete binary input and rational accuracy encoding; neither machine slots nor job units are expanded. |
| **Parameters** | `q` is the physical machine count; `epsilon` is rational accuracy; `H_epsilon` includes its full encoding; `n_j` are mandatory type totals; `C` is the exact assignment-cost budget. |
| **Model and representation** | Arbitrary nonnegative rational processing times, integral recipient polymatroids, mandatory original bases, eligibility masks, and one exact assignment-cost budget. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [Arbitrary-processing profile source](../../sources/checkpoint-q/arbitrary_processing_profile_approximation_scheme.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
