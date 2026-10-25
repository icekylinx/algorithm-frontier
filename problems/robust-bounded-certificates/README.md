# Robust allocation with bounded failure certificates

This is a general robust-unit record under a bounded aggregate minimal-certificate promise.

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns at least the ceiling of `K_star / d` robust units while preserving every scenario budget exactly, under the bounded certificate-width condition. |
| **Objective and output** | Maximize the common robust unit count across explicit scenarios; output one common actual player basis and a scenario-specific integral allocation, or a width-violation certificate when the promise fails. |
| **Time** | Exponential in the forced-omission count with base `A`, times polynomial work in the complete scenario description and rank/budget primitives. Whole-ground conversion has a separate `(2 - 1/A)` base. |
| **Space** | Polynomial in the explicit scenario input, certificate width, and branching state; binary budgets and supplies are not expanded into unit arrays. |
| **Parameters** | `q` is the player count; `r` is the common basis rank; `c = q - r` is the omission count; `d` is the target unit count; `w` bounds minimal certificate width; `K_star` is the robust target; `A` is the source's width-dependent base; `Omega` is the scenario list. |
| **Model and representation** | One common actual player basis, scenario-specific integral recipient polymatroids, exact nonnegative assignment budgets, adaptive allocations, and explicit minimal unit-failure certificates. |
| **Lower-bound scope** | The source retains a whole-ground oracle barrier and a width-violation outcome. It does not claim an explicit-input lower bound for every robust allocation model. |
| **Review status** | Internal display and model review; proof and algorithm follow-up remains in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Bounded-certificate robust tradeoffs](../../sources/checkpoint-q/robust_unit_bounded_certificate_exact_tradeoffs.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
