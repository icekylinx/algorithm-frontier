# Verification note

**Curated source path:** `sources/checkpoint-q/scheduling_bottleneck_commitment_second_audit.md`

The source audit follows.

# Second independent audit of bottleneck commitment rank reduction

**25 October 2026. Independent internal mathematical review.**

This review checks `scheduling_bottleneck_commitment_rank_reduction.md`
separately from the first independent audit. It also checks the exact
two-size specialization against the underlying unit-quota inequality.
The central conclusion is sound: an arbitrary independent commitment
set may reduce the player rank, provided its final load is accounted
for by a separate bottleneck rather than by an assumed resource quota.

## 1. Fixed commitments preserve the residual optimum promise

Let M have rank h and let F0 be independent of size h-k. Every original
target-feasible large-job recipient set I* is an M-basis. Since it
spans M, the rank of its image in M/F0 is k. Therefore some J* subset
of I* minus F0 is a basis of that contraction.

The old dual resource allocation restricted to J* remains independent
in the recipient polymatroid restricted to P minus F0 and keeps its
full K-unit quota. This argument works for any fixed independent F0;
it does not require F0 to belong to I*, have private dual capacity,
or be free in the old resource allocation. Thus the residual core
really has rank k and the full original promise.

Choosing F0 by singleton costs is only an objective-bound decision.
It is not used to establish the promise. The sorted-matroid greedy
construction of lambda_k is correct, because an independent set of
size h-k exists below threshold z exactly when the rank of the
corresponding sublevel set is at least h-k.

## 2. Zero extension is the valid resource operation

The output vector y of the restricted polymatroid is extended by zero
on F0. For every S, y(S)=y(S minus F0)<=f(S minus F0)<=f(S).
This proves independence in the full resource polymatroid directly.
Integral base augmentation then preserves all coordinates already
supplied to the residual basis.

There is no hidden positive resource commitment on F0. In particular,
no contraction loss or private-marginal inequality is needed at this
step. The final largest-job recipient basis F0 union J follows from
matroid contraction; its original same-size job components are
recovered by integral polymatroid base decomposition.

## 3. The committed-machine load bound survives rounding exactly

Every final smaller-job component is an integer base of its original
f_j. Therefore x_j(p)<=f_j({p}) individually. Summing with the true
job sizes gives at most W_p at a committed p, and the assigned large
unit contributes a. Hence its final load is at most a+lambda_k.

This bound is imposed on the final original allocations, not on a
fractional intermediate vector. Adding another u to it would be an
unnecessary loss. The +u rounding term is correctly retained for
residual selected machines and nonselected machines, where the load
bound instead uses the constructed fractional workload allocation.

## 4. Exact workload divisibility and finite-rank coefficients

For rational D=A/B>=3-2/k, choosing Delta=g/A makes K=a/Delta and
b=K/D integral. A target on the Delta-grid has an integer coordinate
cap c=T/Delta. All original loads and OPT also lie on that grid.
The numerical lengths are polynomial, even when counts and ranks
are large in value.

At rank k, the strict quota condition is
(3-2/k)b<K+1+(k-1)/k. The equality Db=K proves it immediately.
For D=3-2/k+eta, the slack divided by 2b-1 is greater than eta/2.
No large-quota proviso is needed after arranging exact divisibility.
This does not eliminate the original indivisible small-quota gate;
the workload construction later pays +u to recover original jobs.

In the hard branch, residual selected machines have load at most
T+(1-1/D)a+u. The assumption D>=1 justifies replacing a by T.
The easy branch has coefficient at most 3/2. Consequently the uniform
coefficient is max{3/2,2-1/D}, including the floor at 3/2 for k=1.
The listed exact values 11/7 at k=3 and 8/5 at k=4 are correct.

## 5. The exactly-two-size specialization removes the rounding term

With genuine integer small counts, a target T has
c=floor(T/u) and K=c-floor((T-a)/u). A feasible schedule supplies
K dual units on its large-recipient basis. The largest certified
integer quota at rank k is

\[
                   b_k(K)=\left\lfloor
                              \frac{kK+2k-2}{3k-2}
                            \right\rfloor.
\]

This follows by multiplying the strict unit inequality by k and using
integer arithmetic; replacing it by a weak unrounded inequality would
be incorrect. At k=1 the quota is K. At k=2 it is ceil(K/2). Thus
their hard-target load is at most T and 3T/2 respectively. At k>=3,
b_k(K)>=ceil(K/3) gives the 5T/3 bound. The easy branch is at most
3T/2 in all cases. These facts verify B9--B10 with no additive u.

The small counts produced after complementing a dual base are already
integer. No artificial fractional job decomposition is introduced
in this specialization, so there is no rounding error to charge.

## 6. One-sided optimization and exceptional ranks are correct

Every failure stated in the note is genuine original target
infeasibility. In particular, the residual core retains a full promise
whenever the original target is feasible; there is no cap-budget
failure to confuse with infeasibility. The commitment set and its
load bound are fixed across target queries.

The output bound is max{beta T+u,a+lambda_k}, or its no-rounding
two-size form, which is monotone in T. All possible original integral
loads lie on the chosen grid. A failed lower and successful upper
endpoint therefore lead at adjacency to a successful target at most
OPT, even if the algorithm's success set is not monotone. The stated
upper endpoint max{V,2a} is genuinely feasible and uses the easy
rounding branch. Binary target ranges have polynomial bit length.

If the Boolean cap of the largest-job polymatroid has rank less than
h, every integral large base assigns at least two large units somewhere.
Thus OPT>=2a, and the public additive bound OPT+a gives 3OPT/2.
No fictitious finite lambda profile is needed. Empty commitments at
k=h and the separately handled zero-budget/one-size cases are also
consistent with the formulas actually used.

## 7. Comparison with the former private cap and public candidates

For OPT<2a, the former private condition at OPT implies
lambda_k<=OPT-a/D. This yields the displayed committed-machine
bound at that optimum. For OPT>=2a, private-cap success is automatic
and provides no bound on lambda_k; the separate public additive
algorithm supplies the 3/2 guarantee instead. The revised Section 7
correctly makes this case distinction.

The public candidate guarantees OPT+a, which is at most 2OPT. Thus
the first term of the minimum in B7 can be written OPT+a if desired.
This is a strengthening from the very same public additive rounding
primitive, not an additional algorithmic assumption. The public
two-value 7/4+epsilon comparison retains its stated polynomial-time
advantage on unrestricted instances.

The additive and decomposition primitives are checked against Bamas
et al., <https://arxiv.org/html/2307.08453v1>, and the independent
per-machine rounding construction in the accompanying workload audit.
No publication-priority conclusion is inferred from this proof review.

## 8. Review outcome

The bottleneck theorem passes this independent review. Its stronger
optimization comparator is justified by dropping the private quota
on F0, extending by zero, and charging the actual final load there.
The theorem does not promise a uniform improved approximation for a
small budget when a+lambda_k is large. It provides an unconditional
rank-budget/load tradeoff, with the public algorithm available as a
directly evaluated fallback candidate.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
