# Simultaneous spectral, norm, and regression summaries

## 1. Model

Each item has at most $d$ labels from an explicit universe of size $L$. A set $F$, $|F|\le h$, deletes every item meeting it. The output is one original-item subset with fixed nonnegative weights; every theorem holds for all allowed failures simultaneously. Define
$$
Q=\sum_{j=0}^{\min(h,L)}\binom Lj,\qquad
\Gamma(h,d)=\frac{(h+d)^{h+d}}{h^h d^d},
$$
with $\Gamma=1$ when $hd=0$. Retained support, preprocessing, and workspace are different resources.

## 2. Importance-pool theorem

Suppose masses $m_e(X)$ are nonnegative, increase when the containing set shrinks, and sum to at most $S$ on every set. Let $\sigma_e$ be the largest mass of $e$ after any allowed query where it survives.

**Lemma 2.1.** $\sum_e\sigma_e\le\Gamma S$.

**Proof.** Fix one maximizing failure witness $F_e$ per item. Put each label in a random pool independently with probability $\alpha=d/(h+d)$, and retain items whose entire own-label sets lie in the pool. The event that the pool contains $\Lambda(e)$ and avoids $F_e$ has probability at least $\alpha^d(1-\alpha)^h=1/\Gamma$. On that event the pool is a subset of $E_{F_e}$ containing $e$, so its mass is at least $\sigma_e$. Pointwise the sum of protected masses is at most $S$. Take expectations. $\square$

For PSD items $B_e$, use $m_e(X)=\operatorname{tr}(B_eM_X^\dagger)$, $M_X=\sum_{e\in X}B_e$. The total is $\operatorname{rank}M_X\le r$. Deletion monotonicity follows from the quadratic inverse variational identity on the range containing $B_e$; it requires no global ordering of pseudoinverses.

For one failed label, sum the nonnegative increases over all single-label scenarios. With $t_e=m_e(E)$ and surviving ranks $r_c$, the sum of per-item maxima is at most
$$
r+\sum_e|\Lambda(e)|t_e-\sum_c(r-r_c)\le(d+1)r.
$$
Orthogonal parallel copies indexed by label subsets make this factor sharp.

Take $J=O(\Gamma\log(NQ/\delta))$ independent pools and scores
$$
\widehat\sigma_e=m_e(E)+\frac{2\Gamma}{J}\sum_{j:e\in X_j}m_e(X_j).
$$
Chernoff and an item/failure-pair union bound give simultaneous domination with high probability. On every pool outcome, their total is at most $3\Gamma r$. An independent importance sample, followed by matrix concentration in each surviving range, therefore gives
$$
(1-\epsilon)M_F\preceq\widehat M_F\preceq(1+\epsilon)M_F
$$
for all failures with support
$$
O\left(\min\{N,\Gamma r\epsilon^{-2}\log(2rQ/\delta)\}\right).
$$
The full-input gate precedes oversized work. For $h=1$, explicitly compute the $L+1$ scenarios and use trace-exponential derandomization, obtaining deterministic polynomial-bit support $O((d+1)r\epsilon^{-2}\log(2r(L+1)))$, capped by $N$.

With fixed PSD background $R$, replace the rank mass by $\rho=\operatorname{tr}(M(R+M)^\dagger)$. Centered matrix Bernstein gives the corresponding regularized statement. It remains valid for every later background larger in PSD order.

## 3. Positive label-code decoder

Assign unit features $z_e\in\mathbb R^K$. Suppose each query has an orthogonal projector $P_F$ killing failed features and leaving survivor squared norms in $[1-\kappa,1]$. Sparsify $B_e\otimes z_ez_e^\top$ at accuracy $\theta$, in rank at most $rK$.

Congruence by $I\otimes P_F$, followed by partial trace, is positive and sends the item to $\alpha_e(F)B_e$. Thus the single lifted PSD inequality gives, for every failure,
$$
(1-\theta)(1-\kappa)M_F\preceq\widehat M_F
\preceq\frac{1+\theta}{1-\kappa}M_F.
$$
Taking $\theta=\epsilon/4$, $\kappa\le\epsilon/4$ proves relative error $\epsilon$ using $O(rK/\epsilon^2)$ items. Output weights never depend on the query.

For one label per item, a random sign code with restricted isometry on $h+1$ columns gives, when $1\le h<L$,
$$
K=1+\min\left\{L,O\left(\epsilon^{-1}
\left[(h+1)\log\frac{eL}{h+1}+\log\frac1\zeta\right]\right)\right\}.
$$
One successful code event covers all failures. No efficient test of optimal-dimensional restricted isometry is assumed.

For label degree $d$, use normalized exterior products in the graded space
$$
K=\sum_{j=0}^{\min(d,D)}\binom Dj,\quad
D=\min\left\{L,\left\lceil\frac{Cd}{\epsilon}
\left[s\log\frac{eL}{s}+\log\frac2\zeta\right]\right\rceil\right\},
\quad s=\min\{h+d,L\}.
$$
Projection kills failed wedges. Restricted isometry bounds squared loss on a live label span by $O(\epsilon/d)$; multiplying at most $d$ squared singular values gives $O(\epsilon)$ volume loss. Identity coding handles the cap, while explicit coherence codes give a separate deterministic tradeoff.

The optimal-support PSD backend is stated in the polynomial-arithmetic model. A specified rational polynomial-bit trace-exponential implementation adds $\log(2rK)$ to support.

## 4. Incidence compression

For an incidence matrix, let row labels satisfy $R_i\subseteq S_e$ at every nonzero entry, with deficit $|S_e\setminus R_i|\le k$ and full-column degree $|S_e|\le q$. Select $r$ independent original rows. In each selected block put the normalized exterior feature of the deficit with its wedge-insertion sign. The lift dimension is
$$
r\sum_{j=0}^{\min(k,D)}\binom Dj.
$$
At a query, append the projected row labels. Every incidence of a column now has the same full-column feature. Congruence, partial trace, and reconstruction of the original rows give the positive decoder above. The total degree $q$ controls code accuracy; the smaller deficit $k$ controls the lift exponent.

Graph vertex/edge list degrees $a,b$ have $k\le a+b$, $q\le2a+b$. For fixed $a,b$, fixed confidence, and $h\ge a+b$, the uncapped support is
$$
O_{a,b}\left(rh^{a+b}\log^{a+b}(2L)/\epsilon^{a+b+2}\right).
$$
A simplicial boundary with one color per vertex has $k=1$, including degree zero when the missing color already occurs on its facet. Its support is
$$
O\left(\min\left\{N,\frac r{\epsilon^2}
\left[1+\min\left\{L,\frac q\epsilon
\left(s\log\frac{eL}{s}+\log\frac2\zeta\right)\right\}\right]\right\}\right),
\quad s=\min\{L,h+q\}.
$$
These are fixed-weight spectral guarantees, separate from exact filtration-prefix preservation.

## 5. Weak convex regression

Augment design $A$ by supplied response basis $B$ and fixed background $R_0=\operatorname{diag}(\lambda_0I,0)$. The effective dimension satisfies $\rho\le\operatorname{sd}_{\lambda_0}(A)+\operatorname{rank}B$. Pool sparsification at embedding accuracy $\eta$ gives support $O(\Gamma\rho\eta^{-2}\log(2(p+q)Q/\delta))$.

Allow any later response in that subspace, $\lambda\ge\lambda_0$, convex feasible set, and nonnegative convex penalty $g$. Let $\widehat X$ attain the sketched minimum and $X_*$ be any feasible comparator. With regularization rows included, put $U=\bar A(\widehat X-X_*)$, $V=\bar A\widehat X-\bar Y$. Optimality along the feasible segment and the uniform bilinear error imply
$$
f(\widehat X)-f(X_*)\le
2\eta\|U\|_F\|V\|_F-\|U\|_F^2
\le\eta^2\|V\|_F^2\le\eta^2f(\widehat X).
$$
Hence $f(\widehat X)\le f(X_*)/(1-\eta^2)$. Choose $\eta^2=\epsilon/(1+\epsilon)$ and take the infimum over comparators. This proves the relative solution guarantee with $\epsilon^{-1}$ support dependence. An attained sketched minimizer and nonnegative penalty are explicit hypotheses. The one-label code route gives a separate linear-$h$, $\epsilon^{-3/2}$ tradeoff with its stated logarithms and background padding.

## 6. Losses, norms, and whole seminorm blocks

Ordinary nonnegative-loss sensitivity is deletion-monotone. A hereditary total bound $S_0$ transfers through Lemma 2.1. For $K_0$ finite queries, scalar concentration yields $O(\Gamma S_0\epsilon^{-2}\log(2K_0Q/\delta))$ support; infinite families need the chosen ordinary sampler's precise uniform-query theorem.

For row $p$-norms, apply the ordinary subset sampler to $a_e\otimes z_e$, then integrate its all-vector guarantee against a Gaussian of covariance $P_F$. A surviving factor is $\|P_Fz_e\|^p$, giving the same sandwich. The chosen sampler's rank dependence remains in force.

For arbitrary whole seminorm blocks, the Gaussian reduction and ordinary optimal seminorm theorem give existential $O(\min\{m,rK/\epsilon^2\})$ support. Construction instead needs evaluation and roundedness access to the lifted seminorm sum and inherits the larger constructive backend bound. Original-space access alone does not supply that interface.

## Complete proofs

[PSD importance](manuscripts/correlated-failure-spectral-and-regression-summaries.md); [general sensitivity](manuscripts/general-nonnegative-sensitivity-compiler.md); [convex regression](manuscripts/weak-convex-regression-under-correlated-failures.md); [label and norm lifts](manuscripts/label-vector-spectral-and-norm-lifts.md); [graph incidence](manuscripts/correlated-vertex-and-edge-failure-spectral-graphs.md); [simplicial incidence](manuscripts/graded-incidence-and-simplicial-spectral-sparsification.md); [whole seminorms](manuscripts/arbitrary-seminorms-under-correlated-failures.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
