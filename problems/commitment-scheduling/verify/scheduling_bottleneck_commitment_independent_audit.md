# Verification note

**Curated source path:** `sources/checkpoint-o/scheduling_bottleneck_commitment_independent_audit.md`

The source audit follows.

# Independent audit: bottleneck commitments and reduced scheduling rank

**25 October 2026. Independent mathematical review of B1--B10.**

The derivation in `scheduling_bottleneck_commitment_rank_reduction.md` passes. Its key distinction is valid: arbitrary independent committed machines receive zero in the residual dual vector, so no private-coordinate allowance is needed. After reconstruction their final original job constraints give a separate singleton-workload bound. This removes the cap threshold from the comparator while retaining an explicit instance-dependent bottleneck term.

One qualification is necessary in the manuscript's comparison with the older private cap: the inequality derived from that private rank condition applies in the hard branch OPT<2a. At OPT>=2a the old cap was automatic and need not bound lambda_k; the easy branch supplies the required approximation independently. This qualification does not affect B1--B10.

## 1. The commitment profile is well defined and target independent

Assume the largest-job unit-box matroid M has rank h. For 1<=k<h, the singleton-workload thresholds W_p are nonnegative rational numbers, and all players together have rank h. Therefore some threshold attains rank h-k. Sorting the W_p and matroid greedy produces an independent F_0 of exactly h-k elements with max_{p in F_0} W_p=lambda_k (or at most lambda_k when equal thresholds occur).

The quantities W_p and lambda_k have units of workload. In the two-size case W_p=u f_s({p}); no additional u should multiply lambda_k in the final bound. Their encoding lengths are polynomial, even when ranks are binary and large. For k=h, take F_0 empty and lambda_h=0. This avoids interpreting a minimum threshold for the zero-rank condition over all real numbers.

Neither F_0 nor M changes with a hard target a<=T<2a. This target independence is what permits an ordinary one-sided search without a separate rank-budget rejection.

## 2. The full residual promise survives an arbitrary commitment

Let I* be the largest-job recipient basis of a true target-feasible schedule. Since I* spans M, its image spans M/F_0. Thus some J* contained in I* minus F_0 is a basis of the contraction, of rank exactly k. This uses no assumption that F_0 is a subset of I*.

The true dual smaller-workload allocation is feasible on the full recipient ground set and supplies K units on every member of I*. Restricting it to J* preserves feasibility in the recipient polymatroid restricted to Q=P minus F_0, and preserves all K units of each selected member. The rank-k residual allocation instance therefore has the full promise needed by the unit-quota theorem. No resource capacity is consumed by F_0 at this stage.

Consequently a sound rejection of that full promise is an original target infeasibility certificate. This remains true even when the final committed assignment would be a poor approximation on that instance; approximation quality and target-promise validity are separate.

## 3. Zero extension and base reconstruction are safe

If y belongs to the restricted recipient polymatroid on Q, its extension by zero satisfies, for every S,

\[
        y(S)=y(S\cap Q)\le f(S\cap Q)\le f(S).
\]

Thus the zero extension is feasible on the whole ground set. It can be extended to an integer base of f. This extension may add positive dual counts on committed machines; no argument requires those counts to remain zero. The selected largest-job set F_0 union J is an M-basis by the contraction identity.

Complementing the extended dual base yields the necessary smaller-workload base. Full-rank capping ensures it is also a base of the uncapped workload polymatroid. Scaled decomposition and per-machine rounding then yield bases of every original smaller-job polymatroid. In the two-size branch, the complement already gives integer small counts and no additional rounding is needed.

The argument would fail for arbitrary positive dual preassignments on F_0, because those could conflict with the residual vector. The actual construction makes no such preassignment, so this issue does not arise.

## 4. Final singleton bounds justify the commitment term exactly

Every final original type assignment satisfies x_j(p)<=f_j({p}). Hence a committed largest-job machine obeys

\[
        a+\sum_{j:p_j<a}p_jx_j(p)
           \le a+W_p\le a+\lambda_k.
\]

This is a bound on the final integral assignment, after all decomposition and rounding. It therefore incurs no additional +u. In particular, even if rounding changes a committed machine's workload unfavorably relative to its fractional precursor, the singleton inequality remains true.

The argument pays for commitments by this independent final load bound. It does not require them to retain the dual quota, and it does not assert that all original jobs can be placed on the committed set.

## 5. Many smaller sizes: exact quotas and the output bound

For rational D=A/B>=D_k=3-2/k, take Delta=g/A where g divides all original sizes. If a=A_0 g, then K=A_0 A and b=A_0 B are integer and Db=K exactly. The workload ranks, cap values, and targets have polynomial binary length; the scaling never creates an explicit list of artificial units.

At residual rank k the unit-quota inequality

\[
             (3-2/k)b<K+1+(k-1)/k
\]

is strict because its left side is at most K. At D=D_k+eta its slack divided by the cover coefficient 2b-1 is greater than eta/2. This is the already reviewed exact-quota workload argument and has no lower bound on K beyond positivity.

A noncommitted selected machine has final load at most T+(1-1/D)a+u. A nonselected machine has load at most T+u. Since D>=1, the former dominates the latter. Together with the commitment bound, the exact hard-target envelope is

\[
          \max\{T+(1-1/D)a+u,\ a+\lambda_k\}.
\]

For T>=2a the public additive rounding has load at most T+a<=3T/2. Therefore beta(D)=max{3/2,2-1/D} bounds both branches by max{beta(D)T+u,a+lambda_k}. The fixed values 3/2, 11/7, and 8/5 at k=2,3,4 are correct. The exact time is 2^{O(k)} poly(H); the positive-slack alternative has the stated rank-quasipolynomial bound. Taking the better explicit schedule with the public two-approximation justifies the minimum in B7.

## 6. Two sizes: the floors and finite-rank formula are consistent

Let c=floor(T/u) and

\[
       K=c-\lfloor(T-a)/u\rfloor
        =\left\lceil\frac{a+cu-T}{u}\right\rceil.
\]

In the hard branch a<=T and a>u, K is a positive integer and K<=c. A true largest-job recipient has at least K dual small-count units. The formula

\[
       b_k(K)=\left\lfloor\frac{kK+2k-2}{3k-2}\right\rfloor
\]

is the largest integer satisfying the strict unit-quota condition; multiplying that condition by k shows that an integer numerator must be at most kK+2k-2.

For k=1, b_1(K)=K. For k=2, b_2(K)=ceil(K/2). For every k>=3, b_k(K)>=ceil(K/3): checking K modulo 3 in the displayed formula proves this directly. Put t=a+cu-T, so 0<t<=a<=T and Ku>=t. The noncommitted selected load T+t-bu is at most T for k=1, at most 3T/2 for k=2, and at most 5T/3 for k>=3. The easy branch is at most 3T/2. Thus B10 has the correct alpha_k and no additive rounding loss.

The commitment term is still a+lambda_k because lambda_k was defined in workload units. Aggregation and later integer decomposition of the small job class do not alter its aggregate singleton count bound.

## 7. Target search and exceptional cases

Every rejection is sound for the original target: a necessary rank loss, T<a, infeasibility of the easy-branch assignment relaxation, or failure of the retained full-K promise. There is no cap failure and no separate budget condition; the contraction rank is exactly k.

Use the Delta-grid in the workload branch and any common original value grid in the indivisible two-size branch. All original schedule loads, hence OPT, lie on the chosen grid. An arbitrary feasible schedule with load V gives a sufficient upper endpoint max{V,2a}; the procedure succeeds there. Zero is a failed lower endpoint for a nonempty positive-size instance. A success below OPT is allowed and retains its actual schedule. At adjacent endpoints, the successful upper trial is at most OPT, because the failed lower trial is strictly smaller than OPT and OPT is a grid point. Substituting into the monotone envelopes proves B7 and B10. Monotonicity of algorithmic success choices is not needed.

If the largest-job Boolean rank is smaller than h, every schedule has makespan at least 2a. The additive all-job algorithm then gives 3OPT/2, using a search restricted to the easy interval; no lambda value is needed. If the user budget is at least h, set k=h and use no commitments. The term a+lambda_h=a is dominated by the other envelope since OPT>=a. Empty and one-size instances retain their exact polynomial routines. A k=0 variant may omit the unit core, but is not needed for B1--B10 and must not substitute into formulas containing 1/k.

## 8. Comparison with private slack and review conclusion

In the hard branch, the old private rank condition at OPT implies lambda_k<=OPT-a/D. Thus a+lambda_k<=OPT+(1-1/D)a<=(2-1/D)OPT, recovering its full-OPT guarantee. If that rank condition fails, the new bottleneck envelope can still be useful because the final singleton load may remain below the desired approximation envelope. For OPT>=2a, use the independent easy-branch guarantee; the old automatic cap alone makes no claim about lambda_k.

The proof supports arbitrary integral job polymatroids, binary counts, a reduced rank k, and a computable instance-dependent commitment cost. It does not prove an unconditional 3/2 or 5/3 polynomial approximation when that cost is large. No gap was found in zero extension, original singleton accounting, numerical scaling, target search, or the approximation statements B1--B10.

This is an independent internal mathematical audit, not formal verification, an implementation, external peer review, or an exhaustive publication-priority determination.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
