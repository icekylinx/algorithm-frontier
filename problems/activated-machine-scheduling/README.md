# Scheduling with an activated machine basis

**Guarantee**

Returns an actual activated basis and a complete legal schedule; offers factor <code class="math">1+\varepsilon</code>, exact factor <code class="math">3/2</code>, and the bucket curve <code class="math">\gamma_k=\frac{3\cdot2^k-1}{2^{k+1}-1}</code>. Detects global infeasibility.

**Objective and output**

Minimize maximum load subject to all original job totals and one exact combined setup and assignment budget.

**Randomness**

Deterministic enumeration of activation bases and profiles, followed by exact feasibility and recovery tests.

**Time**

Let <code class="math">\delta=\varepsilon/2</code>, <code class="math">K=\lfloor1/\delta\rfloor</code>, and <code class="math">L=\left\lceil(1-\delta)/\delta^2\right\rceil</code>. The three bounds are

<!-- math-display: b5a7ea24cf83d06b2d9e67d3
\binom{q}{r}\min\!\left\{\binom{L+K}{K}^{r},\exp(3r(K+1))\right\}\mathrm{poly}(H_\varepsilon)
-->
![Formula](../../assets/math/b5a7ea24cf83d06b2d9e67d3.svg)

<!-- math-display: 775760c026c176838605a99c
\binom{q}{r}6^r\mathrm{poly}(H)
-->
![Formula](../../assets/math/775760c026c176838605a99c.svg)

And

<!-- math-display: 98a6d92cdc17f107f5795169
\binom{q}{r}(k+1)^r\mathrm{poly}(H+k)
-->
![Formula](../../assets/math/98a6d92cdc17f107f5795169.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The full rational accuracy encoding is charged.

**Parameters**

<code class="math">q</code> is the physical-machine count; <code class="math">r</code> is the activation-matroid rank; <code class="math">\varepsilon</code> is rational with <code class="math">0&lt;\varepsilon\le1</code>; <code class="math">k\ge0</code> is an integer. <code class="math">H_\varepsilon=H+\mathrm{size}(\varepsilon)</code>. Original totals are <code class="math">n_j=f_j(P)</code>.

**Model and representation**

Arbitrary nonnegative machine-type processing times, integral job polymatroids, an actual machine-matroid basis, nonnegative setup and assignment costs, eligibility masks, and one shared exact budget.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

**Ready for review.** The complete activated-basis Theorem AS: genuine fixed-cardinality activation bases, original mandatory job-polymatroid totals after eligibility/activation masks, one exact combined nonnegative setup-and-assignment budget, exact global/zero feasibility, active-rank profile enumeration for the approximation scheme, bucket curve and exact three-halves six-profile endpoint, one joint minimum-cost integer recovery and nonmonotone one-sided grid optimization. The fixed-cardinality polynomial-membership extension has the same proved enumeration interface. The complete-table reference realizes activation restriction, binary greedy feasibility and all three local profile clients with their inherited solver costs separate.

**Dependencies and scope.** The original theorem uses the stated paid exact matroid/rank/SFM, rational LP and integral polymatroid-intersection primitives. The reference streams actual bases and profiles and checks original totals before compressing to active coordinates, but its canonical positive-target solver retains explicitly charged LP-vertex and numeric count enumeration and potentially exponential vertex storage. The shared budget is one scalar setup-plus-assignment row; independent affordable pieces or a minimum-setup basis do not replace the joint capacity/cost test. Rank-zero and empty-job cases retain the actual activation requirement. Helper preconditions for genuine bases and already-masked ranks are documented and checked. Finite executable evidence, complete mathematical proof, formal verification, external review and publication priority remain distinct; formal verification, external peer review and exhaustive publication priority are not claimed.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The rank-sensitive enumeration first chooses an actual activated basis, then profiles only its <code class="math">r</code> machines. Original job totals stay mandatory after restriction; an affordable setup basis alone does not certify scheduling feasibility.

**Attribution.** icekylinx · GPT-6 Astra Pro
