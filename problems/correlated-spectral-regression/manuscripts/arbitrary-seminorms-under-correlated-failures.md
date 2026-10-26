# Common-weight sparsifiers for seminorms under correlated failures

**Abstract.** We transfer ordinary sums-of-seminorms sparsification to a single set of nonnegative item weights valid after all correlated label deletions. A linear feature lift and Gaussian decoding reduce the transfer to ordinary all-query sparsification in dimension $rK$, yielding $O(rK/\epsilon^2)$ support existentially. For one label per item, the uncapped bound is $O(r(h+1)\log(eL/(h+1))/\epsilon^3)$. A constructive version retains the evaluation, roundedness, probability, and extra-logarithm requirements of its ordinary seminorm backend.

## 1. Model and statement

Let $f_1,\ldots,f_m:\mathbb R^r\to\mathbb R_{\ge0}$ be seminorms: they are subadditive and satisfy $f_e(tx)=|t|f_e(x)$. Arbitrary nonnegative input weights can be absorbed into the $f_e$. The dimension $r$ may be reduced by the common kernel of all input seminorms.

Each original item has a failure-label set $\Lambda(e)\subseteq[L]$ of size at most $d$. A query chooses $F\subseteq[L]$, $|F|\le h$, and removes exactly the items whose label sets intersect $F$. Write

$$
E_F=\{e:\Lambda(e)\cap F=\varnothing\},\qquad
 N_F(x)=\sum_{e\in E_F}f_e(x).
\tag{N1}
$$

The output is one nonnegative weight vector $\omega$, chosen before either $F$ or $x$, satisfying

$$
(1-\epsilon)N_F(x)
 \le \sum_{e\in E_F}\omega_e f_e(x)
 \le (1+\epsilon)N_F(x)
 \quad\text{for every allowed }F\text{ and every }x.
\tag{N2}
$$

Items are retained and deleted whole. The weights never change between scenarios.

Here is a general feature-based statement.

**Theorem N1.** Suppose unit vectors $z_e\in\mathbb R^K$ and orthogonal projectors $Q_F$ satisfy

$$
\|Q_Fz_e\|^2=0\quad(e\notin E_F),\qquad
 1-\kappa\le\|Q_Fz_e\|^2\le1\quad(e\in E_F).
\tag{N3}
$$

For $0<\epsilon<1$ and $\kappa\le\epsilon/4$, a vector $\omega$ satisfying (N2) exists with support

$$
O\!\left(\min\{m,rK/\epsilon^2\}\right).
\tag{N4}
$$

This uses the ordinary seminorm support theorem of Basu--Brakensiek--Chen--Putterman--Reis--Zhang, Theorem 1.2. No polynomial construction from arbitrary seminorm evaluation oracles follows from that paper's stated theorem. A constructive alternative is given in Section 4.

For one label per item, including unlabeled items, the label-vector construction supplies

$$
K=1+\min\!\left\{L,\,
  O\!\left(\frac{s\log(eL/s)}{\epsilon}\right)\right\},
 \qquad s=\min\{h+1,L\},
\tag{N5}
$$

where the short code may be chosen by the probabilistic method. Thus, in the uncapped regime $1\le h<L$, the support is

$$
O\!\left(\min\left\{m,\,
  \frac{r(h+1)\log(eL/(h+1))}{\epsilon^3}\right\}\right).
\tag{N6}
$$

For a sampled code with failure probability at most $\zeta$, add $\log(2/\zeta)$ inside the numerator determining its dimension. One successful code event already covers every failure set. There is no later union bound over $\sum_{j\le h}\binom Lj$.

If $h=0$, $d=0$, or no labels occur, apply the ordinary theorem directly with $K=1$. If $r=0$, all items are zero. Replace $h$ and $d$ by their minima with $L$ when necessary; the identity-code branch covers $h\ge L$.

## 2. Gaussian decoding proves the transfer

Identify the lifted query space with matrices $U\in\mathbb R^{r\times K}$. For each original item define

$$
g_e(U)=f_e(Uz_e).
\tag{N7}
$$

Composition with a linear map preserves the seminorm axioms, so the $g_e$ are seminorms on a space of dimension $rK$. Apply the ordinary support theorem at accuracy $\theta=\epsilon/4$. It returns one vector $\omega$ with $O(rK/\theta^2)$ nonzero entries such that

$$
(1-\theta)\sum_e g_e(U)
 \le \sum_e\omega_e g_e(U)
 \le (1+\theta)\sum_e g_e(U)
 \quad\text{for all }U.
\tag{N8}
$$

Fix any $F$ and $x$, only after these weights have been selected. Let $g$ be a centered Gaussian vector with covariance $Q_F$, and substitute $U=xg^T$ into (N8). Absolute homogeneity gives

$$
\mathbb E\,g_e(xg^T)
 =f_e(x)\,\mathbb E|\langle g,z_e\rangle|
 =\sqrt{2/\pi}\,\|Q_Fz_e\|\,f_e(x).
\tag{N9}
$$

Every quantity is nonnegative and integrable. Integrating the fixed all-$U$ inequality is therefore valid, including when the Gaussian covariance is singular. Put $\beta_e=\|Q_Fz_e\|$ and $a=\sqrt{1-\kappa}$. Then

$$
(1-\theta)\sum_{e\in E_F}\beta_e f_e(x)
 \le \sum_{e\in E_F}\omega_e\beta_e f_e(x)
 \le (1+\theta)\sum_{e\in E_F}\beta_e f_e(x),
\tag{N10}
$$

with $a\le\beta_e\le1$. Positivity on both sides gives

$$
(1-\theta)a\,N_F(x)
 \le \sum_{e\in E_F}\omega_e f_e(x)
 \le \frac{1+\theta}{a}\,N_F(x).
\tag{N11}
$$

Since $a\ge1-\kappa$, the choices $\theta=\epsilon/4$ and $\kappa\le\epsilon/4$ imply (N2). The factors $\beta_e$ are used only in the proof; they are never included in the output weights. The argument is pointwise for every $F,x$, so both may be selected adaptively after seeing the output.

This proof uses only the ordinary all-query inequality and absolute homogeneity. Its seminorm hypothesis is needed to invoke the ordinary backend. It is not a new theorem about sparsifying arbitrary nonhomogeneous losses.

## 3. Overlapping labels and an explicit deterministic code option

For completeness, the label features can be constructed as follows. Choose unit label vectors $v_c\in\mathbb R^D$ with restricted isometry constant $\delta_0$ on every set of at most

$$
s=\min\{h+d,L\}
$$

columns. Take $\delta_0^2=\epsilon/(64d)$. Random signs give such vectors, with failure probability at most $\zeta$, in dimension

$$
D=\min\!\left\{L,\,
 \left\lceil\frac{Cd}{\epsilon}
       \left(s\log\frac{eL}{s}+\log\frac2\zeta\right)\right\rceil
          \right\}.
\tag{N12}
$$

Use the identity matrix whenever the cap selects $D=L$. No efficient restricted-isometry certification is claimed for a sampled short code.

Use the graded exterior space

$$
\mathcal E_{\le d}
   =\bigoplus_{j=0}^{\min(d,D)}\bigwedge^j\mathbb R^D,
 \qquad K=\sum_{j=0}^{\min(d,D)}\binom Dj,
\tag{N13}
$$

and let $z_e$ be the normalized wedge of its label vectors, in degree $|\Lambda(e)|$. The empty label set has the scalar unit vector in degree zero. If $P_F$ projects away the span of the failed label vectors, set

$$
Q_F=\bigoplus_j\bigwedge^jP_F.
$$

An item with a failed label is annihilated. For a live item, the principal-angle bound from restricted isometry is

$$
\|\Pi_{\operatorname{span}V_F}
       |_{\operatorname{span}V_{\Lambda(e)}}\|
 \le\frac{\delta_0}{1-\delta_0}.
$$

Consequently each squared singular value of the projection on its label span is at least $1-4\delta_0^2$. Taking the exterior volume gives

$$
\|Q_Fz_e\|^2\ge(1-4\delta_0^2)^{|\Lambda(e)|}
             \ge1-4d\delta_0^2
             \ge1-\epsilon/16.
\tag{N14}
$$

Thus (N3) holds. Equations (N4), (N12), and (N13) give the general bound. For fixed $d$, $h\ge d$, and fixed code confidence, an uncapped form is

$$
O_d\!\left(\min\left\{m,\,
       \frac{r h^d\log^d(2L)}{\epsilon^{d+2}}\right\}\right).
\tag{N15}
$$

For one label per item there is also an explicit deterministic coherence code, described in the companion label-vector manuscript. It has

$$
K=1+O\!\left(
      \min\{L,(h^2+h/\epsilon)\log(2L)\}\right).
\tag{N16}
$$

Substituting it into (N4) gives a deterministic choice of decoding features with an existential ordinary seminorm sparsifier. It does not by itself derandomize, or supply an algorithm for, the optimal ordinary seminorm theorem.

## 4. A constructive version with explicit access assumptions

Jambulapati--Lee--Liu--Sidford, Theorem 1.1, gives an ordinary seminorm sparsifier in dimension $R$ with support

$$
O\!\left(\epsilon^{-2}R
       \log(2R/\epsilon)\,[\log(2R)]^{5/2}\right).
\tag{N17}
$$

Its algorithm is randomized. For a total seminorm that is $(a,b)$-rounded on the orthogonal complement of its kernel, the runtime has the form

$$
(m\,\operatorname{polylog}R+\operatorname{poly}R)
    [\log(mb/a)]^{O(1)}T_{\rm eval},
\tag{N18}
$$

with its stated accuracy dependence and probability contract. The source's full theorem gives logarithmic dependence on the rounding ratio; its abstract states a simpler well-conditioned version.

Apply that theorem to the lifted $g_e$, with $R\le rK$, and then use exactly (N9)--(N11). This gives a constructive simultaneous-failure result with the extra logarithms in (N17), provided one supplies the backend's evaluation and rounding access for the **lifted** total $\sum_e g_e$. One evaluation of $g_e(U)$ consists of computing $Uz_e$ and evaluating $f_e$ there.

Original roundedness is not asserted to imply the needed lifted roundedness automatically. For explicit rational polyhedral seminorms, the lifted common kernel and rational-direction conditioning can be analyzed from their linear forms; that is a concrete application-specific implementation issue. For abstract seminorms provided only as unrestricted evaluation oracles, the sharper existential theorem (N4) is the unconditional claim. No general polynomial-bit algorithm for (N4) is inferred from the September 2026 paper.

More generally, any ordinary seminorm sparsification backend with support $S(R,\theta)$ and an explicit access contract transfers with support $S(rK,\epsilon/4)$, retaining that contract.

## 5. Applications retaining whole original objects

**Sums of block norms.** An item can be an entire matrix $A_e$ and a seminorm $\nu_e$, with

$$
f_e(x)=\nu_e(A_ex).
$$

The theorem retains whole blocks, regardless of their row counts or individual ranks. It includes sums of Euclidean residual norms, sums of maximum coordinate deviations, and mixtures of different block seminorms. Fixed affine residuals are included by homogenization: replace $x$ by $(x,t)$ and use $\nu_e(A_ex-tb_e)$, then restrict to $t=1$. This costs one additional query dimension.

**Hypergraph and hedge cuts.** For a hedge $e$, consisting of any collection of edges, define

$$
f_e(x)=w_e\max_{uv\in e}|x_u-x_v|.
\tag{N19}
$$

This is a seminorm, and at a Boolean cut vector it equals $w_e$ if the hedge crosses the cut, and zero otherwise. A hyperedge is the special case obtained by taking all pairs among its vertices. Therefore (N2) gives one weighted subset of original hyperedges or hedges preserving every cut after every allowed correlated label deletion. The theorem actually preserves the continuous sum in (N19). Its ordinary no-fault specialization is already covered by the September 2026 seminorm theorem; only the uniform failure transfer is asserted here.

**Sums of symmetric submodular functions.** Let $F_e:2^{[n]}\to\mathbb R_{\ge0}$ be symmetric submodular functions with $F_e(\varnothing)=0$. Their Lovász extensions are seminorms on $\mathbb R^n$ and agree with $F_e$ on set indicators. Applying (N2) therefore retains and reweights whole functions so that

$$
\sum_{e:\Lambda(e)\cap F=\varnothing}F_e(S)
$$

is preserved simultaneously for every set $S$ and every allowed failed-label set $F$. The output weights serve every post-deletion objective. The ordinary no-fault theorem is an explicit public result, and no new ordinary submodular sparsification claim is made.

The same Gaussian proof extends to absolutely $p$-homogeneous losses, replacing $\beta_e$ by $\|Q_Fz_e\|^p$, **if** an appropriate ordinary all-query sparsification theorem exists for their lifted class. The September 2026 seminorm theorem does not provide such a theorem for arbitrary $p>1$. In particular it must not be cited as a general optimal-support theorem for squared hypergraph energies.

## 6. Public baselines and attribution

1. **Basu, Brakensiek, Chen, Putterman, Reis, Zhang, _Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms_, September 2026.** Theorem 1.2 supplies $O(r/\epsilon^2)$ ordinary seminorm support; Theorems 1.3 and 1.4 state its hypergraph-cut and symmetric-submodular consequences. The full paper states existence, without an oracle-polynomial construction guarantee for arbitrary input seminorms. The ordinary theorem is the support backend; the present contribution is a single-weight-vector transfer to correlated failures. <https://arxiv.org/pdf/2609.20238>.

2. **Jambulapati, Lee, Liu, Sidford, _Sparsifying Sums of Norms_, FOCS 2023.** Theorem 1.1 gives the constructive bound (N17) and the roundedness/evaluation contract (N18); its treatment includes seminorm kernels. It also treats certain sums of powers subject to additional geometric hypotheses, which are not automatic here. <https://homes.cs.washington.edu/~jrl/papers/pdf/norm-sparsify.pdf>.

3. **Quanrud, _Quotient Sparsification for Submodular Functions_, SODA 2024.** An ordinary rank-$r$ integer polymatroid already admits a weighted quotient sparsifier with $O(r\log(mr)/\epsilon^2)$ support in randomized oracle-polynomial time. This independently covers ordinary whole-block linear-code predicates, so those are not claimed as a new consequence of our research. <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.

4. **Chandrasekaran, Chekuri, Wang, Zhu, _Hedgegraph Polymatroids_, 2025/2026.** Theorem 7 gives ordinary arbitrary weighted hedgegraph partition sparsifiers with $O(n\log n/\epsilon^2)$ original hedges. Thus removing a component-count factor from ordinary hedge sparsification was already known before the September optimal seminorm result. <https://arxiv.org/html/2510.25043v1>.

The new transfer should be evaluated against these ordinary baselines and the separate literature on robust/fault-tolerant summaries. Its key distinction is one common nonnegative weight vector for every allowed correlated deletion, obtained without multiplying the support by the number of scenarios.
