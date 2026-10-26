# Static and threshold min-cost flow

**Guarantee**

Exact static min-cost flow and exact fixed-threshold feasibility with witness recovery under the named raw backend.

**Objective and output**

Decide whether the integral demand can be routed under capacities and a cost threshold; when feasible, return an explicit integral flow while retaining original edge identifiers.

**Randomness**

Deterministic exact numerical reductions. The fast dynamic bound requires the stated deterministic cycle-search, flow-maintenance and edge-retirement data structures for adaptive polynomial-length histories.

**Time**

<code class="math">O((N+1)E(S)^4\mathrm{poly}(\log S))</code> under the raw-cycle lifetime interface, where <code class="math">E(S)=\exp\!\left(O((\log S)^{4/5}(\log\log(S+4))^{1/5})\right)</code>; explicit output of a full flow is charged separately.

**Space**

Polynomial binary storage for actual edge records and numerical state; stored values use logarithmic bit length in the declared cap. Writing the full flow is a separate output cost.

**Parameters**

<code class="math">N</code> bounds edge records over their lifetime, including the artificial initialization arcs; lazy initialization keeps their number linear in original edge births. <code class="math">n</code> and <code class="math">m</code> count vertices and current edges; <code class="math">S</code> is the declared power-of-two numerical cap, including the fixed full-stream artificial penalty. Capacities, costs, demands, and threshold are binary encoded.

**Model and representation**

Oriented multigraph with loops, parallel arcs, integral capacities, integral costs, integral divergence, and the explicit initial-flow or initialization interface.

**Lower-bound scope**

No lower bound is claimed. The upper bound is conditional on the raw-cycle and lifetime-maintenance backend.

**Review status**

**Ready for review in the stated scope.** The exact affine integral-recovery proof and reference checks; artificial-edge penalties, fixed-threshold accounting, and initialization that safely defers currently infeasible prefixes.

**Conditions and remaining work.** The faster numerical client still needs deterministic cycle search, dynamic flow maintenance and edge retirement with the stated lifetime and bit bounds. A NO answer at an early insertion prefix is not permanent infeasibility.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
