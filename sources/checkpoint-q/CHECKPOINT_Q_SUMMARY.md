# Checkpoint Q: arbitrary-accuracy allocation and scheduling

**25 October 2026. English research checkpoint.**

The principal advance over checkpoint P is a pair of deterministic
approximation schemes, with arbitrary player-dependent values or
machine-dependent processing times, integral recipient-polymatroid
constraints, binary multiplicities, and exact cost budgets. This
checkpoint also records an explicit scheduling time/quality curve,
a six-profile exact-three-halves endpoint, and sharper positive and
negative results for robust integer allocation.

The historical general-graph matching exponent is not being optimized.
The present results concern related allocation, scheduling and common
integer selection problems. They have complete mathematical manuscripts
and recorded internal full reviews. Publication priority, external peer
review and formal verification are not asserted.

## 1. Principal guarantees

Let q denote the entire explicit player or physical-machine ground.
For optional selection, r is the rank of the original selection matroid.
H contains the binary input and the paid polynomial work for exact rank
oracles, submodular minimization, linear programming and polymatroid
intersection. Write H_epsilon=H+size(epsilon), including the complete
numerator and denominator of the supplied rational accuracy.

| Problem | Integer guarantee | Deterministic time, up to polynomial factors |
| --- | --- | --- |
| Arbitrary-value allocation, optional actual player basis, one shared setup/assignment budget | value at least (1-epsilon)OPT | binom(q,r) exp(O(r/epsilon)) |
| Arbitrary-time scheduling, every original job base mandatory, one assignment budget | makespan at most (1+epsilon)OPT | 2^{O(q/epsilon)} |
| The same scheduling with an activated actual machine basis and shared setup/assignment budget | makespan at most (1+epsilon)OPT | 2^{O(q/epsilon)} |

All three guarantees preserve their original scalar budget exactly and
use polynomial workspace in H_epsilon. Supplies are never expanded
into individual job or resource copies. Accuracy is measured against
the original integer optimum. Allocation may leave resources unused;
scheduling must retain every original mandatory job total.

These are accuracy-dependent exponential algorithms. Ordinary
fixed-machine or fixed-player approximation schemes already exist in
the public literature. The precise full-oracle models, strict budget
accounting, explicit state bounds and polynomial workspace are the
objects proved here.

Main proofs and reviews:

- `arbitrary_value_profile_allocation_approximation_scheme.md`, with
  the `arbitrary_value_profile_polymatroid_audit.md` and
  `arbitrary_value_profile_transfer_audit.md` full reviews.
- `arbitrary_processing_profile_approximation_scheme.md`, with the
  corresponding `..._polymatroid_audit.md` and `..._transfer_audit.md`.
- `activated_machine_profile_scheduling.md` and its independent
  `activated_machine_profile_allocation_four_audit.md`.

## 2. Why the accuracy exponent is linear in 1/epsilon

Both schemes separate units of size at most delta times the current
target from larger units, and put the latter into intervals of width
delta squared times the target. There can be O(1/delta) retained large
units at a player or machine. A profile records integer counts in the
occupied intervals; it does not choose individual unit identities.

The relevant enumeration retains a weighted lower-load constraint.
Mapping one count in interval i to a partition part of size J+i gives
an injective map to integer partitions of a number O(J squared), where
J is proportional to 1/delta. The generating-function bound gives
exp(O(J)) states. The enumeration prunes a partial profile as soon as
its count or lower-load cap would fail. Every retained prefix completes
with zeros, so all traversal work is polynomial per valid profile.

The stronger bound would not follow by first enumerating every
unweighted count composition. Only occupied input intervals are
materialized, and their indices and counts are binary. Consequently
even an extremely small binary-encoded epsilon does not require an
array of length 1/epsilon or 1/epsilon squared in memory.

### Allocation rounding

For a fixed actual selected basis, values are capped at the target.
This preserves integer target witnesses. A protected integer allocation
can be trimmed until at most ceil(1/delta) large units remain per player;
nonnegative costs and downward resource feasibility make this legal.

The profile LP fixes the total count in each large-value interval to an
integer. A free disposal coordinate and complement-polymatroid
construction permit simultaneous lower-prefix floors at all players,
while minimizing the original allocation cost through an equivalent
single linear objective. At each boundary between large intervals the
fractional prefix total is an integer, so that boundary contributes
zero rounding loss. Only the small-value part loses at most delta times
the target. Interval replacement contributes another O(delta) loss.
Taking delta=epsilon/3 proves the displayed utility guarantee.

### Scheduling rounding

The large-job profile uses integer upper count caps. Its lower-load sum
is at most one target. The small jobs receive the remaining fractional
load capacity. One joint integral intersection preserves the resource
bases and all machine profile caps. Upper-prefix ceilings add at most
one small-job size to a machine's load. Interval width contributes at
most another delta times the target. Taking delta=epsilon/2 proves the
displayed makespan guarantee.

In each direction, the exact budget is protected by optimizing one
cost objective on an integral face. It is not justified by adding a
budget inequality to an integral polytope and assuming integrality
survives.

## 3. Explicit scheduling endpoints

For arbitrary unrelated processing times, the bucket construction gives

    gamma_k = (3*2^k-1)/(2^(k+1)-1)
            = 3/2 + 1/[2(2^(k+1)-1)]

in (k+1)^q poly(H+k) time. A separate six-profile construction attains
the exact three-halves endpoint.

| Makespan factor | Whole-machine exponential factor |
| --- | --- |
| 2 | polynomial time |
| 5/3 | 2^q |
| 11/7 | 3^q |
| 23/15 | 4^q |
| 47/31 | 5^q |
| exactly 3/2 | 6^q |
| 1+epsilon | 2^{O(q/epsilon)} |

The six-profile proof first handles machines whose units all have size
at most T/2. Otherwise there is one unit above T/2 and at most one
additional unit above T/4. Two one-large-unit interval profiles and
three compatible two-large-unit interval profiles cover the remaining
cases. Their small-load caps and rounded large-unit upper endpoints
sum to at most 3T/2. Every original full-T schedule supplies an
unchanged feasible profile assignment.

The exact-three-halves base six is not asserted optimal. The earlier
seven-profile manuscript and its independent audit remain in the
archive as valid history; the six-profile theorem is the current
endpoint. The one-large-group bucket template has a matching bound
within that template, not a lower bound for other algorithms.

For the stronger special assumption that each machine has its own two
positive processing times, the exact-three-halves time is

    (50/27)^q E(q) poly(H),
    E(q)=2^{O(q log log(q+2)/log(q+2))}.

The pair may vary arbitrarily between machines. A type's processing
time may depend on its recipient. More generally, fixed integer d>=2
gives factor 2-1/d and base

    2-1/Gamma((d+1)/(d-1)),
    Gamma(R)=R^R/(R-1)^(R-1).

These special-input results retain all original job bases, one exact
assignment budget and polynomial space. They do not impose two values
globally. Their proofs are `per_machine_two_time_costed_scheduling.md`
and the common-two-value predecessor, with separate full reviews.

## 4. Initialization and original-total accounting

Allocation first checks an affordable original player basis; zero
counts are then a legal initializer. Scheduling instead checks whether
all original mandatory counts can be assigned within budget even with
unbounded load. With machine activation this requires enumeration of
candidate bases and a full original-count assignment test. A cheapest
setup basis alone would be insufficient.

Every scheduling pair mask retains n_j=f_j(P) from the original
instance. The common total sum_j n_j forces each separately bounded
resource to attain its original total. A deficient type cannot be
hidden by assigning additional units of another type.

Zero makespan is tested explicitly. Positive target optimization uses
a rational grid dividing the original values or times. Failed target
tests exclude a full integer witness; successful tests save an actual
legal approximate output. The one-sided search does not assume weak
successes are monotone and adds no further approximation factor.

## 5. Robust integer selection: positive regimes and sharp boundaries

The following results concern one common actual player basis across an
explicit scenario list, with scenario-adaptive integer assignments.
They complement rather than replace the schemes above.

**Bounded minimal unit obstructions.** Suppose every inclusion-minimal
set that cannot receive one unit in a scenario has size at most w.
The guarded exact positivity procedure uses w^c poly(H) time, where
c=q-r. Its whole-ground version has base 2-1/w and the displayed E(q)
overhead. This applies to the aggregate budgeted unit-feasibility
family, not merely to individual resources' circuit sizes.

At width two the obstruction graph admits a stronger exact procedure.
In the dual player matroid, omitted players must contain a vertex cover.
Branching on a vertex of degree at least two decreases the residual
rank by one or at least two. A residual matching is solved by matroid
intersection and then full-basis extension. With phi=(1+sqrt(5))/2,
the bounds become phi^c poly(H) and

    ((5-sqrt(5))/2)^q E(q) poly(H).

The whole-ground base is approximately 1.381966. The algorithm returns
an explicit width violation outside the promise rather than reporting
false infeasibility. These unit gates also combine with the earlier
integer-quota approximation tradeoffs.

**Common-setup additive recovery.** For arbitrary unrelated values and
a setup vector shared by all scenarios, the omission method gives
robust utility at least max{0,(1-epsilon)FOPT-u}, where FOPT still
selects a genuine common basis and relaxes only allocation counts, and
u is the largest individual unit value. Every scenario budget remains
exact. This is additive, so it may legitimately return zero on a unit
zero/one obstruction.

**Unrestricted robust lower boundaries.** A self-contained sparse-paving
construction with q unit-valued scenarios requires at least
binom(q,r)/q-1 rank queries for any finite multiplicative guarantee.
At balanced rank this is 2^{q-O(log q)}, excluding every fixed
whole-ground base below two in the oracle model. A separately
attributed consequence of the public three-matroid-intersection lower
bound already gives a no-fixed-base-below-two boundary with two
scenarios, though with a different subexponential loss.

With explicit free Boolean resources and just two cost scenarios, a
separate k-SUM reduction makes robust OPT either zero or one and
preserves omitted rank c=k. Thus a corank-only FPT finite-factor
algorithm would contradict W[1]-hardness. This is a conditional
explicit-input boundary, distinct from the unconditional oracle bound.

## 6. Public-baseline and claim discipline

`scheduling_and_profile_primary_baselines.md` records the sources and
literal comparisons. Shmoys--Tardos already supplies cost-preserving
additive load rounding and compressed multiplicities for ordinary
jobs. Ordinary fixed-machine approximation schemes and Santa Claus
schemes also predate this checkpoint. Their existence is not claimed
as new. The compared running-time curves and exact versus violated
budget scopes must be kept separate.

The public OpenAI math index is used only at its visible index scope;
its entries are not treated as independently verified proofs or as a
search of private results. No matching-exponent improvement or
polynomial-time solution of general unrelated allocation is asserted.

The archive includes the full proofs, independent mathematical audits,
the cumulative prior checkpoint, and a hash manifest. New transfers
whose manuscripts or reviews are still incomplete are excluded from
this frozen checkpoint. The ongoing research direction is to retain
the exact cost and integer recovery interface while extending the
profile method to other genuinely coupled selection problems.
