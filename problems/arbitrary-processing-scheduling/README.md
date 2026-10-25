# Arbitrary processing-time scheduling

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a legal schedule with makespan at most `(1 + epsilon)` times the original integer optimum, or detects infeasibility even without a load bound. |
| **Objective and output** | Minimize maximum load while preserving every original type total and the exact assignment-cost budget; output an integer schedule. |
| **Time** | With `delta = epsilon/2`, `K = floor(1/delta)`, `B = ceil((1-delta)/delta^2)`, and `C_epsilon = binom(B+K,K)`, the direct bound is `C_epsilon^q poly(H_epsilon)`; the source also proves `exp(3q(K+1)) poly(H_epsilon) = 2^(O(q/epsilon)) poly(H_epsilon)`. |
| **Space** | Polynomial in the complete binary input and rational accuracy encoding; neither machine slots nor job units are expanded. |
| **Parameters** | `q` is the physical-machine count; `epsilon` is rational accuracy; `H_epsilon` includes its full encoding; `n_j=f_j(P)` are mandatory type totals; `C` is the exact assignment-cost budget; `ell_pj` and `a_pj` are arbitrary nonnegative rational processing times and assignment costs. |
| **Model and representation** | Arbitrary nonnegative rational processing times, integral recipient polymatroids, mandatory original bases, eligibility masks, and one exact assignment-cost budget. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [Arbitrary-processing profile source](../../sources/checkpoint-q/arbitrary_processing_profile_approximation_scheme.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
