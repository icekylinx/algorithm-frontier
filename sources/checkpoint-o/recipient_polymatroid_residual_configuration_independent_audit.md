# Independent audit of the residual-capacity configuration relaxation

**25 October 2026. Full review of L1--L15 completed successfully.**

This note reviews
`recipient_polymatroid_residual_configuration_relaxation.md`. It accepts
the stated strengthened-LP approximation theorem on top of the separately
audited compressed prefix algorithm. This is an internal mathematical
review, not external peer review or formal verification. In particular,
the audit does not establish efficient separation or optimization of the
new relaxation.

## 1. Each proposed cut is an explicit valid linear inequality

For an integral feasible reserve z in P(f), the individual additional
capacity is

\[
 a_p(z)=\min_{S\ni p}\{f(S)-z(S)\}.
\]

This is exactly the largest nonnegative integer a with z+a e_p feasible:
sets omitting p are unchanged, and sets containing p give precisely
these inequalities. Feasibility makes every slack nonnegative, and the
singleton bound makes the maximum finite. The value is computable for
a fixed z by submodular minimization with p forced into the set.

For two feasible integral count vectors z,n, realize independent natural-
matroid sets Z,N with those counts. Extend Z to a basis of Z union N.
The added set H is a subset of N minus Z, with at least |N|-|Z| units.
Its block counts h satisfy h<=n and h_p<=a_p(z). Therefore

\[
       \sum_p(n_p-a_p(z))_+
          \le\sum_p(n_p-h_p)\le z(P).
\]

This directly proves validity for every integral allocation. An integral
target allocation puts mass one on the configuration of each selected
player, so its resource cut is exactly this inequality. Taking convex
combinations preserves validity. For fixed z, the configuration-variable
coefficients (n_j-a_pj(z))_+ are nonnegative integers, making the proposed
cut linear. The finite family is a genuine outer relaxation of the
integer problem, although it need not have a compact representation.

## 2. Dependent reserved sets really produce one of these feasible cuts

The algorithm's reserved copy set W need not be independent. Choose
a basis Z of W. It is a feasible integral count vector with total
z(P)=r(W). Since Z and W span the same flat, for every player block E_p

\[
 r(Z\cup E_p)-r(Z)=r(W\cup E_p)-r(W).
\]

The left side is a_p(z): all unused copies of a player are symmetric,
and the natural-matroid residual rank equals the maximum number of
additional copies of that player. The right side is exactly the
algorithm's available capacity A_p. Thus the selected cut has the
correct capacity coefficients and right side r(W), with equality rather
than a potentially lossy comparison.

A basis count vector can be found without expanding copies by maximizing
the total of P(f) under the coordinate box specified by W. Integral
box restriction and greedy polymatroid optimization give a maximum-sum
subvector with polynomially many paid submodular-minimization queries.
The allocation algorithm does not need this vector to run; it is useful
if one wants a concrete numerical failure certificate.

## 3. The failed available scan gives the claimed strict LP cover

Clipping an original local configuration coordinatewise to min(n_j,A_pj)
keeps it in the player's downward-closed family and in the exact box
queried by the available-count oracle. A complete failed factor-lambda
scan therefore makes each such clipped configuration worth strictly less
than B/lambda. Mixing the positive configuration mass of an eligible
player gives retained value strictly below (B/lambda)x_p.

The original configurations each have value at least T. Their lost value
is exactly the sum of v_j(n_j-A_pj)_+. Applying the cuts supplied by
the basis reserves above and summing over resource types bounds all such
lost value by Phi=sum_j v_j r_j(W_j). The coefficients are nonnegative,
so restricting the left side to eligible players can only decrease it.
The player-base polytope supplies eligible mass at least w>0. Hence

\[
                       \Phi>(T-B/\lambda)w
\]

for T>=B/lambda. Positive eligible mass preserves strictness, including
at the equality T=B/lambda. This is precisely the lower-cover premise
of the already audited prefix algorithm. No LP point, configuration
decomposition, or cut-separation procedure is used by that algorithm.

## 4. The fat reduction preserves the entire cut family

Choosing one fat unit in each fat-containing configuration gives a
one-service column bounded by its original resource column and by the
unit box. The Boolean restriction of P(f_j) is a matroid independent
polytope, so the existing fat union and dual-player complement operation
applies. The resulting small-player base vector is bounded by the mass
of all-small configurations.

Discarding the fat-containing configurations and scaling each remaining
player row downward preserves the small-resource aggregate constraints.
It also preserves every residual-capacity cut: all of its coefficients
are nonnegative and all remaining configuration masses have only
decreased. Small-resource ranks, feasible reserve vectors, residual
capacities and right sides are unchanged. The player ground set also
stays the same when the selection matroid is replaced by its derived
dual-union complement. Thus no reserve cut is lost through a hidden
change of coordinates or an altered resource function.

The exact-boundary and positive-error factors consequently follow from
the already audited sharp cover and signature, including the uniform
positive growth margin. The integer-optimum theorem follows because
every integral target allocation is feasible in this strengthened LP.

## 5. Support restriction and scaled-matroid redundancy are valid

At a completed normalized state in a rank-r phase, there are at most
r-1 current matching records and at most that many selected centers.
The reserve has at most 2(r-1) distinct player owners; a basis of it
cannot have more. Therefore cuts on feasible reserves with that support
bound suffice for every lower-cover argument. The derived player rank
only decreases, so retaining the original bound is safe throughout the
fat reduction. For rank one, the separate direct local optimization
argument handles the zero support bound.

For f=c r_R, the independently audited scaled-matroid lemma gives

\[
                  \sum_p(1-a_p/c)y_p\le z(P).
\]

Every local count lies between zero and c at a nonloop. Therefore
(n-a_p)_+<=(1-a_p/c)n. This holds trivially for n<=a_p, and otherwise
reduces to a_p n/c<=a_p. Mixing configurations and applying the lemma
proves each residual cut from the existing component column constraint.
The new cuts are therefore redundant for a supplied scaled-matroid
type, but need not remain redundant after merging different types.

## 6. The rank-gap point is rejected and complexity claims stay scoped

In the explicit aggregate gap instance f(S)=|S|+D for nonempty S,
q=Dr, D>=r>=2, reserve D+1 units at one player a. Its residual is zero
at a and one at every other player. The displayed mass-1/D
configurations of D+1 units yield cut left side

\[
                    (D+1)/D+(q-1)=q+1/D>D+1.
\]

The violated support-one cut is valid, so this correctly excludes the
earlier fractional obstruction without asserting that all fractional
points are integral.

For a fixed reserve and an explicitly represented configuration point,
evaluating the cut is polynomial in that explicit description and the
paid oracle costs. Finding a violated reserve or pricing configurations
under arbitrary dual weights is a separate problem. The manuscript
correctly makes neither efficient-separation nor efficient-LP-solution
claims. Its actual deterministic allocation time and space are those
of the existing compressed search; the new theorem strengthens the
comparison target through a soundness proof, without adding hidden
LP-solving work.
