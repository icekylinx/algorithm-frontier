# Integer-quota time tradeoffs for compulsory unrelated two-value allocation

**25 October 2026. Corollary of the reviewed joint-role and integer-quota
manuscripts; root and independent full read requested.**

The factor-d quota tradeoff does not require intrinsic resource values
when all players are compulsory and every pair value is in {0,u,a}.
The joint-role LP and its single heterogeneous-quota recovery handle
types whose units have value u to some players and a to others.
In particular, factor three has whole-player time
`(7/4)^(q+o(q)) poly(H)` and polynomial space, preserving one arbitrary
assignment-cost budget exactly.

## 1. Model and constants

There are q>=1 compulsory players, integral recipient-polymatroid
resources f_j, and nonnegative rational per-unit assignment costs c_pj.
Unused units are allowed. Every pair value v_pj belongs to {0,u,a},
where 0<u<a. One total assignment-cost budget C>=0 is exact. The
integer objective is the minimum utility of all q players.

Zero-value pairs can be dropped. If no positive value remains, return
zero. If only one positive value remains, the fixed-player instance
is solved exactly by minimum-cost uniform-quota polymatroid
intersection and integer quota search. Assume both values occur
for the displayed two-value procedure.

Let nu_C be the largest number of distinct players who can receive one
a-valued unit each with total cost at most C. This is computed by
minimum-cost cardinality-k intersection of the direct sum of the
heavy-pair Boolean recipient matroids and the partition matroid
allowing one pair per player. It is only an upper bound on possible
heavy support; the algorithm does not enlarge an optimum's support.

For a fixed integer d>=2 put

\[
 R_d=\frac{d+1}{d-1},\qquad
 A_d=\Gamma(R_d),\qquad B_d=2-1/A_d,
      \qquad\Gamma(R)=\frac{R^R}{(R-1)^{R-1}}.
 \tag{UQ1}
\]

**Theorem UQ.** A deterministic algorithm returns an integer allocation
of value at least OPT/d and actual cost at most C, in either

\[
 A_d^{\nu_C}\operatorname{poly}(H)
 \quad\text{or}\quad
 B_d^q\,2^{O(q\log\log(q+2)/\log(q+2))}\operatorname{poly}(H),
 \tag{UQ2}
\]

using polynomial workspace. H counts all original numerical bits and
the paid polynomial oracle work. No binary resource supply is expanded.

## 2. The full target procedure

Fix a positive rational target T. We either return value at least T/d
or exclude every integer full-T allocation.

If

\[
                              T\ge\frac d{d-1}a,
 \tag{UQ3}
\]

solve the original full-player fractional allocation LP at utility T,
retaining all shared original resource constraints and the exact
assignment budget. Infeasibility excludes the integer full target.
A feasible LP is rounded once by the accepted cost-preserving lower
rounding; the largest possible positive unit value is a. Its returned
utility is at least T-a>=T/d. This is a polynomial branch.

Otherwise put K=ceil(T/u). If K<=d, use exact minimum-cost one-positive-
unit coverage of all q players. Any integer allocation with positive
minimum utility can be trimmed to one positive unit per player without
increasing cost. Failure therefore excludes the full target. Success
gives each player value at least u>=T/d. The same exact coverage gate
is used for every 1<=K<=d; it is not a claim of full-K feasibility.

The remaining case has K>=d+1 and T<d*a/(d-1)<=d*a. Define

\[
                                b=\lceil K/d\rceil.
 \tag{UQ4}
\]

For K=jd+s, with j>=1 and 1<=s<=d, one has b=j+1 and

\[
              \frac K{K-b}
              =\frac{jd+s}{j(d-1)+s-1}
              \le\frac{d+1}{d-1}=R_d.
 \tag{UQ5}
\]

The last bound is attained at K=d+1. This is the quota calculation
proved in `integer_quota_approximation_time_tradeoffs.md`.

## 3. The joint count gap uses the original shared resources

Treat u-valued pairs as light and a-valued pairs as heavy. Enumerate
every possible exact promised heavy cardinality k<=nu_C. When k<q,
use the joint region of
`unrelated_values_joint_role_near_two_allocation.md`: at an allowed
light ground Q, all pairs are masked so Q may use only u-pairs,
while P\Q may use only a-pairs and has exactly one fractional unit
at each such player. Every original type retains a single rank
constraint on all these counts, and the original cost budget is
enforced once.

The projected service coordinate on Q is its light count. First test
the joint polytope for emptiness. For a nonempty polytope it is a
compact downward service region, and its support LP supplies the
same exact nonnegative packing separator. Query weak count b on
every member of Q, with full promise K on a protected (q-k)-set I*.

A target-T integer allocation supplies that promise: retain one
original a-unit at every player who originally received any, and
retain the original u-counts at every remaining player. A small-only
player has at least K such units. At a recursive Q containing I*,
discard retained heavy counts at players in Q\I* and keep the
original counts on I* and P\Q. The joint masks, forced count-one
equalities, original resource capacities and budget all hold.

Thus every violated row still protects I*. The weighted first-crossing
recursion, with UQ5, has all-input time at most
`A_d^(k-|Z|) poly(H)` after any forced omitted seed Z contained in
the promised heavy set. The full promised set has exactly q-k
light players, although an early relaxed success may have fewer
than k heavy players. The returned original allocation is still legal.

At success, trim the fractional light count at each p in Q to exactly
b, and retain forced heavy total one. These are integer per-player
quotas. Minimum-cost integral polymatroid intersection of the single
joint masked resource product with the per-player quota-cap
polymatroid, on its maximum-total face, recovers those exact quotas
at no larger cost. Every resource is recovered once. Consequently
light players receive bu>=T/d and heavy players receive a>T/d.
There is no largest-unit loss in this branch.

For k=q, test the all-heavy one-unit cover directly; do not introduce
a light-service benchmark for an empty light set. If every applicable
k fails, the full integer target is impossible because its actual
heavy support would have supplied one of the protected witnesses.

## 4. Optimization and the two time bounds

Choose a rational g dividing u and a. Every integer utility, and
therefore OPT, lies on its grid. A uniform bound on each original
player's possible utility is
`V=sum_j(max_p v_pj) f_j(P)`, which is a g-grid number. Initialize
the zero allocation and use external upper target V+g.

One-sided grid maximization saves actual weak allocations on success
and lowers the upper endpoint only on full-target failure. At adjacent
endpoints the saved nominal lower target is at least OPT, so its
recorded allocation has value at least OPT/d. Successes need not be
monotone or certify their full nominal targets. This is polynomially
many target calls in binary encoding length.

The support loop has only q+1 choices. UQ5 bounds every positive-gap
call by A_d^nu_C times a polynomial; the exact coverage and high-target
branches are polynomial. This proves the first time bound.

For the second, apply the accepted polynomial-space global inclusion
cover separately to each exact promised k and target. Its forced
omissions restrict only current light candidacy; the joint LP continues
to retain every original player and resource, with forced-heavy masks
outside Q. A seed inside the original heavy complement preserves the
full witness. The extension budget is k-|Z| and its uniform base is
A_d, proving the whole-q bound in UQ2. No approximation is applied
repeatedly across blocks, and no raw A_d^q fallback is run.

## 5. Numerical consequences and scope

The first tradeoffs are:

| Allocation factor d | Positive-gap ratio R_d | Whole-ground base B_d |
| --- | --- | --- |
| 2 | 3 | 50/27, approximately 1.851852 |
| 3 | 2 | 7/4=1.75 |
| 4 | 5/3 | Approximately 1.674270 |
| 5 | 3/2 | Approximately 1.615100 |

For fixed d, the exact algebraic Gamma constant is handled by the
fixed-rational comparison rule proved in the global conversion note.
Its polynomial space and the binary count implementation carry over.
The displayed sharp bases are fixed-d statements.

This corollary strengthens the scope of QT's compulsory two-value
allocation theorem: the same original resource type may provide
different positive values to different recipients. It relies on J's
joint-role LP and joint quota recovery, not on treating type classes
as independent. One exact assignment budget is retained.

Optional original matroid selection is not added to this exact-d
two-value corollary through the dummy reduction: its dummy value can
introduce a third positive value. The general unrelated near-two
theorem already supports that selection model with its separately
proved time guarantee. No unrelated-machine scheduling theorem follows
from the present allocation argument.

The base transformation is existing monotone-local-search background,
as sourced in the global conversion manuscript. The quota inequality
is QT4 and the shared-resource interface is J6--J18 of the cited
internal proofs. This note records their direct composition, without
an exhaustive priority claim or external-verification claim.
