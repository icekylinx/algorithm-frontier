# Explicit-item allocation on a selected matroid basis

**Guarantee**

Returns value at least <code class="math">T_{\mathrm{conf}}/(4-3/r)</code> against the player-matroid configuration LP, hence also against integer optimum. An alternative gives factor <code class="math">4-3/r+\eta</code>.

**Objective and output**

Select an actual player-matroid basis and disjoint liked-item bundles with large minimum intrinsic value.

**Randomness**

Deterministic matroid-union reduction and current-blocker search, including both the exact rank-dependent factor and the relaxed quasipolynomial variant.

**Time**

Factor <code class="math">d=4-3/r</code> takes

<!-- math-display: f53c232e9b6631d4d9719b29
2^{O(r)}\mathrm{poly}(H)
-->
![Formula](../../assets/math/f53c232e9b6631d4d9719b29.svg)

Factor <code class="math">d+\eta</code> takes

<!-- math-display: 8ced10ea45fea6f141e8d448
\mathrm{poly}(H)\min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}
-->
![Formula](../../assets/math/8ced10ea45fea6f141e8d448.svg)

**Space**

Polynomial in the explicit item and liking-incidence input, rational encodings, and paid matroid workspace.

**Parameters**

<code class="math">r\ge1</code> is the player-matroid rank; <code class="math">\eta&gt;0</code> is rational; <code class="math">T_{\mathrm{conf}}</code> is the configuration optimum. All matroid-union and original-oracle costs are paid in <code class="math">H</code>.

**Model and representation**

Explicit indivisible items with intrinsic values and explicit liking incidences; an arbitrary player matroid. Configurations and an LP solution are not supplied or enumerated.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

**Ready for review.** The complete explicit-item player-basis theorem and configuration-comparator upgrade: fat-item union and duality, rank-sensitive exact and positive-slack current-blocker bounds, recovery by dual-basis extension, fractional union domination and rational-grid target search. The inner player-eligibility, earliest-circuit exchange, refresh and signature arguments were inspected in the shared current-blocker proof.

**Dependencies and scope.** The original player matroid is supplied by an independence oracle. Polynomial matroid-union/partition and bipartite matching remain named, paid algorithmic dependencies; no unit-cost derived union oracle is assumed. The configuration LP is a proof comparator and is neither supplied nor enumerated by the algorithm. No guarantee against the unrestricted original compact LP is asserted. The new finite checker supports rank and recovery identities; it is not the polynomial union algorithm or a complete allocation implementation. The finite-rank factor tends to four, so no fixed improvement below four is claimed.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [configuration-comparator proof](configuration-comparator.md) establishes the stronger comparator without changing the algorithm. Rank one is exact. The factor tends to four as rank grows; no fixed improvement below four for all ranks is asserted.

**Attribution.** icekylinx · GPT-6 Astra Pro
