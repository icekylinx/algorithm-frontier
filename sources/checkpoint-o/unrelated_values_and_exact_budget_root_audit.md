# Root audit: unrelated values and one exact assignment budget

**25 October 2026. Mathematical review for checkpoint N.**

This review accepts `unrelated_values_corank_additive_allocation.md`
(U1--U24) and `unrelated_values_exact_budget_additive_allocation.md`
(B1--B17), together with their separate independent audits. It is
a review of the written proofs, not a claim of external peer review
or a substitute for the precise oracle assumptions in the manuscripts.

The accepted bounds are pointwise on every selected player p:

\[
 v_p\ge\max\{0,(1-\varepsilon)\mathrm{OPT}-u_p\},
 \qquad
 v_p\ge\max\{0,(1-\varepsilon)\mathrm{FOPT}-u_p\}.
\]

Their respective deterministic times are
`Gamma(1/epsilon)^c poly(H)` and
`Gamma(2/epsilon)^c poly(H)`, with polynomial workspace.
Here `Gamma(R)=R^R/(R-1)^(R-1)` and `c=q-r` after deletion of
loops of the original rank-r player matroid. The budgeted theorem
uses the corresponding budget-constrained optima and satisfies its
single nonnegative assignment-cost budget exactly.

## 1. The comparator is an actual selected basis

Integer OPT maximizes the minimum utility on one actual permitted
basis using integral independent resource counts. FOPT relaxes
the resource counts only. It still chooses a single actual basis,
not a fractional mixture of different player sets. This distinction
is essential: the proof's witness is an omitted set of size c.

All recipient polymatroids are integral, normalized and monotone.
Values are arbitrary nonnegative rationals and can differ between
players for the same resource. Resource types are independent
apart from the one assignment-cost inequality in B. Coordinate
caps can be incorporated into their individual rank functions.
Cross-type local constraints are not silently included.

Deleting a player-matroid loop is safe because restricting an
allocation and extending it by zero preserve resource independence.
Nonnegative costs preserve this fact in B. A coordinate with zero
singleton resource rank can have its value set to zero. The term
u_p is the maximum remaining eligible unit value at p.

## 2. The projection separator is both nonnegative and well described

The fixed feasible utility region is compact, convex, nonnegative
and downward closed. In U it is the Minkowski sum of diagonal
images of the resource independence polytopes. In B it is the
lower utility projection of the joint resource polytope with the
assignment-cost row. It remains the same region throughout all
candidate-ground deletions.

The explicit outer support LP uses a nonnegative simplex normal
a and epigraph variables for its support function. In U, each
resource support is computed by greedy optimization. Its vertices
have integral coordinates bounded by encoded singleton ranks.
In B, support is an exact rational LP with submodular separation
for the resource rows and the explicit cost constraint.

For B, a uniform vertex encoding bound is required before using
those vertices as coefficients in the outer LP. A nonsingular
active subsystem has polynomial dimension; its entries are the
original rational costs, zero-one resource coefficients and
encoded rank values. The determinant bound gives polynomial
vertex bit length even though there are exponentially many possible
resource rows. Exact lexicographic refinement can select an extreme
support optimizer. Thus the outer LP has a uniform polynomial
coefficient bound, exact polynomial separation and polynomially
many variables. Nested oracle calls remain polynomial.

A positive optimum yields a globally valid row
`a*z <= h(a)` with `a>=0`, nonnegative capacity and polynomial
encoding. Conversely, downward closure gives `h(a)=h(a_+)` for
every signed normal a. Any signed strict separator of a nonnegative
target therefore has a nonzero positive part that can be normalized
to the simplex. A nonpositive outer optimum proves membership,
including lower-dimensional regions. Merely appealing to an
arbitrary signed projection separator would not have sufficed.

The accepted weighted prefix-free theorem can consequently be
applied with `t=T`, `b=(1-beta)T` and `R=1/beta`. No integer-quota
rounding is needed in this interface. Membership is followed by
a primal feasibility LP reconstructing actual fractional counts.

## 3. Player-dependent type orders do not obstruct lower rounding

In U, extend each reconstructed independent resource vector to
a fractional base. This preserves every utility because values
are nonnegative and no assignment budget is present. Complement
each base with its singleton-cap vector to obtain the stated
integral dual resource polymatroid.

For each player separately, order types by that player's value.
The ceilings of the cumulative fractional dual counts are integral
prefix capacities. Their rank on a set of player-type coordinates
is the sum, over players, of the maximum included prefix capacity.
It is a normalized integral monotone submodular function. Because
the capacities increase along the player's order, its inequalities
are equivalent to the intended prefix constraints.

Intersecting this polymatroid with the direct sum of the resource
dual polymatroids has an integer maximum-total solution. The given
fractional dual vector attains the full sum of resource ranks;
an integer solution of the same total must be a base in every
resource component. Telescoping each player's own decreasing value
sequence bounds the increase in its dual utility by u_p. Complementing
back therefore loses at most u_p in original utility. Different
orders at different players cause no conflict between the two
polymatroids.

Counts stay binary encoded on a polynomial-size product ground.
No replication by the numerical resource supply is used.

## 4. The budgeted completion and rounding preserve cost exactly

Completing to original resource bases could spend extra cost and
is not valid in B. Instead, add a zero-value, zero-cost disposal
coordinate to each resource. Its rank equals f_j(S) on ordinary
subsets and equals f_j(P) whenever disposal is present. The mixed
submodularity inequality reduces to monotonicity of f_j; the
other cases are immediate. An independent vector is completed
to a base by putting its unused total at disposal, without changing
its utility or cost. Disposal is not a candidate player and does
not increase c.

After complementation, first restrict the intersection to the
maximum-total face L, which contains the fractional dual vector.
This face is integral. Only then maximize the dual cost objective
on that face. An integral optimum y' satisfies `cost(y')>=cost(y)`.
Writing the fixed singleton vector as a gives

\[
 \operatorname{cost}(a-y')\le
 \operatorname{cost}(a-y)\le C.
\]

Every prefix inequality remains satisfied during this optimization,
so the same pointwise utility-loss proof holds. Restricting the
extended bases to real players and then to the selected basis
keeps independent resource counts and cannot increase nonnegative
cost. This proves the budget exactly, without expectation or
resource augmentation.

Maximizing cost on the whole independent intersection, rather than
its maximum-total face, would leave a gap. Optimizing one linear
cost does not preserve several unrelated assignment budgets. The
accepted claim is explicitly for one budget.

## 5. The two searches have different precision arguments

For integer OPT, all utilities lie on a common rational value grid
g. Cost denominators do not change that grid. The one-sided target
test fails only above the true target-feasible optimum; it may
succeed beyond it. Binary search uses this valid failure implication
and an externally infeasible upper bound. At adjacent grid endpoints,
the saved successful lower target is at least integer OPT. The
final rounding is performed once.

FOPT need not lie on that grid. In U, if the positive-eligible
players contain a basis, averaging one feasible unit per selected
player gives a positive fractional service lower bound
`lambda=v_min/r`. Otherwise FOPT is zero. In B with positive
budget, scale this average by
`alpha=min(1,C/C_max)` (or alpha=1 when all costs vanish), giving
`lambda_C=alpha*v_min/r`. This can be tiny numerically but its
binary encoding is polynomial. A relative-width search with
inner gap beta=epsilon/2 gives the claimed `(1-epsilon)FOPT`
fractional service before rounding, with base Gamma(2/epsilon).

If C=0, positive-cost coordinates are exactly forbidden even
fractionally; restriction to zero-cost coordinates is represented
by `f_j(S intersect Z_j)`. For C>0, a pair whose whole-unit cost
exceeds C can still be used fractionally and must not be deleted
when comparing to FOPT_C. The final B manuscript states this
distinction explicitly, and its lower-bound construction respects it.

## 6. Boundaries and public attribution

The abstract selector can also be a polynomial exact common-basis
or fixed selection-cost selector. This is distinct from the one
assignment budget treated by B. No third-matroid exact-quota
intersection claim is being made.

These are additive theorems. They do not supply a general unrelated
or budgeted factor-two approximation when u_p is comparable to
OPT. A common-value heavy/light partition cannot simply be copied
to unrelated values: the same resource can be heavy for one player
and light for another. With a budget, independently feasible heavy
and light assignments can also overspend their shared budget.

Classical cost-preserving largest-unit rounding for ordinary items
is an acknowledged primary-source ingredient, not claimed as new.
The checked ICALP 2025 paper by Rohwedder, Rouhani and Wennmann
explicitly recalls that fact and gives a separate randomized
logarithmic guarantee for budgeted intrinsic-value Santa Claus.
The project contribution reviewed here is the stated deterministic
corank selection composition with recipient polymatroids and its
fully specified oracle, rounding and bit-complexity interfaces.
No first-publication claim follows from this mathematical audit.

**Disposition:** U1--U24 and B1--B17 are accepted for checkpoint N
with the exact scopes, additive terms and comparators above.
