# Selected concurrent flow with shared setup and routing budget

| Field | Curated statement |
|---|---|
| **Guarantee** | Selects `r=q-c` commodities and returns a common rate at least `(1-epsilon) OPT`, with one shared setup/routing budget and all listed routing-only budgets exact. |
| **Objective and output** | Maximize common splittable flow rate over an allowed family of `r`-element commodity sets; output the set and a feasible flow. |
| **Time** | `Gamma(1/epsilon)^c poly(H)`, where `Gamma(R)=R^R/(R-1)^(R-1)`. |
| **Space** | Polynomial in the explicit network, selected-set state, and rational flow witnesses. |
| **Parameters** | `q` is the commodity count; `r` is the selected count; `c=q-r`; `epsilon` is rational accuracy; `sigma_i` are setup fees; `C` is the shared budget; `H` includes capacities, demands, costs, routing rows, and the exact minimum-setup restriction oracle. |
| **Model and representation** | Directed rational capacitated network, splittable flows, exact setup/routing budgets, and the minimum-setup restriction oracle specified above. |
| **Lower-bound scope** | No lower bound is claimed; the result is an upper bound conditional on the exact setup optimizer. |
| **Boundary** | An ordinary restriction selector without minimum-setup optimization does not satisfy the theorem's interface. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [allocation/robustness review](../../reviews/backlog/allocation-robustness.md). |
| **Source** | [Shared setup/routing-budget theorem](../../sources/checkpoint-o/shared_setup_routing_budget_corank_flow.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
