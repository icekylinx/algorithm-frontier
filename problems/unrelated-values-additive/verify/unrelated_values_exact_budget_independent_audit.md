# Verification note

**Curated source path:** `sources/checkpoint-p/unrelated_values_exact_budget_independent_audit.md`

The source audit follows.

# Independent audit of unrelated-value allocation with one exact assignment budget

**25 October 2026. Full independent mathematical review of B1--B17.**

Reviewed manuscript:
`unrelated_values_exact_budget_additive_allocation.md`.

The extension passes. It preserves one assignment-cost budget
exactly while retaining the pointwise largest-unit additive utility
loss. The budgeted support oracle, free-disposal base construction,
maximum-total cost optimization, zero-budget reduction, and positive
fractional scale all satisfy their required interfaces. This audit
uses the already completed review of U1--U24 for the underlying
weighted omission method and the two search templates.

## 1. Assignment costs require a different completion argument

The budget constrains resource counts, not only the selected set.
Completing an independent allocation to an original resource base
could add positive cost. The manuscript correctly avoids importing
that unbudgeted completion step.

The resource formulation permits unused units and uses independent
vectors. Costs and budget are nonnegative. Original player loops
can be deleted, since dropping their counts does not increase
cost or decrease any selected utility. Per-type coordinate caps
are incorporated into the recipient ranks as before.

For positive C, a pair with c_pj>C may still be used fractionally.
It must not be deleted when claiming comparison with FOPT_C.
The current manuscript explicitly preserves such pairs. Integer
and fractional comparators both choose one actual permitted basis;
neither permits a fractional mixture of bases.

## 2. The budgeted utility support is polynomially accessible

The allocation polytope X_C contains zero, is bounded by singleton
resource ranks, and is convex. Its lower utility projection is
therefore compact, convex, nonnegative and downward closed. The
budget couples types, so its support generally does not split
into a sum of independent greedy optimizations.

Instead, the inner support problem is a rational LP on q times
the number of types variables. Resource inequalities have exact
separation by submodular minimization, and the budget is an
explicit linear constraint. The variable count and every input
row encoding are polynomially bounded.

There is also a uniform polynomial bound on every vertex of
X_C. Its resource rows have zero-one coefficients and encoded
integer right sides; its additional budget row has the given
rational coefficients. Selecting a full-rank active subsystem
and applying the determinant bound gives a polynomial vertex
encoding in the original data, independent of the number of
implicit subset rows. Lower-dimensional cases are covered by
their active equalities and nonnegativity rows.

Exact optimization can select an extreme optimum by successive
lexicographic refinements. The selected point remains a vertex
of the original bounded polytope and thus has the same uniform
bit bound. There is no dependence on a numerical expansion of
the original capacities.

## 3. The outer support LP returns a genuine nonnegative packing row

The outer LP has a simplex vector a and one support variable t.
Its epigraph inequalities come from vertices of X_C. Their
coefficients are sums of products of original values and the
uniformly bounded vertex coordinates, hence have polynomial
binary length.

For a given candidate a, the inner LP computes h_C(a) exactly.
An attaining vertex supplies a violated epigraph inequality
when needed. The simplex and t-interval rows are explicit, and
t=V is always feasible. Consequently this outer problem is a
bounded, nonempty rational LP with exact polynomial separation.
Nesting the two polynomial oracle computations remains polynomial;
the vertex bound prevents an implicit unbounded coefficient
description from entering the outer problem.

A positive optimum returns a>=0 and the globally valid row
a*z<=h_C(a), with nonnegative capacity and polynomial encoding.
If no positive objective exists, the positive-part separation
argument for a downward region proves membership. That argument
works without full dimension and without separability by type.

Every row is valid for the same fixed U_C during the entire
omission recursion. A membership success is followed by a direct
primal feasibility LP with the original resource inequalities,
the original budget and the selected utility lower bounds.
Thus the proof reconstructs a real fractional budget witness;
it does not rely on membership alone as an assignment.

## 4. The free-disposal rank and its base map are valid

For each resource, add a disposal coordinate with rank
fbar(S)=f(S) without that coordinate and fbar(S)=f(P) with it.
This rank is monotone and integral. Its mixed submodularity case
reduces to f(B)>=f(A intersection B) when only A contains the
disposal coordinate. If neither or both contain it, submodularity
is immediate.

Given an independent x, put its unused total f(P)-x(P) at the
disposal coordinate. The resulting total is f(P). Subsets without
disposal use the original inequalities, while a subset with
disposal has mass at most the full total. Conversely, restricting
an extended base to real players gives an original independent
vector.

Disposal has zero value and zero cost, so this operation preserves
every real utility and the fractional cost exactly. It adds one
coordinate to each resource, but no candidate player, and thus
does not change the selection corank q-r. All unused counts
remain binary encoded.

## 5. The maximum-total face is essential to the cost proof

Complement the extended resource bases by their singleton-cap
vectors. The resulting fractional y is feasible in the intersection
of the direct-sum dual resource polymatroid and the integral
per-player prefix-cap polymatroid. Its total L is exactly the
direct-sum total rank, hence the maximum possible intersection
total.

The face of this intersection with total L is integral: a
maximizing face of an integral polytope has only integral
vertices. The original fractional y belongs to it. Maximizing
the linear assignment-cost expression c*y on this face therefore
has an integer optimum y' with c*y'>=c*y.

This order of operations matters. Maximizing cost over arbitrary
common independent vectors need not preserve full resource totals.
The manuscript explicitly imposes the maximum-total face first.
Weighted polymatroid intersection or exact LP optimization plus
vertex selection implements the required objective in polynomial
oracle time.

Full total forces every dual resource component to be a base.
Complementing y' therefore gives nonnegative integer extended
resource bases. If a denotes the fixed singleton-cap vector,

\[
                  c*x'=c*a-c*y'\le c*a-c*y=c*x\le C.
\]

The cost comparator is the reconstructed fractional witness's
actual cost. No slack or expectation enters this inequality.

## 6. Utility prefixes survive the cost optimization

The maximum-total, maximum-cost point still satisfies every prefix
cap. At each real player the same telescoping proof from the
unrelated-value manuscript therefore loses at most u_p in original
utility. Its type ordering can differ from every other player's
ordering. The zero-valued disposal coordinate causes no utility
loss, regardless of its arbitrary type order.

A resource coordinate with singleton rank zero is identically
zero in the original and complement counts. Its value can be
set to zero or its type omitted at that player's prefix proof.
This also applies to coordinates newly capped to zero when C=0,
and justifies the current definition of u_p using only eligible
pairs. An unusable high-value pair does not enlarge the needed
rounding loss.

Discarding disposal counts gives original independent resource
vectors. Discarding counts outside the selected set preserves
its utility and cannot increase cost because assignment costs
are nonnegative. Thus the final allocation respects the original
budget exactly and proves the stated pointwise lower bound.

There is only one cost objective in this construction. Choosing
an optimum for that objective does not preserve several unrelated
assignment budgets simultaneously. The manuscript correctly
limits the claim to one such budget.

## 7. The integer-comparator search uses utility, not cost, granularity

Every integral utility is on a common grid g determined by the
original values. The costs and budget need not be multiples of g.
Thus OPT_C is still a grid point, and V+g remains a valid
external infeasible utility upper target.

The service gap on U_C with t=T and b=(1-epsilon)T has the
same Gamma(1/epsilon)^c runtime as the unbudgeted gap. Failure
excludes even a fractional budget-feasible target, so it is
sound for integer OPT_C. At adjacent upper and lower grid
endpoints, the saved lower target is at least OPT_C. One final
budgeted reconstruction and cost-preserving rounding then gives
the first line of (B2).

The initial zero allocation respects every nonnegative budget.
The search does not treat success as full target feasibility
or require monotone successes. Nothing about rational costs
changes its utility-grid argument.

## 8. Zero budget is an exact coordinate restriction

When C=0 and costs are nonnegative, every positive-cost coordinate
must vanish even in a fractional allocation. For type j, let
Z_j be its zero-cost players. The rank f_j(S intersection Z_j)
represents exactly the old resource restricted to Z_j and
extended by loops outside it.

For necessity, every feasible zero-supported vector obeys each
original subset inequality on S intersection Z_j. For sufficiency,
the new inequalities imply the old ones by monotonicity. Thus
the preprocessing preserves both integer and fractional feasible
regions, and hence both optima. All remaining usable coordinates
are free, so the unbudgeted positivity test and averaging lower
bound apply without division by the budget.

This argument is qualitatively different from discarding a pair
whose individual cost exceeds a positive budget. The latter can
be fractionally affordable and is correctly not done.

## 9. A positive fractional scale survives any positive budget

For C>0, a positive-valued eligible pair has a feasible one-unit
resource vector, even if that vector exceeds the budget. Choose
one such pair for each member of a permitted r-set and average
the r whole-resource allocations. The averaged vector is resource
feasible, gives utility at least v_min/r at each selected player,
and has total cost at most C_max.

Scaling by alpha=min{1,C/C_max}, or alpha=1 when C_max=0,
makes the budget feasible while preserving all independent
resource constraints. This proves and constructs
lambda_C=alpha*v_min/r>0. A very large cost or very small
positive budget only increases the encoding length logarithmically;
it does not cause iteration over numerical resource units.

If no permitted set lies in the positive-eligible player set,
every permitted set contains a player of zero attainable utility,
so FOPT_C=0. The initial selector must separately report when
the entire permitted family is empty, as in the inherited
general-selector theorem. For a nonempty family this positivity
test is exact. At C=0, use the same reasoning after the zero-cost
rank restriction with alpha=1.

## 10. The fractional-comparator search and complexity close

Use quota loss epsilon/2, a saved feasible lower target lambda_C,
and an external upper target V+lambda_C. Failure excludes FOPT_C
at that target. Once the endpoint distance is at most
epsilon*lambda_C/2, the lower endpoint is at least
(1-epsilon/2)FOPT_C, because lambda_C<=FOPT_C.

Its saved fractional service is at least another factor
1-epsilon/2 times that lower endpoint, hence at least
(1-epsilon)FOPT_C. Rounding gives the second line of (B2).
The initial witness already meets the saved-service condition,
including immediate termination. Midpoint precision grows by
only O(log(1+V/(epsilon*lambda_C))) bits.

All support, reconstruction and rounding LPs have polynomial
dimension and polynomial-bit strong separators. The sink increases
the product ground only to (q+1) times the number of types.
The weighted omission tree and its polynomial-space implementation
therefore retain their previous Gamma bases and space bounds.

The public ICALP 2025 comparison was already freshly verified in
the U audit. Ordinary-item additive rounding with cost preservation
is established background; the manuscript keeps that distinction
and does not claim an unconditional multiplicative improvement
for arbitrary unrelated Budgeted Santa Claus instances.

No gap was found in B1--B17. The exact budget follows from a
single cost objective on an integral maximum-total face, rather
than from an unsupported budget-preserving base extension. This
is independent internal mathematical review, not formal
verification or external peer review.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
