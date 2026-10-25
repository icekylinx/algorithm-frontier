# Independent audit of one-value allocation with arbitrary assignment costs

**25 October 2026. Full independent review of O1--O16.**

Reviewed manuscript: `one_value_exact_budget_corank_two_allocation.md`.
The theorem passes: it returns at least ceil(K*/2) integer units
on one actual original player-matroid basis, respects one arbitrary
nonnegative assignment-cost budget exactly, and runs in
(27/4)^c poly(H) time with polynomial workspace. No price-diversity
parameter or additive unit loss is needed in this one-value model.

## 1. The integer comparator and original ground are precise

The comparator K* is the integer minimum unit count, not the
fractional service optimum. This distinction is necessary when
a positive budget allows a small fractional allocation but no
integer unit. Multiplication by the common positive rational
value v changes utilities without changing quota feasibility.

Removing original player-matroid loops and restricting the
recipient ranks is safe because no selected basis uses those
players. Counts there can be dropped, preserving every downward
resource constraint and reducing nonnegative cost. Zero extension
recovers an allocation on the original instance. Resource bases
need not be exhausted, so restriction does not accidentally
introduce a mandatory disposal obligation.

The fixed budgeted fractional region is kept on this original
loop-deleted player ground throughout omission branching. A
smaller candidate ground is queried by inserting zeros in its
omitted coordinates; no resource contraction or changed budget
is introduced.

## 2. The projected count separator has the required nonnegative rows

The allocation polytope X_C is nonempty, bounded and convex. The
lower count projection U_C is compact and downward closed. Its
support at a nonnegative vector a is the exact LP O7, including
the original cost row. Recipient separation is by submodular
minimization of f_j(S)-x_j(S).

All vertices of X_C have a uniform polynomial rational encoding:
resource rows have zero-one coefficients and integer right sides
bounded by queried total ranks, while the one cost row uses the
original rational data. This controls the coefficients in every
outer epigraph inequality of O8. The outer LP has q+1 variables,
a simplex normal a, and a valid bound 0<=h<=S_tot. Its inner
support oracle returns an attaining extreme point, so exact
polynomial separation and optimization apply without enumerating
the vertices.

For a positive optimum the returned row a*y<=h_C(a) has a>=0,
nonnegative right side, and strict violation by the query. If no
positive optimum exists, any signed strict separator of a
nonnegative query can be replaced by its positive part using
downward closure. The support does not change, and the scalar
product at the query cannot decrease. Normalizing gives an
outer-LP violation, a contradiction. This proves exact membership
and nonnegative-row separation, including lower-dimensional
regions.

C=0 and S_tot=0 do not invalidate this argument. The simplex
still exists because q>=r>=1; h may be fixed to zero, and exact
LP handles that lower-dimensional face. Reconstruction uses
the original budgeted primal rather than separate affordable
components.

## 3. The K>=2 gap has the stated off-promise time

For integer K>=2, b=ceil(K/2) is a positive integer strictly
smaller than K. Any integer K-quota allocation on an M-basis
supplies the stronger fractional service K*1_I in U_C. The
weighted prefix-free omission theorem therefore returns an
actual M-basis with b*1_I in U_C or soundly excludes the full
fractional quota, and hence the original integer target.

The worst ratio K/(K-b) is three, attained at K=3. Monotonicity
of Gamma gives the uniform (27/4)^c bound. The known omission
theorem pays for all local enumeration states and failed selectors
on unpromised inputs, so infeasible targets in the outer search
do not escape the running-time bound.

If a terminal query first established service on a larger Q,
the restriction selector returns I subseteq Q. Dropping other
coordinates preserves the same budgeted region. This supplies
exactly the fixed-basis fractional witness required for recovery.

## 4. Integer quota recovery is stronger than additive rounding

First remove all outside-I counts and trim each selected player's
type coordinates until its total is exactly b. This is a
coordinatewise decrease, preserving resources and not increasing
cost. The resulting fractional point has total br.

On I times the type set, the direct-sum recipient rank A in O13
encodes every resource, while the partition rank B in O14 enforces
the per-player upper count b. Both ranks are integral, since b
is integer. Their polymatroid intersection is integral. The
fractional witness attains total br=B(E), so the maximum-total
face of total br is nonempty and integral.

Minimizing the one actual assignment-cost objective on that face
has an integer optimum of cost no greater than the fractional
witness's cost, which is at most C. Full total and the individual
upper bounds force exactly b units at every selected player.
The resource coordinates remain original independent vectors.
There is no per-player loss to be paid after this operation.

The proof correctly does not assume that adding the budget
inequality preserves integrality. It optimizes that cost over
an integral face and compares its integer optimum with an
already budget-feasible fractional point. This distinction
also explains why the proof preserves one cost budget but does
not automatically preserve several unrelated budgets.

The product ground has polynomial size r times the number of
types. Although b and br can be numerically large, all ranks,
right sides, objectives and the total equation have polynomial
binary encoding. Exact weighted polymatroid intersection, or
exact separated LP followed by an optimum vertex, implements
the step without expanding resource supplies into copies.

For a prescribed I the same construction is an exact feasibility
and minimum-cost test at every integer b. Nonnegative costs and
trimming make feasibility downward in b, so fixed-basis integer
optimization is polynomial by binary search. This does not
solve the combinatorial choice of I; the corank gap handles that
choice.

## 5. The one-unit gate uses exactly two matroids

The t=b=1 case is excluded from the positive-gap invocation.
Instead form one eligible player-type pair for every assignment
with f_j({p})>=1. The direct sum of the type-specific Boolean
recipient matroids ensures feasible one-unit resource assignments.
The parallel extension of the original player matroid enforces
distinct original players and M-independence of their owners.

A common independent set of size r is exactly a one-unit
assignment to an actual M-basis. Conversely any integer
allocation with at least one unit at every selected player can
be trimmed to such a representation without increasing cost.
Minimum-cost matroid intersection at cardinality r consequently
decides the budgeted one-unit problem exactly.

The pair ground is polynomial and independent of the numerical
resource ranks. Zero cost, zero budget, or missing eligible types
are ordinary exact feasibility cases. Adding a second arbitrary
player matroid would introduce another independence requirement
to this gate; the manuscript correctly does not infer that
extension from its positive-quota generic selector theorem.

## 6. Integer target search proves the rounded-half guarantee

The total-count bound U_0=floor(sum_j f_j(P)/r) is an original
integer upper bound on K*. Use external upper U_0+1, lower zero
and an arbitrary M-basis with zero counts. At each midpoint,
the exact K=1 gate or the K>=2 gap/recovery either returns the
claimed integer quota or soundly excludes the original target.

Thus the upper endpoint remains strictly above K*. A success
need only attain ceil(K/2), so the lower endpoint is not claimed
to be a full-target feasible value. At adjacency U=L+1 and
U>K* imply L>=K*. The saved allocation therefore gives
ceil(L/2)>=ceil(K*/2) units. If L=0, the same invariant implies
K*=0. No monotonicity of successful answers is assumed.

There are logarithmically many calls in the binary total-rank
bound. The target search, exact recovery and the pair-matroid
gate add only polynomial factors and preserve polynomial space.
The c=0 case is also directly exactly solvable through fixed-I
optimization, as the manuscript states.

## 7. The strict-below-two oracle boundary remains valid

For q>r>=2, the hidden rank in O16 is normalized, monotone and
submodular by its nonincreasing cardinality increments and the
single slack-consuming perturbation at A. Its total rank is
2r, and 2*1_A is feasible. Any other r-set I has f_A(I)=2r-1,
so no integer allocation with minimum greater than one can use I.
Hence K*=2 and every factor strictly below two identifies A.

Only a rank query at A distinguishes its oracle from the common
baseline. With two candidate r-sets unqueried, the same transcript
requires incompatible valid outputs. At least binom(q,r)-1
=binom(q,c)-1 queries are therefore necessary in the worst case.
Taking fixed c above a proposed uniform polynomial degree and
then growing q excludes an F(c)poly(H) guarantee below two in
this recipient-rank oracle model.

The construction uses zero costs and zero budget, so it lies
inside the present class. It does not identify an optimal
exponential base, imply hardness for explicit ordinary item
representations, or contradict exact polynomial optimization
once the selected basis is fixed. Those distinctions are
correctly retained in the manuscript.

All substantive interfaces in O1--O16 pass independently. The
claimed stronger recovery relies on equal unit values, an
integer output quota, downward independent resource allocations,
and a single nonnegative assignment-cost objective; these are
all explicit assumptions of the theorem.
