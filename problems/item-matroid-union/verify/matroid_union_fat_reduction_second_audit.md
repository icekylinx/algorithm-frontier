# Verification note

**Curated source path:** `sources/checkpoint-o/matroid_union_fat_reduction_second_audit.md`

The source audit follows.

# Second audit of the matroid-union fat-resource reduction

**25 October 2026. Full mathematical and oracle-accounting audit passed.**

This audit checks `matroid_union_fat_resource_allocation.md`, including
its exact rank factor \(d_r=4-3/r\), positive-error guarantee,
target search, and boundary cases. It assumes only the independently
audited local operations of the current-blocker small-resource solver;
the sharper inner threshold used here is proved directly below.

The comparison is the integral optimum of the arbitrary player-basis
allocation problem. It is not a claim that a feasible point of the
original compact LP with arbitrary large items can be rounded at this
factor.

## 1. The forward promise uses exactly the correct matroid

Let \(I\) be an original \(M\)-basis with value-at-least-\(T\)
allocations, and let \(D=P\setminus I\). Then \(D\) is an
\(M^*\)-basis. Let \(F\subseteq I\) be the players whose given
allocations contain at least one fat item. Select one such item per
player. They are distinct because the original allocation is disjoint,
so \(F\) is independent in the fat transversal matroid \(N\).

The sets \(D,F\) are disjoint. Their union is independent in
\(U=M^*\vee N\), so it extends to a \(U\)-basis \(B\).
Its complement is a \(U^*\)-basis contained in \(I\setminus F\).
Every remaining player retains a disjoint all-small original bundle
worth at least \(T\). This gives an integral feasible point of the
derived compact LP.

Players in \(I\setminus F\) may like fat items. That does not affect
the proof: they did not receive any fat item in the chosen witness.
Extension to \(B\) may discard some of these players, but cannot
destroy feasibility for the surviving subset.

Thus failure of the inner compact-LP certificate implies
\(\mathrm{OPT}<T\). Neither an optimum witness nor an auxiliary
fractional solution is algorithmic input.

## 2. The reverse reconstruction permits the necessary deletions

Let \(S''\) be the returned \(U^*\)-basis, with disjoint small
bundles. Its complement \(B''\) is a \(U\)-basis. An explicit
union decomposition partitions it as

\[
 B''=D''\mathbin{\dot\cup}F'',\qquad
 D''\in\mathcal I(M^*),\quad F''\in\mathcal I(N).
\]

Give each \(F''\) player a distinct liked fat item. Extend \(D''\)
to an arbitrary full \(M^*\)-basis \(D'''\). No constraint that
this extension avoid \(S''\) or \(F''\) is needed. Its complement
is an original \(M\)-basis contained in \(S''\cup F''\), since
\(D''\subseteq D'''\). Every retained player already has an
allocation. Deleting allocations belonging to removed players
preserves all values and disjointness for the retained players.

This verifies the step that can otherwise be easy to misstate: the
first union part need not already have full dual rank. Extending it
and deleting the corresponding supplied players is legitimate.

## 3. The inner exact threshold and weak certificate are valid

Let the derived rank be \(r'\le r\), and suppose \(r'>0\).
During a phase let \(k<r'\) be the current matching size, \(s\)
the earlier blocker count, and \(y\) the current last-layer count.
Put \(w=r'-k+s\). Then

\[
       1\le w\le r',\qquad
       s/w\le(r'-1)/r'\le\rho_r=(r-1)/r.
\]

The resource cover satisfies
\(v(F)\le(2B+u)(s+y)\). At a maximal layer, each eligible player's
liked value outside the cover is strictly below \(B\). Since
\(y_{pj}\le x_p\) and the eligible base mass is at least \(w>0\),
the compact LP would require

\[
                         v(F)>(T-B)w.
 \tag{A1}
\]

The strict inequality is valid even at \(B=T\). With
\(\theta_r=1/(4-3/r)\), \(B=\theta_r T\), and small items
\(u<\theta_r T\), an empty last layer instead gives

\[
 v(F)\le(2B+u)s\le3\theta_r T\rho_r w=(T-B)w.
\]

Thus the weak cover certificate is sound: explicitly checking
\(v(F)\le(T-B)(r'-|J_0|)\) suffices together with strict
outside-value maximality. The older theorem's stricter certificate
format is not being silently reused.

Every passing completed layer has at least one matching blocker.
The unchanged integer signature therefore pays all operations in
\(2^{O(r')}\) states. All target and oracle costs are polynomial per
state. This proves the exact factor \(4-3/r\), including the fact
that the derived matroid can have strictly smaller rank.

For \(r'=0\), no inner augmentation or positive-mass argument is
used: return the empty small basis and apply Section 2 to the full
\(U\)-basis. If \(r=1\), then \(\rho_r=0\) and every inner
phase has \(k=s=0\); (A1) rules out an empty search. The direct
maximum-liked-value scan is also valid. Rank zero of the original
matroid is handled before defining a minimum allocation value.

## 4. Positive-error parameters and all work

For \(0<\epsilon<\theta_r\), let
\(B=(\theta_r-\epsilon)T\), \(\gamma=\epsilon/4\), and
\(A=2B+u\). Then

\[
 A<3T,\qquad
 B+\rho_rA\le T-\epsilon T.
\]

If \(y\le\gamma w\), the upper cover bound is strictly less
than \((T-B)w\). Hence every passing completed layer has
\(y>\gamma w\). Within a phase \(r'-k\) is fixed, so
\(r'-k+|Y_{\le i}|\) grows geometrically and never exceeds
\(r'\). The depth is \(O(\epsilon^{-1}\log(r'+1))\).
The earlier-span preservation lemma keeps retained earlier growth
statements literally current; only the changed last layer is refreshed.

For a desired denominator \(d_r+\eta\), the main note chooses

\[
 \epsilon=1/d_r-1/(d_r+\eta),\qquad
 \epsilon^{-1}=d_r+d_r^2/\eta=O(1+\eta^{-1}).
\]

This gives exactly \(B=T/(d_r+\eta)\). The fat threshold remains
\(\theta_rT\), which is at least \(B\), so the reconstruction
has the claimed common value guarantee. The minimum of the
rank-exponential and quasipolynomial signature counts remains valid.
No restart, refresh or full-player scan is outside those counts.

## 5. The derived oracles and rank bound are fully paid

The union contains every independent set of \(M^*\), so
\(r(U)\ge q-r\) and \(r(U^*)\le r\). Oracle cost is not
rank-exponential: rank and independence in \(M^*\) follow by greedy
rank computations in \(M\) and the dual-rank identity. The
transversal matroid uses the explicit fat bipartite graph and
deterministic matching. Matroid union/partition is polynomial in the
ground-set size and the two oracle costs; it also returns the required
decomposition. A further application of dual rank implements \(U^*\).

All nested oracle calls therefore contribute a fixed polynomial in
the full explicit input, with an exponent independent of \(r\).
The source for the polynomial matroid-partition primitive is the
primary paper [Terao, ICALP 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.104).
No algorithmic improvement of that primitive is claimed here.

The wrapper correctly gives up the inner algorithm's linear input
factor. Computing ranks, decompositions, complement bases and fat
matchings is charged in \(\operatorname{poly}(P,b)\). Numerical
work only uses input-rational subset sums and fixed rational target
thresholds; no iteration-length denominator product arises.

## 6. Binary search does not require monotone success above OPT

Let \(\Delta=1/D\) be the common resource grid and \(a\) the
fixed-target output coefficient. Every integral allocation value and
\(\mathrm{OPT}\) lies on the grid. A failed target satisfies
\(T>\mathrm{OPT}\); a successful target returns an actual allocation
worth at least \(aT\), but may be larger than \(\mathrm{OPT}\).

Choose a grid upper target exceeding total resource value divided by
\(a\). Success is impossible there, since it would return more value
to even one selected player than all resources contain. Maintain the
largest target accepted along the binary-search path as the lower
endpoint, with its allocation, and a failed upper endpoint. Failure
soundness maintains \(\mathrm{upper}>\mathrm{OPT}\). At adjacent
grid points, the grid-valued optimum therefore satisfies
\(\mathrm{OPT}\le\mathrm{lower}\). The saved allocation has
value at least \(a\,\mathrm{lower}\ge a\,\mathrm{OPT}\).

This argument never assumes that success itself proves feasibility
at target \(T\), or that the answer predicate is monotone above
\(\mathrm{OPT}\). Polynomial grid-index bit length bounds the
number of trials. If the lower endpoint stays zero, the optimum is
zero and the initialized basis with empty allocations is sufficient.

## 7. Final scope

The exact \(4-3/r\) and positive-error \(4-3/r+\eta\) guarantees
are mathematically established for arbitrary player-matroid basis
selection relative to its integral optimum, with the stated rank and
oracle dependence. They do not round an arbitrary large-item feasible
point of the original compact relaxation. The strict improvement over
four vanishes with rank, so this is not a uniform constant-below-four
restricted-Santa-Claus result. The separate public comparison note
governs novelty and source-version claims; none is inferred merely from
this correctness audit.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
