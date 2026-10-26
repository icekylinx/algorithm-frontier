# Sparsifying sums of transitive Hilbert metrics and finite-group alignment losses

**Abstract.** A family of Hilbertian pseudometrics on an $N$-point space has a whole-item relative-error sparsifier of size $O(\log(2N)/\epsilon^2)$ whenever one transitive action preserves each item individually. Centered Gram matrices yield the required stationary Gaussian process. A wreath representation extends the result to two-anchor finite-group alignment losses, and Bernstein transforms give bounded nonlinear examples. The construction is polynomial in an explicit query table under its stated numerical access contract.

## 1. The $N$-point theorem

Let $X$ be a finite set, $N=|X|\ge2$. Each original item $e\in[m]$ is a Hilbertian pseudometric
$$
d_e(x,y)=\|\phi_e(x)-\phi_e(y)\|_2
 \qquad(x,y\in X),
 \tag{T1}
$$
with an arbitrary finite-dimensional real embedding $\phi_e$. The item dimensions can differ. Complex Hilbert embeddings can be regarded as real embeddings.

Assume that a common group $\Gamma$ acts transitively on $X$ and preserves **every item individually**:
$$
d_e(gx,gy)=d_e(x,y)
 \qquad(e\in[m],\,g\in\Gamma,\,x,y\in X).
 \tag{T2}
$$
For positive weights $w_e$, define
$$
D(x,y)=\sum_e w_e d_e(x,y).
 \tag{T3}
$$

**Theorem 1.** For $0<\epsilon<1$, there are coefficients $\omega_e\ge0$, supported on
$$
O\!\left(\min\left\{m,\frac{\log(2N)}{\epsilon^2}\right\}\right)
 \tag{T4}
$$
original indices, such that
$$
(1-\epsilon)D(x,y)
 \le \sum_e\omega_e w_e d_e(x,y)
 \le (1+\epsilon)D(x,y)
 \qquad(x,y\in X).
 \tag{T5}
$$
No embedding coordinate inside an item is reweighted separately. The group may be represented by a much larger permutation group; its order does not appear in (T4).

For $N=1$, every item vanishes and the empty output suffices. Identically zero items and zero-weight items may always be discarded.

**Optional exact total weight.** The same support order can preserve
$\sum_e\omega_ew_e=\sum_e w_e$ exactly as well as (T5). In this variant, identically zero original items remain available, and their weights count toward this total. If $N=1$, one original index with the total weight suffices. The normalization argument is at the end of Section 3 and also applies to the group-loss corollaries below.

## 2. A centered stationary Gaussian process

Fix an anchor $o\in X$. Center each embedding:
$$
u_e(x)=\phi_e(x)-\frac1N\sum_{z\in X}\phi_e(z).
 \tag{T6}
$$
Its Gram matrix is determined entirely by the squared distances:
$$
\begin{aligned}
 \langle u_e(x),u_e(y)\rangle
 ={}&-\frac12d_e(x,y)^2
 +\frac1{2N}\sum_z d_e(x,z)^2\\
 &+\frac1{2N}\sum_z d_e(y,z)^2
 -\frac1{2N^2}\sum_{z,z'}d_e(z,z')^2.
\end{aligned}
 \tag{T7}
$$
This follows by expanding the squared distances and canceling their common mean terms. Equation (T2), together with the fact that $g$ permutes $X$, shows that (T7) is invariant when both arguments are acted on by $g$.

Independently for each item, sample a standard Gaussian vector $T_e$ in the span of its centered embedding, and put
$$
F_x=\sum_e w_e\langle T_e,u_e(x)\rangle.
 \tag{T8}
$$
The process is centered Gaussian. Its covariance is
$$
\mathrm{Cov}(F_x,F_y)
   =\sum_e w_e^2\langle u_e(x),u_e(y)\rangle,
$$
which is invariant under the common transitive action. Thus the entire joint law is invariant. Every sample has a minimum, and every point has the same probability of being a minimum. Consequently
$$
\Pr[F_o\le F_x\text{ for every }x]\ge\frac1N.
 \tag{T9}
$$
Ties only increase this probability; no nondegeneracy assumption is needed.

Now let the $\xi_e$ be independent scalar standard Gaussians and define
$$
Y_x=F_o-F_x,\qquad
 Z_x=\sum_e w_e\xi_e d_e(o,x).
 \tag{T10}
$$
For every coordinate,
$$
\mathrm{Var}(Y_x)
 =\sum_e w_e^2d_e(o,x)^2
 =\mathrm{Var}(Z_x).
 \tag{T11}
$$
For two coordinates, Cauchy--Schwarz gives
$$
\begin{aligned}
 \mathrm{Cov}(Y_x,Y_y)
 &=\sum_e w_e^2
   \langle u_e(o)-u_e(x),u_e(o)-u_e(y)\rangle\\
 &\le\sum_e w_e^2 d_e(o,x)d_e(o,y)
 =\mathrm{Cov}(Z_x,Z_y).
\end{aligned}
 \tag{T12}
$$
Discard the coordinates with zero variance and normalize the other coordinates to variance one. The event that every coordinate is at most zero is unchanged. Slepian's Gaussian comparison theorem and (T9) imply
$$
\Pr_{\xi}\!\left[
   \sum_e w_e\xi_e d_e(o,x)\le0
   \text{ for every }x\in X
 \right]\ge\frac1N.
 \tag{T13}
$$

The proof applies after any positive rescaling and any restriction to a subfamily of items: stationarity, the variance identity, and the covariance comparison all remain valid. This hereditary guarantee is the ingredient needed for sparsification.

## 3. From the cone bound to whole-item support

The companion manuscript [optimal-whole-subgroup-constraints.md](optimal-whole-subgroup-constraints.md) proves the following Gaussian-section principle.

**Gaussian-section principle.** Suppose nonnegative functions $f_e:Q\to\mathbb R_{\ge0}$ have the property that, for every positive weighting and every restricted subfamily,
$$
\Pr_\xi\!\left[
 \sum_e w_e\xi_e f_e(q)\le0\quad\forall q\in Q
 \right]\ge p.
 \tag{T14}
$$
Then their weighted sum has a relative-error sparsifier on
$$
O\bigl(\min\{m,\log(2/p)/\epsilon^2\}\bigr)
 \tag{T15}
$$
whole original functions.

Here is the support mechanism. For a current positive weighting and $0<a\le1/2$, define
$$
K_a=\left\{z:
 \sum_e w_ez_e f_e(q)
 \le a\sum_e w_ef_e(q)\quad\forall q
 \right\}.
 \tag{T16}
$$
It contains $a[-1,1]^m$, and each coordinate section contains a cone of Gaussian mass at least $p$. The companion Gaussian symmetrization lemma implies that
$$
Q_a=K_a\cap(-K_a)\cap[-1,1]^m
$$
has volume at least $c^m$ when
$m\ge C\log(2/p)/a^2$. Its proof uses hereditary Gaussian sections, a midpoint reflection identity, log-concavity, and Gaussian correlation.

The large-volume partial-coloring theorem of Reis--Rothvoss gives a vector in $sQ_a\cap[-1,1]^m$, for constant $s$, with at least $m/2$ coordinates equal to $1$ or $-1$. Choose its sign to make at least $m/4$ coordinates equal to $-1$, and update $w_e$ to $w_e(1+z_e)$. This deletes at least a quarter of the items while changing every query by a multiplicative factor in $[1-sa,1+sa]$.

At support size $m_t$, choose $a_t=\sqrt{C\log(2/p)/m_t}$ and stop at $M=C'\log(2/p)/\epsilon^2$. The sum of the stage errors is bounded by a geometric series:
$$
\sum_{t:m_t>M}sa_t
 \le
 \frac{s\sqrt{C/C'}}{1-\sqrt{3/4}}\epsilon.
 \tag{T17}
$$
A sufficiently large $C'$ makes this at most $\epsilon/4$, which yields (T15) on multiplying the one-stage guarantees.

Apply the principle to $f_e(x)=d_e(o,x)$ and $p=1/N$ from (T13). This preserves every anchor distance. For any pair $x,y$, choose $g$ with $go=x$. By the itemwise invariance,
$$
d_e(x,y)=d_e(o,g^{-1}y)
 \qquad\text{for every }e.
 \tag{T18}
$$
The same weights therefore preserve the pair $(x,y)$. This proves Theorem 1.

The theorem consequently also preserves every nonnegative weighted sum of pair distances. Objectives formed by minimizing over a specified set of such candidates inherit the usual multiplicative approximation implication. This observation does not supply an efficient algorithm for finding the minimizing candidate.

### Exact total-weight normalization

Replace $X$ by $X\times C_2$ and each item by
$$
\widetilde d_e((x,b),(y,c))
 =\sqrt{d_e(x,y)^2+\mathbf1[b\ne c]}.
 \tag{TN1}
$$
This is a Hilbertian pseudometric, using the direct sum of the original embedding with the scalar embedding $b\mapsto b\in\{0,1\}$. The common action $\Gamma\times C_2$ is transitive and preserves every augmented item. On equal-bit pairs the distances are the original ones, whereas
$\widetilde d_e((o,0),(o,1))=1$ for every item.

Apply Theorem 1 to these $2N$ points with error $\eta=\epsilon/4$. Its bit-changing anchor query approximates the total input weight within $1\pm\eta$. Globally rescale the output weights to make that total exact. The factors on each original pair then lie in
$$
\left[\frac{1-\eta}{1+\eta},
       \frac{1+\eta}{1-\eta}\right]
 \subseteq[1-\epsilon,1+\epsilon].
 \tag{TN2}
$$
No item is added to the output list: (TN1) is only an auxiliary construction of the coefficients. Original zero-loss items have nonzero augmented distances and are kept available if needed for the total-weight requirement. The same augmentation can be applied to the wreath-orbit metrics used below, giving the exact-total-weight variant for arbitrary anchored and Bernstein-transformed losses as well.

### Computational model

Only an anchor-distance table with $N$ rows is needed to specify the error body. If it is explicitly supplied and the distance values admit the separation and precision access required by the partial-coloring backend, its randomized construction is polynomial in that table size. For rational distance tables this is an ordinary rational-input model.

An embedding with rational coordinates can produce irrational square-root distances. The support theorem is exact over the reals; an additional evaluation/weak-separation precision contract is needed for a bit-complexity implementation in that representation. No polynomial bit-complexity conclusion for arbitrary real embeddings is silently included.

The method may enumerate all $N$ group elements or orbit points. It is not, in general, polynomial in $\log N$ or in a compact presentation of the action.

## 4. Arbitrary two-anchor losses over a finite group

Let $G$ be a finite group. For every item $e$, let
$\rho_e:G\to O(V_e)$ be an orthogonal representation and choose arbitrary vectors $u_e,v_e\in V_e$. Consider
$$
\ell_e(g)=\|u_e-\rho_e(g)v_e\|_2,\qquad
 L(g)=\sum_e w_e\ell_e(g).
 \tag{T19}
$$
The two vectors need not have equal norms, lie on the same orbit, or be consistently aligned by any one group element.

**Corollary 2.** There is a nonnegative reweighting of
$$
O\!\left(\min\left\{m,
 \frac{\log(2|G|)}{\epsilon^2}\right\}\right)
 \tag{T20}
$$
whole original pairs preserving $L(g)$ within $1\pm\epsilon$ simultaneously for every $g\in G$.

**Proof.** On $\widetilde G=(G\times G)\rtimes C_2$, define an orthogonal representation on $V_e\oplus V_e$:
$$
\widetilde\rho_e(a,b)
   =\mathrm{diag}(\rho_e(a),\rho_e(b)),
 \qquad
 \widetilde\rho_e(\tau)(x,y)=(y,x).
 \tag{T21}
$$
Take $z_e=(u_e,v_e)/\sqrt2$. For the same embedded query
$q(g)=(g,g^{-1})\tau$ as in the affine-group note,
$$
\begin{aligned}
 \|z_e-\widetilde\rho_e(q(g))z_e\|_2^2
 &=\frac12\left(
   \|u_e-\rho_e(g)v_e\|_2^2
   +\|v_e-\rho_e(g^{-1})u_e\|_2^2
 \right)\\
 &=\|u_e-\rho_e(g)v_e\|_2^2.
\end{aligned}
 \tag{T22}
$$
The second equality uses orthogonality. Thus the original two-anchor loss is exactly a one-anchor orbit distance in the doubled representation.

On the point set $\widetilde G$, the pseudometrics
$$
d_e(a,b)=
 \|\widetilde\rho_e(a)z_e-\widetilde\rho_e(b)z_e\|_2
$$
are preserved by common left translation. Apply Theorem 1 to this $2|G|^2$-point space and restrict to the pairs $(1,q(g))$. Since
$\log(4|G|^2)=O(\log(2|G|))$, this gives (T20). $\square$

This representation identity is also a useful bridge between the metric theorem and coset constraints. Taking the permutation representation on $G/H$, $v$ the identity-coset vector, and $u$ the $aH$-coset vector, scaled by $1/\sqrt2$, makes $\ell(g)=\mathbf1[g\notin aH]$. The separate affine-group manuscript supplies the exact subgroup compiler and the group-CSP consequences directly.

### 4.1 Bernstein transforms, including bounded nonlinear losses

There is a useful closure consequence of the classical Schoenberg--Bernstein theorem. Let each item have its own Bernstein function $\varphi_e$ with $\varphi_e(0)=0$. Equivalently, it has a representation
$$
\varphi_e(t)=\beta_e t+
 \int_{(0,\infty)}(1-e^{-st})\,\mu_e(ds),
 \quad
 \beta_e\ge0,\quad
 \int\min\{1,s\}\,\mu_e(ds)<\infty.
 \tag{TB1}
$$
Then
$$
d'_e(x,y)=\sqrt{\varphi_e(d_e(x,y)^2)}
 \tag{TB2}
$$
is another Hilbertian pseudometric, preserved by the same itemwise action. Theorem 1 therefore applies with exactly the same support order.

For completeness, this closure statement can be checked on any finite point set without constructing the possibly infinite-dimensional feature space. If $K_{ij}=\|\phi_i-\phi_j\|_2^2$ and $\sum_i c_i=0$, then
$$
\sum_{i,j}c_ic_jK_{ij}
 =-2\left\|\sum_i c_i\phi_i\right\|_2^2\le0.
$$
The Gaussian matrix $(e^{-sK_{ij}})_{ij}$ is positive semidefinite. One direct proof expands
$$
e^{-s\|\phi_i-\phi_j\|^2}
 =e^{-s\|\phi_i\|^2}e^{-s\|\phi_j\|^2}
 \sum_{k\ge0}\frac{(2s)^k}{k!}
 \langle\phi_i,\phi_j\rangle^k,
$$
whose summands are positive semidefinite Gram matrices. Thus, by (TB1),
$$
\sum_{i,j}c_ic_j\varphi_e(K_{ij})
 =\beta_e\sum_{i,j}c_ic_jK_{ij}
 -\int\sum_{i,j}c_ic_j e^{-sK_{ij}}\,\mu_e(ds)
 \le0.
 \tag{TB3}
$$
The entries are finite, and the integrability condition justifies the finite sum under the integral. The transformed kernel is nonnegative and has zero diagonal. Double-centering it gives a positive semidefinite Gram matrix, so it is the squared-distance matrix of a Hilbert embedding. This proves (TB2); invariance is immediate from its scalar form.

Applying this transformation on the wreath orbit in the proof of Corollary 2 yields the following stronger version:
$$
\sum_e w_e
 \sqrt{\varphi_e\!\left(\|u_e-\rho_e(g)v_e\|_2^2\right)}
 \tag{TB4}
$$
has an $O(\log(2|G|)/\epsilon^2)$-item relative-error coreset, simultaneously for every $g$. Every item may use a different function and scale.

Concrete choices, with $r\ge0$ and $\sigma>0$, are:

| Original-item loss | Bernstein function applied to $r^2$ |
|---|---|
| $r^\alpha$, $0<\alpha\le1$ | $\varphi(t)=t^\alpha$ |
| $\sqrt{1-\exp(-r^2/\sigma^2)}$ | $\varphi(t)=1-\exp(-t/\sigma^2)$ |
| $r/\sqrt{\sigma^2+r^2}$ | $\varphi(t)=t/(\sigma^2+t)$ |

The last two losses are bounded and generally are not seminorms of the transformation parameters. They inherit the whole-item support theorem through Hilbert metric composition. This is a closure corollary, not a new theorem about Bernstein functions. It does not cover a loss merely because that loss is concave, robust, or bounded.

The classical result and representation are stated, for example, in Kühn--Schilling, *A Probabilistic Proof of Schoenberg's Theorem*, Theorem 3.1 and Section 2, JMAA 2019. [Primary source](https://arxiv.org/pdf/1808.00190). The transform $\varphi(t)=t^2$, which would give ordinary squared Euclidean loss in (TB4), is not in this Bernstein class.

## 5. Concrete whole-item applications

### 5.1 Whole blocks of affine XOR residuals

Let a block $e$ contain arbitrary rows $a_{ej}\in\mathbb F_2^n$, targets $b_{ej}\in\mathbb F_2$, and coefficients $c_{ej}\ge0$. Define
$$
\ell_e(x)=
 \left(\sum_j c_{ej}
   \mathbf1[\langle a_{ej},x\rangle\ne b_{ej}]
 \right)^{1/2},
 \qquad x\in\mathbb F_2^n.
 \tag{T23}
$$
This is a group-alignment loss. Use the diagonal representation
$$
\rho_e(x)=
 \mathrm{diag}\bigl((-1)^{\langle a_{ej},x\rangle}\bigr),
 \quad
 (v_e)_j=\frac{\sqrt{c_{ej}}}{2},
 \quad
 (u_e)_j=(-1)^{b_{ej}}\frac{\sqrt{c_{ej}}}{2}.
 \tag{T24}
$$
Then $\|u_e-\rho_e(x)v_e\|_2^2$ is exactly the sum inside (T23).

Corollary 2 gives $O(\min\{m,(n+1)/\epsilon^2\})$ retained whole blocks preserving
$\sum_e w_e\ell_e(x)$ for every Boolean assignment. There is no dependence on the number of parity rows inside a block. Each retained block has one scalar coefficient; its internal coefficients $c_{ej}$ are not separately changed.

This is a square-root loss on each block, not the block's squared loss. Ordinary individual-parity code sparsification does not by itself preserve such a grouping, because it may assign different coefficients to rows within the same block.

### 5.2 Robust coordinate-permutation alignment

For arbitrary pairs $u_e,v_e\in\mathbb R^d$, consider a common permutation of the coordinate axes:
$$
L(\pi)=\sum_e w_e\|u_e-P_\pi v_e\|_2,
 \qquad \pi\in S_d.
 \tag{T25}
$$
Corollary 2 retains
$$
O\!\left(\min\left\{m,
 \frac{d\log(d+1)}{\epsilon^2}\right\}\right)
 \tag{T26}
$$
whole paired observations and preserves every permutation objective.

The finite query group acts on the coordinates inside each paired observation. The pairing between $u_e$ and $v_e$ is part of the input and is not independently optimized. The loss is a sum of Euclidean norms, rather than a sum of their squares.

For a concrete ordinary-seminorm comparison, regard
$$
f_e(M,t)=\|t u_e-Mv_e\|_2
 \tag{T27}
$$
as a seminorm on $\mathbb R^{d\times d}\times\mathbb R$, and restrict to $(M,t)=(P_\pi,1)$. The optimal general sums-of-seminorms theorem supplies $O(d^2/\epsilon^2)$ support through this direct lifting. Equation (T26) is smaller for this finite-group query family. This comparison is a precise consequence of that checked general theorem, not a claim that every specialized permutation-alignment coreset in the literature has been excluded.

Signed coordinate permutations are also covered, because their finite group has order $2^d d!$, giving the same asymptotic support. More generally, any explicitly specified finite subgroup of orthogonal transformations gives the bound in terms of its own $\log|G|$. Continuous rotations or arbitrary translations are not included by replacing an infinite group order with a finite number.

### 5.3 Common relabeling of matrix-valued observations

The same reasoning applies to matrix pairs $A_e,B_e\in\mathbb R^{d\times d}$ with the orthogonal conjugation representation
$$
\rho(\pi)B=P_\pi B P_\pi^{\mathsf T}.
$$
Thus $O(d\log(d+1)/\epsilon^2)$ whole matrix pairs preserve
$$
\sum_e w_e
 \|A_e-P_\pi B_eP_\pi^{\mathsf T}\|_F
 \qquad\text{for every }\pi\in S_d.
 \tag{T28}
$$
This is a coreset for the family of complete relabeling losses. It neither finds an optimal relabeling nor changes a retained matrix pair internally.

## 6. The logarithmic bound is jointly sharp

Let $K_{s,B}$ be a connected complete bipartite graph on $n=s+B$ vertices, where
$$
s=\lceil\epsilon^{-2}\rceil,\qquad
 B\ge s,\qquad 0<\epsilon\le1/2.
$$
Take
$$
X=\mathbb F_2^n/\langle\mathbf1\rangle,
 \qquad N=2^{n-1}.
 \tag{T29}
$$
For each graph edge $uv$, define the scalar two-cluster pseudometric
$$
d_{uv}(x,y)=
 \mathbf1[(x_u+x_v)\ne(y_u+y_v)].
 \tag{T30}
$$
It is the Euclidean distance between the scalar embeddings
$\phi_{uv}(x)=x_u+x_v\in\{0,1\}$, where the addition in the embedding is modulo two. It is well-defined on the quotient and invariant under the common transitive translation action.

The sum of these edge metrics is a genuine metric on the quotient, because the underlying graph is connected. Its distance from zero to $x$ is the graph cut value. Therefore every whole-item relative-error sparsifier must preserve every cut of $K_{s,B}$.

The standard complete-bipartite cut obstruction, derived in (EC15) of the companion exact-label-cut manuscript, forces at least
$$
\frac{(1-\epsilon)^2sB}
 {(1+3\sqrt2\,\epsilon\sqrt s)^2}
 =\Omega(n/\epsilon^2)
 =\Omega(\log N/\epsilon^2)
 \tag{T31}
$$
retained items. This lower bound allows arbitrary nonnegative output weights. It is an inherited classical cut lower bound, used here to show that the logarithmic parameter in Theorem 1 cannot generally be improved.

The stated joint regime is
$\log_2N+1\ge2\lceil\epsilon^{-2}\rceil$. The natural support cap by $m$ remains in force.

## 7. Two essential boundaries

### Transitivity of the total metric is insufficient

Let $X=[N]$, and for each $e\in[N]$ define
$$
d_e(x,y)=
 |\mathbf1[x=e]-\mathbf1[y=e]|.
 \tag{T32}
$$
Every item is a scalar Euclidean pseudometric. Their sum is the fully symmetric discrete metric:
$$
\sum_{e=1}^N d_e(x,y)=2
 \qquad(x\ne y).
 \tag{T33}
$$
Yet if a reweighting omits two indices $a,b$, every retained item assigns distance zero to the pair $(a,b)$. Consequently any relative-error summary with $\epsilon<1$ must retain at least $N-1$ items.

The full permutation group preserves the total metric and permutes the item list, but it does not preserve each item individually. Thus neither total transitivity nor transitivity up to an item permutation can replace (T2).

### Squared negative-type kernels are a different object

The assumption is that each $d_e$ is a Hilbert distance, equivalently that $d_e^2$ is conditionally negative definite. If a convention calls a kernel $\psi_e$ “of negative type” when $\psi_e$ itself is conditionally negative definite, the theorem applies to $\sqrt{\psi_e}$. It does not automatically apply to $\psi_e$.

The covariance identity (T11) is the reason: the scalar comparison process has variance proportional to $d_e^2$. Replacing an orbit norm by its square changes that identity.

For a small illustration of the distinction, Hamming distance on the four-point Boolean square is conditionally negative definite. Its square is not: for the four coefficients $(1,-1,-1,1)$, which sum to zero, the corresponding quadratic form in the squared Hamming-distance matrix is $8>0$. This example distinguishes the assumptions; it is not claimed as a sparsification lower bound.

In particular, this note does not prove an optimal original-generator spectral sparsifier for an arbitrary nonabelian Cayley graph. Squared displacement energies require a different argument.

## 8. Related work

**Optimal ordinary sums of seminorms.** Basu--Brakensiek--Chen--Putterman--Reis--Zhang, *Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms* (September 2026), Theorem 1.2, already gives $O(R/\epsilon^2)$ whole-item support for seminorms on an $R$-dimensional real query space. A generic linear realization of arbitrary $N$-point Hilbert metrics uses the zero-sum subspace of $\mathbb R^X$, of dimension $N-1$: extend each embedding linearly and query vectors $e_x-e_y$. The new statement replaces this general ambient parameter by $\log N$ under the common itemwise transitivity hypothesis. Equation (T27) gives the more concrete $d^2$-versus-$d\log d$ alignment comparison. [Primary source](https://arxiv.org/pdf/2609.20238).

**Constructive norm sparsification.** Jambulapati--Lee--Liu--Sidford, *Sparsifying Sums of Norms* (FOCS 2023), provides polynomial-time constructions with additional logarithmic factors under its evaluation and roundedness contract. The new existence bound does not supersede those compact construction guarantees. [Primary source](https://homes.cs.washington.edu/~jrl/papers/pdf/norm-sparsify.pdf).

**Codes and abelian Cayley graphs.** Khanna--Putterman--Sudan's weighted code theorem sparsifies individual parity coordinates; Basu--Kothari--Meka--Tudose's July 2026 theorem achieves optimal support for individual abelian Cayley generators. These are important special-purpose antecedents, but independently reweighting the rows inside a block need not preserve the whole-block loss (T23). The present argument keeps that shared coefficient throughout. [Weighted codes](https://arxiv.org/html/2404.06327v2); [abelian Cayley graphs](https://arxiv.org/html/2607.08261v1).

**Robust alignment.** Amir--Kovalsky--Dym, *Symmetrized Robust Procrustes: Constant-Factor Approximation and Exact Recovery* (2022), studies the sum-of-Euclidean-norms alignment objective and gives a $\sqrt2$-approximation using a convex relaxation for rigid motions. Its objective establishes the relevance of the unsquared loss, while its optimization guarantee and continuous transformation family differ from the finite-group original-item coreset theorem here. No improvement over its optimization factor is asserted. [Primary source](https://arxiv.org/abs/2207.08592).

**Analytic ingredients.** Slepian's Gaussian comparison and the Reis--Rothvoss partial-coloring theorem are existing results. The hereditary Gaussian-section symmetrizer is proved in the companion subgroup manuscript. Centering the Hilbert embeddings supplies the stationary process needed to apply that backend to $N$ orbit points; the wreath representation supplies the exact two-anchor loss identity. [Slepian](https://doi.org/10.1002/j.1538-7305.1962.tb02419.x); [Reis--Rothvoss](https://arxiv.org/html/2606.28147v2).

Theorems (T4) and (T20) preserve whole metric items under their common symmetry hypothesis. Their field, group-size, embedding, and numerical-access assumptions are part of the stated contracts.
