# Spectral, norm, and regression summaries under correlated failures

One original-item subset with fixed weights serves every permitted label deletion. Pool and label-code constructions give different time/accuracy/failure-budget tradeoffs.

[Proof](proof.md) · [Sources](sources.md)

**Guarantee**

Simultaneous relative PSD, row-norm, loss, and whole-seminorm preservation, or the stated weak convex-regression solution guarantee. One successful event covers all queries.

**Objective and output**

Fixed nonnegative weights on original items, rows, edges, or top simplices. Weak regression preserves the original objective achieved by a sketched minimizer; it does not claim the same accuracy for every weighted objective value.

**Randomness**

Mixed. Importance pools are Monte Carlo with failure at most $\delta$; random-code variants have code failure at most $\zeta$, plus any ordinary sampler failure. One success event covers all allowed failures and later queries. Single-failure PSD/regression and coherence-code PSD alternatives are deterministic. Optimal arbitrary-seminorm support is existence only; its constructive alternative is Monte Carlo with the ordinary backend's high-probability guarantee and lifted-access assumptions.

**Time**

Pool constructions are uniformly polynomial after the full-input gate and require the stated ordinary importance routine. Label-code constructions are Monte Carlo plus an ordinary PSD/norm backend; deterministic coherence codes give a separate tradeoff. Optimal-support PSD bounds use polynomial arithmetic; the explicit rational bit implementation adds the indicated logarithm.

**Space**

The formulas below count retained support. Lifted matrices, codes, and elimination workspace are separate. Arbitrary seminorm construction requires lifted-sum evaluation and roundedness access.

**Parameters**

$r$ is original rank; $\Gamma=(h+d)^{h+d}/(h^h d^d)$, set to $1$ for $hd=0$; $Q=\sum_{j\le\min\{h,L\}}\binom{L}{j}$. $L$ is label count; $h$ is failure budget; $d$ is item-label degree. $\rho$ is fixed-background effective dimension.

**Model and representation**

Real PSD and norm models; rational data for the explicit polynomial-bit claims. Responses come from a supplied subspace. Graph/simplicial labels are sets, and repeated labels do not require a proper coloring.

**Lower-bound scope**

The robust importance multiplier is at least $\binom{h+d}{d}$; $d+1$ is sharp for $h=1$. Simple graph spectral summaries require $\Omega\!\left(n\binom{h+a+b}{a+b}/\epsilon^2\right)$ in the stated size regime. No optimal inverse-accuracy claim is made for the code upper bound.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete proof](proof.md) and [canonical manuscript map](sources.md).

## Results

**PSD importance pools**

**Retained support, capped by input size.** $O\!\left(\Gamma r\epsilon^{-2}\log(2rQ/\delta)\right)$

**Algorithm / guarantee.** Monte Carlo, failure at most $\delta$ for one simultaneous all-query/all-failure event; uniform polynomial time without failure enumeration

**One-label-failure PSD**

**Retained support, capped by input size.** $O\!\left((d+1)r\epsilon^{-2}\log(2r(L+1))\right)$

**Algorithm / guarantee.** Deterministic polynomial-bit construction

**Fixed PSD background**

**Retained support, capped by input size.** Replace $r$ by $\rho$; ambient dimension remains in the logarithm

**Algorithm / guarantee.** Monte Carlo pool construction with failure at most $\delta$; valid for every later background $R'\succeq R$

**General finite-query nonnegative losses, $K_0$ queries**

**Retained support, capped by input size.** $O\!\left(\Gamma S_0\epsilon^{-2}\log(2K_0Q/\delta)\right)$

**Algorithm / guarantee.** Monte Carlo, failure at most $\delta$; requires hereditary ordinary sensitivity bound/routine $S_0$

**$\ell_1$ row sums, pool construction**

**Retained support, capped by input size.** $O\!\left(\Gamma r\epsilon^{-2}\log(2NQ/\delta)\right)$

**Algorithm / guarantee.** Monte Carlo pool and Lewis-weight sampling, failure at most $\delta$; augmented supplied responses allowed

**Fixed $1<p<2$ row sums, pool construction**

**Retained support, capped by input size.**

$$
O_p\!\left(\Gamma r\epsilon^{-2}\left[(\log(2r))^3\log(2N)+\log(2NQ/\delta)\right]\right)
$$

**Algorithm / guarantee.** Monte Carlo pool and fixed-$p$ norm sampling, failure at most $\delta$

**One label per PSD item, code construction**

**Retained support, capped by input size.** $O(rK/\epsilon^2)$,

$$
K=1+\min\left\{L,O\!\left(\bigl[(h+1)\log(eL/(h+1))+\log(1/\zeta)\bigr]/\epsilon\right)\right\}
$$

**Algorithm / guarantee.** Monte Carlo code, failure at most $\zeta$ in $1\le h<L$, followed by deterministic polynomial-arithmetic PSD sparsification; identity-code branch deterministic

**One-label deterministic coherence code**

**Retained support, capped by input size.**

$$
O\!\left(r\epsilon^{-2}\min\left\{L+1,(h^2+h/\epsilon)\log(2L)+1\right\}\right)
$$

**Algorithm / guarantee.** Deterministic arithmetic; explicit bit version adds $\log(2rK)$

**At most $d$ labels per item, exterior code**

**Retained support, capped by input size.** $O(rK/\epsilon^2)$, $K=\sum_{j\le\min\{d,D\}}\binom{D}{j}$

**Algorithm / guarantee.** Monte Carlo code with failure at most $\zeta$, followed by deterministic PSD sparsification; $D$ as defined below, with fixed $d$ giving $h^d$ up to logarithms

**Graph vertex/edge label degrees $a,b$**

**Retained support, capped by input size.** $O_{a,b}\!\left(rh^{a+b}\log^{a+b}(2L)/\epsilon^{a+b+2}\right)$

**Algorithm / guarantee.** Monte Carlo code with fixed confidence, followed by deterministic PSD sparsification; fixed $a,b$, $h\ge a+b$; exact capped form in proof

**One vertex color, simplicial boundary**

**Retained support, capped by input size.**

$$
O\!\left(r\epsilon^{-2}\left[1+\min\left\{L,q\bigl[s\log(eL/s)+\log(2/\zeta)\bigr]/\epsilon\right\}\right]\right)
$$

**Algorithm / guarantee.** Monte Carlo code with failure at most $\zeta$, followed by deterministic PSD sparsification; $q$ distinct colors per top simplex, $s=\min\{L,h+q\}$; lower skeleton retained

**Weak convex regression, importance pools**

**Retained support, capped by input size.** $O\!\left(\Gamma\rho\epsilon^{-1}\log(2(p+q)Q/\delta)\right)$

**Algorithm / guarantee.** Monte Carlo, failure at most $\delta$ for all later responses in the supplied subspace, $\lambda\ge\lambda_0$, convex constraints and nonnegative convex penalties

**One-failure weak convex regression**

**Retained support, capped by input size.** $O\!\left((d+1)\rho\epsilon^{-1}\log(2(p+q)(L+1))\right)$

**Algorithm / guarantee.** Deterministic polynomial-bit construction

**One-label weak regression, code route**

**Retained support, capped by input size.** $O\!\left(\rho D\epsilon^{-1}\log(2nD)\right)$,

$$
D=O\!\left(\bigl[(h+1)\log(eL/(h+1))+\log(1/\zeta)\bigr]/\sqrt{\epsilon}\right)
$$

**Algorithm / guarantee.** Monte Carlo code with failure at most $\zeta$ when the deterministic lifted PSD routine is used; linear $h$, $\epsilon^{-3/2}$ up to displayed logs; identity branch needs background padding

**Whole seminorm blocks, existential**

**Retained support, capped by input size.** $O(rK/\epsilon^2)$

**Algorithm / guarantee.** Existence only at this support bound; choosing deterministic label features does not supply a deterministic optimal seminorm construction

**Whole seminorm blocks, constructive backend**

**Retained support, capped by input size.** $O\!\left(\epsilon^{-2}R\log(2R/\epsilon)[\log(2R)]^{5/2}\right)$, $R\le rK$

**Algorithm / guarantee.** Monte Carlo with the ordinary seminorm backend's high-probability guarantee, plus code failure $\zeta$ if a random code is used; requires lifted-sum evaluation and roundedness access

For the general exterior code, let $s=\min\{h+d,L\}$ and use the actual rounded dimension
$$
D=\min\left\{L,
\left\lceil\frac{Cd}{\epsilon}
\left[s\log(eL/s)+\log(2/\zeta)\right]\right\rceil
\right\}.
$$

If the cap chooses $L$, use the identity code. Compute the final support target before materializing features; if it reaches the input size, return the original input. The exact arithmetic support bound $O(rK/\epsilon^2)$ has an explicit polynomial-bit implementation with an additional $\log(2rK)$ factor. The sample-confidence and code-confidence probabilities are separate when both stages are randomized.

For regression, $\rho\le\mathrm{sd}_{\lambda_0}(A)+q$, where $q$ is the supplied response-subspace dimension. The pool route has better inverse-accuracy dependence, while the code route has better failure-budget dependence in some regimes; neither uniformly dominates the other.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
