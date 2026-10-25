# Independent audit of type-symmetric binary allocation

**25 October 2026. Independent mathematical and representation audit.**

This audit checks type_symmetric_downward_closed_binary_allocation.md.
The symmetry lift, compressed physical state, exact local polymatroid
oracle, and bounded-knapsack adapter pass. The earlier binary-cell,
player-local, and approximate-oracle analyses are imported only after
checking that their hypotheses survive the count-vector model.

## 1. The perspective condition lifts the whole local family

For x_p>0, the vector y_p/x_p belongs to conv(F_p). Take any
convex decomposition into feasible integral count vectors. Conditional
on one vector n, choose a uniformly random n_j-subset of the c_j
conceptual copies of each type. This is a proof construction, not an
algorithmic sampling step.

Type symmetry makes every chosen physical set feasible for p.
Its per-copy conditional marginal is n_j/c_j, so the resulting
unconditional marginal is y_pj/c_j. Summed over players, each
conceptual copy has usage at most one. A zero-supply type has
only a zero coordinate.

For any fixed physical forbidden set F, restrict each chosen set
to the actual remaining copies. Downward closure keeps it in the
local family. Its count vector is bounded by the actual availability
A, so its value is bounded by the true available optimum.

The uniform marginals imply that its fractional outside value is
exactly sum_j v_j A_j y_pj/c_j, for every F of those available
counts. No independence assumption about F and the history is used.
If a completed unchanged-state lambda-oracle scan returns below B,
the strict bound is consequently (B/lambda)x_p for every positive
eligible player mass.

Separate coordinate quotas would not justify this proof for a
general local family; the full perspective membership is essential
and is stated in the manuscript.

## 2. The cell implementation does not break local feasibility

An oracle returns an integral type-count vector. Selecting those
counts from arbitrary available matching-owner cells is valid
precisely because unit identities of a type are interchangeable
for the player. The existing exact cell partition still represents
a history in one fixed conceptual unit universe.

Minimalization deletes units in type batches. Every deletion is
coordinatewise downward, preserving the local family; after the
single pruning pass every remaining unit is individually essential
to reaching B. No chunk or aggregate-type value replaces its
original unit value in the star bound.

The old matching-row and selected-column operations need no new
resource-copy expansion. In particular, undiscovered matching rows
remain available, and an old stored free column is saved or inserted
into the matching before its selected label is retired. Lower
forbidden sets and maximality remain the same fixed physical sets.

## 3. Box restriction really is an integral polymatroid

For an integral monotone submodular rank function f and availability
A, define

g_A(S)=min_(Q subseteq S) [f(Q)+A(S minus Q)].

Normalization and integrality are immediate. For monotonicity,
restrict a minimizing Q for a larger set to the smaller set;
monotonicity of f and nonnegativity of A give the required bound.

For submodularity, take minimizers Q_1 subseteq S_1 and
Q_2 subseteq S_2. Uncross f by Q_1 union Q_2 and
Q_1 intersection Q_2. The modular terms obey the exact identity

A(S_1 minus Q_1)+A(S_2 minus Q_2)
 =
A((S_1 union S_2) minus (Q_1 union Q_2))
 + A((S_1 intersection S_2) minus (Q_1 intersection Q_2)).

The resulting union/intersection candidates prove submodularity
of g_A.

If z is in P(f) and z<=A, splitting each z(S) over Q and S minus Q
proves z(S)<=g_A(S). Conversely Q=S gives the original rank
bounds, while Q=empty on a singleton gives z_j<=A_j. Therefore

P(g_A)=P(f) intersection [0,A].

This argument applies to nonnegative real vectors as well as
integer vectors.

Sorting the positive profits and taking successive g_A prefix
increments produces a nonnegative integral vector. Submodularity
proves every subset constraint, and summation by parts proves
optimality because all profit-prefix rank bounds are attained.
Thus the returned vector is an exact available count vector.

Each of at most t prefix values is a submodular minimization of
f(Q)-A(Q) restricted to that prefix. This is a deterministic
polynomial oracle implementation with the declared value-encoding
cost, using the primary submodular-minimization results cited by
the manuscript. No expanded unit ground set is used.

## 4. Binary chunks stay inside the knapsack oracle

A bounded integer count can be represented by O(log(c_j+1))
chunks whose subset sums cover every count from zero to the bound.
The chunk sizes sum to the bound and each next size is at most
one plus the sum of previous sizes, including the final remainder.

With nonnegative costs, any chunk representation of a feasible
count vector has no individually infeasible chosen chunk: each
chosen cost is at most the total feasible cost. Removing
individually infeasible chunks therefore loses no feasible vector.

The profit-scaling knapsack routine is applied to these polynomially
many encoded chunks. Its output is converted back into an ordinary
count vector before the allocation algorithm sees it. Subsequent
unit pruning may split a chunk; that is legitimate in the original
downward-closed count model.

The star parameter remains the largest unit profit, not the
possibly much larger profit of a chunk. This distinction is needed
for the claimed approximation denominator and is explicitly kept.

## 5. Fat resources, numerical boundary, and verdict

Fat-service feasibility is equivalent to e_j in F_p. A positive
factor feasible oracle on the singleton availability vector decides
this exactly: its value must be positive if the singleton is
feasible, and no other positive vector is possible.

This test must skip zero-supply types, since e_j is then outside
the oracle's declared domain A<=c. Such types can simply be
removed initially. The largest unit value is zero when no
positive-supply type remains.

Capacitated fat matching uses capacities min(c_j,q), so it does not
expand supplies. Downward closure makes every fat singleton used by
a configuration feasible, and scaling all-small configuration rows
preserves both the local perspective condition and global capacities.
The paid fat-union wrapper and its configuration comparator
therefore apply.

Target search starts above the returned-value ratio times total
possible resource value; it does not assume that success at a target
certifies feasibility of that target. All count arithmetic and the
common value grid have polynomial encoding length.

Subject to the explicit zero-supply convention, the manuscript passes
this independent audit. It concerns player-local type-count families.
It does not convert arbitrary resource-side polymatroids on
receiving-player vectors into this model, and it does not assert a
new public approximation record without the separate same-model
comparison.

