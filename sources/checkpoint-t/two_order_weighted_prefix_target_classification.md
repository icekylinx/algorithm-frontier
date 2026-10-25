# Two weighted coordinate orders: a sharp largest-target classification

**25 October 2026. Complete theorem and proof; full internal mathematical reviews completed for checkpoint T.**

Two arbitrary coordinate orders with a common nonnegative integer weight vector admit exact mixed prefix-quota optimization in

\[
 \boxed{2^{O(B\log(B+2))}\operatorname{poly}(H),
        \qquad B=\max_j b_j,}
 \tag{TP1}
\]

with uniform polynomial binary workspace. There is one global integral polymatroid resource, and the scalar objective is an arbitrary signed rational functional optimized exactly. Optional independent vectors and original-total bases are both covered. The sum of all targets, the number of input rows, and the binary resource rank need not be bounded by \(B\).

The exponential order is necessary for general rank oracles, already for unit weights and equality rows. A separate readable rank-program/circuit reduction gives the corresponding exclusion under deterministic ETH. This lower construction is a cumulative-prefix encoding of the known paving-plus-two-partition framework, not a new general framework for three-matroid intersection.

When the second order reverses the first, the upper bound improves to \(2^{O(B)}\operatorname{poly}(H)\). Thus mixed prefixes and suffixes on one line have a smaller worst-case exponent than two unrestricted orders.

## 1. Model and precise scope

Let \(F\) be one normalized monotone integral polymatroid rank on an explicit ground \(E\). Original integer resource vectors belong either to \(P(F)\) or to the original base \(B(F)\), with required total \(R=F(E)\). Ranks, counts and coordinate capacities are binary encoded. Eligibility masks are allowed.

Two linear orders \(\prec_1,\prec_2\) are explicitly given. The same nonnegative integer weight \(w_e\) is used by every row in both orders. Writing \(P_{i,p}\) for a prefix of order \(i\), the rows have the form

\[
       \sum_{e\in P_{i,p}} w_e x_e\ \rho\ b,
       \qquad i\in\{1,2\},\quad
       \rho\in\{\le,=,\ge\},\quad b\in\mathbb Z_{\ge0}.
 \tag{TP2}
\]

The rows are explicitly listed; not every prefix needs a row. Their endpoints, targets and relations are part of the input. Put \(B=\max b\), with \(B=0\) for an empty row list. An arbitrary rational scalar \(c^\top x\), whose coefficients may have either sign, is minimized or maximized exactly. A threshold on that same scalar is decided by its extremum. An additional different unbounded scalar constraint is not included.

The complete binary size is \(H\). Rank, submodular minimization and exact integral-polymatroid intersection computations are implemented with their polynomial input-bit and oracle costs charged. The result does not grant a free stronger oracle. No rank-sized unit expansion is performed.

## 2. Dominance compression, masks and zero cases

Split every equality into its upper and covering halves. For a duplicate endpoint and direction, retain the strongest target. Empty-prefix tests are immediate. The nonnegative cumulative weights are nondecreasing along each order.

Consequently a later upper row with no larger target dominates an earlier upper row, while an earlier covering row with no smaller target dominates a later covering row. In each order retain upper suffix-record minima and cover prefix-record maxima. After removal of zero-target rows as described next, the retained positive targets increase strictly with the endpoint in each family. If \(u_i\) and \(\ell_i\) are the retained upper and cover counts in order \(i\), then

\[
                  u_i\le B,\qquad \ell_i\le B.
 \tag{TP3}
\]

Zero covers are automatic. A zero upper target masks every positive-weight coordinate in its prefix and is then automatic. Also mask any coordinate with \(w_e>B\) that occurs in any original upper or equality prefix. Its positive integer use would violate that row. One may additionally mask \(w_e>b\) in an upper row of target \(b\), but this stronger mask is not required below. A coordinate is not masked just for occurring in a cover. Keep zero-weight coordinates; their resource mass and signed scalar contributions can matter.

For optional vectors, add one zero-weight, zero-scalar disposal coordinate after the original ground in both orders, outside the original prefixes. Its rank is \(F(S)\) when disposal is absent and \(R\) when it is present. Completing an original optional vector by \(R-x(E)\) disposal units gives an exact base representation. Original mandatory bases receive no disposal. All masks preserve the same required total \(R\); reject prepared rank loss. Denote the prepared resource rank by \(F_0\).

All these operations preserve the original feasible family and objective. They use sorting and lists of original endpoints, without an array indexed through \(B\). At \(B=0\), only the necessary masks remain and exact scalar optimization is polynomial. Assume \(B\ge1\) below.

## 3. Four shared labels and one common capped weight

Define

\[
                         v_e=\min\{w_e,B\}.
 \tag{TP4}
\]

For an eligible coordinate appearing in an upper row, \(v_e=w_e\). On integer vectors, capping at \(B\) preserves every covering predicate of target at most \(B\): if a used unit has weight at least \(B\), its capped weight alone reaches the target; otherwise the contributions are unchanged. This statement is about integer units, and is not asserted as an equivalence on arbitrary fractional vectors.

Give every original coordinate up to four copies \((e,a_1,a_2)\), with \(a_i\in\{0,1\}\). Zero-weight coordinates need only one copy. If an order has no cover rows, its marking bit can be fixed to zero. Every copy keeps the full original scalar coefficient \(c_e\). If \(\pi\) forgets the labels, use the shared rank

\[
                       F^{\uparrow}(Y)=F_0(\pi(Y)).
 \tag{TP5}
\]

This is a normalized monotone integral polymatroid rank. Projection preserves unions, and \(\pi(Y\cap Z)\subseteq\pi(Y)\cap\pi(Z)\); submodularity and monotonicity of \(F_0\) establish the required inequality. It does not create separate resource capacities for the different copies.

Aggregation \(x_e=\sum_{a_1,a_2}z_{e,a_1,a_2}\) is an exact equivalence of the resource regions, including total-\(R\) bases. In one direction, for an original subset \(A\), use the full inverse image \(\pi^{-1}(A)\) in the copied rank inequality. In the other, for any copied subset \(Y\), one has \(z(Y)\le x(\pi(Y))\le F_0(\pi(Y))\). Aggregation preserves the original scalar exactly.

Every upper row retains its full true coefficient on all copies in its prefix. A cover row in order \(i\) has coefficient \(v_e\) on copies with \(a_i=1\) in its prefix, and zero on other copies. Thus each nonzero auxiliary column has the form

\[
                              v_e\mathbf1_A
 \tag{TP6}
\]

for some nonempty set \(A\) of retained row labels. The common original weight is essential here.

Any integer copied point satisfying these auxiliary upper and cover rows projects to an original feasible point: upper values agree, and true covers dominate credited covers. This includes original equalities because both halves were retained or implied by retained rows. No chronological restriction on recovered marking bits is needed for soundness.

## 4. One canonical marked prefix for each order

Fix an arbitrary original feasible integer base, including its legitimate disposal completion if the original problem was optional. For each order with covers, let \(C_i\) be the largest retained cover target, so \(1\le C_i\le B\). Conceptually scan its positive-weight units in that order using capped weights \(v_e\), and mark the prefix through the first unit reaching \(C_i\). It exists by the cover of target \(C_i\). Its mass obeys

\[
                  C_i\le M_i\le C_i+B-1.
 \tag{TP7}
\]

Every cover in order \(i\) receives enough credit. If its prefix contains the cut, it receives all marked mass, at least \(C_i\). If it precedes the cut, all its original capped positive contributions are marked and its capped cover is satisfied. A cut partway through copies of the last coordinate of a prefix belongs to the first case.

Assign each unit its two marking bits. This simultaneous labeling uses the four shared copies and preserves the original counts and scalar. For repeated units of one coordinate, one can fix the same conceptual order of their indices for both scans; the two resulting binary labels coexist without any compatibility requirement. If an order has no covers, use bit zero throughout.

This is a completeness argument only. The algorithm stores no such unit sequence and never loops through a binary-sized \(R\).

## 5. Bounding the union of all nonzero auxiliary mass

For one order \(i\), let \(P_{U,i}\) be its last retained upper prefix when it exists. It contains all coordinates occurring in any retained upper row, and its true weighted mass in the original witness is at most \(B\).

Suppose there are covers. If the marking cut is inside \(P_{U,i}\), every marked positive unit lies there, and every passive unit with a nonzero contribution to this order also lies there. Hence the union of units with a nonzero auxiliary contribution to this order has capped mass at most \(B\).

If the cut is after \(P_{U,i}\), every positive unit of that upper prefix is marked. All nonzero contributions to this order are then contained in the marked units, with mass at most \(C_i+B-1\). With no uppers, this latter bound applies directly. With no covers, the relevant units lie only in \(P_{U,i}\), with mass at most \(B\). An order with no retained rows contributes no mass.

Set \(C_i=0\) when there are no covers, and use the convenient allowance

\[
 L_i=B+\max\{C_i-1,0\}\le2B-1,
 \qquad
 W=L_1+L_2\le4B-2.
 \tag{TP8}
\]

One can set \(L_i=0\) for an order with no rows, but it is unnecessary for the bound. A copied unit has a nonzero full auxiliary column only if it contributes to at least one order. Counting its common capped weight once, the union bound proves that the canonical representative satisfies

\[
                     \sum_{A,v}v h_{A,v}\le W,
 \tag{TP9}
\]

where \(h_{A,v}\) counts copied units whose column is \(v\mathbf1_A\). Units counted in both per-order unions cause no difficulty. The quantity in TP9 is weight per nonzero unit, not the sum of entries in its column. The latter could multiply the bound by the number of rows and is not used.

Every original feasible scalar value therefore occurs in a copied feasible profile with TP9. Conversely, every feasible profile, regardless of how it was marked, projects to an original feasible vector of the same scalar value.

## 6. Quadratically many colors and the profile count

In order \(i\), a passive bit gives the suffix of retained upper rows containing the coordinate, with at most \(u_i\) nonempty possibilities. An active bit gives all upper and cover rows containing it, with at most \(u_i+\ell_i\) nonempty possibilities. These bounds hold because all these sets change only at the respective prefix endpoints and vanish beyond the last endpoint. Merging both bit states leaves at most

\[
                        q_i\le2u_i+\ell_i\le3B
 \tag{TP10}
\]

nonempty support patterns for order \(i\), besides the empty one. The row-label sets of the two orders are disjoint. Thus the full color catalogue satisfies

\[
                q\le(q_1+1)(q_2+1)-1
                    \le(3B+1)^2-1.
 \tag{TP11}
\]

Different magnitudes on one color remain separate classes \((A,v)\), but only the classes actually occurring among at most four copies per coordinate are stored.

For one fixed color and positive total weight \(s\), its multiplicities form a multiset of positive integers with sum \(s\). Sorting these integers injects the multisets into the compositions of \(s\), so there are at most \(2^{s-1}\le2^s\) possibilities. Allowing all positive integer magnitudes only enlarges the actual catalogue.

If a profile uses \(k\) colors, choose them in \(\binom qk\) ways. Their positive weights summing to at most \(W\) have \(\binom Wk\) choices. Therefore

\[
 \#\text{profiles}
   \le2^W\sum_k\binom qk\binom Wk
   =2^W\binom{q+W}{W}
   =2^{O(B\log(B+2))}.
 \tag{TP12}
\]

For example \(\binom{q+W}{W}\le[e(q+W)/W]^W\) proves the last estimate for positive \(W\), using \(q=O(B^2)\) and \(W=O(B)\). If the actual color count or allowance is zero, there is only the zero nonzero-class profile. The resource-count cap \(\sum h_{A,v}\le R\), row filters, and restriction to actual magnitudes can only reduce this count.

## 7. One exact integral face and all-input binary complexity

Enumerate multiplicities of actual nonzero classes subject to TP9 and \(\sum h_{A,v}\le R\). A global zero-column group receives the remainder

\[
                              h_0=R-\sum h_{A,v}.
 \tag{TP13}
\]

At a complete profile compute every auxiliary row value from its class counts, and reject any failed upper or cover. A passing profile prescribes an exact count for each nonzero class and for the single zero group.

Impose the corresponding group caps with a partition-count polymatroid. Explicitly, if the disjoint groups are \(G_g\) with cap \(h_g\), its rank on a subset \(Y\) is \(\sum_{g:Y\cap G_g\ne\varnothing}h_g\). Intersect its independent polytope with \(P(F^{\uparrow})\) and require total \(R\). The intersection is integral. Since the caps sum to \(R\), every cap is tight on this face. An absent group with positive prescribed count makes the face empty, including an absent zero group with positive \(h_0\).

Exact signed scalar optimization on this integral full-total face either returns an integer realization or proves it empty. This is the same resource-plus-partition intersection primitive used in the preceding exact numeric-profile notes. No third resource matroid is introduced. Taking the best scalar value over all profiles is exact, because the completeness and soundness arguments preserve every original feasible scalar value. If every face fails, the original instance is infeasible.

For the all-input bound, traverse only the polynomially many actual classes. A next multiplicity is bounded by the remaining mass divided by that class's positive magnitude and by the remaining count to \(R\). Every partial state extends by zero multiplicities on the remaining classes to a full profile satisfying the mass/count caps. At any fixed depth, distinct partial states have distinct such completions. Hence all tree nodes, failed row filters, and empty integral faces cost at most a polynomial factor times TP12, even on infeasible inputs. No promise of a successful branch is used.

All multiplicities, masses, ranks and running scalar data are stored in binary. The lifted ground has at most four times the prepared number of coordinates; retained rows are sublists of the input; and a DFS state has one count per actual class. The algorithm does not materialize \(B\), \(q\), \(W\) or \(R\) many objects merely because these numbers are large. It stores one current profile and one intersection subproblem. This proves uniform polynomial binary workspace and TP1.

## 8. Reversing the second order gives a sharper exponent

Suppose \(\prec_2\) is the reverse of \(\prec_1\). The quotas are then arbitrary mixed prefixes and suffixes on one common line.

The optional disposal coordinate is a zero column in every row, so its placement after both original orders does not affect this support count. Restricting the original orders to the eligible positive-weight coordinates preserves their reversal.

For a fixed bit pair \((a_1,a_2)\), its support can change only at endpoints of upper rows in either order and of cover rows whose bit is active. Along the first order, each individual prefix or suffix indicator changes at most once. Thus the number of its distinct nonempty colors is at most

\[
                 u_1+u_2+a_1\ell_1+a_2\ell_2+1.
 \tag{TP14}
\]

The extra one allows nonempty colors at both ends of the line. Summing the four catalogues, even before merging duplicates, gives

\[
 q\le4(u_1+u_2)+2(\ell_1+\ell_2)+4
                       \le12B+4.
 \tag{TP15}
\]

The mass proof and recovery are unchanged. In particular TP12 now gives

\[
       2^W\binom{q+W}{W}
          \le2^{q+2W}\le2^{20B}.
 \tag{TP16}
\]

Therefore mixed common-weight prefix/suffix quotas have an exact \(2^{O(B)}\operatorname{poly}(H)\) algorithm in uniform polynomial space. The leading constant in TP16 is only a convenient bound.

The one-order block lower bound in `exact_weighted_prefix_quotas_max_target.md` applies to this subclass: take consecutive blocks of weights \(1,2,3,4\), cumulative equality targets \(5,10,\ldots,5d\), and a rank-\(2d\) paving resource hiding one of the \(2^d\) choices \(\{1,4\}\) or \(\{2,3\}\) in each block. One can leave the second-order list empty or add its redundant whole-ground equality. Thus \(2^{\Omega(B)}\) oracle necessity, and the separately encoded ETH exclusion, persist in the reversed-order subclass. The primary construction and its complete verification are in that companion note.

## 9. Matching oracle lower bound for two unrestricted orders

For any integer \(B\ge2\), take the edge ground of \(K_{B,B}\), identified with pairs \((i,j)\in[B]\times[B]\). Give every coordinate common weight one. Order one lists edges by left endpoint, and order two by right endpoint, with any fixed order inside a block. At the end of block \(k\) in each order, require cumulative weight exactly \(k\), for \(k=1,\ldots,B\).

Subtracting consecutive equalities forces exactly one selected edge in each left block and each right block. Thus the feasible subsets of the prefix equalities are precisely the perfect matchings, or permutations. The largest target is \(B\), although the target sum is \(B(B+1)\). The last equality forces cardinality \(B\), so the statement covers optional independent sets as well as bases.

Let \(\mathcal H\) be these \(B!\) perfect matchings. Distinct members are not single-element-exchange neighbors. Define a reference rank-\(B\) matroid permitting every set of size below \(B\), and every \(B\)-subset outside \(\mathcal H\) as a base. For a hidden \(A\in\mathcal H\), additionally permit \(A\).

These are valid matroids: in the only nontrivial augmentation case, the candidate additions to an independent \((B-1)\)-set yield adjacent \(B\)-sets, so at most one is forbidden. If there is only one candidate, it is the known larger independent set. The rank is truly \(B\), because the \(B\) edges incident with one left vertex form a nonmatching reference base.

The reference and hidden rank oracles differ only on \(A\). Smaller sets have their cardinality as rank. Every larger set contains two adjacent \(B\)-subsets and therefore a reference base. The reference prefix instance is infeasible, while the hidden instance has exactly \(A\) as a feasible solution.

Under the balanced reference/uniform-hidden distribution, an algorithm making at most \(D\) rank queries has success probability at most \(1/2+D/(2B!)\). This follows by following its reference transcript: at most \(D\) candidates can be queried, and all other hidden inputs give that same transcript. Averaging over the algorithm's random coins preserves the bound. Hence success at least \(2/3\) on every instance requires

\[
                         D\ge B!/3
                           =2^{\Omega(B\log B)}.
 \tag{TP17}
\]

All non-oracle data are polynomial in \(B\): the ground has \(B^2\) elements and there are \(2B\) prefix equalities. All scalar coefficients may be zero. The lower bound is for the rank-oracle model and already allows bounded-error randomized decision. It matches the upper exponent order, without asserting an optimal exponential leading constant.

## 10. A readable encoded-rank ETH reduction

For completeness, the same prefix family has an encoded computational lower bound with a polynomial-size rank program or Boolean rank circuit. The algorithm is permitted to inspect the entire representation. This is a conditional result, distinct from TP17.

Given a 3-CNF formula \(\phi\) on \(\nu\ge1\) variables, choose the least integer \(B\ge2\) such that

\[
                              B!\ge2^{\nu}.
 \tag{TP18}
\]

Successive integer multiplication finds it in polynomial time. Since \((\nu+1)!\ge2^\nu\), one has \(B\le\nu+1\). Minimality gives

\[
           \nu\le\log_2 B!
               <\nu+\log_2 B\le2\nu.
 \tag{TP19}
\]

The elementary product bounds \(\log_2 B!=\Theta(B\log(B+1))\), uniform for \(B\ge2\), consequently imply

\[
                       B\log(B+1)=\Theta(\nu).
 \tag{TP20}
\]

Thus the ground, rows, orders and stored factorials are polynomial in the formula size, and all factorial arithmetic uses \(O(\nu)\) bits. No permutation enumeration is part of the reduction.

Recognize a perfect matching by checking that each left and right vertex has degree one, and write its permutation as \(\sigma(1),\ldots,\sigma(B)\). Let \(d_i\) be the number of unused right labels smaller than \(\sigma(i)\). Its zero-based lexicographic rank is

\[
                         J=\sum_{i=1}^B d_i(B-i)!.
 \tag{TP21}
\]

This is a bijection to \(\{0,\ldots,B!-1\}\): each choice of the next unused label leaves \((B-i)!\) completions, proving the positional formula inductively. Ranking and inverse ranking use polynomially many operations on the bounded-length integers.

Call a matching accepted when \(J<2^\nu\) and the \(\nu\) binary digits of \(J\) satisfy \(\phi\). Permit all smaller sets, all nonmatching \(B\)-subsets, and exactly the accepted matchings at rank \(B\). Any forbidden subfamily of \(\mathcal H\) remains nonadjacent, so this defines a valid matroid for every formula, with no uniqueness promise.

Its exact rank decoder has four cases: below \(B\), return cardinality; above \(B\), return \(B\); at \(B\) on a nonmatching, return \(B\); on a matching, compute TP21, evaluate its acceptance predicate, and return \(B\) or \(B-1\). The above-rank branch is valid for the same adjacent-subset reason as in Section 9. Every branch is polynomial-time. Its bounded loops and arithmetic can be uniformly unrolled to a polynomial-size Boolean circuit for the rank on the subset indicator.

Every Boolean assignment appears among the first \(2^\nu\) permutations. Thus the two-order prefix instance is feasible exactly when \(\phi\) is satisfiable. By TP20, a deterministic

\[
                  2^{o(B\log(B+2))}\operatorname{poly}(H)
 \tag{TP22}
\]

exact algorithm in this readable encoded-rank model would give a deterministic \(2^{o(\nu)}\operatorname{poly}(|\phi|)\) algorithm for 3-SAT, contradicting deterministic ETH. A randomized statement requires randomized ETH separately. This is not a corresponding hardness claim for matrix, graphic, laminar, or other restricted explicit resource representations.

## 11. Primary comparison and boundaries

Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*, arXiv:2412.02217v2, Section 1.3 and Lemmas 3.5, 3.9–3.11, explicitly use one paving matroid with partition matroids for coordinate-block counts. Two such partition families already describe bipartite perfect matchings. The lower construction here is an all-one-margin specialization and cumulative-prefix encoding of that established framework. Their Theorem 1.3 also gives rank-parameter oracle lower bounds. No first lower-bound framework or new general three-matroid-intersection hardness is claimed.

<https://arxiv.org/html/2412.02217v2>

Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2, Introduction, records the earlier method of guessing counts of coefficient-vector classes and recovering them through a partition matroid. The resource-plus-partition profile method itself is therefore not claimed as new. The new analysis here bounds the total nonzero common-weight mass under two independently marked prefix systems, while preserving arbitrary signed scalar values and binary resource totals.

<https://arxiv.org/html/2404.03747v2>

The one-order prerequisite and independent prefix/suffix endpoint lower are given in `exact_weighted_prefix_quotas_max_target.md`. The present proof includes the two-order mass and color arguments in full and does not alter that note or any frozen earlier checkpoint.

The upper theorem relies on two orders and a common nonnegative integer weight vector. Row-dependent weights, signed numeric row coefficients, an additional unrelated resource rank, or arbitrary row sets are outside TP1. On a supplied common rational grid, scaling gives the same theorem in the largest normalized integer target. This is a numeric-parameter bound, not a bound polynomial in \(\log B\), and it does not imply a polynomial-time exact or discrepancy result for arbitrary targets.
