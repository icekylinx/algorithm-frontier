# One-value allocation with exact quotas and setup costs

**Guarantee**

Returns at least <code class="math">\lceil K_\star/2\rceil</code> units to every player of an actual selected basis, preserving the exact combined setup and assignment budget. More generally, fixed integer <code class="math">d\ge2</code> gives <code class="math">\lceil K_\star/d\rceil</code>.

**Objective and output**

Maximize the common minimum count of equal-value units; output a selected basis and integral resource counts.

**Randomness**

Deterministic corank branching and exact-budget recovery; the whole-ground alternative uses deterministic inclusion covers.

**Time**

For fixed integer <code class="math">d\ge2</code>, the two time bounds are:

<!-- math-display: 114a0af1b69ee8e6edcafab2
\begin{aligned}
\text{Corank parameter:}\quad &\left(\frac{(d+1)^{d+1}}{4(d-1)^{d-1}}\right)^{c/(d-1)}\mathrm{poly}(H),\\
\text{Whole ground:}\quad &\left(2-\left(\frac{4(d-1)^{d-1}}{(d+1)^{d+1}}\right)^{1/(d-1)}\right)^q 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H).
\end{aligned}
-->
![Formula](../../assets/math/114a0af1b69ee8e6edcafab2.svg)

Exact factor two has corank base <code class="math">27/4</code> and whole-ground base <code class="math">50/27</code>; factor three has the respective bases <code class="math">4</code> and <code class="math">7/4</code>.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

<code class="math">q</code> is the nonloop player count; <code class="math">r\ge1</code> is its matroid rank; <code class="math">c=q-r</code>; <code class="math">K_\star</code> is the integer optimum count; each unit has value <code class="math">v&gt;0</code>. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code>. <code class="math">H</code> includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Arbitrary integral recipient polymatroids, an original player-matroid basis, nonnegative setup and assignment costs, one shared exact budget, and unused resources allowed.

**Lower-bound scope**

The [strict-below-two oracle barrier](../allocation-lower-bounds/proof.md) applies to an included zero-cost subclass; it does not prove these exponential bases optimal.

**Review status**

**Ready for review in the stated scope.** The main exact factor-two theorem with one assignment-cost budget, the exact prescribed-basis endpoint and the stated strict-below-two oracle boundary. The one-unit gate now has a direct Boolean-cap augmentation proof, an exact assignment-pair matroid construction and binary-size accounting; the main proof supplies nonnegative separation, weighted omission, no-loss quota recovery and target search.

**Dependencies and scope.** Exact submodular minimization, rational LP with separation, and weighted matroid or integral-polymatroid intersection remain paid polynomial primitives. The gate proof identifies their original finite grounds and does not expand binary capacities into unit copies. The separate shared-setup, general integer-factor and whole-ground conversion results are outside this bounded main-theorem audit. Finite gate checks do not implement the full allocator or certify the unbounded runtime theorem.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [base proof](proof.md) treats assignment costs; the [setup and full quota tradeoff](setup-tradeoffs.md) proves the stronger shared-budget statement. With <code class="math">c=0</code>, exact count optimization is polynomial after subtracting the fixed setup cost.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
