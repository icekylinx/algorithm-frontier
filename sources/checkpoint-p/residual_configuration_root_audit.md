# Root audit of the residual-capacity configuration relaxation

**25 October 2026. Independent internal mathematical review.**

This review concerns
`recipient_polymatroid_residual_configuration_relaxation.md` and its
relation to the already reviewed compressed factor-four algorithm.
It validates a stronger comparator for arbitrary integral recipient
polymatroids. It does not assert efficient optimization or separation
of the entire configuration LP.

## 1. Every residual cut is a valid integral inequality

For a resource polymatroid f and an integral feasible reserve z, let

\[
 a_p(z)=\min_{S\ni p}\{f(S)-z(S)\}.
\]

This is exactly the maximum number of further units of player p that
can be added to z. It is nonnegative and integral. For any integral
legal allocation column n, take natural-matroid independent sets Z,N
with those respective block counts. Extending Z inside Z union N
adds a subset H of N minus Z with at least |N|-|Z| units. Its block
counts satisfy h<=n and h_p<=a_p(z). Therefore

\[
                 \sum_p(n_p-a_p(z))_+\le z(P).
\]

This proof permits overlap between Z and N; the extension explicitly
uses N minus Z. It also does not assume z is a base of the entire
resource polymatroid. Only z's feasibility is needed.

For a feasible integral target allocation, each chosen player puts
unit mass on its own configuration. The displayed inequality is then
exactly the proposed linear configuration cut. All coefficients are
nonnegative. Convex combinations of target allocations preserve every
cut, so the strengthened system is a valid relaxation.

## 2. The algorithm's dependent reserve is represented exactly

The algorithm's reserved natural-matroid set W can be dependent.
Choose a basis Z of W. Then cl(Z)=cl(W), its size is r(W), and every
whole player block has the same rank increment over Z as over W.
Thus the cut indexed by the feasible block counts of Z uses precisely
the algorithm's available capacities, with right side r(W).

The basis count vector can be computed under W's count box by integral
polymatroid greedy and paid submodular minimization. There is no
expansion by capacities. The comparator proof needs only its existence;
the stronger statement that it can be materialized as count data is
also justified by the existing box-restriction implementation.

## 3. Truncation gives the correct fractional lower cover

For each eligible player's integral count configuration n, replace
every coordinate by min(n_j,A_pj). This keeps local feasibility by
downward closure and satisfies the exact available-count box. A fresh
failed lambda-oracle scan implies that its value is strictly below
B/lambda. Mixing configurations keeps this strict inequality for
every eligible player with positive mass.

The lost expected value is exactly the weighted sum of the cut
coefficients (n_j-A_pj)_+. Summing the corresponding residual cuts
over resources, then restricting their nonnegative left sides to the
eligible players, bounds that loss by Phi=sum_j v_j r(W_j).
The original expected value is at least Tx_p, and the eligible base
mass is at least w. Hence

\[
                     \Phi>(T-B/\lambda)w
\]

for B<=lambda T. Positive eligible mass supplies strictness even when
T=B/lambda. No claim is made that arbitrary fractional player masses
obey the older integer-optimum contraction argument without these cuts.

## 4. The fat reduction preserves the new inequalities

Selecting one fat unit from each fat-containing configuration gives
a fat service marginal bounded by that resource's original column.
It is at most one per player in total, so the cap-one recipient
matroids and their union are the correct fat objects. Local singleton
feasibility follows from downward closure of the original configuration.

The standard fractional dual-union base completion yields a derived
player-base vector no larger than the mass of all-small configurations.
Discard fat-containing configurations and scale each remaining player's
configuration masses down to that vector. Every retained configuration
still has its entire original value at least T; no fat unit is removed
from a retained configuration.

For a small resource, its rank function and its possible residual-cut
indices are unchanged. Every coefficient is nonnegative, and each
configuration mass only decreases. Thus every new cut remains valid,
not merely the aggregate resource column. This closes the required
fractional fat-complement interface for the strengthened comparator.

## 5. Complexity, support and special resource classes

The search algorithm is unchanged. It does not invoke a separation
oracle for the cut family or a pricing oracle for arbitrary dual
configuration costs. Its only optimization queries are the explicitly
paid local available-count oracle and the existing rank/submodular
operations. Its factor-four and positive-error time bounds therefore
carry over without adding the LP's number of variables or inequalities
to the implementation cost.

At a normalized failed state, at most r-1 matching and r-1 selected
records are reserved. A basis of that reserve has support on at most
2(r-1) player names. Consequently cuts on such bounded-support reserves
already suffice for the theorem. The reduced small-player rank never
increases, so the same support family survives fat reduction. Rank one
is handled directly, as in the allocation theorem.

For a scaled matroid type f=c r_R, the independent-set loss lemma and
the pointwise inequality

\[
                  (n-a)_+\le (1-a/c)n\quad(0\le n,a\le c)
\]

make every residual cut redundant under the component configuration
column y/c in P_I(R). Thus the strengthened relaxation agrees with
that previously proved comparator on supplied scaled types.

## 6. The rank-gap repair is explicit

For f(S)=|S|+D on nonempty sets, reserve D+1 units at one player a.
That is feasible. The residual capacity is zero at a and one at every
other player. At the earlier gap point with q=Dr and a D+1-unit
configuration of mass 1/D for every player, this cut's left side is
q+1/D, while its right side is D+1. For r>=2 and D>=r the cut is
violated. It uses only one reserved player.

This proves that the new constraints remove the specific aggregate
gap point. It does not claim the strengthened polytope is integral.
Its proved gap bound is 4-3/r with an exact available oracle, through
the actual rank-exponential rounding/search algorithm.

## 7. Unit quotas and the fat-deficit parameter also inherit the comparator

For integer unit target t and output quota b, every clipped integer
configuration in a failed exact scan has at most b-1 units. Averaging
therefore gives the non-strict retained bound (b-1)x_p. The same cuts
give Phi>=(t-b+1)w. Combined with the normalized upper coefficient
2b-1, this is exactly the previously audited quota inequality. Thus
the exact rank-exponential factor-three quota result also compares to
the residual-capacity configuration relaxation. Its critical t=4,
b=2 quasipolynomial growth gate remains unchanged.

Likewise, `fat_deficiency_parameter_allocation.md` may use this
comparator: its capped target search needs only a sound inner lower
cover and a valid fractional fat reduction, both now proved. A derived
rank delta<=k uses only supports of size at most 2(k-1). One may keep
the larger original-r cut family, or explicitly define the corresponding
weaker k-support relaxation for that capped parameter theorem.

## 8. Assessment

The root audit finds no unclosed step in cut validity, reserve-to-basis
equivalence, strict fractional cover, preservation of all cuts through
fat reduction, or the resulting approximation and time statements.
The new comparator is materially stronger than the refuted aggregate
LP and requires its own name and definition in every claim.

Efficient global separation and general configuration pricing remain
separate questions. The proof is internal mathematical work, not formal
verification or external peer review. The large-gap phenomenon itself
was already discussed by the public BLMRS23 source; this note's concrete
cut construction is not presented as an exhaustive publication-priority
claim.
