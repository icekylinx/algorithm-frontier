# Activation, binary feasibility and the exact six-profile realization

The [reference adapter](reference/activation.py) realizes the construction in
[Theorem AS](proof.md) on complete integral rank tables and exact rational
data. It accepts a positive finite physical-machine count, original job ranks,
arbitrary nonnegative processing times and assignment costs, eligibility masks,
an ordinary activation-matroid rank table, nonnegative setup fees and one
combined budget. The active rank may be zero. It also exposes a direct
`SixBackend` for the original model of [Theorem SX](../six-profile-three-halves/proof.md).

## 1. Exact original-total restriction before compression

**Lemma 1.** For a genuine activated basis, the client's restricted instance
has exactly the original supported schedules and original mandatory totals,
with assignment budget equal to the original budget minus that basis's setup.
Its physical coordinate count is the activated rank.

**Proof.** Stream subsets of the original activation rank and keep exactly
those with that same matroid rank. The table validator checks integral
polymatroid rank axioms and singleton ranks at most one; these are precisely
ordinary matroid rank axioms. Thus every retained subset is an actual basis.
The original setup sum is fixed before scheduling, and an excessive sum
rejects the basis.

For each job type, intersect its original eligible machine set with this basis.
Before constructing any restricted full-rank field, compare the original rank
of that intersection with the original mandatory full rank. A loss rejects the
basis; it never reduces the number of required jobs. On a retained basis, form
the complete local rank table by mapping each subset of active coordinates to
its original physical subset and applying the original eligibility mask.
Its full rank is exactly the original mandatory amount by the preceding check.
The internal restriction helper also checks that its supplied basis is genuine.

A count vector supported on the active eligible pairs is independent in these
local ranks exactly when its zero extension is original independent. In the
forward direction, its count on an arbitrary original set is bounded by the
rank of the active eligible intersection, then by the original set's rank by
monotonicity. The reverse direction applies the original rank constraints
to active subsets. The original total equality makes these independent vectors
original bases in both directions. Local times and costs are unchanged, so
subtracting the fixed setup gives exactly the original shared budget.

There are only as many local physical coordinates as active machines. Profiles
are therefore generated on the activated rank, preserving Theorem AS's
rank-sensitive profile factor. Inactive machines do not create redundant
profile choices. <code class="math">\square</code>

## 2. Binary minimum assignment cost and zero feasibility

**Lemma 2.** `feasible` and `target(0)` decide their original activation problems
exactly. Their per-basis assignment optimization uses binary rank increments,
without numeric count enumeration or a positive-target solver.

**Proof.** After Lemma 1's retained-rank check, the original job types are
independent components before load restrictions. For each masked resource,
order its active machines by increasing original assignment cost and take
the rank increment of each successive prefix. These increments form an
integer base, by polymatroid greedy. They minimize its actual cost: telescoping
the weighted prefix sums expresses any base cost as the largest cost times
the fixed total minus a nonnegative combination of prefix counts. Each prefix
count is at most its rank, and greedy attains all those ranks simultaneously.
Cost ties are resolved by physical index and do not affect the argument.
The internal greedy helper requires already-masked retained-rank tables and
rejects a forbidden coordinate with positive singleton rank. Applying that
helper directly to unmasked original eligibility data is outside its contract.

Add the exact component minima and compare with the single residual budget.
Every accepted result is legal. Conversely any legal schedule has assignment
cost at least that sum on its activated basis, so the streamed basis search
cannot miss it. For zero load, additionally mask every positive-time pair
before the retained-rank check and use the same greedy test. Nonnegative
processing times make this exactly zero-load feasibility.

With no mandatory jobs, the test still chooses a genuine affordable activation
basis and retains its setup charge. Rank zero is feasible exactly when every
original mandatory amount is zero. Its output has the empty basis and zero
counts at every original physical coordinate. All counts are computed by a
bounded number of binary rank differences and rational products; numerical
multiplicity is not a loop bound. <code class="math">\square</code>

## 3. Three positive-target clients and one shared cost recovery

**Lemma 3.** The reference implements the semantic activated profile, bucket
and six-profile target guarantees, with all original bases and the shared
setup-plus-assignment budget exact.

**Proof.** The profile and bucket clients reuse the canonical
[general-processing joint plan realization](../arbitrary-processing-scheduling/reference-realization.md).
The fixed basis and setup remain unchanged while generating its local plans,
solving the joint resource LP and performing one minimum-cost integer recovery.
That recovery's scalar objective is actual assignment cost. Its result costs
no more than its fractional witness and therefore fits the residual assignment
budget; adding the same original setup proves the shared budget. No profile
duplicates resource capacity or activates an extra machine.

`SixBackend` instantiates that same joint solver with the six explicit masks
of Theorem SX, Section 3. Profile zero retains times up to half the target and
one full fractional-load bound. Every other profile has its stated disjoint
open-left/closed-right big groups, each with integer count cap one, and the
quarter-target small group with the table's fractional small-load cap.
All zero-time coordinates stay in the small group. Big upper endpoints never
exceed the target, and every forbidden pair is zero in the original resource
LP. The shared recovery retains all big caps and replaces only small load rows
by complete descending-time prefix ceilings. Theorem SX's five explicit load
sums and profile-zero inequality apply to that same integer point.

Every original full-target schedule supplies one enumerated profile or label
vector on its genuine activated basis, by the respective PS, AB and SX coverage
proofs. Lemma 1 preserves that full schedule and its original totals in the
compressed instance. Hence every successful output has the stated factor,
and full exhaustion over bases and profiles is a sound original rejection.
The direct `SixBackend` applies this same argument to the original unactivated
scheduling problem with its one assignment budget. <code class="math">\square</code>

**Proposition 4.** `optimize` returns Theorem AS's requested approximation on
accepted complete-table inputs, or detects global infeasibility. Direct
`SixBackend.optimize` gives the exact three-halves approximation of Theorem SX.

**Proof.** Lemma 2 supplies an actual finite feasible upper schedule or detects
infeasibility, and decides the zero optimum exactly. After zero failure, a
common denominator and integer gcd give the original positive load grid.
The search saves actual schedules on weak upper successes and raises its lower
endpoint only on Lemma 3's sound full rejection. At adjacent grid endpoints,
the saved nominal upper target is at most the original integer-grid optimum.
Its actual output satisfies the requested factor. This is Theorem AS's
one-sided search, without a monotone-success assumption. Direct six-profile
optimization inherits the identical canonical grid search used by the other
fixed-ground clients. <code class="math">\square</code>

## 4. Costs, streaming and independent evidence

Activation bases are streamed with a combination iterator; only the current
basis, restricted tables, solver and best original output are retained. The
native feasibility gate sorts active costs and reads binary rank increments.
Its storage is polynomial in the explicit complete-table input, independent
of the numerical job totals. Positive profile attempts are counted only on
the active machines, as in Theorem AS. Complete rank-table validation and
restriction work are charged explicitly.

The positive-target clients retain the canonical solver's active-set LP
enumeration, numeric integer-count enumeration and potentially exponential
vertex storage, as specified in the joint realization proof. Multiplying those
actual per-plan costs by the streamed basis/profile attempts gives this
reference's bound. They are not described as the paid polynomial oracle
primitives in AS or SX. The profile iterator itself preserves its binary
accuracy and explicit-stack storage guarantees. The reference does not store
a list of all activation bases or all attempted solver descriptions.

[check_activation.py](verify/check_activation.py) independently enumerates
original physical schedules and original activated bases, then computes original
setup-plus-assignment cost and actual load. Its oracle does not use the
restriction, greedy gate, fixed-profile LP or zero-extension implementation.
It includes a cheapest-setup basis lacking capacity, a cheapest setup whose
assignment is unaffordable, independently affordable pieces exceeding the
combined budget, activation loops, nonuniform matroids, rank zero, empty jobs,
zero times and rational data. Nine extra checks use an 81-bit mandatory count
while disabling positive-target solver creation, testing exact feasibility,
zero load and optimization by binary greedy alone.

[check_six_profiles.py](verify/check_six_profiles.py) tests the direct original
SX model, independently of activation. It compares target failures, optimized
outputs and every tested fixed-plan vertex's joint recovery with original
integer schedules. Six one-machine fixtures each fit precisely one intended
profile, and exact interval endpoints are checked. Finite tests support the
reference connection; they do not prove the arbitrary-oracle theorem by
enumeration, constitute formal verification or claim external peer review.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
