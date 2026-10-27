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

<code class="math">c=q-r</code>; <code class="math">0&lt;\varepsilon&lt;1</code> is rational; <code class="math">u_{\omega,p}=\max(\{v_{\omega,p,j}:f_{\omega,j}(\{p\})\ge1\}\cup\{0\})</code>; <code class="math">u=\max_{\omega,p}u_{\omega,p}</code>. <code class="math">\mathrm{FOPT}</code> maximizes over one actual common basis and relaxes only scenario assignment counts. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code>.

**Model and representation**

Player-specific scenario values, integral recipient polymatroids, a common nonnegative setup vector, scenario-specific exact scalar budgets and assignment costs, one common actual player-matroid basis, and unused resources allowed.

**Lower-bound scope**

This additive guarantee does not imply a finite multiplicative guarantee when the largest-unit loss dominates. Distinct scenario setup vectors and one common integer allocation require separate arguments.

**Review status**

**Ready for review.** Complete canonical actual-common-basis fractional-comparator theorem with arbitrary scenario/player-specific values, recipient polymatroids and assignment costs; one common setup vector and exact scenario scalar budgets; attained minimum-setup restriction selection; intersected scenario nonnegative separation; same-basis protected witnesses through changing residual budgets; weighted prefix and streamed whole-ground time; full-accuracy original fixed-basis rational reoptimization; independent exact-budget scenario rounding; and role/dummy/common-setup boundary constructions. Native reference exercises this actual pipeline with original inputs and explicitly separate finite LP cost.

**Dependencies and scope.** The scenario list is explicit and nonempty. One actual original player-matroid basis is selected before the scenario; only assignments adapt. FOPT relaxes resource counts on one common actual basis and does not mix or change bases by scenario. Original counts may be unused and all original costs are nonnegative. The setup vector is identical in every scenario. Each current residual budget subtracts the cost of the same attaining minimum-setup basis. Arbitrary scenario-specific setup vectors, one common integer assignment or a common heavy/light role mask require additional arguments and are not included. The guarantee retains the scenario/player-specific largest-unit additive loss, including zero when it dominates. It does not provide an unrestricted positive multiplicative guarantee on zero/one robust instances or round a shared fractional dummy into one common integer selection. The fast mathematical bounds charge exact polynomial rank/SFM, LP, weighted intersection and streamed-cover primitives. The complete-table reference enumerates active LP systems and temporarily stores projected support vertices, with potentially exponential local time and memory separate from those bounds. It never expands binary resource units; original labels including loops are retained in software. Rank zero has an explicit empty-basis convention, outside the nontrivial positive-rank theorem. Independent original-input finite checks and code/manuscript reviews do not constitute proof-assistant formalization, external peer review or an exhaustive publication-priority search.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

<code class="math">\mathrm{FOPT}</code> is one comparator name, not a product of an unspecified factor and integer <code class="math">\mathrm{OPT}</code>. The proof retains all fractional coordinates needed by that comparator, including pairs whose full-unit cost exceeds a positive budget.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
