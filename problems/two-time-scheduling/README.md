# Scheduling with two processing times per machine

**Guarantee**

For every fixed integer <code class="math">d\ge2</code>, returns makespan at most <code class="math">(2-1/d)\mathrm{OPT}</code>, including exact <code class="math">3/2</code> at <code class="math">d=2</code>.

**Objective and output**

Assign every original type total when each machine has at most two positive processing times, preserving the exact assignment-cost budget.

**Randomness**

Deterministic quota search and original-total recovery, including the fixed-factor endpoints and deterministic whole-ground conversion.

**Time**

For the fixed integer approximation parameter <code class="math">d\ge2</code>, time is

<!-- math-display: 1978ae1bee1cb5578fcb8a30
\left(2-\left(\frac{4(d-1)^{d-1}}{(d+1)^{d+1}}\right)^{1/(d-1)}\right)^q 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H)
-->
![Formula](../../assets/math/1978ae1bee1cb5578fcb8a30.svg)

Endpoints are

<!-- math-display: 6801e0cf663f5fac123cbc6b
(\text{factor},\text{base})=(3/2,50/27),(5/3,7/4),\bigl(7/4,2-(108/3125)^{1/3}\bigr).
-->
![Formula](../../assets/math/6801e0cf663f5fac123cbc6b.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

<code class="math">q</code> is the physical-machine count; <code class="math">d\ge2</code> is a fixed integer; each machine has its own at most two positive times <code class="math">u_p&lt;a_p</code>. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code>. <code class="math">H</code> includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Integral job polymatroids, mandatory original bases, machine-dependent two-time pairs, arbitrary nonnegative assignment costs, and one exact scalar budget. Zero-time pairs are permitted.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The positive time pair may differ from machine to machine. A rational noninteger <code class="math">d</code> is not included in the discrete quota proof.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
