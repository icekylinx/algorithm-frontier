# Arbitrary-value allocation scheme

This is a supporting approximation scheme for player-dependent values with an
exact shared setup and assignment budget.

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns value at least `(1 - epsilon)` times the integer optimum for every rational accuracy `epsilon` between zero and one. |
| **Objective and output** | Maximize player-dependent value while respecting integral recipient-polymatroid constraints and the exact shared setup/assignment budget; output an integral allocation and the optional actual player basis. |
| **Time** | The source gives a binomial factor in the player count and basis size, multiplied by an exponential factor in the basis size divided by accuracy and polynomial work in the full encoded input. |
| **Space** | Polynomial in `H_epsilon`, including the full binary encoding of the rational accuracy; no unit expansion of counts or accuracy is used. |
| **Parameters** | `q` is the player count; `r` is the optional basis size; `epsilon` is rational accuracy; `C` is the exact shared setup/assignment budget; `H_epsilon` includes all input bits and the encoding of `epsilon`; `K` bounds the retained recipient profile. |
| **Model and representation** | Arbitrary player-dependent nonnegative rational values, integral recipient polymatroids, binary multiplicities, optional actual player bases, setup fees, assignment costs, and one exact budget. |
| **Lower-bound scope** | No lower bound is claimed. The result is an approximation upper bound under the stated polymatroid and budget interfaces. |
| **Review status** | Internal display and model review; proof and algorithm follow-up remains in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Arbitrary-value profile scheme](../../sources/checkpoint-q/arbitrary_value_profile_allocation_approximation_scheme.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
