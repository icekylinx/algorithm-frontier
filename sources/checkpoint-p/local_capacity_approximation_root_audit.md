# Root audit: local feasibility, compressed supplies and approximate bundle search

**25 October 2026. Internal mathematical review completed.** This is
a proof and interface audit, not a formal verification or external
peer review. The accepted current-blocker player-matroid exchange,
signature count, sharp star charge and matroid-union construction are
explicit imports. The new adapters audited here are:

* `player_local_downward_closed_allocation_extension.md`;
* `binary_resource_capacities_compressed_current_blocker.md`;
* `approximate_available_bundle_oracle_allocation.md`.

The separate reviews in `item_matroid_allocation_public_scope_audit.md`,
`binary_resource_capacities_independent_audit.md`, and
`approximate_available_bundle_oracle_independent_audit.md` are also
recorded. Their public-comparison conclusions are kept separate from
the new mathematical implications.

## 1. Downward-closed player constraints

For each player, an exact maximum-common-value oracle on the currently
available physical items is sufficient. Its return is pruned to a
minimal bundle above the allocation threshold; removing items preserves
local feasibility. The resource intersections, player circuits and
earliest-layer truncation rules are unchanged.

The replacement LP argument is sound. A perspective marginal is a
scaled convex combination of feasible local bundles. Intersecting
each such bundle with the available items remains feasible. If every
available feasible bundle has value below B, the available part of a
positive player marginal has value strictly below B times its player
coordinate. Summing over eligible players and using B<=T gives the
same strict resource-cover inequality. The nonnegative multiplier is
explicitly required; strictness survives at B=T.

The fat wrapper uses only feasible singletons and all-small
configurations. The dual/union argument scales their convex
combinations and therefore preserves the local perspective constraint.
It is unnecessary to solve, enumerate or explicitly describe that
polytope. An oracle cost is never declared polynomial without a
separate implementation.

Each player's own item matroid supplies an exact oracle by weighted
greedy. Explicit transversal-resource slots also give a valid model:
each player has a local partition constraint allowing at most one slot
of each original resource. Omitting that constraint would change the
original problem. A representation by slots must be supplied; it is
not obtained for an arbitrary resource matroid from a generic
independence oracle or a fixed-basis exchange graph.

The empty-item convention u=0 and rank-zero empty allocation are
included. Common intrinsic item values are essential to the common
resource charge. This proof does not cover arbitrary player-specific
utilities.

## 2. Binary capacities without copy expansion

The compressed implementation maintains counts of units of type j
having matching owner a and selected-bundle label b. These cells
partition a fixed conceptual universe of units. Splitting a cell can
choose an arbitrary actual subset of its units; merging cells only
forgets a label. Inductively there exists a fixed-identity execution
realizing every count table. No global relabeling is needed.

In particular the lower retained forbidden unions are literally
unchanged under a valid earliest exchange. This is stronger than
merely keeping their numerical sizes unchanged. It is the exact
property needed to preserve old maximality certificates.

Available units include units of matching bundles not yet designated
as blockers. Excluding all matching-owned units would incorrectly
prevent blocked candidates from being found. The formula in the
manuscript includes precisely the required undiscovered rows.

The aggregate LP has a valid symmetric unit lift: set each conceptual
unit marginal to y_pj/c_j. The resource-capacity bound gives total
usage at most one, and y_pj<=a_pj x_p with a_pj<=c_j gives the
individual-unit bound. For A_j available units, its available value
is bounded by

\[
 \sum_j v_j A_j y_{pj}/c_j
       \le x_p\sum_j v_j\min\{a_{pj},A_j\}.
\]

Consequently a failed compressed greedy scan proves the same strict
cover inequality as an explicit unit implementation.

The candidate construction, minimality pruning and all ownership
changes are batched by types and cells. If a type still has a unit
after pruning, the remaining value excess is smaller than that unit
value; later removals only reduce that excess. Thus one pass establishes
unitwise inclusion minimality without iterating over the number of
units. Stored free centers are installed before their old column is
retired. Label reuse occurs only after all counts under that label
are cleared.

There are O(t(r+1)^2) cells, with polynomial-bit integer counts.
The bit parameter includes all supplies and quotas, not just the
item values. Zero-supply types contribute no units, and u is the
largest value among positive-supply types, or zero. Fat matching uses
capacitated types with player capacity one; capacities may be clipped
at the number of players. Neither this step nor the target search
introduces a factor equal to the total number of units.

This adapter covers uniform supplies and per-player quotas. It does
not implement arbitrary resource-side matroid or polymatroid
constraints.

## 3. Approximate available-bundle oracles

If a feasible oracle returns value at least lambda times the true
available optimum, a return below B certifies an available optimum
strictly below B/lambda. A fresh complete scan therefore replaces
the earlier certificate by

\[
 v(F)>(T-B/\lambda)(r-|J_0|),\qquad B\le\lambda T.
\]

This is an oracle-relative certificate: its verifier relies on the
proved approximation contract, not merely the value of an arbitrary
feasible heuristic output. An approximate output need not be monotone
under deletion of items. Restarting the scan after a microstep avoids
that error. Previously completed lower layers retain their mathematical
inequalities because their actual available sets and eligibility
flats remain unchanged.

Write tau=1/lambda, rho=(r-1)/r, and
C=max{u,2B+min(u,B)}. The condition tau B+rho C<=T is valid at
equality because the lower cover bound is strict. Solving it in the
regimes u<=B, B<=u<=3B and u>=3B gives exactly the three branches
in the manuscript. For r=1 the result is lambda T, without a largest
item restriction; exact rank-one optimization is not claimed for an
inexact oracle.

For the fat wrapper let d=tau+3rho, B_0=T/d and B=T/(d+eta).
The coarse star coefficient Cbar=2B+B_0 bounds the true coefficient
on the small-item instance. Direct subtraction gives

\[
 \Delta=T-\tau B-\rho\overline C
          =(\tau+2\rho)(B_0-B).
\]

Using tau>=1>=rho and Cbar<=3T/d gives

\[
 \Delta/\overline C
   \ge\frac{\eta(\tau+2\rho)}{3(d+\eta)}
   \ge\frac{\eta d}{4(d+\eta)}
   \ge\frac18\min\{\eta,1\}.
\]

Thus gamma=min{eta,1}/16 suffices. The rank exponent is uniform in
lambda; the approximation oracle's cost and numerical bits remain
paid. A smaller derived matroid rank only weakens the required star
charge. Feasible singleton tests are exact even with this oracle,
since a feasible positive singleton must be returned on its own
one-item ground set.

The final factor is lambda^-1+3-3/r, or this factor plus eta for
the rank-quasipolynomial bound. Both may compare against the
configuration LP, with the usual union reduction. The common-grid
target search uses its established one-sided failure invariant;
success is not assumed monotone.

## 4. Knapsack specialization and comparison limits

The included profit-scaling implementation is valid. After deleting
singleton-infeasible items, the largest positive retained value is a
lower bound on the optimum. Rounding at kappa times that value divided
by the item count loses at most kappa times the optimum. A minimum-cost
dynamic program over rounded profits returns a feasible bundle with
lambda=1-kappa. Its time, arithmetic and reconstruction are polynomial
in the input and 1/kappa. Its workspace need not be polynomial in
the bit length of an arbitrarily small accuracy parameter alone.

Choosing kappa=min{1/2,zeta/(2+zeta)} and eta=zeta/2 gives factor
4-3/r+zeta. This includes each player's own budget and item costs while
retaining common intrinsic utilities and arbitrary player-matroid
basis selection.

Public comparison is narrower than the mathematical extension. The
older all-player Polacek--Svensson framework already admits the exact
local-family adapter. For knapsack, a common fixed cap and profit
rounding supplies its exact available-bundle interface, giving a
derived public all-player quasipolynomial 4+zeta guarantee. The
public DRZ player-matroid pipeline similarly supplies a named derived
polynomial 6+zeta comparison after the relevant adapters. These are
recorded as derivations, not as verbatim printed theorem statements.
The new statements retain their arbitrary-selection and rank-sensitive
scope; the applications are not advertised as the first all-player
constant approximations.

## 5. Status relative to the original matching goal

These are additional transfer results. They do not change the accepted
research exponent 4/5 for deterministic exact maximum matching in
arbitrary general graphs. The latter still requires a complete and
paid general-support implementation, beyond the forest, feedback-edge
and other restricted interfaces developed separately.
