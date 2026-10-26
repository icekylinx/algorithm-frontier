# Optimal-support sparsification of whole subgroup constraints

**Abstract.** A weighted family of subgroup-complement predicates on a finite group $G$ admits a relative-error sparsifier on $O(\log(2|G|)/\epsilon^2)$ whole original items. We prove a hereditary one-sided Gaussian bound by comparison with a stationary coset process, establish a Gaussian coordinate-section symmetrization lemma, and apply the large-volume partial-coloring theorem. The same analysis applies to Euclidean orbit distances. Construction is randomized polynomial time in an explicitly supplied predicate table; the support bound is independent of that table's size.

*Section 5 extends the Gaussian comparison to sums of entire Euclidean orbit-distance metrics. The subgroup proof remains self-contained and does not depend on that extension.*

## 1. Statement and scope

Let $G$ be a finite group, $N=|G|$, and let $H_1,\ldots,H_m$ be arbitrary subgroups, not necessarily normal. For positive weights $w_e$, define
$$
b_e(g)=\mathbf 1[g\notin H_e],
 \qquad
 W(g)=\sum_{e=1}^m w_e b_e(g).
 \tag{1}
$$

**Theorem 1.** For $0<\epsilon<1$, there are nonnegative coefficients $\omega_e$, supported on
$$
O\!\left(\min\{m,\epsilon^{-2}\log(2N)\}\right)
 \tag{2}
$$
original indices, such that
$$
(1-\epsilon)W(g)
 \le \sum_e\omega_e w_e b_e(g)
 \le (1+\epsilon)W(g)
 \qquad(g\in G).
 \tag{3}
$$
The same weights preserve the associated partition metric on every pair:
$$
\sum_e w_e\mathbf 1[gH_e\ne hH_e]
 =W(h^{-1}g).
 \tag{4}
$$
One can replace $N$ by the index of $\bigcap_eH_e$; the coset field below has that many distinct locations. The simpler $\log(2N)$ form avoids degenerate notation.

The proof applies after every positive rescaling and every restriction to a subfamily. It never separates an original subgroup item into differently weighted character items.

**Finite-field whole-block corollary.** Let $A_e$ be arbitrary matrices over $\mathbb F_q$, all with $n$ columns, and let
$$
W(x)=\sum_e w_e\mathbf 1[A_ex\ne0],\qquad x\in\mathbb F_q^n.
 \tag{5}
$$
Then $O(\min\{m,n\log(q)/\epsilon^2\})$ whole original blocks suffice. The same statement holds for affine blocks after replacing $x$ by $(x,1)$, at the cost of one dimension. More precisely, the exponent $n$ can be replaced by the dimension of the sum of the block row spaces in the homogeneous case.

This also applies to arbitrary matrices over $\mathbb Z_q$, with $q$ composite and given in binary: use the finite additive group $\mathbb Z_q^n$. The support bound does not require factoring $q$. This last statement is about support existence; it does not assert a compact polynomial-time algorithm for the optimal bound.

**Arbitrary finite group codes.** Let $A$ be any finite group and let $\mathcal C\le A^m$ be a subgroup code. Apply Theorem 1 with ambient group $\mathcal C$ and the coordinate kernels
$$
H_e=\{c\in\mathcal C:c_e=1_A\}.
$$
Then every weighted Hamming objective $\sum_e w_e\mathbf 1[c_e\ne1_A]$ has a sparsifier with $O(\log(2|\mathcal C|)/\epsilon^2)$ original coordinates, simultaneously for every codeword. Both the alphabet group and the code may be nonabelian. This sharpens the polylogarithmic-overhead public subgroup-code bounds described in Section 6.

**Arbitrary affine subgroup constraints.** The companion note
[affine-constraints-over-arbitrary-finite-groups.md](affine-constraints-over-arbitrary-finite-groups.md) extends (2)--(3) to
$\mathbf1[g\notin a_eH_e]$ for arbitrary cosets in arbitrary finite groups,
with the same $O(\log(2|G|)/\epsilon^2)$ order. It embeds all these cosets simultaneously into subgroups of
$(G\times G)\rtimes C_2$, whose size is $2|G|^2$, and restricts to queries $(g,g^{-1})\tau$. No normality, commutativity, or common accepting query is required. The homogeneous proof in this manuscript remains independent of that extension.

At constant accuracy, the $\log N$ dependence is necessary: in $G=\mathbb F_2^r$, the $r$ coordinate-kernel predicates must all be retained because a query can isolate each coordinate. Graph cut predicates form a further binary subgroup special case, so the usual graph-cut support lower bounds also apply in their standard accuracy range.

With the full $N$-row predicate table explicitly available, the partial-coloring backend has a separation oracle obtained simply by scanning its linear inequalities. Its randomized implementation therefore runs in time polynomial in the table size and the usual accuracy/encoding parameters. In compact finite-field or modular input this table can have $q^n$ rows, and no efficient implicit separation oracle is supplied here.

There is a concrete obstacle to implementing this particular oracle compactly: the companion note *Exact separation for compact sparsification bodies* reduces MaxCut to membership even for scalar binary parity items. Thus an exact compact separation oracle for this route would imply $P=NP$. This is a limitation of the separation-based implementation, not an impossibility theorem for other compact optimal sparsifier algorithms. The full reduction is kept separately in [../../obstruction-boundaries/manuscripts/exact-separation-for-compact-codes.md](../../obstruction-boundaries/manuscripts/exact-separation-for-compact-codes.md).

## 2. A hereditary one-sided Gaussian bound

We use the following form of Slepian comparison: centered Gaussian vectors with matching coordinate variances and larger off-diagonal covariances have larger probabilities of lying below a common threshold in every coordinate. Zero-variance coordinates may be deleted, and positive coordinate normalization handles unequal variances across coordinates.

**Lemma 2.** For independent standard Gaussian $\xi_e$,
$$
\Pr\!\left[
   \sum_e w_e\xi_e b_e(g)\le0
   \text{ for all }g\in G
 \right]\ge N^{-1}.
 \tag{6}
$$
This holds for every real positive $w_e$, including every restricted subfamily.

**Proof.** Independently for each item $e$ and each left coset $C\in G/H_e$, sample a standard Gaussian $T_{e,C}$. Define
$$
F_g=\frac1{\sqrt2}\sum_e w_eT_{e,gH_e},
 \qquad
 Y_g=F_1-F_g,
 \qquad
 Z_g=\sum_e w_e\xi_e b_e(g).
 \tag{7}
$$
The process $F_g$ is invariant in distribution under left translation of $g$, because that translation permutes the cosets for each item. Every sample has a minimum, and all $N$ locations have equal probabilities of being a minimum, so
$$
\Pr[Y_g\le0\text{ for all }g]\ge 1/N.
 \tag{8}
$$
Ties only increase this probability.

For one item, if either $g$ or $h$ lies in $H_e$, its contribution to both relevant covariances vanishes. If both lie outside $H_e$, its covariance contribution to $Y_g,Y_h$ is
$$
\frac{w_e^2}{2}\bigl(1+\mathbf 1[gH_e=hH_e]\bigr)
 \le w_e^2,
 \tag{9}
$$
whereas its contribution to $\operatorname{Cov}(Z_g,Z_h)$ is $w_e^2$. In particular, the coordinate variances match. Slepian comparison gives
$$
\Pr[Z_g\le0\ \forall g]\ge
 \Pr[Y_g\le0\ \forall g]\ge1/N.
 \qquad\square
$$

The same proof works on any finite transitive space with invariant partitions. The group formulation is sufficient for the applications here.

## 3. Gaussian hereditary sections imply a large symmetric error body

Write $\gamma_k$ for standard Gaussian measure in $\mathbb R^k$. For $S\subseteq[m]$, define the coordinate section
$$
K_S=\{x\in\mathbb R^S:(x,0)\in K\}.
$$

**Lemma 3 (Gaussian symmetrization).** There are absolute constants $C_0,C_1$ with the following property. Let $0<p\le1/2$, $0<a\le1/2$, and let $K\subseteq\mathbb R^m$ be a closed convex set containing $a[-1,1]^m$. Suppose
$$
\gamma_{|S|}(K_S)\ge p
 \quad\text{for every }S\subseteq[m],
 \qquad
 m\ge C_0\frac{\log(2/p)}{a^2}.
 \tag{10}
$$
Then
$$
\gamma_m(K\cap(-K))\ge e^{-C_1m}.
 \tag{11}
$$
Consequently the symmetric body
$$
Q=K\cap(-K)\cap[-1,1]^m
$$
has Gaussian measure at least $e^{-C_2m}$ and volume at least $c^m$, for absolute $C_2$ and $c>0$.

The argument follows the coordinate-section and separating-hyperplane organization of Reis--Rothvoss, but keeps Gaussian measure throughout. The reflection identity used below replaces their Lebesgue-volume reflection argument.

### 3.1 Every normal has a large section near the origin

Set
$$
\lambda=\sqrt{2\log(2/p)},
 \qquad
 r=10\lambda/\sqrt m.
 \tag{12}
$$
Taking $C_0$ sufficiently large ensures $r\le a$. We first show that, for every $v\in\mathbb R^m$,
$$
K(v):=K\cap\{x:\langle v,x\rangle\le r\|v\|_1\}
 \quad\text{satisfies}\quad
 \gamma_m(K(v))\ge e^{-C_3m}.
 \tag{13}
$$

Order coordinates so that $|v_1|\ge\cdots\ge|v_m|$. Put $m_1=m$, $m_{j+1}=\lfloor m_j/2\rfloor$, and stop at the first $\ell$ with $m_\ell\le4\lambda^2$. Define
$$
I_j=(m_{j+1},m_j]\quad(j<\ell),
 \qquad I_\ell=[m_\ell].
$$
Thus early blocks contain the smaller coordinates and the last block contains the largest ones.

For $j<\ell$, let
$$
Q_j=K_{I_j}\cap
 \{x:\langle v_{I_j},x\rangle
              \le\lambda\|v_{I_j}\|_2\}.
$$
The standard Gaussian tail bound gives
$$
\gamma_{|I_j|}(Q_j)\ge p-e^{-\lambda^2/2}\ge p/2.
 \tag{14}
$$
For the last block use $Q_\ell=a[-1,1]^{I_\ell}\subseteq K_{I_\ell}$. Its measure is at least $(a/2)^{m_\ell}$.

Consider the product set with coordinates in $2^{-j}Q_j$ for $j<\ell$, and in $2^{-(\ell-1)}Q_\ell$ on $I_\ell$. The scaling coefficients sum to one, so convexity places this product inside $K$.

For an early block, $m_{j+1}\ge m_j/3$ and
$$
\|v_{I_j}\|_2
 \le \sqrt{m_j}\,\frac{\|v\|_1}{m_{j+1}}
 \le \frac{3\|v\|_1}{\sqrt{m_j}}
 \le\frac{3\cdot2^{j/2}}{\sqrt m}\|v\|_1.
$$
Hence the sum of the early-block contributions to $\langle v,x\rangle$ is at most
$$
\frac{3\lambda\|v\|_1}{\sqrt m}
 \sum_{j\ge1}2^{-j/2}.
$$
On the last block, $a\le1/2\le\lambda/\sqrt{m_\ell}$, and
$$
\frac{2^{-(\ell-1)}}{\sqrt{m_\ell}}
 \le\frac{\sqrt2}{\sqrt m}.
$$
Its contribution is therefore at most $\sqrt2\lambda\|v\|_1/\sqrt m$. Since
$3\sum_{j\ge1}2^{-j/2}+\sqrt2<10$, the product set lies in $K(v)$.

For any measurable $A\subseteq\mathbb R^s$ and $0<t\le1$,
$$
\gamma_s(tA)\ge t^s\gamma_s(A).
 \tag{15}
$$
This follows directly by changing variables in the Gaussian density. The logarithm of the reciprocal product measure is thus at most
$$
(\log2)
 \left(\sum_{j<\ell}j|I_j|+(\ell-1)m_\ell\right)
 +(\ell-1)\log(2/p)
 +m_\ell\log(2/a).
 \tag{16}
$$
The first parenthesis equals $\sum_{j<\ell}m_j<2m$. The second term is $O(m)$, using
$\ell-1\le1+\log_2(m/\lambda^2)$ and
$\lambda^2\log(m/\lambda^2)=O(m)$.
For the last term, $m_\ell\le4\lambda^2$, while
$\lambda^2=O(ma^2)$ by (10), and
$a^2\log(2/a)=O(1)$.
Thus (16) is $O(m)$, proving (13).

### 3.2 A Gaussian reflection center

Define
$$
f_K(z)=
 \Pr_{Y\sim N(0,I_m/2)}[z+Y\in K,\ z-Y\in K].
 \tag{17}
$$
The integrand is log-concave jointly in $z,Y$; integrating $Y$ preserves log-concavity by Prékopa's theorem. Thus every positive superlevel set of $f_K$ is convex. For closed $K$, these superlevel sets are closed. A center with $f_K(z)>0$ belongs to $K$.

Let $A$ be any closed convex set. If $X_1,X_2$ are independent standard Gaussians, then
$$
Z=(X_1+X_2)/2,\qquad Y=(X_1-X_2)/2
$$
are independent $N(0,I_m/2)$ vectors. Therefore
$$
\gamma_m(A)^2=
 \mathbb E_{Z\sim N(0,I_m/2)} f_A(Z).
 \tag{18}
$$
In particular, whenever $\gamma_m(A)\ge q$, there is a $z\in A$ with
$f_A(z)\ge q^2/2$. The factor $1/2$ avoids any supremum-attainment issue.

Apply this to every $A=K(v)$, with the common lower bound $q=e^{-C_3m}$ from (13). The convex closed set
$$
S=\{z:f_K(z)\ge q^2/2\}
$$
must meet $r[-1,1]^m$. Otherwise a strict separating hyperplane would give some $v$ with
$$
\langle v,z\rangle>r\|v\|_1\quad(z\in S).
$$
But (18), applied to $K(v)$, supplies a center in $K(v)$ with $f_K(z)\ge f_{K(v)}(z)\ge q^2/2$, a contradiction.

Choose such a center $z$. Since $\|z\|_\infty\le r\le a$, both $z$ and $-z$ belong to $K$. Convexity then gives
$$
\frac12\bigl((K-z)\cap(z-K)\bigr)
 \subseteq K\cap(-K).
 \tag{19}
$$
Converting the variance-$1/2$ measure in (17) to standard Gaussian measure and scaling by $1/2$ costs at most $2^{3m/2}$ in the reciprocal measure. Equations (17)--(19) prove (11).

Finally, $K\cap(-K)$ and the unit cube are symmetric convex sets. The Gaussian correlation inequality yields
$$
\gamma_m(Q)\ge
 \gamma_m(K\cap(-K))\,\gamma_1([-1,1])^m
 \ge e^{-C_2m}.
 \tag{20}
$$
The standard Gaussian density is at most $(2\pi)^{-m/2}$, so (20) also gives $\operatorname{Vol}_m(Q)\ge c^m$. This proves Lemma 3. $\square$

## 4. From Gaussian sections to sparsification

If $N=1$, every predicate is identically zero and the empty output suffices. Assume $N\ge2$.

For current positive weights $w$ and a parameter $a$, define the unbounded one-sided perturbation body
$$
K_a=\left\{
 z\in\mathbb R^m:
 \sum_e w_ez_e b_e(g)\le a W(g)
 \text{ for every }g\in G
 \right\}.
 \tag{21}
$$
It contains $a[-1,1]^m$. Every coordinate section contains its homogeneous one-sided cone. Lemma 2 therefore supplies the hereditary Gaussian lower bound $p=1/N$.

Whenever $m\ge C_0\log(2N)/a^2$, Lemma 3 gives volume at least $c^m$ for
$$
Q_a=K_a\cap(-K_a)\cap[-1,1]^m
 =
 \left\{z\in[-1,1]^m:
 \left|\sum_e w_ez_e b_e(g)\right|\le aW(g)
 \ \forall g\right\}.
 \tag{22}
$$

We use the standard large-volume partial-coloring theorem in exactly its dilated form: for a universal $c>0$, there is an absolute $s=s(c)$ such that every symmetric convex body $Q\subseteq[-1,1]^m$ of volume at least $c^m$ contains a vector
$$
z\in sQ\cap[-1,1]^m
$$
with at least $m/2$ coordinates in $\{-1,1\}$. This is Theorem 7 in the July version of Reis--Rothvoss, based on their earlier Gaussian partial-coloring theorem. The constant dilation $s$ is necessary and is included in the error calculation.

Replace $z$ by $-z$ if needed so that at least $m/4$ coordinates equal $-1$, and update
$$
w'_e=w_e(1+z_e).
$$
All weights remain nonnegative, support decreases by at least a factor $3/4$, and every query value changes by a factor in $[1-sa,1+sa]$.

At a stage with $m_t$ remaining items, take
$$
a_t=\sqrt{C_0\log(2N)/m_t}.
 \tag{23}
$$
Stop when $m_t\le M=C\log(2N)/\epsilon^2$, with a sufficiently large absolute $C$. Earlier error parameters form a geometrically increasing sequence, since support decreases by a factor $3/4$. In particular
$$
\sum_{t:\,m_t>M} s a_t
 \le
 \frac{s\sqrt{C_0/C}}{1-\sqrt{3/4}}\,\epsilon.
 \tag{24}
$$
Choose $C$ so that this sum is at most $\epsilon/4$, and so that every invoked $a_t\le1/2$. Multiplying the one-stage inequalities then yields (3). Zero queries stay zero exactly because all coefficients and weights are nonnegative. Starting with $m\le M$ simply retains the input.

This closes the support proof. There is no need to establish a lower bound for the uniform-cube mass of the original homogeneous cone; the Gaussian symmetrization handles the missing bridge directly.

## 5. A broader transfer: entire Euclidean orbit-distance metrics

The Gaussian comparison is not specific to indicator predicates.

**Theorem 4.** Let $\rho_e:G\to O(V_e)$ be arbitrary real orthogonal representations of a finite group $G$, and choose vectors $v_e\in V_e$. Define
$$
d_e(g,h)=\|\rho_e(g)v_e-\rho_e(h)v_e\|_2,
 \qquad
 D(g,h)=\sum_e w_e d_e(g,h).
 \tag{25}
$$
There are nonnegative common weights $\omega_e$, supported on
$$
O(\min\{m,\log(2|G|)/\epsilon^2\})
$$
original metric items, for which
$$
(1-\epsilon)D(g,h)
 \le \sum_e\omega_e w_e d_e(g,h)
 \le (1+\epsilon)D(g,h)
 \quad\text{for every }g,h\in G.
 \tag{26}
$$
There is no dependence on the sum of the representation dimensions in the support count. An item can have a nontrivial kernel, so the individual $d_e$ and their sum may be pseudometrics.

**Proof of the required one-sided lemma.** Write
$$
f_e(g)=d_e(1,g)=\|v_e-\rho_e(g)v_e\|_2,
 \qquad
 Z_g=\sum_e w_e\xi_e f_e(g).
$$
Independently sample standard Gaussian $T_e\in V_e$, and put
$$
F_g=\sum_e w_e\langle T_e,\rho_e(g)v_e\rangle,
 \qquad Y_g=F_1-F_g.
 \tag{27}
$$
Left translation of $g$ rotates each $T_e$ orthogonally and therefore preserves the joint law of $F$. Hence the identity is a minimum with probability at least $1/|G|$. Moreover,
$$
\operatorname{Var}(Y_g)=\sum_e w_e^2 f_e(g)^2
 =\operatorname{Var}(Z_g),
$$
and Cauchy--Schwarz gives
$$
\operatorname{Cov}(Y_g,Y_h)
 =
 \sum_e w_e^2
 \langle v_e-\rho_e(g)v_e,v_e-\rho_e(h)v_e\rangle
 \le\sum_e w_e^2 f_e(g)f_e(h)
 =\operatorname{Cov}(Z_g,Z_h).
 \tag{28}
$$
Slepian comparison proves the same hereditary lower bound (6), with $b_e$ replaced by $f_e$. Their nonnegativity is the only other property used in Sections 3--4, so those sections give simultaneous preservation of $\sum_e w_e f_e(g)$. Finally
$d_e(g,h)=f_e(h^{-1}g)$, proving all-pairs preservation. $\square$

For a subgroup $H_e$, take its permutation representation on left cosets and $v_e$ equal to the indicator of the identity coset divided by $\sqrt2$. Its orbit distance is exactly $\mathbf 1[g\notin H_e]$. Thus this theorem contains the subgroup result, while the original proof of Lemma 2 makes that special case independently transparent.

A concrete class beyond whole OR predicates is
$$
f_e(x)=
 \sqrt{\sum_j c_{ej}\,
       \mathbf 1[\langle a_{ej},x\rangle=1]},
 \qquad
 a_{ej}\in\mathbb F_2^n,\quad c_{ej}\ge0.
 \tag{29}
$$
Choose a direct sum of the sign characters
$\rho_e(x)_{jj}=(-1)^{\langle a_{ej},x\rangle}$, and vector coordinates
$(v_e)_j=\sqrt{c_{ej}}/2$. Equation (29) is precisely its Euclidean orbit distance. Therefore $O(n/\epsilon^2)$ entire weighted parity-norm blocks preserve their sum for every $x$, independently of the number of component parities in a block.

The square root in (25) and (29) is essential to the proof. General squared orbit distances have different Gaussian coordinate variances, so (28) does not prove the same statement for them. In particular, this is not an optimal spectral Cayley-generator theorem for arbitrary nonabelian groups. The optimal ordinary seminorm theorem also does not directly give (26): its ambient real dimension can be as large as the entire orbit span, whereas the support bound here depends only on the logarithm of the orbit size.

The companion note [transitive-metrics-and-group-alignment.md](transitive-metrics-and-group-alignment.md) proves the stronger $N$-point formulation: whenever a common transitive action preserves each Hilbertian pseudometric individually, $O(\log(2N)/\epsilon^2)$ original metrics suffice. Centered Gram matrices supply the stationary Gaussian field, so the bound depends on the number of orbit points rather than the order of an unnecessarily large acting group. That note also gives a counterexample showing that transitivity of the total metric alone is insufficient.

The metric theorem is an existence claim. An explicitly supplied anchor-distance table provides a separation oracle in the corresponding real-arithmetic or value-oracle model; additional bit-complexity conclusions require an evaluation/precision contract for those distances. The binary subgroup theorem above has an exact rational predicate table and does not have this additional numerical issue.

## 6. Baselines and algorithmic limits

1. **Quanrud, _Quotient Sparsification for Submodular Functions_, SODA 2024.** Theorem 1.1 gives $O(r\log(mr)/\epsilon^2)$ support for real-valued monotone submodular functions of total value $r$, normalized so every positive marginal is at least one, in randomized evaluation-oracle polynomial time. The rank function $S\mapsto\dim\sum_{e\in S}\operatorname{row}(A_e)$ shows that ordinary finite-field whole-block predicates are already included. More generally, **Corollary 1.7 on joint entropy directly includes all the subgroup predicates of this manuscript**, including nonnormal subgroups; the reduction is detailed below. The support/error part of adaptive repeated sparsification gives $O(r\log(2r/\epsilon)/\epsilon^2)$, so the strongest checked subgroup baseline has only one remaining logarithm. This repeated-application consequence is not attributed as a verbatim theorem of Quanrud. For finite-field blocks one should also compare the ordinary dimension-rank version, which can be better when the field is large. <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>.

2. **Basu, Kothari, Meka, Tudose, _Optimal Sparsifiers for Abelian Cayley Graphs_, July 2026.** This proves optimal $O(\log|G|/\epsilon^2)$ support for individual abelian Cayley generators, using the Reis--Rothvoss framework. A whole subgroup item averages many characters with one shared coefficient. Sparsifying those characters separately does not retain whole original items, so their theorem is an antecedent rather than a direct invocation for (5). The present Gaussian comparison treats that shared coefficient explicitly. <https://arxiv.org/html/2607.08261v1>.

3. **Reis and Rothvoss, _Linear-size $\ell_1$ Sparsifiers_, July 2026 version.** Section 5 supplies the coordinate-section symmetrization strategy and Theorem 7 supplies the partial-coloring theorem with constant dilation. Their Theorem 22 assumes hereditary Lebesgue volume. Lemma 3 above is a Gaussian variant with an unbounded one-sided body, a midpoint reflection identity, and a final Gaussian-correlation intersection. The main ordinary $\ell_1$ theorem and the partial-coloring framework are not claimed here. <https://arxiv.org/html/2606.28147v2>.

4. **Basu, Brakensiek, Chen, Putterman, Reis, Zhang, _Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms_, September 2026.** This already proves optimal ordinary seminorm, hypergraph-cut, and symmetric-submodular support, Arbitrary finite-field block predicates are periodic/discrete and are not automatically real seminorms in $n$ dimensions; no new ordinary hypergraph-cut result is asserted here. <https://arxiv.org/pdf/2609.20238>.

5. **Slepian, _The One-Sided Barrier Problem for Gaussian Noise_, Bell System Technical Journal 41 (1962).** The Gaussian comparison used in Lemma 2 is classical. <https://doi.org/10.1002/j.1538-7305.1962.tb02419.x>.

6. **Royen, _A Simple Proof of the Gaussian Correlation Conjecture Extended to Multivariate Gamma Distributions_ (2014).** Equation (20) uses this standard correlation theorem; it is not a new correlation inequality. <https://arxiv.org/abs/1408.1028>.

7. **Reis and Rothvoss, _Vector Balancing in Lebesgue Spaces_, Random Structures & Algorithms 62 (2023).** This is the constructive arbitrary-constant Gaussian-mass partial-coloring backend. <https://arxiv.org/abs/2007.05634>.

8. **Brakensiek and Guruswami, _Redundancy Is All You Need (for CSP Sparsification)_, STOC 2025, expanded May 2026 version.** Theorem 6.8 explicitly gives weighted subgroup-code sparsifiers for every $\mathcal C\le A^m$, including nonabelian $A$, of size $O(\log|\mathcal C|\,\log^6m/\epsilon^2)$. Thus nonabelian group-code sparsification itself is a public model and theorem. The coordinate-kernel corollary above removes its overhead. The following chain-length theorem improves that explicit code bound, and the entropy reduction to Quanrud gives the still stronger single-logarithm baseline relevant here. The ordered-product word equations discussed in this literature can have zero sets that are not subgroups and are not automatically covered by Theorem 1. <https://arxiv.org/html/2411.03451v2>.

9. **Brakensiek, Guruswami, Putterman, _Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction_, ICALP 2026.** Theorem 1.2 gives, for arbitrary input weights and chain length $d$, support
$$
O\!\left(
 \frac{d\log^2(2d/\epsilon)
        [\log\log(4d/\epsilon)]^2}{\epsilon^2}
 \right),
$$
independent of the original number of items. For subgroup-complement predicates, the union of violation supports of a query set $T$ depends only on the subgroup $\langle T\rangle$: an item is unviolated exactly when that subgroup lies in its acceptance subgroup. A strict union chain therefore forces strict increases of generated subgroups, each by index at least two; hence $d\le O(\log|G|)$. For field block kernels, use the generated linear span to obtain $d\le O(n)$. This is a broad general set-system baseline, but it is not the strongest support consequence for the subgroup model: the entropy reduction to Quanrud below leaves only one logarithm. Their theorem is not an efficient arbitrary-code construction. <https://arxiv.org/html/2605.01508v1>.

### 6.1 The entropy-quotient baseline for arbitrary subgroups

Let $U$ be uniform on $G$, and let $X_e=UH_e$ be its left-coset random variable. For $S\subseteq[m]$, write $K_S=\bigcap_{e\in S}H_e$, with $K_\varnothing=G$. Two elements of $G$ have the same joint coset tuple precisely when they lie in the same left coset of $K_S$. Every fiber therefore has size $|K_S|$, and
$$
f(S)=H((X_e)_{e\in S})
     =\log_2[G:K_S].
 \tag{30}
$$
This is a normalized monotone submodular function by the standard joint-entropy inequality. Its marginal is
$$
f(S+e)-f(S)=\log_2[K_S:K_S\cap H_e],
 \tag{31}
$$
which is either zero or at least one. No normality assumption is used. Its total value
$$
r=f([m])=\log_2[G:\bigcap_eH_e]\le\log_2|G|
 \tag{32}
$$
is exactly the normalized entropy parameter in Quanrud's Corollary 1.7.

For a query $g$, let $Z_g=\{e:g\in H_e\}$. If $e\notin Z_g$, the element $g$ belongs to $K_{Z_g}$ but not to $H_e$, so (31) is positive. Hence $Z_g$ is closed for $f$, and its complement is a quotient. The same argument works after every restriction of the item set. Quanrud's weighted quotient theorem therefore preserves all the original subgroup-complement queries.

The restriction-closed repeated-application argument in [../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md](../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md) consequently yields the inherited support baseline
$$
O\!\left(\frac{r\log(2r/\epsilon)}{\epsilon^2}\right).
 \tag{33}
$$
Its support and error calculation applies to the real-valued entropy function. The integer-rank bit-complexity implementation in that companion note does **not** automatically apply to logarithmic oracle values: an evaluation/comparison precision contract must be supplied for an algorithmic claim. Quanrud's own theorem explicitly uses an entropy evaluation oracle. Neither (33) nor this reduction silently supplies a compact polynomial-time subgroup-intersection entropy oracle.

The later companion [rational-quotient-ranks-from-weak-oracles.md](rational-quotient-ranks-from-weak-oracles.md) closes the logarithmic-value precision gap whenever the indices $[G:K_S]$ themselves have an exact polynomial-time integer oracle. Its canonical-key concave rounding produces an exact rational submodular surrogate with identical closure, unit positive-marginal gap, and rank $O(r)$. This supplies a polynomial-bit quotient implementation under that index-oracle condition, without exact transcendental comparisons. The condition is not assumed for arbitrary succinct nonabelian group presentations.

For arbitrary coset predicates, the same baseline follows after the established common wreath-group reduction in [affine-constraints-over-arbitrary-finite-groups.md](affine-constraints-over-arbitrary-finite-groups.md), whose ambient group has size $2|G|^2$. Thus the optimal subgroup and coset support theorem in this work removes the last support logarithm relative to the strongest checked entropy-quotient consequence. The entropy comparison isolates the final logarithmic factor removed by the Gaussian proof.

The mathematical contributions are the one-sided Gaussian comparisons, the Gaussian hereditary-section transfer in Lemma 3, and their whole-subgroup and orbit-distance sparsification consequences. In particular, no compact polynomial-time optimal block-code algorithm, deterministic optimal construction, or optimal spectral Cayley-generator theorem for general nonabelian groups follows from the argument.
