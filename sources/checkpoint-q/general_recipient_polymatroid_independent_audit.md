# Independent audit of the compressed recipient-polymatroid transfer

**25 October 2026. Independent mathematical review of the complete factor-five draft and aggregate-LP obstruction.**

The reviewed manuscripts are
`general_recipient_polymatroid_integer_optimum_transfer.md` and
`recipient_polymatroid_aggregate_configuration_gap.md`. The former's
displayed factor is tau+4rho, with tau=1/lambda and rho=(r-1)/r.
This audit validates that construction on its stated integer-optimum
comparator. A separate prefix-additivity refinement may improve the
factor; that refinement needs its own proof and is not silently assumed
by this audit. This is an internal independent review, not formal
verification or external peer review.

## 1. The natural matroid can be used without listing copies

For an integral polymatroid f, take a conceptual block of f({p}) copies
for each player p. Independent sets are precisely sets with feasible
block counts. Integer-polymatroid augmentation proves the matroid
augmentation axiom: if one feasible count vector has smaller total than
another, some coordinate can be increased; the larger set contains an
unused copy in that coordinate block. The rank formula

\[
 R(z)=\min_{S\subseteq P}\bigl(f(S)+z(P\setminus S)\bigr)
\]

is the maximum cardinality of a polymatroid vector bounded by z. It
follows from integral box restriction and can be evaluated by a paid
deterministic submodular-minimization operation. No coordinate is
expanded into its potentially exponentially many copies.

The union of whole player blocks E_S has rank f(S). The upper bound is
the inequality on S. For the lower bound, submodularity bounds the
marginal contribution of an omitted player by its singleton value, so
every expression in the rank minimum is at least f(S). Taking the
whole set S attains equality.

## 2. Residual capacity really is a block-independence threshold

Let W have count vector z. Replacing its p coordinate by f({p}) forms
W union E_p. The difference R(W union E_p)-R(W) is a nonnegative
integer A_p. Since this union adds at most f({p})-z_p distinct copies,
the difference is at most that many.

All copies of one player are symmetric under permutations fixing W.
More explicitly, partition the minimum rank formula into sets containing
p and sets not containing p. Increasing z_p by a leaves the first
minimum unchanged and increases the second by a. The resulting rank
increment is min(a,A_p), for 0<=a<=f({p})-z_p. Therefore every chosen
a<=A_p unused copies are jointly independent over W. Testing only
whether one copy is outside a closure would be insufficient; the draft
uses the entire residual count and avoids that error.

## 3. Copy identities and repeated player owners are consistent

At a new candidate search, every selected record is in the reserved
vector. If its player already owns a matching record, eligibility puts
that matching record in an earlier designated blocker layer, and thus
also in the reserved vector. Consequently the computed residual bound
leaves enough unused copies disjoint from every matching and selected
record of that same player. A player outside the matching has no other
matching record to avoid.

This proves, inductively, a conceptual execution in one fixed copy
universe with pairwise disjoint record copies for each player-resource
pair. Numerical records suffice because all relevant ranks depend only
on block counts. Moving an incoming selected bundle to a new matching
record must preserve its counts before retiring the old selected record;
the draft explicitly requires that order. A new matching record does
not inherit an old blocker flag, even if the owner name is unchanged.

This argument differs from the one-service recipient-matroid model:
two records of one player may use the same resource type as long as
their conceptual units are disjoint. The proof correctly works with
copy sets and their counts rather than collapsing player names.

## 4. Reservation and exchange proofs lift as block statements

At a used resource, all-remaining or relevant-only completion deletes
all previously unmarked matching copies of that type. Any old selected
subset reservation, after those deletions, is an independent subset of
the reserved W. The entire candidate block is independent over W by
the residual-capacity argument. It is therefore independent over every
such independent subset. This proves the new reservation for all
selected subsets without enumerating them.

When a group's records are all gone, that center can enter jointly with
every retained selected subset. The one-record earliest player exchange
deletes old service copies and installs the incoming copies. The
reservation argument is unchanged when an outgoing record had already
been excluded from that reservation: deleting both the record and its
group membership does not reintroduce it. Releasing discarded groups
does not delete their matching allocations.

Below the exchange layer, all selected and designated count records are
identical. The numerical residual-rank query therefore returns precisely
the same available vector. Together with equality of the player
eligibility flats, this preserves earlier maximality. The accepted
micro-signature counts all cascades and refreshes. No actual operation
needs to enumerate selected subsets or numerical capacities.

## 5. The lower cover is valid against an integral allocation

Fix an integral target allocation on a player basis and restrict it to
the at least w eligible members of that basis. Let n* be its resource
count vector at one resource. For reserved W, contraction gives the
integral polymatroid

\[
 g(S)=r(W\cup E_S)-r(W)\ge f(S)-r(W).
\]

Box restriction by n* has an integral maximum-sum vector h with

\[
 h(P)=\min_S\{g(S)+n^*(P\setminus S)\}
                      \ge n^*(P)-r(W).
\]

The last inequality follows separately for every S from n*(S)<=f(S).
Thus losing at most r(W) units suffices to make the resource vector
feasible in the contraction. Each coordinate h_p is bounded by the
residual singleton rank A_p. It is also coordinatewise below the
original feasible configuration, so every player-local downward-closed
constraint remains valid.

A complete failed lambda-oracle scan implies that the value of each
such retained local vector is strictly below B/lambda. Comparing to
its original value at least T and summing the lost service value gives
the required strict cover inequality

\[
                 \Phi>(T-B/\lambda)w,
\]

provided B<=lambda T. The use of a fixed integral optimal basis is
essential. Nothing here claims the analogous scaled inequality for
fractional player masses, and the separate obstruction shows why it
would be false.

## 6. Upper cover, binary arithmetic and fat reduction are paid

Rank is at most the total count of reserved copies, so minimality gives
the coarse coefficient 2(B+u) per designated matching bundle. Under
relevant-only completion, sharing a resource type shares a unit value;
the singleton/nonsingleton refinement remains valid even when a bundle
has repeated units. Pruning a positive type in one arithmetic batch
removes the maximum number of its units preserving the target. Later
deletions only lower total value, so a single pass yields individual-unit
minimality. The maximum overshoot is one unit value, not a whole type's
capacity times its value.

The Boolean restriction P(f) intersect [0,1]^P is a matroid polytope.
Its displayed rank formula and the restriction to locally feasible
singletons give the correct fat-recipient matroids. Given an integral
target allocation, selecting one fat unit for each fat-served player
produces an independent set of their union. Extending its union with
the complementary dual player basis yields a derived small-player basis
contained in the original all-small players. This is an integer promise
and does not rely on the refuted aggregate configuration relaxation.

All counts are bounded by singleton oracle values. Sums of O(r) such
counts add only O(log(r+1)) bits. Rank evaluations minimize a submodular
function plus a modular term on q explicit players. The number of rank,
player, local-oracle, union and decomposition operations per signature
change is polynomial. The finite utility grid and total-value upper
bound have polynomial encoding length. The one-sided target search
uses sound failure, without assuming monotone algorithmic success.

## 7. The aggregate configuration gap is correct

For q=Dr, D>=r>=2, and f(S)=|S|+D for nonempty S, submodularity follows
also from writing f as a free-matroid rank plus D rank-one ranks. The
fractional player vector x_p=1/D lies in the rank-r uniform basis
polytope. A D+1-unit configuration at every player gives resource
marginal y_p=1+1/D. For every nonempty S,

\[
 y(S)=|S|+|S|/D\le|S|+D=f(S)
\]

because |S|<=Dr<=D^2. Thus the specified aggregate configuration target
D+1 is feasible.

Any integral selected basis has r players and at most r+D units, so its
minimum is at most 1+floor(D/r). Giving each of its players exactly that
many units satisfies every subset inequality and attains the bound.
Taking D=rL and L large yields a gap tending to r.

The same integral polymatroid decomposes as one free-recipient resource
and D rank-one copies. That finer component-level LP rejects the
displayed configuration: each player must use all D rank-one services,
so its fractional use of that type is one, totaling Dr>D. Integer
feasible sets are preserved by aggregation, but this configuration
relaxation is weakened. The note correctly treats the gap as a
comparator obstruction, not an approximation hardness result.

## 8. Audit conclusion

The factor tau+4rho construction and its positive-error rank-dependent
time bound pass this independent mathematical review on their stated
integer-optimum comparator, including arbitrary integral recipient
polymatroids, binary capacities, and paid local/value oracles.

The equal-unit quota warning is necessary: integer rounding does not
automatically preserve a displayed continuous factor or a uniform
positive growth gap. Any two-value or improved-factor extension must
state and prove its own quota arithmetic and current-layer progress.
