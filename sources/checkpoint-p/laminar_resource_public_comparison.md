# Public comparison for laminar recipient constraints

**25 October 2026. Primary-source comparison and explicit reductions.**
The new reservation proof is independently audited in
`laminar_resource_reservations_independent_audit.md`. This file
records fair named public comparisons. It does not claim that every
possible public-framework reanalysis has been optimized.

## 1. Keep the two directions of matroid constraints distinct

The resource matroid \(R_j\) constrains the set of players receiving
one resource \(j\). A player-local item matroid constrains the
different resource indices in one player's own bundle. The new base
laminar result has arbitrary player-selection matroid \(M\), common
intrinsic resource values and explicit laminar **recipient** matroids.
Its optional local-family extension imposes both kinds of constraints.

The primary definition of laminar matroids can be found in Fife and
Oxley, [*Laminar Matroids*, arXiv:1606.08354v1](https://arxiv.org/abs/1606.08354v1).
Its capacity definition agrees with the one used in the reservation
manuscript. Laminarity is used by that algorithm through a saturated
antichain, not merely through polynomial membership testing.

## 2. The printed general-resource baseline

Bamas, Lindermayr, Megow, Rohwedder and Schloeter,
[*Santa Claus meets Makespan and Matroids: Algorithms and Reductions*,
arXiv:2307.08453v1](https://arxiv.org/abs/2307.08453v1), Theorem 4,
gives polynomial \(8+\varepsilon\) approximation for common-value
resource matroids/polymatroids and \(4+\varepsilon\) for the
two-value compulsory-player problem. The latest arXiv record checked
on 25 October 2026 still lists v1. The original definition is in
Section 1, the algorithm is in Section 4, and the general-value
reduction is Lemma 22 in Appendix E.

The comparator in this displayed theorem is integer optimum. In
particular the source does not state the exact coupled
configuration-LP comparison used in the new laminar note. A stronger
comparator should not be inferred from an approximation headline.

### 2.1 Arbitrary player selection is already covered by a simple reduction

For the base model, the public \(8+\varepsilon\) guarantee also
covers arbitrary player selection, even though the source phrases
its problem with all players compulsory.

Let \(M\) be the selection matroid on \(P\), of positive rank,
and add one new resource of value
\(H>\sum_jv_j\), with receiving-player matroid \(M^*\).
Retain all original resource matroids and make every player compulsory.
The new resource need not be laminar; the public theorem allows
arbitrary resource matroids.

An original solution serves a basis \(I\) of \(M\). Give the
new resource to \(P\setminus I\), a basis of \(M^*\).
Each original resource's used recipient set can be extended to a full
basis in its resource matroid on \(P\); the added recipients only
gain nonnegative value. This gives a valid source instance allocation
whose minimum value is at least the original objective.

Conversely, the recipients \(D\) of the new resource in any source
solution form a basis of \(M^*\). The complement \(I=P\setminus D\)
is a basis of \(M\), and every player in \(I\) received all its
value from original resources. Restricting each original receiving set
to \(I\) preserves independence and preserves those players'
values. The two optimum values are therefore equal. The finite value
\(H\) has polynomial encoding length; dual-matroid queries and
resource-base extensions use paid polynomial matroid operations.

Hence **polynomial \(8+\varepsilon\) for general player selection
and laminar recipient resources is already a derived-public
baseline**. The new factor near five is a quality/time and
rank-dependence tradeoff, not the first constant approximation for
this base model.

### 2.2 Special domains in which four is already public

The printed two-value compulsory-player \(4+\varepsilon\)
guarantee applies to laminar resources as a special case. It should
be used instead of eight in that domain.

There is also a direct \(4+\varepsilon\) public pipeline for
unit-valued resources with arbitrary player selection: use the
Section 4 matroid/polymatroid covering problem with the discard
matroid \(M^*\), and the sum of the resource matroid independent
polytopes as the unit-service polymatroid. Extending the independent
discard set to a dual basis only removes supplied players. Integral
polymatroid-sum decomposition assigns the counted services back to
individual resources. Thus the new near-five general-value claim is
not a uniform improvement in every special case.

Adding the dual dummy resource to a general two-value instance can
introduce a third value. Without another argument, the printed
two-value theorem should not be relabeled as a theorem for every
two-value instance with arbitrary selection.

## 3. Why the existing transversal-slot adapter is insufficient

For an explicitly represented transversal recipient matroid, physical
slots and a player-local partition constraint implement the resource
exactly. The public and new comparisons for that model are documented
in `item_matroid_allocation_public_scope_audit.md`. The all-player
quasipolynomial four-approximation there has a direct public PS
derivation; the general-selection six-approximation uses the named
published DRZ player-side machinery and its verified resource adapter.

Some laminar matroids have no transversal representation. A small
example consists of three disjoint parallel pairs, each with capacity
one, and their common root with capacity two. In a transversal
presentation, a nonloop parallel pair must have a single common
neighbor slot: two distinct available slots would permit a matching
of that pair. Distinct parallel classes require distinct slots because
two elements from different classes are independent. Picking one
element from each of the three pairs would then give a matching of
size three, contradicting the matroid's rank two.

This is a self-contained separation from the old slot representation.
It does not assert that laminar matroids contain every transversal
matroid. The classes are not being compared by such a containment.

## 4. Why an unchanged PS or DRZ physical-item proof does not suffice

The laminar construction represents one service by tokens at several
nodes while counting its value once. Assigning its value to every
token would introduce a depth loss. Assigning positive value only to
a leaf token does not restore the physical-item proof: a blocker can
meet an ancestor token of zero assigned utility while retaining all
its positive utility outside the center. The usual outside-blocker
minimality charge would then be invalid.

The new saturated-antichain inequality instead bounds fractional
service loss by the original resource capacities and charges each
service at most once. This is an additional reservation/certificate
adapter that must be stated and proved. Merely observing that a
laminar independence oracle is polynomial does not provide the
single-owner physical resource interface of the old slot algorithms.

A public outer search might also be combined with this new adapter.
Such a composite would be named as using the new reservation
mechanism; it is not an unchanged theorem printed in the old source.
No globally best approximation or novelty claim is based only on the
absence of a laminar keyword in that source.

## 5. Scope of the optional local-family extension

The dummy-resource reduction in Section 2 does not encode arbitrary
additional player-local bundle families into the Bamas et al.
resource-matroid model. Thus its eight-approximation is a comparison
for the base laminar recipient model. It should not silently be
advertised as a proved algorithm for every combination of recipient
matroids and heterogeneous local item matroids or knapsack constraints.

The optional local-family theorem in the new manuscript keeps a
row-perspective relaxation and column resource polytopes and proves
their common certificate explicitly. A same-model public claim for
that combination needs its own adapter and oracle costs. This audit
does not declare it the first constant approximation; it records the
precise boundaries of the named public results verified here.

