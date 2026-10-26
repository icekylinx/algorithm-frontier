# Arbitrarily weighted Cayley sparsifiers with O(log³ |G|) generators

**Abstract.** We prove that every arbitrarily weighted Cayley graph on a finite group of order $N$ has a spectral sparsifier supported on $O(\epsilon^{-2}\log^3(2N))$ original generator items. The construction is deterministic in the explicit permutation-matrix model. The proof combines a weight-ordered subset-product relation with a total-importance bound that is uniform under positive rescaling. A second theorem constructs one set of coefficients that remains valid after every allowed correlated generator deletion.

## 1. Main statement and exact model

Let G be a finite group of order N≥2. For g∈G let U_g be its right regular permutation representation, with a consistent multiplication convention, and define

$$
L_g=I-\frac{U_g+U_g^*}{2}
     =\frac12(I-U_g)^*(I-U_g).
\tag{1}
$$

Thus L_g is positive semidefinite and L_g=L_{g^{-1}}. An input item e consists of a generator g_e and an arbitrary positive weight w_e, and contributes B_e=w_eL_{g_e}. Identity generators and zero-weight items can be discarded. Repeated generators are allowed as separately identified items. Write m for the number of items and M=Σ_e B_e.

For an ordinary undirected weighted Cayley graph, combine the two members of each inverse pair into one item. The resulting item weight is their total coefficient in Σ_g w(g)L_g. Retaining an item means retaining that entire inverse pair with a common multiplier. Counting individual group elements instead of inverse-pair items changes support size by at most two. This convention also makes the later fault model unambiguous: a failed item deletes the whole undirected generator, including its inverse.

**Theorem 1 (arbitrary weights, arbitrary finite groups).** For every ε∈(0,1), there are nonnegative multipliers ω_e, supported on

$$
O\!\left(\min\left\{m,\frac{\log^3(2N)}{\epsilon^2}\right\}\right)
\tag{2}
$$

original items, such that

$$
(1-\epsilon)M\preceq\sum_e\omega_e B_e
 \preceq(1+\epsilon)M.
\tag{3}
$$

For rational input weights and explicitly available permutation matrices, the multipliers can be found deterministically in time polynomial in N, m, the rational input bit length, and ε^{-1}. The support bound has no dependence on the weight ratio. The resulting graph is still a weighted Cayley graph on the same group; its generator weights are fixed after preprocessing.

The polynomial running time is in the explicit group/action size. It is not polynomial in log N for a succinct black-box group. No such succinct-group construction is claimed. Connectivity is unnecessary: every calculation is restricted to the range of the relevant PSD sum, so disconnected inputs and disconnected failure scenarios are included.

The more general representation statement is also valid. If U is any finite-dimensional unitary representation of G, with representation dimension n, replace (2) by

$$
O\!\left(\min\left\{m,
   \epsilon^{-2}\log^2(2N)\log(2n)\right\}\right).
\tag{4}
$$

For permutation representations this includes Schreier graphs. This is an inherited application of the argument; Schreier sparsification itself is already present in the public baseline. If the image of the representation has known order N_0<N, the proof can use N_0 in place of N. The dependence on the acting group's order cannot simply be replaced by the number of action vertices: BKLM Lemma 4.9 supplies Schreier graphs requiring a linear number of their generator items, with a much larger acting group.

There is also a standard universality consequence of the regular-representation construction: its O(ε^{-2}log³(2N)) support works simultaneously in every unitary representation of G, even one specified after preprocessing. To see this without a representation-decomposition theorem, use the right regular convention R_he_g=e_{gh^{-1}}. For any unitary representation U, the map

$$
Jx=N^{-1/2}\sum_{g\in G}e_g\otimes U_gx
$$

is an isometry satisfying (R_h⊗I)J=JU_h. Tensoring (3) with I and compressing by J gives the desired inequality for U. This also transfers each failure inequality (17) on the same common-weight success event. The direct-action bound (4) can be smaller when n<N; that construction may depend on the supplied action. Universality is an inherited fact about regular-representation sparsification, not a separate claim of a new representation-theoretic principle.

## 2. Related work

The strongest general-group baseline located in the checked sources is Basu–Kothari–Liu–Meka, *Sparsifying Sums of Positive Semidefinite Matrices*, SODA 2026, arXiv:2508.08169v2. Its Theorem 4.1 gives O(ε^{-2}log³N log|S|) generators for unweighted Cayley graphs, hence O(ε^{-2}log⁴N). Its Theorem 4.3 uses dyadic weight classes and gives O(ε^{-2}log³N log|S| log(2W)) for arbitrary positive weights of ratio W. Their Lemma 3.8 bounds total operator importance by a connectivity threshold, with an additional factor 1+log|S|. Their Lemma 4.2 obtains a quantitative redundancy parameter of order 1/log N; its weighted statement loses W.

The concurrent Hsieh–Lee–Mohanty–Putterman–Zhang paper, *Sparsifying Cayley Graphs on Every Group*, arXiv:2508.08078v1, Theorem 1.3, gives O(ε^{-2}log⁵N) generators for polynomially bounded weights. Its Corollary 2.8 gives the explicit weighted bound O(ε^{-2}log⁴N log(|S|W/ε)) after normalizing the minimum positive weight to one. Its runtime is polynomial in N. Its Remarks 1.4 and 2.6 already cover Schreier actions, and its directed-cut extension is also already explicit.

There is a strictly stronger subclass result that must not be omitted: Basu–Kothari–Meka–Tudose, *Optimal Sparsifiers for Abelian Cayley Graphs*, arXiv:2607.08261v1, July 2026, Theorem 1.5, gives O(ε^{-2}log N) generators for arbitrary weighted **abelian** Cayley graphs. Its Theorem 1.4 records O(ε^{-2}log⁴N) as the preceding general, possibly nonabelian, bound. The present theorem does not improve the abelian size bound; its intended increment is for arbitrary finite groups.

Primary sources:

- BKLM: https://arxiv.org/html/2508.08169v2 and https://arxiv.org/pdf/2508.08169.
- HLM+ : https://arxiv.org/html/2508.08078v1 and https://arxiv.org/pdf/2508.08078.
- BKMT: https://arxiv.org/html/2607.08261v1 and https://arxiv.org/pdf/2607.08261.
- Wigderson–Xiao, *Derandomizing the Ahlswede–Winter Matrix-Valued Chernoff Bound Using Pessimistic Estimators*: https://theoryofcomputing.org/articles/v004a003/v004a003.pdf.
- Zouzias, *A Matrix Hyperbolic Cosine Algorithm and Applications*, Theorem 4: https://arxiv.org/pdf/1103.2793.
- Koutis, *Simple Parallel and Distributed Algorithms for Spectral Graph Sparsification*, SPAA 2014: https://arxiv.org/abs/1402.3851.

The refinement of the BKLM argument is as follows: sorting by the current positive weights before choosing a subset-product collision removes W from the redundancy statement; applying that statement after normalizing each item's operator norm avoids integration over importance levels, removing log|S| from the total-importance bound. The matrix-sampling and derandomization ingredients are classical.

## 3. A total-importance lemma using all positive rescalings

For PSD matrices A_1,…,A_m with M=Σ_iA_i, define

$$
\tau_i=\inf\{t\ge0:A_i\preceq tM\}
       =\|M^{\dagger/2}A_iM^{\dagger/2}\|.
\tag{5}
$$

The norm in (5) is on range(M). Zero matrices have importance zero.

**Lemma 2.** Fix α∈(0,1] and an integer k≥2. Suppose that for every choice of positive scalars c_1,…,c_m and every set T⊆[m] with |T|≥k, some i∈T satisfies

$$
\alpha c_iA_i\preceq\sum_{j\in T\setminus\{i\}}c_jA_j.
\tag{6}
$$

Then

$$
\sum_i\tau_i\le\frac{4(k-1)}{\alpha}.
\tag{7}
$$

The same bound holds for every subfamily. It also holds after any further positive rescaling, because (6) is itself closed under those operations.

**Proof.** Discard zero matrices and whiten on range(M), obtaining matrices C_i with Σ_iC_i=I and τ_i=||C_i||∈(0,1]. Put D_i=C_i/τ_i and choose a unit vector x_i with x_i^*D_ix_i=1. Property (6) continues to hold for the D_i, since it allows all positive scalings and is preserved by congruence.

Independently select i with probability p_i=ατ_i/2. Conditional on i being selected,

$$
\mathbb E\left[x_i^*\sum_{j\ne i:\,j\ \mathrm{selected}}D_jx_i\right]
 =\frac\alpha2x_i^*\sum_{j\ne i}C_jx_i
 \le\frac\alpha2.
\tag{8}
$$

Call a selected i good if the random quantity inside the expectation is strictly below α. Markov's inequality shows that, conditional on selection, i is good with probability at least 1/2. Thus the expected number of good items is at least (α/4)Σ_iτ_i.

In every outcome let J be the set of good items. For every i∈J,

$$
x_i^*\sum_{j\in J\setminus\{i\}}D_jx_i
 <\alpha x_i^*D_ix_i.
\tag{9}
$$

Hence no i∈J satisfies αD_i≼Σ_{j∈J\{i}}D_j. Property (6) forces |J|≤k−1. Taking expectations proves (7). The strict inequality in the definition of good ensures that equality at the PSD-domination boundary causes no problem. ∎

This lemma does not follow from a redundancy guarantee only at the original input weights. The ability to apply (6) to A_i/τ_i is the essential extra hypothesis. In particular, it is not asserted as a replacement for BKLM Lemma 3.8 on an arbitrary fixed family without a scaling-uniform guarantee.

**Sharpness up to an absolute constant.** The dependence (k−1)/α in Lemma 2 is necessary for general PSD families, even diagonal ones. For M_0≥1 and i∈[m], let

$$
A_i=I+(M_0-1)e_ie_i^*\in\mathbb R^{m\times m},
 \qquad k=\lceil\alpha M_0\rceil+1,
\tag{9a}
$$

and take m≥k. For any positive weights and any k-item subset, choose an item of minimum weight. At its own coordinate, the other k−1 matrices contribute at least (k−1) times that minimum weight, which is at least αM_0 times it. At every other coordinate, their contribution is also at least the required α times the chosen diagonal entry, since M_0≥1 and α≤1. Thus (6) holds under every positive rescaling. Conversely, any unweighted set of k−1 items is α-minimal: at the private coordinate of each item, its α-scaled diagonal entry is αM_0, whereas the other items contribute k−2<αM_0. Hence this k is the exact threshold.

For the unweighted full family,

$$
\sum_iA_i=(m+M_0-1)I,
 \qquad
 \sum_i\tau_i=\frac{mM_0}{m+M_0-1}\longrightarrow M_0
 \quad(m\to\infty).
\tag{9b}
$$

Choosing αM_0 to be a positive integer makes M_0=(k−1)/α. Consequently no general bound of smaller order than (k−1)/α can replace (7). A further logarithmic improvement for Cayley generators must use additional group structure or a sparsification method beyond this general importance bound.

## 4. Weight-ordered group relations give the hypothesis

Set q=⌈log₂N⌉, k=q+1, and α=1/(4q). Consider any k generator items with arbitrary positive current weights a_1,…,a_k. Relabel them so that

$$
a_1\le a_2\le\cdots\le a_k.
$$

There are 2^k>N binary words indexed by their ordered subset products

$$
g_1^{b_1}g_2^{b_2}\cdots g_k^{b_k},\qquad b\in\{0,1\}^k.
$$

Two distinct words have the same product. Let i be their first differing index. Cancel the common prefix on the left. Exchanging the two words if necessary, the equality becomes

$$
g_i\prod_{j>i}g_j^{b_j}
 =\prod_{j>i}g_j^{c_j},
 \qquad
 g_i=\left(\prod_{j>i}g_j^{c_j}\right)
      \left(\prod_{j>i}g_j^{b_j}\right)^{-1}.
\tag{10}
$$

All products keep their displayed order. No commutativity is used. The right side is a word of length at most 2(k−i), involving only later generators, each appearing at most twice, possibly inverted. If i=k, (10) says g_i is the identity and its PSD contribution is zero, so domination is immediate.

For unitary matrices V_1,…,V_ℓ, telescoping prefixes gives

$$
V_1\cdots V_\ell-I
 =\sum_{t=1}^{\ell}V_1\cdots V_{t-1}(V_t-I).
$$

Consequently, by Cauchy–Schwarz and unitarity,

$$
\|(V_1\cdots V_\ell-I)x\|^2
 \le\ell\sum_{t=1}^{\ell}\|(V_t-I)x\|^2.
\tag{11}
$$

Since L_{g^{-1}}=L_g, applying (11) to (10) yields

$$
L_{g_i}\preceq 4q\sum_{j>i}L_{g_j}.
$$

The weight order now gives

$$
a_iL_{g_i}\preceq4q\sum_{j>i}a_iL_{g_j}
 \preceq4q\sum_{j>i}a_jL_{g_j}.
\tag{12}
$$

Thus every k-item set has an α-dominated item, for every positive choice of weights. The same is true for any larger set by taking an arbitrary k-item subset and adding the other PSD terms to the dominating side.

**Corollary 3 (hereditary Cayley importance bound).** For every subfamily X of arbitrary weighted generator items,

$$
\sum_{e\in X}
 \left\|M_X^{\dagger/2}B_eM_X^{\dagger/2}\right\|
 \le K_G:=16\lceil\log_2N\rceil^2,
 \qquad M_X=\sum_{e\in X}B_e.
\tag{13}
$$

Indeed, apply Lemma 2 with k=q+1 and α=1/(4q). The argument permits repeated generators, arbitrary positive weights, and non-generating subfamilies. It works in any finite-dimensional unitary representation.

## 5. Sampling and deterministic construction

For an ordinary PSD family with importance values τ_e and total T=Σ_eτ_e, sample k_s independent items with probabilities p_e=τ_e/T. A sample of e contributes B_e/(k_sp_e), and repeated samples are combined. On range(M), each unscaled random contribution X_e=M^{†/2}B_eM^{†/2}/p_e has expectation I and satisfies 0≼X_e≼TI. Matrix Chernoff therefore gives a (1±ε) approximation from

$$
k_s=O\bigl(T\epsilon^{-2}\log(2n/\delta)\bigr)
\tag{14}
$$

samples with failure probability at most δ. For Cayley generators T≤K_G and n≤N, proving the randomized version of (2).

The standard two-sided trace-exponential estimator derandomizes the same experiment without increasing its asymptotic support. Alternatively, Zouzias's Theorem 4 applies directly to the centered samples X_e−I: their norm is at most T when T≥1, their mean is zero, and their second-moment matrix is at most TI. This gives the same O(Tε^{-2}log(2n)) support. For completeness, the two-sided estimator can be written explicitly. With θ=ε/(2T) let

$$
a=1+\frac{e^{\theta T}-1}{T},\qquad
 b=1+\frac{e^{-\theta T}-1}{T}.
$$

For the partial sum S_j of j chosen X_e, use

$$
\Phi_j=
 e^{-\theta k_s(1+\epsilon)}a^{k_s-j}\mathrm{tr}e^{\theta S_j}
 +e^{\theta k_s(1-\epsilon)}b^{k_s-j}\mathrm{tr}e^{-\theta S_j}.
\tag{15}
$$

Golden–Thompson and the chord bound for exp on [0,T] show that the p-weighted average of Φ_{j+1} is at most Φ_j. Choose a next item whose value is no larger than that average. Taking k_s=C Tε^{-2}log(2n), for a sufficiently large constant C, makes Φ_0<1/4. At completion Φ_{k_s}<1 excludes every eigenvalue outside [k_s(1−ε),k_s(1+ε)]. The chosen multiplicities give the nonnegative rational multipliers.

For a bit-complexity implementation, compute rational upper estimates \barτ_e∈[τ_e,2τ_e] instead of demanding exact algebraic eigenvalues. They can be found by rational PSD tests for B_e≼tM on a rational basis of range(M), with dyadic search; the logarithmic separation of nonzero eigenvalues from zero is bounded by a polynomial in the rational input length. This multiplies T by at most two and leaves the estimator valid. The probabilities and final multipliers are then rational. Approximate the matrix exponentials with enough additive slack that the sum of the errors in all choices is less than 1/4. This is the classical finite-precision derandomization, rather than an exact-transcendental comparison model.

If the promised sample bound is at least m, simply return all items with multiplier one before the sampling or derandomization. Otherwise the number of steps is polynomially bounded by m. The logarithms of conditioning scales and requested numerical errors are polynomial in the rational input bit length and the stated precision parameter. Thus the deterministic algorithm is polynomial in the explicit input model. It need not construct the exponentially many subset products in Section 4: that argument only proves the score bound.

### 5.1 A randomized construction using group operations instead of dense matrices

There is an additional implementation of the same support order using a small dominating set. This section concerns the ordinary no-failure problem; the merging step below does not silently identify items with different failure labels.

**Dominating-set algorithm.** Process the current generator items in nonincreasing weight order. Maintain a selected set S and the set A of all ordered subset products of S, initially S=∅ and A={1_G}. For a candidate g, test whether A∩Ag is nonempty. If it is empty, select g and replace A by A∪Ag. Otherwise skip g.

Each selection doubles |A|, so at most q=⌈log₂N⌉ generators are selected. A collision has the form a=bg for a,b∈A, hence g=b^{-1}a. This is a word in the already selected heavier generators, with length at most 2|S| and with each selected generator occurring at most twice, possibly inverted. Equation (11) and the weight order imply

$$
B_e\preceq4q\sum_{s\in S}B_s
 \quad\text{for every item }e.
\tag{15a}
$$

Selected items satisfy the inequality trivially. Subsequent additions to S preserve domination of previously skipped items. This proves a q-item, 4q-factor dominating set for every positive reweighting and every subfamily.

With canonical group encodings and a dictionary for A, one scan uses O(mN) group multiplications and polynomially many dictionary/bit operations. A multiplication table also suffices. This bound is polynomial in the explicit group order, not in log N. The algorithm stores at most N group elements and never constructs an N-by-N Laplacian or computes an operator-importance score.

**Bundle sampling.** Apply the standard bundle-and-half-sampling strategy, whose graph antecedent is Koutis (2014); the related PSD support-and-sampling framework is also used in Basu–Brakensiek–Putterman, *Many Hamiltonians Are Sparsifiable* (2026), https://arxiv.org/html/2605.02211v1. The specialization below spells out the parameters rather than claiming a new matrix concentration theorem.

First merge repeated generator items in the ordinary problem, keeping one original representative per generator and adding its weights. There are m_0≤N resulting items. A final coefficient for such a generator can be assigned to its chosen original representative by dividing by that representative's original positive weight. Let

$$
A_0=\lceil\log_2(2N)\rceil+
       \left\lceil\log_2\frac{8m_0}{\delta}\right\rceil,
 \qquad K_0=C_0q^2A_0/\epsilon^2.
\tag{15b}
$$

If m_0≤K_0, return these items. Otherwise, at a stage with M>K_0 current items, set

$$
\eta=\frac\epsilon{100}(K_0/M)^{1/4},
 \qquad \lambda=\left\lceil C_1qA_0/\eta^2\right\rceil.
\tag{15c}
$$

A dyadic η within a factor two below this value suffices. Repeatedly compute and remove λ disjoint dominating sets, retaining their union D. For a large enough constant C_0, chosen after C_1, their total cardinality is at most qλ≤M/4. Every remaining item is dominated by every one of those disjoint sets, and therefore

$$
B_e\preceq\frac{4q}{\lambda}H_{\rm current}
       \quad(e\notin D).
\tag{15d}
$$

Keep D unchanged. Independently keep each other term with probability one half, doubling its weight when kept. After whitening for analysis only, the change is a sum of independent mean-zero matrices ±C_e. Their norms are at most 4q/λ and their total second-moment matrix is at most (4q/λ)I. Matrix Bernstein makes this stage a (1±η) approximation except with probability δ/(4m_0), because λη²/q is a sufficiently large multiple of A_0.

The new item count has mean at most 5M/8, and exceeds 3M/4 with probability at most exp(−Ω(M))≤δ/(4m_0). If this recognized size event fails, declare preprocessing failure. Otherwise continue until the count is at most K_0. There are O(log m_0) stages. Their accuracies sum to at most

$$
\frac{\epsilon/100}{1-(3/4)^{1/4}}<\epsilon/4,
$$

so the multiplicative spectral errors compose to 1±ε. A union bound over fewer than m_0 stages bounds the total failure probability by δ. Thus the final support is

$$
O\!\left(\min\left\{m,
  \frac{\log^2(2N)}{\epsilon^2}
       \left[\log(2N)+\log\frac2\delta\right]
 \right\}\right).
\tag{15e}
$$

Only group products, dictionary operations, rational weight comparisons, and fair random bits are used. Each retained weight is doubled at most O(log N) times. The total number of scans is polynomial in N and m. This gives a randomized group-operations implementation of the same support order without dense linear algebra. It does not improve the deterministic guarantee of Theorem 1 or supply a succinct-group polynomial-time algorithm.

## 6. One summary for every correlated generator failure

Attach to each original item e a label set Λ(e), with |Λ(e)|≤d. There are L occurring labels. A query F, |F|≤h, deletes every item whose label set intersects F. Put E_F={e:Λ(e)∩F=∅} and M_F=Σ_{e∈E_F}B_e. The same original-item weights must work for every F. Clip h to L, take d as the actual maximum label count, and define

$$
Q=\sum_{j=0}^{h}\binom Lj,
 \qquad
 \Gamma(h,d)=\frac{(h+d)^{h+d}}{h^hd^d}
 \quad(h,d>0),
\tag{16}
$$

with Γ=1 when h=0 or d=0.

**Theorem 4 (uniform correlated-failure Cayley certificate).** With probability at least 1−δ, a randomized algorithm returns one set H of original generator items, with fixed multipliers ω_e≥0, satisfying

$$
(1-\epsilon)M_F\preceq
 \sum_{e\in H\cap E_F}\omega_eB_e
 \preceq(1+\epsilon)M_F
 \quad\text{simultaneously for every }|F|\le h.
\tag{17}
$$

Its support has size

$$
O\!\left(\min\left\{m,
 \frac{\Gamma(h,d)\log^2(2N)}{\epsilon^2}
 \log\frac{2NQ}{\delta}\right\}\right).
\tag{18}
$$

The algorithm is polynomial in the explicit input length, N, ε^{-1}, and log(1/δ), uniformly when h and d are input parameters. It avoids enumerating the Q failure sets. For h=1 there is also a deterministic polynomial-time construction with support

$$
O\!\left(\min\left\{m,
 (d+1)\epsilon^{-2}\log^2(2N)\log(2N(L+1))
 \right\}\right).
\tag{19}
$$

The implicit constant in (19) uses Γ(1,d)≤e(d+1). No exact (d+1) operator-importance identity is claimed; the exact one-failure trace-leverage identity from the separate PSD manuscript does not automatically extend to operator norm.

**Proof of the robust mass bound.** For e∈X define

$$
t_e(X)=\inf\{t:B_e\preceq tM_X\}
 =\|M_X^{\dagger/2}B_eM_X^{\dagger/2}\|.
$$

This is deletion-monotone: if e∈Y⊆X then t_e(Y)≥t_e(X). Equation (13) gives the hereditary total bound Σ_{e∈X}t_e(X)≤K_G.

Let σ_e=max_{F:e∈E_F}t_e(E_F), and choose a maximizing F_e. Independently put each label into a pool R with probability p=d/(h+d). Let X_R={e:Λ(e)⊆R}. With probability at least p^d(1−p)^h=1/Γ, all own labels of e lie in R and all labels of F_e lie outside R. On that event e∈X_R⊆E_{F_e}, so t_e(X_R)≥σ_e. Pointwise the sum of σ_e over the items with this event is at most Σ_{e∈X_R}t_e(X_R)≤K_G. Taking expectations gives

$$
\sum_e\sigma_e\le\Gamma K_G.
\tag{20}
$$

This proof is the monotone-mass pool lemma from [../../correlated-spectral-regression/manuscripts/correlated-failure-spectral-and-regression-summaries.md](../../correlated-spectral-regression/manuscripts/correlated-failure-spectral-and-regression-summaries.md), now applied to operator norm rather than trace. Its close methodological antecedent, Bernoulli separation followed by sensitivity estimation in In–Li–Woodruff–Wu, ICML 2025, Section 3.1/Lemma 4.3, is credited in that manuscript.

**Computing safe scores without query enumeration.** Draw

$$
J=\lceil8\Gamma\log(2mQ/\delta)\rceil
$$

independent label pools R_1,…,R_J. There are at most mQ surviving item/query pairs. For each pair, the number of separating pools is binomial with mean at least J/Γ. Chernoff and a union bound show that, with probability at least 1−δ/2, every such pair has at least J/(2Γ) separating pools. Define

$$
\widehat\sigma_e=t_e(E)+\frac{2\Gamma}{J}
       \sum_{j:e\in X_{R_j}}t_e(X_{R_j}).
\tag{21}
$$

On the good event these scores dominate every σ_e, whereas on every pool outcome their total T is at most (1+2Γ)K_G≤3ΓK_G. Constant-factor rational upper estimates of each t_e preserve these conclusions up to a constant. The baseline term ensures positive sampling probability for every nonzero original item.

Now perform the PSD sampling experiment with probabilities proportional to (21), independently of the pools. For any F, the surviving normalized random matrices have mean identity on range(M_F) and norm at most T. Matrix Chernoff gives failure probability at most δ/(2Q) using O(Tε^{-2}log(2NQ/δ)) samples. A union bound proves (17). Rank-zero scenarios are automatic. Both random experiments together fail with probability at most δ.

Before generating pools, cap the advertised target at m. In the nontrivial branch, ΓK_Gε^{-2}log(2NQ/δ)<O(m), and K_G≥1, so Γ is polynomially bounded by m. Also log Q≤L log 2. Thus J and all matrix computations are polynomial in the explicit input size, even though Q itself may be exponential. The cases h=0 or d=0 use Theorem 1 directly; an all-zero input returns the empty set. The trivial group N=1 also has only zero generator Laplacians.

For h=1, compute the robust scores over the L+1 scenarios directly, and apply the two-sided trace-exponential estimator to their block-diagonal whitened matrices. Their total dimension is at most N(L+1), their common importance budget is at most Γ(1,d)K_G, and the same item is chosen once for every block. This proves (19) with one shared weight vector. Enumerating all Q scenarios gives a deterministic algorithm for general h with the same size bound, but this is not uniformly polynomial when h is part of the input.

## 7. Correlated failures and directed cuts

For one label per generator, Γ(h,1)<e(h+1). Keeping log Q explicit is essential: log Q can be Θ(h log(L/h)), so (18) can be quadratic in h. The theorem gives polylogarithmically many generator items for fixed h,d, instead of a rank-based bound proportional to N. It does not by itself achieve a bound linear in h for all h.

The certificate retains original generator identities and one final weight per retained item. A failure query only deletes items. There is no recomputation of generator weights at query time. This quantifier differs from finding an unrelated ordinary sparsifier for each surviving subset.

Every output and surviving output remains a weighted Cayley graph, so the group symmetry and regularity are retained. The exact numerical weighted degree is only spectrally approximated; exact preservation of the degree for every label-deletion scenario is not part of the statement.

**Directed-cut corollary.** The same support bounds also give cut sparsifiers of arbitrary weighted directed Cayley graphs, including the correlated-failure version. Here an item is a directed generator and carries its own labels; inverse-pair symmetry is unnecessary. For every S⊆G, the number of arcs of one permutation generator leaving S equals the number entering S, and

$$
|\{x\in S:xg\notin S\}|=\mathbf1_S^*L_g\mathbf1_S.
$$

Apply the PSD theorem to the symmetrized generator matrices L_g, then retain the original directed generator orientations with the resulting multipliers. This preserves all outgoing cut weights, simultaneously for every allowed failure set. It does not assert an approximation of the nonsymmetric directed Laplacian as a bilinear operator. HLM+ already proves the directed-cut reduction; the improvement inherited here is the arbitrary-weight O(ε^{-2}log³N) generator bound and the common-weight failure guarantee.

The general-group O(log³N) bound is not claimed optimal. The public abelian O(log N) theorem is stronger on that subclass. The next genuine mathematical bottleneck is improving the O(log²N) worst-case total operator importance, or bypassing importance sampling for arbitrary noncommuting group representations. A sharper algorithm in a succinct group-operation model would require additional access/computation ideas: the present algorithm explicitly handles matrices of dimension N and does not solve that problem.
