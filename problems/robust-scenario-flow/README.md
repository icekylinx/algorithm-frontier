# Robust selected flow across scenarios

This is a supporting robust-flow record with adaptive routing after the
scenario is revealed.

| Field | Curated statement |
|---|---|
| **Guarantee** | Selects one common commodity set and routes it in every explicit scenario at a common rate at least `(1 - epsilon)` times the robust optimum. |
| **Objective and output** | Maximize the common selected rate; output the selected set and a scenario-specific feasible routing for every listed scenario. Routing decisions may adapt to the revealed scenario. |
| **Time** | Polynomial input and separation work multiplied by the inverse-accuracy selector base raised to the rejected-commodity count `c`; equivalently, the source uses Gamma of inverse accuracy raised to `c`, times polynomial work. The scenario count and routing-budget-row count are charged through the explicit input length. |
| **Space** | Polynomial in the complete explicit scenario description, rational data, selector state, and routing witnesses; no scenario is compressed into an undocumented common flow. |
| **Parameters** | `q` is the commodity count; `r` is the selected count; `c = q - r` is the rejected count; `epsilon` is rational accuracy; `H` includes all scenarios, capacities, demand scales, and routing budgets; `Omega` is the explicit scenario list. |
| **Model and representation** | Common selected set, scenario-dependent networks or demands, exact capacities, explicit nonnegative routing-budget rows, and adaptive fractional flows. Exact full-rate admission hardness is separate. |
| **Lower-bound scope** | The source includes an exact unit-admission hardness boundary without routing budgets. It does not imply hardness for every approximate or adaptive-flow model. |
| **Review status** | Internal display and model review; proof and algorithm follow-up remains in the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). Finite audits are not formal verification. |
| **Source** | [Adaptive selected flow](../../sources/checkpoint-o/robust_scenario_selected_flow_corank.md), its [proof map](proof.md), and `verify/`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
