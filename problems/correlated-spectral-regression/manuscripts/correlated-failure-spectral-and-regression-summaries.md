# Correlated-failure spectral sparsification and Lewis-weight summaries

**Abstract.** We bound the sum of worst-case item importance under correlated label failures and construct safe common importance estimates without enumerating failure sets. Shared sampling then preserves PSD sums, row norms, and supplied-response regression objectives simultaneously. Matrix concentration, deterministic finite-scenario derandomization, and Lewis-weight sampling are established ingredients.

## 1. Model and principal statements

There are N original items. Item e has a set of failure labels Λ(e), of size at most d. The L labels appearing in the input are explicit. Failing a set F deletes precisely the items meeting F; write

```math
E_F=\{e:\Lambda(e)\cap F=\varnothing\},\qquad
 Q=\sum_{j=0}^{h}\binom Lj.
```

Here h is replaced by min(h,L), and d by the actual largest label-set size. Q is a count, not a list of queries. Its binary representation and its logarithm can be computed without enumerating the queries.

For positive h,d define

```math
\Gamma(h,d)=\frac{(h+d)^{h+d}}{h^h d^d}.
\tag{1}
```

Set Γ=1 when h=0 or d=0. For h=1 a sharper factor d+1 is available below.

Item e contributes an explicitly given real symmetric positive semidefinite matrix B_e. Let

```math
M_X=\sum_{e\in X}B_e,\qquad r=\mathrm{rank}(M_E).
```

The rank-one case B_e=a_ea_e^T includes covariance matrices and weighted graph Laplacians. Arbitrary-rank PSD items are allowed. Define, for e∈X,

```math
t_e(X)=\mathrm{tr}(B_eM_X^\dagger),\qquad
 \sigma_e=\max_{|F|\le h,\ e\in E_F}t_e(E_F).
\tag{2}
```

**Importance theorem.**

```math
\sum_e\sigma_e\le \Gamma(h,d)r.
\tag{3}
```

For one label failure,

```math
\sum_e\sigma_e\le(d+1)r.
\tag{4}
```

The factor d+1 in (4) is exact. For general h,d, examples require total importance r binom(h+d,d). Thus (3) is within the ratio Γ(h,d)/binom(h+d,d) of the natural sharp lower bound. In particular, for d=1 it is less than e(h+1)r. This is a near-sharp importance bound, not by itself a near-sharp all-h sparsifier-size theorem.

**Spectral summary theorem.** For ε,δ∈(0,1), a randomized algorithm constructs one subset H of original items and one fixed set of nonnegative weights ω_e such that, with probability at least 1−δ, simultaneously for every |F|≤h,

```math
(1-\epsilon)M_{E_F}\preceq
 \sum_{e\in H\cap E_F}\omega_eB_e
 \preceq(1+\epsilon)M_{E_F}.
\tag{5}
```

The same weights are used for every F. The number of retained items is

```math
O\!\left(\min\left\{N,
 \frac{\Gamma(h,d)r}{\epsilon^2}
 \log\frac{2rQ}{\delta}\right\}\right).
\tag{6}
```

Preprocessing is uniformly polynomial in the explicit input, after the cap at N described below; it does not enumerate F. It is not asserted to be nearly linear time.

For h=1, exact scores can be computed by L+1 covariance calculations. There is then a **deterministic polynomial-time** construction of size

```math
O\!\left(\min\left\{N,
 \frac{(d+1)r}{\epsilon^2}\log(2r(L+1))\right\}\right).
\tag{7}
```

For arbitrary h, enumerating all Q scenarios and using the same derandomization gives a deterministic algorithm polynomial in N,Q and the matrix dimensions; this is not a uniform polynomial bound when h is part of the input.

The logarithm in (6) must remain explicit. For d=1 and varying h it may give

```math
O\!\left(\frac{hr}{\epsilon^2}
 [\log(2r/\delta)+h\log(eL/h)]\right),
```

which can be quadratic in h. We do not hide log Q in a polylogarithmic factor in h and L.

## 2. A monotone-importance pool lemma

The main bound is more general than matrices. Suppose each subset X has nonnegative masses m_e(X), e∈X, such that

1. if e∈X⊆Y then m_e(X)≥m_e(Y); and
2. every X satisfies Σ_{e∈X}m_e(X)≤S.

Define σ_e as in (2), replacing t by m. Then

```math
\sum_e\sigma_e\le\Gamma(h,d)S.
\tag{8}
```

**Proof.** Fix, separately for each e, a maximizing valid failure set F_e. Include every label in a random set R independently with probability α∈(0,1). Let the associated item pool be

```math
X_R=\{e:\Lambda(e)\subseteq R\}.
```

The event A_e that Λ(e)⊆R and F_e∩R=∅ has probability

```math
\Pr(A_e)=\alpha^{|\Lambda(e)|}(1-\alpha)^{|F_e|}
 \ge\alpha^d(1-\alpha)^h.
```

On A_e, e∈X_R⊆E_{F_e}, so monotonicity gives m_e(X_R)≥σ_e. Pointwise in R,

```math
\sum_e\mathbf1_{A_e}\sigma_e
 \le\sum_{e\in X_R}m_e(X_R)\le S.
```

Taking expectations and setting α=d/(h+d) proves (8). Empty own-label sets and empty failure sets need no modification. ∎

For PSD items, Σ_{e∈X}t_e(X)=rank(M_X)≤r. Deletion monotonicity holds even when rank drops. Indeed, for v in the range of M_X and M_X≼M_Y,

```math
v^TM_X^\dagger v
 =\sup_z(2v^Tz-z^TM_Xz)
 \ge\sup_z(2v^Tz-z^TM_Yz)
 =v^TM_Y^\dagger v.
```

Decompose B_e into rank-one PSD terms; every such vector is in range(M_X) when e∈X. Summing this inequality proves t_e(X)≥t_e(Y). No incorrect global order between the two pseudoinverses is needed.

## 3. The sharper one-failure identity and the lower example

Let t_e=t_e(E), let E_c be the items surviving failure of c, and let r_c=rank(M_{E_c}). For each surviving item, t_e(E_c)−t_e≥0. Therefore

```math
\begin{aligned}
 \sum_e\max\{t_e,\max_{c\notin\Lambda(e)}t_e(E_c)\}
 &\le r+\sum_c\sum_{e\in E_c}[t_e(E_c)-t_e]\\
 &=r+\sum_c\left[r_c-r+\sum_{e:\ c\in\Lambda(e)}t_e\right]\\
 &=r+\sum_e|\Lambda(e)|t_e-\sum_c(r-r_c)\\
 &\le(d+1)r.
\end{aligned}
\tag{9}
```

The middle expression is also a useful data-dependent bound. The proof applies to any masses whose total equals an inclusion-monotone rank statistic; it does not follow merely from a hereditary upper bound on their total.

For the lower example, take r orthogonal coordinate directions. In each direction include one unit vector for every d-subset A of a label universe of size h+d, assigning that vector exactly the labels A. For any particular A, failing its h-element complement leaves only the A-vector in each coordinate direction. Its leverage is one. Thus every one of the r binom(h+d,d) items has σ_e=1. This proves the claimed lower bound, and proves exactness of (4) when h=1. It also forces every multiplicative spectral summary with ε<1 to retain all these items: a query isolates each one in its coordinate direction.

## 4. Computing safe importance overestimates without failure enumeration

For h,d>0 set α=d/(h+d), so an admissible protected-item/failure pair is separated by a random pool with probability at least 1/Γ. Draw

```math
J=\left\lceil8\Gamma\log\frac{2NQ}{\delta}\right\rceil
\tag{10}
```

independent label pools. There are at most NQ admissible pairs (e,F). For each fixed pair, a multiplicative Chernoff bound shows that fewer than J/(2Γ) of the pools separate it with probability at most exp(−J/(8Γ)). A union bound proves that, with probability at least 1−δ/2, **every** admissible pair is separated at least J/(2Γ) times.

Compute t_e(X_j) on each pool. To avoid zero sampling probabilities on any nonzero item, define

```math
\widehat\sigma_e=t_e(E)+\frac{2\Gamma}{J}
                \sum_{j:\ e\in X_j}t_e(X_j).
\tag{11}
```

On the coverage event, for every admissible (e,F), all separating pools satisfy X_j⊆E_F and contain e. Consequently

```math
\widehat\sigma_e\ge t_e(E_F),\qquad
 \widehat\sigma_e\ge\sigma_e.
\tag{12}
```

For **every** outcome of the pool experiment, including bad outcomes,

```math
T:=\sum_e\widehat\sigma_e\le(1+2\Gamma)r\le3\Gamma r.
\tag{13}
```

This deterministic mass bound follows by summing pool ranks. The construction never seeks a maximizing failure set and never tests the exponentially many coverage conditions. Their simultaneous validity is an analysis event.

To obtain a uniform polynomial algorithm, first compute a sufficiently conservative upper bound for the target in (6). If it is at least N, return the entire input with weight one. Otherwise Γ≤N because r≥1, ε<1, and the logarithmic factor is at least a constant. Equation (10) then uses polynomially many pools. The labels, h≤L, and d≤L are explicit; log Q≤L log 2 has polynomial encoding length. Exact rational PSD matrices yield rational scores with polynomial bit complexity via rank-revealing elimination and inverse calculations. There is no field-extension or symbolic independence assumption here.

For h=0 or d=0, simply use t_e(E), because there is only one distinct surviving matrix. For r=0 all PSD items vanish, and the empty summary suffices. Zero items can always be discarded. The cases h>L and oversized d were clipped at the outset.

## 5. One shared spectral sample

Condition on a good pool outcome. Put p_e=\widehat\sigma_e/T for nonzero items. Independently draw

```math
k=\left\lceil C T\epsilon^{-2}\log\frac{4rQ}{\delta}\right\rceil
```

items from this distribution, with a sufficiently large absolute constant C. If item e is drawn n_e times, give it the single fixed weight ω_e=n_e/(kp_e), and aggregate duplicate draws.

Fix F with surviving rank r_F>0 and whiten only on range(M_{E_F}). The contribution of a surviving e has operator norm at most t_e(E_F). A normalized sampled contribution therefore has norm at most T/k. Its expectation sums to the identity on this r_F-dimensional range. The usual PSD matrix Chernoff bound gives spectral failure probability at most

```math
2r_F\exp[-\epsilon^2k/(3T)]\le\delta/(2Q).
```

A union bound over the Q failure sets proves simultaneous validity. Rank-zero queries are automatic. This second random experiment is independent of the pools; its conditional failure probability is at most δ/2 for **every** good pool outcome. Combining the two error probabilities proves (5). The number of distinct retained items is at most k and at most N. No query changes a retained item's weight; it only deletes the items carrying failed labels.

Adding an arbitrary common PSD background R later preserves (5), since the same R can be added to both sides and PSD order absorbs the ±εR slack. This is a consequence of the proved spectral inequality, not an extra sampling assumption.

## 6. Deterministic construction for one failure

For h=1, calculate the exact σ_e using the no-failure matrix and the L single-label matrices. Let T=Σσ_e≤(d+1)r. Whiten each nonzero-rank scenario separately and form the block-diagonal item matrix

```math
C_e=\bigoplus_F
 \left[M_{E_F}^{\dagger/2}B_eM_{E_F}^{\dagger/2}\right]_{\mathrm{range}(M_{E_F})},
```

with a zero block when e is deleted. The block dimension D=Σ_F r_F is at most (L+1)r. We have Σ_e C_e=I_D and ||C_e||≤σ_e. Thus the matrices X_e=C_e/p_e, p_e=σ_e/T, have expectation I_D and satisfy 0≼X_e≼T I_D.

The matrix-Chernoff experiment can be derandomized by the classical Wigderson–Xiao pessimistic-estimator method. For completeness, a direct two-sided estimator is as follows. Let θ=ε/(2T), choose k=O(Tε^{-2}log(2D)), and write

```math
a=1+\frac{e^{\theta T}-1}{T},\qquad
 b=1+\frac{e^{-\theta T}-1}{T}.
```

For a partial sum S_j of j chosen matrices define

```math
\Phi_j=
 e^{-\theta k(1+\epsilon)}a^{k-j}\mathrm{tr}e^{\theta S_j}
 +e^{\theta k(1-\epsilon)}b^{k-j}\mathrm{tr}e^{-\theta S_j}.
\tag{14}
```

Golden–Thompson and the scalar chord bound for exp on [0,T] imply E_e Φ_{j+1}≤Φ_j. Choose an index attaining at most that average. For a sufficiently large constant in k, Φ_0<1/4. At completion, Φ_k<1 rules out any eigenvalue outside [k(1−ε),k(1+ε)]. The resulting multiplicities give the same fixed original-item weights as in Section 5.

For rational input, use slack, for example keeping the total numerical error in the k choices below 1/4, and approximate the matrix exponentials to sufficient precision. After the cap at N, k and the logarithms of all needed accuracy/conditioning scales are polynomial in the input length. This yields the ordinary deterministic polynomial bit-complexity interpretation; no exact transcendental comparison is required. The derandomization itself is not proposed as a new theorem.

## 7. Lewis weights and correlated-deletion regression

Let A have rows a_e and rank r. Fix 0<p≤2, and let w_e^{(p)}(A_X) be the ordinary ℓ_p Lewis weight of row e in A_X, computed in its row span. These weights are nonnegative, sum to rank(A_X), and do not increase when rows are added. The last property is Cohen–Peng, Lemma 5.5.

The rank-deficient case follows from the full-rank version: append arbitrarily small rows spanning the orthogonal complement of row(A_X), apply full-rank monotonicity before and after adding the other original rows, and let the artificial rows tend to zero. The old weights in the first augmented matrix are exactly the Lewis weights within row(A_X); in the second they converge to the ordinary full-span weights. Zero original rows have weight zero. Thus every deletion and pool used above is legitimate even when its rank drops.

Consequently, with

```math
\sigma_e^{(p)}=\max_{|F|\le h,\ e\in E_F}w_e^{(p)}(A_{E_F}),
```

we obtain

```math
\sum_e\sigma_e^{(p)}\le\Gamma(h,d)r,
 \qquad
 \sum_e\sigma_e^{(p)}\le(d+1)r\quad(h=1).
\tag{15}
```

The orthogonal-copy example from Section 3 proves the same lower bounds for every p. Constant-factor upper approximations to the Lewis weights can be used in the pool estimator: if w≤\widetilde w≤c w, the resulting mass bound is only multiplied by c.

Combining (15) with classical high-probability one-shot Lewis-weight sampling gives one common weighted row subset preserving

```math
\sum_{e\in E_F}|a_e^Tx|^p
```

within 1±ε for every x and every allowed F. For p=1 one may use the explicit safe bound

```math
O\!\left(\min\left\{N,
 \Gamma(h,d)r\epsilon^{-2}\log\frac{2NQ}{\delta}\right\}\right).
\tag{16}
```

For each fixed 1<p<2, a conservative bound from the published one-shot sampling theorems is

```math
O_p\!\left(\min\left\{N,
 \frac{\Gamma(h,d)r}{\epsilon^2}
 \left[(\log(2r))^3\log(2N)+\log\frac{2NQ}{\delta}\right]\right\}\right).
\tag{17}
```

These logarithmic factors are not optimized. Replace Γ by d+1 when h=1 and exact or constant-factor all-scenario weights are computed. Independent Bernoulli row sampling with probability min{1,α\widehatσ_e} and retained loss weight equal to the inverse probability realizes the usual theorem; a Chernoff bound also controls the retained count. Failure sets remove rows after this one shared sampling experiment. The same pool cap makes preprocessing uniformly polynomial for fixed p, using existing Lewis-weight approximation routines.

For regression with a fixed response vector b, apply this to the augmented rows (a_e,b_e). For every allowed failure, all residual objectives Σ_{e∈E_F}|a_e^Tx−b_e|^p are then preserved simultaneously. Solving the weighted surviving problem gives the standard relative-objective approximation to the full surviving problem. This statement concerns fixed supplied responses, or more generally a fixed supplied response subspace included in the augmentation. It is not an assertion about arbitrary later response vectors. The norm-preservation theorem itself does not claim deterministic ℓ_p sampling for p≠2.

## 8. Graph interpretation and public comparison

For a weighted undirected graph, let B_e=w_e b_e b_e^T. Equation (5) is a spectral sparsifier after every allowed correlated failure. For one edge-color failure, d=1 and (7) gives O(r log(2r(L+1))/ε²) original reweighted edges. A failed color may contain arbitrarily many edges. For one vertex-color failure, give edge uv the labels of u and v; then d≤2 and the same asymptotic bound holds. Failed vertices are represented as isolated zero rows/columns in the common ambient vertex space. Edge and endpoint colors together give d≤3. These are correlated color failures, not a bound on the number of deleted individual vertices or edges.

The closest verified graph baseline is Zhu–Storandt–Lam–Han–Bi, ICML 2019, Definition 1 and Theorem 1. Their stated theorem handles at most f **individual** edge or vertex faults, with size O(f n log ρ+n log²n log³ρ/ε²+m/ρ). It does not state tolerance of an unbounded-size failed color class. The probability quantifier needs care: Oko–Sakaue–Tanigawa, Section 7.8.2 of arXiv:2204.02537, explicitly classifies the available Zhu et al. proof and its hypergraph extension as weak, meaning high probability for each fixed fault set, and explains that a uniform extension incurs an additional multiplicative fault factor. For ordinary edge failures their stated uniform extension is O(f n log²n/ε²). The certificates here use one event valid for every allowed correlated failure simultaneously. This manuscript does not claim a general improvement over specialized individual-fault algorithms.

Cohen–Peng supplies the nonrobust Lewis-weight computation, monotonicity and sampling ingredients. Woodruff–Yasuda supplies explicit high-probability one-shot sampling suitable for the union over Q. The claimed increment is the total importance under correlated failure and its uniform pool estimation, not new nonrobust row sampling. In–Li–Woodruff–Wu, ICML 2025, studies trimmed-loss robust coresets that discard the largest m individual losses. Its model differs from preserving each specified group-deletion scenario with the original group identity and shared weights. A separate compiler manuscript discusses the more general sensitivity-sampling connection.

There is a particularly close methodological antecedent in In–Li–Woodruff–Wu, Section 3.1 and Lemma 4.3: they sample a Bernoulli subinstance so that one contributing function survives while its at-most-m outliers do not, and evaluate ordinary sensitivity inside that sample. This paper must be credited for that separation-and-sensitivity idea. The present proof uses label pools for correlated overlapping deletions, bounds the sum of all worst-surviving-scenario importance values by ΓS, and obtains common upper estimates by averaging ordinary pool scores. Their Lemma 4.4 concerns the cardinality of functions contributing to a trimmed-loss objective; it does not state this all-scenario total-importance inequality.

The following remain open in this manuscript: replacing Γr by r binom(h+d,d) for general robust leverage/Lewis weights; removing the log Q price without a new uniform concentration argument; and a uniformly polynomial deterministic construction for arbitrary h with the size in (6).

## 9. Fixed regularization: replace rank by effective dimension

There is a useful variant when a positive-definite background matrix R is fixed in advance. Set

```math
d_R=\mathrm{tr}\bigl(M_E(R+M_E)^{-1}\bigr),\qquad
 t_e^R(X)=\mathrm{tr}\bigl(B_e(R+M_X)^{-1}\bigr).
```

These masses are deletion-monotone. Their total is

```math
d_R(X)=\mathrm{tr}\bigl(M_X(R+M_X)^{-1}\bigr)\le d_R.
```

To see the last inequality, write K_X=R^{-1/2}M_XR^{-1/2}; the total is tr[I−(I+K_X)^{-1}], which increases in the PSD order. The pool lemma and the one-failure accounting therefore give robust importance bounds Γd_R and (d+1)d_R, respectively.

The same pool estimator and a shared sample yield

```math
(1-\epsilon)(R+M_{E_F})\preceq
 R+\sum_{e\in H\cap E_F}\omega_eB_e
 \preceq(1+\epsilon)(R+M_{E_F})
\tag{18}
```

for all queries, with size

```math
O\!\left(\min\left\{N,
 \Gamma d_R\epsilon^{-2}\log\frac{2nQ}{\delta}\right\}\right),
\tag{19}
```

where n is the ambient matrix dimension. For h=1, replace Γ by d+1 and use deterministic finite-scenario derandomization.

Here is the concentration detail, since the sampled part no longer has identity expectation. Whiten R+M_{E_F}. If X is one importance-weighted item draw, then 0≼X≼T I, its mean K satisfies 0≼K≼I, and also K≼T I. Thus Z=X−K satisfies ||Z||≤T and

```math
\mathbb E Z^2=\mathbb E X^2-K^2
 \preceq T K\preceq T I.
```

Matrix Bernstein for the average of k independent draws gives failure probability at most 2n exp(−c kε²/T). Adding back the fixed whitened R turns additive error εI into (18). The standard two-sided trace-exponential pessimistic estimator with the bound

```math
\mathbb E e^{\pm\theta Z}
 \preceq\exp\!\left(\frac{e^{\theta T}-\theta T-1}{T}\right)I
```

provides the same deterministic polynomial construction for the L+1 scenarios when h=1.

Small effective dimension does not invalidate the uniform preprocessing cap. First, if d_R≤ε, return the empty item summary: for every F, the whitened M_{E_F} has norm at most d_R, so R itself already satisfies (18). In the remaining case d_R>ε, a nontrivial target in (19) below N again implies Γ≤N. Hence the pool count stays polynomial. This precheck also absorbs the rounding of the sample count to an integer.

The same certificate remains valid for every later background R'≽R, by adding R'−R. For R=λ_0I this covers all regularization strengths λ≥λ_0, with size controlled by the effective dimension at λ_0. No new right-hand-side claim is implicit in this matrix statement.

All statements of this section also hold for a positive-semidefinite background R, with (R+M_X)^† replacing the inverse. Indeed, apply the monotonicity and total-mass statements with R+ζI and let ζ decrease to zero. Every B_e with e∈X is supported on range(M_X), hence on range(R+M_X), so its trace expression converges to the finite pseudoinverse expression. The concentration proof whitens only range(R+M_{E_F}); both the true and sampled matrices vanish on its orthogonal complement. The small-effective-dimension precheck is unchanged. This extension is useful for augmented regression matrices with background diag(λI,0).

Ridge leverage/effective-dimension sparsification is an established nonrobust technique: Calandriello–Koutis–Lazaric–Valko (ICML 2018) develops ridge spectral graph sparsification. The increment here is the same original-item, correlated-deletion certificate and its total-importance bound. Kacham–Woodruff (AISTATS 2020) already gives optimal deterministic nonrobust weak ridge-regression coresets, with a different solution-preservation objective. A separate short regression corollary records the ε^{-1} dependence available for that weaker objective under correlated failures.

## 10. A precise obstruction to a tempting sharper-bound proof

The exact binomial importance bound would follow if all restriction leverage marginals could be coupled to minimum-weight matroid bases under one random additive item-cost vector. That coupling assertion is false, even for rank two and four individually failing columns.

Take

```math
a_0=(1,-10),\quad a_1=(1,10),\quad
 a_2=(2,-10),\quad a_3=(3,15).
```

Every pair is independent, so their matroid is U_{2,4}. Direct two-by-two determinant calculations give

```math
\tau_1(\{0,1,2\})=\frac{13}{14},\quad
 \tau_0(\{0,1,3\})=\frac{97}{106},\quad
 \tau_3(\{0,2,3\})=\frac{225}{229},\quad
 \tau_2(\{1,2,3\})=\frac{20}{21}.
```

Their sum is 963073/254877>3. For any fixed additive ordering, every greedy rank-two basis after one individual deletion is contained in the globally first three elements. Therefore the four corresponding selected-item indicators sum to at most three, pointwise. Taking expectations contradicts the displayed leverage marginals. The argument includes any fixed consistent tie-breaking order.

This counterexample only rules out that coupling proof: the proposed bound r binom(h+d,d) equals four in this example, so it is not a counterexample to the sharper numerical conjecture.

### Primary sources

1. Michael B. Cohen and Richard Peng. *ℓ_p Row Sampling by Lewis Weights*. STOC 2015. Lemma 5.5; Theorems 2.3 and 7.1. https://arxiv.org/pdf/1412.0588
2. David P. Woodruff and Taisuke Yasuda. *Online Lewis Weight Sampling*. SODA 2023/current corrected manuscript. Appendix A, especially Theorem A.2. The corrected manuscript removes an unrelated adversarially robust streaming claim; that removed claim is not used here. https://arxiv.org/pdf/2207.08268
3. Avi Wigderson and David Xiao. *Derandomizing the Ahlswede–Winter Matrix-Valued Chernoff Bound Using Pessimistic Estimators, and Applications*. Theory of Computing 4 (2008), 53–76. https://theoryofcomputing.org/articles/v004a003/v004a003.pdf
4. Chunjiang Zhu, Sabine Storandt, Kam-Yiu Lam, Song Han, Jinbo Bi. *Improved Dynamic Graph Learning through Fault-Tolerant Sparsification*. ICML 2019. https://proceedings.mlr.press/v97/zhu19b/zhu19b.pdf
5. Marcel K. de Carli Silva, Nicholas J. A. Harvey, Cristiane M. Sato. *Sparse Sums of Positive Semidefinite Matrices*. General arbitrary-rank PSD sparsification baseline. https://www.cs.cmu.edu/afs/cs/academic/class/15859n-s20/RelatedWork/SparsifierMMWUM.pdf
6. Chansophea Wathanak In, Yi Li, David Woodruff, Xuan Wu. *Robust Sparsification via Sensitivity*. ICML 2025. https://proceedings.mlr.press/v267/in25a.html
7. Daniele Calandriello, Ioannis Koutis, Alessandro Lazaric, Michal Valko. *Improved Large-Scale Graph Learning through Ridge Spectral Sparsification*. ICML 2018. https://proceedings.mlr.press/v80/calandriello18a/calandriello18a.pdf
8. Praneeth Kacham and David P. Woodruff. *Optimal Deterministic Coresets for Ridge Regression*. AISTATS 2020. https://proceedings.mlr.press/v108/kacham20a/kacham20a.pdf
9. Kazusato Oko, Shinsaku Sakaue, Shin-ichi Tanigawa. *Nearly Tight Spectral Sparsification of Directed Hypergraphs by a Simple Iterative Sampling Algorithm*. Section 7.8.2 distinguishes fixed-failure and uniform fault-tolerance guarantees. https://arxiv.org/pdf/2204.02537
