# Two-scenario robust allocation hardness

| Field | Curated statement |
|---|---|
| **Guarantee** | Exact positive service for a common player basis is W[1]-hard when parameterized by the corank `c`, even with two scenarios and free Boolean recipient resources. |
| **Objective and output** | Decide whether one common basis can receive one unit in both scenarios; the reduction distinguishes robust optimum `1` from `0`. |
| **Time** | The reduction is polynomial in the explicit instance and parameter-preserving with `c=k`; an `F(c) poly(H)` finite-factor algorithm would imply `FPT=W[1]`. |
| **Complexity consequence** | Under `FPT != W[1]`, no algorithm with running time `F(c) poly(H)` can guarantee a finite multiplicative approximation for the exact-admission problem in this model. |
| **Parameters** | `q` is the player count; `r=q-k` is the selected basis rank; `c=k` is the corank; the two scenarios use budgets `C_1=A-T` and `C_2=rL-A+T`, with `A=sum_i a_i` and `L=A+1`. |
| **Space** | Polynomial-size explicit reduction; no algorithmic workspace bound is claimed for the hardness statement. |
| **Lower-bound scope** | The W[1]-hardness is conditional on the named parameterization and does not imply a whole-ground exponential lower bound. |
| **Model and representation** | Two explicit scenarios, a uniform player matroid, free Boolean recipient ranks, unit values, zero setup fees, and scenario-adaptive allocations. |
| **Scope** | The reduction distinguishes robust optimum `1` from `0`; it does not claim a whole-ground exponential lower bound or hardness for relaxed budgets. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. |
| **Source** | [Two-scenario unit-budget obstruction](../../sources/checkpoint-q/two_scenario_unit_budget_corank_obstruction.md). |

**Finite reduction check.** [`tools/verify_finite_reductions.py`](../../tools/verify_finite_reductions.py) exhaustively checks the budget equivalence on small integer instances; it does not prove the hardness theorem.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
