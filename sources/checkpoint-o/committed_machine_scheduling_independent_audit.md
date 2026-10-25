# Independent audit: committing large-job machines without a private-slack cap

**25 October 2026. Independent mathematical review completed after a full read of the root manuscript, equations B1--B10.**

Reviewed manuscript: `scheduling_bottleneck_commitment_rank_reduction.md`.

The proposed refinement is valid in the supplied arbitrary integral
job-polymatroid model. It replaces a target-dependent private-slack
condition by an explicit absolute load bound on committed machines.
The new argument needs no private dual units at a committed machine.
It does need the original model's separation of the job-polymatroid
constraints by job type: all their interaction is through machine load.

This review uses the definitions and reconstruction established in
`many_small_sizes_private_slack_deficiency.md`,
`many_small_sizes_workload_makespan_transfer.md`, and
`two_size_makespan_private_slack_deficiency.md`.

## 1. Arbitrary independent commitments preserve the residual promise

At a hard target a<=T<2a, assume the largest-job Boolean cap has its
required full rank h, and call its matroid M. Let F0 be any M-independent
set. There is no workload or private-coordinate condition on F0.
Write Q=P\\F0 and contract F0 only in the player matroid.

A target-feasible original schedule gives an M-basis I* and a feasible
dual-workload allocation with at least K units at every member of I*.
Since I* spans M,

\[
 r_{M/F_0}(I^*\setminus F_0)
   =r_M(I^*\cup F_0)-r_M(F_0)=h-|F_0|.
\]

Consequently I*\\F0 contains a basis J of M/F0. Restricting the
promised dual vector to J leaves at least K units at each selected
coordinate and is feasible in the recipient polymatroid restricted
to Q. This is a restriction, not a contraction of the recipient
resource. There is no reservation of capacity for F0.

The rank-(h-|F0|) core therefore retains the full original K-unit
promise. Its failure, under that promise and its proved quota
condition, is a genuine original-target infeasibility certificate.
This reasoning does not require F0 to be a subset of I*.

## 2. Zero extension is always feasible

Let y be the dual-independent allocation produced on Q. Extend it by
zero on F0. For every S subset of P,

\[
 y(S)=y(S\cap Q)\le f(S\cap Q)\le f(S).
\]

Thus zero extension is feasible in the full dual recipient
polymatroid. Extend this vector coordinatewise to a full integral
dual base, and complement to the capped workload base as in the
accepted reconstruction. The full base extension may add positive
dual units on F0; this only helps its final small workload.

The selected largest-job machines F0 union J form an M-basis. Their
indicator is a base of the aggregate largest-job polymatroid, and
integer decomposition restores the original largest-job types.
There is at most one largest unit per selected machine.

The earlier private-coordinate lemma was needed when inserting a
positive quota at F0. No such insertion occurs here. Therefore a
missing private-slack condition is not a gap in this refinement.

## 3. Committed machines have an absolute final load bound

Let

\[
                  W_p=\sum_{j:p_j<a}p_j f_j(\{p\}).
\]

After workload decomposition and integral smaller-job rounding, each
original smaller-job vector x'_j is an integer base of its original
polymatroid. In particular,

\[
                     x'_j(p)\le f_j(\{p\}).
\]

The final smaller-job load at p is at most W_p, independently of the
fractional workload on p or of the rounding error estimate. Therefore
every committed machine p in F0 has final total load at most a+W_p.
One must not add an extra u to this absolute bound: the singleton
inequalities already apply to the rounded original schedule itself.

Every residual selected machine in J retains the quota guarantee,
and hence has the earlier bound beta(D)T+u in the many-small-sizes
construction. Unselected machines satisfy the smaller bound T+u.
It follows that the complete fixed-target bound is

\[
 \max\left\{\beta(D)T+u,\ a+\max_{p\in F_0}W_p\right\}.
\]

For exactly two sizes there is no fractional smaller-job rounding.
Here W_p=u f_s({p}), so lambda_k in the root manuscript is already
in workload units. The corresponding bound is max{5T/3, a+lambda_k};
one must not multiply this lambda_k by u a second time. For k=1,2,
the exact finite-rank quota in (B9) strengthens the hard-branch
coefficient to at most 3/2, and the easy branch has the same bound.
For k>=3 the uniform certified coefficient is 5/3, with the integer
quota qualification correctly retained in the manuscript.

## 4. Choosing commitments and optimizing the target

For 1<=k<h, matroid greedy can choose an independent F0 of size h-k
minimizing its largest W_p. The optimum bottleneck is

\[
 \lambda_k=\min\{z:r_M(\{p:W_p\le z\})\ge h-k\}.
\]

It is computed by sorting the singleton workloads and rank or
independence queries. The same F0 works for every hard-branch target,
because M and W do not depend on T there. The residual core rank is
exactly k, and every core failure is now a genuine target failure;
there is no cap-failure outcome to interpret.

The usual one-sided target search has sound failed targets below OPT
and stores an actual successful schedule at each upper endpoint.
At adjacent target-grid points its successful target is at most OPT.
The displayed fixed-target bound is nondecreasing in T, so it gives

\[
                C_{\max}\le
          \max\{\beta(D)\mathrm{OPT}+u,\ a+\lambda_k\}.
\]

The easy branch T>=2a returns at most 3T/2 and is covered because
beta(D)>=3/2. If k>=h, use F0 empty; the constant committed term may
be omitted. If the largest-job Boolean cap has rank below h, every
hard target is genuinely infeasible and OPT>=2a; the easy branch
already gives its stated guarantee. These cases must be separated
when defining lambda_k so that an undefined bottleneck is never
treated as finite.

## 5. Review conclusion

All of (B1)--(B10) pass the review. The exact artificial-quantum
choice makes K/D integral; D>=3-2/k supplies the strict unit-core
condition, and D=3-2/k+eta supplies the claimed relative margin.
The optional minimum with the public polynomial two-approximation
is implemented by returning the better actual schedule. The target
search uses the globally nondecreasing bound max{beta(D)T+u,
a+lambda_k}, so the different easy and hard branches cause no
monotonicity problem.

No counterexample or hidden player/resource coupling was found.
The crucial facts are that contraction acts only on the player
matroid, the full target promise survives on a contracted basis,
zero extension consumes no dual capacity, and original singleton
polymatroid bounds hold after rounding. The result is an unconditional
two-term guarantee in the stated model. It becomes a multiplicative
guarantee of the residual-core coefficient whenever its explicit
committed-machine term is no larger than that coefficient times OPT
(plus the displayed smaller-job rounding term, where present).

This is an internal mathematical audit. It does not claim external
peer review, formal verification, or an exhaustive publication-priority
determination.
