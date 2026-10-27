# Binary pricing and original residual-configuration realization

The [fractional reference](reference/fractional.py) implements subset cuts,
signed convex-cost pricing, aggregate greedy support, actual weak
configuration/vertex generation, and original-grid fractional optimization.
It complements the existing [count representation](reference-realization.md).
Its finite generation and exact Bland-pivot costs are separate from the
polynomial-in-retained-cuts ellipsoid algorithm proved in the
[bounded-support companion](../../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md).

## 1. Original data and the fractional output

`Residual(player_rank, resource_ranks, values, quotas=None, support=None,
cut_sets=None)` validates complete original integral rank tables and a
player-matroid table. Each local family is exactly an integer coordinate
box, with owner-major quotas at most the original singleton ranks. Values
are either one common nonnegative exact rational per type, or an owner-major
matrix of nonnegative exact rational profits. The latter is the
fractional-only value corollary; it does not extend the intrinsic-value
integer allocation theorem.

The default retains every resource/subset cut. A nonnegative `support`
retains exactly subsets of at most that size. Alternatively, `cut_sets`
lists explicit distinct resource/subset pairs. Player-base and aggregate
resource constraints are always retained, including when a chosen residual
cut family does not imply them. Binary capacities stay numerical, and all
original labels, including player loops, remain named.

`Point(target, masses)` has positive exact rational `Mass` records on
original `Configuration(owner, counts)` objects. Its standalone verifier
checks original local integer boxes, the target of every positive-mass
configuration, every original player and resource subset inequality, the
original player-base total, and every retained residual cut. No pricing,
support, LP, column-generation or allocation producer is called. Strict
record and coordinate types prevent a supplied object from overriding the
computed objective or feasibility. The output is fractional configuration
mass, not one integer allocation or one actual selected basis.

Rank zero explicitly returns empty mass at target zero; the nontrivial
finite optimum theorem concerns positive rank. Empty resources and zero
profits are handled by the same zero initialization and hard-target gates.

## 2. Subset cuts and dependent reservations

**Lemma 1.** The native retained subset rows are precisely the requested
residual-capacity relaxation, and `reserved_basis` preserves availability
of a possibly dependent original reservation.

**Proof.** For a resource and subset `S`, native coefficients are exactly
`max(0,n_j-(f(S union {p})-f(S)))`, with right side `f(S)`. The
[subset-compression theorem](../../manuscripts/allocation-and-scheduling/recipient-polymatroid-subset-cut-compression.md)
proves that all such rows are equivalent to every feasible integral
reserved-count cut. Its proof applies convexity of reserve-cut violation
on the real polymatroid and identifies each greedy vertex cut with the
subset spanned by that vertex. On a support-restricted coordinate face,
the same argument uses exactly subsets within the same support budget.
This is exact equivalence, without count enumeration or a general
polymatroid-to-matroid decomposition assertion.

For dependent reservation counts, the natural rank restricted to each
growing owner prefix is the rank of the original polymatroid restricted
by that reservation box. Successive prefix differences form an integral
greedy base of that box. Thus `reserved_basis` returns an original
independent subvector of the reservation, of exactly its natural rank.
It represents a basis of the reserved natural-matroid set, so it spans
that set and has identical whole-owner availability. This supplies the
feasible-reserve representative needed by the residual lower-cover proof.
No reserved unit identities are expanded.

`separate_subsets` evaluates the stated rows directly on an explicit mass
list. Enumeration is over the retained original subsets and mass support,
with exact rational arithmetic. This proves the lemma.

## 3. Signed convex-cost pricing with an exact budget

**Lemma 2.** `price` returns an original integer box vector within its
supplied exact signed-cost budget, with at least its requested fraction of
the best nonnegative value. It returns `None` precisely when no vector
meets that cost budget.

**Proof.** Per-type cost has a signed linear term and nonnegative hinge
weights at integer breakpoints. Marginal unit costs are nondecreasing.
The code sorts only supplied breakpoints and endpoints, producing a
constant-cost segment for each interval between them. Capacities remain
binary integers. Fill the entire initial prefix of nonpositive marginal
costs, including free and zero-profit units. Its cost is the minimum
possible cost in the box. Any feasible vector can be extended to contain
this prefix without increasing its cost or decreasing its nonnegative
value. If its cost already exceeds the budget, infeasibility follows.

Subtract that exact, possibly negative prefix cost from the budget. All
remaining segments have positive cost. Binary chunks of each segment
represent every integer count in its capacity with logarithmically many
items. Temporarily ignoring inter-segment precedence is exact for the
best value: move any chosen units of one type to its cheapest prefix,
preserving count and profit and decreasing cost. Conversely every legal
prefix count has a chunk representation.

Discard positive-cost zero-profit chunks and chunks individually more
expensive than the remaining budget. If any items remain, each remaining
item individually fits. Their maximum profit is therefore at most the
optimal remaining profit. The code scales profits with
`delta=epsilon*maximum_profit/number_of_items`, then keeps the minimum
exact rational cost for each rounded total. Dropping items of rounded
profit zero loses less than one scale unit per such item, which is included
in the same rounding estimate. An optimal subset loses less than the
number of items times `delta`; maximizing rounded total therefore retains
at least the requested fraction of the optimal remaining profit. The
prefilled nonnegative profit preserves that fraction for the full problem.

Reconstruct counts, compress them to their cheapest type prefixes, and
evaluate the original signed hinge cost. This stays within the exact
budget. All original counts remain within their original box. This proves
the lemma, including empty item sets, zero budgets, negative budgets and
nonpositive minimum costs.

**Lemma 3.** `strict_price` either returns a genuinely violating
configuration at the weaker target or correctly excludes every violating
configuration at the hard target, for any rational sign of the threshold.

**Proof.** A common denominator of the original linear and hinge prices
puts every integer configuration cost on its reciprocal integer grid.
The code computes exactly the largest point of that grid strictly below
the threshold, including negative thresholds. Lemma 2 is called at this
exact cost budget. A returned value reaching the weaker target is a
genuine strict violation. If it does not reach that target, no hard-target
configuration could fit the budget, by Lemma 2's approximation guarantee.
Equality to the price threshold is never treated as a violation. This
proves the lemma without any arbitrary downward-closed local oracle.

## 4. Aggregate support retains signed prices and original ranks

**Lemma 4.** `aggregate_vertex` returns a genuine integral maximizing vertex
of the original product of player-base and resource-independent polytopes
for every signed rational aggregate objective.

**Proof.** Maximum-weight matroid-basis greedy keeps all needed negative
weights until original rank is reached. For each resource independent
polymatroid, order only positive weights and use the exact original rank
differences on its prefixes; nonpositive coordinates receive zero.
The standard telescoping greedy inequality proves optimality for every
feasible vector. These integral greedy vectors are vertices of their
respective polytopes; their product is the claimed aggregate vertex.
Neither a restriction of physical resource rank nor configuration pricing
is hidden in this operation. This proves the lemma.

## 5. Normalized finite Farkas generation and direct primal extraction

Let `e(c)` encode one original configuration's player and aggregate count
coordinates, let `h(c)` encode its retained hinges, and let `b` be the
retained cut right sides. For configurations `C` and aggregate vertices
`V` generated so far, the finite primal asks for nonnegative weights with
`sum(mu*e)=sum(lambda*v)`, `sum(mu*h)<=b` and `sum(lambda)=1`.
The compact dual uses signed `alpha`, nonnegative `zeta`, configuration
conditions `alpha*e+zeta*h>=0`, and vertex conditions
`alpha*v+zeta*b<=-1`.

**Lemma 5.** The native normalized homogeneous LP either supplies that
finite dual or extracts a valid finite primal directly from its LP dual.

**Proof.** Split `alpha=beta_plus-beta_minus` and append `zeta` to the
nonnegative vector `beta`. Put `a_c=(e,-e,h)` and `b_v=(v,-v,b)`.
The native LP maximizes nonnegative margin `t`, subject to

```text
-a_c * beta <= 0              for generated configurations
 b_v * beta + t <= 0         for generated aggregate vertices
 sum(beta) <= 1
 t <= 1
 beta >= 0, t >= 0
```

Every right side is zero or one, so the origin is feasible. The canonical
exact [Bland simplex](../selected-flow/reference/concurrent.py) applies
directly, and its primal/dual certificate is checked on the constructed
matrix. A positive optimum scales `beta` by the margin and gives the
finite dual conditions above.

At zero optimum, call the LP-dual multipliers on configuration rows `u`,
on vertex rows `v_weight`, and on the last two bounds `eta,xi`. Dual
objective zero and nonnegativity force `eta=xi=0`. The margin column
requires the sum `L` of vertex multipliers to be at least one. The two
opposite signed aggregate-coordinate inequalities force exact equality
between the `u`-weighted configuration aggregates and the vertex-weighted
aggregates. The hinge-coordinate inequality gives
`sum(u*h)<=L*b`. Divide all these multipliers by `L`. The resulting
configuration and vertex weights satisfy the finite primal exactly.
In particular their aggregate lies in the convex hull of genuine product
vertices and hence satisfies every original aggregate row, including rows
never explicitly generated. This proves the lemma.

**Theorem 6.** `weak_target(T,epsilon)` either returns a feasible original
fractional point at the weaker target or correctly reports original hard
target infeasibility.

**Proof.** Start with empty generated families and apply Lemma 5. At
positive margin, scale to the finite dual. Lemma 4 finds an exact
maximizing aggregate vertex. If it violates a vertex condition, append
it. Otherwise all aggregate vertices satisfy their dual conditions.
For each owner, the signed count coefficients and nonnegative hinge
coefficients are exactly the cost input to Lemma 3. A returned weak column
violates its configuration dual condition and is appended. If every owner
certifies no hard violation, the dual is valid for the full hard-target
configuration family and every aggregate vertex. Farkas' lemma therefore
proves hard-target infeasibility.

Every appended object is new: old objects satisfy the finite dual, whereas
the appended object strictly violates it. Both object universes are finite.
Thus the process terminates. At zero margin Lemma 5 extracts an original
feasible point supported on generated configurations, all of which have
already met the weaker target. The final original verifier checks it.
This proves the theorem. Requested accuracies above one half use one half
internally, giving at least the requested retention.

## 6. Original-grid weak optimization

**Corollary 7.** `optimize` returns a feasible fractional point attaining
the requested fraction of the optimum of its precisely retained relaxation.

**Proof.** All local configurations have values on the gcd grid of the
original exact pair profits. The finite allowed configuration families
change only at such values, so the true optimum target is on that grid.
The original aggregate ranks and largest pair values give a finite total
utility upper bound for positive player rank. An external trial whose weak
target exceeds that bound cannot succeed. The zero-bundle basis point
initializes target zero. Binary search saves weak feasible points on
success and lowers the upper endpoint only on sound hard-target failure.
The failed upper endpoint remains strictly above the true optimum. At
adjacent grid endpoints, the saved nominal lower target is at least that
optimum, regardless of nonmonotone weak successes. Its returned point has
the claimed fractional retention. Zero profit and rank-zero conventions
are handled before this search. This proves the corollary.

## 7. Complete mathematical dependency audit

The [residual comparator](../../manuscripts/allocation-and-scheduling/recipient-polymatroid-residual-configuration-relaxation.md)
uses a feasible basis of each actual dependent reservation. Clipping a
configuration at those availabilities stays in its downward-closed local
family. Its failed certified availability scan bounds retained expected
value, while the residual cuts bound exactly the lost value. Eligible
player mass is at least the original rank deficit, yielding the strict
lower cover. Only a support budget twice one less than the original rank
is needed in normalized states. Discarding fat-containing configurations
and downscaling all-small mass preserves every nonnegative residual row;
the derived player rank never increases. Integer quotas use the separate
non-strict integral loss bound, so the critical small-quota growth boundary
is unchanged.

For [scaled recipient matroids](../../manuscripts/allocation-and-scheduling/scaled-recipient-matroids-binary-configuration-transfer.md),
each supplied component remains separate. Contracted-rank subadditivity on
independent original player sets bounds the fractional weighted
availability loss by the actual reserved natural rank. The local
hypergeometric clipping argument uses only downward closure, and its
expectations supply the lower cover. Its Boolean fat union can clip binary
copy multiplicity to the original player count. Components are not merged:
equal intrinsic value does not imply equal fractional configuration data.
This verifies the stronger component comparator with no recipient-rank
factor and no numerical copy expansion.

For the [count-box solver](../../manuscripts/allocation-and-scheduling/residual-configuration-box-pricing-and-weak-solver.md)
and [implicit-aggregate XP solver](../../manuscripts/allocation-and-scheduling/residual-configuration-bounded-support-xp-solver.md),
the breakpoint/chunk, strict-grid and signed-prefix arguments match Lemmas
2–4. The mixed compact dual has split dimension twice the aggregate
dimension plus the number of retained cuts. An integer coefficient bound
uniformly covers all allowed columns and aggregate vertices. A pointed
nonnegative Farkas system has the stated determinant-bounded vertex.
Increasing player-positive split coordinates to two while all other
direction coordinates equal one gives positive slack on every column;
its aggregate-vertex scalar product is the original player rank plus
the sum of cut right sides. The displayed perturbation therefore gives
a uniform interior ball for every finite mixed subsystem. Rational
ellipsoid containment and volume decrease then make the final generated
primal feasible. Keeping aggregate vertices as well as configurations
makes that final primal explicit. This is the missing interface that
subset separation alone would not supply.

Thus the mathematical weak optimizer is polynomial in the number of
retained cuts and inverse accuracy, with full accuracy encoding charged.
Subsets of bounded support give the stated XP dependence; all subsets
give singly exponential dependence on the total owner count. The
player-dependent-profit corollary changes only local nonnegative profits
and the original target grid, and remains fractional-only. Arbitrary
downward-closed local families are allowed by the separate allocation
comparator only through its paid certified availability oracle, and are
not given a pricing solver here.

The [configuration-gap proofs](../allocation-lower-bounds/configuration-gaps.md)
also match these comparators: merging components permits an aggregate
gap approaching player rank; even the full residual relaxation retains
an exact gap of two. Neither is a complexity lower bound against integer
optimum or a claim of integral fractional output.

## 8. Actual reference cost and remaining software boundaries

If binary segment splitting yields `N` retained positive-profit chunks,
the DP has at most `O(N**2/epsilon)` rounded totals and
`O(N**3/epsilon)` elementary updates. Counts, exact costs, profits, selected
item bit masks and full accuracy numerators/denominators have charged bit
costs. Prefix shifts, segment construction and chunk generation loop over
original breakpoints and binary digits, never individual supplied units.

The native outer implementation uses Theorem 6, not the polynomial-cut
ellipsoid procedure. Its iterations are bounded by one plus the number of
possible original weak configurations plus the number of aggregate
vertices. The former is at most the sum, over owners, of the products of
one plus each local quota; it may be enormous in binary encoding. The
aggregate vertex count is bounded by the number of original matroid bases
times the products of the ordered-subset greedy counts for resources.
All generated objects are stored. A normalized LP with `D+1` variables
and `R` rows has the canonical finite Bland pivot bound from its number
of possible bases, with exact rational bit costs. Neither generation nor
these pivots is asserted polynomial in the retained-cut description.

This is actual column generation using binary FPTAS pricing and exact
aggregate support, with no exhaustive configuration list and no hidden
general local oracle. It does not claim the fast theorem's time or
workspace, and it does not implement the full player-layer integer
allocation algorithm. The fast mathematical constructions and the
finite executable realization remain separate evidence.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. **License:** Apache-2.0.
