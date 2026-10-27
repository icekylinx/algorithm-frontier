# An approximation scheme for arbitrary-value allocation

**Guarantee**

Returns an actual selected basis and an integer allocation of utility at least <code class="math">(1-\varepsilon)\mathrm{OPT}</code> under the exact combined setup and assignment budget.

The [native exact-table reference](reference/README.md) implements the full
original-basis/profile construction and output verifier. Its finite streamed
active-system LP costs are charged separately from the theorem below.

**Objective and output**

Maximize minimum player-specific utility; detect whether any selected basis is affordable even at zero utility.

**Randomness**

Deterministic profile and basis enumeration with paid exact rank, submodular-minimization, LP and intersection primitives.

**Time**

Put <code class="math">\delta=\varepsilon/3</code>, <code class="math">J=\lfloor1/\delta\rfloor</code>, <code class="math">K=\lceil1/\delta\rceil</code>, <code class="math">L=\left\lceil(1-\delta)/\delta^2\right\rceil</code>, and <code class="math">C_\delta=\binom{L+K}{K}</code>. Time is

<!-- math-display: e9ede6a0724f2a2292ed888c
\binom{q}{r}\min\{C_\delta^r,\exp(4r(J+1))\}\mathrm{poly}(H_\varepsilon)
-->
![Formula](../../assets/math/e9ede6a0724f2a2292ed888c.svg)

Hence

<!-- math-display: ea221737035e25693956aef6
\binom{q}{r}\exp(O(r/\varepsilon))\mathrm{poly}(H_\varepsilon)
-->
![Formula](../../assets/math/ea221737035e25693956aef6.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. Space includes the full rational accuracy encoding.

**Parameters**

<code class="math">q</code> is the nonloop player count; <code class="math">r</code> is the selected matroid rank; <code class="math">0&lt;\varepsilon\le1</code> is rational; <code class="math">H_\varepsilon=H+\mathrm{size}(\varepsilon)</code>. <code class="math">H</code> includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Arbitrary nonnegative player-type values, integral recipient polymatroids, an actual original player basis, nonnegative setup and assignment costs, eligibility masks, and one shared scalar budget. Unused resources are allowed.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

**Ready for review.** The complete arbitrary-value optional-player approximation scheme with a genuine original player basis, recipient polymatroids, eligibility, optional unused capacity, arbitrary nonnegative player/type values, setup fees and one shared exact setup/assignment budget: integer-target capping, occupied profiles and both state-count envelopes, original joint LP feasibility, cost-preserving disposal/complement-prefix rounding, full requested accuracy and one-sided original-grid optimization. Includes a native complete-table implementation and independent original-input/output verification with separately charged finite LP costs.

**Dependencies and scope.** The mathematical time envelopes charge named polynomial exact rank/SFM, LP and weighted polymatroid-intersection primitives. The complete-table reference streams LP active systems after exact fixed-coordinate substitution, with an additional `binom(R,D)` factor for actual remaining rows and free dimension `D<=m*q`; it does not implement those fast primitive costs. Complete rank-table input, augmented disposal tables, rational arithmetic and the full binary accuracy encoding are charged. The approximation comparator is original integer optimum, not the capped fractional relaxation or a fractional selected basis. Original type capacities remain shared across all players and bins; one actual scalar cost objective preserves the single shared setup and assignment budget. Several independent exact budgets and extra coupling constraints between types are outside this scope. Internal proof review, exact finite original-input comparisons and producer-independent output verification are not proof-assistant formalization or external peer review. The cited ICALP 2025 rounding paper is a public antecedent, not a black-box proof of this full profile model.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
