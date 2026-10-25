# Independent audit: near-equal large sizes and bottleneck rank budgets

**25 October 2026. Independent mathematical review of H1--H16.**

The proof in `near_equal_large_sizes_bottleneck_makespan_draft.md` passes, with the explicit convention that a_- and a_+ are the actual minimum and maximum positive-rank sizes in the chosen large band. That convention is necessary: if they were merely arbitrary enclosing bounds, a_- need not belong to the original size grid and T<a_+ need not imply infeasibility.

The reviewed conclusion is an original integral schedule with

\[
 C_{\max}\le\max\{\beta(D,R)\mathrm{OPT}+u,B_k\},
 \qquad
 \beta(D,R)=\max\{1+R/2,2-1/(DR)\},
 \qquad R=a_+/a_-.
\]

Its nonpolynomial running time depends on the residual rank budget k. Both the additive u and the computable commitment term B_k are retained. The k=0 polynomial endpoint has the stronger envelope max{OPT+u,B_0} when the large-band Boolean matroid has full rank.

## 1. Aggregate large positions can be decomposed after the search

Let f_b be the sum of the original large-type ranks and h=f_b(P). An M-basis, where M is the unit-box cap of f_b and has rank h, is an integer base of f_b with all coordinates Boolean. Integral polymatroid decomposition therefore writes its indicator as a sum of integer bases of the original large-type ranks. Since the sum at each chosen machine is exactly one, that machine receives precisely one unit of exactly one original large type.

If type j is assigned to p, then 1<=f_j({p}); its size is therefore at most the locally defined

\[
 a_p=\max\{p_j:j\text{ large},\ f_j(\{p\})\ge1\}.
\]

A loop of M has f_b({p})=0 and cannot belong to any selected basis. Thus setting a_p=0 there is harmless. Crucially, the construction commits positions only, not particular large types. An arbitrary early type decomposition could obstruct extension, but no such decomposition is used.

This validates the coupling of the large-type reconstruction with the player-matroid search, including the case where the committed set F_0 is far from the unknown optimum's large recipients.

## 2. The bottleneck profile bounds final original loads

For each machine, W_p is the sum of all smaller-type singleton workload bounds and C_p=W_p+a_p. In every final original integral assignment, a machine carrying one large unit has load at most C_p. This statement is true after smaller-job rounding because every final original component still satisfies its singleton rank inequality.

A minimum-bottleneck independent F_0 of cardinality h-k is found by sorted matroid greedy. The same sorted greedy basis gives the optimum threshold for each cardinality: a cost threshold permits j independent choices exactly when its low-cost prefix has rank at least j. Consequently B_0,...,B_h is computable in polynomial time and is nonincreasing; B_h=0 represents the empty commitment.

The bound on a committed machine is C_p<=B_k with no extra +u. The comparison B_k<=a_++lambda_k is valid by choosing a set minimizing its maximum W_p. In the homogeneous large-size case a_p=a on all nonloops, equality holds for nonempty commitments.

## 3. Rank loss and the hard-target promise

If the Boolean cap loses total large rank, a legal schedule cannot have at most one large unit per machine. It must contain a machine with two such units, so OPT>=2a_-. Public all-job additive rounding yields OPT+a_+<=(1+R/2)OPT. This branch does not need a bottleneck profile or a unit core.

Otherwise M has rank h. For a hard target a_+<=T<2a_-, a true schedule uses exactly one large unit on each member of an M-basis I*. Every such unit has size at least a_-, so the smaller workload at that member is at most T-a_-. Capping the smaller-workload polymatroid at c=T/Delta must preserve its total rank. Complementing its true base supplies K=a_-/Delta dual units at every member of I*.

Contracting F_0 only in M gives rank k. Since I* spans M, some subset of I* minus F_0 is a basis of this contraction. Restricting the true dual allocation to that subset retains the full K quota. Therefore the unit core's failure is a genuine target infeasibility certificate, independently of the value of B_k.

The returned restricted dual vector can be extended by zero on F_0: monotonicity gives y(S)=y(S minus F_0)<=f(S minus F_0)<=f(S). Extending to a full integral dual base preserves the residual quota. No positive private allocation on F_0 is required.

## 4. Numerical scaling and the positive growth margin

Choose a common original quantum g and write D=A/B. With Delta=g/A, the actual band minimum a_-=A_0g gives K=A_0 A and b=A_0 B, so Db=K exactly. Every smaller coefficient p_j/Delta and every target T/Delta is integral on the chosen grid. All these numbers retain polynomial bit length; none is expanded into individual workload units.

For D>=D_k=3-2/k, the strict unit condition holds because D_k b<=Db=K<K+1+(k-1)/k. For D=D_k+eta its slack is eta b+1+(k-1)/k. Dividing by 2b-1 gives a ratio strictly greater than eta/2. The rank-quasipolynomial growth argument therefore applies without an additional large-quota requirement. The choice D=3+eta has at least the same excess above D_k.

The original small-job integrality cost remains +u. The artificial scaling bypasses a workload quota ceiling only because the final algorithm separately reconstructs and rounds the original smaller jobs.

## 5. All three machine classes have the claimed loads

Decompose the final Boolean aggregate basis into original large bases after the search. Decompose the smaller workload into scaled integer bases, divide the components to obtain fractional original smaller bases, and use the independently proved per-machine rounding lemma.

On the residual selected set J, the dual quota leaves smaller workload at most T-a_-/D before rounding. The assigned large type has size at most a_+, yielding load at most T+a_+-a_-/D+u. On the committed set F_0, the direct final singleton argument gives B_k. Off the selected set, the load is at most T+u.

For a hard target T>=a_+,

\[
 T+a_+-a_-/D
 =T+\left(1-\frac1{DR}\right)a_+
 \le\left(2-\frac1{DR}\right)T.
\]

The coefficient multiplying a_+ is nonnegative because D>=1 and R>=1. For an easy target T>=2a_-, all-job additive rounding gives T+a_+<=(1+R/2)T. These yield the displayed beta(D,R) envelope. No interaction with the later large-type decomposition can violate it, since the proof uses the uniform a_+ bound on J and the valid local a_p bound on F_0.

## 6. Target optimization and the k=0 endpoint

All target rejections are sound original infeasibility statements. Every original optimum load lies on the original grid and hence the finer Delta-grid. The upper endpoint max{V,2a_-}, for any actual feasible original schedule of load V, succeeds in the easy branch. With a failed lower and successful upper trial, adjacent-grid termination gives a successful trial at most OPT, even if success choices are not monotone. The fixed envelope max{beta T+u,B_k} is monotone in T, so the optimized guarantee follows.

For k=0, choose a full bottleneck basis of M and solve only the fractional smaller-job balancing problem. Deleting the large jobs from an optimum schedule proves that the fractional smaller makespan is at most OPT. Smaller rounding increases every load by at most u. Committed machines obey B_0 directly; all other machines obey OPT+u. The aggregate Boolean basis still decomposes into all original large types. This proves H13 without any D_0 or target-dependent private condition.

The same endpoint can be obtained by workload capping on a common original grid: the integer workload representation of an original optimum schedule guarantees a feasible cap no larger than OPT. Exact recovery of a fractional optimum is unnecessary for this alternative.

Running all budgets up to a chosen maximum adds only a polynomial factor because h<=q in the full-Boolean-rank branch. Returning the best actual schedule, also comparing with the public two-approximation, justifies an envelope of the individual bounds. Empty smaller bands cause no problem: their workload is zero and u=0.

## 7. Numerical corollaries and baseline scope

For R<=1+tau and D=3+eta,

\[
 2-\frac1{(3+\eta)(1+\tau)}
       \le\frac53+\frac\eta9+\frac\tau3.
\]

This follows by splitting the reciprocal loss first in eta and then in tau. The easy coefficient 3/2+tau/2 is at most 5/3+tau/3 for 0<=tau<=1. Thus H14--H16 are correct. At k=3, the hard coefficient is 2-3/(7R), and beta(D_3,R)<5/3 precisely in the stated sufficient regime R<9/7; the easy requirement R<4/3 is then automatic.

The general arbitrary-job-polymatroid comparison is to the public polynomial two-approximation and the checked additive rounding primitive from [Bamas et al.](https://arxiv.org/html/2307.08453v1). The independently opened primary source [Jansen and Rohwedder, Theorem 16](https://arxiv.org/html/1701.07208v2) gives the constructive ordinary restricted-assignment bound 11/6+epsilon in n^{O(epsilon^{-1} log n)}. That theorem needs no band or small-size condition; the present comparison is explicitly conditional and in part concerns a broader oracle-polymatroid model.

The elementary enumeration comparison is also valid: enumerate all h large-unit placements in q^{O(h)} time, test their original polymatroid feasibility, optimize fractional smaller workloads for those fixed loads, and round. The optimum large placement appears in the enumeration and yields OPT+u. This explains why the present result trades approximation quality for a polynomial input degree independent of h; the enumeration is not an FPT bound in h.

With the explicit actual-extrema convention, no gap was found in H1--H16, reconstruction, target search, or the claimed running-time parameter. This is an independent internal mathematical audit, not implementation, formal verification, external peer review, or exhaustive publication-priority determination.
