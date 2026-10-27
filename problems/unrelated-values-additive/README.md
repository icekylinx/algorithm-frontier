# Unrelated-value allocation with exact cost and additive loss

**Guarantee**

Returns utility at least <code class="math">\max\{0,(1-\varepsilon)\mathrm{FOPT}-u_p\}</code> at each selected player, and hence minimum utility at least <code class="math">\max\{0,(1-\varepsilon)\mathrm{FOPT}-u\}</code>. One assignment-cost budget is exact.

**Objective and output**

Choose one permitted actual player set and allocate integral recipient counts; maximize the fractional fixed-set comparator before cost-preserving rounding.

**Randomness**

Deterministic selection, rational optimization and additive-loss rounding with paid exact primitives; whole-ground selection uses deterministic covers.

**Time**

<!-- math-display: 5d5877611e1d9853318e206a
\left(\frac{1}{\varepsilon(1-\varepsilon)^{(1-\varepsilon)/\varepsilon}}\right)^c\mathrm{poly}(H)
-->
![Formula](../../assets/math/5d5877611e1d9853318e206a.svg)

Against <code class="math">\mathrm{FOPT}</code> itself. For fixed rational <code class="math">\varepsilon</code>, also

<!-- math-display: 9b29a55c59319e994d0659cc
\bigl(2-\varepsilon(1-\varepsilon)^{(1-\varepsilon)/\varepsilon}\bigr)^q 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H)
-->
![Formula](../../assets/math/9b29a55c59319e994d0659cc.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The full rational accuracy encoding is included.

**Parameters**

<code class="math">c=q-r</code>; <code class="math">u_p=\max_j v_{pj}</code>; <code class="math">u=\max_p u_p</code>; <code class="math">0&lt;\varepsilon&lt;1</code> is rational. <code class="math">\mathrm{FOPT}</code> chooses an actual permitted set and relaxes only resource counts. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code>.

**Model and representation**

Arbitrary nonnegative player-type values and assignment costs, integral recipient polymatroids, unused resources allowed, one exact scalar assignment budget, and a fixed-cardinality family with an exact restriction selector; an original player-matroid basis is a principal case.

**Lower-bound scope**

No multiplicative constant follows without controlling the largest-unit term. The comparator does not fractionally mix selected bases.

**Review status**

**Ready for review.** The complete exact-budget unrelated-value additive theorem against the fractional optimum on an actual fixed-family selected set: nonnegative original service support separation, full-accuracy weighted omission, uniform denominator recovery and original fixed-set reoptimization, disposal/complement-prefix integral rounding with one exact cost objective, and fixed-accuracy whole-ground conversion.

**Dependencies and scope.** The original fixed-cardinality restriction selector and paid exact rational LP, rank/SFM and integral polymatroid intersection primitives remain mathematical dependencies. The fractional comparator relaxes resource counts, never mixes selected bases. Prefix rounding preserves one scalar assignment cost and loses the stated original largest unit per player. It supplies no positive multiplicative factor without controlling that additive term and does not preserve several independent cost budgets. Shared executable evidence realizes weighted selection, rational recovery and global cover primitives; no native general unrelated-value allocation or rounding solver is claimed. Positive-cost coordinates exceeding the whole budget remain in the fractional model unless a zero-budget exact mask applies. The sharp global expression uses fixed rational accuracy; binary-variable accuracy retains the stated rational upper-envelope implementation.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

Exact reoptimization of the returned fixed-set LP removes the target-search loss, so the old <code class="math">\Gamma(2/\varepsilon)</code> fractional-comparator base is unnecessary. Positive-cost pairs whose full-unit cost exceeds the budget remain eligible for the fractional comparator.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
