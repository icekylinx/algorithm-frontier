# Verification note

**Curated source path:** `sources/checkpoint-q/unrelated_two_size_scheduling_polymatroid_audit.md`

The source audit follows.

# Independent audit of unrelated two-size scheduling with one exact cost budget

**25 October 2026. Full independent read of
`unrelated_two_size_costed_scheduling_tradeoff.md`, US1--US20.
The stated theorem passes.**

This review rederives the mandatory-count, service-separation and
rounding interfaces. The approximation is constructive, the cost
budget is exact, and the exponential parameter is the number of
physical machines. No intrinsic-value interpretation or ordinary
job-unit expansion is used in the proof.

## 1. Original mandatory totals are the correct invariant

The schedule requires x_j(P)=n_j=f_j(P) for every original type.
Masking a type to a set of eligible pairs replaces its independent
rank by f_j(S intersect A_j), whose full rank is at most n_j.
If the rank drops, the algorithm must reject the masked state; it
cannot replace n_j by that smaller rank.

On the direct-sum product ground, demanding total
N=sum_j n_j enforces all these equalities simultaneously. Every
component total is bounded above by its own n_j, so a full total
cannot compensate for a missing unit in one type by extra units
in another. This observation validates the full-total recovery
primitive, including every masked branch.

A separate initial eligibility mask has the same interpretation.
If it destroys original rank, the original mandatory instance is
infeasible. Otherwise minimum-cost base optimization for each type
and summing the costs gives exact budget feasibility without load
bounds. Independent integer bases are available by integral
polymatroid optimization. A retained feasible schedule has load
at most a*N, whose bit length is polynomial even for binary N.
The empty-job case is handled before any positive-target search.

## 2. The machine caps are integral polymatroids on count coordinates

For one machine, let L be its large-pair coordinates and S its
small-pair coordinates. With integers 0<=h<=c, the constraints
x(L)<=h and x(L union S)<=c are represented by the rank

\[
 r(A)=\max\bigl(\{h:e\in A\cap L\}
                  \cup\{c:e\in A\cap S\}\cup\{0\}\bigr).
\tag{AU1}
\]

The maximum-of-weights function is normalized, monotone and
submodular. Its inequalities are exactly these nested caps:
subsets consisting only of large coordinates have cap h, while
every subset containing a small coordinate has cap c. Empty
groups and h=0 cause no difficulty. Summing AU1 over machines
gives one integral cap polymatroid.

The separate caps on the large and small groups used at a
positive-gap success are an even simpler partition polymatroid.
Different types may be large or small at different machines;
the product ground makes each coordinate belong to exactly one
machine and one of its two groups. Original types are not split
into independent capacity copies.

Intersecting this machine polymatroid with the resource direct
sum is integral. The face of maximum total N is also integral.
The budget row is not claimed to preserve integrality: it is
handled by minimizing actual assignment cost over that full-total
face. A fractional witness with cost at most B then guarantees
an integer point with cost at most B. This distinction is essential
and is maintained throughout US.

## 3. The easy-target upper rounding is simultaneous and cost preserving

For a feasible fractional target-T schedule, let H_p denote the
large count and Z_p the total count at machine p. Since H_p<=Z_p,
their ceilings satisfy ceil(H_p)<=ceil(Z_p), so AU1 applies.
The original fractional schedule fits those integer nested caps
and has total N. Minimum-cost full-total recovery gives one
integer schedule satisfying both caps at every machine.

Its load is bounded by

\[
 u\lceil Z_p\rceil+(a-u)\lceil H_p\rceil
 \le uZ_p+(a-u)H_p+a\le T+a.
\tag{AU2}
\]

All types retain their mandatory totals and the same integral
point preserves the budget. For T>=d*a/(d-1), AU2 is at most
(2-1/d)T. There is no hidden +u term and no need to round a
large allocation separately from a small allocation.

The strict-versus-nonstrict boundary is safe: the manuscript uses
the easy branch at equality, leaving a strictly smaller hard
range. In particular every hard-range integer target schedule
has at most one a-unit at each machine.

## 4. Small-only and small-quota gates are sound on NO instances

If T<a, every target-feasible integer schedule uses only u-pairs.
The small-only mask with integer cap floor(T/u) is therefore an
exact cost-and-load feasibility test via the full-total primitive.
For larger targets a successful small-only schedule is still a
legal early success, while its failure alone is not treated as
full infeasibility.

In the remaining range define C=floor(T/u),
delta=a+Cu-T and K=C-floor((T-a)/u). Directly,

\[
 0<\delta\le a\le T,\qquad
 K=\lceil\delta/u\rceil,\qquad 1\le K\le C.
\tag{AU3}
\]

For K<=d, every full target schedule obeys large count<=1 and
total count<=C. Indeed a large recipient has at most C-K small
units, and 1+C-K<=C. Failure of the minimum-cost integral face
therefore rules out a full target schedule.

At success a large recipient has load at most
T+delta-u. Since delta<=Ku<=du,

\[
 T+\delta-u\le T+(1-1/d)\delta\le(2-1/d)T.
\tag{AU4}
\]

At K=1 this gate is exact for the nominal target; at larger
K<=d it is only a relaxed target success, as US explicitly says.
This does not affect target-search soundness. Processing every
K<=d is what permits the sharper subsequent ratio R_d.

## 5. The spare-capacity region has the required exact separator

At Q, only large pairs outside Q are removed. Small pairs remain
on every physical machine, and all original type equalities
remain in X_Q. Baseline small caps C and the global cost row are
also retained. The initial empty-X_Q test is necessary: the
projection of an empty mandatory-job region must not be treated
as a downward region containing zero.

For nonempty X_Q, spare service z_p obeys 0<=z_p<=C-S_p(x).
Thus U_Q is compact, convex and downward, and contains zero.
For a>=0 its support is exactly

\[
              h_Q(a)=C\sum_{p\in Q}a_p
                         -\min_{x\in X_Q}\sum_{p\in Q}a_p S_p(x).
\tag{AU5}
\]

The negative coefficients in the equivalent maximization form
are not negative coefficients in a packing separator. The support
is nonnegative because a nonempty X_Q satisfies every baseline
small cap. A normalized support-gap LP produces a valid row with
nonnegative normal and nonnegative capacity. A positive optimum
strictly separates the query; a nonpositive optimum establishes
membership through the positive-part separator argument for a
downward region.

Every type inequality has zero-one coefficients and an encoded
rank right side. The remaining rows are original base totals,
count caps and one rational cost row. Exact extreme optimizers
and their spare vectors have uniform polynomial bit length by
active-row determinant bounds. The nested support LP therefore
supplies polynomial-bit rows. Direct feasibility reconstructs
the successful joint schedule. Nonempty Q is ensured by the
fixed-k branch k>=1; the empty promised-large-set case is handled
by the small-only gate.

## 6. The protected witness preserves every job, without deletion

Fix an actual full target-T schedule and its exact large-recipient
set I*. At a node Q containing I*, every forbidden large pair was
unused by that schedule. The whole original schedule remains
feasible, with all resource vectors, costs and type totals
unchanged. In particular no nonnegative-cost disposal argument
is used to justify preservation of mandatory jobs.

For p in I*, the small count is at most C-K, so
K*1_(I*) belongs to the current U_Q. If a row a*z<=w rejects
b*1_Q, where b=ceil(K/d), then

\[
        K a(I^*)\le w<b a(Q),\qquad
        a(Q\setminus I^*)>(1-b/K)a(Q).
\tag{AU6}
\]

For every K>=d+1 the quota arithmetic gives
K/(K-b)<=(d+1)/(d-1). The weighted first-crossing certificates
therefore include a deletion inside Q\\I*. Recompute the masks
and service region at the child; the same complete schedule
again proves preservation. At zero deficit Q=I*, the weak query
is feasible. Empty-region gates cannot reject a protected node.

This argument uses a changing region correctly. It does not need
the old separator to remain a complete description of the new
region, or the output large-recipient set to equal I*.

## 7. Recovery at success retains all original types and the actual output

A successful weak query has integer caps large<=1 and
small<=C-b on Q, and large=0 and small<=C outside Q. Their
nonnegativity follows from b<=K<=C. The successful fractional
point lies in the resource/machine intersection at total N.
Minimum-cost full-total recovery therefore returns an integer
schedule with every original type total n_j and cost at most B.

For a large recipient inside Q,

\[
 a+u(C-b)=T+\delta-bu
       \le T+(1-1/d)\delta\le(2-1/d)T,
\tag{AU7}
\]

because bu>=Ku/d>=delta/d. Other machines have only a smaller
load. No machine or real count is discarded after this recovery.

An early success may place large units on more or fewer machines
than the protected cardinality k. This is legal in the scheduling
problem. The global wrapper's auxiliary k-subset metadata must
not be used to delete the other returned machine assignments;
the manuscript explicitly retains the full recovered schedule.

## 8. One-sided minimization and the whole-machine exponent

The complete target routine covers every full target schedule:
the high branch, the small-only case, the small-K gate, and then
all possible exact positive large-recipient cardinalities k.
Therefore failure implies OPT>T, while success promises only an
actual schedule of makespan at most rho_d*T.

For N>0, target zero is false because every job unit has positive
processing time. The initial upper target a*N is a grid number
and has a saved budget-feasible schedule. If the lower failed
endpoint is L, then L<OPT persists. At adjacent g-grid endpoints
the saved upper nominal target is L+g<=OPT, since integer OPT
lies on the same grid. Its saved schedule therefore has the
claimed ratio. Weak successes need not be monotone or full
feasibility certificates. O(log(a*N/g+2)) calls have polynomial
bit complexity.

For a fixed k and forced omission seed Z, the remaining deficit
is q-k-|Z|. The full all-input weighted certificate bound pays
for failed masks, empty regions, cost gates and all branches.
The global cover applies separately for each k, preserving a
seed inside P\\I*. Summing over q cardinalities and polynomially
many target calls changes only the polynomial factor. Binary
job multiplicities never become elements of the branch ground.

For fixed d the exact constant is
2-1/Gamma((d+1)/(d-1)); the manuscript correctly distinguishes
this from the safe rational 3R_d upper bound for varying binary
d. Depth-first recursion, streamed covers and polynomial-size
count tables give polynomial workspace.

## 9. The inherited oracle barrier has the right scope

Section 5 of `recipient_polymatroid_below_two_oracle_barrier.md`
uses an ordinary uniform large-job matroid of unit size two and
an arbitrary small-job polymatroid of unit size one. A schedule
of makespan strictly below three identifies its hidden set when
OPT=2. On balanced rank, the binomial query requirement is
2^(q-O(log q)). This is an intrinsic zero-cost subclass of US,
so the below-three-halves oracle barrier transfers.

It does not prove that the base 50/27 is optimal at exact factor
three halves. It is not an explicit ordinary-job hardness claim,
and it is not a lower bound for a prescribed relaxed quota with
the boundary factor already allowed.

## 10. Bounded primary-source comparison

The following comparisons are about the stated source versions
and their actual models, not an exhaustive claim of priority.

* Shmoys and Tardos,
  [*An approximation algorithm for the generalized assignment
  problem* (1993)](https://www.cs.cornell.edu/~eva/Approx.Algorithm.Generalized.Assignment.Prob.pdf),
  Theorem 2.1, give ordinary unrelated-job rounding with exact
  cost and additive maximum supported processing time. Their
  following remark also treats integer job multiplicities in
  polynomial time by fixing the integral parts of fractional
  assignments and rounding fewer than m*n residual units. Thus
  ordinary multiplicity compression and exact-cost additive
  upper rounding are established background.

* Bamas et al.,
  [*Santa Claus meets Makespan and Matroids* (arXiv:2307.08453v1)](https://arxiv.org/html/2307.08453v1),
  Theorem 2, relate two-value allocation factor alpha to
  scheduling factor 2-1/alpha. Their Appendix C.1 constructs
  one allocation player for each original machine and each
  original job, plus bounded machine slots. Applying a
  player-exponential routine to that displayed construction
  therefore does not by itself give a physical-machine-only
  exponent. Corollary 5 concerns intrinsic restricted
  job-matroid scheduling, while Corollary 6 concerns ordinary
  two-value unrelated scheduling. Those statements should not
  be relabeled as the exact-cost binary polymatroid theorem US.

* Huang and Ott,
  [*A Combinatorial Approximation Algorithm for Graph Balancing
  with Light Hyper Edges*](https://arxiv.org/abs/1507.07396),
  give a constructive three-halves result for intrinsic two-size
  restricted assignment when each heavy job has at most two
  allowed machines. Thus three halves for every ordinary
  two-size subcase is not new. The restriction on heavy-job
  eligibility and the absence of the present arbitrary
  polymatroid/cost interface matter.

* Kolliopoulos and Moysoglou,
  [*The 2-valued case of makespan minimization with assignment
  constraints*](https://arxiv.org/abs/1212.1609),
  use intrinsic job sizes on their allowed machines and state
  an approximation to the value of the optimum. A numerical
  estimation result must not be advertised as an algorithm
  producing the schedule required here.

The direct proof's relevant scope is the joint original recipient
polymatroids, pair-dependent size classes, exact mandatory totals
and budget, and exponent on physical machines. It does not
improve the public general-purpose additive rounding primitive.

## 11. Verdict

All US1--US20 statements pass this independent review. No
substantive correction is requested. The current theorem covers
nonnegative assignment costs as stated. The proof also suggests
that a separately stated signed-cost extension would be possible,
because no mandatory assignment is discarded and all cost
optimizations occur on bounded full-total faces; that observation
is not needed to accept or silently broaden the present theorem.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
