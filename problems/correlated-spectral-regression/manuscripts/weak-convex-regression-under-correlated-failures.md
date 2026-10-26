# Correlated-failure coresets for convexly regularized least squares with linear inverse-accuracy dependence

## Scope

This is a corollary of the correlated-failure PSD importance and sparsification theorem in [correlated-failure-spectral-and-regression-summaries.md](correlated-failure-spectral-and-regression-summaries.md). The contribution is simultaneous tolerance of specified, potentially large and overlapping, label failures with one common subset of original rows and one common set of weights. The conversion from a square-root-accuracy embedding to a relative-error least-squares solution is classical; below we record its elementary form for arbitrary convex constraints and nonnegative convex penalties. No priority claim is made for nonrobust ridge regression, lasso, effective-dimension sampling, or this optimization conversion.

The guarantee is a weak coreset guarantee: a minimizer of the weighted surviving regression problem gives a near-optimal solution on the original surviving data. The weighted objective value itself is only preserved to the embedding accuracy, which is proportional to the square root of the requested solution error.

## Theorem

Let A be an N-by-p real matrix. Let B be an N-by-q matrix specifying a supplied response subspace; one may remove dependent columns and assume rank(B)=q. Each row e carries a set Λ(e) of at most d failure labels from an explicitly given universe of L occurring labels. For F with |F|≤h, write

```math
E_F=\{e:\Lambda(e)\cap F=\varnothing\},\qquad
 Q=\sum_{j=0}^{\min\{h,L\}}\binom Lj.
```

Clip h at L and d at the actual maximum label-set size. Define

```math
\Gamma(h,d)=\frac{(h+d)^{h+d}}{h^h d^d}
```

when h,d>0, and set Γ=1 if either parameter is zero. Fix λ_0≥0 and set C=[A B],

```math
R_0=\begin{pmatrix}\lambda_0 I_p&0\\0&0_q\end{pmatrix},
 \qquad
 \rho=\mathrm{tr}\left(C^TC(C^TC+R_0)^\dagger\right).
\tag{1}
```

For ε,δ in (0,1), there is a randomized uniformly polynomial-time construction of a row subset H and fixed nonnegative weights ω_e, of size

```math
O\!\left(\min\left\{N,
  \frac{\Gamma(h,d)\rho}{\epsilon}
  \log\frac{2(p+q)Q}{\delta}\right\}\right),
\tag{2}
```

with the following simultaneous guarantee, with probability at least 1−δ. Choose any allowed F, any λ≥λ_0, any response matrix Y=BT with any finite number of columns, any convex feasible set K of coefficient matrices, and any convex penalty g:K→[0,∞). Every attained minimizer \widehat X over X∈K of

```math
\sum_{e\in H\cap E_F}\omega_e\|a_e^T X-y_e^T\|_2^2
  +\lambda\|X\|_F^2+g(X)
\tag{3}
```

satisfies

```math
\|A_{E_F}\widehat X-Y_{E_F}\|_F^2
  +\lambda\|\widehat X\|_F^2+g(\widehat X)
 \le(1+\epsilon)
  \inf_{X\in K}\{\|A_{E_F}X-Y_{E_F}\|_F^2+\lambda\|X\|_F^2+g(X)\}.
\tag{4}
```

The same H and weights work for all these choices, including choices of K and g made after inspecting the summary. No additional union bound over λ, T, K, or g is needed. The lower endpoint λ_0 and the supplied response subspace must be fixed before preprocessing. Examples include nonnegative least squares, simplex or box constraints, lasso and generalized lasso, elastic net, and nuclear-norm penalties on matrix coefficients. Convexity and nonnegativity of the added penalty are explicit assumptions; arbitrary discrete constraints or nonconvex penalties are not covered by this precision bound.

The quantity in (1) obeys

```math
\rho\le\mathrm{sd}_{\lambda_0}(A)+q,
 \qquad
 \mathrm{sd}_{\lambda}(A)
   =\mathrm{tr}\bigl(A^TA(A^TA+\lambda I)^\dagger\bigr).
\tag{5}
```

For h=1, there is a deterministic polynomial-time construction of size

```math
O\!\left(\min\left\{N,
 \frac{(d+1)\rho}{\epsilon}
 \log\bigl(2(p+q)(L+1)\bigr)\right\}\right).
\tag{6}
```

In particular, a fixed response vector costs at most one additional effective dimension. For λ_0=0, one may use the sharper expression ρ=rank([A B]). Rational-input statements have their usual polynomial bit-complexity interpretation, using the finite-precision derandomization in the spectral manuscript. A zero-dimensional input or ρ=0 is handled by the empty summary.

## 1. The PSD-background extension needed here

The spectral manuscript initially writes fixed regularization as R≻0. Its proof extends to any R≽0. For X⊆E and e∈X, use

```math
t_e^R(X)=\mathrm{tr}\bigl(B_e(R+M_X)^\dagger\bigr),
 \qquad M_X=\sum_{e\in X}B_e.
```

Apply the positive-definite version with R+ζI and let ζ decrease to zero. Since range(B_e)⊆range(M_X)⊆range(R+M_X), each trace converges to this finite pseudoinverse trace. Thus deletion monotonicity, the hereditary total bound, the Γ pool argument, and the exact h=1 accounting all remain valid. Their total bound is

```math
d_R=\mathrm{tr}\bigl(M_E(R+M_E)^\dagger\bigr).
```

Concentration and derandomization whiten range(R+M_{E_F}) separately for each scenario. All item matrices and the background vanish on its orthogonal complement, so rank changes cause no extra error. The cap at the full input size and the small-effective-dimension precheck from the spectral manuscript remain valid. This proves the PSD version, not just a limiting existential statement about output weights.

Apply that result to B_e=c_ec_e^T, where c_e is the transpose of row e of C, and background R_0. With embedding accuracy η∈(0,1), it gives simultaneously for all F

```math
(1-\eta)(C_{E_F}^TC_{E_F}+R_0)
 \preceq
 C_{H\cap E_F}^T W C_{H\cap E_F}+R_0
 \preceq
 (1+\eta)(C_{E_F}^TC_{E_F}+R_0).
\tag{7}
```

Adding diag((λ−λ_0)I_p,0) preserves (7), with R_0 replaced by diag(λI_p,0), for every λ≥λ_0. Congruence under diag(I_p,T) gives the analogous statement for responses Y=BT. Thus all these later choices are covered by the one event in (7).

## 2. A quadratic-optimization lemma with arbitrary convex penalties

Fix F, λ and Y, and use the augmented ordinary least-squares matrices

```math
\bar A=\begin{pmatrix}A_{E_F}\\\sqrt\lambda I_p\end{pmatrix},
 \qquad
 \bar Y=\begin{pmatrix}Y_{E_F}\\0\end{pmatrix}.
```

Let S scale/select the data rows according to the common surviving summary and leave the regularization rows untouched. Statement (7) means that S preserves all squared norms in col([\bar A\ \bar Y]) within 1±η. Therefore its bilinear error satisfies

```math
|\langle Su,Sv\rangle-\langle u,v\rangle|
  \le\eta\|u\|_2\|v\|_2
\tag{8}
```

for all u,v in that column space. This follows by representing S^TS−I on an orthonormal basis of the space and using its operator norm bound η.

Fix any feasible comparator X_* with finite objective. It need not be an optimizer. Set

```math
\Delta=\widehat X-X_*,\qquad
 U=\bar A\Delta,\qquad
 V=\bar A\widehat X-\bar Y.
```

For 0<t≤1, the point X_t=\widehat X−tΔ is feasible. Optimality of \widehat X and convexity of g imply

```math
0\le
 -2t\langle SU,SV\rangle_F+t^2\|SU\|_F^2
 +t\bigl(g(X_*)-g(\widehat X)\bigr).
```

Divide by t and let t decrease to zero. This gives

```math
2\langle SU,SV\rangle_F
 \le g(X_*)-g(\widehat X).
```

Thus, writing f(X)=\|\bar AX−\bar Y\|_F^2+g(X),

```math
\begin{aligned}
 f(\widehat X)-f(X_*)
 &=2\langle U,V\rangle_F-\|U\|_F^2
   +g(\widehat X)-g(X_*)\\
 &\le2\bigl(\langle U,V\rangle_F-\langle SU,SV\rangle_F\bigr)
       -\|U\|_F^2\\
 &\le2\eta\|U\|_F\|V\|_F-\|U\|_F^2\\
 &\le\eta^2\|V\|_F^2
 \le\eta^2 f(\widehat X).
 \end{aligned}
```

The penultimate inequality is 2ab−b^2≤a^2. The last uses g≥0. Consequently

```math
f(\widehat X)\le\frac{1}{1-\eta^2}f(X_*).
\tag{9}
```

Take the infimum over all finite feasible comparators. Choosing η^2=ε/(1+ε) proves (4), while η^{-2}=(1+ε)/ε proves the size bounds. This segment proof handles nonsmooth penalties without requiring a subgradient sum rule or a constraint qualification. It includes zero optimum and rank-deficient design matrices. An attained sketched minimum is the only optimization existence requirement. Because (8) holds uniformly on the supplied column space, the same argument applies to every subsequently chosen convex K and g on the single successful embedding event.

A penalty with a known lower bound ℓ can instead be replaced by g−ℓ; then the relative guarantee concerns the objective shifted by ℓ. No uniform relative claim for arbitrarily signed, unshifted penalties follows from (9).

## 3. The augmented effective-dimension bound

For λ_0=0, (5) is the elementary inequality rank([A B])≤rank(A)+rank(B).

Suppose λ_0>0. Put

```math
H=A^TA+\lambda_0 I_p,\qquad
 X_*=H^{-1}A^TB,\qquad U=B-AX_*,
```

and let

```math
V=B^TB-B^TAH^{-1}A^TB
   =U^TU+\lambda_0X_*^TX_*.
```

After dependent response columns have been removed, V is positive definite: it equals B^T[I−AH^{-1}A^T]B and the middle matrix is positive definite. The block inverse of C^TC+R_0 gives, for each row,

```math
c_e^T(C^TC+R_0)^{-1}c_e
  =a_e^TH^{-1}a_e+u_e^TV^{-1}u_e.
```

Summing and using U^TU≼V proves

```math
\rho=\mathrm{sd}_{\lambda_0}(A)
       +\mathrm{tr}(V^{-1/2}U^TUV^{-1/2})
       \le\mathrm{sd}_{\lambda_0}(A)+q.
```

The same formula also exposes why the response contribution is bounded even when its scale is large. The response subspace, rather than the number of separately queried response matrices, controls this term.

## Baseline and interpretation

Kacham–Woodruff, AISTATS 2020, Theorem 1.1 already constructs deterministic nonrobust weak ridge-regression coresets with O((sd_λ(A)+q)/ε) rows, without the logarithmic factor above, and proves corresponding nonrobust lower bounds. Calandriello–Koutis–Lazaric–Valko, ICML 2018, develops the nonrobust ridge spectral sparsification viewpoint. These results are credited ingredients and baselines.

The present increment supplies a single common row subset for every specified correlated label deletion. For one failed label and constant label degree d, its size is independent of the number of rows in the failed class and depends only logarithmically on the number L of possible classes. It also covers an entire regularization path, a supplied response subspace, and later convex constraints and nonnegative convex penalties. For arbitrary h, keep log Q explicit: it may itself be of order h log L, and is not a polylogarithmic dependence on h.

There is extensive prior work on nonrobust constrained and regularized least-squares sketching. Boutsidis–Drineas–Magdon-Ismail treats arbitrary constrained regression, including nonconvex constraints, and gives deterministic coresets. Chhaya–Dasgupta–Shit studies strong coresets for regularized regression. Yang–Li, ICLR 2025, studies sketches and iterative algorithms for convex/nonconvex regularization; its displayed sketched objective retains the original linear term and its principal guarantees concern solution/estimation error. None of these citations is being used as evidence for a new nonrobust lasso claim here. The scope to compare is simultaneous correlated deletion with a common subset of original rows and common weights.

The theorem does not supply deletion privacy or machine-unlearning guarantees; it is a simultaneous optimization-preservation statement. Broader priority of correlated-failure regression coresets has not been established here.

### Primary sources

1. Praneeth Kacham and David P. Woodruff. *Optimal Deterministic Coresets for Ridge Regression*. AISTATS 2020, Theorem 1.1. https://proceedings.mlr.press/v108/kacham20a/kacham20a.pdf
2. Daniele Calandriello, Ioannis Koutis, Alessandro Lazaric, Michal Valko. *Improved Large-Scale Graph Learning through Ridge Spectral Sparsification*. ICML 2018. https://proceedings.mlr.press/v80/calandriello18a/calandriello18a.pdf
3. Michael B. Cohen, Jelani Nelson, David P. Woodruff. *Optimal Approximate Matrix Product in Terms of Stable Rank*. ICALP 2016. Standard subspace-embedding and bilinear-error background. https://people.eecs.berkeley.edu/~minilek/publications/papers/stable_ammv2.pdf
4. Christos Boutsidis, Petros Drineas, Malik Magdon-Ismail. *Near-optimal Coresets for Least-Squares Regression*. IEEE Transactions on Information Theory, 2013. https://arxiv.org/pdf/1202.3505
5. Rachit Chhaya, Anirban Dasgupta, Supratim Shit. *On Coresets for Regularized Regression*. ICML 2020. https://proceedings.mlr.press/v119/chhaya20b/chhaya20b.pdf
6. Yingzhen Yang and Ping Li. *Sketching for Convex and Nonconvex Regularized Least Squares with Sharp Guarantees*. ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/file/1d769a56c0fd47b03cfa491bdc3be9ba-Paper-Conference.pdf
