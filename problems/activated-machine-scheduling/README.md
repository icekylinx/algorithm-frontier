# Scheduling with an activated machine basis

**Guarantee**

Returns an actual activated basis and a complete legal schedule; offers factor $1+\varepsilon$, exact factor $3/2$, and the bucket curve $\gamma_k=\frac{3\cdot2^k-1}{2^{k+1}-1}$. Detects global infeasibility.

**Objective and output**

Minimize maximum load subject to all original job totals and one exact combined setup and assignment budget.

**Randomness**

Deterministic enumeration of activation bases and profiles, followed by exact feasibility and recovery tests.

**Time**

Let $\delta=\varepsilon/2$, $K=\lfloor1/\delta\rfloor$, $L=\left\lceil(1-\delta)/\delta^2\right\rceil$, and $\Pi_\varepsilon=\min\{\binom{L+K}{K},\exp(3(K+1))\}$. The three bounds are $\binom{q}{r}\Pi_\varepsilon^r\mathrm{poly}(H_\varepsilon)$, $\binom{q}{r}6^r\mathrm{poly}(H)$, and $\binom{q}{r}(k+1)^r\mathrm{poly}(H+k)$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The full rational accuracy encoding is charged.

**Parameters**

$q$ is the physical-machine count; $r$ is the activation-matroid rank; $\varepsilon$ is rational with $0<\varepsilon\le1$; $k\ge0$ is an integer. $H_\varepsilon=H+\mathrm{size}(\varepsilon)$. Original totals are $n_j=f_j(P)$.

**Model and representation**

Arbitrary nonnegative machine-type processing times, integral job polymatroids, an actual machine-matroid basis, nonnegative setup and assignment costs, eligibility masks, and one shared exact budget.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The rank-sensitive enumeration first chooses an actual activated basis, then profiles only its $r$ machines. Original job totals stay mandatory after restriction; an affordable setup basis alone does not certify scheduling feasibility.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
