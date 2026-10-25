# Verification note

**Curated source path:** `sources/checkpoint-o/matroid_sharp_star_and_union_independent_audit.md`

The source audit follows.

# Independent audit: sharp stars and the fat-resource matroid union

**25 October 2026.** This is an independent first audit of
`matroid_allocation_sharp_star_rank_quality.md` and
`matroid_union_fat_resource_allocation.md`, read in full. It uses the
already audited exchange and implementation interface in
`matroid_allocation_current_blocker_independent_audit.md`.

**Verdict:** both refinements pass. The sharp-star theorem applies to
the compact player-basis relaxation. The union reduction applies to
the integral optimum with arbitrary resource values. These are
different comparators. The resulting ratio `4-3/r` is a finite-rank
improvement and tends to four; it is not a constant improvement below
four for unbounded rank.

## 1. The current-star coefficient is valid

Let every selected and matching bundle be inclusion minimal above a
positive target `B`. The existing layer invariant assigns each
matching blocker to exactly one selected center, and every retained
center is blocked outside the explicitly processed free cascade.
Write `u` for the largest resource value and

\[
 C(B,u)=\max\{u,\;2B+\min(u,B)\}.
\]

For a singleton center `{e}`, the condition `v_e>=B` forces any
minimal blocker containing `e` to be the same singleton. Resource
disjointness in the matching permits only one such blocker. The
complete star has value at most `u`.

For a nonsingleton center `A`, every item has value below `B` and
minimality gives `v(A)<B+min(u,B)`. If a blocker intersects `A`,
its resources outside `A` form a proper subset and have total value
below `B`. A center with `t>=1` blockers therefore has star value

\[
 v(A\cup R(Y_A))<B+\min(u,B)+tB
                  \le t[2B+\min(u,B)].
\]

Summing the stars gives `v(F)<=C(B,u)|Y|`. In particular, when
`u>=B`, the coefficient is `max(u,3B)`, not `2B+u`.
Repeated player names do not affect this resource argument. There is
no need to assume that distinct centers have different owners.

## 2. Strict LP separation permits an equality certificate

For a completed maximal layer, put

\[
 J_0=I\setminus\operatorname{owners}(Y_{<i}),\quad
 U=P_{\rm players}\setminus\operatorname{cl}(J_0),\quad
 w=r-|J_0|.
\]

The current matching has size `k<r`, so `w>=1`. The base-polytope
inequality gives `x(U)>=w` in every feasible `Q(T)` point. Maximality
means that each eligible player's total liked value outside the
forbidden resource union `F` is strictly below `B`. The individual
constraint `y_pj<=x_p` then gives strictly less than `B x_p` value
outside `F` for every eligible player with positive `x_p`.

The sum is strict because `x(U)>0` and the ground set is finite.
Resource capacities bound the value supplied from `F` by `v(F)`.
For `B<=T` this proves

\[
                       v(F)>(T-B)x(U)\ge(T-B)w.
\]

Thus an independent `J_0`, a resource set `F`, and the checks

\[
 v(L_p\setminus F)<B\quad(p\notin\operatorname{cl}(J_0)),
 \qquad v(F)\le(T-B)(r-|J_0|),
\]

with positive remaining rank give a sound infeasibility certificate.
The weak upper inequality is sufficient. This also handles `B=T`;
the strict fractional lower bound then says `v(F)>0`.

This uses exactly the relaxation in
[DRZ v4, equation (1)](https://arxiv.org/html/1807.07189v4), including
the individual upper bound `y_pj<=x_p`.

## 3. Rank-sensitive thresholds and running times

Let `s=|Y_<i|`. Since `s<=k<r`,

\[
 \frac{s}{r-k+s}\le\rho_r:=\frac{r-1}{r}.
\]

When a maximal new layer has no blockers, the star bound and the
strict LP lower bound contradict feasibility whenever

\[
                         B+\rho_r C(B,u)\le T.
\]

Consequently the integer growth test `|Y_i|>0` is enough. The
existing signature and composition count apply without modification:
all stored selected centers are blocked, their total is at most `k`,
all blocker coordinates also sum to at most `k`, and an unblocked
candidate is processed without being added to that signature. The
work remains

\[
 \mathcal P\,2^{O(r)}\operatorname{poly}(b+\log\mathcal P).
\]

The equality equation is continuous and strictly increasing in `B`.
For `r>=2`, a positive solution exists exactly for `u<T/rho_r`.
Solving on the three branches gives, with `d_r=4-3/r`,

\[
 B_r^*(T,u)=
 \begin{cases}
 (T-\rho_r u)/(1+2\rho_r),&u\le T/d_r,\\
 T/d_r,&T/d_r\le u\le3T/d_r,\\
 T-\rho_r u,&3T/d_r\le u<T/\rho_r.
 \end{cases}
\]

The transition conditions agree exactly with the conditions selecting
the corresponding branch of `C`. Rank one is solved directly and
has target `T`; rank zero is vacuous.

For `B=B_r^*-epsilon T>0`, monotonicity gives
`B+rho_r C(B,u)<=T-epsilon T`. In its positive domain,
`u<T/rho_r<=2T`, so `C(B,u)<=3T`. If a layer has at most
`(epsilon/4)(r-k+s)` new blockers, its cover value is strictly below
the required fractional value. Every passing completed layer grows
`r-k+|Y_<=i|` by more than a factor `1+epsilon/4`, giving depth
`O(epsilon^-1 log(r+1))`. The unchanged signature yields the
minimum of the rank-exponential and rank-quasipolynomial bounds.

The note's endpoint example is a genuine obstruction for this LP:
`r` mandatory players and only `r-1` shared items of value
`rT/(r-1)` satisfy `Q(T)` by equal splitting but have zero integral
minimum. Its local-star examples have a more limited purpose: they
bound this resource certificate, not all algorithms. The note
correctly does not claim its displayed warm state is necessarily
reached by the prescribed scan from an empty matching.

## 4. Matroid union establishes the required small-instance promise

For the unrestricted-value problem, let `M` have rank `r` on the
player ground set. At a target `T`, classify items of value at least
`theta T` as fat, and let `N` be the transversal matroid of players
that can receive distinct liked fat items. Define

\[
                         U=M^*\vee N.
\]

Since every independent set of `M*` is union independent,
`rank(U)>=q-r`, hence `rank(U*)<=r`.

Suppose an original `M` basis `I` has disjoint allocations worth at
least `T`. Its complement `D` is an `M*` basis. Let `F` consist of
the players in `I` whose original allocation contains a fat item.
Those items give a matching for `F`, and `D` and `F` are disjoint.
Thus `D union F` is independent in `U`. Extend it to a union basis
`B`. The complement `S'=P_players minus B` is a `U*` basis contained
in `I minus F`. Every player in `S'` retains an all-small allocation
of value at least `T`.

This is an integral witness to `Q_U*(T)`, which is stronger than the
fractional promise the inner theorem needs. It proves the crucial
one-sided failure implication

\[
 Q_{U^*}(T)=\varnothing\quad\Longrightarrow\quad\mathrm{OPT}<T.
\]

It does not say that an arbitrary feasible original `Q_M(T)` point
at unrestricted item sizes induces this promise. No such implication
is used.

## 5. Recovery does not require preserving every small player

Let the inner algorithm return a `U*` basis `S''`, with small bundles.
Its complement has a disjoint union decomposition

\[
 P_{\rm players}\setminus S''=D''\mathbin{\dot\cup}F'',
 \qquad D''\in\mathcal I(M^*),\quad F''\in\mathcal I(N).
\]

Match `F''` to fat items. Extend `D''` to any full `M*` basis
`D'''`, allowing this extension to discard some players in either
`F''` or `S''`. The complement of `D'''` is an original `M` basis
contained in `F'' union S''`. Every retained player already has an
allocation. Discarding other allocations cannot create collisions
or lower a retained player's value. Fat and small resources are
disjoint by their definition.

Requiring the extension to avoid every small player would be an
unnecessary extra condition; the main proof correctly allows their
removal.

## 6. The factor and the costs of the derived oracles

Set `theta=1/(4-3/r)` and first take the exact target `B=theta T`.
The largest small item satisfies `u<B`. In the auxiliary matroid of
rank `r'<=r`,

\[
 B+\rho_{r'}(2B+u)\le B+3\rho_r B=T.
\]

The exact rank-exponential solver therefore provides the required
small allocations. Fat items also have value at least `B`. This
proves ratio `4-3/r` against the integral optimum, once the target
selection in Section 7 is applied.

For any positive `eta`, take

\[
 \epsilon=\frac1{d_r}-\frac1{d_r+\eta}
          =\frac{\eta}{d_r(d_r+\eta)}.
\]

Then `B=T/(d_r+eta)` and
`epsilon^-1=d_r+d_r^2/eta=O(1+eta^-1)`. The fat threshold remains
`T/d_r`, so a fat item is still sufficient. The numerical depth test
in the union note has the same positive-slack proof as Section 3.

All dual ranks are computable using the original independence oracle.
Union ranks and decompositions require polynomial matroid partition
work, and transversal tests require polynomial bipartite matching
work. A primary source for the partition interface is
[Terao, ICALP 2023](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.104).
Substituting these implementations multiplies the inner bound by a
fixed polynomial in full input size. It does not put `q` in the
rank exponential, but it does lose the inner theorem's linear input
multiplier. The main note states this distinction explicitly.

When there are no small resources, take `u=0` by convention. If
`r'=0`, no inner allocation is needed; if `r'>0`, a positive target
has the direct empty-resource infeasibility certificate. This is a
minor boundary convention rather than an additional algorithmic
condition.

## 7. Grid search is sound without monotone success above OPT

Let `Delta=1/D`, with `D` the product or least common multiple of
the positive input denominators. Its bit length is bounded by the
total input encoding. Every bundle value and therefore `OPT` lie on
this grid.

At a target `T`, success gives an allocation worth at least `aT`;
failure gives `OPT<T`. Above `OPT`, either outcome may occur. This
does not prevent the stated search. Maintain a successful lower
grid point and a failed upper grid point. The latter is always
strictly above `OPT`. At termination the two are adjacent, so the
grid-valued `OPT` is at most the lower point. The saved successful
allocation is therefore worth at least `a OPT`.

A starting upper point greater than `V/a`, where `V` is the total
resource value, cannot succeed for a positive-rank basis. Zero is a
valid lower point with any basis and empty bundles. All queried
targets, derived thresholds and the number of binary-search trials
have polynomial encoding length. The rank-zero and zero-optimum
conventions in the main note are consistent with these statements.

## 8. Public comparison and the precise advance

[DRZ v4, Theorem 2](https://arxiv.org/html/1807.07189v4) displays the
polynomial guarantee `(T-u)/5-epsilon T` for the same player-basis
LP. Composing that displayed theorem with the union reduction gives
a polynomial `6+eta` guarantee for the general player-basis
integral-optimum problem: classify fat items at `T/6` and choose
`epsilon=1/6-1/(6+eta)`. This is a derived consequence, not a claim
that the paper explicitly states the general union wrapper.

For a promise algorithm one may enforce its displayed polynomial
time bound and validate its returned allocation; a timeout or invalid
result means the LP-feasibility promise did not hold. Thus its
one-sided target test can be used in the same grid-search argument
without importing the new explicit certificate. This comparison
remains conditional on the displayed public theorem, whose separate
literal-pseudocode interface question is documented in
`public_matroid_repeated_owner_interface_gap.md`.

The old DRZ v2 one-third theorem would likewise imply `4+eta` by the
same union wrapper. It belongs in the historical comparison, and its
later revision prevents treating it as an additional independently
closed current proof. Ordinary all-player Santa Claus already has a
polynomial `4+eta` algorithm, while ordinary fixed-player
approximation schemes use a different parameter and do not supply a
rank-only factor when the number of eligible players is much larger.
These distinctions are recorded in
`matroid_allocation_public_comparison_and_version_audit.md`.

The present audited result is a rank-sensitive construction and
certificate, plus its explicit general-player-matroid reduction. It
does not change the accepted general-graph maximum-matching exponent.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
