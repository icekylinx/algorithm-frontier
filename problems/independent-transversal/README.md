# Independent transversals with explicit obstruction certificates

**Guarantee**

Returns an independent transversal, or a class set $S$, a total dominating set $D$, and a constellation $K$ with $V(K)\subseteq D$, $\lvert D\rvert<(2+\varepsilon)(\lvert S\rvert-1)$, and $\lvert D\setminus V(K)\rvert<\varepsilon(\lvert S\rvert-1)$.

**Objective and output**

Select one vertex from each class with no selected edge, or output the stated directly checkable domination and constellation objects.

**Randomness**

Deterministic certifying construction, including the elementary exponential fallback; arbitrary choices use fixed tie rules.

**Time**

$$
P\min\{\exp(O(q)),(q+1)^{O(\varepsilon^{-1}\log(2+r/\varepsilon))}\}\mathrm{poly}(b_\varepsilon+\log P).
$$

**Space**

Polynomial in the explicit graph, partition, and current blocker state.

**Parameters**

$q$ is the number of nonempty classes; $r\ge2$ bounds independent neighbours in distinct classes; $0<\varepsilon<1$ is rational; $P=\lvert V\rvert+\lvert E\rvert+q+2$; $b_\varepsilon=\mathrm{size}(\varepsilon)$.

**Model and representation**

A finite loopless graph with a given vertex partition and no vertex having $r$ independent neighbours in distinct classes. The constellation is induced after deleting edges within classes.

**Lower-bound scope**

No complexity lower bound is claimed. A returned certificate refutes the stated domination condition; it need not rule out every independent transversal.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The qualitative certifying theorem and operations are due to [Graf and Haxell](https://arxiv.org/html/1811.02687v2). The proof gives the uniform parameter analysis and its certified stopping test.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
