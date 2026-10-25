# Independent audit of arbitrary-cost near-two allocation

**25 October 2026. Complete read of R1--R14: passes.**

This audit covers `arbitrary_cost_residual_budget_near_two_allocation.md`.
The statement keeps intrinsic resource values, allows arbitrary nonnegative
player-type costs, selects an actual original player-matroid basis, and
preserves one assignment budget exactly. The proportional-light-cost and
price-diversity restrictions of the preceding applications are not needed.

## 1. The attaining completion oracle is a genuine polynomial operation

For fixed heavy/light type classes and k, form a light copy of every p in Q
and the eligible heavy pairs (p,j). The parallel extension of M enforces
distinct owners and original player independence. The other matroid is the
direct sum of the light uniform rank r-k and the heavy direct sum truncated
to rank k. A common independent set of size r therefore has exactly the
required two class counts and its owners form an M-basis.

Zero weights on light copies and actual nonnegative assignment costs on
heavy pairs make minimum-weight cardinality-r matroid intersection compute
exactly h_k(Q). It returns the attaining pair I_Q,H_Q, not merely a lower
bound. No additional color condition is being added outside the two
matroids: the exact class cardinalities follow from their two rank caps and
the total cardinality r.

The pair ground has polynomial size. Every attained cost is the sum of at
most k encoded input costs, so its bit length is uniformly polynomial. The
Boolean recipient matroids encode one unit on each distinct heavy recipient;
no binary-sized supply is expanded.

## 2. The current residual region protects the same original pair

Fix any promised pair I*,H* and light allocation x* with full target t and
total cost at most C. If I* remains contained in Q, this very pair is an
eligible competitor in the minimization defining h_k(Q). Consequently

\[
 h_k(Q)\le c(H^*),\qquad
 c(x^*)\le C-c(H^*)\le C-h_k(Q).
\]

Thus the promised full light target t*1_(I*) belongs to the current light
budget region. A completion failure or h_k(Q)>C is impossible on this
surviving path.

If a nonnegative packing row a*z<=U is violated by b*1_Q, then

\[
 a(Q\setminus I^*)\ge a(Q)-U/t
 >(1-b/t)a(Q).
\]

The weighted first-crossing certificate therefore supplies an enumerated
omission contained in Q\I*. After that omission, the same original pair
again satisfies the displayed comparison. The proof does not require all
rows to belong to a fixed budget region. It requires, and proves, the
stronger per-node surviving-pair property.

This is also the essential forced-omission interface for the later global
time conversion. Excluding p from Q excludes p only as a light recipient;
the original heavy options and original matroid remain available.

## 3. Success uses the particular cheapest completion

If b*1_Q is feasible at budget C-h_k(Q), reconstruct its fractional light
allocation and restrict it to the actual light set I_Q returned by the
minimum-cost oracle. Nonnegative costs and downward resource feasibility
make this restriction safe. Adding the attaining H_Q costs at most

\[
 [C-h_k(Q)]+h_k(Q)=C.
\]

An arbitrary completion would not justify this equality. The manuscript
expressly uses the attaining one, so there is no mismatch between a lower
bound on heavy cost and the heavy assignment actually returned.

The light and heavy classes consist of disjoint original types. This is why
their separately feasible allocations combine without double-spending a
resource. It also explains the correctly stated intrinsic-value boundary:
an unrelated-value split could divide one type between both classes and
would need a different proof.

## 4. Uniform off-promise time and numerical separation

At a node Q, the residual omission measure is |Q|-(r-k), initially c+k.
The weighted prefix-free analysis charges all generated branches and all
failed completion checks. Its bound depends on t/(t-b), not on the values
of the current row or the identity of the current residual-budget region.
Hence the same Gamma(t/(t-b))^(c+k) bound applies to every input, including
unpromised targets.

The original light ranks stay fixed. Only the explicit rational budget
C-h_k(Q) changes, with polynomial encoding as verified above. Fractional
support, nonnegative separation, and reconstruction therefore retain their
uniform polynomial dimension and bit bounds. The normalized support test
uses the nonpositive case for membership, which is necessary because its
optimum need not equal zero at an interior point.

All relevant nested subroutines use polynomial workspace. The recursion
stores a single path and generates prefix certificates sequentially. No
price-level enumeration or numerical resource-unit expansion is hidden in
the polynomial factor.

## 5. The fixed joint benchmark makes the target search valid

For a fixed split and k<r, the benchmark X uses an integral one-unit heavy
assignment, an actual selected basis, fractional light allocation, and one
joint actual budget. It is downward in its light target. The gap query at
full target T and relaxed target (1-epsilon)T therefore has a sound failure
certificate T>X, regardless of whether relaxed successes are monotone.

If h_k(P)<=C, a zero-service pair exists and provides an initial legal saved
candidate. At least one light player is selected when k<r, so
V_L=sum_(j light) v_j f_j(P) is an upper bound on X. Both V_L and every
integer optimum lie on the common rational value grid g. The external
upper endpoint V_L+g is a valid hard upper certificate without being queried.

The one-sided binary search keeps an upper endpoint strictly above X and
moves it only on failure. At adjacent grid endpoints, its saved lower
endpoint is at least X. This argument does not infer full-target feasibility
from a relaxed success. Binary grid length and the number of queries are
polynomial in the encoding size.

An empty light class gives X=0 when k<r. The k=r branch is instead solved
as minimum-cost pure-heavy basis selection. It is not assigned a spurious
finite target on an empty light set. Skipping k>K is never used as a
certificate about the original problem.

## 6. Exact-cost integer recovery has the stated one-unit loss

The accepted disposal-and-complement rounding applies to the fractional
light allocation at its actual residual cost. It optimizes the one scalar
assignment objective on an integral maximum-total intersection face and
returns integer light counts of no greater cost, losing at most u_L utility
per selected light player. Discarding all outside counts remains safe.

The heavy assignment is retained unchanged, so the combined output costs
at most C and has selected minimum utility at least

\[
 \min\{a_H,b-u_L\}.
\]

This does not assert that intersecting an integral polytope with a budget
row preserves integrality. The budget is preserved by the cost objective of
the rounding procedure. A second unrelated hard assignment budget is not
claimed.

## 7. The original integer optimum supplies the correct split witness

At theta*=(1-epsilon)OPT_C/2, choose an optimum having at most K selected
heavy recipients. Retain one originally assigned heavy unit on each such
recipient and all original light utility only on the remaining selected
players. All deletions are resource-feasible and nonincreasing in cost.
The original basis remains exactly partitioned by these two groups.

If the light group is nonempty, its utility is at least OPT_C and therefore
X>=OPT_C. The optimized saved b is at least (1-epsilon)OPT_C. Since equality
at the threshold belongs to the heavy class,

\[
 u_L<\theta^*\le a_H,
 \qquad b-u_L\ge 2\theta^*-u_L>\theta^*.
\]

The pure-heavy case directly achieves at least a_H. Thus the factor is
2/(1-epsilon), equivalently 2+eta for epsilon=eta/(2+eta).

The algorithm tries polynomially many splits and all k through K. The
largest relevant exponent is c+K. With K=r the support condition is
automatic, although the direct corank bound becomes Gamma(1/epsilon)^q.
The separately proved global conversion improves this all-instance time
without changing the present approximation argument.

## 8. The affordable-heavy refinement is sound

The maximum affordable cardinality h_C(theta) is computed on the heavy pair
ground by weighted intersection of the parallel player matroid and the
direct sum of Boolean resource matroids. Minimum costs by cardinality are
nondecreasing because an independent assignment can be trimmed and all
costs are nonnegative. Binary search for the largest affordable cardinality
is therefore legitimate.

Every such M-independent recipient set extends to an original M-basis;
the added players can be zero-cost light labels in the completion oracle.
This proves h_C(theta)=max{k:h_k(P)<=C}. Dropping an optimum to one unit per
heavy recipient proves its support is bounded by h_C(theta). The condition
h_C(theta*)<=K is thus sufficient. The principal theorem correctly allows
the weaker existential hypothesis that only one optimum has support at
most K, even if the largest affordable heavy support is bigger.

## 9. Complete output and scope

A zero allocation on an arbitrary M-basis is always legal after the usual
rank-zero preprocessing. The accepted additive exact-budget algorithm
provides a nontrivial unconditional fallback, and selecting the best actual
output cannot invalidate costs or basis membership. The zero-optimum case
requires no threshold-zero support hypothesis.

The theorem concerns arbitrary nonnegative costs, one exact assignment
budget, intrinsic resource values, and recipient-polymatroid value oracles.
It is not a polynomial-time near-two theorem for ordinary Budgeted Santa
Claus and does not claim the unrelated-value or multi-budget extension.
The manuscript preserves these limits and attributes public cost-preserving
rounding separately from the adaptive residual-budget contribution.

**Disposition:** all R1--R14 claims and the stated corner cases pass. No
substantive correction is required. The loss of the price-diversity and
proportionality assumptions follows from a proved surviving-pair invariant,
not from treating a signed joint projection as an ordinary downward region.
