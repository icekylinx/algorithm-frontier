# Root audit of the count-box weak residual-LP optimizer

**25 October 2026. Internal mathematical review of the completed derivation.**

The root reviewer read the full pricing and optimization manuscript,
then reread its revised Section 6 and the independent interior-ball
audit. The weak optimizer in
`residual_configuration_box_pricing_and_weak_solver.md` passes within
its stated coordinate-box scope. The result is fractional and has
single-exponential dependence on the total player count q.

## 1. Pricing and the strict inequality

For nonnegative row prices, each coordinate cost is convex with integer
hinge breakpoints. Its constant-marginal segments admit a binary chunk
representation. Permitting out-of-order segments does not change the
optimal attainable value: move any selected units to the cheapest
prefix of their type, preserving count and value and reducing cost.

Preselecting zero-cost positive-value chunks is safe in that segment
model. The remaining standard profit-scaled knapsack routine preserves
the exact rational cost budget and loses only an epsilon fraction of
the maximum value. Prefix compression after the routine preserves the
guarantee. Quota magnitudes enter logarithmically, through the chunks.

The denominator D of the rational marginal costs makes every count
vector cost a multiple of 1/D. The budget
`(ceil(D w)-1)/D` therefore implements the strict inequality `cost<w`
exactly. For w>0 it is nonnegative. If the returned value falls below
`(1-epsilon)T`, a value-T violating configuration cannot exist.
Otherwise the returned weaker-target configuration is a genuinely
violated column. No false strict inequality is introduced at equality.

## 2. The finite-column certificate bound is uniform

For every finite set of configuration columns, infeasibility of
`A mu <= b, mu>=0` has a normalized nonnegative Farkas witness.
The normalized witness polyhedron is pointed. A vertex is determined
by independent integer equations with bounded coefficients and right
sides zero or minus one. Cramer's rule gives the common bound U0 in
W11. The same bound applies to every generated column subset.

This last uniformity is necessary: a witness bound only for the full
implicit LP would not suffice to extract a feasible restricted primal.
The manuscript uses the stronger, correct assertion.

## 3. The revised interior-ball proof closes the extraction step

The special row signs supply a vector theta with all coordinates one
except the upper-total coordinate two. Its scalar product with every
configuration column is at least one: that column has only one
negative entry, the minus-one lower-total entry.

Starting from a normalized witness beta0, the point
`2 beta0 + gamma theta` has positive slack on all generated columns
and coordinate lower bounds, remains safely inside the enlarged box,
and satisfies the normalization with slack at least 3/4. The supplied
radius delta changes any column or normalization scalar product by
at most gamma/2. Thus every infeasible finite primal produces a
known-radius ball in its bounded Farkas region.

The logarithms of the radius and box size are polynomial in row
dimension and coefficient bit bounds. The proof does not assume
full dimension of a general Farkas system; it derives positive
interior radius from this matrix's signs and redundant total row.

## 4. Volume exhaustion extracts a point for all explicit rows

At a query point, the weak pricing routine either provides an actual
violated weak-target column or certifies all hard-target column
conditions, in which case the current vector is a valid hard-target
infeasibility witness. Early termination in the latter case is sound.

If no such termination occurs, all continuation cuts contain the
weak-target Farkas region. More precisely, the final ellipsoid contains
the intersection of the box, normalization and all retained column
inequalities. This holds even for central cuts, because they are weaker
than the defining violated inequalities and every later retained set
only shrinks that intersection.

Once volume is below the uniform ball volume, the retained-column
primal cannot be infeasible. Solving that finite primal yields weights
satisfying every original enumerated row, not just rows encountered
during separation. The support consists of polynomially many generated
weak-target configurations. This establishes the correct hard/weak
alternative without a lower-dimensional oracle-LP assumption.

## 5. Optimization and boundaries

The LP optimum is attained on the common rational configuration-value
grid because its finite allowed column family changes only at these
values. A hard-target failure lies strictly above that optimum. A
saved weak success need not be feasible at its trial's hard target.
Adjacent successful-lower and failed-upper trials nevertheless put
the lower trial at least at the grid-valued optimum, giving the
claimed `(1-epsilon)` guarantee. No monotone-success assumption is
required. The upper endpoint greater than `V/(1-epsilon)` and the
empty-configuration zero endpoint have the correct meanings.

Rank zero is separated and epsilon can be clipped at 1/2. All costs,
ellipsoid prices, knapsack tables and explicit LP data have polynomial
bit length in the enumerated row size and original input. This gives
`2^{O(q)} poly(H,1/epsilon)`, not a rank-only bound.

For a subfamily of subset cuts, the extension remains valid when all
aggregate resource rows are supplied explicitly. They add nonnegative
linear pricing terms and preserve the positive-direction proof.

## Verdict

The weak fractional solver is accepted for count-box local families.
It is not an integer approximation scheme and does not provide pricing
for a general downward-closed local oracle. Classical knapsack and
ellipsoid primitives remain external mathematical ingredients, cited
in the main note. This audit is internal, without implementation,
formal verification or external peer review.
