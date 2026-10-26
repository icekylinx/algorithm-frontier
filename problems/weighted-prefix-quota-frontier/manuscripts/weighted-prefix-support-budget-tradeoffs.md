# Sharp support-budget tradeoffs for one and two weighted-prefix orders

**25 October 2026. Complete incremental theorem and proof; full internal mathematical reviews completed for checkpoint T.**

For common-weight prefix quotas, the largest target alone does not describe the full exact complexity. The number of distinct original row-incidence patterns gives a sharper tradeoff. One order has a square-root product exponent, capped by the linear largest-target exponent. Two arbitrary orders have a second regime, reaching the largest-target-times-logarithm exponent.

This note concerns one common nonnegative integer weight vector. It does not permit a different weight vector on each row. The resource is one arbitrary integral polymatroid, with optional vectors or original-total bases, and the separately optimized scalar is arbitrary signed rational.

The upper bounds are deterministic and use polynomial binary workspace. The matching lower classification is in the general rank-oracle model under parameter upper budgets. A separate section gives readable-rank-program ETH families without claiming an ETH theorem for every exact parameter pair.

## 1. The original incidence parameter

Use the one-order model PX or the two-order model TP. Let B be the largest input target. Split equalities, perform the exact zero-target preparation and within-order dominance cleanup, and retain the original required resource total.

For each eligible positive-weight coordinate e, let S_e be the set of retained quota rows whose prefix contains e. Define

$$
C=\left|\{S_e:S_e\ne\varnothing,\ w_e>0\}\right|.
 \tag{PS1}
$$

C counts original positive supports after the prescribed preparation, before active/passive copying. It does not count distinct coefficient magnitudes. Zero-weight coordinates remain available for resource use and the scalar objective, but contribute no positive support.

Within one order there are at most 2B retained rows, so C<=2B. With two orders a coordinate occupies one prefix-incidence interval in each order, and therefore

$$
C\le(2B+1)^2-1.
 \tag{PS2}
$$

These are counting bounds, not arrays constructed through the numeric target. Actual supports and occupied intervals are obtained from the explicit row and coordinate data.

For positive real b,c define

$$
\begin{split}
 g_1(b,c)&=\sqrt{b\min\{c,b\}},\\
 g_2(b,c)&=\min\left\{\sqrt{bc},\
 b\log_2\left(2+\min\{c/b,b\}\right)\right\}.
 \end{split}
 \tag{PS3}
$$

**Upper theorem.** One order admits exact time

$$
2^{O(g_1(B,C))}\mathrm{poly}(H);
 \tag{PS4}
$$

two arbitrary orders admit exact time

$$
2^{O(g_2(B,C))}\mathrm{poly}(H).
 \tag{PS5}
$$

Both have polynomial binary workspace. If B=0 or C=0, the direct preprocessing and scalar tests are polynomial.

**Worst-case budget theorem.** For every integer b>=2^14 and c>=1, there are polynomial(b)-size explicit coefficient families with actual largest target at most b and actual support count at most c, for which any randomized algorithm correct with probability at least 2/3 needs at least

$$
2^{g_1(b,c)/64}\quad\hbox{or}\quad 2^{g_2(b,c)/64}
 \tag{PS6}
$$

worst-case rank queries, respectively.

For mandatory bases these are equality-feasibility lower bounds with scalar zero. For optional independent sets the low-pattern construction uses exact scalar cardinality maximization; the high-pattern two-order construction already works for equality feasibility. These distinctions are part of the statement.

The constants are deliberately conservative. The budget theorem does not assert a lower bound for each exact parameter pair, nor for every given order geometry or explicit resource representation.

## 2. Two analyses of the same colored profile catalogue

On the prepared ground every nonzero column has the form a times the indicator of a support color. The one-order lift has at most two copies per coordinate; the two-order lift has at most four. Consequently

$$
q\le2C\ \hbox{for one order},\qquad
 q\le4C\ \hbox{for two orders}.
 \tag{PS7}
$$

This holds even when distinct original supports merge after deleting cover components. Each original support has at most two or four deterministic marked images.

The canonical first-reaching representatives from PX and TP have total nonzero magnitude mass at most

$$
W_1=2B-1,\qquad W_2=4B-2.
 \tag{PS8}
$$

All original resource units remain, including the zero-vector remainder, and every real scalar weight remains on its copies. The mass is an auxiliary profile bound, not the original resource rank.

Let P_q(W) be the cumulative number of q-colored integer partitions of mass at most W. The generating function proof gives

$$
P_q(W)\le\exp(2\sqrt{2qW}).
 \tag{PS9}
$$

A second direct count gives

$$
P_q(W)\le2^W\binom{q+W}{W}.
 \tag{PS10}
$$

Indeed, choose h used colors, then their positive masses summing to at most W in binomial(W,h) ways. A partition of a positive mass w on one color injects into compositions of w and has at most 2^w choices. Multiply and sum over h; Vandermonde's identity gives PS10.

These are bounds on the same catalogue. No selection of a numerical analysis parameter is required. The streamed occupied-class generator maintains mass and total-count caps. Zero completion of remaining multiplicities charges every generated state, including failed quota filters and empty resource intersections, to the catalogue up to polynomial depth.

Every final profile is recovered on one global resource/partition-count integral face with the original required total. Neither the coordinates nor the resource are decomposed by support color.

## 3. Deriving the upper tradeoffs and budget monotonicity

For one order, PS7--PS9 give exp(O(sqrt(BC))). The original q<=3B bound also gives exp(O(B)). Their minimum proves PS4.

For two orders, PS7--PS9 give exp(O(sqrt(BC))). Using PS10 and binomial(q+W,W)<=[e(1+q/W)]^W gives exp(O(B log(2+C/B))). The general two-order color bound q<=(3B+1)^2-1 separately gives exp(O(B log(B+2))). Taking the minimum proves PS5.

All counts concern polynomial-size copied grounds. For one order there are two shared labels; for two orders there are four. No array indexed by B or the original resource rank is stored. The smaller analytic bound therefore retains the original uniform polynomial-space guarantee.

Both g_1 and g_2 are nondecreasing in both arguments. For g_1 this follows by writing it as min{sqrt(bc),b}. For g_2, write it as the minimum of sqrt(bc), b log_2(2+c/b), and b log_2(b+2). The only less immediate derivative, apart from a positive logarithm conversion constant, is

$$
\frac{d}{db}\bigl[b\ln(2+c/b)\bigr]
 =\ln(2+z)-\frac{z}{2+z}>0,\qquad z=c/b.
 \tag{PS11}
$$

Thus the per-instance upper bounds also bound the entire class with B<=b and C<=c.

## 4. Complementary-pair blocks for the low-pattern regime

Fix positive integers p and a. Make p consecutive blocks of 4a elements each. Within each block the common weights are 1,2,...,4a. Put

$$
\alpha=a(4a+1),
 \tag{PS12}
$$

and impose equality to j alpha at the prefix ending after block j, for j=1,...,p. Thus

$$
B'=p\alpha,\qquad C'=p.
 \tag{PS13}
$$

There is exactly one distinct original positive incidence support per block. Within a block, pair i with 4a+1-i. There are 2a complementary pairs. Choose any a of them, giving 2a elements of weight alpha.

Let G be the products of these choices across all p blocks. Its sets have size r=2ap and satisfy every cumulative equality. Its size obeys

$$
N=\binom{2a}{a}^p\ge2^{ap},
 \tag{PS14}
$$

because binomial(2a,a)>=2^a.

Crucially, let H be ALL rank-r subsets satisfying the cumulative equalities, not just the explicitly countable subfamily G. Some other sets in H can distribute their cardinalities differently between blocks.

Every individual full coefficient vector is distinct: weights distinguish elements inside a block, and the cumulative prefix incidences distinguish different blocks. Consequently two distinct members of H are not one-exchange neighbors.

The reference rank-r matroid permits all sets smaller than r and all rank-r sets outside H. A hidden instance additionally permits one A in G. The usual two-augmentation argument proves validity because no two forbidden rank-sized sets are exchange neighbors. Reference rank-r bases exist by replacing one element of a member of G with a different, unselected weight in the same block.

The rank oracles differ only on the hidden query A. In the base model, the reference equality instance is infeasible and the hidden instance has unique feasible base A.

For optional independent sets, the equalities do not in general force cardinality r. Instead maximize cardinality as the separately optimized scalar. The hidden optimum is r. The reference has no feasible set of that size; it is either infeasible or has a smaller optimum. Thus exact scalar optimization still distinguishes the family. This is not an optional pure-feasibility lower claim.

Under the balanced reference/hidden distribution, success at least 2/3 needs at least N/3 worst-case rank queries. The full ground has 4ap elements, and all coefficient data are explicit.

## 5. Calibrating every low-pattern budget

Given integers b>=20 and c>=1, choose

$$
p=\min\{c,\lfloor b/5\rfloor\},\qquad
 a=\left\lfloor\sqrt{\frac{b}{5p}}\right\rfloor.
 \tag{PS15}
$$

Both are positive. Since a>=1,

$$
B'=pa(4a+1)\le5pa^2\le b,\qquad C'=p\le c.
 \tag{PS16}
$$

Also a>=one half of sqrt(b/(5p)), and p>=min(c,b)/10. Therefore

$$
\log_2N\ge ap
 \ge\frac{\sqrt{bp}}{2\sqrt5}
 \ge\frac{g_1(b,c)}{2\sqrt{50}}
 >\frac{g_1(b,c)}{16}.
 \tag{PS17}
$$

This proves the one-order budget lower across every c, including c larger than the number of possible effective patterns. The chosen actual parameter need only be below the budget.

The same one-order instances are also two-order instances, by providing no extra rows in the second order. When c/b<=4, one has g_2(b,c)<=2g_1(b,c). Hence PS17 gives

$$
\log_2N>g_2(b,c)/32
 \qquad(c/b\le4).
 \tag{PS18}
$$

The input size is polynomial in b: p<=b/5, a<=sqrt(b), and 4ap=O(b). No numeric budget c enlarges the actual coefficient encoding beyond polynomial(b).

## 6. Bipartite permutation blocks for higher pattern budgets

Suppose b>=20 and c/b>4. Set

$$
k=\min\{\lfloor c/b\rfloor,\lfloor b/2\rfloor\},
 \qquad L=\lfloor b/k\rfloor,\qquad B'=Lk.
 \tag{PS19}
$$

Then k>=4, k<=b/2, and b/2<=B'<=b. Take L disjoint copies of K_{k,k}, with B' vertices on each side in total. The ground consists of their edges, all with common weight one.

Order edges first by their left endpoint, with arbitrary order inside a block. At the end of the i-th left block impose cumulative equality i, for i=1,...,B'. The second coordinate order groups edges by right endpoint and has the analogous equalities.

Subtracting consecutive cumulative equalities forces degree one at every left and right vertex. The feasible edge sets are exactly perfect matchings of the disjoint union. The largest target and original support count are

$$
B',\qquad C'=Lk^2=B'k\le bk\le c.
 \tag{PS20}
$$

The original support distinguishes every allowed pair of endpoints, so C' is exactly the edge count, despite the common weight being one.

There are

$$
N=(k!)^L
 \tag{PS21}
$$

candidate perfect matchings, all of rank size B'. Distinct cumulative coefficient vectors imply nonadjacency under one exchange. A reference rank-B' matroid forbids all of them; a hidden instance restores one. An outside reference basis is obtained by a single replacement creating a repeated endpoint. All equalities, including the last full-prefix equality, force cardinality B', so the reference/hidden distinction is feasibility in both resource conventions.

For k>=4, k!>=(k/2)^{k/2} gives log_2(k!)>=(k/4)log_2k. Put z=min(c/b,b). Since k>=z/4 and k>=4, one has 2+z<=5k<=k^3. Thus

$$
\log_2N\ge\frac{B'}4\log_2k
 \ge\frac b{24}\log_2(2+z)
 \ge\frac{g_2(b,c)}{24}.
 \tag{PS22}
$$

There are O(b squared) edges and O(b) rows, giving polynomial(b) explicit data. The resource is one globally hidden matroid, not a direct sum of independent resource oracles.

Combining PS17, PS18 and PS22 gives N>=2^{g_i(b,c)/32} in the corresponding models. Since g_i(b,c)>=sqrt(b), taking b>=2^14 ensures N/3>=2^{g_i(b,c)/64}. This proves PS6.

## 7. Readable-rank-program families and computational hypotheses

The low-pattern construction also gives a uniform family of encoded ETH reductions. Let phi have nu variables. Choose any polynomial-time computable p with 1<=p<=nu, and set a=ceil(nu/p). Then

$$
\nu\le ap\le2\nu,\qquad
 B'=pa(4a+1),\qquad C'=p,\qquad
 \sqrt{B'C'}=\Theta(\nu).
 \tag{PS23}
$$

The hidden-candidate count in PS14 is at least 2^nu and at most 2^{4nu}. A candidate in G is represented by, in each block, an a-subset of the 2a complementary-pair identifiers. Standard binomial suffix counts rank each such subset in polynomial time. Combining the p ranks in radix binomial(2a,a) ranks all members of G.

Accept a member of G precisely when the nu assignment bits of its rank modulo 2^nu satisfy phi. Reject H minus G. Permit every rank-r set outside H and all smaller sets. The forbidden family is a subfamily of the nonadjacent family H, so this is a valid matroid for every formula.

Its complete rank evaluator returns cardinality below r, full rank above r, and full rank on rank-sized sets outside H. Within H it recognizes the complementary-pair form, computes the product rank when applicable, and evaluates one assignment. All these operations and the full program/circuit size are polynomial in nu+|phi|.

The rank-r equality instance is feasible exactly when phi is satisfiable. The optional exact-cardinality objective distinguishes the same inputs. Therefore deterministic ETH rules out time 2^{o(sqrt(BC))} poly(H) along these calibrated low-pattern families. Ordinary deterministic ETH is not used to exclude randomized algorithms.

The dense two-order endpoint already has the permutation-ranking ETH reduction in TP. Product permutation ranking gives analogous intermediate families, but the oracle budget theorem above does not rely on an assertion of encoded hardness for every arbitrary numerical pair (b,c).

Algorithms may read all rank-program data, including the formula. No lower statement is transferred to graphic or explicitly matrix-represented resources by this construction.

## 8. Interpretation, dependencies, and attribution

For one order, a bounded number of actual incidence patterns gives a square-root largest-target exponent. As the pattern budget reaches the order of the target, the exponent becomes linear. For two unrelated orders, larger incidence catalogues add a second regime, reaching B log B.

In particular, C=1 does not have the same behavior as the one-support construction OS in checkpoint S. Here every row uses the same weight on a given coordinate, so the numeric vectors are scalar multiples of their incidence patterns. OS allowed different positive magnitudes in different rows. The parameterized models are different.

The lower family in Sections 4--5 uses a rankable complementary-pair subfamily only to supply many hidden candidates. The whole quota-feasible rank-sized family is forbidden in the reference matroid. This prevents overlooked feasible bases outside the chosen countable subfamily.

The upper proofs depend on the complete new PX and TP manuscripts:

- exact_weighted_prefix_quotas_max_target.md
- two_order_weighted_prefix_target_classification.md

Count-profile intersection and paving/SAT-decoder constructions have primary antecedents already recorded there, including:

https://arxiv.org/html/2404.03747v2

https://arxiv.org/html/2307.07773v2

https://arxiv.org/html/2412.02217v2

The new contribution here is the incidence-sensitive upper analysis, the complementary-pair low-pattern family, and the all-budget calibration for one and two orders. No publication-priority claim or optimal leading exponential constant is asserted.
