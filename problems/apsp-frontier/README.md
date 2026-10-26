# Fully dynamic APSP tradeoff frontier

The manuscript gives incomparable fully dynamic all-pairs shortest-path tradeoffs. Each parameter choice retains both its update cost and its metric stretch.

**Guarantee**

Maintains approximate all-pairs distances under fully dynamic updates with the stretch stated for each parameter choice.

**Objective and output**

Trade amortized update work against distance stretch and return approximate distances for every queried pair.

**Randomness**

Deterministic conditional composition using the metric hierarchy, construction/update guarantees and uniform numerical bounds listed in the source map.

**Time**

Equalized choice: amortized update work $`\exp(O(U^{4/5}h^{1/5}))`$; fixed-$`C`$ choice: $`\exp(O(U^{3/4}h^{(C+1)/4}))`$; queries are polynomial in $`U`$.

**Space**

Actual-size hierarchy storage and query structures, charged to the graph inventory and update history; no master-cap padding is materialized.

**Parameters**

**n** is the fixed vertex count; **m** is the current edge count; **N** is the declared polynomial history cap; **U** is log of N plus a constant; **h** is log of U plus a constant. **C** is the fixed stretch-tuning constant in Tradeoff B. Local depth and branching parameters are rounded as specified in the source.

**Model and representation**

Conditional numerical-hierarchy composition for undirected graphs with polynomial-range integer lengths and amortized maintenance. All displayed frontier points support nonnegative lengths and exact zero-distance answers by Corollary 6.1; the unrestricted general family is stated for positive lengths. The normalized local work, recourse and approximation inequalities remain explicit hypotheses.

**Lower-bound scope**

The record is an upper-bound frontier and comparison map. It does not assert that either point is globally optimal.

**Review status**

**Ready for review in the stated scope.** The five explicit parameter substitutions and the nonnegative-integer distance adapter, including exact zero answers, transformed length range, and the required uniform stretch bound.

**Conditions and remaining work.** The positive-distance hierarchy remains an explicit prerequisite. For the general parameter family, the zero-length extension additionally needs t^4 h=o(U); t^2 h=o(U) alone is insufficient. Only numerical distance output is claimed.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Quantitative tradeoffs

Set $`U=\log_2(N+4)`$ and $`h=\log_2(U+4)`$. The general parameter choice gives work per charged input/update record
$`\exp(O(U/t+t^3h))`$ and stretch $`\exp(O(t^4h))`$, where $`t\to\infty`$ and $`t^2h=o(U)`$.
Distance queries cost $`\mathrm{poly}(U)`$.

- **Balanced:** $`t=(U/h)^{1/5}`$ gives logarithmic work and stretch
  both $`O(U^{4/5}h^{1/5})`$.
- **Smaller work exponent:** $`t=U^{3/14}`$ gives logarithmic work
  $`O(U^{11/14})`$ and logarithmic stretch $`O(U^{6/7}h)`$.
- **Matched finer stretch:** $`t=(U/h)^{5/28}`$ gives logarithmic
  work $`O(U^{23/28}h^{5/28})`$ and logarithmic stretch $`O(U^{5/7}h^{2/7})`$.
- **Fixed $`C>0`$:** $`t=(U/h^{C+1})^{1/4}`$ gives logarithmic work
  $`O(U^{3/4}h^{(C+1)/4})`$ and logarithmic stretch $`O(U/h^C)`$.
- **Fixed $`0<a<1`$:** $`t=(U^a/h)^{1/4}`$ gives logarithmic work
  $`O(U^{1-a/4}h^{1/4})`$ and logarithmic stretch $`O(U^a)`$.

Total work multiplies the displayed factor by the actual initial vertex/edge inventory plus the number of updates. The port adapter supports arbitrary original degree and accounts for every allocated native record.

Read the [complete proof](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact symbolic forms, the amortized-update scope, and the comparison points. The source does not claim worst-case update time or a constant/polylogarithmic stretch point for Tradeoff B.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
