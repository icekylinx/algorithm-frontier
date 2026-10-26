# Label-vector lifts for simultaneous correlated-failure spectral sparsification

## Theorems and computational models

This manuscript gives a label-code construction for the correlated-failure PSD problem. It lifts each item using a vector associated with its failure labels, performs one ordinary PSD sparsification in the lifted space, and decodes every failure scenario by an order-preserving linear map. Surviving items acquire nearly equal scalar factors; a final sandwich removes those factors without changing any output weights.

For one label per item, the randomized construction has support

```math
O\!\left(\min\left\{N,
 \frac{r}{\epsilon^3}
 \left[(h+1)\log\frac{eL}{h+1}+\log\frac1\zeta\right]\right\}\right)
\tag{A}
```

in the usual regime 1≤h<L, with an identity-code cap described below. Here N is the number of PSD items, r is the rank of their total, L is the number of occurring labels, h is the failure budget, ε is the spectral error, and ζ is the failure probability. This improves the h^2 dependence obtained by combining an O(hr) robust-importance bound with a union bound over all h-label deletions. It trades one factor ε^{-1} for that improvement. At fixed ε, the h dependence is optimal up to logarithms.

The short random code is a Monte Carlo construction. We do not claim a polynomial-time test of its restricted isometry property, or a deterministic construction with the same dimension. An explicit deterministic coherence construction instead gives support

```math
O\!\left(\min\left\{N,
 \frac{r}{\epsilon^2}\,
 \min\left\{L+1,\ (h^2+h/\epsilon)\log(2L)+1\right\}
 \right\}\right).
\tag{B}
```

Both displayed support bounds use the standard deterministic O(R/ε^2)-support PSD sparsification theorem in lifted rank R. They inherit its standard polynomial-arithmetic construction. A fully specified rational, polynomial-bit alternative replaces that subroutine by the trace-exponential derandomization described below and adds a factor log(2R). Thus the deterministic-code route also has an explicit deterministic polynomial-bit construction, with that extra logarithm. The coding and lifting parts themselves have polynomial rational bit complexity and are detailed below.

The same method extends to overlapping label sets of size at most d. Its support is O(rK/ε^2), where K=Σ_{j=0}^{min(d,D)}binom(D,j), D=O((d/ε)[s log(eL/s)+log(1/ζ)]), and s=min{h+d,L}, with D capped at L. For fixed d and ε, this has h^d dependence up to logarithms, improving the h^{d+1} dependence of the direct all-scenario concentration bound. A separate graph manuscript uses a smaller incidence-based lift for vertex colors; the generic overlapping-label bound here is not its best graph specialization.

## 1. Model and a positive decoding lemma

Let B_1,...,B_N be real symmetric positive-semidefinite matrices. Let

```math
M=\sum_e B_e,\qquad r=\mathrm{rank}M.
```

Work inside range(M), so the matrices have ambient dimension r. Each item has a label set Λ(e) of size at most d. For F⊆[L], |F|≤h, the survivors are E_F={e:Λ(e)∩F=∅}. The required output is a single subset H and nonnegative weights ω_e such that

```math
(1-\epsilon)\sum_{e\in E_F}B_e
 \preceq\sum_{e\in H\cap E_F}\omega_e B_e
 \preceq(1+\epsilon)\sum_{e\in E_F}B_e
\tag{1}
```

holds for every allowed F simultaneously. The weights do not depend on F.

Suppose each item is assigned a unit vector z_e in a K-dimensional auxiliary Euclidean space. Set

```math
\widetilde B_e=B_e\otimes z_ez_e^T,
 \qquad \widetilde M=\sum_e\widetilde B_e.
```

Suppose that for each F there is an orthogonal projector Q_F on the auxiliary space with

```math
\alpha_e(F)=\|Q_Fz_e\|_2^2
 =0 \text{ if }e\notin E_F,
 \qquad 1-\kappa\le\alpha_e(F)\le1 \text{ if }e\in E_F.
\tag{2}
```

Apply ordinary PSD sparsification at accuracy θ to obtain one set of weights with support O(rK/θ^2) and

```math
(1-\theta)\widetilde M
 \preceq\sum_e\omega_e\widetilde B_e
 \preceq(1+\theta)\widetilde M.
\tag{3}
```

For each F, apply the positive linear map

```math
\mathcal T_F(Z)=\mathrm{Tr}_{\rm aux}
   \bigl((I_r\otimes Q_F)Z(I_r\otimes Q_F)\bigr).
```

Partial trace preserves positive semidefiniteness: for an orthonormal auxiliary basis u_j,
x^T Tr_aux(Z)x=Σ_j(x⊗u_j)^T Z(x⊗u_j)≥0 whenever Z≽0. Also
T_F(\widetilde B_e)=α_e(F)B_e. Consequently (3) holds for the true and selected sums with coefficients α_e(F).

Let M_F=Σ_{e∈E_F}B_e and \widehat M_F=Σ_{e∈H∩E_F}ω_e B_e. From (2),

```math
(1-\theta)(1-\kappa)M_F
 \preceq\widehat M_F
 \preceq\frac{1+\theta}{1-\kappa}M_F.
\tag{4}
```

Choosing θ=ε/4 and κ≤ε/4 makes (4) imply (1) for 0<ε<1. The α_e(F) are used only in this proof. A query simply deletes the failed original items and keeps their preassigned weights.

## 2. Random label vectors: the one-label case

Assume d=1 and h≥1. Let s=min{h+1,L}. Use a sign matrix V with D rows and L columns, normalized so every column v_c has norm one. With probability at least 1−ζ, V has restricted isometry constant δ_0 on every subset of at most s columns, provided

```math
D\ge C\delta_0^{-2}
   \left[s\log\frac{eL}{s}+\log\frac2\zeta\right].
\tag{5}
```

This is the classical random-sign RIP theorem. For completeness, a fixed-vector concentration inequality is exp(−cDδ_0^2); a constant-radius net on each s-dimensional coordinate sphere has exp(O(s)) points; union over binom(L,s) supports gives (5). No enumeration of those supports is performed by the algorithm.

If the right side in (5) reaches L, use the identity code V=I_L instead. Its restricted isometry constant is zero and it is deterministic. Thus D can always be capped at L. An additional permanent orthogonal vector handles unlabeled items.

For a fault set F, let P_F be the orthogonal projector onto the complement of span{v_f:f∈F}. It kills each failed label vector. For c∉F, restricted isometry on F∪{c} implies

```math
\|V_F^Tv_c\|_2\le\delta_0,\qquad
 V_F^TV_F\succeq(1-\delta_0)I.
```

Therefore

```math
1-\|P_Fv_c\|_2^2
   =v_c^TV_F(V_F^TV_F)^{-1}V_F^Tv_c
   \le\frac{\delta_0^2}{1-\delta_0}.
\tag{6}
```

The empty F has zero loss. Select δ_0^2=ε/64; then the right side of (6) is at most ε/4. Take z_e=v_{c(e)}, or the permanent vector if e is unlabeled, and Q_F=P_F extended by identity on that permanent coordinate. The positive decoding lemma gives support O(r(D+1)/ε^2). Substituting (5) proves (A), with the more precise capped form

```math
O\!\left(\min\left\{N,
 \frac{r}{\epsilon^2}
 \left[1+\min\left\{L,
 \frac{C}{\epsilon}\left(s\log\frac{eL}{s}+\log\frac2\zeta\right)
 \right\}\right]\right\}\right).
\tag{7}
```

The one successful code event already quantifies over all F and all surviving labels. There is no subsequent union bound over fault scenarios. Both fault sets and tested vectors in (1) may be chosen after seeing the output.

## 3. Overlapping labels through a normalized exterior feature

Now let d≥1, h≥1, and s=min{h+d,L}. Choose a δ_0-RIP code on at most s real labels, with

```math
\delta_0^2=\frac{\epsilon}{64d},\qquad
 D=\min\left\{L,
 \left\lceil\frac{Cd}{\epsilon}\left(s\log\frac{eL}{s}+\log\frac2\zeta\right)\right\rceil\right\}.
\tag{8}
```

As before, use an identity code when the cap chooses D=L. Work in the graded exterior space

```math
\mathcal E_{\le d}=\bigoplus_{j=0}^{\min(d,D)}\bigwedge^j\mathbb R^D.
```

For an item with j=|Λ(e)| labels, put

```math
w_e=\bigwedge_{c\in\Lambda(e)}v_c,\qquad
 z_e=w_e/\|w_e\|_2
 \quad\text{in the degree-}j\text{ summand of }\mathcal E_{\le d}.
\tag{9}
```

The auxiliary dimension is

```math
K=\sum_{j=0}^{\min(d,D)}\binom Dj.
```

The empty label set uses the scalar unit vector in degree zero. On the successful code event, every w_e is nonzero. The chosen order of the wedge only changes its sign, which disappears in z_ez_e^T. No dummy labels or padding are needed.

For F, let P_F project away its label span, and set Q_F=\bigoplus_{j=0}^{\min(d,D)}\bigwedge^jP_F, with the identity map in degree zero. This is itself an orthogonal projector. If an item has a failed label, Q_Fw_e=0.

Consider a live item with real labels A=Λ(e). The spans of V_A and V_F are nearly orthogonal. Indeed, after orthonormalizing each set,

```math
\left\|(V_F^TV_F)^{-1/2}V_F^TV_A
       (V_A^TV_A)^{-1/2}\right\|
 \le\frac{\delta_0}{1-\delta_0}.
\tag{10}
```

It follows that P_F loses at most
κ_0=δ_0^2/(1−δ_0)^2≤4δ_0^2
of the squared norm of any vector in span(V_A). All singular values of its restriction to this j-dimensional span, j=|A|≤d, therefore have square at least 1−κ_0. The exterior volume ratio satisfies

```math
\|Q_Fz_e\|_2^2
  \ge(1-\kappa_0)^j
  \ge1-d\kappa_0
  \ge1-\epsilon/16.
\tag{11}
```

The upper bound is one because Q_F is an orthogonal projector. Apply the positive decoding lemma to obtain

```math
|H|=O\!\left(\min\left\{N,
   \frac{r}{\epsilon^2}
       \sum_{j=0}^{\min(d,D)}\binom Dj\right\}\right).
\tag{12}
```

For fixed d, h≥d, and a fixed success probability, an uncapped convenient form is

```math
O_d\!\left(\min\left\{N,
 \frac{r h^d\log^d(2L)}{\epsilon^{d+2}}\right\}\right).
\tag{13}
```

The explicit sum of binomial coefficients in (12) should be used when d varies. The deterministic existence lower example with one item for each d-subset of h+d labels, replicated in r orthogonal directions, requires r binom(h+d,d) original items for every ε<1: failing the complement isolates each item in its direction. Thus (13) has the correct h exponent for fixed d and ε, up to logarithms. It is not an optimized bound in ε or d.

## 4. A deterministic code for every failure budget

Here is a finite-bit replacement for random RIP in the one-label theorem. For any rational μ∈(0,1/2), one can deterministically construct L unit vectors with pairwise inner products of absolute value at most μ in

```math
D=O(\mu^{-2}\log(2L))
\tag{14}
```

dimensions. A short conditional-expectation proof is included to specify the algorithm.

Start with D-by-L independent signs s_{ic}. Let q=1+μ, a=(q+q^{-1})/2, and t_0=floor(μD). Define the nonnegative potential

```math
\Psi=\sum_{c<c'}
 \left[q^{\sum_i s_{ic}s_{ic'}-t_0}
       +q^{-\sum_i s_{ic}s_{ic'}-t_0}\right].
\tag{15}
```

Its expectation is L(L−1)a^Dq^{-t_0}. Since log a≤(log q)^2/2≤μ^2/2 and log q≥3μ/4, taking D≥C μ^{-2}log(2L) makes the expectation below 1/4. Fix signs successively, always taking the value with no larger conditional expectation. For a pair of columns, every coordinate whose two signs have not both been fixed contributes the factor a, while a fully fixed coordinate contributes q^{±1}; therefore every conditional expectation is an explicitly computable rational number. At completion Ψ<1, which forces every absolute sign inner product below t_0≤μD. Dividing the columns by sqrt(D) gives the desired unit vectors. The sqrt(D) never needs to be represented when forming their normalized outer products.

Choose μ, within a constant factor of its upper bound, so that

```math
\mu\le\frac1{4h},\qquad
 \mu^2\le\frac{\epsilon}{64h}.
\tag{16}
```

A rational dyadic μ suffices. For any F of size at most h, Gershgorin's theorem gives V_F^TV_F≽(3/4)I. For any c∉F,

```math
1-\|P_Fv_c\|_2^2
 \le\frac43\|V_F^Tv_c\|_2^2
 \le\frac43 h\mu^2\le\epsilon/48.
\tag{17}
```

Consequently D=O((h^2+h/ε)log(2L)) is sufficient, with the identity-code cap D≤L, and (B) follows. This code is not asserted to satisfy the stronger RIP condition at the random-code dimension; (17) is all the one-label decoder requires.

The graph and simplicial applications use the graded exterior incidence decoder in [the incidence theorem](graded-incidence-and-simplicial-spectral-sparsification.md). Its deterministic coherence requirement depends on the maximum number of distinct labels on a column; the corresponding bounds are stated in that manuscript.

## 5. Uniform preprocessing, arithmetic and bit complexity

First clip h at L and d at the actual maximum label-set size. If h=0 or d=0, use ordinary PSD sparsification without a label lift. If r=0, all PSD items vanish and the empty output suffices. L=0 is included in d=0. If L=1, the identity label code is available directly.

Compute the promised lifted dimension K and target C rK/ε^2 before forming exterior coordinates. If this target reaches N, return the entire input with unit weights. Otherwise rK and ε^{-2} are polynomially bounded by N. In particular, explicitly constructing the lifted matrices is uniformly polynomial even when h and d are part of the input. This gate is essential; a claim of polynomial time in an exponentially large lift would not by itself be uniform polynomial preprocessing.

For rational input, the coding and lifting steps need only rational arithmetic of polynomial bit length. One can round the random/coherence sign-code dimension up to a perfect square, losing at most a constant factor (or switch to the identity cap), so its unit coordinates ±1/sqrt(D) and the one-label permanent coordinate are rational. Alternatively, use the unscaled integer sign columns in (9). The factor D^{|Λ(e)|/2} relating an item's unscaled and unit-column wedge cancels in w_ew_e^T/||w_e||^2. In degree j≤d, each exterior coordinate is a j-by-j determinant with entries 0 or ±1, of magnitude at most j^{j/2}≤d^{d/2}; the degree-zero determinant is one. Its normalizing squared norm is a positive integer at most K d^d. Hence

```math
\widetilde B_e=B_e\otimes\frac{w_ew_e^T}{\|w_e\|_2^2}
```

has polynomial-bit rational entries; no normalized wedge square root is required. The range reduction can likewise use a rational basis and a rational left inverse, rather than an explicitly orthonormal basis. All later congruences recover the original matrices exactly.

If a random code gives a zero exterior vector, detect that before division and declare failure. This happens only outside the sufficient RIP event. The algorithm does not test RIP, enumerate fault sets, or certify the output by checking all F. It is Monte Carlo, with failure probability at most ζ. The identity-code branch and the coherence-code construction are deterministic.

The usual O(R/ε^2)-support PSD sparsification theorem of de Carli Silva–Harvey–Sato is invoked with R≤rK. Their theorem gives a deterministic construction in O(NR^3/ε^2) arithmetic operations. The rough bound (12) uses this standard black box. We distinguish that invocation from a fully spelled-out bit implementation of its barrier updates; an unproved exact-arithmetic-to-bit simulation is not part of the new lifting argument.

A direct polynomial-bit fallback avoids that issue. Compute the rational lifted leverage traces t_e=tr(\widetilde B_e\widetilde M^†), with total R'=rank(\widetilde M)≤rK. The deterministic two-sided trace-exponential conditional-expectation algorithm in [correlated-failure-spectral-and-regression-summaries.md](correlated-failure-spectral-and-regression-summaries.md), applied to this single lifted matrix, returns O(R' ε^{-2}log(2R')) weighted items. Use error slack and polynomial-precision exponential evaluation as described there. All input matrices now have polynomial bit length, and the same full-input cap bounds the iteration count. This adds only log(2rK) to the displayed support guarantees. Standard rational leverage sampling is another polynomial-bit option, with its usual logarithmic factor and sampling failure probability. Neither option requires fault enumeration.

## 6. Transfer to fixed-p row-norm coresets by Gaussian integration

The lifting argument is not restricted to quadratic forms. Let A have rows a_e and rank r. Fix p>0. Suppose an ordinary weighted row-subset routine, on any rank-R matrix with N rows, preserves the sum of p-th powers of all linear evaluations within 1±θ using S_p(R,N,θ,δ) rows with failure probability at most δ. This paragraph is a reduction to that standard nonrobust guarantee; its available support bound and computation assumptions are inherited from the chosen routine.

Use the label features z_e above and form lifted rows

```math
\widetilde a_e=a_e\otimes z_e
```

of rank at most rK. Apply the ordinary routine once. On its all-query success event,

```math
(1-\theta)\sum_e|\langle\widetilde a_e,u\rangle|^p
 \le\sum_{e\in H}\omega_e|\langle\widetilde a_e,u\rangle|^p
 \le(1+\theta)\sum_e|\langle\widetilde a_e,u\rangle|^p
\tag{18}
```

for every u in the lifted space.

Fix any fault set F and vector x. In (18), take u=x⊗g and integrate over a centered Gaussian g of covariance Q_F. For a standard one-dimensional Gaussian Z, let c_p=E|Z|^p, a finite positive number. Then

```math
\mathbb E_g|\langle\widetilde a_e,x\otimes g\rangle|^p
  =c_p\|Q_Fz_e\|_2^p|a_e^Tx|^p
  =c_p\alpha_e(F)^{p/2}|a_e^Tx|^p.
\tag{19}
```

This is a proof integration, not an additional sampling step. Finite sums and finite Gaussian moments justify the interchange. Because (18) already holds for every u, the argument simultaneously covers every F and x, including choices made after the row sample is seen.

For 0<p≤2, a live coefficient α_e(F)^{p/2} lies in [1−κ,1]. For fixed p>2 it lies in [1−(p/2)κ,1] by Bernoulli's inequality. Using projection loss κ≤ε/(4 max{1,p/2}) and θ=ε/4, the same scalar sandwich as in (4) proves

```math
(1-\epsilon)\sum_{e\in E_F}|a_e^Tx|^p
 \le\sum_{e\in H\cap E_F}\omega_e|a_e^Tx|^p
 \le(1+\epsilon)\sum_{e\in E_F}|a_e^Tx|^p.
\tag{20}
```

The common output loss weights ω_e are those of the ordinary lifted routine. The result is for a fixed p; it does not assert one weight vector for every p at once.

Cohen–Peng's classical Lewis-weight sampling supplies the ordinary routine for 0<p≤2. In particular, for p=1 a conservative high-probability bound is S_1(R,N,θ,δ)=O(R θ^{-2}log(2N/δ)). Thus the one-label RIP construction gives, for constant success probability and 1≤h<L,

```math
O\!\left(\min\left\{N,
 \frac{r}{\epsilon^3}
 \left[(h+1)\log\frac{eL}{h+1}+\log\frac1\zeta\right]
 \log\frac{2N}{\delta}\right\}\right)
\tag{21}
```

rows preserving (20) for every h-label deletion, with total failure probability at most ζ+δ. For fixed 1<p<2, insert any valid ordinary high-probability Lewis sampling bound; the same h exponent is obtained, with its usual additional logarithms. For p>2, (19) remains valid but the larger rank dependence of the ordinary row-embedding theorem must be retained; no O(R)-sample assertion is made here.

The graded exterior construction similarly uses R≤rΣ_{j=0}^{min(d,D)}binom(D,j). The full-input cap is applied to the final ordinary sample bound, not just rK, before building an overly large lift. Normalization may be represented as an input loss weight ||w_e||^{-p}, approximated to extra relative-error slack for a fixed rational p, or a fixed p admitting polynomial-time power evaluation; its logarithmic precision is polynomial in the rational coordinate length. The unnormalized row directions remain exact. This is separate from the entirely rational PSD outer-product implementation.

The same conclusion yields strong group-deletion coresets for fixed-response ℓ_p regression after augmenting the input by a supplied response subspace. No new ordinary Lewis-weight theorem is claimed; the new step is Gaussian integration of the lifted all-query event.

## 7. Fixed-background effective dimension in the one-label lift

There is also an effective-dimension version of the d=1 PSD theorem. Fix R≽0 and let

```math
\rho=\mathrm{tr}\bigl(M(R+M)^\dagger\bigr).
```

We seek a common summary approximating R+M_F, with R kept exactly. This subsection uses the original ambient dimension n: one must not merely restrict R to range(M) when R has cross terms with its orthogonal complement. The earlier positive decoding map is applied with I_n in place of I_r. Write η for the final spectral accuracy in this subsection. Use the one-label RIP code at projection-loss accuracy O(η). Its auxiliary dimension D must additionally satisfy D≥32h/η; append zero coordinates to the label vectors if necessary. In particular, the identity-code cap cannot discard this condition. Include a permanent coordinate for unlabeled items, and use D for the resulting total auxiliary dimension.

Set

```math
\widetilde M=\sum_eB_e\otimes v_ev_e^T,
 \qquad
 \widetilde R=R\otimes I_D/D.
```

For the fault projection P_F, partial trace sends the background to

```math
\mathcal T_F(\widetilde R)
   =\frac{D-\mathrm{rank}V_F}{D}R.
\tag{22}
```

This scalar lies in [1−η/32,1], while all live data coefficients also lie in [1−O(η),1]. Thus any ordinary fixed-background spectral sparsifier for \widetilde R+\widetilde M, retaining \widetilde R exactly, decodes by the same sandwich to a common approximation of R+M_F. The background participates in the sandwich as one additional PSD summand with fixed weight one; its coefficient (22) is only used in the analysis.

The lifted effective dimension is at most Dρ. To prove this first suppose R≻0. Put C_e=R^{-1/2}B_eR^{-1/2}, C=Σ_eC_e, and

```math
A=D\sum_eC_e\otimes v_ev_e^T.
```

For f(X)=X(I+X)^{-1}, the lifted effective dimension is tr f(A). Average conjugation of A over signed permutation matrices on the auxiliary factor. The average is C⊗I_D, since every v_e is a unit vector. The function f is operator concave; equivalently, matrix inversion is operator convex. One elementary proof of the latter averages the PSD block matrices [[X,I],[I,X^{-1}]] and applies the Schur complement. Jensen's inequality and trace invariance give

```math
\mathrm{tr}f(A)
 \le\mathrm{tr}f(C\otimes I_D)
 =D\mathrm{tr}\bigl(C(I+C)^{-1}\bigr)
 =D\rho.
\tag{23}
```

The finite twirl is only a proof operation and need not be enumerated. For semidefinite R, replace R by R+ξI and pass to ξ↓0. All item trace terms have finite pseudoinverse limits because their ranges are contained in the total range. Hence (23) also holds for R≽0.

Apply the ordinary fixed-background importance sampler, or its deterministic single-scenario trace-exponential derandomization, to the lifted instance. In original ambient dimension n, the resulting support is

```math
O\!\left(\min\left\{N,
 \frac{\rho D}{\eta^2}\log(2nD)\right\}\right).
\tag{24}
```

Only the code selection needs randomness if the latter derandomization is used. One can choose

```math
D=O\!\left(\frac{(h+1)\log(eL/(h+1))+\log(1/\zeta)}{\eta}\right)
```

in the regime 1≤h<L. Identity-code padding gives the corresponding capped construction when h is near L. For a fully deterministic tradeoff, use the coherence code at η accuracy and the same extra dimension condition.

The small-effective-dimension check is necessary for uniform polynomial preprocessing: if ρ≤η, return no data items, since R already η-approximates every R+M_F. Otherwise ρ>η, and a nontrivial target ρDη^{-2} below N forces D<N, so the lift and the iteration count remain polynomial after the full-input cap. The same reasoning applies to the logarithmic target in (24).

Combining (24) with the convex-regularized least-squares lemma in [weak-convex-regression-under-correlated-failures.md](weak-convex-regression-under-correlated-failures.md), set η^2=ε/(1+ε). For a fixed supplied response subspace of dimension q and base regularization λ_0, use R=diag(λ_0I,0) and ρ≤sd_{λ_0}(A)+q. This gives a shared weak regression coreset with linear h dependence and ε^{-3/2} dependence, up to the displayed logarithms, valid for all later responses in the supplied subspace, λ≥λ_0, convex constraints, and nonnegative convex penalties. The importance-pool route has ε^{-1} dependence but can be quadratic in h; the better of the two bounds can be used. No single bound dominates all parameter regimes.

## 8. Baselines and limits

The random-sign RIP theorem and the ordinary PSD sparsification theorem are established tools. The contribution is their composition with a label-failure projector and an order-preserving partial trace, yielding one common original-item weight vector for all correlated deletions. The earlier exterior construction for exact rank preservation alone cannot yield this spectral conclusion: controlling the norm of every live decoded feature is the extra property supplied here.

The probability quantifier is substantive. Oko–Sakaue–Tanigawa, Section 7.8.2, explicitly distinguishes high probability for each fixed fault set from one high-probability event for all fault sets, and explains that the existing Zhu et al. proof falls in the former category. The theorem here has the latter quantifier and permits failed color classes of unbounded size.

The general PSD sparsification theorem of Basu–Kothari–Liu–Meka, arXiv:2508.08169v2, gives a separately computed sparsifier for each requested subset, parameterized by a quantitative connectivity threshold. Its statement does not assert a common weight vector across all requested subsets, and its threshold is stronger than mere rank redundancy. It is useful related work, not a substitute for the all-scenario decoding argument.

Khanna–Putterman–Sudan, *A Unified Theory of Sparsification* (July 2026), already places spectral and other continuous sparsification problems in the common framework of arbitrary nonnegative real-valued codes, with size governed by continuous-valued non-redundancy. The present all-failure query family also fits that abstraction. Accordingly, no new universal abstraction for continuous sparsification is claimed here; the contribution is the explicit label-code construction, its polynomial preprocessing, and the stated failure-budget and accuracy tradeoffs.

The d=1 rank-one lower example consists of h+1 equally directed items per each of r orthogonal directions, one color per item position; deleting the other h colors isolates every item. Hence Ω(r(h+1)) items are necessary even for constant ε<1. For simple graphs, K_{h+1,k} with distinct colors on the left vertices gives Ω(nh) necessity when k≥h+1; color all edges incident to a left vertex by that same color for the edge-color version. After failing the other h colors, each remaining star edge is a bridge and must be retained.

No running-time improvement over specialized fast graph sparsifiers is claimed: preprocessing is polynomial but potentially high degree. No deterministic optimal-dimension RIP construction is claimed. Priority of the new correlated-failure lift still requires broader review.

### Primary sources

1. Richard Baraniuk, Mark Davenport, Ronald DeVore, Michael Wakin. *A Simple Proof of the Restricted Isometry Property for Random Matrices*. Constructive Approximation 28 (2008). https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/2/436/files/2011/04/baraniuk08si.pdf?bid=436
2. Marcel K. de Carli Silva, Nicholas J. A. Harvey, Cristiane M. Sato. *Sparse Sums of Positive Semidefinite Matrices*. Theorem 3. https://www.math.uwaterloo.ca/~harvey/Publications/SparsifierMMWUM/SparsifierMMWUM.pdf
3. Kazusato Oko, Shinsaku Sakaue, Shin-ichi Tanigawa. *Nearly Tight Spectral Sparsification of Directed Hypergraphs by a Simple Iterative Sampling Algorithm*. Section 7.8.2. https://arxiv.org/pdf/2204.02537
4. Arpon Basu, Pravesh K. Kothari, Yang P. Liu, Raghu Meka. *Sparsifying Sums of Positive Semidefinite Matrices*. January 2026 version, Definitions 1.3–1.4 and Theorem 1.5. https://arxiv.org/pdf/2508.08169
5. Avi Wigderson and David Xiao. *Derandomizing the Ahlswede–Winter Matrix-Valued Chernoff Bound Using Pessimistic Estimators, and Applications*. Theory of Computing 4 (2008). https://theoryofcomputing.org/articles/v004a003/v004a003.pdf
6. Michael B. Cohen and Richard Peng. *ℓ_p Row Sampling by Lewis Weights*. STOC 2015. https://arxiv.org/pdf/1412.0588
7. David P. Woodruff and Taisuke Yasuda. *Online Lewis Weight Sampling*. Corrected manuscript, Appendix A, for high-probability one-shot Lewis sampling. https://arxiv.org/pdf/2207.08268
8. Sanjeev Khanna, Aaron Putterman, Madhu Sudan. *A Unified Theory of Sparsification*. July 2026. https://arxiv.org/abs/2607.16126
