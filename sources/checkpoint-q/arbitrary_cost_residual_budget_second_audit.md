# Second independent audit of arbitrary-cost near-two allocation

**25 October 2026. Full independent read of R1--R14, with particular
attention to residual-budget encoding and affordable heavy support.**

Reviewed manuscript:
`arbitrary_cost_residual_budget_near_two_allocation.md`.
The theorem passes. It obtains factor 2+eta for the stated integer
optimum under the corank/heavy-support parameter, with arbitrary
nonnegative assignment costs and one exact budget. It needs no
price-diversity or proportional-cost assumption.

The adaptive abstract proof was independently reviewed in
`adaptive_residual_budget_corank_independent_audit.md`. This audit
checks that the application actually satisfies that proof's stronger
interfaces and that its optimization and rounding close the stated
allocation theorem.

## 1. The completion oracle finds a cheapest actual compatible assignment

At Q, the first intersection matroid is the parallel extension of
the original M, on light labels for p in Q and every original
eligible heavy pair. Its independence enforces distinct owners and
M-independence. The second matroid bounds light labels by r-k and
heavy pairs by k while enforcing type-specific Boolean recipient
independence. A common independent set of size r saturates both
counts and gives a genuine original M-basis.

Weights zero on light labels and actual costs on heavy pairs make
the optimum exactly h_k(Q), with an attaining pair I_Q,H_Q. The
heavy assignments retain their types and resource feasibility;
the oracle is not merely pricing a heavy-recipient set. Its ground
has polynomial size and does not expand binary resource supplies.

Only light labels are removed when Q shrinks. All original heavy
pairs remain available. Hence a protected pair I*,H* still belongs
to the completion family whenever I* lies in Q. This is the key
implementation detail required by RB3, and the application has it.

## 2. The current utility region has a uniform exact support interface

The light allocation polytope X_s(D) uses the original recipient
polymatroids and one explicit cost row with right side D. It is
nonempty at zero, bounded by singleton ranks, and downward because
costs are nonnegative. Its lower utility projection is compact,
convex and downward.

The earlier budgeted support construction applies with this D:
an inner exact LP optimizes light utility in a nonnegative direction,
and an outer normalized support LP either certifies membership or
returns a strictly violated nonnegative packing row. Reconstruction
uses the same original budgeted primal. No contraction of resource
capacity to Q replaces the fixed-ground projection.

The changing D does not conceal a growing rational description.
Every h_k(Q) is the cost of at most k original heavy pairs, and
therefore is a sum of at most k original input rationals. A
uniform bit bound for h_k(Q) and C-h_k(Q) follows from the original
cost encodings and q, independent of recursion depth. The minimum
operation chooses among such sums; it does not alter their bound.

For any such residual budget, the inner LP has polynomial dimension,
zero-one recipient rows with integer right sides at most f_j(P),
and original value/cost coefficients. Determinant bounds therefore
give a uniform polynomial encoding for its vertices. Outer support
rows are sums of products of these bounded coordinates with the
original values, and its dimension is polynomial as well. Thus
all returned normals and capacities have a fresh uniform polynomial
bound. No parent row is substituted into a child LP's coefficient
description. Zero residual budget and resource loops only create
lower-dimensional feasible regions, already covered by exact LP.

## 3. The paired-witness invariant and output budget both hold

If a full promised pair I*,H*,x* survives inside Q, then
h_k(Q)<=c(H*) and c(x*)<=C-c(H*)<=C-h_k(Q). Its full light target
is therefore feasible in the current utility region. Every
current nonnegative separator row is valid for that same target.
The weighted prefix argument finds an omission certificate inside
Q\I*, preserving the pair at the child. This directly instantiates
the independently audited adaptive lemma.

At success the light allocation serves all of Q at b with cost
at most C-h_k(Q). It consequently serves the particular I_Q
attaining h_k(Q). Discarding all other light counts leaves that
service and decreases cost. Adding the actual H_Q gives total
cost at most C. This step neither combines independently priced
solutions nor assumes the cheapest completion was chosen for a
different light allocation.

The omission deficit is |Q|-(r-k), initially c+k. Local first-
crossing enumeration and its prefix-free branch sum do not depend
on a globally fixed region. The uniform polynomial oracle bounds
therefore give the stated Gamma(t/(t-b))^(c+k) time on both
promised and unpromised calls.

## 4. The fixed joint benchmark makes the outer target search sound

For each split and k<r, the benchmark X optimizes light service
over actual original-basis decompositions and integral one-unit
heavy assignments, with fractional light allocations and their
joint cost at most C. It is a fixed problem independent of the
search target, and it is downward in its requested light service.
Restricting its optimum to the original value grid gives the
largest feasible grid target X.

The adaptive routine's failure excludes the full target for this
same joint problem. Its weaker output on success supplies the
required saved lower-endpoint witness. Since at least one light
player is served, X<=V_L, and V_L+g is a valid external upper
grid target. At adjacent endpoints the saved lower is at least
X, without any monotonicity assumption on successes.

The zero-service family is available precisely when h_k(P)<=C.
An empty light class or an impossible completion is handled as
stated. For k=r the algorithm records an affordable all-heavy
original basis directly and does not use an empty-light objective.
Skipping k>K affects only that support family and is never used
as an original-target infeasibility conclusion.

## 5. Integer recovery preserves the actual combined cost

The saved light allocation has a known actual cost at most
C-c(H). The disposal extension, complement ranks and per-player
prefix intersection apply to its light resources. Maximizing the
actual cost applied to the dual vector on the maximum-total
integral face minimizes the original complement's cost. This
gives an integer light allocation costing no more than the
fractional witness and losing at most u_L utility per selected
light player.

Dropping disposal and outside-I counts preserves the selected
utilities and cannot raise cost. H and its type assignments are
kept unchanged. Because the split is by intrinsic type value,
heavy and light resource collections are disjoint; aggregation
does not introduce an unaccounted recipient-capacity conflict.
Their combined cost remains at most C and their selected owners
remain the genuine M-basis produced by the completion oracle.

This argument would not automatically cover a player-dependent
value split of one original resource across both sides. The
manuscript explicitly retains intrinsic values and excludes that
unsupported transfer. It also correctly preserves one scalar
assignment budget, not several unrelated hard budgets.

## 6. The original integer optimum supplies the support promise

Choose the stated optimal allocation at theta*. Discard counts
outside its selected basis. At every selected heavy recipient,
retain one of its original heavy units and remove its other
counts. The remaining selected players had only light resources
and retain at least OPT_C light utility. Nonnegative costs make
the resulting actual heavy/light pair budget feasible.

Its heavy-support size k is among the processed values under the
theorem's hypothesis. If k=r, the pure-heavy branch suffices.
Otherwise OPT_C lies on the original value grid and supplies a
full joint witness, so X>=OPT_C. The saved light service b is
at least (1-epsilon)OPT_C. At theta*=(1-epsilon)OPT_C/2, strict
lightness gives u_L<theta*, while every heavy unit has value
at least theta*. After rounding, the light utility exceeds
theta*, and heavy utility meets it. This proves the stated ratio.

The support hypothesis concerns one actual integer optimum. It
does not require every optimum to have small support and does
not silently replace that optimum by a fractional allocation
whose heavy assignments might have sizes below one unit.

## 7. The affordable-heavy sufficient parameter is computable and exact

The parallel lift of M on heavy pairs, intersected with the direct
sum of heavy Boolean matroids, represents exactly feasible
one-heavy-unit assignments to M-independent recipients. Minimum
weight at each cardinality is polynomial by weighted intersection.
These minimum costs are nondecreasing: trimming a larger common
independent set gives a smaller one at no greater nonnegative
cost. Thus binary search finds the largest affordable size h_C.

Every such M-independent heavy recipient set extends to an
original M-basis. The new players are only zero-weight light
labels in the completion oracle; no real light service is being
asserted by this extension. Consequently h_C is exactly the
largest k with h_k(P)<=C. This equality is about completion
availability, not about light-quota feasibility, and is used
only in that valid sense.

Dropping an original budget-feasible optimum to one unit per
heavy recipient produces an affordable M-independent heavy
assignment. Hence its support is at most h_C(theta*). This
proves the sufficient condition R14. Since affordability can
only reduce the available common-independent cardinality,
h_C is at most the uncosted common rank of M and the heavy
Boolean matroid, and at most the heavy Boolean rank itself.

The main existential support condition can still be weaker
than h_C<=K, as stated: large affordable heavy supports may
exist even though one optimum uses a smaller one.

## 8. Complete algorithm and accepted scope

The polynomial number of value splits, support cardinalities
and binary-search calls leaves exponent at most c+K. All
completion, support, reconstruction and rounding operations
have polynomial dimension and encoding. The generic omission
tree and all oracles have polynomial workspace. No dependence
on cost diversity is hidden in the exponent.

The zero allocation and the budget-feasible additive fallback
ensure a complete output even without the support promise.
The fallback's exponent c is absorbed in c+K, and actual
achieved utility determines the returned candidate. These
checks establish the unconditional validity of every output
and the conditional near-two multiplicative guarantee.

All R1--R14 interfaces pass this independent review. The result
supersedes the price-profile requirement for this scalar-budget,
intrinsic-value model while retaining the exact stated oracle,
parameter and comparator restrictions.
