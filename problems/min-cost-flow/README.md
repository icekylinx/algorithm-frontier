# Static and threshold min-cost flow

**Guarantee**

Exact static min-cost flow and exact fixed-threshold feasibility with witness recovery under the named raw backend.

**Objective and output**

Decide whether the integral demand can be routed under capacities and a cost threshold; when feasible, return an explicit integral flow while retaining original edge identifiers.

**Randomness**

Deterministic exact numerical client conditional on the stated deterministic raw-cycle/lifetime backend, including its guarantees for adaptive polynomial-length histories.

**Time**

$O((N+1)E(S)^4\mathrm{poly}(\log S))$ under the raw-cycle lifetime interface, where $E(S)=\exp\!\left(O((\log S)^{4/5}(\log\log(S+4))^{1/5})\right)$; explicit output of a full flow is charged separately.

**Space**

Polynomial binary storage for actual edge records and numerical state; stored values use logarithmic bit length in the declared cap. Writing the full flow is a separate output cost.

**Parameters**

$N$ bounds edge records over their lifetime; $n$ and $m$ count vertices and current edges; $S$ is the declared power-of-two numerical cap; capacities, costs, demands, and threshold are binary encoded.

**Model and representation**

Oriented multigraph with loops, parallel arcs, integral capacities, integral costs, integral divergence, and the explicit initial-flow or initialization interface.

**Lower-bound scope**

No lower bound is claimed. The upper bound is conditional on the raw-cycle and lifetime-maintenance backend.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
