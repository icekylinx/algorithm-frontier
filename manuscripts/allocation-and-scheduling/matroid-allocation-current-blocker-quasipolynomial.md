# Current blocker growth for matroid max-min allocation

**25 October 2026. New research construction; root review and two independent mathematical audits completed.**

The public comparison uses the precise versions and qualifications stated below.

## 1. Result and exact comparison target

Let a matroid on a ground set P of q players be given by an independence
oracle, and let its rank be r. Let J be a set of indivisible resources, with positive rational
values v_j and explicit liking sets L_p contained in J. A resource has
the same value to every player who likes it. Write

$$
u=\max_{j\in J}v_j,
 \qquad \mathcal P=q+|J|+\sum_p|L_p|+2.
$$

Zero-value resources may be removed. The case of rank zero is vacuous.
If the resource set is empty, take u=0 and use the same failure
certificate below whenever a positive target is requested.

The public fractional relaxation Q(T) has variables x_p and y_pj,
with x in the matroid base polytope, and

$$
\sum_{j\in L_p}v_jy_{pj}\ge T x_p,
 \qquad
 \sum_{p:j\in L_p}y_{pj}\le1,
 \qquad
 0\le y_{pj}\le x_p.
 \tag{M1}
$$

For T>u and rational

$$
0<\varepsilon<\frac{1-u/T}{3},
 \qquad
 B=\frac{T-u}{3}-\varepsilon T>0,
 \tag{M2}
$$

the deterministic algorithm described here returns either:

* a matroid basis of players with disjoint allocations, each of value
  at least B; or
* an explicit, oracle-checkable certificate that Q(T) is infeasible.

In particular, Q(T) nonempty guarantees the first outcome. A fractional
solution is not needed as an algorithmic input. With b denoting the
total bit length of the rational numerical input, the time and number
of independence-oracle calls are bounded by

$$
\boxed{
 \mathcal P\,\min\!\left\{2^{O(r)},
            (r+1)^{O(\varepsilon^{-1}\log(r+1))}\right\}
             \mathrm{poly}(b+\log\mathcal P).
 }
 \tag{M3}
$$

Polynomial factors in r are absorbed in the displayed exponent. The
time bound assumes unit-cost oracle calls; otherwise multiply their
number by the cost of an independence query. Space is polynomial in
the explicit input. The exponent depends on the numerical value of
epsilon; this is not a claim of polynomial dependence on its encoding
length or on 1/epsilon. The minimum is an analysis of the same
algorithm, not an assumption that a separate fallback is free.

One may also set epsilon to zero and obtain the exact additive
boundary B=(T-u)/3 in time and oracle calls

$$
\boxed{\mathcal P\,2^{O(r)}
                 \mathrm{poly}(b+\log\mathcal P).}
 \tag{M3a}
$$

This version uses the same operations and tests completed layers for
at least one blocker; it does not claim quasipolynomial time at the
exact boundary. In particular, this is fixed-parameter tractable in
the matroid rank for the exact additive guarantee, with polynomial
space and a linear explicit-input multiplier. The total number of
players can be much larger than the rank.

The guarantee is additive in the largest resource value. It is not an
unqualified one-third approximation for arbitrary resources. If B is
nonpositive, choosing any matroid basis and giving empty allocations
already satisfies that nonpositive lower bound, so the interesting
case is exactly (M2).

The comparison is with Davies--Rothvoss--Zhang, *A Tale of Santa Claus,
Hypergraphs and Matroids*, arXiv:1807.07189v4, Theorem 2:

<https://arxiv.org/html/1807.07189v4>.

That current public theorem gives
(1/5-epsilon)T-u/5 in polynomial time for fixed epsilon. Its Section 4
explicitly explains the correction of an earlier approximation claim:
layer growth at birth did not necessarily survive later collapses.
Our result changes the quality/time tradeoff to (M2)--(M3). It does
not improve the published polynomial-time theorem at the same runtime.
Earlier versions also contained one-third claims, with different
largest-item losses or integral-value assumptions. We do not claim
that the numerical coefficient one third was never previously proposed.
An algebraic reparameterization of the current public framework suggests
a stronger polynomial comparison curve, but its precise exchange
contract is still under review. We do not count that unclosed derivation
as either a proved competitor or a failure of the printed theorem.

The matroid allocation formulation, relaxation, and exchange framework
are public; the fully blocked current-layer construction and its
quasipolynomial analysis below are the research contribution here.

## 2. Stored objects and the individual eligibility rule

Maintain a matching M of resource bundles. Each bundle is inclusion
minimal subject to having value at least B, has a distinct owner p,
and is contained in L_p. Different bundles in M are resource-disjoint.
Their owner set I is independent in the matroid. Let k=|I|. Compute
the matroid rank r by the ordinary greedy oracle procedure. A phase
starts with k<r and seeks to increase k by one.

A layer i contains a set X_i of selected candidate bundles and a set
Y_i of current bundles in M that block them. The following invariants
are required whenever the algorithm is not inside the explicitly
described free-center cascade.

1. All selected bundles in all X_i are resource-disjoint. A selected
   owner may occur more than once. No joint matroid-independence claim
   is made for the selected owner sets.
2. The Y_i are disjoint subsets of the current matching M. Every
   bundle in Y_i intersects exactly one selected bundle, in X_i,
   and intersects no selected bundle of another layer.
3. Y_i contains all current M-blockers of X_i. Every selected bundle
   has at least one blocker. In particular |X_i|<=|Y_i|.
4. A selected bundle in layer i has an owner in

$$
U_i=P\setminus\mathrm{cl}\bigl(I\setminus
                 \mathrm{owners}(Y_{<i})\bigr).
 \tag{M4}
$$

Here closure is matroid closure and Y_<i is the union of the earlier
blocking sets. The criterion is individual eligibility of an owner.
It does not require several candidate owners to be simultaneously
exchangeable. The algorithm uses one free candidate at a time.

For a completed layer i, also require maximality: there is no
inclusion-minimal B-bundle belonging to a player in U_i that is
disjoint from all resources in

$$
F_i=R(X_{\le i}\cup Y_{\le i}).
 \tag{M5}
$$

R denotes the resource union. The proof below shows that an exchange
preserves this maximality in all lower layers that it retains.

## 3. Building or extending the last layer

Only the last current layer is built or extended. Given its already
stored X_i,Y_i and the lower prefix, search for a player p in U_i
whose available liked resources outside F_i have total value at least B.
If no such player exists, the layer is maximal.

Otherwise form an inclusion-minimal B-bundle C from those available
resources. One deterministic procedure takes resources in fixed ID
order until the threshold is reached, then deletes a resource whenever
the remainder still has value at least B. One deletion scan suffices:
a resource that cannot be deleted cannot become deletable after the
total value decreases further.

If C has a current M-blocker, add C to X_i and all its blockers to Y_i.
All newly found blockers are outside Y_<=i, since C avoids F_i. A new
blocker cannot intersect an old selected bundle: it would already have
been that bundle's current blocker and hence belonged to the forbidden
Y prefix. Thus blocker ownership remains unique, and the extended
selected set remains resource-disjoint.

If C has no current M-blocker, process it by the free-candidate rule in
Section 4. It need not be stored as a new X member first. Each blocked
addition discovers at least one previously undiscovered M edge, so
there are at most k such additions before the next exchange or phase
completion. No implicit family of bundles is enumerated.

## 4. A free candidate and the earliest circuit exchange

Suppose a free candidate C with owner p is found in layer i. This
includes an already stored selected bundle that became free when its
last blocker was removed.

If p is outside cl(I), add C to M. The owner set grows independently,
and the phase succeeds. Discard all layers and begin the next phase,
or return the allocation if the owner set is now a basis.

Otherwise p is in cl(I). There are two cases.

* If p is already in I, eligibility (M4) forces its current M bundle
  to belong to Y_<i. Let y be that bundle, and j its layer. Replace
  y by C. The independent owner set I itself does not change.
* If p is not in I, let C_mat be its unique fundamental circuit in
  I union {p}. Eligibility implies that C_mat intersects the owners
  of Y_<i. Let j be the earliest such layer and choose a bundle y in
  Y_j whose owner belongs to C_mat. Replace y by C in M and replace
  its owner by p in I.

In either case j<i. Delete y from Y_j, discard every layer above j,
and retain X_j. The new M edge is free of the retained selected
resources: a newly built candidate avoided them, while an old selected
candidate was resource-disjoint from every other selected bundle.
It introduces no new blocker of a retained selected bundle.

Only the selected bundle that owned blocker y can have become newly
free. If it has lost its last blocker, process that free selected
bundle immediately by the same rule. A nonaugmenting step in this
cascade moves to a strictly earlier layer. The cascade therefore has
at most the old number of layers before it augments or leaves all
retained selected bundles blocked.

Then resume the greedy extension of the last surviving layer. This
refresh occurs before another layer is appended or a maximality-based
growth test is applied.

### 4.1 Why lower eligibility survives

Consider the case p not in I. For every h<=j, the fundamental circuit
contains no owner from Y_<h, by the earliest-layer choice. It is
therefore a circuit in

$$
(I\setminus\mathrm{owners}(Y_{<h}))\cup\{p\}.
$$

The independent set inside parentheses contains owner(y). Replacing
owner(y) by p is a basis exchange inside its span. Consequently

$$
\mathrm{cl}(I'\setminus\mathrm{owners}(Y'_{<h}))
 =\mathrm{cl}(I\setminus\mathrm{owners}(Y_{<h}))
 \quad (h\le j).
 \tag{M6}
$$

The earlier blocking sets are unchanged. In the case p in I, the
independent owner set is unchanged and (M6) is immediate.

Thus every retained selected owner remains eligible. This is the
reason for choosing the earliest circuit layer rather than an
arbitrary exchangeable blocker.

### 4.2 Why lower maximality survives

For h<j, both the eligibility set U_h and the resource set F_h are
unchanged. The new M edge avoids all retained selected resources, so
it cannot change their blocker identities. Hence the old statement
that no eligible bundle avoids F_h remains literally true.

At layer j, y has disappeared from F_j; this can create additional
available bundles. That layer is exactly the one refreshed next.
All higher layers are discarded. No argument relies on a layer being
maximal only at its birth, or on a stale candidate set remaining
representative after a swap.

## 5. The current-prefix resource bound

Let i be a completed maximal layer. Put

$$
a=|X_{\le i}|,\quad t=|Y_{\le i}|,
 \quad w=1+|Y_{<i}|.
$$

Each selected bundle has value less than B+u. A matching blocker
intersects its unique selected owner. Removing one resource in that
intersection leaves a proper subset of an inclusion-minimal B-bundle,
so the blocker's resources outside its selected owner have value
strictly less than B. Summing over the resource-disjoint selected
bundles and matching bundles gives

$$
v(F_i)<(B+u)a+Bt\le(2B+u)t,
 \tag{M7}
$$

when t>0. If t=0, F_i is empty and its value is zero. The inequality
a<=t uses current nonempty blocker sets, not their historical sizes.

This proof also applies when several selected bundles have the same
player label. Their resource disjointness, and the unique current
blocker ownership, are the properties used in (M7).

## 6. A fractional rank bound forces current blocker growth

Assume for this paragraph that (M1) has a feasible solution. The set
I minus owners(Y_<i) is independent of size k-|Y_<i|. Its closure is
a flat of that rank. Since x is in the base polytope,

$$
x(U_i)\ge r-k+|Y_{<i}|\ge 1+|Y_{<i}|=w.
 \tag{M8}
$$

Maximality of layer i says that for every p in U_i,

$$
v(L_p\setminus F_i)<B.
 \tag{M9}
$$

Otherwise those available resources contain a minimal B-bundle. The
constraints y_pj<=x_p then imply that the fractional value assigned to
p from outside F_i is less than B x_p whenever x_p>0. Summing the
remaining required value over U_i and using the unit resource capacities
gives

$$
v(F_i)\ge (T-B)x(U_i)\ge(T-B)w.
 \tag{M10}
$$

The weak inequality is sufficient; one can obtain a strict inequality
because x(U_i)>0. We do not need that refinement.

Write A=2B+u. By (M2), A<T and

$$
(T-B)-A=3\varepsilon T.
$$

If |Y_i|<=epsilon w, then

$$
t=w-1+|Y_i|\le(1+\varepsilon)w-1,
$$

and (M7) gives

$$
v(F_i)\le A((1+\varepsilon)w-1)<(T-B)w.
 \tag{M11}
$$

Indeed the difference of the coefficients on w is
3epsilon T-epsilon A>2epsilon T. This contradicts (M10).
Therefore every completed layer in a feasible instance has

$$
\boxed{|Y_i|>\varepsilon(1+|Y_{<i}|).}
 \tag{M12}
$$

This is a statement about the current matching blockers after all
earlier exchanges and the required last-layer refresh.

### 6.1 An explicit infeasibility output

The algorithm does not assume access to x,y. At a maximal layer that
fails (M12), return its independent set
J_0=I minus owners(Y_<i), its closure flat, and the explicit resource
set F_i. Verify (M9) for every player outside that flat and verify

$$
v(F_i)<(T-B)(r-|J_0|).
 \tag{M13}
$$

The calculation above guarantees (M13), including the empty-layer
case. These two facts contradict (M1) by the same rank and capacity
argument. Thus failure is a valid fractional-infeasibility certificate,
not merely a statement that the local search ran out of moves.

## 7. A bounded integer signature gives quasipolynomial termination

Whenever a maximal layer passes (M12), append a new empty last layer
and start building it. Since the blocking sets are disjoint subsets of
M, (M12) implies

$$
1+|Y_{\le i}|>(1+\varepsilon)(1+|Y_{<i}|).
$$

Thus the number of completed layers is at most

$$
L=\left\lceil\frac{\log(r+1)}{\log(1+\varepsilon)}\right\rceil
   =O(\varepsilon^{-1}\log(r+1)).
 \tag{M14}
$$

During construction there is at most one additional unfinished last
layer. A collapse or a refresh never increases the number of layers.
An exchange cannot invalidate growth in a lower retained layer,
because its blocker sets there are unchanged; the last surviving
layer is checked again after its refresh.

For the current stack use the integer signature

$$
(-|X_1|,|Y_1|,\ldots,-|X_\ell|,|Y_\ell|,\infty).
 \tag{M15}
$$

Every nonterminal change strictly decreases this vector in ordinary
lexicographic order:

* appending an empty layer replaces the sentinel by 0,0,sentinel;
* adding a blocked candidate increases the first selected count in
  the last layer, hence decreases its negative coordinate, before
  any increase of the corresponding blocker coordinate matters;
* a nonaugmenting free exchange first changes layer j by deleting
  one blocker while keeping X_j unchanged, then discards all higher
  layers. Its first changed coordinate therefore decreases.

The same reasoning applies to every step in a free-center cascade.
Merely scanning for a candidate is not a state change: a complete scan
either finds a candidate, finishes a layer, or returns a certificate.
There is no uncharged sequence of failed trial updates.

All selected and blocker counts are at most r. Just after a removal,
one selected center can be free, but its count has not increased; the
same r bound holds until the cascade is processed. Together with the
temporary length bound L+1, the number of signatures is at most

$$
(2r+3)^{2L+3}
  =(r+1)^{O(\varepsilon^{-1}\log(r+1))}.
 \tag{M16}
$$

No signature repeats. There are at most r successful augmentation
phases. This proves the quasipolynomial part of the bound. It does
not invoke the obsolete birth-growth assumption identified in the
revised public matroid allocation paper.

### 7.1 A second count for the same signatures

At every microstate, including a free-center cascade,

$$
\sum_i|X_i|\le k<r,\qquad \sum_i|Y_i|\le k<r.
 \tag{M17}
$$

Before a free exchange all stored centers are blocked. A newly found
free candidate is not stored in X. Every step of a subsequent cascade
only removes blockers or truncates selected sets. A new blocked
addition is permitted only after the cascade has restored the fully
blocked invariant. This proves the selected-count bound even in
transient states. The blocker-count bound is immediate from Y being
disjoint subsets of the size-k matching.

Every non-last layer has a positive blocker count, and only the last
may be unfinished or have just lost its last blocker. Hence the stack
length is at most k+1, at most r. For fixed length ell, the number
of nonnegative count lists with total at most r is
binomial(r+ell,ell). Counting the two lists independently gives at most

$$
\sum_{\ell=0}^{r}\binom{r+\ell}{\ell}^2
       \le(r+1)2^{4r}=2^{O(r)}
 \tag{M18}
$$

possible signatures. This overcounts many impossible states, which
is harmless. Multiplying by r phases and polynomial work per event
preserves the exponential bound and proves the minimum in (M3).

### 7.2 Exact additive guarantee when epsilon is zero

Set B=(T-u)/3>0 and replace (M12) by the test |Y_i|>0. All exchange
and freshness invariants are unchanged. Now A=2B+u=T-B. If a completed
maximal layer has Y_i empty, then t=w-1, and (M7), including its empty
case, gives

$$
v(F_i)\le A(w-1)<Aw\le(T-B)(r-|J_0|).
 \tag{M19}
$$

This is the same explicit failure certificate. Every passing layer
has at least one blocker, so the composition count (M18) still applies.
This proves (M3a). The positive-epsilon logarithmic-depth estimate is
not used. No limiting argument, infinitesimal perturbation or supplied
fractional solution is required.

## 8. Explicit implementation and finite arithmetic

An independence test determines whether a player belongs to U_i:
compare the independent set I minus owners(Y_<i) with that set plus p,
handling membership of p itself in the set explicitly. A scan over
players and their explicit liking lists tests (M9), finds an available
bundle when one exists, and constructs it by the threshold-and-prune
procedure. No configuration LP and no exponential bundle graph is
constructed.

Resource-owner maps for M identify all blockers of a new bundle.
Each stored matching blocker has one selected-owner pointer. A free
exchange identifies whether that selected owner has become free.
When p is outside I but in its span, the fundamental circuit can be
found by testing I minus {a} plus {p} for each a in I. Select an
exchangeable blocker with the earliest layer index.

The input resources, liking lists, all matching bundles, and all
selected bundles can be stored explicitly. M has at most r bundles,
and the selected bundles are pairwise resource-disjoint, with at most
r of them, including every transient free cascade. An eligibility
scan uses q independence queries on sets of size at most r+1;
constructing those query sets costs O(qr), not O(q squared).
Scanning liking lists, rebuilding resource marks, and finding the
blockers of a selected bundle cost a fixed polynomial in r times
the explicit input size. A fundamental circuit uses at most r oracle
queries. Initially the rank itself is computed using q greedy
independence queries. These costs give the linear multiplier P in
(M3) with all remaining combinatorial polynomial factors absorbed
in the displayed rank exponent. No enumeration of pairs of players
or delicate dynamic matroid data structure is required.

The algorithm compares rational sums and performs no numerical
perturbation of resource values. Sums of subsets of the input values,
and the fixed rational thresholds T,B,epsilon, have polynomial bit
complexity in their total input encoding. The logarithms in (M14)--
(M16) are proof quantities only. The algorithm stores integer counts
and tests (M12) by exact rational comparison.

## 9. What the result does and does not imply for Santa Claus

The public large-resource matching/co-matroid reduction is checked
in Section 8 of the independent audit. For completeness, let the
large-resource threshold be theta T and let N be the transversal
matroid of players matchable to one large resource. In the public
compact relaxation, the fractional large-resource assignment has
player marginal a, and the small assignments z satisfy

$$
v(z_p)\ge T(1-a_p),\qquad z_{pj}\le1-a_p,
 \qquad\sum_pz_{pj}\le1.
$$

Extend a coordinatewise to a base vector a' of N. Scale each player's
small assignments by (1-a'_p)/(1-a_p), treating a_p=1 separately as
zero. Resource capacities only decrease, and x=1-a' is a base vector
of the dual matroid. Thus these scaled variables satisfy (M1) for
that dual matroid and small resources of maximum value u<=theta T.
The new algorithm allocates small resources to a dual basis, and its
complement can be matched to distinct large resources. The guaranteed
value per player is therefore

$$
\min\{\theta,(1-\theta)/3-\varepsilon\}T.
$$

Choosing theta=(1-3epsilon)/4 gives (1-3epsilon)T/4. The compact LP
may be supplied or solved in polynomial time. This proves a
quasipolynomial 4/(1-3epsilon) guarantee against that relaxation.
The exact-boundary exponential algorithm similarly permits theta=1/4.

It does not break the factor-four barrier for the unrestricted
restricted-Santa-Claus allocation problem. Cheng--Mao already provide
a polynomial (4+delta) algorithm against the configuration LP. Nor
does the theorem algorithmize the 53/15 topological integrality-gap
bound. The present concrete gain is the general matroid allocation
quality/time tradeoff in (M2)--(M3), with a complete current-blocker
invariant and an explicit failure certificate.
