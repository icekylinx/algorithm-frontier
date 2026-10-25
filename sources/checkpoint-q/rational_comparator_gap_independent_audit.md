# Independent audit of rational-comparator gap recovery

**25 October 2026. Full independent review of RG1--RG11.**

Reviewed manuscript: `rational_comparator_gap_optimization.md`.
The refinement passes. For a fixed permitted family whose fixed-set
optima have a known uniform rational denominator bound, it removes
the additional approximation loss formerly paid by the relative
target search. In the unrelated-allocation and selected-flow
applications, it improves the fractional-comparator running-time
base from Gamma(2/epsilon) to Gamma(1/epsilon). It changes neither
the integer rounding loss nor the constraints preserved by those
applications.

## 1. The exact object needing a denominator bound is identified

For each actual permitted set I, lambda_I is the optimum of the
original fixed-I optimization problem. The family F and those
problems are fixed throughout the target search. Since F is finite
and nonempty, Lambda=max_I lambda_I is attained by some permitted
set, so the same denominator bound D applies to Lambda itself.

This fact would fail for a benchmark defined by target-dependent
families without an additional argument. The manuscript explicitly
excludes that case. In particular, the structured budgeted heavy-
support family B_(b,k) changes when its charged quota b changes,
and cannot be substituted into this lemma merely because each
individual target call has an exact selector.

The denominator bound is also for an optimum of the original
fixed-set problem, not for a feasible point returned at a target.
A target witness can inherit the artificial grid's denominator.
Exact fixed-set reoptimization is consequently a necessary part
of the stated proof, not an optional output cleanup.

## 2. The one-sided search has the correct invariant

Let alpha=A/B in (0,1), in lowest terms, and set
delta=1/(2BD^2). The upper grid endpoint
(ceil(V/delta)+1)delta is strictly larger than V and hence than
Lambda. Zero is a valid initial lower target, with any permitted
set saved, because every lambda_I is nonnegative.

When a target succeeds, the returned I certifies
lambda_I>=alpha*T. When it fails, the gap routine's promised
failure meaning gives T>Lambda. Thus a failed endpoint remains
strictly above Lambda, regardless of the behavior of successful
calls elsewhere. No monotonicity of success is used or needed.

At adjacent grid indices U=L+delta and U>Lambda, whence
L>Lambda-delta. The saved set, including the initial set when no
positive target succeeded, therefore satisfies

\[
          \lambda_I\ge\alpha L
                         >\alpha\Lambda-\alpha\delta.
\]

It is harmless if L exceeds Lambda: success is only a lower-rate
certificate, and such an endpoint makes the final estimate stronger.
An externally certified upper endpoint need not be a failed call
to the gap routine.

## 3. The rational separation calculation is exact

Write lambda_I=p/d and Lambda=z/e in lowest terms, with d,e<=D.
If alpha*Lambda-lambda_I is positive, then

\[
 \alpha\Lambda-\lambda_I
      =\frac{Azd-Bpe}{Bed}
      \ge\frac1{BD^2}=2\delta.
\]

The numerator is a positive integer. No assumption about the
numerators' sizes or a shared denominator is required. Cancellation
can only increase the minimum positive gap, so using the product
Bed is safe.

The search inequality gives the same difference strictly smaller
than alpha*delta<delta. These inequalities contradict each other.
Hence exact reoptimization of the saved set achieves
lambda_I>=alpha*Lambda, with no remaining search loss.

This covers Lambda=0 and a possible final lower endpoint L=0.
For positive Lambda the argument itself precludes an inadequate
zero-valued saved optimum; a separate positive lower scale is not
needed. Empty families must still be detected before the search,
as required by RG1's interface.

## 4. The very fine grid still has polynomial bit complexity

The number of binary-search calls is logarithmic in V/delta+2.
The denominator of delta has binary length
O(log B+log D). Grid indices and target rationals therefore have
polynomial binary encoding whenever V, D and alpha do. The method
does not enumerate the grid or iterate D^2 times.

Each call retains its original corank exponent G(alpha,c). The
additional fixed-set optimization and logarithmically many calls
are polynomial factors. The ordinary binary search stores only
its endpoints and one saved set; it does not enlarge the previous
polynomial workspace bound. The exact arithmetic used in the gap
routine continues to have polynomial-bit inputs.

For alpha=1-epsilon, the gap ratio is
t/(t-alpha*t)=1/epsilon exactly. Thus the stated improvement to
Gamma(1/epsilon)^c is algebraic, not an asymptotic replacement
that conceals another accuracy parameter in the exponent.

## 5. A uniform denominator bound is computable as claimed

Suppose an original fixed-set LP has n variables and every rational
coefficient and right side has numerator and positive denominator
at most 2^L in absolute value. Clearing denominators separately in
one row multiplies at most n+1 denominators, including its right
side. The displayed W=2^((n+2)L) is a safe bound on all resulting
integer entries.

At a vertex of a nonempty bounded polytope, the active constraint
normals span the full ambient variable space. Otherwise a nonzero
direction orthogonal to all active normals would permit a small
two-sided movement preserving feasibility, contradicting extremality.
This remains true for a lower-dimensional polytope: its affine-hull
equalities are among the active constraints. Thus n independent
active rows can be selected without a full-dimensionality promise.

Their integer matrix has nonzero integer determinant. Cramer's
rule expresses every vertex coordinate with denominator dividing
that determinant, whose magnitude is at most n!W^n by the
elementary determinant expansion. RG9 is therefore valid. If
different fixed-set formulations have fewer than the uniform n
variables, one may pad them with zero-fixed variables or use the
larger displayed bound; this resolves the manuscript's 'at most n'
wording without changing any complexity.

The integer D has polynomial binary length and can be computed by
ordinary integer arithmetic. Exponentially many implicit rows do
not alter the bound: only their uniform encoding bound and the
fixed variable dimension enter. A rational objective that is not
already one coordinate can be made a coordinate using one extra
variable and an equality, as stated.

An oracle's query-dependent output length alone is not a substitute
for this hypothesis. One needs a known uniform description bound
for the original fixed-set problems, or a directly supplied valid
D. The manuscript makes that requirement explicit and the two
applications below satisfy it concretely.

## 6. Unrelated allocation satisfies the uniform hypotheses

For a specified actual selected basis I, introduce lambda and
the original resource coordinates x_j(p). Use resource feasibility,
the selected-player utility inequalities, nonnegativity and the
redundant bound lambda<=V. Add the original assignment-cost row
when that budget is present. The zero allocation is feasible and
all variables are bounded by the recipient singleton ranks and V.

Every recipient subset row has zero-one coefficients and an
integer right side at most f_j(P). Querying each total rank once
gives a known bound on every unlisted subset value. Utility rows
come from the explicit rational v_pj values. Cost and budget
coefficients, when present, are also explicit original rationals.
Thus n and L in RG8 are known with polynomial encoding. Choosing
a different basis merely chooses a subset of the existing service
rows; it introduces no target-dependent coefficient.

Exact fixed-I optimization is the same polynomial separated LP
already used for reconstruction, now with lambda maximized. After
the improved search, the optimum witness has service at least
(1-epsilon)FOPT at every selected player. The accepted per-player
lower rounding then loses at most u_p. In the budgeted case, free
disposal and the maximum-total dual-cost face preserve the one
assignment budget exactly. The cost-preserving proof is unaffected
by optimizing the saved basis first.

FOPT continues to optimize over one actual selected basis and
fractional resource counts. The lemma introduces no fractional
mixture of selected bases and no new relaxation of the budget.
The previous positive-scale relative search remains correct, but
is no longer needed for the sharper exponent.

## 7. Selected concurrent flow satisfies the hypotheses

For one permitted commodity set I, maximize its common rate lambda
in the explicit arc-flow LP. Capacities and the optional total
routing-cost budget are fixed. Flow-conservation rows use the
original positive demands and incidence coefficients. Finite
capacities and distinct terminals give an explicit finite rate
bound, and arc variables are bounded by capacities.

This is a bounded, nonempty rational LP of polynomial dimension
with original rational data. Its optimum has the uniform bound
RG9 without any projected-facet description. Exact reoptimization
of the saved commodity set gives actual flows at lambda_I, so the
rational-separation conclusion is attained by a constructive
routing, not merely an objective estimate.

Combined with the separately stated nonnegative flow separator and
weighted omission gap, this proves (1-epsilon)OPT in
Gamma(1/epsilon)^c poly(H), with exact capacities, an exact optional
routing budget and polynomial workspace. There is no integer
rounding step in the flow application. This conclusion does not
extend to unsplittable or integral multicommodity routing.

## 8. Accepted scope of the refinement

The improvement is a rational-comparator recovery theorem for
fixed families, exact fixed-set optimization, and a uniform known
denominator bound. It does not turn a gap solver into an exact
combinatorial optimizer, remove an additive allocation rounding
term, or validate target-dependent selection families. Within
that scope, every arithmetic, search, zero-value, implicit-row and
bit-complexity interface checks independently.
