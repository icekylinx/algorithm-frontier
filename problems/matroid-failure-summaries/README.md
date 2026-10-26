# Sharp matroid and submodular failure summaries

Exact binomial-size restrictions under correlated label failures, with a sharp weighted oracle endpoint and an explicit representation boundary.

[Proof](proof.md) · [Sources](sources.md)

**Guarantee**

For $C=\binom{h+d}{d}$, represented matroids preserve every surviving fixed-cost prefix with at most $\min\{N,rC\}$ items. Arbitrary matroids preserve surviving rank with the same bound. For one failed label, arbitrary oracle matroids also admit the sharp weighted bound $(d+1)r$ in uniform polynomial time. For two or more failures, an explicit nonrepresentable family rules out the same weighted binomial bound.

**Objective and output**

Original-element restrictions; canonical minimum-cost surviving bases and all cost prefixes, with different size bounds for represented and arbitrary oracle matroids; exact surviving ranks and integer-submodular values for arbitrary failure budgets.

**Randomness**

Deterministic exact constructions. Random permutations and Bernoulli failures appear only in output-size proofs; no query sampling or probability of error.

**Time**

Represented: uniform deterministic polynomial preprocessing, with $O(ND^2)$ field operations for elimination at gated dimension $D=rC$, plus feature construction and rank compression. Arbitrary weighted oracle: at most $N(K+1)\sum_{i=0}^{h}(dr)^i$ independence queries, where $K=\min\{N,\lfloor r\Gamma(h,d)\rfloor\}$ and $\Gamma(h,d)=(h+d)^{h+d}/(h^h d^d)$, taking $\Gamma=1$ if $hd=0$. A final reverse-deletion pass attains the sharp rank-only size within $(N+K)(K+1)\sum_{i=0}^{h}(dr)^i$ queries, linear in $N$ for fixed parameters. Weighted oracle, $h=1$: at most $(1+dr)N$ queries. Integral values have the analogous bound with rank replaced by the numerical range $R$.

**Space**

Output counts original IDs. The $O(D^2)$ elimination workspace and oracle representation are separate. The bounded-depth oracle searches use polynomial input workspace after clipping the failure budget to the explicit label universe. No bit-kernel bound for arbitrary oracles is asserted.

**Parameters**

$N$ is element count; $r$ is rank; $h$ is failed-label budget; $d$ is actual maximum labels per item; $L$ is the explicit label universe; $R$ is the numerical submodular value range.

**Model and representation**

Rational or explicit finite-field columns for the general weighted-prefix theorem. Independence oracles suffice for arbitrary-budget rank preservation and weighted-prefix preservation with the larger W–LF factor; one failure attains the sharp factor. Value oracles supply integer-valued monotone submodular functions.

**Lower-bound scope**

The $rC$ and $RC$ retained-size bounds are exact in the worst case via labeled parallel classes or coverage functions. The weighted one-failure oracle bound is also sharp. For every $h\ge2$, a rank-four one-label-per-item oracle matroid forces $4(h+1)+1$ items to preserve exact optimum costs, exceeding $rC=4(h+1)$. This is a retained-support obstruction, not an oracle-query hardness claim.

**Review status**

**Ready for review.** Main Theorems 1–5: represented prefix lift; sharp oracle-rank and integral-value constructions; sharp one-failure weighted endpoint; explicit weighted obstruction; deterministic arbitrary-budget prefix construction. The two-stage rank construction has linear input dependence for fixed parameters.

**Conditions and remaining work.** Oracle results require the stated independence or value oracle; they bound retained original items, not an encoding of an arbitrary oracle. The exact general weighted-oracle optimum size beyond one failure is not determined. Finite programs complement the written proofs and do not constitute formal verification.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**Represented fixed-cost matroid summary**

**Exact bound.** $\min\left\{N,r\binom{h+d}{d}\right\}$ items

**Construction / interpretation.** Uniform deterministic polynomial preprocessing

**Arbitrary-matroid weighted summary for one failed label**

**Exact bound.** $\min\{N,(d+1)r\}$ items

**Construction / interpretation.** At most $(1+dr)N$ independence queries; canonical bases and every cost prefix are preserved, including rank drops.

**Arbitrary-matroid weighted summary for any failure budget**

**Exact upper bound.** $\min\{N,\lfloor r\Gamma(h,d)\rfloor\}$ items

**Construction / interpretation.** The unique smallest preserver of every prefix of one fixed order, computed in deterministic FPT oracle time. The size factor is the existing W–LF baseline; the [complete construction](manuscripts/weighted-oracle-prefix-fpt-construction.md) gives the explicit algorithm and query bound.

**Arbitrary-matroid rank summary**

**Exact bound.** $r\binom{h+d}{d}$ items

**Construction / interpretation.** Deterministic FPT construction with linear input dependence for fixed $r,h,d$; the direct $N(N+1)\sum_{i=0}^{h}(dr)^i$ construction remains an alternative.

**Integral monotone-submodular failure-value summary**

**Exact bound.** $R\binom{h+d}{d}$ items

**Construction / interpretation.** Deterministic FPT in $R+h+d$; $R=f(E)-f(\varnothing)$

**Worst surviving final-marginal sum**

**Exact bound.** $\sum_e\sigma_e\le\binom{h+d}{d}\,[f(E)-f(\varnothing)]$

**Construction / interpretation.** Real-valued monotone submodular $f$; sharp

**Correlated-erasure conditional entropy**

**Exact bound.** $\sum_e\max_F H(X_e\mid X_{E_F\setminus\{e\}})\le\binom{h+d}{d}H(X_E)$

**Construction / interpretation.** Finite joint Shannon entropy; sharp

**Represented completion and mergeability**

**Exact bound.** Same $r\binom{h+d}{d}$ size

**Construction / interpretation.** Fixed original linear representation and common feature assignment; arbitrary later matroid extensions preserve the original restriction

**Weighted oracle obstruction from two failures onward**

**Necessary size.** $r(h+1)+r/4$ for $d=1$, $h\ge2$ and ranks divisible by four

**Construction / interpretation.** An explicit 13-item rank-four example, then parallel extensions and direct sums. The [complete failure table and proof](manuscripts/weighted-oracle-two-failure-obstruction.md) are independently reproducible.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
