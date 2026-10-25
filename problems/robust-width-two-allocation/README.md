# Robust width-two allocation

This is a boundary-sensitive robust allocation record under a width-two
minimal-obstruction promise.

| Field | Curated statement |
|---|---|
| **Guarantee** | Under the width-two promise, returns an exact robust positivity decision and the corresponding allocation or a concrete width-violation certificate. |
| **Objective and output** | Test whether one common actual player basis admits one unit in every explicit scenario; on success, return the basis and scenario-specific allocations; on failure, return the promised obstruction or width-violation outcome. |
| **Time** | The width-two gate takes `phi^c poly(H)`, with `phi=(1+sqrt(5))/2`; the whole-ground conversion takes `(2-1/phi)^q 2^(O(q log log(q+2)/log(q+2))) poly(H)`. |
| **Space** | Polynomial in the explicit scenario input and branching state. The implementation keeps width certificates and basis reconstruction separate from the asymptotic time factor. |
| **Parameters** | `q` is the player count; `r` is the common basis rank; `c=q-r`; `Omega` is the explicit scenario list; `H` is complete encoded input and paid oracle work; `phi=(1+sqrt(5))/2`. |
| **Model and representation** | One common actual player basis across scenarios, integral recipient polymatroids, exact nonnegative assignment budgets, and inclusion-minimal one-unit obstructions of width at most two. Outside the promise, the algorithm returns a width-violation certificate. |
| **Lower-bound scope** | The source records a whole-ground oracle barrier and does not claim an unconditional lower bound for explicit-input allocation. |
| **Review status** | Internal display and model review; proof and algorithm follow-up remains in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Width-two Fibonacci gate](../../sources/checkpoint-q/robust_unit_width_two_fibonacci_gate.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
