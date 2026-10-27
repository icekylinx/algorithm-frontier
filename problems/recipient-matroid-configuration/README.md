# Allocation with recipient matroids and a configuration comparator

**Guarantee**

Returns value at least <code class="math">T_{\mathrm{conf}}/d</code> with <code class="math">d=4-3/r</code>. With a certified local factor-<code class="math">\lambda</code> oracle, use <code class="math">d=\lambda^{-1}+3-3/r</code>. Factor <code class="math">d+\eta</code> has the rank-quasipolynomial alternative.

**Objective and output**

Select a player basis and integral resource bundles satisfying every recipient matroid and any supplied downward-closed local family.

**Randomness**

Deterministic current-blocker search with exact paid primitives. The optional factor-`lambda` availability oracle requires a certified per-call guarantee.

**Time**

For factor <code class="math">d</code>, the time bound is:

<!-- math-display: f53c232e9b6631d4d9719b29
2^{O(r)}\mathrm{poly}(H)
-->
![Formula](../../assets/math/f53c232e9b6631d4d9719b29.svg)

For <code class="math">d+\eta</code>, it is:

<!-- math-display: 8ced10ea45fea6f141e8d448
\mathrm{poly}(H)\min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}
-->
![Formula](../../assets/math/8ced10ea45fea6f141e8d448.svg)

**Space**

Polynomial in the original encoded matroid and resource input and paid oracle workspace. The exponentially many configurations are not input or stored.

**Parameters**

<code class="math">r\ge1</code> is the selected player rank; <code class="math">\eta&gt;0</code> and the certified <code class="math">0&lt;\lambda\le1</code> are rational; <code class="math">T_{\mathrm{conf}}</code> is the coupled configuration optimum. <code class="math">H</code> includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

One service per player-resource pair, common intrinsic resource values, arbitrary recipient matroids, an arbitrary player matroid, and a paid local availability oracle when local families are present.

**Lower-bound scope**

No lower bound is asserted. The coupled configuration comparator uses separate recipient-matroid columns; arbitrary polymatroid aggregation need not preserve it.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The manuscript defines the comparator explicitly and proves its reduction to the compact small-resource promise. No LP solution or configuration enumeration is required.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
