# Robust unrelated allocation with common setup

This is a supporting robust-allocation record with a common selected basis and
scenario-adaptive assignments.

| Field | Curated statement |
|---|---|
| **Guarantee** | Robust additive utility at least the source's nonnegative version of `(1 - epsilon) F OPT - u`, with every scenario budget exact. |
| **Objective and output** | Maximize common robust utility across explicit scenarios; keep one common actual player basis, allow scenario-adaptive integral assignments, and return the basis plus each scenario allocation. |
| **Time** | The inverse-accuracy base is raised to the corank `c`, multiplied by polynomial work in the complete scenario input and paid primitives. |
| **Space** | Polynomial binary workspace in the explicit scenarios, common-basis state, setup vector, and scenario allocations; no separate space exponent is claimed. |
| **Parameters** | `c` is the corank/omission parameter in the source; `epsilon` is rational accuracy; `F` is the source's baseline factor; `u` is the additive term; `H` includes all scenario data and paid primitive work; `Omega` is the explicit scenario list. |
| **Model and representation** | Common actual player basis across scenarios, scenario-adaptive integral assignments, unrelated values, a common setup vector, recipient polymatroids, and exact nonnegative budgets. |
| **Lower-bound scope** | No universal explicit-input lower bound is claimed. The source's obstruction records remain scoped to their named oracle or promise models. |
| **Review status** | Internal display and model review; proof and algorithm follow-up is tracked in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Robust unrelated allocation source](../../sources/checkpoint-q/robust_unrelated_common_setup_additive.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
