# Independent polymatroid audit of the shared setup-and-assignment budget

**25 October 2026. Full independent read of SD1--SD15 in
`unrelated_allocation_shared_setup_budget.md`. This is the review owned
by the polymatroid-transfer agent, separate from the other SD audits.**

The theorem passes. The persistent zero-utility dual resource, its signed
auxiliary objective, and final dummy-free basis extraction preserve the
original nonnegative setup-plus-assignment budget exactly. The current
service projections remain appropriate for the weighted omission gap,
and the zero-adjoined target benchmark closes optimization without an
unproved optimizer over unknown role sets.

The result retains arbitrary nonnegative unrelated values, arbitrary
integral recipient polymatroids, one original player matroid, one combined
budget, the stated near-two guarantee, and polynomial space. This audit
does not infer an extension to multiple exact budgets or arbitrary
negative costs in the original problem.

## 1. Original zero-utility feasibility is tested correctly

Every selected original basis must pay its setup fees, even when no
resource units are assigned. With nonnegative original assignment costs,
the original instance is feasible at any utility precisely when some
M-basis has setup cost at most C. Minimum-weight basis optimization
therefore gives the correct initial feasibility test.

If affordable, the returned minimum-setup basis with zero original
counts is a legal original output. If unaffordable, adding any original
assignment cannot repair the budget. Rank zero is handled separately,
so no finite objective is assigned to a minimum over an empty set.

Counts on player-matroid loops or outside a selected original basis can
be discarded without harming its utilities. Thus the protected optimum
may be assumed to allocate only on its actual selected basis before
the auxiliary construction is applied.

## 2. The signed dummy is an exact accounting device at integer outputs

The dummy vector belongs to P(M*), so its coordinates are at most one.
Its integer support D is M*-independent, possibly smaller than a dual
basis. The dual rank identity implies that P\D spans M. It therefore
contains an actual M-basis B, obtainable by ordinary matroid optimization.

At an integer auxiliary point, the setup part of the affine expression is

\[
 S_\sigma-\sum_p\sigma_p y_p=\sum_{p\notin D}\sigma_p.
\]

For every basis B inside P\D, its actual setup fee is at most this sum.
Discarding original resource counts outside B cannot increase their
nonnegative assignment cost. Hence the actual original combined cost
is at most the auxiliary affine cost, exactly as in SD6.

This deduction does not require D to be a full dual basis. That matters
because free disposal and rounding may leave some dummy units unused.
It also does not require finding a minimum-setup basis after rounding:
every basis in the dummy-free set has the displayed budget bound and
the same pointwise utility guarantee proved below.

The affine expression is not being treated as a new original model
with arbitrary negative assignment costs. Its negative terms have the
specific meaning of credits for dummy-covered, hence avoidable, players.
Those terms are retained until the integer complement extraction.

## 3. The dummy must remain available inside the light ground

Each real type keeps one masked rank f_j^Q, coupling all of its allowed
light and heavy recipients. The dummy rank M* stays on every original
player, including those inside Q. Its utility in the light projection
is zero. It must not be removed by the positive-value preprocessing
used for ordinary nonnegative-cost resources.

For a canonical original optimum with selected basis B*, the dummy
indicator on P\B* is a full dual basis. It cancels exactly the setup
fees of originally unselected players. At a protected node Q containing
the optimal small-only selected set I*, those dummy counts remain
unchanged even when their owners lie inside Q.

Real heavy units on Q\I* can be discarded because their assignment
costs are nonnegative. Deleting a dummy credit there would instead
increase the affine objective and could destroy feasibility. The
manuscript performs only the former operation and explicitly retains
the latter coordinates.

## 4. Empty current regions and signed budget rows are handled properly

For fixed Q, SD8 is a bounded rational polytope with original real
resource ranks, the dummy matroid rank, explicit unit count equalities
outside Q, and one affine budget row. Its right side C-S_sigma may be
negative. A bounded feasibility LP permits that sign; it does not need
a zero count vector to be feasible.

The algorithm tests this polytope for emptiness first. If nonempty,
its lower projection onto nonnegative real light utilities contains
zero, is compact and convex, and is downward in the *service vector*.
Indeed the same witness supports every smaller service vector. No
assertion that the full signed-cost count region is downward is needed.

Nonnegative support optimization and the normalized outer support LP
therefore apply just as in the joint-role theorem. The support capacity
is nonnegative because the service region contains zero. A negative
right side in the internal cost inequality does not turn into a negative
capacity or a signed coefficient in the service packing separator.

Uniform bit complexity also survives. The only new coefficients are
the original fees with negative signs and the sum S_sigma. These have
polynomial encoding. Rank rows remain zero-one with bounded integer
right sides; forced counts are one. Extreme support optimizers have
uniform polynomial-bit descriptions, and the outer LP inherits these
bounds. The mask and Q vary combinatorially, without recursively
generated numerical coefficients.

## 5. The protected-witness argument works for the entire benchmark family

The original optimum gives the required strong witness: retain all
light service at its small-only selected players, one original heavy
unit at each other selected player, and the canonical dummy basis at
all unselected players. The affine setup term remains exactly the
original selected setup fee. The discarded real assignments only
decrease cost and resource loads.

The proof needs more than this one optimum to justify the target
search. It must also preserve every full-role witness in the fixed
benchmark. SD Section 4 explicitly does so. Given a witness in X_I
and a larger allowed Q containing I, retain every dummy count, real
counts on I and outside Q, and discard real counts on Q\I. All
remaining real coordinates respect the new masks. Every player
outside Q keeps its total heavy-or-dummy count one. Resource loads
and nonnegative real costs decrease, while all negative dummy terms
are unchanged.

Thus its full light target on I remains in U_Q even if the original
full-role witness had dummy fractions on I itself. This proves the
needed invariant for the actual benchmark family, rather than only
for a special canonical integer witness.

A nonnegative row violated by b on all of Q then forces omitted weight
greater than a(Q)/R outside I. The weighted first-crossing certificates
include a deletion preserving I. Its child has the same invariant,
and at zero remaining deficit Q=I the weak query must succeed.
Empty-region rejection is impossible along such a protected branch.

The local enumeration and prefix-free cost depend only on R and the
remaining deficit. Uniform LP costs therefore give the claimed
all-input bound after every forced seed, including failed branches
and unpromised role families. No nesting of U_Q is assumed.

## 6. The signed rounding objective preserves the affine cost exactly

The previously proved count-prefix rounding can be used with a signed
linear objective. The reason is linear optimization on an integral
bounded face, not a monotonicity assertion about costs.

Extend every real and dummy independent vector to a base by adding
a zero-cost disposal coordinate. This changes no real-position count
and no signed linear objective. Let a be the integral singleton-capacity
vector and let z=a-w be the fractional complement of all resource
coordinates w. The prefix constraints and direct-sum dual ranks have
a nonempty integral maximum-total face containing z.

For the signed coefficient vector ell, one has

\[
                         \ell\cdot w=\ell\cdot a-\ell\cdot z.
\]

Maximizing ell*z over that integral face therefore gives an integer
original point with no larger signed objective. This identity is valid
for arbitrary signs. Bounded resource ranks ensure an optimum exists.
Adding the unchanged constant S_sigma then preserves the affine budget.

No real-position dummy is trimmed during or after this step before
the cost is converted by SD6. Disposal coordinates have cost zero and
can be removed safely. This is precisely the operation that the
original nonnegative-cost theorem could not justify by indiscriminate
coordinate deletion; the manuscript instead retains all auxiliary
credits until their interpretation is used.

## 7. Light utility, heavy count, and budget hold at the same point

At a player in Q, use the real light values in its own prefix order
and include the dummy with value zero. Keeping this zero-valued
coordinate is harmless for utility telescoping and necessary for
the signed objective. The largest positive value is at most u_L,
so the real light utility after rounding is at least b-u_L.

Outside Q, the full prefix includes all allowed real heavy coordinates
and the dummy. The fractional total is exactly one, so the integer
count-floor constraint gives real-heavy-plus-dummy total at least one.
This conclusion does not require the rounded total to remain exactly
one. It holds at the same integral point that minimizes the signed
objective and satisfies all masked resource constraints.

Let D be the resulting actual dummy support and take any M-basis B
inside P\D. If p is in B outside Q, its dummy coordinate is zero,
so at least one real heavy unit remains there and its utility is at
least a_H. If p is in B intersect Q, its real light utility is at
least b-u_L. Restrict original assignments to B and apply SD6.
This yields both the original budget and the asserted minimum
min{a_H,b-u_L}, with no additional optimization or resource allocation.

If there are no heavy pairs, a dummy-free player outside Q cannot
occur at a successful integer point; otherwise its count floor would
be violated. The infinity convention for a_H therefore causes no
spurious guarantee. Internal disposal recipients are not candidates
in the outer selection ground and do not increase its exponential
parameter q.

## 8. The zero-adjoined benchmark and non-role initialization are sound

For fixed mask and k<q, the full-role family is fixed independently
of the target. Its light selected set has positive cardinality, so
its service target is bounded by the original real-resource utility
bound V. Every nonempty role family's feasible targets are downward.
If the family is empty, adjoining zero defines X=0 without claiming
that a zero-role witness exists.

The saved nominal-zero output is the globally affordable minimum-setup
basis with zero original counts. It need not satisfy this particular
role pattern. Its actual utility zero nevertheless meets the weak
bound at nominal zero, since min{a_H,-u_L}<=0. The initialization
therefore supplies exactly what the one-sided search requires.

At a positive grid target, total gap failure excludes all full-role
witnesses of that target. Because feasible positive grid targets are
downward, failure implies T>X, including when the role family is
empty. The externally certified upper point V+g and these failures
maintain U>X. At adjacent endpoints the saved nominal lower L is
at least X. Every positive success has an actual recovered original
basis allocation; a final L=0 has the already legal zero output.

There is no need for an exact optimizer over unknown zero-role sets.
The benchmark also need not equal the original integer optimum for
every mask. The approximation proof uses only that the comparator
mask contains a full-role witness at original OPT. Allowing a larger
fractional role benchmark does not invalidate the search or the
legality of its weak outputs.

## 9. The all-heavy/dummy gate is an exact integral computation

For k=q, impose cap one on the total of real-heavy and dummy counts
at every player and seek total q. The direct-sum resource polymatroid
intersected with this partition polymatroid is integral. If total q
is fractionally feasible, its maximum-total face is nonempty and
integral. Minimizing the signed linear objective there gives an
integer optimum, with no larger cost than any fractional witness.

Add S_sigma and compare with C. At an accepted integer point, each
dummy-free player has one real heavy unit. Dual-rank extraction
therefore produces an original heavy-served M-basis of value at
least a_H and actual budget at most C. Conversely, an original
all-heavy selected basis plus its canonical dummy complement gives
an affordable total-q witness. Thus no pure comparator case is lost.

The total q is an explicit player count. The computation does not
expand numerical supplies and does not create an unbounded target
benchmark for an empty light set. Negative objective weights cause
no issue on this bounded integral face.

## 10. Approximation and complete running time

At theta*=alpha*OPT/2 for a positive original optimum, the canonical
extended witness has k=c+|F*| omitted light positions, where F* is
its selected heavy-recipient set. If it has a light selected player,
k<q and its full light target is original OPT. Since that value is
on the common value grid, the fixed benchmark X is at least OPT.
The saved weak light level is at least alpha*OPT, and
u_L<theta*<=a_H gives the claimed minimum theta* after recovery.
If every selected player is heavy, the pure gate gives the same bound.

For a supplied support cap K, the processed cardinalities include
every k<=min(c+K,q-1), and the pure gate is included when relevant.
Thus the conditional Gamma(R)^(c+K) bound follows. Processing all
k<q and the pure gate removes that support promise. The verified
forced-omission interface permits the global block conversion on
each finite target, yielding the stated base B(R) on the original
q players.

The number of masks, cardinalities, and binary target calls is
polynomial. All LPs, signed rounding faces, and output extractions
have uniform polynomial encodings and workspace. Fixed rational
Gamma comparisons and the safe varying-accuracy rational bound retain
the same distinction as in the global conversion. No larger raw-corank
fallback is hidden in the complete global algorithm.

## 11. Audit conclusion

All SD1--SD15 claims pass. The essential safeguards are explicit:
dummy credits persist on every original position; only nonnegative-cost
real assignments are removed from protected witnesses; signed costs
are optimized on a bounded integral face; zero-valued dummy coordinates
remain in the prefix system; and original budget recovery is proved
after integer dummy-free basis extraction.

The proof is a direct protected-optimum argument, not an equality
claim between the original optimum and a new large-valued dummy
problem. The zero-adjoined benchmark correctly avoids an unsupported
initial role optimizer. The resulting near-two theorem preserves one
shared nonnegative original setup-and-assignment budget in the stated
unrelated-value matroid-selection model.
