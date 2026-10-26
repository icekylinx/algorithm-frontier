# Independent transversals with explicit obstruction certificates

**Guarantee**

Returns an independent transversal, or a class set <code class="math">S</code>, a total dominating set <code class="math">D</code>, and a constellation <code class="math">K</code> with <code class="math">V(K)\subseteq D</code>, <code class="math">\lvert D\rvert&lt;(2+\varepsilon)(\lvert S\rvert-1)</code>, and <code class="math">\lvert D\setminus V(K)\rvert&lt;\varepsilon(\lvert S\rvert-1)</code>.

**Objective and output**

Select one vertex from each class with no selected edge, or output the stated directly checkable domination and constellation objects.

**Randomness**

Deterministic certifying construction, including the elementary exponential fallback; arbitrary choices use fixed tie rules.

**Time**

<!-- math-display: f11f263ea859ef2e2a4540e1
P\min\{\exp(O(q)),(q+1)^{O(\varepsilon^{-1}\log(2+r/\varepsilon))}\}\mathrm{poly}(b_\varepsilon+\log P).
-->
![Formula](../../assets/math/f11f263ea859ef2e2a4540e1.svg)

**Space**

Polynomial in the explicit graph, partition, and current blocker state.

**Parameters**

<code class="math">q</code> is the number of nonempty classes; <code class="math">r\ge2</code> bounds independent neighbours in distinct classes; <code class="math">0&lt;\varepsilon&lt;1</code> is rational; <code class="math">P=\lvert V\rvert+\lvert E\rvert+q+2</code>; <code class="math">b_\varepsilon=\mathrm{size}(\varepsilon)</code>.

**Model and representation**

A finite loopless graph with a given vertex partition and no vertex having <code class="math">r</code> independent neighbours in distinct classes. The constellation is induced after deleting edges within classes.

**Lower-bound scope**

No complexity lower bound is claimed. A returned certificate refutes the stated domination condition; it need not rule out every independent transversal.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The qualitative certifying theorem and operations are due to [Graf and Haxell](https://arxiv.org/html/1811.02687v2). The proof gives the uniform parameter analysis and its certified stopping test.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
