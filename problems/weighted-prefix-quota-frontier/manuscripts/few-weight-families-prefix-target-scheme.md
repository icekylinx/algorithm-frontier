# Exact prefix quotas with a bounded number of weight families

**25 October 2026. Complete theorem and proof; full internal mathematical reviews completed for checkpoint T.**

One common coordinate order can support several different weight vectors without losing fixed-parameter tractability in the largest target. Let p be the number of supplied nonnegative integer weight vectors used by the prefix rows, and let B be the largest integer target. Exact mixed upper, equality and covering quotas on one global integral polymatroid admit

$$
\boxed{2^{O(pB\log(p+2))}\mathrm{poly}(H)}
 \tag{FW1}
$$

time and uniform polynomial binary workspace. The scalar objective is an arbitrary signed rational functional optimized exactly. Zero entries in the weight vectors are allowed, and the exponent in FW1 does not pay a separate factor for their support patterns.

The result covers optional independent vectors and original-total bases. It keeps all mandatory resource mass, shares capacity between copied coordinates, and preserves every feasible original scalar value. The resource rank may be binary-large, and the initial explicit row list need not have size bounded by p or B.

Two sharp endpoint obstructions are proved here: p=1 can require $2^{\Omega(B)}$ rank queries, while B=1 can require $2^{\Omega(p\log p)}$ queries. Corresponding readable rank-program/circuit ETH exclusions hold at those endpoints. The companion [few-weight-prefix-joint-lower-bounds.md](few-weight-prefix-joint-lower-bounds.md) additionally proves the joint order $2^{\Theta(pB\log(p+2))}$ on the full even-p grid and in worst-case parameter-budget envelopes. The upper proof below is unchanged by that addendum.

## 1. Input model and theorem

Let F be a normalized monotone integral polymatroid rank on an explicit ordered ground E. Original integer vectors lie in P(F) or in the original base B(F), whose required total is R=F(E). Resource counts, capacities and rank values are binary encoded. Eligibility masks are permitted.

There are p explicitly supplied weight vectors

$$
w^1,\ldots,w^p\in\mathbb Z_{\ge0}^{E}.
 \tag{FW2}
$$

Every quota row chooses a family i, an endpoint t in the same coordinate order, a relation rho in {<=,=,>=}, and an integer target b>=0. Its expression is

$$
\sum_{e\le t}w^i_e x_e\ \rho\ b.
 \tag{FW3}
$$

Put B=max b, with B=0 for no rows. Duplicate weight vectors can be identified and unused families removed in polynomial time; the theorem also holds using any larger supplied family count p. If each row originally lists its own vector, equality of those lists can be checked to obtain the family table.

An arbitrary rational scalar c^T x, including signed coefficients, is minimized or maximized exactly with infeasibility reporting. A threshold on this same scalar can be decided by its appropriate extremum. An additional different unbounded scalar constraint is not included.

H denotes the complete binary input encoding, including the weight-family table, row list, scalar coefficients and rank-value bit bounds. Polynomially implemented rank, submodular minimization and exact integral-polymatroid intersection operations are charged. The running-time constant in FW1 is uniform in p and B; these need not be fixed constants. The workspace is polynomial in H, not in the numeric quantities B or R.

At B=0, or when no row survives preparation, ordinary scalar optimization after the necessary masks is polynomial. Below assume B>=1, at least one retained row, and p>=1.

## 2. Compress the rows separately within each family

Split equalities into upper and covering halves. At a duplicate endpoint within one family retain the smallest upper target and largest cover target. Empty-prefix tests are immediate. Each family's cumulative weight is nondecreasing in the coordinate order.

Thus, within that family, a later upper prefix with no larger target dominates an earlier upper row, and an earlier cover prefix with no smaller target dominates a later cover row. Keep upper suffix-record minima and cover prefix-record maxima. Remove automatic zero covers. A zero upper target masks every positive coefficient in that prefix and becomes automatic.

Also mask a coordinate e if, in any family i, it has w^i_e>B and belongs to an original upper or equality prefix of that family. A positive integer use would violate that row. Stronger masks w^i_e>b for a particular upper target b are also safe but unnecessary. Do not mask a coordinate merely for having a large coefficient in a covering row. Masks are global resource exclusions, so all families use the same eligible ground.

For optional vectors add one disposal coordinate, of zero coefficient in every weight vector and in the scalar, after the original order and outside every original prefix. Its rank is F(S) when disposal is absent and R when it is present. Completion by R-x(E) gives the exact optional-to-base correspondence. Original mandatory bases receive no disposal. Retain the same required total R after all masks and reject prepared rank loss. Write F0 for the prepared rank. Keep coordinates with zero coefficients in all quota rows; their signed scalar values and original resource mass may matter.

Recheck empty-prefix tests after restriction if necessary. In each family the remaining positive targets increase strictly along the endpoints of each direction. Let u_i and ell_i be its upper and cover counts. If d is the total retained row count, then

$$
u_i\le B,\qquad \ell_i\le B,
 \qquad d=\sum_{i=1}^p(u_i+\ell_i)\le2pB.
 \tag{FW4}
$$

The record lists are sublists of the explicitly given rows. Their computation never allocates an array indexed through B. No dominance rule is applied between different weight families.

Set v^i_e=min{w^i_e,B}. On eligible coordinates in an upper prefix of family i, v^i_e=w^i_e. On integer vectors this capping preserves every cover predicate of that family with target at most B: a used unit of original weight at least B already reaches that target after capping, and otherwise all contributions are unchanged. Fractional equivalence is not asserted.

## 3. One first-reaching cut per covering family

Let C be the set of families having a retained positive cover, and s=|C|<=p. For i in C let C_i be its largest cover target, with 1<=C_i<=B.

Fix any feasible original integer base, including legitimate disposal completion when appropriate. Conceptually order its individual units first by coordinate and then by an arbitrary fixed order of the units of that coordinate. Use this same complete unit list for every family, including units of weight zero in some or all families.

For each i in C mark the whole initial unit segment through the first crossing of capped weight C_i. Let its final unit position be tau_i. This crossing exists because the prefix row with target C_i remains satisfied after integer capping. Its capped marked mass satisfies

$$
C_i\le M_i\le C_i+B-1.
 \tag{FW5}
$$

Every retained cover of family i is satisfied by the marked credit. A prefix containing the cut receives all marked mass, at least C_i. A prefix ending before the cut has all its capped contributions marked. A cut inside the units of its last coordinate belongs to the first case. Marking zero-contribution units changes no credited value.

The marks are nested prefixes of one common unit list, even though their weight vectors differ. This common order is the reason exponentially many independent subset labels can be avoided.

## 4. Stream s! chains with only s+1 shared copies

Enumerate permutations sigma=(sigma_1,...,sigma_s) of the covering families. For a fixed permutation define

$$
A_l=C\setminus\{\sigma_1,\ldots,\sigma_l\},
                    \qquad 0\le l\le s.
 \tag{FW6}
$$

Create copies (e,l) of each eligible coordinate, with the shared resource rank

$$
F^{\uparrow}(Y)=F0(\mathrm{pr}(Y)),
 \tag{FW7}
$$

where pr forgets the layer. This is a normalized monotone integral polymatroid rank. Projection preserves unions and maps intersections into intersections; submodularity and monotonicity prove the rank inequality. Aggregating x_e=sum_l z_(e,l) gives exact equivalence of independent resource regions and total-R bases. Querying the full preimage of a subset proves one direction; z(Y)<=x(pr(Y)) proves the other.

Every copy keeps the original scalar c_e. An upper row keeps its true coefficient on every copy in its prefix. A cover of family i gives coefficient v^i_e to copies in its prefix whose layer has i in A_l, and zero otherwise. Upper values and scalar values therefore agree under aggregation, while credited covers are at most true covers. Every feasible integer lifted output is sound for the original problem.

For completeness, choose sigma sorting the stopping positions tau_i nondecreasingly. A unit at position t is marked precisely by the families with tau_i>=t. These form the suffix A_l after exactly the families with tau_i<t have been removed. Assign the unit to that layer. Tied stopping positions simply create empty intermediate layers: the common crossing unit is marked in every tied family, and all those families disappear before the next unit.

Thus every original feasible vector has an exact lifted representative in some enumerated chain, with the same resource projection and scalar. This proof uses a conceptual unit sequence only. No list of length R is generated. Recovered outputs need not themselves respect a chronological cut order, since credited feasibility already proves soundness.

The copied ground has (s+1)|E0| coordinates, at most (p+1)|E0|. All capacities remain shared. The s! permutations are streamed, not stored together.

## 5. At most 2B-1 reduced mass per family

Consider the canonical representative of an original feasible vector. For family i, call a unit relevant when its auxiliary column has a nonzero entry in at least one retained row of that family. Count its capped weight v^i_e once, irrespective of how many rows it enters.

Let P_U be the last upper prefix of that family, if present. Its true weighted mass is at most B and it contains every coordinate visible to any retained upper row.

If the marked cut is inside P_U, every marked positive unit and every passive relevant unit lies in P_U, so the total relevant capped mass is at most B. If the cut is after P_U, every positive unit of P_U is marked; relevant mass is then contained in the marked units and is at most C_i+B-1. With no upper rows only marked mass matters. With no covers only upper-visible mass matters and it is at most B. A family with no rows contributes zero.

In every case the relevant reduced mass for one family is at most 2B-1. Summing over the families gives the global allowance

$$
W=p(2B-1).
 \tag{FW8}
$$

This is a sum of one magnitude per contributing family and unit, not the entry sum over all retained prefix rows. Replication of a coefficient in many rows of the same family is counted only once. This distinction is what keeps the bound linear in B rather than in the sum of prefix targets.

## 6. Endpoint base colors, with zeros retained inside the vectors

Fix one chain. Let t_1<...<t_m be the distinct endpoints of its retained rows, so m<=d. Divide the coordinate order through t_m into the segments (t_(j-1),t_j], with t_0=0. Row membership is constant within each segment. Coordinates after t_m have zero auxiliary columns. Empty segments after masking can be discarded.

Define a base color g=(l,j) by a chain layer and an endpoint segment. There are at most

$$
D\le(s+1)m\le(p+1)d\le2p(p+1)B
 \tag{FW9}
$$

such colors. This bound has no extra trailing segment: all row templates are empty after the last endpoint, and those coordinates belong to the global zero group below.

For each base color g and family i, let T_i(g) be the template of its retained rows that include this segment and either are upper rows or are covers with i active in the layer. The template depends only on g. For a copied coordinate (e,l) of color g, define its collapsed vector y in nonnegative integer p-space by

$$
y_i=\begin{cases}
       v^i_e,&T_i(g)\ne\varnothing,\\
       0,&T_i(g)=\varnothing.
      \end{cases}
 \tag{FW10}
$$

An actual zero weight remains a zero entry even when the corresponding template is nonempty. Given (g,y), every auxiliary row coefficient is reconstructed exactly: a row j in family i receives y_i if j belongs to T_i(g), and zero otherwise.

A copied coordinate has y=0 exactly when its full auxiliary column is zero. Merge all such coordinates into one global zero-vector group, regardless of their base colors, positions, scalar values or chain layers. This is a grouping for a total-count cap, not an identification of their resource coordinates or scalar costs. Their identities and costs remain in the intersection subproblem.

Every other coordinate belongs to an actual class (g,y) with y nonzero. The number of stored classes is at most the number of copied coordinates. The algorithm does not generate all p-dimensional vectors or all subsets of zero entries.

For the canonical representative, the relevant mass in Section 5 is precisely the sum of entries of these collapsed vectors. Thus its nonzero class profile h satisfies

$$
\sum_{g,y\ne0}\|y\|_1 h_{g,y}\le W.
 \tag{FW11}
$$

Completeness is retained by this refinement of the profile classes: every actual lifted vector has its own such profile. Splitting otherwise identical full columns into different base colors cannot remove that vector from the union of profiles.

## 7. An alphabet-and-cuts bound that includes arbitrary zero entries

Fix one base color and a positive total reduced weight w. A local profile is a multiset of nonzero vectors in $\mathbb Z_{\ge0}^p$ whose total l1 weight is w.

Sort its vector occurrences lexicographically. Encode one occurrence y as a word containing y_1 copies of symbol 1, followed by y_2 copies of symbol 2, and so on. Each occurrence contributes a nonempty word. Concatenate all occurrence words and mark the cut positions between consecutive occurrences.

The concatenation has length w over an alphabet of p symbols. Its cuts form a subset of the w-1 interior positions. From the word and cuts, take the histogram of each nonempty segment to recover the ordered vectors, and therefore the multiset. This proves injectivity even when a vector has arbitrarily many zero entries. Repeated vector occurrences cause no ambiguity.

Consequently the number of local profiles of exact positive weight w is at most

$$
p^w2^{w-1}\le(2p)^w.
 \tag{FW12}
$$

For weight zero only the empty nonzero-vector profile is permitted. Excluding zero vectors is essential; their unbounded multiplicities have already been moved to the one global remainder group. The length-w word is a counting device only; the algorithm never materializes it.

If a complete profile uses k of the D base colors, choose them in binomial(D,k) ways. Their positive total weights summing to at most W have binomial(W,k) choices. Using FW12 and Vandermonde's identity gives

$$
\begin{aligned}
 \#\text{nonzero profiles}
 &\le(2p)^W\sum_k\binom Dk\binom Wk\\
 &=(2p)^W\binom{D+W}{W}.
 \end{aligned}
 \tag{FW13}
$$

Allowing every nonzero p-vector only enlarges the actual class family. The original count cap and final quota filters can only decrease it. There is no enumeration of 2^p zero patterns in either this count or the algorithm.

## 8. Exact integer recovery for one profile

Enumerate multiplicities of actual nonzero classes with FW11 and the resource count bound sum h<=R. Set the one global zero-group count to

$$
h_0=R-\sum_{g,y\ne0}h_{g,y}.
 \tag{FW14}
$$

For a complete profile reconstruct every auxiliary row total by FW10 and test its actual upper or covering inequality. Original equalities are enforced by their two halves. A profile that fails a row is rejected.

A passing profile supplies one count cap for each nonzero class and for the zero group. These disjoint group caps define one partition-count polymatroid. For groups G_a with caps h_a its rank on a set Y is sum of h_a over groups meeting Y. Intersect its independent region with P(Fup) and require total R. The intersection is integral; on that face every cap is tight because their sum is R. An absent group with positive count, including an absent zero group with positive remainder, makes the face empty.

Exact signed scalar optimization on this integral full-total face returns an integer profile realization or proves it empty. Only the shared original resource and this one partition-count rank are used. Original zero-column units are retained with their real scalar coefficients and resource identities.

Every original feasible scalar value appears in some chain and profile by Sections 3–6. Every recovered profile projects to an original feasible vector of the same scalar by Section 4. Taking the best value over all chains and profiles is therefore exact. If none is feasible, the original instance is infeasible.

## 9. Uniform time, failed-input accounting and polynomial space

For each chain traverse only the actual nonzero classes. A next multiplicity is bounded by the remaining mass divided by the positive class mass ||y||_1 and by the remaining count to R. Every partial state extends by zero counts on the remaining classes to a full state satisfying those two caps. At a fixed depth, distinct partial states have distinct such completions. Thus all traversal nodes, failed quota filters and empty integral faces are bounded by a polynomial factor times FW13, including on infeasible inputs.

The complete explicit bound is

$$
s!\,(2p)^W\binom{D+W}{W}\mathrm{poly}(H),
      \quad W=p(2B-1),\quad D\le2p(p+1)B.
 \tag{FW15}
$$

For B>=1, W>=pB, so D/W<=2(p+1). Therefore

$$
(2p)^W\binom{D+W}{W}
       \le\bigl[2ep(2p+3)\bigr]^W,
       \qquad W\le2pB.
 \tag{FW16}
$$

Also s!<=p!<=p^p. Its logarithm is absorbed by O(pB log(p+2)) because B>=1. This proves FW1 with uniform constants. At a zero actual class count there is just one nonzero profile, namely the empty one, followed by the same row and resource tests.

All list lengths are controlled by the explicit input: retained rows are an input sublist, p is an input family count, endpoint segments number at most d, and the copied ground has at most (p+1)|E0| coordinates. Store one permutation, one copied ground, one actual class table, one binary count profile, the running totals, and one intersection subproblem. All numeric counters have polynomial bit length in H. No target-sized array, rank-sized unit list, family-subset catalogue or table of all possible vectors is materialized. Permutations and profiles are streamed depth first. Workspace is polynomial in H uniformly even when p, B and R vary.

## 10. Sharp endpoint at one family

For p=1, FW1 becomes 2^{O(B)} poly(H). The one-order construction in [exact-weighted-prefix-quotas-max-target.md](exact-weighted-prefix-quotas-max-target.md) supplies its sharp oracle endpoint, recalled briefly here.

Take t consecutive four-element blocks of common weights 1,2,3,4, and impose cumulative equalities of weight 5j at the end of block j. The largest target is B=5t. Every feasible subset chooses exactly {1,4} or {2,3} in each block, giving a nonadjacent family of 2^t rank-2t subsets.

A reference paving matroid forbids that family at rank and permits all smaller sets; a hidden version restores one candidate. The rank is truly 2t, the two rank oracles differ only at the candidate, and prefix feasibility is NO for the reference and uniquely YES at the hidden candidate. The balanced reference/hidden distribution gives at least

$$
2^t/3=2^{\Omega(B)}
 \tag{FW17}
$$

queries for bounded-error randomized decision. Equalities force full rank also in the optional formulation. The scalar may be zero.

For a readable encoded endpoint, let the block choices encode the variables of a 3-CNF formula and permit exactly its satisfying choices. Any forbidden subfamily remains nonadjacent, and the complete rank decoder evaluates the one specified assignment in polynomial time. With t equal to the variable count, deterministic ETH excludes 2^{o(B)} poly(H) time on this promised rank-program/circuit representation. The complete construction is in the cited companion note; no graphic or matrix-representation hardness is inferred.

## 11. Sharp endpoint at unit maximum target

Let p>=4 be even. On the edge ground of K_p, take an arbitrary single coordinate order. Give family i the vertex-incidence weight vector

$$
w^i_e=\mathbf1[i\in e],
                         \qquad i\in[p].
 \tag{FW18}
$$

These are p distinct nonnegative vectors with zero entries. For each family impose one equality of target one on the full prefix. Hence B=1. No cardinality row or larger target is added.

The equalities describe precisely the perfect matchings and already force cardinality r=p/2. Let H be the family of all (p-1)!! matchings. Distinct members are not single-element-exchange neighbors: their endpoint sums are equal, while individual edge-incidence vectors are distinct.

Make every subset below r independent and every r-subset outside H a reference base; the hidden matroid additionally permits one A in H. This is a valid rank-r matroid. In the nontrivial augmentation case, two candidate r-sets are adjacent and cannot both be forbidden; a sole candidate is the known larger independent set. Nonmatching r-sets exist for p>=4, so the rank is r. Larger query sets contain two adjacent r-subsets and therefore a reference base. The rank oracles differ only on A.

The reference unit-target instance is infeasible and each hidden instance has its unique hidden feasible matching. The same balanced-distribution argument gives the unconditional lower bound

$$
(p-1)!!/3=2^{\Omega(p\log p)}
 \tag{FW19}
$$

on worst-case rank queries for bounded-error randomized exact feasibility. It holds for optional independent sets and bases with scalar zero and polynomial-size explicit non-oracle data. Thus FW1's p log p endpoint at B=1 is necessary.

There is also a readable rank-program/circuit ETH endpoint, as established in [conditional-lower-bound-encoded-target-matroids.md](../../numeric-target-frontier/manuscripts/conditional-lower-bound-encoded-target-matroids.md). To make its calibration explicit, for a formula on nu>=1 variables choose the least even p>=4 with (p-1)!!>=2^nu. Minimality and the recursion L_p=(p-1)L_(p-2) give log L_p<nu+log(p-1), while elementary product estimates give log L_p=Theta(p log(p+2)). Since p<=2nu+2, the counts have O(nu) bits and

$$
p\log(p+2)=\Theta(\nu).
 \tag{FW20}
$$

Rank a perfect matching by choosing the partner of the smallest remaining vertex in increasing order: the choice at a residual set of m vertices has (m-3)!! completions. This recursion ranks all matchings in polynomial time. Its rank modulo 2^nu supplies a surjection onto assignments. Permit a matching exactly when that assignment satisfies the formula, retaining all nonmatchings at rank and all smaller sets. Every forbidden subfamily is still nonadjacent, so the matroid promise holds for every formula. The exact rank decoder treats smaller, larger, nonmatching rank-sized, and matching rank-sized sets separately; only the last case evaluates the formula. All operations have polynomial bit complexity and can be unrolled into a polynomial-size Boolean rank circuit.

Consequently deterministic ETH excludes 2^{o(p log(p+2))} poly(H) exact time at B=1 in this readable encoded-rank model. Randomized exclusion requires randomized ETH separately. These are the same complete-graph matching and encoded-predicate constructions from the earlier total-target notes, now viewed as full-prefix weight families.

## 12. Scope, comparison and the joint lower companion

The two constructions in this manuscript prove separate endpoint necessities. The companion [few-weight-prefix-joint-lower-bounds.md](few-weight-prefix-joint-lower-bounds.md) supplies the additional joint construction: for every even p>=4 and every B>=1 it has ((p-1)!!)^B hidden candidates. It also proves a matching worst-case upper-budget classification and carefully calibrated readable-program ETH families. Read that companion for the joint lower theorem; neither file asserts encoded ETH hardness at every independently prescribed exact parameter pair.

The requirement of a bounded number of weight families is substantive. [row-dependent-full-prefix-target-boundary.md](row-dependent-full-prefix-target-boundary.md) reduces k-SetCover to a rank-k uniform resource with full-prefix coefficients 1+1[u in S] and target k+1. It is W[2]-hard in B alone when the number of row weight vectors is unbounded, even though every coefficient is one or two and every column has the same full positive support. Thus FW1 is a positive repair using the additional parameter p; it does not contradict that obstruction.

The primary source for that SetCover complexity statement is Lin, Ren, Sun and Wang, *Constant Approximating Parameterized k-SetCover is W[2]-hard*, arXiv:2202.04377v2, Introduction and Theorem 1:

<https://arxiv.org/html/2202.04377v2>

Count-profile recovery with a partition matroid has earlier primary antecedents explicitly recorded in Eisenbrand, Rohwedder and Węgrzycki, *Sensitivity, Proximity and FPT Algorithms for Exact Matroid Problems*, arXiv:2404.03747v2, Introduction:

<https://arxiv.org/html/2404.03747v2>

The use of selected acceptable families in paving-type matroids is also established in Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute Force for 3-Matroid Intersection*, arXiv:2412.02217v2, Section 3:

<https://arxiv.org/html/2412.02217v2>

The common-unit-order chain compression is the previously reviewed [mixed-target-cover-chain-compression.md](../../numeric-target-frontier/manuscripts/mixed-target-cover-chain-compression.md); the present chain is over covering families rather than over all cover rows. The new parameter analysis combines one cut per family, endpoint base colors, and the alphabet-and-cuts count for vectors with arbitrary zero entries. No priority claim is made for the earlier profile, chain or paving constructions.

All families must use one common coordinate order. Different orders per family, signed numeric row weights, another unrelated resource rank, or a second unrelated scalar side condition require additional arguments. On a supplied common rational grid, scaling gives the same theorem in the largest normalized integer target. The algorithm preserves zero weights and signed scalar costs, but it is not polynomial in log B and makes no fractional-feasibility equivalence assertion for the capping step.
