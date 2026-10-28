# A discrete scheduling tradeoff from processing buckets

**Guarantee**

For every integer <code class="math">k\ge0</code>, returns makespan at most <code class="math">\gamma_k\mathrm{OPT}</code>, where <code class="math">\gamma_k=\frac{3\cdot2^k-1}{2^{k+1}-1}=\frac{3}{2}+\frac{1}{2(2^{k+1}-1)}</code>.

**Objective and output**

Assign all original job totals with exact recipient feasibility and one exact assignment-cost budget.

**Randomness**

Deterministic bucket enumeration and exact minimum-cost recovery, for every stated integer bucket depth.

**Time**

<!-- math-display: 0ec2ea6f2751405f583d3074
(k+1)^q\mathrm{poly}(H+k)
-->
![Formula](../../assets/math/0ec2ea6f2751405f583d3074.svg)

Choosing <code class="math">k=O(\log(1+1/\varepsilon))</code> gives factor <code class="math">3/2+\varepsilon</code> in

<!-- math-display: e55ad0d26aed68993a20d89b
[O(1+\log(1+1/\varepsilon))]^q\mathrm{poly}(H_\varepsilon)
-->
![Formula](../../assets/math/e55ad0d26aed68993a20d89b.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. Bucket depth is charged as stated in the time bound.

**Parameters**

<code class="math">q</code> is the physical-machine count; <code class="math">k</code> is an integer bucket depth. The first points are <code class="math">(\text{factor},\text{base})=(2,1),(5/3,2),(11/7,3),(23/15,4)</code>. <code class="math">H</code> includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Arbitrary nonnegative rational processing times and assignment costs, integral job polymatroids, mandatory original totals, eligibility masks, and one exact scalar budget.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

**Ready for review.** The complete arbitrary-time bucket-label Theorem AB and its depth/accuracy tradeoff: exact open-left/closed-right masks, full-target label witness, mandatory original bases and exact one-budget joint recovery, upper-prefix machine bounds, zero processing and one-sided grid optimization, complete depth-dependent enumeration accounting and optimality of the stated contiguous one-big-group analysis template. The reference bucket client instantiates the shared general-processing joint plan solver with separate finite solver costs.

**Dependencies and scope.** The theorem uses paid exact rank/SFM, rational LP and integral polymatroid-intersection primitives. The reference shares the canonical general-processing/two-time LP and numeric count baseline, preserving its explicit enumeration and vertex-storage costs rather than claiming the fast per-label implementation. Depth is charged numerically in the stated H+k bounds; no polynomial-in-log-depth claim is made, and no finite depth attains exact three-halves by this one-big-group construction. Template optimality is not a general scheduling lower bound. Finite executable evidence is not proof-assistant verification or external peer review; exhaustive publication priority is not claimed.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

For an exact <code class="math">3/2</code> guarantee at constant base, use the separate [six-profile construction](../six-profile-three-halves/README.md).

**Attribution.** icekylinx · GPT-6 Astra Pro
