# Independent review of robust unrelated allocation with a common setup charge

**25 October 2026. Reviewer: transfer_frontier. Full review of
`robust_unrelated_common_setup_additive.md`, RA1--RA20: PASS.**

The comparator chooses one genuine player-matroid basis and only then
relaxes its scenario allocations. This review checks that same-basis
fractional comparator, the common setup objective, and the separate
exact-budget integer recoveries. It does not replace the comparator
with a fractional mixture of selected bases.

## 1. Zero feasibility and the attained common setup cost

Because all assignment costs are nonnegative, a common basis can be
used at zero utility exactly when its setup cost is at most every
scenario budget. Minimizing the same setup vector once therefore
gives the exact feasibility test h_0<=min_omega C_omega and a legal
zero initializer.

At an omission node Q, an actual minimum-setup basis I_Q has cost
h(Q). A protected common basis I* contained in Q satisfies
h(Q)<=sigma(I*). Subtracting this same scalar from every scenario
budget leaves at least the residual amount available to I* in that
scenario. Thus every original full-service scenario witness for I*
belongs to the corresponding current region. This holds
simultaneously because the minimizing basis and setup objective are
common, not separately optimized scenario by scenario.

At success, the algorithm must take the attaining I_Q. A full-Q
service allocation supplies its service on that basis, and discarding
counts outside I_Q preserves independent resource feasibility and
nonnegative assignment cost. The actual setup charge of the returned
basis is exactly h(Q). These observations justify both the protected
witness and the output, rather than only a lower bound on setup cost.

## 2. Intersected regions and nonnegative rows

For each residual budget, the original fractional utility region is
bounded, convex, downward and contains zero. Exact membership and
reconstruction are direct resource LPs. A nonnegative separating row
is valid: for a downward nonnegative region, zeroing the negative
coordinates of a supporting normal preserves its support value and
does not decrease its value at a nonnegative query. A strict separator
cannot have all its positive coefficients zero. The normalized outer
support construction can therefore return a strict nonnegative row
with nonnegative right-hand side.

Intersecting the regions does not require a new separation theorem.
A row from any failed scenario is valid for the entire intersection;
passing all explicit scenarios gives witnesses for each one. Original
resources remain on the physical ground when Q changes. The budget
is the current original rational residual, with polynomial bit length.

The stated extreme-point support construction provides a uniform bit
bound even for zero budgets and lower-dimensional regions. Expensive
positive-cost coordinates are not removed merely because one integer
unit would exceed a budget; fractional use can affect the comparator.
The resulting largest-unit bound may be conservative, but is valid.

## 3. The omission invariant and all-input running time

For full target t and weak target b=(1-epsilon)t, the same protected
I* satisfies t 1_(I*) in every current region. If a returned row is
violated by b 1_Q, then

    t a(I*) <= w < b a(Q),
    a(Q without I*) > epsilon a(Q).

The weighted first-crossing certificates therefore include a deletion
set wholly outside I*. Recomputing h and every residual region after
that deletion preserves the same invariant. Different nodes may use
different scenarios without changing the protected basis.

At zero deficit Q=I*, downward closure makes the weak query feasible.
Rank and setup gates cannot reject the protected branch. Thus complete
failure excludes all genuine common fractional full-t bases. The
standard prefix-free recurrence applies with R=1/epsilon and the same
uniform polynomial per-node work, including every failed branch and
all scenario tests.

Starting from forced omissions Z reduces the budget to c-|Z| and
retains the invariant whenever I* avoids Z. This is the exact
extension interface required by the polynomial-space global wrapper.
Its fixed-accuracy sharp base and varying-accuracy rational upper-base
qualification are correctly distinguished. The scenario list affects
the polynomial input work, not the corank exponent or the physical
ground size in the global exponent.

## 4. The rational comparator and final reoptimization

The family of bases affordable under every setup budget is fixed and
nonempty after initialization. For a specified basis, RA16 is bounded
and feasible at zero. Its optimum is exactly the best fractional
common-scenario minimum service on that basis. Taking the maximum over
this fixed finite family gives the stated FOPT.

The denominator argument is derived from this fixed LP family. All
resource right sides are bounded by encoded full ranks, setup sums
have a uniform polynomial bit bound, and the other coefficients are
original values, costs and budgets. Rowwise denominator clearing
produces bounded integer rows. An active square system at a vertex
therefore gives the safe denominator bound D=n!W^n. Its bit length is
polynomial; the possibly exponential number of available rank rows
does not change the maximum number of active independent rows.

After the one-sided rational search on grid
delta=1/(2 B_0 D^2), the saved lower target L is greater than
FOPT-delta. The actual saved basis has exact LP value lambda_I at
least alpha L. If lambda_I<alpha FOPT, the two rational numbers would
differ by at least 1/(B_0 D^2), since both basis LP values have
denominator at most D and alpha=A_0/B_0. But the search inequality
makes their difference less than alpha delta<=delta, a contradiction.
Reoptimizing the saved actual basis thus yields

    lambda_I >= alpha FOPT

without splitting the accuracy into two losses or assuming a positive
fractional lower scale. The zero initializer and a strict external
upper endpoint cover FOPT=0 as well.

## 5. Scenario rounding preserves the common basis

Only after that basis is fixed does each scenario round its own
allocation. Free disposal makes its independent resource vectors into
auxiliary bases. Complement-resource ranks and player prefix ceilings
give one integral full-total face. Maximizing that scenario's cost on
the complement minimizes its original assignment cost while preserving
the lower-prefix inequalities. The resulting utility on selected p
is at least lambda_I-u_(omega,p).

This uses one cost objective per integer assignment vector. Different
scenarios have different vectors, so their separate budgets can be
preserved independently. Their discrete selection I and its setup
fee remain unchanged. Dropping disposal and outside-I real counts
does not increase original cost or change selected utilities.

Nonnegative values additionally give a zero lower bound, proving the
pointwise maximum in RA4 at the same output. The algorithm does not
try to round a common fractional selection dummy across scenarios.

## 6. Limits and source check

The theorem is additive and can return a zero guarantee when the
largest unit absorbs the comparator. It therefore does not solve the
robust zero-or-one positivity obstruction. Arbitrary scenario setup
vectors are also not covered by the minimum of one shared scalar;
their separate feasibility obstruction is substantive.

A fresh primary-source check confirmed the authors and public
cost-preserving-rounding background of Rohwedder, Rouhani and
Wennmann's [ICALP 2025 paper](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.127).
The full recipient-polymatroid lower-prefix argument used here is
supplied by the project's explicit disposal/complement proofs. The
current review makes no exhaustive publication-priority claim.

## 7. Verdict

All RA sections pass. The common attaining setup basis, fixed-basis
fractional comparator, denominator-gap reoptimization and separate
scenario recoveries fit together without a shared-integer-selection
gap. No substantive correction is requested.
