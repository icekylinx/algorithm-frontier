# Independent audit of the exact-two global enumeration endpoint

**25 October 2026. Full independent read by the transfer-frontier researcher
of `exact_two_global_enumeration_unrelated_allocation.md`, X2-1--X2-3 and
all three sections. Internal audit, not formal or external verification.**

The endpoint passes. Enumerating a complete role set removes the need
for a positive service gap. Each resulting LP uses full light service,
and the existing one-shot signed-cost rounding loses less than half
the original optimum at the relevant value mask. The selected player
basis, exact setup-plus-assignment budget and original shared resources
are recovered exactly as in the audited SD proof.

## 1. A fixed nonempty role set has a bounded polynomial LP

For a mask and nonempty I, the real-resource ranks are masked once on
the complete role partition. The dummy remains available on every
player. Its zero service value means that the common light objective
is bounded by original real resource utility; one protected light
coordinate suffices to bound the objective. All independent count
vectors are bounded by original finite ranks, and the dummy by its
matroid rank. Thus a feasible role polytope has an attained finite
rational optimum with uniform polynomial bit complexity.

The affine budget may have a negative right side, but it is an ordinary
linear constraint on a bounded polytope. Exact rank separation, the
forced count-one equalities and objective optimization are the same
paid polynomial primitives as in SD. An infeasible role is correctly
skipped. No numerical utility grid, inverse-accuracy loop or exact
positive-gap limit is required for this endpoint.

## 2. Recovery is legal for every enumerated candidate

The signed complement objective on its integral maximum-total face
cannot increase the affine cost. Every real player's full-prefix
count floor and the light utility guarantee hold at that same integer
point. The integer dummy support is M*-independent, so its complement
contains an original M-basis. Every selected player outside I is
dummy-free and hence has a real heavy unit; every selected player
inside I has the preserved original light utility.

Nonnegative original setup fees and assignment costs imply that
restricting to this basis costs no more than the affine certificate.
The dummy is not discarded before that certificate is converted.
Therefore every recorded output is an actual original solution,
regardless of whether the enumerated role pattern came from an
optimum. Comparing the actual rational utilities of these integer
outputs is polynomial and preserves the best candidate.

For I empty, there is no light objective to bound. The separate
full-total one-unit heavy-or-dummy intersection gate is integral and
has a bounded signed objective. Its use avoids an unbounded artificial
target and provides the correct output when every originally selected
player is heavy.

## 3. The optimum supplies an enumerated half-threshold witness

Choose an original optimum on B*. Original zero-valued assignments
can first be discarded, because their costs are nonnegative and
resources are downward. This operation is only on real assignments;
the zero-utility negative-credit dummy remains intact.

At threshold OPT/2, the selected light-only set I*=B*\F* and the
canonical dummy basis P\B* are among the enumerated role choices.
Retaining the original light service on I*, one original heavy unit
on each member of F*, and every canonical dummy unit preserves the
shared original resources and the affine original setup cost. If
I* is nonempty, its role LP is feasible at full service OPT, so its
computed service t is at least OPT.

The global light maximum is strictly below OPT/2 and the heavy
minimum is at least OPT/2. One-shot rounding therefore leaves at
least OPT/2 at every selected player. If I* is empty, the canonical
cover witnesses the pure gate. If OPT is zero, the initial feasible
minimum-setup basis with zero resources suffices. These arguments
cover both class endpoints and the exact equality convention at
the threshold.

## 4. Time, space and comparison scope

There are at most qm+1 masks and exactly 2^q possible role sets.
One LP, one polynomial rounding/recovery and actual-value evaluation
per case cost polynomial H. The role sets and masks can be streamed;
only one current workspace and the best original output are retained.
This gives 2^q polynomial time and polynomial workspace on the
original explicit player ground, including binary resource supplies.

The endpoint is obtained by direct enumeration, not by setting the
accuracy loss to zero in Gamma or in the sub-two-base conversion.
It does not supersede the exact-two special two-value theorem at
base 50/27, and it does not prove that base two is optimal for the
general exact-two guarantee. Its comparison with the fixed-positive-
slack near-two algorithm is correctly stated as a time/quality tradeoff.
No substantive mathematical correction is requested beyond making the
safe zero-valued-original preprocessing convention explicit if desired.
