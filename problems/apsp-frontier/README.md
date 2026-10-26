# Fully dynamic APSP tradeoff frontier

The manuscript gives incomparable fully dynamic all-pairs shortest-path tradeoffs. Each parameter choice retains both its update cost and its metric stretch.

**Guarantee**

Maintains approximate all-pairs distances under fully dynamic updates with the stretch stated for each parameter choice.

**Objective and output**

Trade amortized update work against distance stretch and return approximate distances for every queried pair.

**Randomness**

Deterministic fully dynamic metric construction. The source map supplies the hierarchy, initialization/update and numerical bounds; the parameter and output restrictions remain part of the theorem.

**Time**

Equalized choice: amortized update work <code class="math">\exp(O(U^{4/5}h^{1/5}))</code>; fixed-<code class="math">C</code> choice: <code class="math">\exp(O(U^{3/4}h^{(C+1)/4}))</code>; queries are polynomial in <code class="math">U</code>.

**Space**

Actual-size hierarchy storage and query structures, charged to the graph inventory and update history; no master-cap padding is materialized.

**Parameters**

**n** is the fixed vertex count; **m** is the current edge count; **N** is the declared polynomial history cap; **U** is log of N plus a constant; **h** is log of U plus a constant. **C** is the fixed stretch-tuning constant in Tradeoff B. Local depth and branching parameters are rounded as specified in the source.

**Model and representation**

Undirected graphs with polynomial-range integer lengths and amortized maintenance. Theorem 2.1 gives the generic hierarchy implication; Corollary 2.2 instantiates it with the local construction. All displayed frontier points support nonnegative lengths and exact zero-distance answers by Corollary 6.1; the unrestricted general family is stated for positive lengths.

**Lower-bound scope**

The record is an upper-bound frontier and comparison map. It does not assert that either point is globally optimal.

**Review status**

**Ready for review.** The constructed fully dynamic metric hierarchy, full time/stretch curve and all five explicit parameter points, including the same-stretch 23/28 versus 6/7 comparison. The nonnegative-integer adapter supplies exact zero answers and transformed-range accounting.

**Dependencies and scope.** The tradeoff is amortized and reports numerical distances. Its general family assumes t tends to infinity and t^2 h=o(U); extending that family to zero lengths additionally needs t^4 h=o(U) and a uniform stretch bound. The five displayed points satisfy the stronger conditions.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Quantitative tradeoffs

Set <code class="math">U=\log_2(N+4)</code> and <code class="math">h=\log_2(U+4)</code>. The general parameter choice gives work per charged input/update record
<code class="math">\exp(O(U/t+t^3h))</code> and stretch <code class="math">\exp(O(t^4h))</code>, where <code class="math">t\to\infty</code> and <code class="math">t^2h=o(U)</code>.
Distance queries cost <code class="math">\mathrm{poly}(U)</code>.

- **Balanced:** <code class="math">t=(U/h)^{1/5}</code> gives logarithmic work and stretch
  both <code class="math">O(U^{4/5}h^{1/5})</code>.
- **Smaller work exponent:** <code class="math">t=U^{3/14}</code> gives logarithmic work
  <code class="math">O(U^{11/14})</code> and logarithmic stretch <code class="math">O(U^{6/7}h)</code>.
- **Matched finer stretch:** <code class="math">t=(U/h)^{5/28}</code> gives logarithmic
  work <code class="math">O(U^{23/28}h^{5/28})</code> and logarithmic stretch <code class="math">O(U^{5/7}h^{2/7})</code>.
- **Fixed <code class="math">C&gt;0</code>:** <code class="math">t=(U/h^{C+1})^{1/4}</code> gives logarithmic work
  <code class="math">O(U^{3/4}h^{(C+1)/4})</code> and logarithmic stretch <code class="math">O(U/h^C)</code>.
- **Fixed <code class="math">0&lt;a&lt;1</code>:** <code class="math">t=(U^a/h)^{1/4}</code> gives logarithmic work
  <code class="math">O(U^{1-a/4}h^{1/4})</code> and logarithmic stretch <code class="math">O(U^a)</code>.

Total work multiplies the displayed factor by the actual initial vertex/edge inventory plus the number of updates. The port adapter supports arbitrary original degree and accounts for every allocated native record.

Read the [complete proof](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact symbolic forms, the amortized-update scope, and the comparison points. The source does not claim worst-case update time or a constant/polylogarithmic stretch point for Tradeoff B.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
