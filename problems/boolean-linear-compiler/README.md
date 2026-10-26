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

$`T_B\le\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha n+Q-(1-\alpha)B}`$, $`0\le B\le Q`$. Branch count is at most $`\left(\prod_i p_i\right)2^{Q-B}`$, not necessarily equal to that bound.

**Space**

If the same backend has writable space $`\mathrm{poly}(L')2^{\sigma N}`$, then $`S_B\le\mathrm{poly}(L)2^{\sigma(n+B)}`$. No space bound is inferred from a time-only backend.

**Parameters**

$`s_i`$ is row support; $`W_i=u_i-\ell_i`$; $`\kappa_i=\min\{W_i+1,5s_i+1\}`$; $`q_i=\lceil\log_2\kappa_i\rceil`$; $`Q=\sum_iq_i`$. Catalogue sizes satisfy $`p_i\le4\lceil\log_2(W_i+1)\rceil+1`$, with $`p_i=1`$ when $`W_i\le5s_i`$. $`L`$ is full binary input length.

**Model and representation**

Boolean variables; signed binary coefficients, endpoints, and objectives; a deterministic Subset Sum backend with the stated indexed-witness contract. Exact equalities affect $`L`$ but contribute no slack parameter.

**Lower-bound scope**

No universal dominance or lower bound is claimed. Signed interval rounding is inherited from the cited literature; the theorem isolates short-interval/slack interpolation and exact accounting.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**$`B=0`$**

**Time.** $`\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha n+Q}`$

**Writable space, when supplied by the backend.** $`\mathrm{poly}(L)2^{\sigma n}`$

**Any $`0\le B\le Q`$**

**Time.** $`\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha n+Q-(1-\alpha)B}`$

**Writable space, when supplied by the backend.** $`\mathrm{poly}(L)2^{\sigma(n+B)}`$

**$`B=Q`$**

**Time.** $`\mathrm{poly}(L)\left(\prod_i p_i\right)2^{\alpha(n+Q)}`$

**Writable space, when supplied by the backend.** $`\mathrm{poly}(L)2^{\sigma(n+Q)}`$

**Fixed number of interval constraints**

**Time.** $`\mathrm{poly}(L)2^{\alpha n}`$

**Writable space, when supplied by the backend.** $`\mathrm{poly}(L)2^{\sigma n}`$

**Meet-in-the-middle / low-space backend $`\alpha=1/2`$**

**Time.** $`\mathrm{poly}(L)\left(\prod_i p_i\right)2^{n/2+Q-B/2}`$

**Writable space, when supplied by the backend.** Use the space contract of the selected backend

Numerical repository instantiations are stated in the [complete manuscript](manuscripts/boolean-linear-optimization-compiler.md). The fast-time theorem and the distinct low-space theorem supply separate algorithmic points.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
