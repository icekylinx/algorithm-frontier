# Independent audit of unrelated-value allocation through joint role LPs

**25 October 2026. Full independent read of J1--J19 and all twelve
sections of `unrelated_values_joint_role_near_two_allocation.md`.**

The complete theorem passes. A resource may serve light and heavy roles
at different players without duplicating its capacity: every node uses
one masked original-resource LP, and every successful witness is rounded
once. The count-prefix invariant supplies the integer heavy units at
that same cost-preserving rounded point. The fixed-witness recursion,
finite target benchmarks, optional-player adapter, and compulsory
two-valued exact-two specialization all close within the stated time
and polynomial-space bounds.

The audit explicitly retains one exact assignment budget, nonnegative
original costs and values, and free disposal. It does not infer an
extension to several independent hard assignment budgets or to
selection setup fees through the ordinary dummy-value construction.

## 1. Masking one original rank preserves shared capacity

For fixed Q, the allowed owner set A_j(Q) contains light-eligible players
inside Q and heavy-eligible players outside Q. The function
f_j^Q(S)=f_j(S intersect A_j(Q)) is normalized, monotone, integral and
submodular. The set intersection map preserves unions and intersections,
so the submodular inequality follows directly from that of f_j.

An independent vector for this masked rank is exactly an original
f_j-independent vector supported on A_j(Q). Forbidden coordinates have
zero singleton rank. Conversely, for an original feasible supported
vector, its count on any S is its count on S intersect A_j(Q), bounded
by that original rank. Thus the characterization holds in both directions.

There is only one column vector and one recipient rank for type j.
Light and heavy owners of that type are coupled by its original subset
constraints. No two independent allocations or rounded copies of that
type are combined. This resolves the capacity-sharing obstacle that
prevented the earlier separate-role proof from using unrelated values.

Deleting zero-valued pairs is safe in this manuscript because all
original assignment costs are nonnegative and resource feasibility is
downward. Keeping whole-unit costs above C in fractional LPs is also
necessary and is correctly done. A fraction of an expensive unit may
still participate in a valid fractional witness.

## 2. The empty-region gate and nonnegative separator are well founded

Forced heavy equalities need not be feasible for an arbitrary Q. The
algorithm first checks X_Q for emptiness, rather than applying a support
oracle to an empty set or presuming a zero allocation satisfies those
equalities.

If X_Q is nonempty, its lower utility projection U_Q contains zero,
because every utility is nonnegative. The same allocation witnesses
any coordinatewise smaller service vector. The region is compact and
convex: counts are bounded by original singleton ranks, and it is a
closed bounded projection of the explicit finite-dimensional rational
allocation polytope. Counts on light players can additionally be
discarded without disturbing forced heavy equalities or increasing cost.

For a nonnegative direction a, maximizing the service support is exactly
the inner LP J9. Its value is nonnegative and at most the stated global
utility bound V when a has total one. Hence the outer LP has a valid
finite h interval. At an optimum, h equals the inner support value.

If a nonnegative query is outside a compact downward region, a strict
signed separator can be replaced by its positive part. Coordinates with
negative coefficients can be set to zero within the region, so this
replacement leaves the support value unchanged and does not decrease
the queried dot product. Normalizing its nonzero positive part then
gives a positive outer objective. This proves the two directions of
the separation test.

The manuscript correctly tests whether the optimum is *nonpositive*
for membership. With a normalized normal, an interior feasible query
may have a strictly negative optimum, so testing equality to zero alone
would be wrong. The Q-empty case does not enter this simplex-normalized
LP: k=q is treated separately, and for k<q recursion keeps |Q|>=q-k>=1.

## 3. Every node has a uniform polynomial rational description

The inner LP has qm count variables, zero-one recipient subset rows,
integer rank right sides bounded by f_j(P), explicit heavy count
equalities with right side one, and one original rational cost row.
Changing Q or the mask changes zero-coordinate restrictions and the
listed heavy equalities; it does not generate recursively growing
numerical coefficients.

The dimension and uniform row encoding imply a uniform polynomial-bit
bound on vertices, including lower-dimensional feasible regions.
Support rows of the outer LP are utility vectors of such vertices,
whose entries are polynomial-bit combinations of original values and
bounded coordinates. Exact inner optimization and exact outer rational
LP therefore provide a polynomial-bit strictly violated row or a
membership decision. Direct reconstruction retains the same joint
cost and resource constraints.

These are fresh bounds from original data, not bounds that depend on
the length of previously generated separator histories. Binary supplies,
quotas, and denominators do not index any expanded table. All paid
optimization primitives have polynomial descriptions at every bad
seed as well as every promised seed.

## 4. One protected allocation survives the changing masks and equalities

Fix a full role witness with light set I* of cardinality s=q-k, and
suppose I* is contained in the current Q. Retain its allocation on
I* and P\Q, and discard its counts on Q\I*. The discarded coordinates
belonged to full-witness heavy players not yet forced heavy at this
node. The retained allocation has only allowed light pairs on I*,
only allowed heavy pairs outside Q, and zero counts elsewhere in Q.

Every player outside Q still receives exactly one fractional heavy
unit. Each original resource count only decreases, and nonnegative
costs ensure the budget remains feasible. Thus the same full light
target t on I* belongs to U_Q. In particular, the empty-X_Q test
cannot reject a node preserving the protected light set.

For a row a*z<=U violated by b*1_Q, the protected full allocation gives
t*a(I*)<=U<b*a(Q). The omitted weight is therefore strictly greater
than (1-b/t)*a(Q)=a(Q)/R. The original weighted prefix argument finds
a certificate contained in Q\I*. At its child the identical original
allocation can be restricted in the same way, proving the invariant
again for the new masks and additional heavy equalities.

No nesting of U_Q under deletion is assumed or needed. At zero remaining
deficit, Q=I* and the original full witness directly supplies the weak
query. The prefix-free branch recurrence and its complete enumerator
depend only on R and the remaining deficit. Uniform node costs therefore
give J13 on promised and unpromised calls, with polynomial space.

## 5. Early success is a valid relaxed output even with fewer heavy players

A successful query serves *every* member of Q at the weak light level,
and forces heavy units only outside Q. If |Q|>s, the returned allocation
has fewer than k heavy recipients. This is permitted by the original
all-player allocation objective.

The exact k is a property of the full-target role witness used for
completeness and for the omission measure. It is not imposed on the
relaxed output. The global cover can attach any s-subset of Q as its
auxiliary selected-set metadata; no light allocations at other members
of Q are deleted. Its correctness proof needs a surviving full witness
and a legal relaxed output, both of which remain available.

In particular, the manuscript does not incorrectly force the extra
Q\I players into a heavy role after an early success. That operation
could lose feasibility or cost. It simply retains the valid joint
allocation already constructed on Q.

## 6. The same integral rounded point satisfies cost and count floors

The count-floor lemma follows from the complete prefix system of the
accepted lower-rounding construction. Apply free disposal first so
each independent resource vector becomes a full extended base without
changing its real counts or cost. Let a_j be the integral singleton
capacity vector and y_j=a_j-x_j its dual base.

For each player's own nonincreasing value order, impose all upper
prefix bounds on y' given by ceilings of the fractional y prefix sums,
including the full prefix. These nested bounds define an integral
prefix-maximum polymatroid; its direct sum over players remains
integral. Intersect it with the direct sum of the dual resource
polymatroids.

The fractional y attains the sum of all resource dual ranks. This is
an upper bound on the total of any feasible intersection point, so
the corresponding maximum-total face is nonempty and integral. Total
equality forces every resource component onto its own dual base face.
Maximizing the original assignment-cost coefficients on y' over this
face minimizes the original complement cost. An integer optimum
therefore has no larger original cost than the fractional point.

For any prefix L, the singleton sum A_L is integral, and

\[
 x'(L)=A_L-y'(L)
 \ge A_L-\lceil A_L-x(L)\rceil
 =\lfloor x(L)\rfloor.
\]

This includes the full prefix, so it preserves at least the floor of
the player's total fractional count. Telescoping nonincreasing values
gives utility loss at most the player's largest eligible value.
Different players may use different value orders because their
prefix constraints act on disjoint player-coordinate groups.

The masks are applied before disposal and dualization. A forbidden
pair has singleton capacity zero, so neither dual completion nor
rounding can reintroduce it. Applying this lemma once to the joint
masked allocation therefore leaves at least one integer heavy unit
outside Q, and at least b-u_L light utility at every player in Q.
Trimming extra heavy units is safe under nonnegative costs and downward
recipient constraints. Both properties hold simultaneously at one
integer resource allocation, with total cost at most C.

## 7. Exact-k zero-role initialization is valid even for fractional promises

The minimum-cost k-heavy-unit gate uses heavy-eligible pair copies,
the direct sum of their Boolean recipient matroids, and the player
partition matroid. It computes the cheapest actual assignment to k
distinct players. Cardinality costs are nondecreasing under trimming.

Suppose a fractional exact-k zero-light role witness exists on some
fixed heavy recipient set F. Each player in F has total heavy count
one, so each type-player coordinate is at most one. These fractional
counts belong to the type Boolean-cap matroid polytopes and the
per-player unit partition polytope. They attain total k. The integral
full-total intersection face consequently has an integer minimum-cost
point of no larger cost. Hence an affordable fractional zero-role
witness implies an affordable actual k-heavy assignment.

This proves that k>nu_C can be skipped without losing a positive
full-target role witness. For k<=nu_C, the actual heavy assignment
and zero counts on its complement supply both a legal zero-valued
initial output and the benchmark's zero-role witness. The initialization
does not assume that arbitrary forced heavy players at later nodes
are affordable; local empty-region checks remain necessary.

For k=q, the light set is empty and its nominal light target would
not be bounded. The manuscript correctly avoids that benchmark and
uses exact all-heavy unit coverage directly. The heavy-empty mask
has only k=0, and a light-empty finite benchmark has only zero light
service unless the separate all-heavy case applies.

## 8. Finite benchmarks, target search, and the approximation close

For a fixed mask and k<q, the exact-role family is fixed before target
search. Its full witness is one joint fractional allocation with a
genuine light recipient set and one-unit heavy roles on its complement.
It is downward in requested light service and has finite upper bound V
because at least one light player is promised. A grid dividing all
original pair values contains every original integer minimum utility.

The external upper point V+g is sound. Only a total gap failure lowers
the upper endpoint, and such a failure excludes the full target for
this fixed benchmark. At adjacent grid endpoints the saved lower target
is at least the benchmark. Early successes need neither have exact
heavy cardinality k nor be feasible at their nominal full target;
their actual weak light service and joint rounded output suffice.

At theta*=alpha*OPT/2, an original integer optimum can be trimmed to
one originally assigned heavy unit per heavy recipient, retaining all
light counts at its small-only players. Original shared-resource
feasibility and cost are preserved by these coordinatewise deletions.
Its role cardinality is among those processed. If k<q, OPT is a grid
target for its joint benchmark, so the saved weak light level is at
least alpha*OPT. Since u_L<theta*<=a_H, the rounded minimum is at
least theta*. If k=q, the affordable all-heavy coverage gives that
same conclusion directly.

Enumerating all pair masks and all affordable k removes any support
promise from the whole-ground theorem. Each forced-omission gap has
the verified interface for the polynomial-space block conversion.
The number of masks, cardinalities, and target queries is polynomial.
No unglobalized raw-corank fallback spoils the stated time.

If only a support cap K is processed, the same reasoning gives the
conditional Gamma(R)^K bound, with unconditional legality of every
returned output. Zero optimum is initialized directly and needs no
threshold convention at zero. Fixed rational accuracy and varying
binary accuracy retain the exact distinction established by the
global-conversion proof.

## 9. The compulsory unrelated two-value exact-two specialization passes

With pair values in {0,u,a}, the shared type masks remain necessary:
a type may supply small units to some players and large units to others.
For u<T<2a, a full allocation supplies K=ceil(T/u) small units on its
small-only set after retaining one a-valued unit at each other player.
The joint count gap uses b=ceil(K/2), whose ratio is at most three.

At success, trim each Q player's fractional small total to b, while
forced heavy totals outside Q remain one. The per-player target d_p
is therefore an integer, equal to b or one. Intersect the direct sum
of the *joint masked* recipient polymatroids with the partition
polymatroid having cap d_p at each player. The supplied fractional
point attains total sum_p d_p. Its integral maximum-total face has
a minimum-cost integer point no dearer than that witness, and total
equality forces all individual quotas. This recovery treats every
shared resource jointly and loses no small unit.

Small utility is bu>=T/2 and heavy utility is a>T/2. Positive targets
at most u use exact one-positive-unit coverage; every full positive
integer allocation can be trimmed to such a coverage. Targets at
least 2a use the fixed all-player fractional LP and cost-preserving
lower rounding, giving T-a>=T/2. The zero target remains the explicit
initialization rather than an infeasible positive-coverage request.

Every full integer target has one affordable actual a-recipient
cardinality, so the complete target procedure has sound failures.
The usual grid search and A=27/4 globalization prove J17. The raw
parameterized bound uses nu_C. No intrinsic-type restriction is
needed in this specialization, because both its LP and its integral
quota recovery retain one original resource rank for all its roles.

## 10. The dual-resource adapter preserves the integer optimum exactly

For an original rank-r matroid M on its q nonloops, the dummy resource
is the dual matroid M*, with common value D=V+g and cost zero. Its
integer counts form an independent indicator set S, not an arbitrary
integer polymatroid count vector with multiplicities.

An original M-basis B extends to a compulsory allocation by putting
one dummy unit on P\B, a dual basis. The dummy value exceeds every
possible original player's utility, so this extension preserves the
original minimum value and budget.

Conversely, for any integer compulsory output, M*-independence of
its actual dummy support S gives

\[
 |S|=r_{M^*}(S)=|S|+r_M(P\setminus S)-r,
\]

so P\S spans M even when S is not a dual basis. Extract an M-basis
inside that dummy-free set. Its players received no dummy utility and
retain at least the compulsory output's minimum from original resources
alone. Discarding other original counts does not increase cost and
preserves every recipient constraint. This proves equality of integer
optima and transfers the actual approximation, not merely a fractional
relaxation comparison.

D has polynomial encoding on the same value grid. Adding one type
does not add any candidate players, so the global exponent remains q.
At the comparator near-half threshold, the canonical extension of an
original optimum has c=q-r dummy heavy recipients plus its K original
heavy recipients. This proves the conditional Gamma(R)^(c+K) bound.

The adapter correctly does not claim to preserve the two-positive-value
specialization: D normally introduces an additional value. It also does
not encode setup fees charged only to selected original players. Those
need a different budget representation and proof.

## 11. Conclusion and maintained boundaries

All J1--J19 claims pass. The new joint role interface repairs the exact
shared-capacity problem that made separate light/heavy allocation
invalid for unrelated values. Empty current regions, exact-k zero-role
initialization, early relaxed success, and the total-count floor are
all addressed explicitly rather than assumed.

The result has the stated deterministic whole-player exponential time,
polynomial space, integer original-resource output, and one exact
assignment budget. The global oracle barriers from intrinsic zero-cost
subclasses remain applicable, without claiming optimality of the new
time base. Multiple hard assignment budgets, naive selected-player
setup charging, and an automatic optional-player exact-two theorem
from the new dummy value remain outside the accepted statement.
