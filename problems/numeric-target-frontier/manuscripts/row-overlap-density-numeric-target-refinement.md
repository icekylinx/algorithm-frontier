# Exact numeric targets controlled by row-overlap density

**25 October 2026. New complete incremental theorem and proof; root and independent full mathematical reviews passed.**

This successor refines the support-one/support-two boundary. When each resource coordinate is positive in at most two numeric rows, let `m` be the number of distinct row pairs that actually interact. With total integer target `T>0`, exact scalar optimization takes

$$
\boxed{
\exp\!\left(O\!\left(T\log\left(2+\frac mT\right)\right)\right)
\mathrm{poly}(H)
}
\tag{RD1}
$$

and polynomial binary workspace. In particular, `m=O(T)` gives singly exponential time even when the maximum row-interaction degree is unbounded. Dense hidden-matching families match the displayed exponent order; the support-one family supplies the zero-overlap endpoint.

The proof retains arbitrary mixed integer upper, equality, and covering rows, one global integral polymatroid with binary counts, and exact minimization or maximization of one arbitrary rational scalar. It also gives a general support-pattern counting lemma whose constant is independent of the support size.

## 1. Model, preprocessing, and the overlap graph

Use one normalized monotone integral polymatroid rank `F` on an explicit coordinate ground `E`. Integer vectors belong either to `P(F)` or to an original-total base `B(F)`. Eligibility masks are allowed. There are explicit nonnegative integer row vectors `a^j`, nonnegative integer targets `T_j`, and arbitrary relations `rho_j in {<=, =, >=}`. Let

$$
T=\sum_jT_j.
\tag{RD2}
$$

The separately optimized scalar `c x` is arbitrary rational, including signed coefficients; it is not counted as a numeric target row.

For optional vectors, use the legitimate free-disposal base conversion with original rank `R`, zero row coefficients, and zero scalar coefficient. Mandatory original bases receive no disposal. Remove automatic zero-target cover rows. Mask coordinates exceeding an upper or equality target; a zero target of these kinds masks every positive coefficient in that row and the resulting zero row is removed. Retain the original required total and reject rank loss.

Let `F0` be the resulting prepared resource rank. All surviving targets are positive integers, so their number `d'` is at most `T`. The original target sum is unchanged by removal of zero-target rows. If no positive row survives, exact scalar optimization is polynomial.

Assume each eligible coordinate has a positive coefficient in at most two surviving rows. Form the simple row-interaction graph with these rows as vertices: distinct rows are adjacent if some eligible coordinate is positive in both. Let `m` denote its edge count. Multiple original coordinates with the same positive row pair create only one interaction edge.

This graph records target-row incidence, not the structure of the resource rank. `F0` may couple all coordinates arbitrarily.

## 2. At most four shared copies per original coordinate

For an original coordinate `e`, let `C_e` be the positive covering rows incident with it. It has at most two members. Create one copy `(e,S)` for every subset `S` of `C_e`, and let `pi` forget the subset label. Give these copies the shared rank

$$
F^\uparrow(Y)=F0(\pi(Y)).
\tag{RD3}
$$

As in the earlier shared-copy proofs, this is an integral polymatroid rank. Aggregation `x_e=sum_S z_(e,S)` gives exact independent-vector and base equivalences. Every copy retains the original scalar coefficient `c_e`. The ground has at most four times its original size.

An upper or equality row keeps its original coefficient on every copy. A covering row incident with `e` gives `(e,S)` coefficient `min(a^j_e,T_j)` if `j in S`, and zero otherwise. All other row coefficients are zero.

For a feasible original integer base, choose in every positive cover row a first-reaching prefix after capping its unit contributions at the target. Its credited total belongs to `[T_j,2T_j-1]`. Each original unit is labeled by those incident cover rows that marked it. Since only positive incident rows matter, the local subset labels include every simultaneous marking choice. No global ordering or enumeration of all cover-row permutations is needed.

Conversely, true covering values dominate their credited values, while all upper/equality rows and the scalar agree exactly. The union of copied integer bases with allowed credited totals therefore represents precisely the feasible original integer vectors with the same scalar values. No original resource unit is discarded.

Let

$$
U_j=\begin{cases}
T_j,&\rho_j\in\{\le,=\},\\
2T_j-1,&\rho_j=\ge,
\end{cases}
\qquad U=\sum_jU_j.
\tag{RD4}
$$

For positive targets,

$$
T\le U\le2T.
\tag{RD5}
$$

Every nonzero auxiliary coefficient vector has support either a singleton row or an original interaction edge. Local copying may delete a positive cover component, but it cannot create a new interaction pair. If `Q` is the number of distinct nonempty support patterns among the actual copied vectors, then

$$
Q\le d'+m\le T+m.
\tag{RD6}
$$

Different coefficient magnitudes on the same row pair do not increase `Q`.

## 3. An exact-support composition bound

Fix one nonempty support set `S` of size `t`. Consider a multiset of nonzero nonnegative integer vectors having **exactly** support `S`, with total entry sum `w`. If `w>=1`, the number of such multisets is at most

$$
2^{w-1}\le2^w,
\tag{RD7}
$$

independently of `t`.

To prove this, fix an order on the coordinates of `S` and lexicographically order the vector occurrences of a multiset. Suppose there are `k` vector occurrences, including repetitions. Write all their entries in order. Because the support is exactly `S`, this is a sequence of `kt` positive integers with sum `w`.

Encode the sequence as a composition of `w`, equivalently as the subset of cut positions among `w-1` places. The cut set determines the sequence length; since `t` is fixed, it also determines `k`. Grouping the decoded sequence into consecutive groups of length `t` recovers the canonically ordered vectors and hence their multiset. Thus the encoding is injective. There are exactly `2^{w-1}` compositions of `w`.

Alternatively, for each `k` the ordered positive sequences number `binom(w-1,kt-1)`, and summing these over the possible `k` uses distinct binomial coefficients from the same row, with sum at most `2^{w-1}`. There is no additional multiplicity factor for `k`.

For weight zero there is only the empty multiset. The positivity of every entry on the exact support is essential; zero entries outside `S` are omitted from the encoding.

## 4. Choosing used patterns and their numeric weights

A complete nonzero coefficient profile is a multiset of actual auxiliary vectors. Decompose it uniquely according to their exact nonempty supports. If it uses `h` of the `Q` available support patterns, choose those patterns in `binom(Q,h)` ways. In their fixed order, let their positive total entry weights be `w_1,...,w_h`.

The total target allowance gives `sum_i w_i<=U`. The number of ordered positive integer weight assignments with this inequality is

$$
\binom Uh.
\tag{RD8}
$$

This follows by subtracting one from each positive entry and adding one nonnegative slack variable. For any such assignment, RD7 bounds the choices of local vector profiles by

$$
\prod_{i=1}^h2^{w_i}\le2^U.
\tag{RD9}
$$

Restricting vectors to those actually present in the input, imposing componentwise caps, or imposing a resource-count cap only reduces the family. Summing over `h`, including the empty profile, gives

$$
\begin{aligned}
\#\{\text{admissible upper-cap profiles}\}
&\le2^U\sum_{h=0}^{\min(Q,U)}\binom Qh\binom Uh\\
&=2^U\binom{Q+U}{U}.
\end{aligned}
\tag{RD10}
$$

The equality is Vandermonde's identity. The count records a multiplicity for each distinct coefficient vector, not the identities of the resource coordinates assigned that vector. Choosing those identities and optimizing their scalar weights is the integral subproblem below; it contributes no extra factor to RD10.

This lemma is independent of a bounded row dimension. It depends on the number of distinct exact support patterns, not on a full universe of coefficient vectors or row subsets.

## 5. Exact integer recovery and all-input enumeration

Group copied coordinates by their complete auxiliary coefficient vector `b`. Enumerate counts `h_b` only for occupied nonzero classes, maintaining

$$
m_0=\sum_{b\ne0}h_b\le R,
\qquad
W_j=\sum_{b\ne0}b_jh_b\le U_j.
\tag{RD11}
$$

The global zero-vector group receives `R-m_0`. At a complete profile apply the precise upper, equality, or credited-cover filter to each row.

The prescribed class counts define an integral partition-count polymatroid. Intersect it with `Fup` and require the original total `R`. This face is integral when nonempty, and every class cap is tight because their sum is `R`. Exact minimization or maximization of the original scalar on the face therefore gives an integer solution to that profile. An absent zero group with positive remainder gives an empty face, as required.

Use depth-first traversal with the next count bounded by the remaining rank and by every positive component's remaining allowance. Every partial state has a zero completion satisfying all component upper caps. Distinct partial states at the same depth have distinct such completions. Consequently all generated nodes, including every final row-filter and resource failure on infeasible inputs, are charged by occupied depth times RD10.

The resulting explicit time bound is

$$
\boxed{2^U\binom{Q+U}{U}\mathrm{poly}(H).}
\tag{RD12}
$$

Only one profile and one exact intersection subproblem are retained. The ground has at most four copies per original coordinate; the row vectors, count registers, and rank values have polynomial binary length. Neither numeric targets nor the resource rank are expanded into unit lists. This proves polynomial binary workspace uniformly in the number of rows.

Componentwise pruning is compatible with the older multivariate target bounds as well. RD10 itself only needs the total entry-weight upper bound, but the written implementation retains the stronger component restrictions throughout.

## 6. Deriving the overlap-density exponent

For `U>=1`,

$$
\binom{Q+U}{U}\le
\left(e\left(1+\frac QU\right)\right)^U.
\tag{RD13}
$$

Combining RD5–RD6 and RD12–RD13 bounds the logarithm of the profile factor by

$$
\begin{aligned}
U\left(\log2+1+\log\left(1+\frac QU\right)\right)
&\le2T\left(\log2+1+\log\left(2+\frac mT\right)\right)\\
&=O\!\left(T\log\left(2+\frac mT\right)\right).
\end{aligned}
\tag{RD14}
$$

This proves RD1. The zero-target case is handled by preprocessing and exact scalar optimization and needs no expression involving `m/T`.

If `m=O(T)`, the time is `2^{O(T)} poly(H)`. This includes row-interaction forests and any class with a linear number of interaction edges, even high-degree stars. If the maximum row-interaction degree is `Delta`, then `m<=d'Delta/2<=T Delta/2`, giving the weaker but sometimes convenient bound `exp(O(T log(Delta+2))) poly(H)`.

The number of possible interaction edges is at most `binom(d',2)<=T^2/2`. Hence the dense limit of RD1 is `2^{O(T log(T+2))}`, agreeing with the unrestricted variable-dimensional target order.

The support-one partition bound `exp(3 sum_j sqrt(U_j))` can be smaller than RD12. These are alternative analyses, and the tighter applicable estimate may be used.

## 7. Lower families matching the density order

The lower statements concern subfamilies and upper budgets on the interaction count. They do not assert that every exact prescribed pair `(T,m)` realizes the same lower bound.

Fix an even integer `b>=4` and take `l` disjoint complete graphs on `b` vertices. There are

$$
T=lb,\qquad m=l\binom b2=\frac{T(b-1)}2
\tag{RD15}
$$

vertices and edges as indicated. Use the edges as the resource ground and give an edge its endpoint-incidence vector as numeric row coefficients. Put target one at every vertex, so each column has support two and the row-interaction graph is exactly the chosen disjoint-clique graph.

Let `r=T/2` and let `H` be the family of its perfect matchings, viewed as rank-sized edge subsets. Its size is

$$
N=((b-1)!!)^{l}
=\exp\!\left(\Theta\!\left(T\log\left(2+\frac mT\right)\right)\right).
\tag{RD16}
$$

The equality in order follows from `log((b-1)!!)=Theta(b log b)`. An elementary lower estimate uses at least `floor(b/4)` factors of size at least `b/2`, and the upper estimate is `b^{b/2}`. Constants can be chosen uniformly for even `b>=4`.

Two distinct perfect matchings are not single-exchange neighbors, since all their vector sums are the all-ones vector and different edges have distinct incidence vectors. Define a reference rank-`r` matroid permitting every set smaller than `r` and every rank-sized set outside `H`. A hidden instance additionally permits one `A in H`.

The augmentation proof is the same elementary argument as in the mixed-target lower bounds: two candidate augmentations of an `(r-1)`-set are one-exchange neighbors, so at most one is forbidden. The two rank oracles differ only on query `A`; any larger query contains two adjacent rank-sized subsets and therefore a reference base. Reference bases exist, for example by replacing one matching edge within a clique by an edge creating a repeated endpoint.

Equality targets admit no reference basis and exactly the hidden basis. Pure covering targets do the same on independent sets or bases: at most `r` edges have total incidence at most `T`, while the `T` covers force incidence at least `T`. Pure upper rows do the same on bases, whose total incidence is already `T`. Thus these pure-feasibility orientations require

$$
\exp\!\left(\Omega\!\left(T\log\left(2+\frac mT\right)\right)\right)
\tag{RD17}
$$

rank queries along this family. Bounded-error randomized decision follows from the balanced reference/hidden distribution: success at least `2/3` requires at least `N/3` worst-case queries. The explicit coefficient data are polynomial in `T`.

For the zero-overlap endpoint, take disjoint equality rows with the four coefficients `1,2,3,4` and target five. At rank two per row, exactly the pairs `{1,4}` and `{2,3}` meet each equality. Their Cartesian products form `2^{T/5}` nonadjacent rank-sized sets, and the same hidden-matroid construction gives `2^{Omega(T)}` queries with `m=0`, as proved in [column-support-numeric-target-dichotomy.md](column-support-numeric-target-dichotomy.md).

Together these families match the worst-case order of RD1 from no overlap to dense overlap. They are rank-oracle constructions; they do not give analogous lower bounds for explicit graphic, linear, or laminar resource representations.

## 8. General fixed-support corollary

Suppose instead every original coordinate has a positive coefficient in at most a fixed number `s` of target rows. Copy it according to subsets of its positive incident cover rows, using at most `2^s` shared copies. All earlier soundness, completeness, scalar preservation, and profile-recovery arguments apply.

Let `Q` be the number of distinct nonempty exact support patterns after this local copying. The composition proof RD7 is independent of `s`. Therefore the same explicit profile bound and time bound hold:

$$
2^U\binom{Q+U}{U}\mathrm{poly}(H)
\tag{RD18}
$$

for fixed `s`, with polynomial binary workspace. The hidden constant in the polynomial pays for the explicit local copies. The bound depends on support patterns actually produced, not on all subsets of the row set.

If `s` is not fixed, this local-copy implementation may have an exponentially large ground. No uniform polynomial-space claim for that implementation is made. The separately reviewed common-order chain reduction remains the uniform-space method for unrestricted support, with its explicit chain enumeration factor.

## 9. Attribution and boundaries

Guessing coefficient-vector multiplicities and imposing them through a partition matroid has established public antecedents; a primary account appears in Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*:

<https://arxiv.org/html/2404.03747v2>.

Paving-matroid hiding constructions and hard intersections involving one arbitrary matroid and partition or matching constraints also have public antecedents, including Doron-Arad, Kulik and Shachnai:

<https://arxiv.org/html/2412.02217v2>.

This note proves the stated density-sensitive numeric-target bound and its matching-order families directly. It does not claim first publication of a broad constrained-matroid algorithmic paradigm.

The optimized scalar is preserved exactly. No unrelated extra scalar objective under another side condition is added. One global resource polymatroid is used; a second unrelated resource rank would invalidate the two-rank integral-profile subproblem. Target coefficients remain nonnegative integers, and the numeric target sum remains distinct from approximation accuracy.
