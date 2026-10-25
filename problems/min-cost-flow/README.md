# Static and threshold min-cost flow

| Field | Curated statement |
|---|---|
| **Guarantee** | Exact static min-cost flow and exact fixed-threshold feasibility with witness recovery under the named raw backend. |
| **Objective and output** | Decide whether the integral demand can be routed under capacities and a cost threshold; when feasible, return an explicit integral flow while retaining original edge identifiers. |
| **Time** | `O((N+1) E(S)^4 poly(log S))` under the raw-cycle lifetime interface, where `E(S)=exp(O((log S)^(4/5) (log log(S+4))^(1/5)))`; explicit output of a full flow is charged separately. |
| **Space** | Polynomial binary storage for actual edge records and numerical state; stored values use logarithmic bit length in the declared cap. Writing the full flow is a separate output cost. |
| **Parameters** | `N` bounds edge records over their lifetime; `n` and `m` count vertices and current edges; `S` is the declared power-of-two numerical cap; capacities, costs, demands, and threshold are binary encoded. |
| **Model and representation** | Oriented multigraph with loops, parallel arcs, integral capacities, integral costs, integral divergence, and the explicit initial-flow or initialization interface. |
| **Lower-bound scope** | No lower bound is claimed. The upper bound is conditional on the raw-cycle and lifetime-maintenance backend. |
| **Review status** | Conditional research record; finite backend audits are not formal verification. See the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [Moving-box min-cost-flow source](../../sources/checkpoint-o/moving_box_log_barrier_flow.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
