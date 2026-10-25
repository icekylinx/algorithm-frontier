# Independent audit: safe machine contraction and residual-rank profiles

**25 October 2026. Full independent mathematical review of S1--S12.**

The theorem in `safe_machine_contraction_rank_kernel_draft.md` passes. Its reduction safely fixes complete machine loads, contracts every job polymatroid, and gives a residual optimum no larger than the original integer optimum. The greedy threshold closure and the all-budget profile are exact for the stated full-marginal absorption rule. They are not asserted to optimize over arbitrary partial assignments on removed machines.

The composition bound is

\[
             C_{\max}\le\max\{\beta_k,
                         \alpha_F\mathrm{OPT}+e_F\},
\]

where the residual large-job rank is at most k. Unlike one-large-position commitment, this reduction may absorb multiple large units at a machine and does not require the original unit-box large-job rank to be full.

## 1. Greedy marginal assignments are genuine restricted bases

For each job type j, absorbing p after a prefix F assigns exactly the integer increment f_j(F+p)-f_j(F). These counts are nonnegative. Along any absorption order on a final set F, the assigned vector is the usual greedy base of the restriction f_j|F: its total telescopes to f_j(F), and diminishing returns bounds its count on every subset of F by that subset's rank.

The total load assigned at the absorption step is exactly

\[
             c_p(F)=\sum_j p_j[f_j(F+p)-f_j(F)].
\]

Later steps assign counts only at newly absorbed machines and do not change earlier assignments. Therefore a sequence whose recorded marginal costs are at most B certifies an actual load at most B on every removed machine. It does not require those machines to be independent in any player matroid or to receive at most one unit of a type.

Each c_p(F) is nonincreasing as F grows while p remains outside. This follows separately from submodularity of every f_j and from the nonnegative job sizes. Exact rational comparisons and binary counts suffice; no individual job-copy expansion is involved.

## 2. Any restricted base combines with any contracted base

Fix one rank f, let Q=P minus F, and let a be a base of f|F while b is a base of f/F. For A subset P, write U=A intersect F and V=A intersect Q. Then

\[
 \begin{split}
 a(U)+b(V)
 &\le f(U)+f(F\cup V)-f(F)\\
 &\le f(U\cup V).
\end{split}
\]

The last inequality is precisely submodularity for F and U union V, whose intersection is U. Total counts add to f(P), so a union b is a base of f.

There is no hidden compatibility condition between the two bases. In particular, the committed greedy vector need not agree with the restriction of the unknown optimum. Applying this statement independently to all types gives a legal full original schedule after any legal residual schedule is reconstructed. Since the two schedules occupy disjoint machine sets, their makespan is the maximum of their two bounds, rather than their sum.

## 3. The dominated contracted-base lemma is correct

Let x be any original integer base of f, and put g=f/F on Q. For A subset Q,

\[
 \begin{split}
 g(A)+x(Q\setminus A)
 &=f(F\cup A)-f(F)+f(P)-x(F\cup A)\\
 &\ge f(P)-f(F)=g(Q).
\end{split}
\]

The minimum over A equals g(Q), since A=Q attains it. The ordinary integral box-restriction formula therefore supplies an integer base z of g with z<=x|Q.

The manuscript's direct proof also passes and avoids relying only on a quoted formula. Choose a maximum-total integer independent z bounded by x|Q. Every coordinate below its upper bound belongs to a tight g-set; otherwise all sets containing it have integer slack at least one and the coordinate could be increased. The union of these tight sets is tight, because union and intersection of two tight sets remain tight by submodularity and feasibility. Outside that union all coordinates are at their upper bounds. This gives z(Q)=g(A)+x(Q minus A)>=g(Q), and feasibility forces equality. If the union is empty, all coordinates are already at their bounds and the same calculation uses g(empty)=0.

Apply this lemma separately to every type in an original optimum. Each residual type count can be no larger at any remaining machine than in that optimum. Since all sizes are nonnegative, the resulting residual schedule has makespan at most OPT. Thus OPT_F<=OPT is exact. The dominated vectors are needed only for the proof; the algorithm does not need to recover the unknown optimum.

## 4. Threshold closure is unique and monotone

At a fixed B, a legal step adds p with c_p(F)<=B. Compare any legal sequence with a terminal set G obtained by another legal sequence. If the first sequence's current prefix F lies in G and its next p were outside G, diminishing marginal costs would give c_p(G)<=c_p(F)<=B, contradicting terminality. Induction gives containment of the first final set in G; reversing roles gives equality.

This proves an order-independent final set F*(B). The same argument compares thresholds B<=B' and proves F*(B) subset F*(B'). The actual type counts assigned on the closed set may depend on the chosen order, but every legal order certifies the same load threshold and the same contracted ranks. The theorem only requires those properties.

This is the least closed set reachable from the empty set under the threshold rule. It is not a statement that an arbitrary subset with a feasible B-load assignment must be reachable by full-marginal absorption.

## 5. One minimum-marginal order gives all closures

Construct a complete order by choosing a minimum current c_p(F) at every step. The recorded costs l_i need not be monotone: absorption can lower subsequent costs, and removal of a low-cost machine can also leave a larger minimum. The prefix maximum B_i=max_{t<=i} l_t is therefore the correct profile.

For any threshold B, all steps before the first l_i>B are legal. At that first violation, l_i is the minimum current cost, so no unabsorbed machine is legal. The earlier prefix is thus the terminal closure F*(B). Equivalently, it is the longest prefix with B_i<=B. This equivalence includes cascades in which an expensive eligible step unlocks cheaper later steps, and includes zero-cost initial machines at B=0.

The residual large rank kappa_i is nonincreasing along the order. For k<h, let i be the first index with kappa_i<=k. A smaller threshold than B_i stops before reaching any such index, so beta_k=B_i is the exact minimum threshold under this rule. Completing the entire equal-B_i plateau gives the actual F*(beta_k), whose residual rank can only be smaller. For k>=h, beta_k=0; for k=0 the terminal full set ensures existence. There are only q possible positive threshold values, even if h is exponentially large numerically.

This is a precise all-budget computation, not a binary search over h or an enumeration of all machine subsets. The naive implementation needs O(q^2 t) original rank queries and polynomial binary arithmetic, with cached f_j(F) values. It stores all assigned counts explicitly in a q by t table.

## 6. Composition has no extra promise or target-search loss

The contracted rank is f_j^F(S)=f_j(F union S)-f_j(F). Its oracle uses one original rank evaluation after the baseline f_j(F) is cached. It remains integral, monotone, normalized, and submodular. Its total large rank is exactly kappa(F), so a residual algorithm whose nonlinear cost depends on that rank runs within the stated rank-k bound.

For a residual guarantee C_res<=alpha_F OPT_F+e_F with alpha_F>=0, substitute OPT_F<=OPT. Combining schedules on disjoint machine sets gives max{beta_k,alpha_F OPT+e_F}. Neither the committed loads nor beta_k depend on a trial makespan. The residual algorithm may run its own already proved target search; no additional cap-failure rule or unknown-optimum threshold is introduced by this preprocessing.

The original large Boolean rank need not equal h. After contraction, the residual scheduling theorem handles its own Boolean-rank check or easy branch. If many large units can be safely absorbed, the original h can exceed q while the residual large rank is small. This is a different parameter reduction from committing one large position in an aggregate Boolean basis.

## 7. Numerical consequences and zero-rank residual cases

For one homogeneous large size a and arbitrary smaller sizes at most u<a, the reviewed workload theorem gives

\[
  C_{\max}\le\max\left\{\beta_k,
              \left(2-\frac1{3+\eta}\right)\mathrm{OPT}+u\right\}
\]

with the stated rank-k exact or rank-quasipolynomial runtime. If eta>1 is allowed in the statement, use eta0=min{eta,1} in the referenced algorithm. Its coefficient is no larger than the displayed one, and its accuracy-dependent runtime still fits O(1+eta^{-1}) up to an absolute constant factor. Contracted singleton ranks only decrease; types with zero residual rank can be removed. The remaining maximum smaller size is at most the original u.

For two original positive sizes, residual integer small counts require no workload rounding, so the rank-exponential bound is max{beta_k,(5/3)OPT}. If all large rank is absorbed, the residual one-size problem is solved exactly by a coordinate-cap total-rank check, yielding max{beta_0,OPT}. For many smaller sizes and no residual large rank, fractional assignment plus the per-machine additive rounding gives max{beta_0,OPT+u}. These are stronger zero-rank endpoints and do not invoke a positive-rank unit theorem.

An original-instance public additive schedule can be run independently and compared by actual makespan, giving the minimum with OPT+a and therefore with 2OPT when a is the largest positive original size. No conclusion that beta_k is automatically small is needed or justified. Combining safe absorption with a further residual bottleneck-position commitment is valid if the latter's separate load term is also included in the final maximum.

## 8. Review conclusion and scope

No gap was found in S1--S12. The exact dominated-base comparison is the central reason arbitrary safe commitments do not worsen the residual optimum. Diminishing marginal loads then make the threshold closure unique and allow all residual-rank certificates to be computed in a single polynomial run.

The profile is optimal only for full-marginal threshold absorption. More selective assignments could remove machines more cheaply, so this theorem is not a general kernel optimality statement or a worst-case approximation improvement without a favorable beta_k. The generic contraction, greedy-base, and box-intersection facts are classical; the reviewed result is their particular scheduling composition and parameter profile.

This is an independent internal mathematical audit, not implementation, formal verification, external peer review, or exhaustive publication-priority determination.
