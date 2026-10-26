# A sharp column-support dichotomy for exact numeric targets

**25 October 2026. Complete incremental theorem and proof; root and independent full mathematical reviews passed.**

For one global integral polymatroid, exact mixed numeric rows behave differently when each resource coordinate participates positively in at most one row versus at most two rows. With total integer target `T`, column support one admits `2^{O(T)}` time, while column support two already requires `2^{Omega(T log T)}` rank queries in the general oracle model. Both upper bounds have polynomial binary workspace. The distinction concerns target-row incidence; the scalar being optimized is separate.

This note strengthens the parameter comparison in [fixed-dimensional-mixed-numeric-targets.md](fixed-dimensional-mixed-numeric-targets.md) and [variable-dimension-total-target-classification.md](variable-dimension-total-target-classification.md). It does not assert that count-profile intersection itself is new.

## 1. Model and theorem

Let `F` be one normalized monotone integral polymatroid rank on an explicit ground `E`. Integer vectors are required to belong either to `P(F)` or to the original base `B(F)`. Rank values and resource counts are binary encoded. Eligibility masks are allowed and retain the original total in the base model.

There are explicitly listed nonnegative integer row coefficients `a^j_e`, integer targets `T_j>=0`, and independently chosen relations `rho_j` from `{<=, =, >=}`. The number of rows is part of the input. Put

$$
T=\sum_jT_j,
\qquad
s=\max_{e\in E}|\{j:a^j_e>0\}|.
\tag{CS1}
$$

An arbitrary rational scalar functional `c x` is to be minimized or maximized exactly. Its coefficients may be signed and do not contribute to `s` or `T`.

**Support-one theorem.** If `s<=1`, exact optimization with infeasibility reporting takes

$$
\boxed{
\exp\!\left(3\sum_{j:T_j>0}\sqrt{U_j}\right)
\mathrm{poly}(H)
\ \le\ e^{3T}\mathrm{poly}(H),
}
\tag{CS2}
$$

where surviving upper/equality rows have `U_j=T_j`, surviving cover rows have `U_j=2T_j-1`, and zero-target rows are preprocessed as below. Workspace is polynomial in the full binary input `H`, uniformly in the number of rows.

For this support-one model there are equality-target instances with `T=5d` requiring `2^{Omega(T)}` rank queries. This lower bound holds for bounded-error randomized decision with success at least `2/3`, already on ordinary matroids. Therefore the total-target exponent is sharp in order.

**Support-two boundary.** If `s<=2`, the general mixed-target upper bound is

$$
2^{O((T+1)\log(T+2))}\mathrm{poly}(H),
\tag{CS3}
$$

with polynomial binary workspace. A matching `2^{Omega(T log T)}` rank-query lower bound already holds with `s=2`, every nonzero coefficient equal to one, and every target equal to one. Thus merely allowing a coordinate to participate in a second target row changes the worst-case total-target exponent.

These are oracle-model classifications, not lower bounds for explicit graphic or linear representations. The numeric target sum is not approximation accuracy.

## 2. Base representation and zero targets

For optional vectors, add one free disposal coordinate of zero target coefficients and zero scalar coefficient. Its rank equals `F(S)` on sets not containing disposal and the original rank `R=F(E)` on sets containing it. This is an integral polymatroid rank and represents exactly the original independent vectors by completion to total `R`.

An original mandatory base receives no disposal. Every later mask retains its original total. Mask coordinates whose coefficient exceeds an upper or equality target. This is valid for nonnegative integer counts. A zero upper or equality target masks every positive coefficient in that row, after which the row is identically zero. A zero covering target is automatic. Remove these zero-target rows and reject original rank loss when applicable.

All remaining targets are positive integers. The support-one property is retained. Coordinates with zero coefficients in every target row are retained, including when their scalar coefficient is nonzero; they can be necessary for a mandatory base or for exact scalar optimization.

## 3. Only one active/passive choice is needed per cover coordinate

Let `F0` denote the prepared resource rank after the masks and the legitimate optional disposal conversion, retaining the original required base total `R`.

The positive supports of the target rows are now disjoint. If a coordinate `e` has positive coefficient in a covering row `j`, create two copies, active and passive. Both retain its original scalar coefficient. The active copy has credited coefficient `min(a^j_e,T_j)` in row `j`; the passive copy has zero coefficients in every target row. A coordinate belonging to an upper or equality row, or to no row, needs only one copy and retains its original row coefficients.

Let `pi` project the copied ground to the original eligible ground, and define

$$
F^\uparrow(Y)=F0(\pi(Y)).
\tag{CS4}
$$

This is an integral polymatroid rank. Aggregating copy counts gives exact equivalences of independent regions and original-total bases. All original resource capacities are shared, and every original scalar contribution is preserved.

Take an arbitrary original feasible integer base. In each positive covering row, cap unit credits at its target and mark a first-reaching prefix of its positive units. Its credited total lies in `[T_j,2T_j-1]`. Mark those units active and all other units of that row passive. Since a coordinate has a positive coefficient in at most one row, these choices never conflict with a second row. No permutation of covering rows and no subset-label family is needed.

Upper/equality totals and scalar contributions remain unchanged. Conversely, every credited cover total is bounded above by the true original row value, so any lifted vector satisfying the credited cover threshold projects to an original feasible vector. Exact scalar optima are preserved in both directions. This argument keeps all original units and applies to signed scalar coefficients.

The copied ground has at most twice the original number of coordinates, independently of the number of covering rows.

## 4. Per-row integer partitions and exact recovery

Every nonzero lifted coefficient vector has exactly one positive component. Group such coordinates by the pair `(j,a)`, where `j` is their row and `a>=1` their integer credited coefficient. Let `h_(j,a)` be its guessed count. For each row require during generation

$$
W_j=\sum_{a\ge1}a h_{j,a}\le U_j.
\tag{CS5}
$$

Also keep the total nonzero count

$$
m=\sum_{j,a}h_{j,a}\le R.
\tag{CS6}
$$

The one global zero-vector group receives count `R-m`. At complete profiles apply the actual upper, equality, or credited-cover interval to every `W_j`.

Prescribe these group counts through a partition-count polymatroid and intersect it with `Fup`. The total-`R` face is integral when nonempty. All group caps are tight there because they sum to `R`. Exact scalar optimization on this face therefore returns an integer vector with the entire profile enforced. An absent zero group with positive required remainder makes the face empty and is handled without exception.

Taking the best scalar over all feasible profiles solves the original problem exactly. The subproblem still uses only two polymatroids: the original shared resource and the profile partition.

## 5. Count bound, all-input traversal, and space

For each row, its profile is an ordinary integer partition of some value at most `U_j`, restricted to the coefficient values actually present. Let `P_1(U)` be the cumulative number of unrestricted integer partitions through `U`. For `U>=1` and `t>0`,

$$
P_1(U)\le
e^{tU}\prod_{a\ge1}(1-e^{-ta})^{-1}.
\tag{CS7}
$$

The logarithm of the product is

$$
\sum_{\ell\ge1}\frac{1}{\ell(e^{t\ell}-1)}
\le \frac1t\sum_{\ell\ge1}\frac1{\ell^2}
\le\frac2t.
\tag{CS8}
$$

Choosing `t=1/sqrt(U)` gives `P_1(U)<=exp(3 sqrt(U))`. Independent row-profile choices therefore have total number at most the exponential in CS2. The total count cap and final row filters can only reduce this number.

For a positive integer target `t`,

$$
\sqrt t\le t,
\qquad
\sqrt{2t-1}\le t,
\tag{CS9}
$$

where the second inequality is equivalent to `(t-1)^2>=0`. Thus `sum_j sqrt(U_j)<=T`, proving the final bound in CS2.

Use depth-first search only over occupied classes. Each next multiplicity is bounded by the remaining rank and the remaining allowance in its single row. Every partial state has a zero completion satisfying all these upper bounds. Distinct partial states at the same depth have distinct completions. Hence the whole traversal, including profiles later rejected by exact-row tests or resource infeasibility, costs only a polynomial factor times the counted profile family.

The algorithm stores one class list, one binary count profile, component sums, and one exact integral-intersection subproblem. Its depth is at most twice the original explicit ground size. No coefficient universe through `T`, rank-sized unit expansion, or collection of all profiles is stored. This proves uniform polynomial binary workspace. If no positive target row survives, scalar optimization is polynomial directly.

## 6. A support-one oracle lower bound

For any positive integer `d`, create four elements in each disjoint row block. Their positive coefficients in that row are respectively `1,2,3,4`, and all other row coefficients are zero. Set every equality target to `5`, so

$$
n=4d,\qquad r=2d,\qquad T=5d.
\tag{CS10}
$$

A row subset of these four elements sums to `5` precisely when it is either `{1,4}` or `{2,3}`. No singleton reaches `5`, and every three-element subset has sum at least `6`. Thus the family `H` of all sets satisfying every equality consists exactly of the `2^d` Cartesian choices of these two pairs, each of total size `r`.

Two distinct members of `H` differ in at least two elements on each changed row, so no two are single-exchange neighbors. Define the reference matroid `M0` by declaring all sets smaller than `r` independent and every rank-sized set outside `H` a base. For each hidden `A in H`, let `MA` additionally admit `A` as a base.

These are matroids. In the only nontrivial augmentation case, an independent `(r-1)`-set is compared with an independent `r`-set. With one possible added element, the result is the known independent larger set. With at least two possibilities, the resulting rank-sized sets are one-exchange neighbors, so at most one is forbidden. At least one valid augmentation exists. This argument also applies after the hidden member is added.

Their rank oracles differ only on query `A`. Below rank every set has its cardinality as rank. Above rank a queried set contains two adjacent rank-sized subsets, at least one of which is a reference base. At rank only the hidden member changes status.

The reference equality instance is infeasible, while the hidden instance has exactly its hidden member as a feasible set. This holds both for the base model and the optional independent-set model, because meeting every row requires exactly two elements per row and hence total rank.

The explicit row data have polynomial size in `d`. Under a balanced mixture of the reference instance and a uniformly random hidden instance, a worst-case `Q`-query algorithm has average decision success at most `1/2+Q/(2|H|)`: only hidden sets queried along the reference transcript can cause a different transcript. Success at least `2/3` on every input forces

$$
Q\ge 2^d/3=2^{\Omega(T)}.
\tag{CS11}
$$

This is a rank-oracle lower bound for the claimed exact numeric-target model, without an explicit-representation hardness claim.

## 7. Pure-cover and pure-upper optimization versions

The same family gives useful exact-optimization boundaries with only one orientation of numeric rows. In these versions let the scalar coefficient of an element be its unique positive row coefficient, so `c x` is the sum of all row contributions.

**Covering rows, scalar minimization.** Replace every equality by the cover `a^j x>=5`. Any feasible independent set has at most `r=2d` elements. Each row needs at least two elements because its largest individual coefficient is four, so every row receives exactly two. The scalar is at least `5d`. Equality holds exactly for `H`. The hidden optimum is therefore `5d`; the reference optimum is `5d+1`, attained by changing one chosen pair `{1,4}` to `{2,4}` while keeping equality pairs elsewhere. That set is a reference base. This proves the lower bound for exact scalar minimization with pure covers, in either resource convention. Equivalently, adding the separate scalar upper condition `c x<=5d` gives a feasibility distinction.

**Upper rows, scalar maximization.** Replace every equality by `a^j x<=5`. Three elements in one row would contribute at least six, so a base of size `2d` has exactly two in every row. The scalar is at most `5d`, with equality exactly for `H`. The hidden optimum is `5d`; the reference optimum is `5d-1`, attained by replacing one pair `{1,4}` with `{1,3}`. The same exact scalar-maximization distinction holds for optional independent sets: reaching total scalar `5d` forces every row to its cap and hence forces a full equality family member.

These constructions do not claim a support-one pure-cover or pure-upper feasibility lower bound without the scalar condition. In particular, pure upper feasibility over optional vectors always permits the zero vector. The extra scalar is not counted among the target rows in the incidence parameter.

## 8. Why support two has a larger exponent

The variable-dimensional theorem gives CS3 for every support. Its lower family already has support exactly two: use edges of a complete graph on an even number `d` of vertices as distinct endpoint-incidence vectors, put target one on every vertex row, and use a rank-`d/2` oracle matroid that forbids all perfect matchings except an optionally hidden one.

There are `(d-1)!!=2^{Theta(d log d)}` candidate perfect matchings, and two distinct candidates are not one-exchange neighbors. The same reference/hidden rank-oracle argument applies. Since `T=d`, this gives

$$
2^{\Omega(T\log T)}
\tag{CS12}
$$

queries. It works for equality targets, pure covers over independent sets or bases, and pure upper rows over bases, as proved in [variable-dimension-total-target-classification.md](variable-dimension-total-target-classification.md).

Thus the support-one `2^{Theta(T)}` order and support-two `2^{Theta(T log T)}` order form a sharp worst-case distinction for exact mixed-row optimization. For support one, the finer `sum_j sqrt(U_j)` upper bound can still be substantially smaller than `T`; the lower bound here establishes total-target worst-case order, not matching lower bounds at every specified target vector.

## 9. Public comparison and limits

Count-vector guessing followed by partition matroid intersection is an established technique. A primary description appears in Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2:

<https://arxiv.org/html/2404.03747v2>.

The proof here supplies the support-sensitive partition count, the charged two-copy representation for mixed covers, and the matching target-order oracle constructions. No first-use or publication-priority claim is made.

This incidence classification is also distinct from rank-parameterized intersection of several matroids. Huang and Ward already give deterministic fixed-parameter algorithms for weighted matchoids under independence oracles, and Huang, Kakimura, Kobayashi and Terao give polynomial-size reachable kernels for several cases involving one arbitrary matroid and partition or transversal matroids. These primary sources prevent treating the mere existence of rank-FPT algorithms for those intersections as a new consequence:

<https://arxiv.org/abs/2011.06268>,
<https://arxiv.org/html/2603.17345v1>.

The present theorem retains one global resource polymatroid, binary capacities, exact mixed numeric rows, and one arbitrary scalar optimization. It does not cover a second unrelated resource polymatroid through an unproved three-rank integrality claim. Signed target coefficients and cancellation-based representations are outside its counting argument.
