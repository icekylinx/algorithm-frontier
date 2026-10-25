# Independent audit of corank additive allocation with unrelated values

**25 October 2026. Full independent mathematical review of U1--U24.**

Reviewed manuscript: `unrelated_values_corank_additive_allocation.md`.

The theorem passes this review. Arbitrary nonnegative player-dependent
values are supported by a fixed downward utility polytope with an
exact nonnegative separating-row oracle. The weighted prefix-free
gap algorithm then selects a genuine player basis, and per-player
prefix rounding gives the stated additive loss. The integer-OPT
and selected-basis fractional-OPT searches have distinct, correct
precision arguments and the stated Gamma bases.

## 1. The two optima and preprocessing retain their intended meaning

The integer optimum uses independent integer resource vectors on
one actual selected M-basis. FOPT relaxes only resource counts;
its selected basis is still an actual set. The proof never mixes
different player bases fractionally. Both maxima are attained
because the resource polytopes are compact and there are finitely
many player bases.

Deleting player-matroid loops is safe: every basis avoids them,
and resource vectors restrict and extend by zero. A value on a
coordinate of singleton rank zero can be set to zero because
that coordinate is identically zero in its resource polytope.
Thus the defined u_p is a valid per-player largest possible unit
value after these harmless changes. Coordinate caps already
incorporated into each resource rank are preserved throughout.

No local constraint coupling different types is present. This
matters when independent fractional resource vectors are later
extended to bases and rounded.

## 2. The utility polytope is downward closed, including zero values

For nonnegative diagonal D_j, the image D_j P(f_j) is compact,
convex and nonnegative. Reducing a positive-value utility coordinate
is implemented by reducing the corresponding resource count.
A zero-value coordinate already has zero utility. Hence every
summand is downward closed.

A decrease of a coordinate of a sum can be distributed among
the nonnegative summands, so their Minkowski sum U is also
downward closed. This proves the equivalence between exact image
membership and the existence of resource counts dominating a
requested utility vector. The resource region remains fixed during
all candidate-ground deletions.

For nonnegative a, its support is the sum of the independently
optimized resource supports. Greedy optimization gives integral
base vertices because the weights a_p v_pj are nonnegative and
an independent vector can be extended without reducing objective.
The count coordinates are bounded by singleton ranks; no capacity
copies are needed.

## 3. The support LP supplies a valid polynomial-bit packing row

The LP over a>=0, a(P)=1 and support epigraph variables t_j is
bounded and nonempty. The choice t_j=V_j is feasible for every
simplex vector a. Indeed, each coordinate of a resource base is
bounded by its singleton rank, and every a_p is at most one.

Its implicit inequalities are indexed by resource base vertices.
Every such vertex is integral with polynomial-bit coordinates,
so the coefficients v_pj*x_p have a uniform polynomial bit bound.
The number of LP variables is polynomial. Strong separation of
each epigraph family is exact: maximize the current linear
resource objective by greedy and use the attaining vertex if
its inequality is violated. The simplex and interval constraints
are tested explicitly.

Consequently this is a well-described bounded rational LP with
exact separation, under the exact-LP primitive stipulated in H.
The optimizer can be chosen with polynomial encoding length even
when the feasible set has lower dimension, for example because
some V_j are zero. This step is not an approximate separation
argument or an assumed finite extraction from an invalid oracle.

At an optimum, each t_j can be lowered to its exact support h_j(a),
so the objective is a*z-h(a). If positive, recomputing h(a)
returns the valid row a*y<=h(a) with a nonnegative and h(a)
nonnegative. Products and sums of the polynomial-bit optimizer,
original values and greedy counts retain polynomial binary length.
This is precisely the row representation required by WP.

The possible rows are adaptive, but every one is globally valid
for the same original U. Their bit bounds depend on the original
data and the polynomially encoded query, not on accumulated
descriptions of previous rows. There is no recursive coefficient
blow-up from row to row.

## 4. Nonnegative normals characterize membership exactly

The sign reduction is valid and necessary. For any signed normal
a, downward closure implies h(a)=h(a_+): negative coordinates
can be set to zero without changing the retained positive
coordinates. If z>=0 is strongly separated by a, then
a_+*z>=a*z>h(a)=h(a_+).

The vector a_+ cannot be zero, since U contains zero and a
nonpositive normal cannot strictly separate a nonnegative z
above its support. Dividing by a_+(P) gives a simplex normal
with a positive support-LP objective. Therefore a nonpositive
optimum of that LP really proves z in U, including utility
regions with identically zero coordinates or lower dimension.

A generic signed separation theorem alone would not have supplied
the nonnegative row needed by weighted omission. The explicit
positive-part argument closes that interface.

## 5. The service gap and reconstruction use the same fixed region

For t>b>0, an integer target allocation on I* implies t*1_(I*)
belongs to U; so does a fractional target allocation. The exact
matroid restriction selector and the support separator satisfy
all hypotheses of the weighted prefix-free theorem. The returned
basis I is a genuine basis and has b*1_I in U. Failure excludes
every genuine basis attaining full service t.

For target T and parameter beta, taking t=T and b=(1-beta)T
uses ratio 1/beta exactly. Unlike the intrinsic workload route,
this proof needs no integer quota engineering: the weighted
packing theorem explicitly allows rational quotas.

Membership provides existence of the reconstruction LP for the
original resource counts and selected-player value inequalities.
Its resource separation is submodular minimization of f_j(S)-x_j(S),
and the remaining constraints are explicit rational rows. An exact
polynomial-bit solution therefore exists and is computable in
the assumed LP oracle model.

Every resource vector can be completed to a fractional base by
coordinate saturation. Increasing counts preserves the utility
requirements because values are nonnegative. This is justified
here because there is no assignment-cost budget or other local
coupling in the main U theorem. Such constraints require a separate
adapter and are not being ignored.

## 6. Different value orders at different players do not conflict

Complementing each resource base with its singleton-cap vector
produces a base of the integral monotone dual rank stated in
(U15). The affine map is exact in both directions, as proved
in the earlier additive manuscript.

At each player separately, sort the resource types by that
player's values and take integer ceilings of cumulative dual
counts. The rank in (U17) is the sum, over players, of maximum
element weights C_p,k. It is normalized, monotone, integral and
submodular. Because C_p,k is nondecreasing along that player's
own order, its rank inequalities are equivalent to the intended
prefix count constraints.

Changing the type order at one player does not alter the direct
sum of the resource dual polymatroids. Thus the two systems still
form one integral polymatroid-intersection instance on only q*m
coordinates. The fractional dual vector attains the full direct-sum
total rank, so an integer common vector of that total exists.
Equality of the total forces every resource component to remain
a base.

Telescoping each player's own decreasing values gives an increase
of at most u_p in its dual utility. Complementing back loses
at most u_p in original utility. This is a pointwise guarantee
for each selected player; it does not require a common global
ordering of types. Discarding counts outside the selected basis
preserves resource independence and the selected utilities.

## 7. The integer-optimum search has an exact grid comparator

Choose g dividing every player-resource value. Integer allocation
utilities and integer OPT are g-grid values, while V bounds all
such utilities. The external upper target V+g is infeasible,
regardless of whether the weaker gap procedure might succeed
there. Zero is a valid initial saved lower target.

Every failed trial excludes the fractional target, hence excludes
the integer target. The upper endpoint stays strictly above OPT.
At adjacent grid indices, the successful lower endpoint L is
at least OPT. Its saved service is (1-epsilon)L, and one final
reconstruction and rounding proves (U4).

No success is treated as full target feasibility and no monotone
success behavior is assumed. If L remains zero at termination,
the grid invariant implies OPT=0, so the zero allocation suffices.
The runtime base is Gamma(1/epsilon), and the number of target
trials is polynomial in the numerical encoding length.

## 8. The positive fractional scale is constructive

A player has positive possible utility exactly when it has some
positive-value resource coordinate of singleton rank at least one.
Integrality of ranks makes that test exact. If no allowed basis
is contained in P+, every basis includes a zero-utility player,
so FOPT=OPT=0.

Otherwise choose one permitted basis I inside P+. For each of
its r players choose an eligible type. Giving one unit solely
to that player is a feasible whole-instance allocation: every
resource set containing it has rank at least its singleton rank,
and all other coordinates are zero. Averaging these r allocations
is resource-feasible and gives every member of I at least
v_min/r. Thus lambda=v_min/r is both a positive lower bound
on FOPT and an explicitly realizable saved fractional target.

This works even if many selected players choose the same scarce
resource. The averaging divides the entire vector by r, so it
uses convexity rather than assuming simultaneous integral service.
The scale has polynomial binary length. Restricting candidate
players to P+ preserves any positive FOPT and can only reduce
the corank used by the gap routine.

## 9. Relative search does not assume that FOPT is a value-grid point

For the fractional comparator, beta=epsilon/2 leaves room for
search precision. The upper endpoint V+lambda exceeds FOPT,
and every failure keeps the upper endpoint above FOPT. At
termination, U-L<=epsilon*lambda/2, so

\[
 L\ge\operatorname{FOPT}-\epsilon\lambda/2
       \ge(1-\epsilon/2)\operatorname{FOPT}.
\]

The saved service is at least (1-epsilon/2)L. Therefore it is
at least (1-epsilon/2)^2 FOPT, which is at least
(1-epsilon)FOPT. The initial lambda allocation already meets
its own saved-service requirement, including termination before
any midpoint call. One rounding then proves (U5).

The original inequality lambda<=FOPT is the correct direction
for converting the absolute search tolerance to relative loss.
Midpoint denominators grow by only the polynomial number of
iterations, bounded by the logarithm of V/(epsilon*lambda).
The gap ratio is 2/epsilon, yielding the stated second runtime.

The argument handles a genuine selected-basis fractional optimum,
not a fractional player-base relaxation, and does not assume that
FOPT lies on the integer allocation grid.

## 10. Scope, source check and outcome

The selector generalization in Section 10 is valid: the proof
needs only a restriction oracle for a fixed-cardinality family.
The positivity test becomes a selector call on P+, and the
averaging construction uses its actual returned member. Exact
player-selection budgets remain valid because resource rounding
does not change the chosen set. This does not by itself preserve
a budget on assignment counts.

The primary ICALP 2025 source was freshly checked:
[Rohwedder, Rouhani and Wennmann, Cost Preserving Dependent Rounding
for Allocation Problems](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.127/LIPIcs.ICALP.2025.127.html),
Section 1 and Lemma 10. Its discussion explicitly records the
ordinary-item additive rounding for unrelated values without a
cost increase. The manuscript correctly treats this rounding as
background and does not transfer an intrinsic-value multiplicative
baseline to unrelated valuations.

No gap was found in U1--U24. The nonnegative polynomial-bit
separator, fixed resource region, primal reconstruction, local
value orders, zero-FOPT test, positive scale and both search
orientations are accounted for. This is independent internal
mathematical review, not formal verification or external peer review.
