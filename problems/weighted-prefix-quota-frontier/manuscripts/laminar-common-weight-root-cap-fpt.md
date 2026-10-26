# Exact common-weight laminar quotas under a root cap

**25 October 2026. Complete incremental proof; full internal mathematical reviews completed for checkpoint T. The stronger arbitrary-zero-cost version is in [laminar-valuated-zero-completion-fpt.md](laminar-valuated-zero-completion-fpt.md).**

This note gives a deterministic algorithm parameterized solely by the root weighted cap, with no exponential dependence on the number of laminar nodes. It uses one global integral polymatroid and preserves one rational scalar objective exactly. Strictly positive common weights are covered without a scalar-sign restriction. Zero-weight coordinates are also covered when they have scalar zero in an optional problem, or one common scalar coefficient in a mandatory-base problem. The latter restriction is substantive and is kept explicit.

The proof uses a bounded-depth representative recursion adapted from Huang and Ward's joint-representative method. It proves the needed restricted lemma directly. It does not assert integrality of three matroid or polymatroid constraints.

## 1. Model and theorem

Let $F:2^E\to\mathbb Z_{\ge0}$ be a normalized, monotone, integral submodular rank function on an explicit coordinate ground. The resource is either the integer independent-set polytope $P(F)$, or the integer base polytope with original total

$$
x(E)=R=F(E).
\tag{LM1}
$$

Eligibility restrictions and binary coordinate domains may be prepared using restriction and the standard box-cap rank formula. In the mandatory case, all preparations retain the original $R$; a preparation whose maximum rank falls below $R$ is rejected. Below, $F$ denotes the resulting rank on the allowed ground, so its full rank is still $R$ in every nonrejected mandatory instance.

Let $\mathcal L$ be an explicitly represented laminar family. Each coordinate has one common nonnegative integer weight $w_e$. Every numeric row uses that same weight:

$$
l_A\le\sum_{e\in A}w_ex_e\le u_A,
                       \qquad A\in\mathcal L.
\tag{LM2}
$$

An absent lower bound means zero, an absent upper bound means infinity, and an equality uses equal bounds. All finite bounds are nonnegative integers. There is an explicit root upper bound

$$
\sum_{e\in E}w_ex_e\le B.
\tag{LM3}
$$

The root can additionally have a lower bound, including equality to $B$. Let $c\in\mathbb Q^E$ be the scalar coefficient vector; either minimize or maximize $c\cdot x$ exactly. Thus an exact bound on this one scalar can also be decided by optimizing in its required direction. No additional independent scalar budget is included.

Put $Z=\{e:w_e=0\}$. The theorem assumes one of the following:

* $Z=\varnothing$, with arbitrary signed rational $c$;
* the resource is optional and $c_z=0$ for every $z\in Z$;
* the resource is mandatory and $c_z=\gamma$ for one common rational $\gamma$ and every $z\in Z$. The common value may have either sign.

Let $H$ be the full binary input size, including the explicit laminar family, numbers, and the rank-oracle encoding/bit bounds. Polynomial-time rank evaluation, submodular minimization, and standard integral polymatroid operations are charged.

**Theorem.** Under these assumptions, feasibility and exact scalar optimization can be solved deterministically in

$$
2^{O(B^2\log(B+1))}\mathrm{poly}(H)
\tag{LM4}
$$

time and uniform polynomial binary workspace. Counts and ranks are not expanded in proportion to their binary numerical values when that would violate the space bound. The number of laminar nodes affects the polynomial factor only. The case $B=0$ is polynomial.

## 2. Safe preparation and the two dominance reductions

Zero-weight coordinates contribute nothing to every numeric row. Project the numeric sets onto the surviving positive-weight ground $P=E\setminus Z$, merge identical sets, and retain the strongest lower and upper bounds. Projecting a laminar family preserves laminarity. Empty positive lower rows are infeasible; empty upper rows are automatic.

Every lower target exceeding $B$ is infeasible, and an upper target exceeding $B$ can be clipped to $B$, because of the root. A positive-weight coordinate is ineligible if it is a resource loop or if $w_e>u_A$ for some upper-bounded set $A$ containing it. In particular $w_e>B$ is ineligible. Since counts are integral, even one unit of such a coordinate violates a row. Remove these coordinates, repeat the elementary merging of rows, and check the original total in a mandatory problem. A zero upper bound removes all its positive-weight coordinates. This preparation is polynomial and does not discard any feasible integer vector.

For the upper bounds, discard a set's upper row whenever an ancestor has an upper bound no larger. After this dominance reduction, upper bounds strictly increase up any retained inclusion chain. Every retained nonempty upper has capacity in $\{1,\ldots,B\}$, so the upper forest has depth

$$
D\le B.
\tag{LM5}
$$

The root is retained, with its strongest bound. This does **not** bound the number of upper nodes. For example, arbitrarily many disjoint upper-one blocks may occur below a root of capacity two. The proof below never enumerates one occupancy choice per such block.

For lower bounds, use the inclusion forest of the lower-row sets, with a
dummy root of lower bound zero. At each node $A$, let its children be the
maximal proper lower-row subsets, and compute bottom-up

$$
q_A=\max\left\{l_A,\sum_{C\text{ child of }A}q_C\right\}.
$$

The children are disjoint. Hence every feasible nonnegative mass vector
has mass at least $q_A$ in $A$, by induction. Reject if the dummy-root
value exceeds $B$. A row $A$ is redundant whenever
$l_A\le\sum_Cq_C$, because the children's constraints imply it. Delete
exactly those redundant lower rows; retained descendants still imply the
same $q_A$ by induction, so all original lower constraints are preserved.

Every retained node has a positive integer charge
$q_A-\sum_Cq_C\ge1$; every deleted node has charge zero. Summing these
charges telescopes to the dummy-root value, at most $B$. Consequently

$$
m_-:=\#\{\text{retained lower rows}\}\le B.
\tag{LM6}
$$

There are at most $m_-+1$ distinct lower-row membership patterns of coordinates. Indeed, a nonempty membership pattern is determined by its deepest containing lower set; its other containing lower sets are precisely that set's ancestors. The empty pattern supplies the additional class.

Upper and lower dominance are applied independently, including when they came from an equality. All discarded rows remain consequences of retained rows. Therefore preserving every retained lower row and satisfying every retained upper row suffices for the original instance.

## 3. Natural matroids on bounded positive copies

For the moment suppose positive units are explicitly represented. For each positive coordinate $e$, make

$$
b_e=\min\{F(\{e\}),\lfloor B/w_e\rfloor\}
\tag{LM7}
$$

distinct conceptual copies. Let $U$ be this positive-copy ground and $U_A$ the copies owned by coordinates in $A\subseteq P$. For $S\subseteq U$, write $x_S(e)$ for its number of copies of $e$.

The natural matroid $M$ has rank

$$
r_M(S)=\min_{A\subseteq P}
                     \bigl(F(A)+|S\setminus U_A|\bigr).
\tag{LM8}
$$

Thus $S$ is independent exactly when $x_S\in P(F|_P)$. This is the standard natural-matroid rank of an integral polymatroid with bounded copies. Each query is a submodular minimization over the original coordinate ground, with the selected copy counts as modular coefficients. Copies are distinguishable for replacement arguments, while their resource effects depend only on their owner counts.

Every root-feasible vector contains at most $B$ positive units. Its coordinates satisfy LM7, so it has a representation by a set $S\subseteq U$ of size at most $B$. Conversely, each such independent set represents its integer resource-feasible positive vector. Section 9 implements this interface in polynomial binary space without assuming that numerical $B$ is polynomial in its encoding.

## 4. Exact completion through zero-weight coordinates

In an optional problem with scalar-zero $Z$, simply set those coordinates to zero. Downward closure proves that this preserves every feasible positive vector and its scalar value. No completion matroid is needed.

In a mandatory problem, let

$$
g(A)=F(A\cup Z)-F(Z),\qquad
 r'=R-F(Z),\qquad A\subseteq P.
\tag{LM9}
$$

The function $g$ is the normalized integral contraction rank on $P$, with full rank $r'$. Reject if $r'>B$. Let $Q$ be the natural matroid of $g$ on the same copy ground $U$. Its rank on a represented count vector is

$$
q(S)=\min_{A\subseteq P}
                  \bigl(g(A)+x_S(P\setminus A)\bigr).
\tag{LM10}
$$

**Completion criterion.** If $S$ is independent in $M$, its positive counts can be completed through $Z$ to a base of original total $R$ if and only if

$$
q(S)=r'.
\tag{LM11}
$$

To prove the criterion and obtain a constructive completion, put $x=x_S$ and define on $Z$

$$
h_x(A)=\min_{C\subseteq P}\bigl(F(A\cup C)-x(C)\bigr).
\tag{LM12}
$$

This is a normalized, monotone, integral submodular rank. Normalization follows from $x\in P(F|_P)$ and the empty choice of $C$. Monotonicity is immediate. For submodularity, take minimizers for two sets in $Z$, apply submodularity of $F$ to their unions with the two minimizing positive sets, and use modularity of $x$; their union and intersection give valid minimizing candidates for the corresponding sets in $Z$.

For a zero vector $z\ge0$, the inequalities $z\in P(h_x)$ are exactly the conditions that $x+z\in P(F)$ with the positive coordinates fixed. Its maximum zero total is therefore $h_x(Z)$. Equations LM9–LM10 give

$$
h_x(Z)=F(Z)+q(S)-x(P).
\tag{LM13}
$$

As $q(S)\le g(P)=r'$, a full completion is possible exactly in LM11. When it is possible, an integral greedy base of $h_x$ has total $R-x(P)$ and gives the desired zero coordinates. Each rank query for $h_x$ uses submodular minimization over $P$. This construction uses binary counts and polynomially many rank queries, even when $R$ or $F(Z)$ is large.

If all zero coordinates have common scalar coefficient $\gamma$, every such full completion has scalar

$$
c\cdot(x+z)
                =\gamma R+\sum_{e\in P}(c_e-\gamma)x_e.
\tag{LM14}
$$

Hence exact scalar optimization reduces to the linear positive-copy coefficients $c_e-\gamma$, with one fixed additive constant. This is why an arbitrary sign of $\gamma$ causes no issue, and why nonuniform zero coefficients are not included in this theorem.

## 5. A restricted representative lemma with a total-rank bound

Here is the precise representative fact used below. It is stated with independent tests separately in each matroid, so there is no assumption about the global rank of a matchoid.

**Lemma.** Let $N_1,\ldots,N_\ell$ be matroids on a common finite ground $U$, let $T\subseteq U$ contain no loop of any $N_i$, and give the candidates in $T$ rational scores $a_e$. For an integer $d\ge0$, one can generate a set of at most

$$
K_{\ell,d}=\sum_{j=0}^{d}\ell^j
\tag{LM15}
$$

candidates with the following property. For any independent sets $B_i$ of $N_i$ satisfying $\sum_i|B_i|\le d$, and any $e\in T$ outside every $\mathrm{cl}_{N_i}(B_i)$, an emitted candidate $f$ has $a_f\ge a_e$ and is also outside all those closures. The sets $B_i$ may differ, overlap, or contain elements outside $T$.

Generate the candidates recursively. Maintain independent $J_i$, initially empty, and let

$$
Y(J)=T\setminus\bigcup_{i=1}^{\ell}
                                   \mathrm{cl}_{N_i}(J_i).
\tag{LM16}
$$

If $Y(J)$ is empty, stop this branch. Otherwise emit a highest-score candidate $f\in Y(J)$, using a fixed tie order. If $\sum_i|J_i|<d$, branch on each $i$, inserting $f$ into $J_i$. The inserted set remains independent. The tree has depth at most $d$ and at most LM15 nodes.

For correctness, maintain $J_i\subseteq\mathrm{cl}(B_i)$ and the target $e\in Y(J)$. The emitted score is then at least $a_e$. If $f$ fails a test, choose $i$ with $f\in\mathrm{cl}(B_i)$. Since $f\notin\mathrm{cl}(J_i)$, independence and closure containment imply $|J_i|<|B_i|$. Inserting $f$ in this $J_i$ preserves containment; $e$ remains outside its closure. Thus a legitimate branch continues until a candidate passes all tests. It cannot require depth greater than $\sum_i|B_i|\le d$. This proves the lemma.

One may obtain the same restricted tests from private copies in the joint-representative formulation of Huang–Ward. The direct proof above makes the smaller **sum of test ranks** bound explicit; it does not substitute $d$ for a public theorem's rank parameter without proof. Matroid closures are evaluated only on the generated candidate sets.

## 6. Candidate classes and auxiliary partitions

For each positive copy, record its weight, its membership pattern in the retained lower family, and, in the mandatory case, whether it is a loop of $Q$. Form candidate classes with identical records. There are at most

$$
G\le2B(B+1)
\tag{LM17}
$$

classes; the factor two can be omitted if there is no completion matroid. Every class has one fixed positive weight $w$. Use the scalar coefficient itself as the score for maximization and its negative for minimization, after the adjustment in LM14 when required.

At each depth $j\in\{1,\ldots,D\}$ of the retained upper forest, its nodes are mutually disjoint. Define a rank-one partition matroid $P_j$ whose classes are the copy sets of those nodes and one additional class for everything outside them. These partitions are auxiliary tests; the original selected set need not be independent in them.

For a candidate class, apply the lemma to $M,P_1,\ldots,P_D$, and also to $Q$ if the class consists of $Q$-nonloops. Omit $Q$ for a $Q$-loop class. Thus

$$
\ell\le B+2.
\tag{LM18}
$$

Each candidate is nonloop in every included matroid. Use depth $d=3B-3$ for $B\ge1$. If no completion matroid is required, $d=2B-2$ suffices, but the uniform bound is convenient.

## 7. The replacement proof

Let $S\subseteq U$ be any feasible positive-copy set, with $|S|\le B$, and take a copy $e\in S$. Write $S^-=S\setminus\{e\}$, and let its class have weight $w$.

### Resource test

Use $B_M=S^-$ in the natural resource matroid. This is independent, has size at most $B-1$, and $e$ lies outside its closure.

### Upper-quota tests

Call a retained upper node $A$ relevantly blocking if

$$
u_A\ge w,
          \qquad \sum_{f\in S^-\cap U_A}w_f+w>u_A.
\tag{LM19}
$$

Nodes with $u_A<w$ contain no candidate of the present class by the individual-eligibility preparation, so they require no blocker. Each relevantly blocking node contains at least one copy of $S^-$: its current weight is strictly larger than $u_A-w\ge0$. No blocking node contains $e$, since reinserting $e$ recovers the feasible set $S$.

Take the inclusion-maximal relevantly blocking nodes. They are disjoint, number at most $|S^-|\le B-1$, and contain every relevantly blocking node. For each such maximal node, choose one copy of $S^-$ inside it. At depth $j$, put the chosen copies for nodes of that depth into the test set $B_j$ of $P_j$. This is independent because its node classes are distinct. The candidate $e$ is outside every such tested partition class, and

$$
\sum_j|B_j|\le B-1.
\tag{LM20}
$$

A replacement outside these closures cannot enter any newly overloaded upper node. Nodes containing the removed copy have lost weight $w$, and inserting the same weight into such a node cannot exceed its old feasible load. Equivalently, any violated node after a replacement would be a relevantly blocking node containing the replacement, which the tests exclude.

### Completion test

If there is no completion requirement, skip this test. Otherwise $q(S)=r'$. If $e$ is a $Q$-loop, its deletion leaves full span, and every candidate in its class is also a loop; no completion test is needed.

For a nonloop class, if $q(S^-)=r'$, take the empty $Q$-test. The target $e$ passes it because it is a nonloop, and any replacement retains the already full span. If $q(S^-)<r'$, single-element rank change gives $q(S^-)=r'-1$. Choose a $Q$-basis $B_Q\subseteq S^-$; then $|B_Q|=r'-1\le B-1$, and $e$ is outside its closure. A passing replacement restores rank $r'$.

The sum of all test ranks is at most

$$
|S^-|+(B-1)+(B-1)\le3B-3.
\tag{LM21}
$$

The lemma therefore supplies an emitted replacement $f$ of no worse scalar score. It preserves natural resource independence. It cannot already belong to $S^-$, since the resource test would then reject it. It preserves every lower-row total exactly, because its weight and lower membership agree with those of $e$. It satisfies all uppers by LM19–LM20 and preserves full completion by the $Q$-test. Its cardinality is unchanged.

Consequently any feasible solution can be converted into one supported on the union of emitted candidates without worsening the scalar: repeatedly replace a selected candidate outside that union. Each step increases the number of selected copies in the union. In the mandatory case, LM14 ensures that this comparison is the true full scalar comparison, including all zero units.

## 8. Exact optimization from the representatives

The total number of emitted positions, including any duplicates, is at most

$$
K\le2B(B+1)\sum_{j=0}^{3B-3}(B+2)^j
                  =2^{O(B\log(B+1))}.
\tag{LM22}
$$

Enumerate sets of at most $B$ emitted copies, reject repetitions of a copy, test all numeric rows and natural resource independence, and in a mandatory instance test LM11. Keep the exact best scalar value. Empty sets are included. The replacement proof shows that the best surviving value is the original optimum. If no candidate survives, the original problem is infeasible.

Enumeration may use ordered index tuples padded by a blank symbol. There are at most $(K+1)^B$ such tuples. Duplicate enumeration is harmless and gives

$$
(K+1)^B\mathrm{poly}(H+B)
                    =2^{O(B^2\log(B+1))}\mathrm{poly}(H).
\tag{LM23}
$$

Only one exact scalar is optimized. A separate unrelated scalar restriction would not be preserved by selecting a highest-score replacement and is not claimed.

## 9. Uniform polynomial binary space

Let $n=|P|$ be the number of surviving positive coordinates. Handle $B=0$ or $n=0$ directly: all positive counts are zero; positive lower rows are impossible; an optional scalar-zero instance has value zero; a mandatory instance is feasible precisely when the zero ground has original rank $R$, and then has value $\gamma R$.

For $B\ge n\ge1$, use a simpler streaming fallback. Enumerate

$$
0\le x_e\le\lfloor B/w_e\rfloor
                              \quad(e\in P).
\tag{LM24}
$$

Test the root and all rows, test $x\in P(F|_P)$ by submodular minimization, and test LM10–LM11 when necessary. There are at most

$$
(B+1)^n\le(B+1)^B
\tag{LM25}
$$

vectors. Store only $n$ binary counters, the current best vector, and polynomial-space oracle work. Thus this branch is faster than LM4 and never expands numerical capacities. Obtain the final zero completion using LM12.

For $1\le B<n$, the copy ground has size at most $nB<n^2$, and the recursion depth $3B-3$ is polynomial in explicit input length. The exponentially many representatives still need not be stored. An emitted position is specified by a candidate-class index and a branching word of length at most $3B-3$ over at most $B+2$ auxiliary matroids. Reconstruct its candidate by replaying that path, selecting the fixed highest-score element in LM16 at each step. If a prefix has no candidate, the position is invalid. This representation includes every actual emitted candidate.

Store at most $B$ such indices for the outer enumeration, reject invalid positions or repeated copies, and regenerate their actual candidates as needed. Each index has $O(B\log(B+1)+\log(H+1))$ bits. Each replay stores only the current independent sets $J_i$, whose total size is at most $3B-3$, and scans the polynomial-size copy ground. The index bound LM22 includes all possible branching words, so invalid paths and failed tuples are also charged. No accepted-solution list or exponential kernel is retained.

The rank queries in LM8, LM10 and LM12 use binary modular counts on the original ground. Rational score comparisons and objective sums have polynomial bit length. The final zero completion is an explicit binary vector on $Z$, constructed with polynomially many greedy rank queries. This proves uniform polynomial binary space for both branches.

## 10. Boundaries and an exponential lower example

### Nonuniform zero costs are not covered

The zero restriction cannot simply be dropped from the proof. Consider a rank-two partition matroid with parallel pairs $\{p_1,z_1\}$ and $\{p_2,z_2\}$. Give $p_1,p_2$ common numeric weight one and $z_1,z_2$ weight zero. Require one positive unit by a root equality, so $B=1$, and require an original resource base. Let $c_{p_1}=c_{p_2}=c_{z_1}=0$ and $c_{z_2}=100$, and minimize cost.

The positive choices have identical positive scalar scores and identical numeric membership. However, completing $p_1$ costs 100, whereas completing $p_2$ costs zero. A positive-only representative chosen by an arbitrary tie order need not preserve the optimum. This is a counterexample to removing the uniform-zero-cost hypothesis from the present argument, not an impossibility theorem for that broader model.

### A genuine exponential root-cap dependence can be necessary

The reviewed disjoint-row hidden-family construction in [column-support-numeric-target-dichotomy.md](../../numeric-target-frontier/manuscripts/column-support-numeric-target-dichotomy.md) gives a lower example already at laminar depth two. Take $d$ disjoint blocks, each with four elements of common coordinate weights $1,2,3,4$, and impose weighted equality five on each block. Add root cap $B=5d$. Use one rank-$2d$ hidden matroid whose potentially restored feasible sets choose in every block either the pair $\{1,4\}$ or $\{2,3\}$.

Each equality needs at least two elements, so resource rank forces exactly one of these two pairs in every block. The $2^d$ candidate sets are pairwise nonadjacent under one exchange and support the usual reference/one-restored-base rank-oracle family. Scalar zero suffices, and both optional and mandatory formulations work. The decision-distribution argument requires $2^{\Omega(B)}$ rank queries. This does not match the upper exponent in LM4; no optimal $B^2\log B$ dependence is asserted.

The theorem also genuinely uses common weights across rows. Arbitrary row-specific coefficients, even on the same apparent prefix or set, are a different model. Finally, the single global resource may have arbitrary cross-coordinate dependence, but no second independently supplied global resource rank is added by the result.

## 11. Primary-source comparison

Huang and Ward's *FPT-Algorithms for the $\ell$-Matchoid Problem with a Coverage Objective*, SIAM Journal on Discrete Mathematics (2023), gives a general-oracle deterministic joint-representative construction for the linear-objective case. Definition 3.1, Algorithm 1 and Theorem 3.6 in the [author PDF](https://www.di.ens.fr/~cchuang/work/matchoid.pdf) are the direct methodological antecedent. Lemma LM15 is a restricted total-blocking-rank version with its proof included above. Representative-set methods and rank-parameter tractability are not claimed as new here.

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with Reachability for Weighted $d$-Matroid Intersection*, [arXiv:2603.17345v1](https://arxiv.org/html/2603.17345v1), provide stronger reachable-kernel results for one arbitrary matroid with special additional matroids, including partition and laminar cases. Their Theorems 1–4 and Section 5 are relevant public comparisons. The original weighted-laminar feasible set here is not simply a common independent set of the auxiliary depth partitions: those partitions are only used to encode a particular replacement's blocking subtrees. Their kernel theorem is therefore not invoked as an unproved direct solver for this model.

Doron-Arad, Kulik and Shachnai, *An FPTAS for Budgeted Laminar Matroid Independent Set*, [arXiv:2304.13984](https://arxiv.org/abs/2304.13984), studies a laminar matroid resource together with a single knapsack budget and gives an FPTAS. Its resource/side-constraint placement differs from the present arbitrary global polymatroid with common-weight quotas throughout an explicit laminar family. The comparison here uses the verified primary abstract and does not infer a missing exact parameterized theorem from that abstract.

These bounded comparisons establish antecedents and model distinctions, not a first-algorithm or priority claim. The new proved interface is the deterministic compression of arbitrarily many laminar weighted nodes into bounded total-rank replacement tests, together with original-total zero completion and the binary-space implementation.

## 12. Incremental status

This complete proof is included in checkpoint T. It does not edit the frozen support-pattern classification. The companion prefix manuscripts have a better exponential dependence in their narrower geometry. The present theorem handles a branching laminar family, with the explicit zero-cost scope stated in Section 1 and challenged in Section 10.

Arbitrary nonuniform scalar coefficients on zero-weight coordinates require an additional argument: their optimal completion cost is not the fixed affine expression LM14. The separate companion [laminar-valuated-zero-completion-fpt.md](laminar-valuated-zero-completion-fpt.md) supplies that argument for both optional and mandatory resources using an optimal-completion valuation. The present elementary proof and its stated scope remain unchanged.
