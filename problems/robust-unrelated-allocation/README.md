# Robust unrelated allocation with common setup costs

**Guarantee**

Returns per-player, per-scenario utility at least <code class="math">\max\{0,(1-\varepsilon)\mathrm{FOPT}-u_{\omega,p}\}</code> on one common actual basis. Hence robust minimum utility is at least <code class="math">\max\{0,(1-\varepsilon)\mathrm{FOPT}-u\}</code>. Every scenario's combined setup and assignment budget remains exact.

**Objective and output**

Maximize robust common utility while choosing a single basis before the scenario and allowing integral assignments to adapt afterward.

**Randomness**

Deterministic common-basis selection and exact-budget rounding in each listed scenario; whole-ground selection also uses deterministic covers.

**Time**

<!-- math-display: 5d5877611e1d9853318e206a
\left(\frac{1}{\varepsilon(1-\varepsilon)^{(1-\varepsilon)/\varepsilon}}\right)^c\mathrm{poly}(H)
-->
![Formula](../../assets/math/5d5877611e1d9853318e206a.svg)

For fixed rational <code class="math">\varepsilon</code>, the whole-ground alternative is

<!-- math-display: 9b29a55c59319e994d0659cc
\bigl(2-\varepsilon(1-\varepsilon)^{(1-\varepsilon)/\varepsilon}\bigr)^q 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H)
-->
![Formula](../../assets/math/9b29a55c59319e994d0659cc.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. All scenarios are explicit.

**Parameters**

<code class="math">c=q-r</code>; <code class="math">0&lt;\varepsilon&lt;1</code> is rational; <code class="math">u_{\omega,p}=\max_j v_{\omega,p,j}</code>; <code class="math">u=\max_{\omega,p}u_{\omega,p}</code>. <code class="math">\mathrm{FOPT}</code> maximizes over one actual common basis and relaxes only scenario assignment counts. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code>.

**Model and representation**

Player-specific scenario values, integral recipient polymatroids, a common nonnegative setup vector, scenario-specific exact scalar budgets and assignment costs, one common actual player-matroid basis, and unused resources allowed.

**Lower-bound scope**

This additive guarantee does not imply a finite multiplicative guarantee when the largest-unit loss dominates. Distinct scenario setup vectors and one common integer allocation require separate arguments.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

<code class="math">\mathrm{FOPT}</code> is one comparator name, not a product of an unspecified factor and integer <code class="math">\mathrm{OPT}</code>. The proof retains all fractional coordinates needed by that comparator, including pairs whose full-unit cost exceeds a positive budget.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
