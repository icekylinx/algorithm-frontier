# Exact laminar quotas with arbitrary zero-weight completion costs

**25 October 2026. Complete incremental proof; full internal mathematical reviews completed for checkpoint T.**

This note removes the uniform-zero-scalar restriction from `laminar_common_weight_root_cap_fpt.md` (LM). All coordinates may now have arbitrary signed rational scalar coefficients, including coordinates whose common numeric weight is zero. The resource remains one global integral polymatroid, with either optional integer vectors or original-total integer bases. All common-weight laminar quotas and the one scalar objective remain exact.

The new ingredient is a representative lemma for a valuated matroid supplied with an exact overlap-first optimization oracle. Optimal zero completion at a fixed positive cardinality is a valuated matroid by the established weighted Rado-induction theorem. Its possibly enormous matching representation is used only to prove exchange. Every actual optimization uses a compressed polymatroid intersection with just two ranks.

## 1. The full theorem

Let \(F\) be a normalized monotone integral polymatroid rank on an explicit ground \(E\), with binary counts and rank values. Integer resource vectors are in \(P(F)\), or in the original base with total \(R=F(E)\). Eligibility masks and binary coordinate domains are allowed; a mandatory preparation always retains its original \(R\).

Let \(\mathcal L\) be an explicit laminar family. One nonnegative integer vector \(w\) supplies the coefficients of every row:

\[
                 l_A\le\sum_{e\in A}w_ex_e\le u_A,
                         \qquad A\in\mathcal L.
\tag{VZ1}
\]

Rows may be upper, lower, or equality requirements. A missing lower bound is zero and a missing upper bound is infinity. An explicit root row gives

\[
                              w\cdot x\le B.
\tag{VZ2}
\]

Every finite target is a nonnegative integer. The scalar \(c\cdot x\) has arbitrary signed rational coefficients and is minimized or maximized exactly. A bound on this same scalar may be tested by its optimum. No additional independent scalar constraint is assumed.

**Theorem.** Exact feasibility and scalar optimization have a deterministic algorithm with running time

\[
                  2^{O(B^2\log(B+1))}\operatorname{poly}(H)
\tag{VZ3}
\]

and uniform polynomial binary workspace. The exponential factor is independent of the number of laminar nodes, the numerical resource rank, and the number or scalar diversity of zero-weight coordinates. Here \(H\) includes the full explicit binary input and polynomial rank-oracle encoding/bit bounds. Standard exact submodular minimization and integral polymatroid intersection are charged polynomially.

For maximization, negate \(c\) and solve the minimization problem. The proof below therefore uses a minimum-cost convention throughout.

## 2. Preparation and optional disposal

Use LM's safe integer preparation. Lower targets exceeding \(B\) are impossible. Upper targets can be clipped to \(B\). A positive-weight coordinate with \(w_e>u_A\) in a containing upper row cannot be used even once, and is masked. Resource loops are also removed. Zero upper rows mask their positive-weight coordinates. Numeric sets are projected onto the surviving positive ground, with duplicate sets merged and empty positive lower rows rejected. None of these rules removes a zero-weight coordinate merely because its scalar is nonzero.

For an optional resource, first add one disposal coordinate \(\delta\), of numeric weight and scalar zero. On the enlarged ground define

\[
 F^+(A)=
 \begin{cases}
 F(A),&\delta\notin A,\\
 R,&\delta\in A.
 \end{cases}
\tag{VZ4}
\]

This is an integral polymatroid rank. An optional vector \(x\) extends to its total-\(R\) base by placing \(R-x(E)\) in disposal, and projection back preserves every original row and scalar. Original mandatory resources receive no disposal. All subsequent masks retain the required total \(R\); rank loss rejects a mandatory attempt. In the optional lift, disposal supplies the original total without forcing the retained real resource itself to have rank \(R\).

Hence it is enough to solve the resulting full-base problem. Write \(P\) for its positive-weight coordinates and \(Z\) for all zero-weight coordinates, including disposal if present. The scalar coefficients on \(Z\) are unrestricted. Below \(F\) denotes this prepared rank and its full rank is \(R\).

The two dominance reductions from LM are unchanged. Retained upper capacities strictly increase up an inclusion chain, so their depth \(D\) is at most \(B\). For lower rows, an ancestor is redundant if a descendant has a no-smaller lower target. The remaining positive lower targets strictly decrease down each inclusion chain. Their minimal sets are disjoint; reject if the sum of those lower bounds exceeds \(B\). Otherwise at most \(B\) such leaves and depth at most \(B\) give at most \(B^2\) retained lower rows.

There are thus at most \(B^2+1\) distinct lower-membership patterns. Candidates will be classified by their common positive weight and this membership pattern. This gives at most

\[
                              G\le B(B^2+1)
\tag{VZ5}
\]

classes. The number of upper nodes may be arbitrarily large; only their depth is bounded. No occupancy vector over all upper nodes is enumerated.

## 3. An abstract valuated replacement lemma

Let \(U\) be a finite ground and let

\[
                    p:\binom Uk\longrightarrow\mathbb Q\cup\{+\infty\}
\tag{VZ6}
\]

be a minimum-cost valuated matroid of rank \(k\), with nonempty finite domain. Its exchange axiom says that for domain bases \(S,A\) and \(e\in S\setminus A\), some \(f\in A\setminus S\) satisfies

\[
            p(S)+p(A)\ge p(S-e+f)+p(A-f+e).
\tag{VZ7}
\]

Assume an exact oracle which, for a set \(Y\subseteq U\), returns a domain basis \(A\) first maximizing \(|A\cap Y|\), and subject to that minimizing \(p(A)\).

**Overlap replacement lemma.** For any domain basis \(S\) and \(e\in S\cap Y\), an element \(f\in A\cap Y\) is a feasible no-worse replacement:

\[
                         p(S-e+f)\le p(S).
\tag{VZ8}
\]

If \(e\in A\), choose \(f=e\). Otherwise apply VZ7. If the exchanged \(f\) were outside \(Y\), the domain basis \(A-f+e\) would have greater overlap with \(Y\), a contradiction. Thus \(f\in Y\), and \(A-f+e\) has the same maximum overlap as \(A\). Optimality on that face gives \(p(A-f+e)\ge p(A)\). Cancelling this inequality in VZ7 proves VZ8.

Notice that \(A\) is optimized over **all** domain bases. It is not required to lie in \(Y\). Only the emitted replacement candidates \(A\cap Y\) lie in the desired pool.

## 4. Representatives against separately bounded blocker ranks

Let \(N_1,\ldots,N_D\) be auxiliary matroids on \(U\), and let \(T\subseteq U\) be a candidate pool. The following generator emits a small set of candidates.

Maintain independent sets \(J_i\), initially empty, and form

\[
                   Y(J)=T\setminus\bigcup_{i=1}^{D}
                                      \operatorname{cl}_{N_i}(J_i).
\tag{VZ9}
\]

Use the overlap oracle on \(Y(J)\) and emit every element of \(A\cap Y(J)\), at most \(k\) elements. Stop if this set is empty. If \(\sum_i|J_i|<d\), branch for every emitted \(f\) and every \(i\), replacing \(J_i\) by \(J_i+f\). Each insertion preserves independence, because \(f\in Y(J)\). The depth is at most \(d\), the branching factor at most \(kD\), and the number of emitted positions is at most

\[
                            k\sum_{j=0}^{d}(kD)^j.
\tag{VZ10}
\]

**Representative property.** Suppose \(S\) is a domain basis and \(e\in S\cap T\). Let \(B_i\) be independent in \(N_i\), with total size at most \(d\), and suppose \(e\) is outside all their closures. Some emitted \(f\) satisfies VZ8 and lies outside every \(\operatorname{cl}_{N_i}(B_i)\).

To prove it, maintain a recursion path with \(J_i\subseteq\operatorname{cl}(B_i)\) and \(e\in Y(J)\). The overlap replacement lemma supplies at least one emitted \(f\) with VZ8. If that \(f\) passes every blocker test, the proof is complete. Otherwise it lies in \(\operatorname{cl}(B_i)\) for some \(i\). Since it is outside \(\operatorname{cl}(J_i)\), one has \(|J_i|<|B_i|\). The branch inserting this particular \(f\) in \(J_i\) remains legitimate: closure containment persists and \(e\) stays outside. A legitimate path cannot exceed the total test rank \(\sum_i|B_i|\le d\). Thus it reaches a passing candidate.

All emitted candidates are tried as branch choices; the algorithm need not identify which one is good for the unknown protected solution. This is the step that replaces the fixed element scores of LM. There is no assumption that \(S\) is independent in the auxiliary matroids.

## 5. Applying the lemma to laminar quotas at fixed positive cardinality

Use positive copies so that a set \(S\subseteq U\) represents the positive counts. Each copy has its owner's positive weight, scalar coefficient, and numeric memberships. For a fixed \(k\le B\), the finite domain of \(p_k\) will consist of the \(k\)-sets that admit a full resource completion through \(Z\); its value will be their minimum true scalar cost. Sections 6–7 establish exactly this valuated matroid and its polynomial oracle.

For each upper depth \(j\), define a rank-one partition matroid whose classes are the retained upper nodes at that depth, together with a remainder class. For each weight/lower-membership class \(T\), run Section 4 with these \(D\) auxiliary partitions and \(d=k-1\).

Here is why the test-rank budget is enough. Fix a numerically feasible domain basis \(S\), remove \(e\in S\) of weight \(w\), and let \(S^-=S-e\). An upper node can newly block an equal-weight replacement only if

\[
                  u_A\ge w,
           \qquad w(S^-\cap U_A)+w>u_A.
\tag{VZ11}
\]

Nodes with \(u_A<w\) contain no candidate of this class by individual eligibility. Every node in VZ11 contains a unit of \(S^-\), and none contains \(e\). The inclusion-maximal such nodes are disjoint, number at most \(k-1\), and contain all the relevant blocking nodes. At each depth, choose one unit of \(S^-\) in each maximal blocker at that depth; these chosen units form an independent test in that depth's partition. The total test size is at most \(k-1\), and \(e\) passes every test.

The representative lemma gives a same-class replacement \(f\) that avoids all blocking nodes and satisfies \(p_k(S-e+f)\le p_k(S)\). The valuated domain preserves both resource feasibility and full zero completion. The common weight and lower-membership class preserve every lower total exactly. Avoiding the blocking nodes preserves every upper. Since VZ7 returns \(f\in A\setminus S\) when \(f\ne e\), a proper replacement preserves the set's cardinality.

Repeatedly replace any selected copy outside the union of emitted candidates. Each proper replacement increases the number of selected copies in that union, keeps all numeric rows feasible, and does not worsen the true completed scalar. Hence an optimum at this fixed \(k\) is represented in the union.

For \(1\le k\le B\), the emitted-position count satisfies

\[
 K_k\le B(B^2+1)\,k\sum_{j=0}^{k-1}(kD)^j
                     =2^{O(B\log(B+1))}.
\tag{VZ12}
\]

Enumerating \(k\)-sets from these positions, testing the numeric rows, and computing their exact completion values costs at most \((K_k+1)^k\operatorname{poly}(H)\). Summing over \(k\le B\) gives VZ3. The zero-positive-cardinality case is handled separately by exact optimization on the zero ground.

## 6. Optimal zero completion is a valuated matroid

Give positive coordinate \(e\) a pool \(U_e\) of

\[
                         b_e=\min\{F(\{e\}),\lfloor B/w_e\rfloor\}
\tag{VZ13}
\]

distinct copies. These represent all possible root-feasible positive counts. Let \(U=\bigcup_{e\in P}U_e\). For \(|S|=k\), define \(p_k(S)\) as the minimum of the true scalar over all original-total bases whose positive units are exactly \(S\), using arbitrary integer zero counts on \(Z\). Set \(p_k(S)=+\infty\) if no such completion exists.

We now apply a checked primary theorem, rather than assume a new projection property. Husić, Loho, Smith and Végh, *On complete classes of valuated matroids*, TheoretiCS 3 (2024), Definition 1.1, define an R-minor valuation by a maximum-weight matching from \(X\cup W\) into a full basis of a right-hand matroid. Their Theorem 2.9 gives the underlying weighted network-induction property, and their contraction closure fixes the mandatory left set \(W\). The maximum-value exchange axiom appears as (1b); negating the value yields the minimum-cost form VZ7. The [primary article](https://theoretics.episciences.org/14792/pdf) was checked at these statements.

For the mapping, consider the finite natural matroid of the entire prepared polymatroid \(F\): it has \(F(\{e\})\) conceptual right-hand copies for every coordinate and rank exactly \(R\). This is the **full** natural matroid, even if only some positive copies are allowed on the left. Its size may be numerically enormous and it will never be constructed by the algorithm.

On the left, use one vertex for each allowed positive copy \(u\in U\), with a single private edge to that same right-hand positive unit. Add \(R-k\) dummy vertices, each adjacent to every right-hand zero-weight unit. Give an edge ending at a unit owned by \(e\) weight \(-c_e\). A matching whose left endpoint set is \(S\) together with all dummies and whose right endpoint set is a basis chooses exactly those positive units and a legal full zero completion. Its maximum weight is exactly \(-p_k(S)\).

Thus, whenever the finite domain is nonempty, \(-p_k\) is the R-minor valuation in the cited definition, and \(p_k\) satisfies VZ7. If the domain is empty, the compressed oracle below detects that and the cardinality \(k\) is skipped. Allowing a conceptual graph with a huge finite dummy set is a proof device only; no running-time or workspace statement is charged to its construction.

## 7. The compressed overlap-first oracle

All actual computations use the coordinate ground

\[
                                  U\ \dot\cup\ Z,
\tag{VZ14}
\]

where positive copies have individual cap one and zero coordinates retain their original binary counts. Define one integral polymatroid rank on this mixed ground by

\[
 G(A)=\min_{C\subseteq P}
      \left[F\bigl((A\cap Z)\cup C\bigr)
               +\sum_{e\in P\setminus C}|A\cap U_e|\right].
\tag{VZ15}
\]

This is the shared projection rank with a box cap of one on each positive copy. Its independent region is exactly the vectors that aggregate to \(P(F)\) and satisfy those unit caps. It is the standard box-cap polymatroid rank; VZ15 also evaluates it by submodular minimization on the original positive-coordinate ground. No zero units are expanded.

For an attempted cardinality, first guard

\[
                             0\le k\le\min\{R,|U|\}.
\tag{VZ16}
\]

Use **one** additional partition-count rank, with positive-group cap \(k\) and zero-group cap \(R-k\). Intersect it with \(P(G)\) and require total \(R\). This integral face forces both group totals to be exact. Each positive coordinate is zero or one, so its positive part is a \(k\)-set in the domain of \(p_k\). Conversely every such domain set and every full completion lie on this face. An empty face detects an empty domain.

To obtain the overlap-first oracle for \(Y\subseteq U\), clear the denominators of the scalar coefficients, obtaining integer coefficients \(\widetilde c\), and put

\[
 C_{\max}=\max_e|\widetilde c_e|,
                 \qquad M=2RC_{\max}+1.
\tag{VZ17}
\]

Every full allocation has integer scalar in \([-RC_{\max},RC_{\max}]\). Minimize on the same integral face

\[
                          \widetilde c\cdot z
                                  -M\sum_{u\in Y}z_u.
\tag{VZ18}
\]

One extra overlap unit dominates every possible true-cost difference. Thus the returned positive set \(A\) maximizes \(|A\cap Y|\) and then minimizes \(p_k(A)\). The reward is attached to individual positive copies; their cap one in \(G\) is essential. Zero coordinates keep their original arbitrary scalar coefficients.

The oracle does **not** restrict all positive choices to \(Y\), and it does not add an exact \(Y\)-count as a third rank. The remaining laminar quotas are not imposed on this overlap query either: its returned basis need not satisfy them. The same-class replacement and blocker argument restores those requirements for the protected feasible solution. The oracle's only ranks are \(G\) and the two-group partition. Standard deterministic weighted integral-polymatroid intersection supplies this optimization with polynomial binary complexity.

Fix deterministic tie rules for replay. If a canonical positive set is desired, multiply VZ18 by \(2^{|U|+1}\) and add a distinct subset-bit score \(\sum_{j=0}^{|U|-1}2^j z_{u_j}\). Since positive entries are binary, this tertiary term cannot change the overlap or true-cost ordering and uniquely fixes the positive subset. In the branch where this oracle is used, \(|U|\) is polynomial in the original input, as proved next.

For a final candidate \(S\) of size \(k\), mask every positive copy outside \(S\), use the same positive-total \(k\)/zero-total \(R-k\) partition, and optimize the true scalar. The positive unit caps force every copy of \(S\) to be chosen. This evaluates \(p_k(S)\) and returns an attaining binary zero completion without extra constraints or a third polymatroid.

## 8. Uniform polynomial binary workspace and all-input time

Let \(n=|P|\). If \(B=0\) or \(n=0\), all positive counts vanish. Reject any positive lower requirement and optimize the scalar on the zero resource, retaining original total \(R\) in the lifted base problem. Rank loss gives infeasibility. This is a polynomial problem, including arbitrary signed zero costs.

If \(B\ge n\ge1\), use a direct count-vector fallback instead of constructing positive copies. Stream

\[
                          0\le x_e\le\lfloor B/w_e\rfloor
                                    \quad(e\in P).
\tag{VZ19}
\]

There are at most \((B+1)^n\le(B+1)^B\) vectors. Test their numeric rows and positive resource independence. For a surviving fixed \(x\), define

\[
                   h_x(A)=\min_{C\subseteq P}
                         \bigl(F(A\cup C)-x(C)\bigr),
                                  \qquad A\subseteq Z.
\tag{VZ20}
\]

As proved in LM, this is an integral residual polymatroid and describes all compatible zero completions. Its full rank cannot exceed \(R-x(P)\). A full completion exists exactly when equality holds; then minimum-cost greedy base optimization on \(h_x\), using the original signed zero coefficients, gives the exact best completion. Rank evaluations are submodular minimizations with binary modular terms. Only \(n\) counters, one best vector, and polynomial oracle workspace are retained. This branch costs \(2^{O(B\log(B+1))}\operatorname{poly}(H)\).

If \(1\le B<n\), construct the at-most-\(nB<n^2\) positive copies and keep all zero counts compressed. Every attempted \(k\) is at most \(B\), every representative recursion has depth at most \(k-1<n\), and every auxiliary partition list is explicit-input size. The rank formula VZ15 and the integral intersections have polynomial-size grounds and polynomial-bit coefficients. Clearing rational denominators and the overlap reward VZ17 also use polynomially many bits. The optional canonical subset score has \(O(|U|)\) bits, not \(2^{|U|}\) stored bits.

Do not store the representative union. An emitted position is encoded by a candidate-class index, a recursion path, and the final index of an element in the sorted set \(A\cap Y\). Each path step gives an emitted-element index at most \(k\) and a partition index at most \(D\). Replay the path using the deterministic oracle and discard an index if a step has no such emitted element. Recompute candidates whenever required. The number of all possible encoded positions is bounded by VZ12, including invalid positions.

Enumerate \(k\)-tuples of those indices, reject repeated copies and failed numeric rows, and evaluate exact completion on each surviving set. Every actual representative set is included. The stored indices use \(O(B^2\log(B+1)+B\log(H+1))\) bits, and the current \(J_i\) have total size at most \(k-1\). All are polynomial in \(H\) in this branch. Invalid paths, failed tuples, empty completion faces, and empty cardinality domains are counted within the same \(2^{O(B^2\log(B+1))}\operatorname{poly}(H)\) bound on arbitrary inputs.

The output is the positive vector together with an attaining zero vector, both in binary. For an originally optional instance, discard only the designated disposal coordinate. No real mandatory unit or scalar contribution is discarded.

## 9. Exactness and the earlier zero-cost obstruction

Fix an original optimum after optional disposal if needed, and let \(k\) be its positive cardinality. Its zero portion must already be a minimum-cost completion of its positive set: otherwise replacing it by a cheaper completion would leave all numeric rows unchanged and improve the optimum. Hence its scalar is \(p_k(S)\). The representative replacement theorem moves it to the finite candidate union without worsening \(p_k\), and the final compressed oracle returns an original feasible allocation attaining that value. Conversely every returned allocation satisfies the original resource, rows, total convention, and scalar definition. Therefore the optimum is exact.

The nonuniform-zero example in LM remains a valid counterexample to choosing representatives using positive element costs alone. It does not refute this theorem: the overlap oracle compares the **completed** value \(p_k\). At \(B=1\), it chooses the cheaper full completion directly, even when the positive coefficients tie.

The exponentially necessary \(2^{\Omega(B)}\) rank-oracle dependence from LM's depth-two example still applies, since it has strictly positive weights and scalar zero. It does not match the present upper exponent, and no optimal \(B^2\log B\) dependence is asserted.

## 10. Scope and primary-source positioning

The result uses one common numeric weight per coordinate across the laminar rows, nonnegative integer numeric weights, an explicit root cap, one global integral resource, and one exact rational scalar. Row-dependent numeric weights, overlapping nonlaminar families, another unrelated global rank, or a second independent unbounded scalar condition require further arguments. Rational common weights can be placed on a supplied common integer grid, with the normalized root cap used as the parameter.

The valuated exchange property is an established theorem, not a newly claimed characterization. The exact primary interface is Husić–Loho–Smith–Végh, [*On complete classes of valuated matroids*, TheoretiCS 3 (2024), Article 24](https://theoretics.episciences.org/14792/pdf), Definition 1.1, axiom (1b), and Theorem 2.9 (there attributed to Murota's network-induction theorem). Only their induced-valuation statement is needed; their structural negative results are not used.

The bounded-blocker recursion follows the representative-method perspective of Huang–Ward, with the new overlap-optimal-basis replacement argument written in Sections 3–4. LM records the directly checked [author version](https://www.di.ens.fr/~cchuang/work/matchoid.pdf) and the relevant 2026 reachable-kernel comparison. Count-profile and rank-parameter methods have substantial prior literature; this note makes no priority claim for those foundations.

The new proved composition is: arbitrary scalar zero completion becomes a valuated resource; one polynomial compressed overlap oracle supplies cost-aware candidate replacements; only the disjoint upper-blocker partitions need bounded-rank recursion. It removes the scalar-uniformity restriction while retaining the exact original model and the same root-cap running-time and binary-space bounds.

## 11. Incremental status

This is a separate stronger theorem in checkpoint T. It does not change the proofs of LM or `uniform_zero_scalar_laminar_extension.md`, or any frozen checkpoint. The elementary uniform-cost arguments remain useful independent special-case derivations. Full internal reviews covered the valuation mapping, overlap cancellation, individual-copy box caps, true-cost oracle, and all-input binary-space implementation. These reviews are not formal verification or external peer review.
