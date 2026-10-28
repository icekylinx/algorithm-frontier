# Rational realization of the sharp vertex-color certificate

## Scope

The [reference backend](../reference/vertex_colors.py) constructs the exact
fixed-order certificate of Sections 1–5 of the
[canonical manuscript](colored-graph-and-vertex-failure-certificates.md).
It covers disconnected undirected multigraphs, arbitrary correlated vertex
color classes, signed rational weights, permanent input-position tie breaks,
all allowed color-failure sets and all ordered edge prefixes. It stores only
original retained edge records and the vertex color list.

The mixed/list-color constructions and one-color dynamic-MSF acceleration
remain mathematical results; this implementation does not claim those
interfaces. Its rational arithmetic is exact, without numerical tolerances.

## Construction and correctness

Delete validated loops, then compute connected components using every other
original edge. An isolated vertex forms its own original component. For each
component, cap the Vandermonde dimension by both one more than the failure
allowance and the component's number of occurring colors. Assign all colors
distinct positive integers. Repeated colors receive the same vector; the
occurring component vectors span the chosen dimension.

For each nonloop edge, place its opposite endpoint's Vandermonde vector at
each endpoint block with opposite signs. Perform exact rational incremental
elimination separately in each original component, while processing the
single global order `(weight, original ID)`. Component rows are disjoint,
so this is exactly the greedy basis of the block-diagonal global matrix.
Every discarded edge is spanned by accepted predecessors in that same
component. IDs and weights of accepted edges are copied without alteration.

For any allowed failed-color set leaving a component nonempty, the root
polynomial for failed colors occurring there has degree below the chosen
dimension. Its coefficient functional vanishes exactly on failed vertices.
Multiplying each block by its own vertex's survival factor sends a lifted
edge to zero if an endpoint failed, and otherwise to a nonzero scalar times
its ordinary incidence column. Applying that map to every predecessor-span
relation gives equality of surviving incidence spans at every original
ordered prefix. The completely failed component is empty and needs no
functional. Thus the retained and original graphs have identical surviving
prefix connectivity partitions.

An original edge absent from the certificate cannot increase surviving
prefix rank: its incidence column is spanned by retained predecessors.
Every accepted original Kruskal edge is consequently retained. The query
scans retained records in the same fixed order, so it returns exactly the
same original canonical forest, not merely a forest of equal weight.
Negative weights and weight ties cause no change to this argument.

For the size claim, every symmetric matrix on the component's Vandermonde
space supplies an annihilating row via its action on all vertex vectors.
The map is injective because those vectors span. Subtracting the symmetric
matrix dimension from the component row count gives the sharp bound in
Section 2 of the canonical manuscript. Sum over components. The code checks
this bound on the final number of retained records; isolated vertices
contribute zero.

## Arithmetic and query work

The component Vandermonde dimension never exceeds its vertex count, even
for a binary huge failure allowance. Coordinate degrees and integer-code
bit lengths are polynomial in the explicitly supplied vertex list.
Rational echelon entries are ratios of minors of this bounded-bit input
matrix, so exact arithmetic has polynomial bit complexity. The conservative
field-operation and workspace bounds in Section 4 of the canonical manuscript
apply, in addition to cost sorting and input processing.

Queries use the stored vertex list and retained edges only. Disjoint-set
initialization is linear in the vertex count; a full scan performs at most
two color tests and one union per retained edge, plus writing the answer.
No optimization over the discarded graph and no activation elimination
occurs at query time. The returned original-ID list is a forest report,
not an independently checkable optimality certificate for an absent input.

## Independent finite verification

The checker compares every permitted failed-color set and every ordered
prefix on its small fixtures. Its comparator uses graph reachability flood
fills rather than linear elimination or the backend's disjoint-set routine.
A separate greedy scan using these partitions computes canonical forest IDs.
It covers complete small simple-graph/color assignments, seeded multigraphs
with loops and signed rational ties, empty/disconnected graphs, isolated
vertices, absent-color queries and huge failure allowances.

The classical core-clique/outer-star example is replayed over all tested
failure budgets. Every original edge is retained and the component bound is
met exactly. These tests support the implementation; the general bound and
all-query guarantee follow from the activation proof above.

**Attribution:** icekylinx and GPT-6 Astra Pro.
