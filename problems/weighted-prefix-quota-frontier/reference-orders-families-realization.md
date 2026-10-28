# Exact two-order and variable-family prefix clients

The [native clients](reference/orders_families.py) implement the complete
bounded [two-order theorem](manuscripts/two-order-weighted-prefix-target-classification.md)
and [variable-family theorem](manuscripts/few-weight-families-prefix-target-scheme.md).
Both reuse the original-subset resource and signed scalar recovery of the
[one-order realization](reference-prefix-realization.md). The broader kernel,
laminar-coloring and sparse-hash families are separate.

## Original contracts and shared recovery

`TwoOrders` has two explicit permutations of the original coordinate IDs and
one common nonnegative integer weight vector. Its rows select an order, prefix
length, relation and nonnegative integer target. `Families` has one original
coordinate order and an explicit table of nonnegative integer weight vectors;
its rows select a family instead of an order. The family count is part of the
input and may vary. Zero entries, unused families and duplicate vectors are
permitted. Neither model permits arbitrary differing orders and weights on
every row at once.

There is one complete original integral polymatroid rank, one signed rational
scalar objective and original eligibility. Mandatory mode retains the original
full rank after every mask. Optional mode adds exactly one internal zero-cost
disposal coordinate. Every real zero-column coordinate retains its original
resource identity and signed scalar coefficient. No second resource or unrelated
scalar budget is introduced.

Preparation is performed separately within each order or family: split
equalities, merge duplicate endpoints, keep upper suffix-record minima and
lower prefix-record maxima, remove automatic zero rows, and apply original
upper-coefficient prohibitions globally. Empty-prefix positive lower targets
are impossible. A lower-only large coefficient is retained and capped for
credit by the largest target. The capping equivalence is used only for integer
witnesses and outputs.

`recover_original` is the same native routine for all three prefix clients.
Its ownership map can have repeated original IDs and an optional disposal ID.
Every original subset bounds the aggregate of its copies, and the original
full total is a global cap. This exactly describes the shared copied rank:
partial copy sets are bounded by their full owner preimages. Disposal-containing
sets have the original-total rank. No copied-ground subset table is built.

One disjoint partition of copied coordinates prescribes the profile group
caps, including one zero-column remainder. Their sum is the original required
total. Resource/partition intersection is integral; on the full-total face
all caps are tight. Exact Bland simplex optimizes the same dominant objective
as the one-order client: total first, then the requested signed scalar. Its
coefficient is `2*original_total*maximum_absolute_cost + 1`. An absent positive
group or an unattained original total is infeasible. Returned integral counts
are aggregated and checked against all original rows, ranks and costs.

## Two orders: four labels and one common magnitude

For every order with positive lower rows, mark a conceptual first-reaching
prefix through its largest lower target using common capped weights. Each
original unit gets its two mark bits, yielding at most four shared copies per
original coordinate. An order without lower rows has a fixed zero mark bit.
All copies keep the true scalar coefficient.

The credited coefficient is the common capped magnitude in each incident
upper row and in each incident lower row whose bit is active. Thus every
nonzero column is one common magnitude times a row-support incidence vector.
Class grouping uses that actual full column, with its common magnitude charged
once per copied unit, independent of how many rows it enters.

For each order, if its marked cut lies inside its last upper prefix, relevant
mass is at most the largest target. Otherwise relevant mass is contained in
its marked units and is at most that target plus its largest lower target
minus one. Summing these two allowances bounds the union of all nonzero
copied units. The native cap is the sum of these exact per-order allowances,
with zero allowance for an order with no prepared rows. It is at most the
companion's `4*B-2` bound when `B >= 1`.

Every original integer witness therefore has an emitted profile. Conversely,
upper values agree exactly under projection and lower credited values are
dominated by true values, so every recovered profile is sound. The two-order
companion's support count, colored-partition estimate and all-input charging
apply to this actual catalogue. Its reverse-order improvement and the
[actual-support refinement](manuscripts/weighted-prefix-support-budget-tradeoffs.md)
analyze the same streamed profiles, without a separate native search or a
numerical analysis parameter.

## Variable families: streamed chains with only linear copied dimension

Every covering family has one first-reaching stopping position in the same
conceptual unit order. These marked segments are nested. Stream permutations
of the covering families. A permutation determines one chain of active-family
suffixes, with only one more layer than covering families. Each retained
coordinate gets one shared copy per layer, giving at most `(p+1)*n` real
variables, plus optional disposal. There is no family-subset catalogue.

Sort the actual stopping positions of any original witness to obtain one
enumerated chain. A unit belongs to the layer whose active suffix is exactly
the families still marking it. Tied stops cause empty intermediate layers;
the common crossing unit remains marked by all tied families. Consequently
every original feasible scalar value has a representation in some chain.
The implementation never generates the unit list or these stopping positions.

For each chain, partition original coordinates by the actual retained row
endpoints. A base color is a layer and endpoint segment. Within a base color,
each family's row template is fixed. Collapse the copied column to a vector
whose family entry is its capped weight if that template is nonempty, and
zero otherwise. Actual zero entries remain zero. Recover every row coefficient
from its template and this collapsed vector.

The code groups by base color, complete row column and charged mass; this is
equivalent to grouping by base color and collapsed vector, since every
nonempty family template exposes its entry in an actual row. The charged mass
is the vector's sum, counting a family weight once rather than once per row.
All zero vectors join the one global zero-column group while retaining their
distinct resource coordinates and true scalar costs.

The companion proves a mass allowance of `p*(2*B-1)` and at most
`2*p*(p+1)*B` base colors. Its alphabet-and-cuts injection counts nonzero vector
multisets even with arbitrary zero entries. Streaming the cover permutations
and occupied profiles therefore realizes exactly the bounded family algorithm.
Credited feasibility proves projection soundness, and the canonical stopping
chain proves completeness. A best profile over all chains gives the exact
original minimum or maximum scalar; exhaustion proves original infeasibility.

## All-input work, binary representation and bounded audit

Both clients use the canonical explicit-stack occupied-profile iterator with
charged masses normalized by the plan's cap. There is one nonnegative integer
count per actual class, a binary original-total count cap and one zero-group
remainder. Empty and zero-cap plans are handled before normalization.

Every partial profile extends by zeros under the count/mass caps. At a fixed
depth these extensions are distinct. The companion catalogue bounds therefore
charge all iterator states, failed row filters and empty recovery faces, not
just successful outputs. One permutation, one copied plan, one current profile,
one best original vector and one LP tableau are stored. Counts, weights,
targets, scalar denominators and original total remain binary throughout.

The native LP has a separately charged potentially exponential Bland basis
factor. The asymptotic theorems instead pay the stated polynomial exact
integral-intersection primitive. This distinction also applies to the unchanged
one-order API, whose native recovery now calls the same shared routine.

The bounded proof audit covers both full companions, the reversed-order and
actual-support tradeoffs, and the
[joint family/target lower construction](manuscripts/few-weight-prefix-joint-lower-bounds.md).
Oracle query lower bounds allow the specified bounded-error randomness;
readable-rank-program exclusions use deterministic ETH on their calibrated
families. Parameter-budget lower envelopes do not assert hardness at every
independently prescribed exact parameter pair. In the low-support optional
model the lower bound is for exact scalar optimization, while mandatory
instances use feasibility. No lower bound is transferred to graphic or matrix
resources, and no optimal leading exponential constant is claimed.

The [independent native checker](verify/check_orders_families.py) enumerates
literal original count vectors and compares their exact signed extrema in
mandatory, optional and eligibility modes. It separately bulk-constructs the
two simultaneous marks and the family stopping chain, including tied stops
and cuts within one coordinate. Binary-large fixtures use actual LP recovery
with more than 330-bit counts, targets, weights or scalar denominators. A
1,100-family zero-target case uses one layer and no subset expansion. These
finite checks supplement the proofs; proof-assistant verification and external
peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
