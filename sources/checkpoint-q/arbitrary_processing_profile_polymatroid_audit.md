# Independent polymatroid audit of the arbitrary-processing profile scheme

**25 October 2026. Full independent read of PS1–PS19 and all thirteen
sections of `arbitrary_processing_profile_approximation_scheme.md`.
Result: the stated theorem passes; no substantive correction requested.**

This review is independent of the author and of the separate Frontier
review. It checks the complete algorithm, including unsuccessful
targets, exact budget recovery, numerical encoding, zero optimum, and
the stronger partition bound. It is a mathematical audit, not formal
verification or a publication-priority assessment.

## 1. The theorem being accepted

There are q physical machines and integral recipient polymatroids f_j.
Every original count n_j=f_j(P) is mandatory, even after eligibility or
target masks. Processing times and nonnegative assignment costs may
depend arbitrarily on both machine and type. Supplies and ranks are
binary encoded. One assignment-cost budget must hold exactly.

For a supplied rational 0<epsilon<=1, the manuscript gives a
deterministic (1+epsilon)-approximation in

    2^{O(q/epsilon)} poly(H+size(epsilon))

time and polynomial space in the full binary encoding. It first
detects infeasibility of the original budget-feasible family. This is
a whole-machine-ground result, with no low-corank, heavy-support, or
bounded-number-of-processing-values promise.

The two displayed finite time bounds apply to the same streamed
algorithm. They are not obtained by pretending that a large bin
universe, a partition table, or the resource units have polynomial
size. No multiple-budget, optional-machine, or robust-scenario claim
is being accepted here.

## 2. Original totals and the exact-cost integer recovery

Let E be the explicit machine-type coordinate ground and let R be
the direct sum of the masked recipient polymatroids. On every type,
available rank is at most its original n_j. Consequently

    x(E)=N=sum_j n_j

inside P(R) forces x_j(P)=n_j for every j. This argument continues
to hold after arbitrary pair deletions. If a mask loses rank, keeping
the old N makes the face infeasible; the algorithm does not redefine
the supply to be the smaller masked rank.

The recovered machine constraints form another integral polymatroid
K on the same coordinate ground. If a fractional witness x lies in
P(R) intersect P(K) and has total N, the intersection contains a
nonempty full-total face. The intersection is integral, and total N
is a maximum-total face because R already bounds total count by N.
Thus that face is integral as well.

Minimizing the one actual assignment-cost objective on this face
has an integral optimum no more expensive than x. This is the precise
reason the budget is preserved. It does not assert integrality after
adding a cost inequality to an arbitrary integral polytope. It also
does not optimize different costs in separate recoveries.

All resource and machine constraints act on the same coordinates.
A type that is big on one machine and small on another still has one
recipient polymatroid. No extra independent copy of its capacity is
introduced.

## 3. The upper-prefix rank is correct, including zero times

For one small group, order its coordinates by decreasing nonnegative
time v_1,...,v_m and set U_h=ceil(sum_{i<=h}x_i). The U_h are
nondecreasing integers. The function

    k(S)=max_{h in S} U_h,       k(empty)=0

is a normalized monotone submodular rank. One direct justification
is the diminishing-returns identity for a maximum of nonnegative
weights: adjoining coordinate h raises the current maximum by
max(0,U_h-current maximum), which can only decrease as the set grows.

The claimed equivalence to prefix caps is exact. Rank feasibility
implies y({1,...,h})<=U_h. Conversely, for any nonempty S with largest
index h, nonnegativity and the h-th prefix cap give

    y(S)<=y({1,...,h})<=U_h=k(S).

Summation by parts then bounds the rounded group load by its
fractional load plus v_1. Empty groups contribute zero. If v_1=0,
the load is exactly zero and the count caps still matter: they are
retained rather than dropping zero-time coordinates from the joint
mandatory-total recovery.

For each big bin, a single integer cap h on its total count is the
polymatroid with rank h on every nonempty subset. Big bins and the
small prefix group are disjoint. Their direct sum over machines is
therefore precisely the integral K needed in Section 2.

## 4. Exact bins and completeness of the target witness

Write delta=epsilon/2 and K=floor(1/delta). At a positive target T,
pairs above T are forbidden. Small pairs have time at most delta*T.
The remaining normalized times are partitioned into

    (delta+i*delta^2, min(1,delta+(i+1)*delta^2)],

for 0<=i<B=ceil((1-delta)/delta^2). Every interval has positive
width, including the last one. The ceiling-minus-one index sends an
internal endpoint to the preceding interval. A time equal to delta*T
is small, and a time equal to T lies in the last big interval.

In a full-T integer schedule, every big unit is strictly larger than
delta*T. Hence the number of big units on one machine is strictly
less than 1/delta, which safely implies the stated cap K even when
1/delta is integral. With actual bin counts h_i and lower endpoints
lambda_i, the normalized lower load

    L=sum_i lambda_i h_i

is at most the actual normalized big load, so L<=1. The original
small load is at most T minus the actual big load and therefore at
most (1-L)T. The unmodified integer schedule is feasible for its
fixed-profile LP, including the original budget and all type bases.

Only occupied bins need to be considered. A bin absent from the
explicit eligible pair ground cannot contain an assigned unit in
any witness. Setting its profile count to zero therefore loses no
full-target schedule.

The LP intentionally does not impose a separate full machine-load
cap. Its big count caps and small fractional load cap are sufficient
for recovery, and the completeness argument above uses only these
actual inequalities.

## 5. The recovered load and the absence of lower-count assumptions

For a feasible profile, integer recovery respects each big-bin upper
cap. The machine's big load is at most

    T sum_i (lambda_i+delta^2)h_i
      <= LT+delta^2*T*K
      <= LT+delta*T.

The small prefix routine gives load at most

    (1-L)T+delta*T.

Adding the bounds yields (1+2delta)T=(1+epsilon)T.

The profiles are upper bounds, not exact bin counts. Using fewer
big units can only reduce the first bound. No lower bin count is
required to compensate for unused profile capacity. Mandatory units
cannot disappear, because the single recovery still has total N and
each original type total. They may move among permitted coordinates
only through that joint resource-feasible recovery.

Thus every profile success is a legal weak success. If all profiles
fail, a full-T witness cannot exist, by Section 4. This supplies the
one-sided semantics needed for target optimization without assuming
that weak successes are monotone.

## 6. All-input occupied-bin enumeration and polynomial space

At a partial profile with count s and lower load L, the next count h
is enumerated only up to

    min(K-s, floor((1-L)/lambda)).

This enforces both monotone inequalities before descending. Every
generated partial vector has a valid all-zero completion on later
bins. There are no dead subtrees hidden in the sharper complexity
bound.

At a fixed recursion depth, distinct partial vectors have distinct
all-zero completions. If there are p valid complete profiles and m
occupied bins, there are at most (m+1)p enumeration nodes. Consecutive
outputs require only a polynomial number of stack/counter operations;
there is no unary scan over rejected counts beyond the permitted
range. The same zero-completion injection applies to a combined
machine-by-machine enumeration. It bounds work on bad global profiles
as well as on successful ones.

The recursion depth is the number of occupied input bins, bounded
by the explicit pair ground. Each count, index, B and K is stored
in binary. Rational lower loads are sums of at most that many
encoded endpoints times binary counts. Their bit length is polynomial
in H+size(epsilon) and the target encoding. An epsilon whose reciprocal
is enormous therefore enlarges time, not the size of the stored
enumeration stack.

The same argument would not justify the stronger time bound for an
algorithm that first generated every unweighted composition and only
then tested L<=1. The pruned enumerator in the manuscript is essential
and is sufficient.

## 7. Independent derivation of both profile bounds

Ignoring lower load and including every possible bin gives the usual
count-vector bound

    binomial(B+K,K).

The occupied-bin profiles inject into this family by filling absent
coordinates with zero.

For the stronger bound, let n=floor(delta^(-2)). Since K=floor(1/delta),
we have n<(K+1)^2. Each bin lower endpoint satisfies

    lambda_i=delta+i*delta^2 >= delta^2*(K+i).

Therefore every valid profile satisfies sum_i(K+i)h_i<=n. Mapping
h_i to h_i copies of the positive integer part K+i is injective:
different bins have different part sizes. The count is at most the
number p_{<=n} of integer partitions of all weights at most n.

For t>0, each such partition contributes at least exp(-tn) to the
partition generating product, so

    p_{<=n} <= exp(tn) product_{j>=1}(1-exp(-tj))^(-1).

Expanding the logarithm, interchanging nonnegative series, and using
exp(t*l)-1>=t*l gives

    log product = sum_{l>=1} 1/[l*(exp(t*l)-1)]
                <= (1/t) sum_{l>=1} l^(-2)
                <= 2/t.

Choosing t=1/(K+1) yields p_{<=n}<=exp(3(K+1)). This derivation
bounds the cumulative partition count, not merely the partitions of
exactly n, so no extra factor n is missing.

The bound is used only in analysis. The algorithm does not evaluate
the infinite product or store a partition table. Over q machines it
gives at most exp(3q(K+1)) global profiles, and K<=2/epsilon proves
the stated 2^{O(q/epsilon)} time. The finite binomial and exponential
bounds simultaneously apply to the same traversal.

## 8. Budget feasibility, zero optimum, and target search

The initial minimum-cost full-total assignment checks whether any
original schedule is legal under the budget, without a load cap. A
rank loss or excessive minimum cost is a genuine global infeasibility
certificate. If N=0, the empty schedule is optimal.

When N>0, the separate zero-target test is necessary and correct:
restrict to zero-time pairs and minimize cost while retaining every
old type total. Success gives OPT=0. Failure establishes OPT>0 even
if the initially cheapest unconstrained assignment happened to use
positive times. The profile routine is never called at T=0.

A rational common grid g for all positive processing times has
polynomial encoding. All integer schedule loads lie on this grid,
including schedules with binary-large counts. An actual initial
budget-feasible assignment supplies a finite grid upper endpoint U.
It also supplies the initial weak output.

The maintained lower endpoint L is certified to satisfy L<OPT.
Only total profile failure raises it. A weak success lowers U and
retains the corresponding actual schedule of load at most
(1+epsilon)U. At adjacent endpoints, grid integrality gives

    U=L+g<=OPT.

Thus the saved schedule has the claimed approximation ratio. The
upper endpoint need not remain an upper bound on OPT after a weak
success; the invariant actually used is that U has a legal weak
output. This distinction makes the search valid even for nonmonotone
weak successes.

The initial load is at most N times the largest eligible time, so
binary search makes only polynomially many calls. No rational-gap
reoptimization lemma or extra multiplicative accuracy loss is needed.

## 9. Encoding and conclusion

The LPs have the explicit pair dimension. Rank inequalities use the
given exact recipient oracle and polynomial SFM separation; all
original counts bound feasible coordinates. Profile coefficients,
targets, prefix ceilings and rational costs have polynomial encoding
in H_epsilon=H+size(epsilon). The full numerator/denominator size is
the appropriate precision parameter; log(1/epsilon) alone would not
handle an arbitrarily long rational near one.

Each fixed-profile LP and integer polymatroid-intersection recovery
therefore fits the stated polynomial oracle work and workspace.
Keeping only the current profile, current solver state and saved
actual schedule suffices. All unsuccessful targets and profiles are
already included in the enumeration analysis.

The complete claim passes. Its significant scope is the joint
arbitrary-processing recipient-polymatroid model with mandatory
binary supplies, one exact cost budget, physical-machine parameter,
and polynomial space. The manuscript correctly avoids claiming
priority over fixed-machine schemes for ordinary unrelated jobs,
and it does not infer optimality of its accuracy-dependent base.
