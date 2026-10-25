# Verification note

**Curated source path:** `sources/checkpoint-q/arbitrary_value_profile_transfer_audit.md`

The source audit follows.

# Independent review of the arbitrary-value exact-budget allocation scheme

**25 October 2026. Reviewer: transfer_frontier. Full mathematical review of
`arbitrary_value_profile_allocation_approximation_scheme.md`, PA1--PA20
and all thirteen sections: PASS.**

This review covers the original optional player matroid, arbitrary
player-dependent values, integral recipient polymatroids, nonnegative
selected-player setup fees and one shared exact setup-plus-assignment
budget. Original resource units are optional. It checks the integer
comparator and does not reinterpret it as a fractional optimum.

## 1. Feasibility and the selected basis

A minimum-setup original M-basis with no assignments is an exact
zero-utility feasibility test. If its setup fee exceeds the budget,
nonnegative assignment costs cannot repair feasibility. Otherwise it
provides a legal zero initializer. Player loops and zero-valued
assignments may be omitted because they cannot improve a selected
basis's utility and discarding assignments preserves both independence
and nonnegative cost.

Each actual basis is fixed before its profile LP and rounding. Its
setup fee is constant throughout that attempt. Enumerating r-subsets
and rejecting nonbases or unaffordable setups is therefore a valid
complete selection procedure, with the stated binomial factor. No
dummy-resource selection reduction or fractional mixture of player
bases is used.

## 2. Capping and the full integer witness

At a target T, replacing a positive value v by min{v,T} preserves a
full **integer** target witness. Either all assigned units are below
T, or one capped unit already contributes T. This would not preserve
all fractional full-target witnesses, and the manuscript correctly
limits the claim.

If the capped big-unit total reaches T, keep a first-reaching prefix
of any order. Its value is below 2T because its preceding sum is below
T and its last unit is at most T. Since every big unit exceeds
delta T, the prefix has at most ceil(1/delta) units. If the big total
is below T, all its units already satisfy the same count bound.

Dropping the other big units, and dropping all small units only in
the first case, decreases every original allocation coordinate.
Original resource independence and actual assignment cost therefore
remain feasible, with setup unchanged. The retained big lower sum
is at most two. Its upper-bin value U times T either reaches T or
leaves a small requirement no larger than the original small utility.
Thus every integer full-T allocation supplies an enumerated profile
and a feasible joint LP.

## 3. Exact bin boundaries and the joint LP

The open-lower, closed-upper intervals partition (delta,1] exactly.
The ceiling-minus-one formula handles every equality correctly:
delta is small, an internal boundary belongs to the preceding bin,
and a capped value of one belongs to the last bin. Only occupied
eligible input bins are constructed, so no accuracy-sized universe
is materialized.

The LP fixes each big-bin fractional count to the specified integer
h_i, uses one small-utility lower bound per selected player, and
retains each original resource exactly once across every value bin.
The assignment-cost bound is the original budget less the fixed
basis setup fee. Arbitrary player-dependent values and costs cause
no separation of a shared resource into fictitious independent
copies. Its coordinates and ranks are bounded with polynomial
binary encoding.

## 4. Disposal rank and complement duality

For a masked resource f on the current player ground, let n=f(P).
Adding disposal coordinate zero with rank n on sets containing it,
and rank f otherwise, gives a normalized monotone integral submodular
rank. In the mixed submodularity case, the needed inequality reduces
to f(B)>=f(A intersection B). A fractional independent allocation
extends to a base by putting exactly n-x(P) at free disposal.

With integer singleton vector d and augmented rank fhat, the rank

    g(S)=fhat(E without S)+d(S)-n

is normalized, integral and submodular. It is monotone because a
marginal of fhat is at most the corresponding singleton d_e.
The equality of base totals and the complementary rank inequality
give y=d-xhat in B(g). Conversely, singleton g bounds imply y_e<=d_e,
and complementing a base of g recovers a nonnegative base of fhat.
Thus this is genuine base complementation with no unit expansion.

At each selected player, ceiling-prefix caps on y form an integral
chain polymatroid. Disposal gets its singleton cap. Intersecting this
side with the complement resource direct sum and fixing its full
resource total gives a nonempty integral face; the original fractional
y is its witness and every resource must remain a base.

Maximizing the actual assignment coefficients applied to y minimizes
the original cost of d-y, since the constant sum of a_e d_e does not
change. The integer optimum therefore has original cost at most the
fractional witness. Dropping only free disposal leaves valid original
independent allocations. This is one simultaneous scalar objective,
not separate budget arguments for different players or bins.

## 5. Every prefix survives at the same cost-preserving point

For any player prefix S, integrality of d(S) gives

    x'(S) >= d(S)-ceil(y(S))
          = floor(d(S)-y(S)) = floor(x(S)).

All such inequalities and the cost comparison hold at the same
integer point. This verifies the exact lower-prefix interface used
later, rather than merely an aggregate additive-value guarantee.
The construction adds one disposal coordinate per resource and keeps
all large ranks and counts in binary.

## 6. Why there is no large-value rounding loss

Each big bin receives its lower endpoint as surrogate value; small
coordinates retain their true values. Order bins by decreasing
surrogate, then the small coordinates by decreasing value, with big
coordinates first at a tie. This is a nonincreasing ordering because
big surrogates are at least delta T and all small values are at most
delta T.

Within a big bin, adjacent surrogate differences are zero. At each
big-bin boundary, the fractional cumulative count is a sum of the
integer LP bin counts and therefore has zero fractional part. This
also holds at the last big-to-small boundary. In the lower-prefix
summation-by-parts expression, every potentially large-value error
thus vanishes. The only remaining differences occur in the small
part and telescope to at most its largest value, delta T.

The integer allocation need not preserve individual bin counts.
Preserving cumulative lower prefixes suffices. In the absence of
small coordinates this calculation loses zero; in the absence of big
coordinates it is exactly the ordinary small-value bound. Capped
and original output values are both at least the surrogate values.

## 7. Utility and exact shared-budget calculation

The fractional surrogate utility is at least

    [L+max{0,1-U}]T.

The gap U-L is at most K delta^2. If U<=1, the displayed expression
is 1-(U-L); if U>1, it is L=U-(U-L), which is at least as large as
1-K delta^2. Lower-prefix rounding consequently gives at least
(1-delta-K delta^2)T in original utility.

For delta=epsilon/3 and K=ceil(1/delta),

    delta+K delta^2 <= 2delta+delta^2
                    =2epsilon/3+epsilon^2/9 <= epsilon

throughout 0<epsilon<=1. The requested (1-epsilon)T guarantee
follows with slack. The chosen original basis and its setup fee do
not change, and actual assignment cost does not increase. The same
one shared budget is therefore exact.

## 8. Profile count, enumeration and binary space

The unweighted count bound is binomial(b_delta+K,K). For the sharper
bound, put J=floor(1/delta). The lower-load condition L<=2 gives
integer partition weight

    sum_i(J+i)h_i <= floor(2/delta^2) < 2(J+1)^2.

Distinct occupied bin indices map to distinct integer part sizes,
so the profile-to-partition map is injective. The nonnegative-term
generating-product argument bounds partitions of weight at most n
by exp(tn+2/t). Choosing t=1/(J+1) gives exp(4(J+1)). No partition
table or infinite product is evaluated by the algorithm.

The enumeration prunes at every partial count and lower-load bound.
Every generated prefix extends by zeroing later bins, and distinct
prefixes at a fixed depth have distinct zero completions. Hence the
entire traversal costs polynomial work per valid profile, including
targets on which every LP fails. Streaming bases and products of
profile families gives both complete bounds in PA5.

The theorem correctly charges the full rational accuracy encoding
H_epsilon. Only occupied input bins, binary counters, exact LP and
intersection workspace, and one saved output are stored. Neither
1/epsilon, all bins, all profiles nor resource copies are expanded.
This establishes polynomial space even for binary-small accuracy.

## 9. One-sided maximization and the original value grid

Original integer utilities and their minimum over a basis lie on a
common rational grid g of polynomial bit length. The finite bound
V=sum_j f_j(P) max_p v_pj is also on that grid and is an upper bound
on the optimum. The external endpoint V+g is strictly above OPT.

Every total profile failure excludes an original integer full-T
witness and therefore has T>OPT. Such failures preserve a strict
upper endpoint. Weak successes save a legal solution of value at
least (1-epsilon)T and raise the lower target, without asserting
full-target feasibility. At adjacent grid targets U=L+g, the strict
upper endpoint implies L>=OPT, giving the final guarantee. The
legal zero initializer covers the zero lower endpoint and zero
optimum cases.

Target-dependent capping and bins do not need monotone weak successes.
Only the sound failure implication is used. The number of target
calls is polynomial in the binary input and there is no additional
rounding loss in target optimization.

## 10. Verdict and scope

All PA sections pass. The proof gives the stated optional-M result
with setup fees and one exact shared budget, arbitrary pair values,
and the complete binomial-by-profile time bound. It makes no
fractional-comparator, corank-only, multi-budget or first-public-scheme
claim. No substantive mathematical correction is requested.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
