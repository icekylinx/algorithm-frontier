# Optimal-support sparsification of affine constraints over arbitrary finite groups

**Abstract.** We prove that weighted complements of arbitrary subgroup cosets in a finite group $`G`$ have relative-error sparsifiers on $`O(\log(2|G|)/\epsilon^2)`$ original constraints. The cosets may be inconsistent and their subgroups need not be normal. A common wreath-product embedding turns every accepting coset into a subgroup and every original query into one fixed group element, allowing the whole-subgroup theorem to apply. Consequences include arbitrary-arity group-derived Mal'tsev constraints and coordinate coresets for group codes with arbitrary received words.

## 1. Main theorem

Let $`G`$ be a finite group, $`N=|G|`$. For each original item $`e\in[m]`$, choose a subgroup $`H_e\le G`$, an element $`a_e\in G`$, and a weight $`w_e>0`$. Put
```math
C_e=a_eH_e,\qquad
 b_e(g)=\mathbf1[g\notin C_e],\qquad
 W(g)=\sum_e w_e b_e(g).
 \tag{A1}
```
There is no assumption that the subgroups are normal, that the cosets intersect, or that any assignment has zero cost.

**Theorem 1.** For every $`0<\epsilon<1`$, there are coefficients $`\omega_e\ge0`$, supported on
```math
O\!\left(\min\left\{m,\frac{\log(2N)}{\epsilon^2}\right\}\right)
 \tag{A2}
```
original indices, such that
```math
(1-\epsilon)W(g)
 \le \sum_e\omega_e w_e b_e(g)
 \le (1+\epsilon)W(g)
 \qquad\text{for every }g\in G.
 \tag{A3}
```
All items retain their original predicates. In particular, a coset is not replaced by separately weighted character tests, generators, or coordinates.

Identically zero items can be discarded. An empty accepting set gives a constant-one item; any collection of such items can be represented exactly by one of those original indices with their total weight. This adds at most one item and preserves (A2). Right cosets are included because $`Ha=a(a^{-1}Ha)`$.

**Optional exact total weight.** One can additionally require
$`\sum_e\omega_ew_e=\sum_e w_e`$, with the same support order and relative error. For this version the total includes identically zero original items; those items are kept available to the construction instead of being discarded in advance. The short augmentation proof is given at the end of Section 3.

With the $`N\times m`$ predicate table explicitly supplied and rational input weights, the separation-based partial-coloring implementation is randomized polynomial in the table and encoding sizes, under the usual accuracy contract of the backend. The table can be exponentially larger than a compact presentation of $`G`$ and its cosets. The theorem does not turn a difficult compact separation problem into a polynomial-time algorithm.

## 2. One common wreath product turns every coset into a subgroup

Write
```math
\widetilde G=(G\times G)\rtimes C_2,\qquad
 \tau(x,y)\tau=(y,x).
 \tag{A4}
```
Thus $`|\widetilde G|=2N^2`$. For a particular coset $`C=aH`$, set
```math
B_C=(aHa^{-1})\times H,\qquad
 t_C=(a,a^{-1})\tau.
 \tag{A5}
```
The same ambient group $`\widetilde G`$ is used for every original item.

First, $`t_C^2=1`$. Moreover
```math
t_C(x,y)t_C^{-1}
   =(aya^{-1},a^{-1}xa),
 \tag{A6}
```
so $`t_C`$ normalizes $`B_C`$. Therefore
```math
K_C=B_C\rtimes\langle t_C\rangle
 \tag{A7}
```
is a subgroup of $`\widetilde G`$. Its odd part is exactly
```math
B_Ct_C
   =\{(ah_1,h_2a^{-1})\tau:h_1,h_2\in H\}.
 \tag{A8}
```

Use the query embedding
```math
q(g)=(g,g^{-1})\tau.
 \tag{A9}
```
Equations (A8)--(A9) give the exact membership identity
```math
q(g)\in K_C\quad\Longleftrightarrow\quad g\in aH.
 \tag{A10}
```
Indeed, if $`g=ah`$, the second coordinate is $`h^{-1}a^{-1}`$, so take $`h_1=h`$ and $`h_2=h^{-1}`$. Conversely, the first coordinate in (A8) already forces $`g\in aH`$.

The map $`q`$ is not claimed to be a homomorphism. That is unnecessary: the homogeneous sparsifier is valid on every element of $`\widetilde G`$, and hence also on this fixed embedded query set.

The wreath subgroup in (A7) is established algebra. For example, Proposition 3 of Dinh--Moore--Russell's 2011 hidden-shift reduction writes the subgroup
```math
(H_0\times s^{-1}H_0s)
 \ \cup\
 (H_0s\times s^{-1}H_0)\tau.
```
Taking $`H_0=aHa^{-1}`$ and $`s=a`$ gives (A7)--(A8). The contribution here is its application to simultaneous sparsification with one retained coefficient per original coset, together with the Gaussian support theorem; the wreath construction itself is not claimed as new.

## 3. Gaussian consequence and support proof

We state the needed result from the companion manuscript
[optimal-whole-subgroup-constraints.md](optimal-whole-subgroup-constraints.md).

**Homogeneous subgroup theorem.** If $`L_e`$ are subgroups of a finite group $`A`$, then, for every positive weighting and every restricted item subfamily,
```math
\Pr_{\xi}\!\left[
   \sum_e w_e\xi_e\mathbf1[x\notin L_e]\le0
   \text{ for all }x\in A
 \right]\ge |A|^{-1},
 \tag{A11}
```
where the $`\xi_e`$ are independent standard Gaussians. The associated hereditary Gaussian-section argument and dilated partial-coloring theorem yield $`O(\log(2|A|)/\epsilon^2)`$ whole original items.

For clarity, the Gaussian part has a short direct proof. Independently sample a standard Gaussian $`T_{e,D}`$ for each left coset $`D\in A/L_e`$, and define
```math
F_x=2^{-1/2}\sum_e w_eT_{e,xL_e},
 \quad
 Y_x=F_1-F_x,
 \quad
 Z_x=\sum_e w_e\xi_e\mathbf1[x\notin L_e].
 \tag{A12}
```
Left translation preserves the law of $`F`$, so the identity is a global minimum with probability at least $`1/|A|`$. For each coordinate, $`Y_x`$ and $`Z_x`$ have the same variance. For two coordinates outside $`L_e`$, the contribution to $`\mathrm{Cov}(Y_x,Y_y)`$ is
```math
\frac{w_e^2}{2}\bigl(1+\mathbf1[xL_e=yL_e]\bigr)\le w_e^2,
```
and the corresponding contribution to $`\mathrm{Cov}(Z_x,Z_y)`$ is $`w_e^2`$. If either coordinate belongs to $`L_e`$, both contributions vanish. Slepian comparison, after normalizing nonzero coordinates, proves (A11).

Apply (A11) to $`A=\widetilde G`$ and $`L_e=K_{C_e}`$, and restrict its event to $`q(G)`$. The exact identity (A10) gives
```math
\Pr_{\xi}\!\left[
   \sum_e w_e\xi_e b_e(g)\le0
   \text{ for all }g\in G
 \right]\ge\frac1{2N^2}.
 \tag{A13}
```
Crucially, the same lower bound holds after every positive rescaling and every restriction of the item family.

Here is the remaining support argument, with the companion Gaussian symmetrization lemma made explicit. For a current positive weighting and $`0<a\le1/2`$, let
```math
K_a=\left\{
 z:\sum_e w_ez_e b_e(g)\le aW(g)\quad\forall g
 \right\}.
 \tag{A14}
```
It contains $`a[-1,1]^m`$, and every coordinate section contains the corresponding one-sided cone from (A13). The companion Gaussian symmetrization lemma says that, whenever
```math
m\ge C\log(2/p)/a^2,
 \qquad p=(2N^2)^{-1},
```
the symmetric body
```math
Q_a=K_a\cap(-K_a)\cap[-1,1]^m
 \tag{A15}
```
has volume at least $`c^m`$, for an absolute $`c>0`$. This lemma uses Gaussian coordinate sections, midpoint reflection, Prékopa's theorem, and Gaussian correlation; its full proof is in the companion manuscript.

The Reis--Rothvoss large-volume partial-coloring theorem then produces
$`z\in sQ_a\cap[-1,1]^m`$, with constant $`s`$, having at least $`m/2`$ coordinates equal to $`1`$ or $`-1`$. Choose its sign so that at least $`m/4`$ coordinates are $`-1`$, and replace
```math
w_e\longleftarrow w_e(1+z_e).
```
This keeps weights nonnegative, deletes at least a quarter of the items, and incurs relative error at most $`sa`$ for every query.

At support size $`m_t`$, use
```math
a_t=\sqrt{C\log(4N^2)/m_t}.
 \tag{A16}
```
Stop at $`M=C'\log(2N)/\epsilon^2`$. Since the support shrinks by a factor at most $`3/4`$, the sum of the earlier $`sa_t`$ is $`O(\sqrt{\log(2N)/M})`$. A sufficiently large $`C'`$ makes this at most $`\epsilon/4`$ and keeps every invoked $`a_t\le1/2`$. Multiplying the one-stage inequalities yields (A3). If the initial support is already at most $`M`$, retain it unchanged.

Only the $`N`$ original query inequalities in (A14) need to be supplied to this algorithm. The $`2N^2`$-element wreath group proves the mass bound; it need not be materialized as the query table used by the partial-coloring procedure.

### Exact total-weight normalization

To obtain the optional variant, first work over $`G\times C_2`$ and replace each accepting coset $`C_e`$ by $`C_e\times\{0\}`$. At a query $`(g,0)`$ its violation is the original predicate; at every query $`(g,1)`$ its violation equals one. Apply Theorem 1 with error $`\eta=\epsilon/4`$ to these augmented items. Let $`W_{\mathrm{tot}}=\sum_e w_e`$ and let $`\widehat W_{\mathrm{tot}}`$ be the total output weight. The bit-one query guarantees
```math
(1-\eta)W_{\mathrm{tot}}
 \le\widehat W_{\mathrm{tot}}
 \le(1+\eta)W_{\mathrm{tot}}.
```
For a nonempty positive-weight input, rescale every output coefficient by
$`W_{\mathrm{tot}}/\widehat W_{\mathrm{tot}}`$. The total is then exact, and each original query has multiplicative factors between
$`(1-\eta)/(1+\eta)`$ and $`(1+\eta)/(1-\eta)`$, contained in $`[1-\epsilon,1+\epsilon]`$. The extra binary factor changes $`\log(2|G|)`$ only by an additive constant.

This argument keeps even an original zero-loss item $`C_e=G`$ available, since its augmented predicate is nonzero on bit-one queries. Empty accepting sets, if present, can first be combined exactly into one original constant-one item while preserving their total weight. The empty input is trivial.

## 4. Arbitrary-arity group CSPs

Let $`A`$ be any finite group, and let $`x=(x_1,\ldots,x_n)\in A^n`$ be an assignment. An original constraint $`e`$ may have arbitrary arity $`r_e`$ and accept a coset
```math
R_e=a_eH_e\subseteq A^{r_e}.
 \tag{A17}
```
Its scope selects coordinates of $`x`$; repeated variables are allowed. Coordinate selection is a group homomorphism
$`\pi_e:A^n\to A^{r_e}`$.

If $`\pi_e^{-1}(R_e)`$ is nonempty, choose one $`x_e`$ in it. Then
```math
\pi_e^{-1}(R_e)=x_e\,\pi_e^{-1}(H_e).
 \tag{A18}
```
This is a coset in the common assignment group $`A^n`$. If the preimage is empty, the violation predicate is constant one and is handled as above.

**Corollary 2.** The weighted number of violated constraints
```math
\mathrm{Viol}(x)
 =\sum_e w_e\mathbf1[\pi_e(x)\notin a_eH_e]
```
has a relative-error sparsifier retaining
```math
O\!\left(\min\left\{m,
 \frac{1+n\log|A|}{\epsilon^2}\right\}\right)
 \tag{A19}
```
whole original constraints, simultaneously for all assignments. The bound has no arity factor. The alphabet group may be nonabelian and may be part of the input.

This includes heterogeneous relations and inconsistent constraint systems. The objective is the weight of violations of the accepting cosets, equivalently the weight satisfied by their complementary predicates. It is not a simultaneous multiplicative guarantee for both satisfaction and violation counts.

### Exact relation to group-derived Mal'tsev predicates

The relevant ternary operation on a group is
```math
\mu(x,y,z)=xy^{-1}z.
 \tag{A20}
```
A nonempty subset $`R\subseteq A^r`$ is closed under this coordinatewise operation if and only if it is a left coset of a subgroup of $`A^r`$.

To prove the nontrivial direction, fix $`a\in R`$ and put $`H=a^{-1}R`$. It contains the identity. If $`h_1,h_2\in H`$, then
```math
(ah_1)a^{-1}(ah_2)=ah_1h_2\in R,
```
so $`h_1h_2\in H`$. Also
```math
a(ah_1)^{-1}a=ah_1^{-1}\in R,
```
so $`h_1^{-1}\in H`$. Thus $`H`$ is a subgroup and $`R=aH`$. Conversely,
```math
(ah_1)(ah_2)^{-1}(ah_3)=ah_1h_2^{-1}h_3
```
stays in $`aH`$.

Consequently (A19) applies to the entire class of predicates preserved by the **group-derived** Mal'tsev operation (A20), for arbitrary finite groups. It does not assert an optimal bound for every algebra carrying an arbitrary Mal'tsev operation. It also does not assert that every ordered nonabelian word equation defines a subgroup coset: that requires a separate closure check.

## 5. Arbitrary-center coordinate coresets for finite group codes

Let $`\mathcal C\le A^m`$ be a subgroup code over any finite group $`A`$. Fix an arbitrary received word $`y\in A^m`$ and positive coordinate weights $`w_e`$. Consider
```math
d_w(c,y)=\sum_{e=1}^m w_e\mathbf1[c_e\ne y_e],
 \qquad c\in\mathcal C.
 \tag{A21}
```
For the coordinate homomorphism $`\pi_e:\mathcal C\to A`$, the fiber
$`\pi_e^{-1}(y_e)`$ is either empty or a coset of its kernel. Theorem 1 therefore gives
```math
O\!\left(\min\left\{m,
 \frac{\log(2|\mathcal C|)}{\epsilon^2}\right\}\right)
 \tag{A22}
```
retained original coordinates preserving every distance (A21).

The center need not belong to the code, and there need not be a codeword matching every center coordinate. The same conclusion holds for a coset code after parametrizing it by its underlying subgroup. One may also replace singleton coordinate acceptance by any coset acceptance set in the alphabet, or use a projection to an entire coordinate block and keep that block as one item.

This is a coreset for the whole nearest-codeword objective, not a new decoding algorithm. If the retained objective is minimized exactly over the same code, its minimizer has original objective at most $`(1+\epsilon)/(1-\epsilon)`$ times the original optimum. Solving the retained optimization may remain hard.

## 6. Lower bound and parameter range

At constant accuracy, $`\Omega(\log N)`$ items are necessary already for $`G=\mathbb F_2^r`$: take the $`r`$ coordinate kernels. A unit-vector query isolates each coordinate item, forcing every one to remain.

The joint $`\log N/\epsilon^2`$ dependence is also necessary in the usual nontrivial accuracy regime. Let $`K_{s,B}`$ be a complete bipartite graph, with
```math
s=\lceil\epsilon^{-2}\rceil,\qquad
 B\ge s,\qquad 0<\epsilon\le1/2,
```
and $`n=s+B`$. Take the assignment group
```math
G=\mathbb F_2^n/\langle\mathbf1\rangle,
 \qquad N=2^{n-1}.
```
For each edge $`uv`$, its accepting subgroup is
$`\{x:x_u=x_v\}`$, which is well-defined on the quotient. The sum of violations is exactly the cut size.

The elementary complete-bipartite cut lower bound gives, for any nonnegative reweighting preserving all cuts, at least
```math
\frac{(1-\epsilon)^2sB}
 {(1+3\sqrt2\,\epsilon\sqrt s)^2}
 =\Omega(n/\epsilon^2)
 =\Omega(\log N/\epsilon^2)
 \tag{A23}
```
retained original edges. A derivation using degree constraints, signed cut discrepancies, Khintchine's inequality, and Jensen's inequality appears as (EC15) in the companion exact-label-cut manuscript. This is an inherited classical cut obstruction, not a claim of a new ordinary cut lower bound.

Thus (A2) has the correct worst-case order when
$`\log_2N+1\ge2\lceil\epsilon^{-2}\rceil`$, subject to the natural cap by $`m`$.

## 7. Related work

**Quanrud's entropy/quotient theorem gives a particularly relevant comparison.** For homogeneous subgroups $`H_e\le G`$, let a uniformly random $`g\in G`$ induce the coset-valued variables $`gH_e`$. Their joint entropy is
```math
f(S)=\log_2\!\left[G:\bigcap_{e\in S}H_e\right].
```
It is a normalized monotone submodular function, every positive marginal is at least one, and $`r=f([m])\le\log_2|G|`$. For a fixed query $`g`$, the zero-item set $`Z_g=\{e:g\in H_e\}`$ is closed: if adding $`H_e`$ leaves the intersection unchanged, that intersection is contained in $`H_e`$, so a query satisfying all its members also satisfies $`e`$.

Quanrud's public Theorem 1.1 therefore gives $`O(r\log(mr)/\epsilon^2)`$ support directly, including for nonnormal subgroups. The adaptive resparsification consequence in [../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md](../../label-block-cut/manuscripts/adaptive-quotient-resparsification.md) removes the ground-set dependence and gives
```math
O\!\left(\frac{r\log(2r/\epsilon)}{\epsilon^2}\right).
 \tag{A24a}
```
The wreath compiler applies the same comparison to arbitrary cosets with $`r=O(\log(2N))`$. Thus (A24a) is the sharper checked comparison for this group class; the new Gaussian result removes its remaining logarithm. The cleaner resparsified formula is not attributed as a verbatim theorem of Quanrud.

The public theorem explicitly permits real-valued ranks with minimum positive marginal one; integrality is not needed for this existential/oracle comparison. Whether an implicitly represented logarithmic rank admits the required polynomial-bit optimization oracle is a separate computational question and does not invalidate the comparison. [Primary source, Theorem 1.1 and Corollary 1.7](https://kentq.s3.amazonaws.com/submodular-sparsification.pdf).

**Brakensiek--Guruswami, STOC 2025, expanded 2026 version.** Theorem 6.8 of *Redundancy Is All You Need (for CSP Sparsification)* explicitly gives weighted subgroup-code sparsifiers, including nonabelian alphabet groups, of size
```math
O(\log|\mathcal C|\,\log^6m/\epsilon^2).
```
Theorems 6.11--6.12 give weighted sparsification with a polylogarithmic overhead for complements of general Mal'tsev predicates. Nonabelian group-code sparsification and Mal'tsev CSP sparsification are therefore established public models. [Primary source](https://arxiv.org/html/2411.03451v2).

**Brakensiek--Guruswami--Putterman, ICALP 2026.** Theorem 1.2 of *Multiplicative Error Set System Sparsification: A Simpler Proof via Chain Length Contraction* improves the general weighted support bound to
```math
O\!\left(
 \frac{d\log^2(2d/\epsilon)
 [\log\log(4d/\epsilon)]^2}{\epsilon^2}
 \right),
 \tag{A24}
```
where $`d`$ is the union-closure chain length. The result is independent of the number of original items, so an older $`\log^6m`$ comparison alone would be incomplete. This is the stronger general set-system bound, while the entropy-based comparison above is sharper for the present group class. [Primary source](https://arxiv.org/html/2605.01508v1).

For the present coset predicate family, $`d=O(\log(2N))`$. To see this on the correct side of the incidence system, let
```math
S_g=\{e:g\notin C_e\}.
```
A nested chain of unions of the $`S_g`$'s can be represented by nested accumulated query sets $`T\subseteq G`$. The complement of such a union consists of cosets $`C_e`$ containing all of $`T`$, equivalently containing its affine hull: for nonempty $`T`$ and $`a\in T`$, this hull is
```math
\mathrm{aff}(T)
 =a\langle a^{-1}t:t\in T\rangle.
```
Every strict increase of a nonempty affine hull multiplies its size by at least two. The possible initial empty hull contributes one extra step. If the violated-item union increases, its affine hull must increase as well. This proves the claimed chain bound and makes (A24) an applicable broader baseline.

**Algebraic antecedent.** Dinh--Moore--Russell's *McEliece and Niederreiter Cryptosystems That Resist Quantum Fourier Sampling Attacks*, Proposition 3, supplies the standard wreath subgroup used in Section 2. The present proof is classical and uses no quantum algorithm. [Primary 2011 manuscript](https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/aa/25/aa2531de-e04e-4fea-8772-6f9341ddb6b7/11-06-021.pdf).

**Analytic antecedents.** Slepian's Gaussian comparison is classical. The dilated partial-coloring theorem is Reis--Rothvoss, Theorem 7 of the July 2026 version of *Linear-size $`\ell_1`$ Sparsifiers*. The new hereditary Gaussian-section bridge and the homogeneous subgroup mass theorem are proved in the companion subgroup manuscript; they are the support backend used here. [Slepian](https://doi.org/10.1002/j.1538-7305.1962.tb02419.x); [Reis--Rothvoss](https://arxiv.org/html/2606.28147v2).

The resulting increment is the removal of the remaining support logarithm for arbitrary weighted finite-group coset constraints, with arbitrary arity and no common satisfying assignment, and the arbitrary-center group-code corollary. This manuscript does not claim a compact polynomial-time optimal construction, an improvement for arbitrary Mal'tsev algebras, or a theorem for arbitrary nonabelian word equations.
