# Exact rational realization of the packing product lift

## Statement and scope

The [reference implementation](../reference/packing_summary.py) realizes the
rational construction in the [packing transfer theorem](represented-resource-packing-transfer.md).
It returns original item IDs with the full original-context, fixed-cost
replacement guarantee of that theorem, for all allowed failure queries and
all requested positive cardinalities up to the supplied limit. Its input
representation and return fields are specified in the
[API note](../reference/README.md).

The proof applies to arbitrary later matroid extensions restricting to the
original resource, even when the extension is not represented. The routine
needs neither an extension representation nor a future independence oracle.
It computes a restriction; solving an arbitrary extension query remains a
separate task. The current implementation uses rationals only.

## Lossless normalization and the gate

Every support and label list is validated as a set of explicit nonnegative
integer IDs. Costs and resource entries must be exact integers or fractions.
Copying these values into immutable records makes caller mutation irrelevant
to preprocessing. Input positions remain the original IDs; even identical
parallel records are not coalesced.

Clip the cardinality limit to the number of items, and each failure budget
to the number of explicitly occurring IDs in that system. Failing an absent
ID cannot remove an item. Clipping therefore leaves every effective query
unchanged. Normalize the support degree to the maximum actual support size,
with minimum one, and each label degree to its maximum actual list size.
The private padding construction consequently has polynomial encoded size.

When a resource is supplied, select a basis of the rows of its full original
matrix. A dependence among columns of the selected-row matrix is a dependence
in every original row, because every discarded row is a linear combination
of selected rows. The converse follows by restriction. Thus all original
column dependencies, all flats and the full original resource rank are
preserved. This step does not truncate or contract the matroid.

An empty ground, zero cardinality limit or rank-zero resource returns the
empty summary. In the last case every positive item is a loop, so every
feasible query has positive cardinality zero. Otherwise compute the product
of the exterior, label and resource dimensions with saturation at the item
count. The incremental binomial calculation stops as soon as it reaches
that count. No exterior-coordinate list, dummy padding or coefficient-monomial
list is built before this gate. If the dimension reaches the item count,
return the original ground unchanged, which immediately preserves all queries.

## Exact construction below the gate

Assign distinct positive integers to original support IDs and then to each
private dummy. Dummies are unique to an item and never fail. The implementation
lists all increasing row subsets of the Vandermonde matrix and evaluates the
corresponding minors by exact rational elimination. These are precisely the
coordinates of the exterior vector in the canonical increasing wedge basis;
row swaps carry their determinant sign.

Within each label system, assign distinct positive integers to labels and
use zero for the nonfailing dummy. Multiply the padded monic root polynomial
coefficient by coefficient, then list every coefficient monomial of total
degree at most the clipped failure budget. This enumeration is finite even
for an empty label system: its sole coordinate is one. The query product of
root-polynomial evaluations is a polynomial of at most that total degree,
so it defines the required failure-annihilating linear functional.

Take the tensor product with all label features and, when present, the
compressed resource column. Exact incremental elimination accepts a column
if and only if it is outside the span of previously accepted columns.
Columns arrive in increasing `(cost, original ID)` order. Therefore every
discarded column is a linear combination of retained predecessors, each of
no greater cost. This is exactly the weighted span relation required by the
main theorem.

## Universal replacement and finite work

Fix an independent extension context and a protected live positive item.
The intersection of the original ground with the extension closure of the
other context elements is an original-matroid flat. It excludes the protected
item, so a linear functional on the original resource annihilates the flat
and not that item. The selected-row compression does not change this fact.

Wedge with the union of the other padded supports and failed universe IDs.
The protected wedge is nonzero by distinct-point Vandermonde independence;
any conflicting or failed candidate has a repeated factor and maps to zero.
Apply this functional, the resource functional when present, and every label
query functional to the weighted span relation. Some retained predecessor
survives all factors. It replaces the protected item at no greater cost,
without changing the background or positive cardinality. Private padding
rules out choosing an already selected empty-support item. Iterating reduces
the number of omitted items and terminates. Since the summary is a restriction
of the original ground, this also proves equality of the optimum fixed cost,
including signed costs and infeasible prescribed cardinalities.

Below the gate all listed feature dimensions are smaller than the explicit
item count. Ambient Vandermonde degree and dummy count are polynomial after
normalization. The matrix-entry bit bound in Section 7.1 of the main companion
therefore applies. Rational echelon entries are ratios of minors of this
bounded-bit matrix, so their numerator and denominator lengths remain
polynomial. Sorting and resource rank computation are additional polynomial
work; the feature-column elimination has the main theorem's quadratic
per-column field-operation bound. No numerical tolerances or randomized
identity tests occur.

## Verification boundary

The independent checker enumerates actual item subsets, failures and fixed
backgrounds. It compares every prescribed-cardinality optimum and tests the
stronger protected-item replacement property directly, without using product
features in its comparator. Its resource feasibility routine independently
eliminates the original columns together with background columns in a larger
space. It also checks malformed inputs and replaces the determinant routine
with a failing stub to ensure the identity gate performs no exterior work.

These finite fixtures test implementation behavior. They do not enumerate
all matroid extensions or prove the parameter-dependent theorem; the flat
and annihilating-functional argument above supplies that quantifier.

**Attribution:** icekylinx and GPT-6 Astra Pro.
