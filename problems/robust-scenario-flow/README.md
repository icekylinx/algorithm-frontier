# Selected flow with scenario-adaptive routing

**Guarantee**

Selects one permitted commodity set and routes it in every explicit scenario at common rate at least <code class="math">(1-\varepsilon)\mathrm{OPT}</code>.

**Objective and output**

Maximize robust selected concurrent rate; output the common set and a separate feasible splittable routing in each scenario.

**Randomness**

Deterministic for the explicit scenario list, with a paid exact selector. Scenario-dependent routing is recourse after selection, rather than randomized or adversarial input.

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

Polynomial in the full explicit scenario description, rational witnesses, selector state, and paid oracle workspace.

**Parameters**

<code class="math">q</code> is the commodity count; <code class="math">r</code> is the selected cardinality; <code class="math">c=q-r</code>; <code class="math">0&lt;\varepsilon&lt;1</code> is rational. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code>. Scenario count and routing-budget rows are charged in <code class="math">H</code>.

**Model and representation**

Explicit rational networks and demand scales, one common selected set, exact capacities and nonnegative routing budgets, adaptive fractional flow, and an exact permitted-set restriction selector.

**Lower-bound scope**

Exact full-rate admission is <code class="math">\mathrm{W}[2]</code>-hard in the rejected count via Hitting Set, even on the stated forest instances with an unbounded explicit scenario list and no routing budgets. This does not imply the same hardness for the displayed approximate-rate output.

**Review status**

**Ready for review.** The complete adaptive explicit-scenario selected-flow theorem, including scenario-tagged nonnegative Farkas separation, original-coordinate weighted omission, fixed-family rational comparator recovery and fixed-accuracy whole-ground conversion; the parameter-preserving exact-admission Hitting Set reduction including its forest and nonconstant-gap scope. Exact reference supplies common-set certificates, separately scaled adaptive routings and scenario separation.

**Dependencies and scope.** Exact polynomial rational LP, Farkas duality and the paid fixed-family restriction selector remain theorem dependencies. The sharp whole-ground base requires fixed rational accuracy. Scenario list and routing-budget rows are explicit and charged. Selection is common, routing is adaptive and splittable. No implicit uncertainty, oblivious or unsplittable routing guarantee. Reference uses potentially exponential finite Bland simplex and original selected-set enumeration, not the omission recursion or rational target search. Search-free certificates prove fixed-set optimality; global optimality additionally relies on enumeration and the fixed-family predicate. W[2] hardness uses the source fact recorded by Jansen 2017 and the assumption FPT differs from W[2]. It concerns exact admission with arbitrary explicit scenarios, supplies no constant approximation gap and no single-edge-failure-only lower bound.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

Continuous scenario flows permit positive-rate approximation. The [integer robust-allocation obstruction](../robust-two-scenario-hardness/README.md) concerns a distinct positivity decision.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
