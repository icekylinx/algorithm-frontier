# Exact realization and review of adaptive scenario flow

The [reference backend](reference/README.md) completes executable exact
fixed-set optimization, common-set enumeration, witness recovery and
scenario-tagged separation. It uses the independently documented
[selected-flow primitives](../selected-flow/reference-realization.md).
The main approximation theorem keeps its paid polynomial rational LP
primitive; the reference's finite Bland simplex has a separate time bound.

## Fixed-set optimality and adaptive witness recovery

Fix the same nonempty tuple of distinct original commodity IDs in all
scenarios. Solve each original scenario's concurrent-flow LP exactly,
including its own demand scales, topology, physical capacities and every
routing-budget row. Let `rho[omega]` be that scenario's certified optimum
and `lambda=min(rho)`.

Every feasible robust common rate is at most every individual optimum,
so it is at most `lambda`. Conversely, multiply every coordinate of a
scenario's optimal primal routing by `lambda/rho[omega]` when its optimum
is positive. Conservation gives the required common normalized rate;
nonnegative capacities and routing charges stay within their original
bounds. If any optimum is zero, the common rate is zero and the all-zero
primal vectors work in every scenario. This proves attainment and exact
optimality for the fixed common set. The certificate retains the individual
optimal primal/dual pairs; the output also exposes their common-rate
routings. Different scenarios may use completely different paths.

The verifier rebuilds each original scenario formulation, checks its
primal/dual inequalities and equality of objective values, and checks
that every constituent certificate names the identical common selected
tuple. Thus the minimum is both an upper bound and an attained lower bound.
Both the outer and constituent records must have their canonical certificate
types, so an arbitrary object cannot replace the derived rate property with
a false value. No optimization is called during verification. Individual scenario
optimality is a stronger certificate than necessary, but makes the
fixed-set contract direct. Global selected-set optimality additionally
requires the complete enumeration and its fixed permitted-family predicate.

## Intersection separation and exact common selection

For a query on the original common commodity coordinates, inspect scenarios
in fixed order. A scenario's strict nonnegative packing row is valid for
its service region, hence for their intersection. If all scenarios accept,
the independent routing-existence statements prove membership in the
intersection. No scenario-dependent selected set or shared flow template
is introduced. Materializing all budget rows before repeated calls avoids
consuming a one-shot iterator differently on different selected sets.

For exact optimization, stream all combinations of the requested original
selected cardinality, test the fixed permitted predicate, and optimize
each permitted set as above. The greatest minimum is precisely the robust
objective because the same combination is used across all scenarios.
An empty permitted family returns `None`; a permitted zero-rate solution
returns a certificate. Neither is confused with independent optimization
of selection in each scenario.

## Time, arithmetic and storage

Each fixed-set call invokes one native rational LP per explicit scenario.
Its time is the sum of the individual finite Bland-simplex bounds given
in the selected-flow realization, plus polynomial work for storing and
comparing their exact optima. Complete selection enumeration multiplies
this by the number of original commodity combinations, with paid family
predicate work. Scenario separation similarly sums the finite normalized
Farkas-LP costs up to its first rejection. These are constructive bounds;
no polynomial pivot bound or corank approximation running time is claimed
for this software.

Each LP and each primal/dual certificate has polynomial encoding in the
total explicit input, by the original rational determinant bounds. Scaling
a routing by a ratio of two polynomial-bit rational optima preserves
polynomial bit length. The scenario count is explicit, so storing all
certificates and routings is polynomial in the full input. Enumeration
retains only the current best result. Binary capacities are never expanded
into individual units.

## Scope of the proof audit

The audit covers the complete main theorem's scenario-region intersection,
nonnegative polynomial-bit Farkas rows, original-coordinate zero insertion,
weighted first-crossing omissions and their failed-branch accounting,
fixed-family rational comparator search, original fixed-set reoptimization,
and deterministic streamed whole-ground conversion at fixed rational
accuracy. The combined LP in the main proof is bounded, contains zero,
and uses only original data plus the explicit redundant rate bound; its
polynomial-bit denominator bound therefore applies even in lower-dimensional
cases. Equivalently, the minimum of individual scenario optima is itself
one of those rational optima. Exact routing budgets are continuous
constraints, without an integrality claim.

The Hitting Set reduction has also been checked in both directions:
selected members of a listed set have exactly one path through its shared
bottleneck; unit admission is equivalent to rejecting a member of that
set. Zero-capacity arcs are removed before asserting the forest property.
The cited [Jansen 2017 primary source](https://jgaa.info/index.php/jgaa/article/view/paper413)
explicitly records the source problem's solution-size parameterization
as `W[2]`-complete. The reduction preserves the rejected count, admits a
rate-one solution exactly in the hitting-set YES cases, and supplies no
constant approximation gap. It uses an arbitrary explicit scenario family;
it proves no hardness for only individual edge failures.

The named exact LP/Farkas and restriction-selector dependencies remain
part of the theorem's model. Internal proof review and finite executable
evidence do not constitute external peer review or proof-assistant
verification.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
