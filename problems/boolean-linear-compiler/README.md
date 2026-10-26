# Exact Boolean linear optimization compiler

A support-sensitive interval/slack reduction transfers a supplied indexed-witness Subset Sum backend to signed Boolean feasibility and optimization.

[Proof](proof.md) · [Sources](sources.md)

**Guarantee**

Exact feasibility, indexed witness recovery, and linear or explicitly listed polynomial-size lexicographic optimization for any number of signed equalities and signed interval rows.

**Objective and output**

An original Boolean vector satisfying every row and attaining the requested optimum, or an infeasibility answer.

**Randomness**

Deterministic compiler with a supplied deterministic indexed-witness Subset Sum backend; optimization, witnesses and the stated space transfer retain that same backend contract.

**Time**

<code class="math">T_B\le\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha n+Q-(1-\alpha)B}</code>, <code class="math">0\le B\le Q</code>. Branch count is at most <code class="math">\left(\prod_i p_i\right)2^{Q-B}</code>, not necessarily equal to that bound.

**Space**

If the same backend has writable space <code class="math">\mathrm{poly}(L')2^{\sigma N}</code>, then <code class="math">S_B\le\mathrm{poly}(L)2^{\sigma(n+B)}</code>. No space bound is inferred from a time-only backend.

**Parameters**

<code class="math">s_i</code> is row support; <code class="math">W_i=u_i-\ell_i</code>; <code class="math">\kappa_i=\min\{W_i+1,5s_i+1\}</code>; <code class="math">q_i=\lceil\log_2\kappa_i\rceil</code>; <code class="math">Q=\sum_iq_i</code>. Catalogue sizes satisfy <code class="math">p_i\le4\lceil\log_2(W_i+1)\rceil+1</code>, with <code class="math">p_i=1</code> when <code class="math">W_i\le5s_i</code>. <code class="math">L</code> is full binary input length.

**Model and representation**

Boolean variables; signed binary coefficients, endpoints, and objectives; a deterministic Subset Sum backend with the stated indexed-witness contract. Exact equalities affect <code class="math">L</code> but contribute no slack parameter.

**Lower-bound scope**

No universal dominance or lower bound is claimed. Signed interval rounding is inherited from the cited literature; the theorem isolates short-interval/slack interpolation and exact accounting.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**<code class="math">B=0</code>**

**Time.** <code class="math">\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha n+Q}</code>

**Writable space, when supplied by the backend.** <code class="math">\mathrm{poly}(L)2^{\sigma n}</code>

**Any <code class="math">0\le B\le Q</code>**

**Time.** <code class="math">\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha n+Q-(1-\alpha)B}</code>

**Writable space, when supplied by the backend.** <code class="math">\mathrm{poly}(L)2^{\sigma(n+B)}</code>

**<code class="math">B=Q</code>**

**Time.** <code class="math">\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha(n+Q)}</code>

**Writable space, when supplied by the backend.** <code class="math">\mathrm{poly}(L)2^{\sigma(n+Q)}</code>

**Fixed number of interval constraints**

**Time.** <code class="math">\mathrm{poly}(L)2^{\alpha n}</code>

**Writable space, when supplied by the backend.** <code class="math">\mathrm{poly}(L)2^{\sigma n}</code>

**Meet-in-the-middle / low-space backend <code class="math">\alpha=1/2</code>**

**Time.** <code class="math">\mathrm{poly}(L)\left(\prod_i p_i\right)2^{n/2+Q-B/2}</code>

**Writable space, when supplied by the backend.** Use the space contract of the selected backend

Numerical repository instantiations are stated in the [complete manuscript](manuscripts/boolean-linear-optimization-compiler.md). The fast-time theorem and the distinct low-space theorem supply separate algorithmic points.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
