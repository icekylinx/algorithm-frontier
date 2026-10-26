# Scheduling with arbitrary processing times

**Guarantee**

Returns an integer schedule of makespan at most $(1+\varepsilon)\mathrm{OPT}$, or detects infeasibility even without a load bound.

**Objective and output**

Assign every original type total while preserving one exact assignment-cost budget.

**Randomness**

Deterministic profile enumeration and exact integral recovery, including the compressed-slot-surplus branch, with paid deterministic primitives.

**Time**

With $\delta=\varepsilon/2$, $K=\lfloor1/\delta\rfloor$, $L=\left\lceil(1-\delta)/\delta^2\right\rceil$, and $\Pi_\varepsilon=\min\{\binom{L+K}{K},\exp(3(K+1))\}$, time is

$$
\Pi_\varepsilon^q\mathrm{poly}(H_\varepsilon)=2^{O(q/\varepsilon)}\mathrm{poly}(H_\varepsilon).
$$

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The rational accuracy is never expanded into unary coordinates.

**Parameters**

$q$ is the physical-machine count; $0<\varepsilon\le1$ is rational; $H_\varepsilon=H+\mathrm{size}(\varepsilon)$; all original totals $n_j=f_j(P)$ are mandatory. $H$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Arbitrary nonnegative rational processing times and assignment costs, integral job polymatroids, eligibility masks, and one exact budget. Every original resource base must be recovered.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

## A separate slot-surplus guarantee for common type sizes

The [compressed slot-surplus theorem](slot-surplus.md) handles common
processing sizes and mandatory original job-polymatroid bases, with
arbitrary binary multiplicities and no assignment-cost budget.
Let $a$ be the maximum size, $h$ its mandatory total, $u$ the largest
smaller size, and

$s_p(T)=\min\{f_b(\{p\}),\lfloor T/a\rfloor\}$,  $c_{\mathrm{slot}}(T)=\sum_p s_p(T)-h$.

**$C_{\max}\le\mathrm{OPT}+a$**

Always retained as a polynomial fallback

**$C_{\max}\le\min\{\mathrm{OPT}+a,(1+\varepsilon)\mathrm{OPT}+u\}$**

$\Gamma(1/\varepsilon)^k\mathrm{poly}(H)$ when $c_{\mathrm{slot}}(\mathrm{OPT})\le k$, for rational $0<\varepsilon\le1/2$

**Factor $1+\eta$**

$\Gamma(2/\eta)^k\mathrm{poly}(H)$ when $u\le(\eta/2)\mathrm{OPT}$ and $c_{\mathrm{slot}}(\mathrm{OPT})\le k$, for rational $0<\eta\le1$

Here $\Gamma(R)=R^R/(R-1)^{R-1}$. The supplied slot-surplus budget $k$
can itself be binary encoded. A hybrid count enumeration guarantees
polynomial workspace even when its numerical value exceeds the number
of machines. This theorem does not impose at most one largest unit per
machine, and its additive smaller-unit loss is explicit.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
