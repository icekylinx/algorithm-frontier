# Independent audit of the joint-role unrelated-value allocation theorem

**25 October 2026. Complete independent mathematical read of J1--J19: passes.**

This is the allocation-four review of
`unrelated_values_joint_role_near_two_allocation.md`. The separate
polymatroid-transfer review is preserved in
`unrelated_values_joint_role_second_audit.md`. This file covers the full
compulsory-player theorem, unrelated two-value exact-two specialization,
and optional original-player-matroid adapter. No substantive correction
is required.

## 1. A masked rank represents one original resource

For each type j, the allowed set A_j(Q) contains its light pairs at Q
and heavy pairs outside Q. The rank f_j^Q(S)=f_j(S intersect A_j(Q))
is normalized, monotone, integral and submodular. Its independent
vectors are exactly original feasible vectors with zero forbidden
coordinates. For a supported original vector,
x_j(S)=x_j(S intersect A_j(Q))<=f_j(S intersect A_j(Q)); conversely
the masked constraints imply original feasibility and zero forbidden
singletons.

Thus a type serving both roles is constrained once. The construction
does not duplicate capacity into separate light and heavy resources.
This exact representation is retained in every feasibility, support
and rounding operation.

## 2. Empty regions and downward service

The forced count-one equalities outside Q may be infeasible or
unaffordable. The explicit empty-X_Q gate is therefore necessary and
correctly included. When X_Q is nonempty, the lower light-service
projection contains zero and is compact, convex and downward. Dropping
light counts leaves the forced heavy counts unchanged and cannot raise
cost. The changing regions need not be nested, and no proof step
assumes that they are.

The empty-Q case is handled by all-heavy coverage, so the outer LP
never asks for a normal summing to one on an empty coordinate set.
Unused resource capacity is permitted, which justifies every disposal
and restriction operation.

## 3. Exact separation and uniform encoding

The inner support LP has polynomial dimension, original masked rank
separation through submodular minimization, explicit heavy equalities,
and one assignment budget. An extreme optimal support allocation can
be chosen by exact lexicographic refinement. Its polynomial-bit bound
follows from Cramer's rule in polynomial dimension: rank rows have
zero-one coefficients and encoded integer right sides, heavy equalities
have right side one, and values and costs retain their input encodings.
The number of possible rank subsets does not affect a vertex determinant.

The outer support LP therefore has polynomial-bit separating rows.
Compact downward service regions admit nonnegative separators for
nonnegative outside points: discard negative normal entries, preserve
the support using downward closure, and normalize the remaining
nonzero normal. A positive optimum supplies a strictly violated row;
a nonpositive optimum proves membership. The manuscript correctly
uses nonpositive, since an interior feasible query can give a negative
normalized support objective.

Reconstruction uses the corresponding joint feasibility LP. All these
bounds are uniform over masks, Q and target values. No numerical
resource units or denominators are enumerated.

## 4. One original full allocation survives every protected node

Fix a full witness with exact heavy cardinality k and light set I*
of size q-k. At a node Q containing I*, retain its original allocation
on I* and outside Q and drop the counts on Q\I*. Those dropped players
were heavy in the original witness but have not yet been forced heavy.
Every retained count now obeys the current role masks, every forced
heavy player still has total count one, and capacities and nonnegative
cost only decrease. Consequently t*1_(I*) belongs to the current U_Q.

The empty-region gate cannot reject this node. If a nonnegative row
is violated at the weak all-Q query, then

\[
 t a(I^*)\le U<b a(Q),\qquad
 a(Q\setminus I^*)>(1-b/t)a(Q).
\]

The first-crossing omission routine has an enumerated branch inside
Q\I*. The same original full allocation supplies the invariant again
after this deletion. At zero remaining deficit Q=I*, so its stronger
service implies weak-query membership directly.

This is a per-node protected-witness proof for changing joint regions.
It does not assert that a signed joint selection projection is an
ordinary fixed downward packing polytope.

## 5. All-input time and exact-cardinality global seeds

All feasibility, separator and reconstruction work is uniformly
polynomial. The prefix-free count depends only on R and remaining
deficit |Q|-(q-k), independent of the current masks. Therefore every
execution, including all failed and unpromised calls, costs
Gamma(R)^(k-|Z|) times a polynomial after a forced seed Z.

If Z lies in the original heavy set, its forced heavy roles retain the
same witness. The global block wrapper is applied separately to every
exact promised k. This avoids the invalid inference that a cover for
size-K omitted sets must also hit a witness with fewer than K heavy
players.

An early relaxed success may use fewer than k heavy roles. It is still
a legal original compulsory allocation. Recording an arbitrary
(q-k)-subset of its actual light set as wrapper metadata changes none
of the allocations or their utilities; no extra player is declared
served merely by that metadata.

The recursion, local certificate generation and streamed global cover
use polynomial space. The explicit q-player ground is preserved.

## 6. Count floors and cost hold at the same integer point

Free disposal is applied to the masked ranks before forming complement
bases y_j=a_j-x_j. The per-player prefix-ceiling polymatroid includes
all type prefixes, including the full prefix. On its intersection with
the dual resource direct sum, a maximum-total face saturates every
resource component. Maximizing actual assignment-cost coefficients at
an integer point of this face makes the complementary allocation cost
no more than the original fractional witness.

For each prefix L, A_L=sum_(j in L)a_j(p) is integral, and therefore

\[
 x'_p(L)\ge A_L-\lceil A_L-x_p(L)\rceil
                  =\lfloor x_p(L)\rfloor.
\]

This count inequality and the cost inequality hold at the same point.
Telescoping each player's own decreasing value order gives the usual
largest-unit utility loss. Different value orders at different players
are valid because the prefix polymatroid is a direct sum over players.

Every forced heavy player had total fractional count exactly one, so
the full prefix retains at least one integer unit. Every retained unit
is on a heavy pair because forbidden coordinates were masked before
rounding. Keep any one heavy unit and discard the rest. Nonnegative
costs and downward capacities make this safe. Light players retain at
least b-u_L utility, while heavy players retain at least a_H. The final
minimum is therefore at least min{a_H,b-u_L}, at cost at most C.

The additive utility inequality alone would not suffice for heavy
players when their possible values differ greatly. The total-count
floor is the precise extra fact closing that issue.

## 7. Affordable supports and finite target benchmarks

One heavy unit on exactly k distinct recipients is optimized by weighted
intersection of the direct sum of heavy Boolean resource matroids and
the player partition matroid. Nonnegative costs make minimum cost
nondecreasing with cardinality, giving nu_C and exact-k zero-light
witnesses. A fractional zero-light witness on a fixed heavy set can be
made integral at no higher cost on the one-unit maximum-total face.
Thus skipping k>nu_C cannot discard a positive full role witness.

For k<q, at least one light player is promised, so the fixed exact-k
benchmark is bounded by V and downward in the light target. A common
rational grid g divides all original pair values, including integer
OPT and the chosen V. The external upper endpoint V+g is valid without
being queried. Every failure excludes the full benchmark target.
One-sided maximization consequently ends with a saved lower target at
least the benchmark, even if weak successes are nonmonotone or use
fewer heavy players.

For k=q a light-service benchmark would be unbounded. Direct all-heavy
coverage is correctly used instead. Empty classes, zero optimum and
empty positive-value data have explicit legal zero or one-unit gates.
No threshold at zero is required for the zero-optimum guarantee.

## 8. Approximation and unconditional global time

At theta*=alpha*OPT/2, one enumerated pair mask has
u_L<theta*<=a_H, with equality assigned heavy. An integer optimum can
be trimmed to one original heavy unit on every heavy recipient and
its original light utility only on the other players. This is a joint
full witness at target OPT for its actual exact k, without increasing
cost or capacity use.

If light players remain, the benchmark is at least OPT and the saved
weak light target is at least alpha*OPT. Rounding leaves those players
strictly above theta* and heavy players at least theta*. The pure-heavy
gate gives the same conclusion when k=q.

Polynomially many masks, cardinalities and target calls preserve the
stated global base 2-1/Gamma(R), explicit subexponential overhead and
polynomial space. Every global call uses the same full and relaxed
targets once. Fixed-rational Gamma comparisons and the varying-input
rational fallback are correctly separated. No slower raw-corank
fallback is included in the advertised unconditional algorithm.

## 9. Unrelated two-value exact two uses one joint quota face

For pair values in {0,u,a} and u<T<2a, set K=ceil(T/u) and
b=ceil(K/2). The original integer target supplies K small units on
its small-only players and one retained a-unit on every other player.
The same joint protected-witness proof applies to count service, with
K/(K-b)<=3.

At success, trim each light total to b and retain the forced heavy
total one. These heterogeneous integer quotas define a partition
polymatroid. The masked original resource direct sum intersects it
in a nonempty maximum-total face of total sum_p d_p. This face is
integral; a minimum-cost integer point has no greater cost, and total
equality forces every quota exactly. Thus light utility is bu>=T/2
and heavy utility is a>T/2, without an additive loss or a resource split.

For T<=u, exact one-positive-unit coverage is a sound gate and returns
at least T. For T>=2a, one original joint LP followed by cost-preserving
lower rounding returns at least T-a>=T/2. Equality at both boundaries
is handled correctly. Trying every affordable actual heavy support
makes total failure a full original-target certificate. The grid search
then yields exact factor two with parameter base27/4 or global base50/27.
A missing positive value class is solved by exact compulsory one-value
quota intersection.

## 10. The dummy adapter extracts a genuine original basis

After loop deletion, add a zero-cost resource of value D=V+g and
recipient matroid M*. Any original M-basis B extends to a compulsory
allocation by one dummy on its complement, a dual basis. D exceeds
any original possible player utility, so the minimum is preserved.

In the reverse direction, the actual dummy support S of an integer
output is M*-independent. The matroid singleton caps prevent multiple
dummy units at one player. The dual rank identity gives
r_M(P\S)=r_M(P), so an original M-basis can be found entirely among
dummy-free players. Their utility uses original resources alone.
Deleting other counts and the dummy cannot raise nonnegative cost.
This proves equality of the integer optima and preserves the
approximation guarantee.

Only the integer rounded support is used for basis extraction; a
fractional dummy support need not identify a basis and is never used
that way. The player ground stays q, the rank oracle is polynomial,
and D has polynomial encoding. The canonical extension has c dummy
recipients plus the original optimum's K heavy recipients at the true
threshold, giving Gamma(R)^(c+K).

The adapter does not automatically transfer the two-value exact-two
statement, since the dummy can introduce a third value. It also does
not prove a selected-player setup-fee extension.

## 11. Disposition and boundaries

The complete J1--J19 chain passes. The intrinsic-value restriction is
removed by one masked joint LP and one count-floor, exact-cost integer
recovery. Optional players are recovered as an actual original basis,
not as a mixture of bases.

The theorem retains one scalar assignment budget, arbitrary nonnegative
pair values and costs, binary integral recipient polymatroids, and its
explicit q-player ground. Multiple independent assignment budgets and
an optimal exponential base are not claimed. Public monotone-local-
search conversion and additive rounding remain separately attributed.
This internal review is not formal verification or an exhaustive
publication-priority claim.
