# Root audit: XP weak optimization with implicit aggregate polytopes

**25 October 2026. Independent internal mathematical review.**

The root reviewer read X1--X20 of
`residual_configuration_bounded_support_xp_solver.md` in full. The
compact dual, signed pricing, uniform interior-ball argument and
finite mixed-primal extraction pass this review. This extends the
previous fully enumerated-row solver to a polynomial runtime in the
number m of explicitly retained residual cuts.

## 1. The aggregate product is represented exactly

The product `K=B(M) times product_j P(f_j)` includes the complete
player-base and aggregate recipient constraints. Its support function
for signed rational weights is optimized by independent greedy
procedures: maximum-weight basis greedy for M, and the positive-weight
prefix construction for each recipient polymatroid. Negative basis
weights are retained when needed to reach full rank; negative recipient
weights receive zero. Deterministic tie breaking supplies genuine
integral product vertices.

Hence a convex combination of returned vertices satisfies every
aggregate constraint. The construction does not replace the aggregate
polymatroid by only the small-subset residual cuts.

## 2. The compact Farkas system has the correct signs

For finite configurations C and aggregate vertices V, the primal links
`sum mu_c e(c)` to `sum lambda_v v`, bounds `sum mu_c h(c)` by b,
and requires `sum lambda_v=1`. Its Farkas multipliers are a signed
linking vector alpha, nonnegative residual-cut prices zeta, and a free
normalization multiplier omega. The column conditions are

\[
 \alpha e(c)+\zeta h(c)\ge0,\qquad
 \omega\ge\alpha v,
\]

while the negative right-side condition is `zeta b + omega < 0`.
Scaling and eliminating omega give exactly X8. This also handles an
empty finite vertex set: its primal is infeasible because no convex
combination can have total mass one, while the eliminated system has
no vertex inequalities. No artificial normalization is then imposed.

For the full product-vertex set, support optimization separates all
vertex inequalities at once. If those and all hard-target column
conditions hold, the returned certificate is a valid original LP
infeasibility certificate.

## 3. Signed convex pricing remains valid

Signed aggregate prices change a type's linear cost coefficient but
do not change convexity: every hinge coefficient is nonnegative.
All nonpositive marginal-cost units form a prefix. Adding any missing
part of that prefix to a feasible count vector weakly lowers cost
and weakly raises value, since values are nonnegative.

Preselecting the whole prefix therefore loses no optimum under any
budget. Its cost G0 is the minimum possible total cost. If C<G0
there is no feasible vector; otherwise the remaining budget C-G0 is
nonnegative and all remaining marginal costs are positive. Binary
chunking, profit scaling and cheaper-prefix compression give an
exact-budget `(1-epsilon)` value solution. The preselected value is
not discounted, so it preserves the same approximation factor.

The strict rational grid now has to allow negative thresholds and
negative budgets. X11 does this correctly. The old nonnegative-price
shortcut for a nonpositive threshold is explicitly not used.

## 4. Pointedness, coefficient bounds and the positive direction

Splitting the signed linking prices into two nonnegative vectors
makes the finite certificate region a polyhedron in the nonnegative
orthant. It is pointed even though the split has redundant directions:
an unbounded ray in both split coordinates is not a two-sided line.
A nonempty finite certificate region therefore has a vertex. Cramer's
rule gives a uniform witness bound from the dimension and the common
integer coefficient bound, independently of C and V.

The proposed theta has one more unit in each positive player-price
coordinate than in its negative counterpart, equal signed count-price
coordinates, and positive residual-cut coordinates. Its product with
every configuration normal is `1+sum h_i(c)`, at least one. Its
product with every aggregate-vertex normal is `r+sum b_i`, because
every player base has total r. This is the key exact identity.

Doubling a bounded witness and adding the small theta perturbation
gives strict column slack, coordinate slack, and at least 3/4 slack
in each vertex inequality. The supplied delta-ball lies in the
enlarged bounded certificate region. Its radius is uniform for every
finite pair C,V. Arbitrary mixed-sign linking systems would not have
this property; it is justified here by the displayed column structure.

## 5. Both generated families are needed for extraction

Each continuation cut is either a box row, a genuine violated
aggregate-vertex inequality, or a genuine violated weak-target
configuration inequality. The current ellipsoid contains the bounded
certificate region for all generated objects. If no hard-target
certificate appears before its volume falls below the uniform ball
volume, the finite primal on both generated families must be feasible.

Solving that finite explicit primal yields nonnegative configuration
weights and a convex combination of true product vertices. Therefore
it satisfies all aggregate constraints and all m retained residual
cuts, not merely rows queried during the run. Every generated
configuration reaches the weaker target. The extraction is explicit
and does not defer a second exponential-row optimization problem.

## 6. Complexity, target search and the exact comparator

The dual dimension is `2q(t+1)+m`. Greedy separation, signed pricing,
rational ellipsoid precision and final LP extraction are polynomial
in that dimension, H and inverse accuracy. Capacities enter through
their binary lengths. Output size and workspace are polynomial in m,
which may itself be large; original-input polynomial space is not
asserted for this fractional optimizer.

The maximization target search has the same correct one-sided
orientation as the earlier solver. Every hard-target failure exceeds
the grid-valued LP optimum. Grid adjacency leaves a saved weak success
at a trial at least as large as the optimum, giving the stated
`(1-epsilon)` approximation. The bounded-box configurations make the
column family finite; an aggregate total-value bound supplies the
failed upper endpoint.

With `m=t sum_(i<=s) binom(q,i)`, the runtime is `(q+1)^{O(s+1)}`
times polynomial input factors. At `s=2(r-1)`, this is an XP optimizer
for the weaker support-restricted LP sufficient for the factor-four
allocation proof. It is not an XP optimizer for the full residual
LP unless all its cuts are retained. It is neither rank-only FPT nor
rank-quasipolynomial, and its output remains fractional.

## Verdict

The full derivation is accepted within its stated count-box model.
No lost sign condition, unpriced aggregate interface, false strict
inequality, or numerical unit expansion was found. The integer
allocation factor and its common-value assumptions remain separate
from this fractional computation. This is internal mathematical
review, without formal verification or external peer review.
