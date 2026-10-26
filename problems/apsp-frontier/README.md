# Fully dynamic APSP tradeoff frontier

The manuscript gives incomparable fully dynamic all-pairs shortest-path tradeoffs. Each parameter choice retains both its update cost and its metric stretch.

**Guarantee**

Maintains approximate all-pairs distances under fully dynamic updates with the stretch stated for each parameter choice.

**Objective and output**

Trade amortized update work against distance stretch and return approximate distances for every queried pair.

**Randomness**

Deterministic conditional composition under the normalized deterministic metric-hierarchy contract, including its construction, update and query interfaces.

**Time**

Equalized choice: amortized update work $\exp(O(U^{4/5}h^{1/5}))$; fixed-$C$ choice: $\exp(O(U^{3/4}h^{(C+1)/4}))$; queries are polynomial in $U$.

**Space**

Actual-size hierarchy storage and query structures, charged to the graph inventory and update history; no master-cap padding is materialized.

**Parameters**

**n** is the fixed vertex count; **m** is the current edge count; **N** is the declared polynomial history cap; **U** is log of N plus a constant; **h** is log of U plus a constant. **C** is the fixed stretch-tuning constant in Tradeoff B. Local depth and branching parameters are rounded as specified in the source.

**Model and representation**

Conditional numerical-hierarchy composition for undirected weighted graphs with positive polynomial-range lengths and amortized maintenance. The normalized local work, recourse and approximation inequalities are explicit hypotheses of the proof.

**Lower-bound scope**

The record is an upper-bound frontier and comparison map. It does not assert that either point is globally optimal.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Quantitative tradeoffs

Set $U=\log_2(N+4)$ and $h=\log_2(U+4)$. The general parameter choice gives work per charged input/update record
$\exp(O(U/t+t^3h))$ and stretch $\exp(O(t^4h))$, where $t\to\infty$ and $t^2h=o(U)$.
Distance queries cost $\mathrm{poly}(U)$.

**$t=(U/h)^{1/5}$**

**Work per charged record.** $\exp(O(U^{4/5}h^{1/5}))$

**Stretch.** $\exp(O(U^{4/5}h^{1/5}))$

**$t=U^{3/14}$**

**Work per charged record.** $\exp(O(U^{11/14}))$

**Stretch.** $\exp(O(U^{6/7}h))$

**$t=(U/h)^{5/28}$**

**Work per charged record.** $\exp(O(U^{23/28}h^{5/28}))$

**Stretch.** $\exp(O(U^{5/7}h^{2/7}))$

**$t=(U/h^{C+1})^{1/4}$, fixed $C>0$**

**Work per charged record.** $\exp(O(U^{3/4}h^{(C+1)/4}))$

**Stretch.** $\exp(O(U/h^C))$

**$t=(U^a/h)^{1/4}$, fixed $0<a<1$**

**Work per charged record.** $\exp(O(U^{1-a/4}h^{1/4}))$

**Stretch.** $\exp(O(U^a))$

Total work multiplies the displayed factor by the actual initial vertex/edge inventory plus the number of updates. The port adapter supports arbitrary original degree and accounts for every allocated native record.

Read the [complete proof](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact symbolic forms, the amortized-update scope, and the comparison points. The source does not claim worst-case update time or a constant/polylogarithmic stretch point for Tradeoff B.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
