# Sparsifying Hilbert metric sums under an action with few orbits

**Abstract.** Suppose one group action preserves every metric in a family of Hilbertian pseudometrics on $`N`$ points and has orbits of sizes $`N_1,\ldots,N_k`$. A transitive tuple completion gives a whole-item sparsifier of size $`O(\min\{N,\log(2k!\prod_jN_j)\}/\epsilon^2)`$. Its symmetry-based construction uses only the original distance table. An explicit family requires $`\Omega(k\log(N/k)/\epsilon^2)`$ items when the orbits are sufficiently large.

## 1. Statement

Let $`X`$ be a finite set of $`N\ge2`$ points. Each original item $`e\in[m]`$ is a Hilbertian pseudometric
```math
d_e(x,y)=\|\phi_e(x)-\phi_e(y)\|_2.
 \tag{FO1}
```
Embedding dimensions may vary. Let $`w_e>0`$, and set $`D(x,y)=\sum_e w_e d_e(x,y)`$. Suppose a common group $`\Gamma`$ acts on $`X`$ and preserves every item individually:
```math
d_e(gx,gy)=d_e(x,y)
 \qquad(e\in[m],\ g\in\Gamma,\ x,y\in X).
 \tag{FO2}
```
Its orbits $`X_1,\ldots,X_k`$ have sizes $`N_1,\ldots,N_k`$. Put
```math
L=\log\!\left(2\,k!\prod_{j=1}^kN_j\right).
 \tag{FO3}
```
Only the permutation action matters; its image is finite even if $`\Gamma`$ was originally described as an infinite group.

**Theorem 1.** For $`0<\epsilon<1`$, there are nonnegative coefficients $`\omega_e`$, supported on
```math
O\!\left(
   \min\left\{m,\frac{\min\{N,L\}}{\epsilon^2}\right\}
 \right)
 \tag{FO4}
```
whole original metric items, such that
```math
(1-\epsilon)D(x,y)
 \le\sum_e\omega_e w_e d_e(x,y)
 \le(1+\epsilon)D(x,y)
 \qquad(x,y\in X).
 \tag{FO5}
```
In particular, $`L\le\log2+k\log N`$.

The $`L`$-branch has a randomized construction polynomial in the original explicit distance-table size and encoding/accuracy parameters, under the separation/precision contract of the partial-coloring backend. The $`N`$-branch is the published general sums-of-seminorms support theorem. No unverified construction guarantee for that separate branch is bundled into this statement.

For $`N=1`$, all distances vanish and the empty output suffices. Zero items can otherwise be discarded. Every retained item receives one scalar coefficient; no internal embedding coordinate is separately reweighted.

## 2. A transitive completion

Let $`Y`$ be the set of ordered $`k`$-tuples containing exactly one point from each original orbit, in arbitrary coordinate positions. Then
```math
|Y|=k!\prod_{j=1}^kN_j.
 \tag{FO6}
```
The product action $`\Gamma^k`$, together with coordinate permutations by $`S_k`$, acts transitively on $`Y`$. First align the orbit labels of two tuples by a permutation, then move each coordinate within its orbit using a separate group element.

Lift each metric by its Euclidean product:
```math
\widetilde d_e(u,v)
   =\left(\sum_{i=1}^k d_e(u_i,v_i)^2\right)^{1/2}.
 \tag{FO7}
```
This is Hilbertian, via the direct-sum embedding
```math
\widetilde\phi_e(u)
   =(\phi_e(u_1),\ldots,\phi_e(u_k)).
```
Independent group actions preserve each summand in (FO7), and coordinate permutations preserve their sum. Thus one common transitive action preserves every lifted metric individually.

Every original pair is encoded by a lifted pair with a common scalar factor:

- If $`x,y`$ belong to the same orbit, use tuples identical except that the corresponding coordinate changes from $`x`$ to $`y`$. Then $`\widetilde d_e(u,v)=d_e(x,y)`$ for every item.
- If $`x,y`$ belong to different orbits, take a tuple containing both, and swap those two entries to obtain the second tuple. Then $`\widetilde d_e(u,v)=\sqrt2\,d_e(x,y)`$ for every item.

The factor $`\sqrt2`$ is common to every summand and cancels from a multiplicative approximation. Applying the companion transitive-metric theorem on $`Y`$ proves the $`O(L/\epsilon^2)`$ support branch.

Finally,
```math
\prod_jN_j\le(N/k)^k,\qquad k!\le k^k,
```
so $`|Y|\le N^k`$ and $`L\le\log2+k\log N`$.

## 3. The tuple space need not be constructed

The same argument yields a hereditary Gaussian cone bound on the original pair queries. For arbitrary positive item weights, the stationary-process comparison in the companion note gives, for any anchor $`o\in Y`$,
```math
\Pr_{\xi\sim N(0,I)}
 \left[
   \sum_e w_e\xi_e\widetilde d_e(o,v)\le0
   \quad\text{for every }v\in Y
 \right]\ge |Y|^{-1}.
 \tag{FO8}
```
Transitivity and itemwise invariance make this anchor-pair event exactly the event that the inequalities hold for all pairs in $`Y`$. Every original pair row is a positive scalar multiple of a lifted pair row. Consequently,
```math
\Pr_{\xi}
 \left[
   \sum_e w_e\xi_e d_e(x,y)\le0
   \quad\text{for all }x,y\in X
 \right]\ge |Y|^{-1}.
 \tag{FO9}
```
This proof remains valid after every item restriction and positive rescaling, since those operations do not change the common action.

Apply the Gaussian-section sparsification principle directly to the original table $`(d_e(x,y))_{(x,y),e}`$. Its symmetric relative-error body is
```math
\left\{z:
 \left|\sum_e w_ez_e d_e(x,y)\right|
 \le a\sum_e w_ed_e(x,y)
 \quad\forall x,y\in X
 \right\}.
 \tag{FO10}
```
At most $`N^2`$ rows need to be checked by a separation oracle. The proof parameter is $`\log(2|Y|)=L`$, but no tuple in the potentially much larger space $`Y`$ needs to be enumerated.

Thus the $`L`$-branch inherits a randomized polynomial-time construction in the original table model. Rational distances and weights give rational linear inequalities. If distances are represented indirectly as square roots of rational quadratic expressions, an evaluation and weak-separation precision contract must be provided; a bit-complexity statement for arbitrary real input is not implicit.

The action and its orbit information are structural input or promises for the support bound. This result does not discover an unknown common isometry group.

## 4. Comparison with unrestricted metric sums

The published optimal sums-of-seminorms theorem already supplies $`O(N/\epsilon^2)`$ support without any action assumption. On the $`(N-1)`$-dimensional zero-sum subspace of $`\mathbb R^X`$, define
```math
f_e(z)=\left\|\sum_{x\in X}z_x\phi_e(x)\right\|_2.
 \tag{FO11}
```
This is a seminorm, and $`f_e(\mathbf e_x-\mathbf e_y)=d_e(x,y)`$. The existing theorem therefore proves the $`N`$-branch in (FO4).

The increment is meaningful when $`\log(k!)+\sum_j\log N_j\ll N`$. A bounded number of orbits gives logarithmic dependence on the number of points. For a trivial action, $`k=N`$, the unrestricted support bound is the appropriate one. The assumption still requires preservation of each metric item: invariance of only the total sum is insufficient.

## 5. A joint lower-bound family

The dependence on the number of large orbits cannot generally be removed. Fix $`0<\epsilon\le1/2`$, let
```math
s=\lceil\epsilon^{-2}\rceil,\qquad B\ge s,\qquad v=s+B,
```
and take $`k`$ disjoint copies of
```math
X_j=\mathbb F_2^v/\langle\mathbf1\rangle,
 \qquad |X_j|=2^{v-1}.
 \tag{FO12}
```
The common action is the product of the translation groups of the $`k`$ copies.

For each orbit $`j`$ and each edge $`ab`$ of $`K_{s,B}`$ on the $`v`$ Boolean coordinates, make one scalar metric item, with embedding on the entire disjoint union
```math
\phi_{j,ab}(x)=
 \begin{cases}
 (-1)^{x_a+x_b},&x\in X_j,\\
 0,&x\notin X_j.
 \end{cases}
 \tag{FO13}
```
The parity is well-defined on the quotient by $`\mathbf1`$. Translating within $`X_j`$ multiplies this whole scalar embedding by one common sign; it remains zero outside $`X_j`$. Therefore the action preserves every item, including cross-orbit distances.

On two points inside $`X_j`$, only that orbit's items contribute. Their distance is twice the corresponding parity-cut indicator. Every whole-item sparsifier must therefore induce a separate $`(1\pm\epsilon)`$ cut sparsifier of $`K_{s,B}`$ for each orbit. The complete-bipartite cut lower bound recorded as (EC15) in the companion exact-label-cut manuscript forces $`\Omega(v/\epsilon^2)`$ retained edges per copy, even with arbitrary nonnegative output weights. Hence the metric instance requires
```math
\Omega\!\left(\frac{kv}{\epsilon^2}\right)
 =
 \Omega\!\left(\frac{k\log(N/k)}{\epsilon^2}\right)
 \tag{FO14}
```
whole original items, where $`N=k2^{v-1}`$.

This is a joint regime with
```math
\log_2(N/k)+1\ge2\lceil\epsilon^{-2}\rceil.
```
It gives the correct linear dependence on the number of these large orbits and matches the upper order in broad parameter ranges. It is not a sharpness claim for every $`k,N,\epsilon`$; the completion's $`\log(k!)`$ term can leave a gap.

## 6. Sources and scope

The analytic theorem and construction contract are in [transitive-metrics-and-group-alignment.md](transitive-metrics-and-group-alignment.md); the Gaussian hereditary-section transfer is in [optimal-whole-subgroup-constraints.md](optimal-whole-subgroup-constraints.md). The new step here is the transitive tuple completion, its original-table implementation, and the orbit-dependent support consequence.

The unrestricted support comparison uses Basu--Brakensiek--Chen--Putterman--Reis--Zhang, *Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms*, Theorem 1.2 (September 2026): <https://arxiv.org/pdf/2609.20238>. The partial-coloring backend is Reis--Rothvoss, Theorem 7 in the July 2026 version: <https://arxiv.org/html/2606.28147v2>. These published theorems are credited separately from this extension.

The result concerns sums of Hilbert distances. It does not replace distances by their squares, and a small number of action orbits alone does not remove the Hilbert-embedding requirement.
