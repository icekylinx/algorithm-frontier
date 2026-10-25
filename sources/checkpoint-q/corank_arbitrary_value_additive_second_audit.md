# Independent audit of arbitrary-value additive allocation

**25 October 2026. Independent full review of V1--V19.**

This audit concerns `corank_arbitrary_value_additive_allocation.md`.
I read its complete argument independently of the author's derivation.
The claimed guarantee `(1-epsilon) OPT-u` in
`Gamma(1/epsilon)^c poly(H)` time passes the checks below.

## 1. The promise and the numerical quota gap

After deleting player-matroid loops, restricting every resource rank
preserves the selected-basis optimum: all bases avoid those loops and
resource feasibility is downward closed. If `1-epsilon=B/A`, the choice
`Delta=g/A` gives integral workload multipliers and exact quotas
`t=Ak`, `b=Bk` at target `T=kg`. Their ratio `t/(t-b)=1/epsilon` is
independent of k. Thus even the smallest positive target has a genuine
positive gap; the exact one-unit matroid-intersection gate is not used.

An original integer allocation at target T yields a vector in the sum
of the scaled resource polymatroids, with at least t units on its
selected basis. Pruning yields `t 1_I`, which is the precise promise
needed by the omission theorem. Throughout branching, the aggregate
resource is only restricted. No contraction changes that promise.

## 2. Completion and decomposition have binary polynomial size

The successful b-quota vector can be completed to a base without adding
units individually: saturate one coordinate at a time, using the
minimum residual rank slack of sets containing that coordinate.
Increasing other coordinates cannot make a saturated coordinate
augmentable again. A maximal polymatroid independent vector is a base.

On the product ground of players and resource types, the manuscript's
first rank is the direct sum of the scaled resource ranks; the second
imposes each completed player's exact total as an upper capacity.
For any product-ground subset S, let R contain the players whose copies
for every type belong to S. Then the second rank of the complement is
`w(P)-w(R)`, while the first rank of S is at least `F(R)>=w(R)`.
The polymatroid-intersection min-max condition is therefore satisfied
at total `w(P)`. Equality of that total forces all type components to
be bases and all player totals to match w.

Dividing each scaled component by its multiplier gives fractional
original-resource bases. The divisibility need not be integral, and
the note correctly retains a separate rounding step. The product
ground has only q times the number of types elements; numerical
multipliers remain binary encoded.

## 3. The lower-rounding lemma is proved at every player

For one original rank f, put `a(p)=f({p})` and
`f#(S)=a(S)+f(P\S)-f(P)`. Submodularity is preserved by complementing
the argument and adding a modular function. Every marginal is
nonnegative because an f-marginal is at most its singleton rank.
The affine map `x -> a-x` is an exact bijection between the two base
polytopes. In the inverse direction, nonnegativity follows from
`f#({p})<=a(p)`, and complementary base inequalities give all original
rank inequalities. The singleton-cap vector itself need not be a base.

After ordering values decreasingly, the prefix ceilings of the
fractional dual allocation define an integral polymatroid. At one
player its rank on a set of type indices is the maximum corresponding
prefix ceiling. Since these ceilings are nondecreasing, these rank
inequalities are exactly the required nested prefix upper bounds.
The starting fractional allocation lies in the intersection with
the direct sum of the dual resource polymatroids. An integral maximum
common independent vector reaches the total dual rank, so every
resource component is again a base.

Telescoping decreasing values against the prefix inequalities raises
each player's dual weighted load by at most the largest unit u.
Complementing back therefore lowers each player's original value by
at most u. This is a per-player bound, not merely a bound on the
minimum or the global average. It survives discarding all allocations
outside the selected basis because those operations do not change
selected-player counts.

## 4. Target search does not need algorithmic monotonicity

The original total value V is an external upper bound on any selected
player's value because the selected rank is positive. Thus `V+g` is a
sound infeasible upper endpoint, without calling the weaker gap
procedure there. A failed trial certifies that its original target is
infeasible. A successful trial supplies a constructive additive
guarantee but may lie above the true optimum.

Maintain a saved success at the lower endpoint and an upper endpoint
strictly above the true optimum. On adjacent grid indices, the lower
endpoint is at least OPT. The saved allocation consequently has the
advertised additive value. This remains valid even if the algorithm's
success pattern is nonmonotone, and it is not necessary for every
upper endpoint to be an observed gap-algorithm failure.

## 5. Scope and parameter accounting

The parameter is the original player matroid's corank after deleting
its loops. All quota magnitudes, value denominators, complement ranks,
and prefix ceilings have polynomial binary length. The omission tree
counts failed rank-test children as well as recursive survivors.
The reconstruction and both intersections have polynomial-size
grounds. These facts justify the fixed polynomial degree and the
polynomial-workspace claim.

Coordinate caps on one resource at one player can be absorbed into
that resource's rank by the standard box restriction. Couplings
between different resource types cannot be absorbed in this way and
could be violated by completion or rounding; the note correctly
excludes them. Common intrinsic values are also needed for the
aggregate workload identity.

The small-unit multiplicative corollary follows by paying both
`epsilon OPT` and u separately. It is not an unconditional integer
approximation scheme. The hidden optimum-two examples have largest
unit one, so this additive guarantee is consistent with their
strict-below-two oracle obstruction.

## 6. Comparison and conclusion

The source attribution to the public largest-unit additive rounding
is appropriate. In the compulsory-player case, the public fractional
LP plus rounding already yields `OPT-u` in polynomial time. The new
selection contribution is for optional matroid-basis players and a
corank-dependent bounded omission tree; it does not claim to improve
the compulsory-player additive rounding itself.

The complete V1--V19 proof passes this independent audit. In addition,
the argument works against the maximum engineered-grid workload
quota on a player basis, which can exceed the original integer
allocation optimum. That stronger intermediate comparator is safe
when followed by the same explicit u rounding loss and is used in
the separate heavy/light transfer. No stronger LP comparator is
claimed here.
