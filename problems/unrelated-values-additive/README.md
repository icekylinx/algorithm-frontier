# Unrelated-value allocation with exact cost and additive loss

**Guarantee**

Returns utility at least <code class="math">\max\{0,(1-\varepsilon)\mathrm{FOPT}-u_p\}</code> at each selected player, and hence minimum utility at least <code class="math">\max\{0,(1-\varepsilon)\mathrm{FOPT}-u\}</code>. One assignment-cost budget is exact.

**Objective and output**

Choose one permitted actual player set and allocate integral recipient counts; maximize the fractional fixed-set comparator before cost-preserving rounding.

**Randomness**

Deterministic selection, rational optimization and additive-loss rounding with paid exact primitives; whole-ground selection uses deterministic covers.

**Time**

<code class="math">\Gamma(1/\varepsilon)^c\mathrm{poly}(H)</code> against <code class="math">\mathrm{FOPT}</code> itself. For fixed rational <code class="math">\varepsilon</code>, also <code class="math">\bigl(2-1/\Gamma(1/\varepsilon)\bigr)^q E(q)\mathrm{poly}(H)</code>.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The full rational accuracy encoding is included.

**Parameters**

<code class="math">c=q-r</code>; <code class="math">u_p=\max_j v_{pj}</code>; <code class="math">u=\max_p u_p</code>; <code class="math">0&lt;\varepsilon&lt;1</code> is rational. <code class="math">\mathrm{FOPT}</code> chooses an actual permitted set and relaxes only resource counts. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code> and <code class="math">E(q)=2^{O(q\log\log(q+2)/\log(q+2))}</code>.

**Model and representation**

Arbitrary nonnegative player-type values and assignment costs, integral recipient polymatroids, unused resources allowed, one exact scalar assignment budget, and a fixed-cardinality family with an exact restriction selector; an original player-matroid basis is a principal case.

**Lower-bound scope**

No multiplicative constant follows without controlling the largest-unit term. The comparator does not fractionally mix selected bases.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

Exact reoptimization of the returned fixed-set LP removes the target-search loss, so the old <code class="math">\Gamma(2/\varepsilon)</code> fractional-comparator base is unnecessary. Positive-cost pairs whose full-unit cost exceeds the budget remain eligible for the fractional comparator.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
