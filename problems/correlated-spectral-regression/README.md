# Spectral, norm, and regression summaries under correlated failures

One original-item subset with fixed weights serves every permitted label deletion. Pool and label-code constructions give different time/accuracy/failure-budget tradeoffs.

[Proof](proof.md) · [Sources](sources.md)

| Field | Statement |
|---|---|
| **Guarantee** | Simultaneous relative PSD, row-norm, loss, and whole-seminorm preservation, or the stated weak convex-regression solution guarantee. One successful event covers all queries. |
| **Objective and output** | Fixed nonnegative weights on original items, rows, edges, or top simplices. Weak regression preserves the original objective achieved by a sketched minimizer; it does not claim the same accuracy for every weighted objective value. |
| **Time** | Pool constructions are uniformly polynomial after the full-input gate and require the stated ordinary importance routine. Label-code constructions are Monte Carlo plus an ordinary PSD/norm backend; deterministic coherence codes give a separate tradeoff. Optimal-support PSD bounds use polynomial arithmetic; the explicit rational bit implementation adds the indicated logarithm. |
| **Space** | The formulas below count retained support. Lifted matrices, codes, and elimination workspace are separate. Arbitrary seminorm construction requires lifted-sum evaluation and roundedness access. |
| **Parameters** | $r$ is original rank; $\Gamma=(h+d)^{h+d}/(h^h d^d)$, set to $1$ for $hd=0$; $Q=\sum_{j\le\min\{h,L\}}\binom{L}{j}$. $L$ is label count; $h$ is failure budget; $d$ is item-label degree. $\rho$ is fixed-background effective dimension. |
| **Model and representation** | Real PSD and norm models; rational data for the explicit polynomial-bit claims. Responses come from a supplied subspace. Graph/simplicial labels are sets, and repeated labels do not require a proper coloring. |
| **Lower-bound scope** | The robust importance multiplier is at least $\binom{h+d}{d}$; $d+1$ is sharp for $h=1$. Simple graph spectral summaries require $\Omega\!\left(n\binom{h+a+b}{a+b}/\epsilon^2\right)$ in the stated size regime. No optimal inverse-accuracy claim is made for the code upper bound. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Complete proof](proof.md) and [canonical manuscript map](sources.md). |

## Results

| Result / construction | Retained support, capped by input size | Algorithm / guarantee |
|---|---|---|
| PSD importance pools | $O\!\left(\Gamma r\epsilon^{-2}\log(2rQ/\delta)\right)$ | Randomized uniform polynomial; no failure enumeration |
| One-label-failure PSD | $O\!\left((d+1)r\epsilon^{-2}\log(2r(L+1))\right)$ | Deterministic polynomial-bit construction |
| Fixed PSD background | Replace $r$ by $\rho$; ambient dimension remains in the logarithm | Valid for every later background $R'\succeq R$ |
| General finite-query nonnegative losses, $K_0$ queries | $O\!\left(\Gamma S_0\epsilon^{-2}\log(2K_0Q/\delta)\right)$ | Requires hereditary ordinary sensitivity bound/routine $S_0$ |
| $\ell_1$ row sums, pool construction | $O\!\left(\Gamma r\epsilon^{-2}\log(2NQ/\delta)\right)$ | Classical Lewis-weight sampler; augmented supplied responses allowed |
| Fixed $1<p<2$ row sums, pool construction | $O_p\!\left(\Gamma r\epsilon^{-2}\left[(\log(2r))^3\log(2N)+\log(2NQ/\delta)\right]\right)$ | Separate fixed-$p$ norm theorem |
| One label per PSD item, code construction | $O(rK/\epsilon^2)$, $K=1+\min\left\{L,O\!\left(\bigl[(h+1)\log(eL/(h+1))+\log(1/\zeta)\bigr]/\epsilon\right)\right\}$ | Random code in $1\le h<L$; polynomial-arithmetic PSD step |
| One-label deterministic coherence code | $O\!\left(r\epsilon^{-2}\min\left\{L+1,(h^2+h/\epsilon)\log(2L)+1\right\}\right)$ | Deterministic arithmetic; explicit bit version adds $\log(2rK)$ |
| At most $d$ labels per item, exterior code | $O(rK/\epsilon^2)$, $K=\sum_{j\le\min\{d,D\}}\binom{D}{j}$ | $D$ as defined below; fixed $d$ gives $h^d$ up to logarithms |
| Graph vertex/edge label degrees $a,b$ | $O_{a,b}\!\left(rh^{a+b}\log^{a+b}(2L)/\epsilon^{a+b+2}\right)$ | Fixed $a,b$, $h\ge a+b$, fixed code confidence; exact capped form in proof |
| One vertex color, simplicial boundary | $O\!\left(r\epsilon^{-2}\left[1+\min\left\{L,q\bigl[s\log(eL/s)+\log(2/\zeta)\bigr]/\epsilon\right\}\right]\right)$ | $q$ distinct colors per top simplex; $s=\min\{L,h+q\}$; lower skeleton retained |
| Weak convex regression, importance pools | $O\!\left(\Gamma\rho\epsilon^{-1}\log(2(p+q)Q/\delta)\right)$ | All later responses in supplied subspace, $\lambda\ge\lambda_0$, convex constraints, nonnegative convex penalties |
| One-failure weak convex regression | $O\!\left((d+1)\rho\epsilon^{-1}\log(2(p+q)(L+1))\right)$ | Deterministic polynomial-bit construction |
| One-label weak regression, code route | $O\!\left(\rho D\epsilon^{-1}\log(2nD)\right)$, $D=O\!\left(\bigl[(h+1)\log(eL/(h+1))+\log(1/\zeta)\bigr]/\sqrt{\epsilon}\right)$ | Linear $h$, $\epsilon^{-3/2}$ up to displayed logs; identity branch needs background padding |
| Whole seminorm blocks, existential | $O(rK/\epsilon^2)$ | Same label features; ordinary optimal seminorm theorem |
| Whole seminorm blocks, constructive backend | $O\!\left(\epsilon^{-2}R\log(2R/\epsilon)[\log(2R)]^{5/2}\right)$, $R\le rK$ | Randomized; lifted-sum evaluation and roundedness access |

For the general exterior code, let $s=\min\{h+d,L\}$ and use the actual rounded dimension
$$
D=\min\left\{L,
\left\lceil\frac{Cd}{\epsilon}
\left[s\log(eL/s)+\log(2/\zeta)\right]\right\rceil
\right\}.
$$

If the cap chooses $L$, use the identity code. Compute the final support target before materializing features; if it reaches the input size, return the original input. The exact arithmetic support bound $O(rK/\epsilon^2)$ has an explicit polynomial-bit implementation with an additional $\log(2rK)$ factor. The sample-confidence and code-confidence probabilities are separate when both stages are randomized.

For regression, $\rho\le\operatorname{sd}_{\lambda_0}(A)+q$, where $q$ is the supplied response-subspace dimension. The pool route has better inverse-accuracy dependence, while the code route has better failure-budget dependence in some regimes; neither uniformly dominates the other.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
