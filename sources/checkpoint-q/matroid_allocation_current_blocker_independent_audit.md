# Independent audit: current-blocker matroid allocation

**25 October 2026.** Audited construction:
`matroid_allocation_current_blocker_quasipolynomial.md`, Sections 1--8.

**Verdict:** the stated deterministic quasipolynomial construction and
its explicit infeasibility alternative pass this audit. The accepted
quality guarantee is `(T-u)/3-epsilon T` for the player-basis LP
`Q(T)`, not a constant one-third guarantee without the largest-item
term. A separate public-comparison audit remains necessary before any
global novelty claim. Section 9's ordinary-Santa-Claus reduction is
checked separately below.

## 1. Exact interface

The ground set is the set of players. A basis of that matroid must be
selected and supplied with mutually disjoint bundles of liked
resources. The resource values are player-independent. The supplied
fractional promise, used only in the proof, is

\[
 x\in P_{\mathcal B(\mathcal M)},\quad
 \sum_jv_jy_{pj}\ge T x_p,\quad
 \sum_p y_{pj}\le1,\quad 0\le y_{pj}\le x_p.
\]

The last constraint is essential for the available-resource argument.
The result does not apply by merely assuming an assignment LP with
`y_pj<=1`.

The source model is exactly the one in
[DRZ v4, equation (1) and Theorem 2](https://arxiv.org/html/1807.07189v4).
The new algorithm does not import the source's disputed earlier
post-collapse growth invariant. It proves a different invariant using
individual exchanges and a fresh last-layer extension.

## 2. The earliest-circuit rule preserves every retained lower span

Let the current matched player set `I` be independent. Suppose a free
bundle with owner `p` is eligible in layer `i`, so

\[
 p\notin\operatorname{cl}(I\setminus Y_{<i}),
\]

where a blocking set denotes its player set in matroid expressions.

If `p` is outside `cl(I)`, its addition is a valid rank augmentation.
If `p` belongs to `I`, eligibility forces `p` to occur in an earlier
blocking set. Replace its old bundle directly. This special case is
necessary: a new-element fundamental circuit is not defined for
`p in I`.

Now let `p in cl(I)\I`. Let `C` be the unique circuit in `I+p`.
It intersects `Y_<i`; otherwise it would witness
`p in cl(I\Y_<i)`. Choose `y` from the earliest layer `j` represented
in this circuit. For every `h<=j`, the circuit avoids `Y_<h`, and
therefore lies in

\[
 (I\setminus Y_{<h})+p.
\]

Its chosen element `y` is present in the independent set
`I\Y_<h`. Exchanging `y` for `p` gives another basis of exactly the
same span. Hence, with `I'=I-y+p`,

\[
 \operatorname{cl}(I'\setminus Y'_{<h})
 =\operatorname{cl}(I\setminus Y_{<h})
 \qquad(h\le j).
\]

This proves the required equality of eligibility sets. Merely knowing
that `I'` is independent would not suffice. For `h>j` the equality
need not hold, which is why every higher layer is discarded.

## 3. Resource consistency, free-centre cascades, and fresh maximality

All selected bundles are physically resource-disjoint, even when
several selected bundles have the same player label. Every matching
blocker belongs to exactly one selected bundle. These are stronger
physical conditions than anticompleteness after removing within-class
edges in an independent-transversal graph.

A newly added blocked bundle avoids all earlier selected and blocker
resources. Therefore every newly discovered matching blocker is new,
and it cannot also block an earlier selected bundle. The greedy
extension preserves the unique-blocker invariant.

A free candidate is disjoint from the current matching. When it
replaces blocker `y` in layer `j`, it is also disjoint from every
retained selected bundle. This holds both for a newly found candidate
and for an old selected bundle that has just become free: the latter
belongs to a higher layer than `j` and all selected bundles were
resource-disjoint. Thus no retained selected bundle acquires a new
blocker.

Removing `y` can free at most its one selected owner. This old selected
bundle must be processed immediately, before searching only for new
available bundles. Its eligibility is preserved by the span equality.
If it does not augment, its chosen exchange lies at a strictly earlier
layer. The cascade length is therefore bounded by the old stack depth.

For `h<j`, both the eligibility set and the entire forbidden resource
set through layer `h` are unchanged. Its previous maximality statement
is literally still true. Layer `j` can lose some forbidden resources
when `y` disappears, so only that last surviving layer needs a fresh
greedy extension. No higher layer remains to carry a stale assertion.
This validates the main note's simplification from full superposition
to refreshing only the last surviving layer.

## 4. The star-resource inequality needs no small-item assumption

Let a completed prefix contain `a` selected bundles and `t` matching
blockers. A minimal `B`-bundle has value less than `B+u`, where
`u=max v_j`. Every blocker intersects its unique selected owner, so
its value outside that selected bundle is less than `B`. Thus

\[
 v(F)<(B+u)a+Bt\le(2B+u)t,
\]

using `a<=t` at a fully blocked boundary. Summing may overcount
resources, which only strengthens this upper bound.

The proof is valid also for `u>B`. A bundle containing a resource of
value at least `B` is a singleton; any intersecting minimal blocker is
the same singleton, whose value outside the centre is zero. There is
no hidden hypothesis `u<=B`. The numerical guarantee is nontrivial
only in the explicitly stated range `T>u` and `B>0`.

## 5. Current growth and the fractional infeasibility witness

Let the matroid rank be `r`, `k=|I|<r`, and

\[
 J_0=I\setminus Y_{<i},\qquad
 U_i=P\setminus\operatorname{cl}(J_0),\qquad
 w=1+|Y_{<i}|.
\]

The flat `cl(J_0)` has rank `|J_0|=k-|Y_<i|`. A base-polytope
vector consequently satisfies

\[
 x(U_i)\ge r-|J_0|\ge w.
\]

Fresh maximality means `v(L_p\F_i)<B` for every `p in U_i`.
The inequalities `y_pj<=x_p` bound the fractional value available
outside `F_i` by `B x_p`. Summing over `U_i` and using resource
capacities yields

\[
 v(F_i)\ge(T-B)x(U_i)\ge(T-B)w.
\]

Put `A=2B+u`. With `B=(T-u)/3-epsilon T`,

\[
 (T-B)-A=3\epsilon T,\qquad A<T.
\]

If the current layer has `|Y_i|<=epsilon w`, the resource upper
bound is at most `A((1+epsilon)w-1)`, which is strictly less than
`(T-B)w`. The coefficient gap alone is
`3 epsilon T-epsilon A>2 epsilon T`.

Therefore every completed feasible layer has current growth
`|Y_i|>epsilon(1+|Y_<i|)`. This argument makes no reference to a
layer's birth size.

On failure, the explicit triple `(J_0,cl(J_0),F_i)` is a certificate:
its available-value inequalities can be checked from liking lists and
its flat from independence queries; its total value is less than
`(T-B)(r-|J_0|)`. The same rank/capacity argument rules out every
fractional point of `Q(T)`. It does not merely rule out the current
partial allocation.

## 6. Termination includes intermediate, unfinished layers

At a settled boundary, all completed layers satisfy current growth
and their blockers are disjoint subsets of a size-`k` matching. Their
depth is at most `O(epsilon^{-1} log(q+1))`. There can be only one
extra unfinished last layer. A collapse never adds a layer, and a
last-layer refresh occurs before another append.

Use the integer signature

\[
 (-|X_1|,|Y_1|,\ldots,-|X_l|,|Y_l|,\infty).
\]

An append, a blocked addition, or a nonaugmenting free exchange each
strictly decreases its first changed coordinate. Deleting higher
layers cannot reverse the earlier decrease. A temporarily free old
centre does not enlarge the selected count. All finite coordinates
remain between `-q` and `q`, and the temporary length bound is one
more than the completed-depth bound. Thus the number of state-changing
events per rank-augmentation phase is

\[
 (q+1)^{O(\epsilon^{-1}\log(q+1))}.
\]

There are at most `q` successful phases. Scans that find no candidate
either complete a layer or output the infeasibility certificate; there
is no loop of state-free failed trials.

## 7. Implementation and arithmetic

Each event can be implemented by a fixed polynomial in `q` times the
explicit input volume. Eligibility uses independence tests on
`J_0+p`; available values use explicit liking lists and resource marks.
A circuit can be recovered by testing `I-a+p` for each `a in I`.
Resource-owner and blocker-owner pointers detect the next free centre.

The bundle-selection rule only needs inclusion minimality. A fixed
resource order, threshold crossing, and one deletion pass suffices.
It requires neither a minimum-value feasible bundle nor a bundle
minimizing the number of blockers. All selected bundles can be stored
explicitly because they are resource-disjoint.

Rational subset sums have polynomial bit complexity in the numerical
input size. The logarithms in the analysis are not computed by the
algorithm. Counts are integers and growth tests use exact rational
comparisons. These observations support the main note's
input-linear multiplier times a polynomial in `q`, absorbed into its
quasipolynomial factor, and its polynomial space bound.

## 8. Public comparison and ordinary Santa Claus

The numerical comparison with corrected
[DRZ v4 Theorem 2](https://arxiv.org/html/1807.07189v4) is accurate:
the current polynomial theorem has the one-fifth coefficient, while
the audited algorithm allows quasipolynomial time for one third.
Earlier DRZ versions and the 2021 Davies dissertation contained
one-third claims. This audit does not establish that the numerical
coefficient is historically new, or that no other public specialization
matches it.

The public large-resource reduction can be verified directly. For a
threshold `theta T`, let `N` be the transversal matroid of players
matchable to a large resource. Its complementary basis matroid selects
the players who must receive small resources. DRZ's compact Santa
Claus relaxation has large-assignment mass `a_p` and small assignments
`z_pj` satisfying

\[
 v(z_p)\ge T(1-a_p),\qquad z_{pj}\le1-a_p,
 \qquad\sum_pz_{pj}\le1.
\]

Extend the large-assignment vector coordinatewise from the matroid
polytope of `N` to a base vector `a'`. For `a_p<1`, multiply all its
small assignments by `(1-a'_p)/(1-a_p)`; when `a_p=1`, all those
assignments were zero and remain zero. The resulting vector
`x=1-a'` is in the base polytope of the dual matroid, and the scaled
small assignments satisfy exactly `Q(T)` for that matroid. No
resource capacity increases.

The new allocation gives every chosen small-resource player at least
`((1-theta)/3-epsilon)T`. Its complementary player set is a basis of
`N`, so an ordinary bipartite matching gives each other player a large
resource. The minimum value is

\[
 \min\{\theta,(1-\theta)/3-\epsilon\}T.
\]

Taking `theta=(1-3epsilon)/4` closes the conditional reduction in the
main note's Section 9 and gives `(1-3epsilon)T/4` against that compact
relaxation. The explicit LP can be supplied or solved in polynomial
time. This is still a factor greater than four and has no claim to
improve Cheng--Mao's polynomial `4+delta` result for ordinary
restricted Santa Claus.

## 9. Rank dependence and the exact additive endpoint

The bounds in Sections 6--7 admit a stronger parameterization by the
matroid rank `r`, while the total number `q` of ground-set players
remains inside the explicit input volume. In a phase, `k=|I|<r`.
At every settled state,

\[
 \sum_i|X_i|\le k,
 \qquad\sum_i|Y_i|\le k.
 \tag{9}
\]

These inequalities also hold at each free-cascade microstate. A new
free candidate is not stored in an `X_i`; subsequent free exchanges
only truncate selected layers and delete blockers. A blocked addition
is performed only after restoring the fully blocked invariant, and
receives at least one new blocker. Thus there is no extra selected
object in (9), even transiently.

For positive epsilon, the completed-layer growth proof gives depth
`O(epsilon^{-1} log(r+1))`. Each integer signature coordinate has
magnitude at most r. Consequently the previous quasipolynomial bound
improves to `(r+1)^{O(epsilon^{-1} log(r+1))}`.

There is also an epsilon-independent count. Since every completed
layer has a blocker and there is at most one unfinished tail, there
are at most r layer pairs. The absolute coordinate sum is at most
`2k<2r`. Padding and marking the tail only adds a constant factor to
the dimension. Stars and bars bounds the number of possible ordered
integer lists by `2^{O(r)}`. This argument counts reachable signatures,
not the exponentially larger collection of resource assignments;
strict lexicographic descent already prevents returning to an earlier
signature with different resource identities.

Each microevent is implementable in `mathcal P poly(r)` work and
oracle calls: scanning all q players and liking lists is charged to
`mathcal P`; every tested independent set has at most r elements;
finding a fundamental circuit takes at most r tests; there are at
most r phases. No additional power of q is required outside the
input factor. Combining the two counts gives

\[
 \mathcal P\min\left\{2^{O(r)},
        (r+1)^{O(\varepsilon^{-1}\log(r+1))}\right\}
       \operatorname{poly}(b+\log\mathcal P).
 \tag{10}
\]

At epsilon zero, take `B=(T-u)/3>0`. Empty completed layers are
still impossible under `Q(T)` feasibility: their resource cover has
value strictly below `(2B+u)(w-1)`, whereas fractional feasibility
requires at least `(T-B)w`, and now `T-B=2B+u`. Hence all completed
layers remain nonempty. The algorithm, exchange invariants and
integer-signature descent require no positive epsilon; only the
geometric depth improvement did. It therefore returns the **exact**
additive boundary `(T-u)/3`, or a valid infeasibility certificate,
in `mathcal P 2^{O(r)} poly(b+log mathcal P)` work and oracle calls.

This is a fixed-parameter bound in the matroid rank under the stated
independence-oracle model, with the input representation and numerical
bit cost explicitly paid. It does not assert that this endpoint or
parameterization is globally new without the separate public audit.

