# Second independent audit of current-blocker matroid allocation

**25 October 2026. Full mathematical and implementation audit passed.**

This audit checks
`matroid_allocation_current_blocker_quasipolynomial.md` in its
last-layer-refresh form, including the explicit existing-free-center
cascade and same-player exchange case. The result is the additive
largest-item guarantee

\[
                         B=(T-u)/3-\varepsilon T>0
\]

with quasipolynomial dependence on the matroid rank \(r\), or
\(2^{O(r)}\) dependence even at \(\varepsilon=0\). The ground set
may have \(q\) players with \(q\) much larger than \(r\); its size
enters the explicit-input factor \(\mathcal P\). It is not an
unqualified one-third approximation for arbitrary item sizes, and it does
not improve the public polynomial-time result at its runtime.

The comparison model and relaxation were checked against the primary
source [Davies--Rothvoss--Zhang, arXiv:1807.07189v4, Theorem 2 and
equation (1)](https://arxiv.org/html/1807.07189v4). Its current guarantee
has coefficient one fifth and the same additive largest-resource term.
The arguments below independently audit the proposed new construction;
they do not import the revised public paper's old layer-growth premise.

## 1. One free object is exchangeable; a whole selected set need not be

Let the current owner set \(I\) be independent. A candidate in layer
\(i\), with player \(p\), is eligible precisely when

\[
              p\notin\operatorname{cl}(I\setminus Y_{<i}),       \tag{A1}
\]

where a blocking set in a matroid expression denotes its owner set.
Selected bundles can repeat a player. There is no assertion that all
selected owners form an independent set or can be exchanged together.
The procedure only processes one free candidate at a time, which is
enough for the following exact matroid argument.

If \(p\notin\operatorname{cl}(I)\), augmentation is legitimate. If
\(p\in I\), then (A1) forces its matching bundle to lie in \(Y_{<i}\).
Replacing that particular bundle leaves the owner set unchanged. This
case is necessary: a fundamental circuit for a duplicate ground-set
element is not an ordinary circuit in the original matroid.

In the remaining case, \(p\notin I\) but \(p\in\operatorname{cl}(I)\).
Its unique fundamental circuit \(C\subseteq I\cup\{p\}\) meets
\(Y_{<i}\), because otherwise (A1) would fail. Let \(j\) be its earliest
blocking layer and choose \(y\in C\cap Y_j\). For every \(h\le j\),
the circuit is contained in

\[
                (I\setminus Y_{<h})\cup\{p\}.
\]

It follows that

\[
 \operatorname{cl}((I\setminus Y_{<h})-y+p)
       =\operatorname{cl}(I\setminus Y_{<h}).                    \tag{A2}
\]

For completeness, the circuit places \(p\) in the old span and places
\(y\) in the span of the exchanged set. Both independent sets have
the same size, so the two inclusions of spans give equality. None of
the earlier blocker sets \(Y_{<h}\) contains the removed \(y\).
This proves the main note's closure identity for every retained layer.

A useful same-player check is automatic. The inserted player \(p\)
belonged to \(\operatorname{cl}(I\setminus Y_{<h})\) for every
\(h\le j\), since the complete fundamental circuit lies there.
Consequently no retained selected object could already have this
player while satisfying its eligibility rule. This prevents a hidden
loss of eligibility caused by adding a player that appeared in the
retained selected prefix.

## 2. Resource blockers and the free cascade remain exact

All selected bundles are pairwise resource-disjoint, including those
with the same player. A newly generated candidate avoids the complete
selected and blocker prefix of its layer. If it has a matching blocker,
that blocker is new to the retained prefix. Otherwise it would already
belong to the forbidden resource set. The new blocker cannot also hit
an old selected bundle: exact blocker inventories would have recorded
it there earlier. Thus a new blocked center receives a nonempty,
previously unused set of matching blockers.

A newly generated free candidate avoids every selected bundle that
survives its exchange. An existing selected candidate that became free
is disjoint from every other selected object; the layer containing it
is discarded because the exchange takes place strictly earlier.
Either type can therefore enter \(M\) without creating any new blocker
of a retained selected center.

Removing the chosen matching bundle \(y\) deletes exactly one current
blocker record. Only its unique selected owner can become newly free.
If it does, that **existing** object is processed immediately. Searching
only for new available bundles would miss this case; the main note now
includes the required owner pointer and cascade.

By (A2), this newly free center remains eligible at its old layer.
A nonaugmenting exchange for it touches an even earlier blocking layer.
The cascade consequently has strictly decreasing layer indices. It
cannot make an unbounded sequence of free swaps at one layer, and it
ends in augmentation or in a fully blocked retained prefix.

## 3. Earlier maximality is unchanged as a statement, not re-assumed

Consider a nonaugmenting exchange at layer \(j\). For \(h<j\):

* the eligible player set \(U_h\) is exactly the same by (A2);
* \(X_{\le h}\) and \(Y_{\le h}\) are exactly the same records;
* the inserted matching bundle is disjoint from all those selected
  resources and hence creates no new blocker there.

Therefore the resource union \(F_h\) is unchanged as well. The previous
maximality statement

\[
             v(L_p\setminus F_h)<B\quad(p\in U_h)
\]

is literally the same collection of inequalities after the exchange.
It is independent of any unrecorded adjacency to the new matching.

At \(j\), removing \(y\) can remove resources from \(F_j\), so that
one layer genuinely needs new work. The construction truncates all
higher layers and refreshes this last surviving layer before applying
growth again. If the free cascade continues, the same reasoning applies
at its earlier target. This handles both the eligibility and resource
parts of freshness and avoids the public paper's obsolete birth-growth
assumption.

## 4. Current cover value and the compact fractional relaxation

Every selected or matching bundle is inclusion-minimal for target \(B\).
With \(u\) the largest resource value, any selected bundle has value
less than \(B+u\). A matching blocker intersects its unique selected
owner. Deleting one intersecting resource leaves a proper subset of a
minimal bundle, so the value of the blocker outside its owner is less
than \(B\). Thus at a completed layer

\[
 v(F_i)<(B+u)|X_{\le i}|+B|Y_{\le i}|
                  \le(2B+u)|Y_{\le i}|.                        \tag{A3}
\]

The count \(|X_{\le i}|\le|Y_{\le i}|\) uses the **current** fully
blocked state. Resource disjointness and unique blocker ownership
justify the union bound. Repeated selected player labels do not enter
this calculation.

Let the matroid rank be \(r\), let \(k=|I|<r\), and put
\(w=1+|Y_{<i}|\). The flat
\(\operatorname{cl}(I\setminus Y_{<i})\) has rank
\(k-|Y_{<i}|\). For the compact fractional base vector,

\[
                         x(U_i)\ge r-k+|Y_{<i}|\ge w.           \tag{A4}
\]

Maximality says that the entire set of liked resources outside \(F_i\)
has value below \(B\) for each player in \(U_i\). The compact LP's
individual inequalities \(y_{pe}\le x_p\) are essential here: they
bound that player's outside contribution by \(Bx_p\). Resource
capacities then give

\[
                            v(F_i)\ge(T-B)x(U_i).                \tag{A5}
\]

This is a proof for the stated compact relaxation. It does not assume a
configuration-LP representation of the fractional vector.

For the declared \(B=(T-u)/3-\varepsilon T>0\), put \(A=2B+u\).
Then \(A<T\) and \((T-B)-A=3\varepsilon T\). If
\(|Y_i|\le\varepsilon w\), (A3) is at most
\(A((1+\varepsilon)w-1)\), strictly below \((T-B)w\). This
contradicts (A4)--(A5). The main note's current growth bound follows.

The same arithmetic works as an explicit failure certificate without
knowing a fractional solution. An independent set \(J_0\), its computed
closure, and a resource set \(F\) with

\[
 v(L_p\setminus F)<B\quad(p\notin\operatorname{cl}(J_0)),
 \qquad v(F)<(T-B)(r-|J_0|)
\]

contradict the compact LP. These statements can be checked using the
independence oracle, resource lists and rational arithmetic.

## 5. The signature pays for the entire algorithm, including repairs

Every completed layer that is retained for further growth satisfies

\[
       1+|Y_{\le i}|>(1+\varepsilon)(1+|Y_{<i}|).
\]

The blocking sets are disjoint subsets of the current \(M\), so there
are \(O(\varepsilon^{-1}\log(r+1))\) completed layers. At most one
additional last layer is being built or refreshed. A free exchange
cannot invalidate growth in any earlier retained layer: its relevant
blocking sets are unchanged. The new last layer is tested again after
refresh, rather than inheriting an old test.

The micro-signature is

\[
             (-|X_1|,|Y_1|,\ldots,-|X_\ell|,|Y_\ell|,\infty).
\]

Appending an empty layer decreases the old sentinel. Adding a blocked
center decreases its negative selected coordinate before the blocker
increase is examined. A nonaugmenting exchange keeps \(X_j\), decreases
\(|Y_j|\), and truncates only later coordinates. Each member of a free
cascade has the same strict descent. These statements apply to the
actual intermediate states, not merely to an amortized summary after
a long sequence of repairs.

All counts are at most \(r\). Even immediately after a deletion, when
one selected center may be free, the selected count has not increased.
A full scan of the available players either finds a candidate, completes
the current layer, or returns the failure certificate. A completed layer
is immediately followed by failure or an append. There is no possible
sequence of repeated full scans without a charged state change.

This validates the finite signature count and the asserted total
quasipolynomial work. In particular, refreshing the last layer can add
many blocked centers, but **each** such addition is itself a strict
signature decrease. Free cascades and their oracle work are also counted.

## 6. The implicit and numerical costs are polynomial per state change

The independence oracle checks each player's membership in the eligible
set. A resource scan then either produces a threshold bundle and prunes
it to minimality, or verifies maximality. A current resource-owner table
identifies its matching blockers. Fundamental circuits are found by at
most \(r\) independence tests of the sets \(I-y+p\). No enumeration of
all minimal bundles and no arbitrary-neighbour oracle are required.

All resource values remain fixed. Numerical quantities are subset sums
of the input rationals and the fixed thresholds. Their common-denominator
bit length is polynomial in the total input encoding; denominators do not
multiply with the number of iterations.

The claimed polynomial space bound is also valid even for very small
\(\varepsilon\). The analytic depth bound may be large, but every
completed layer has at least one distinct matching blocker, so actual
depth is at most \(r\), including the temporary last layer. Matching bundles
are disjoint, selected bundles are disjoint, and neither collection has
more than \(r\) objects. No array of size exponential in the encoding
of \(\varepsilon\) is required.

## 7. An exponential count and the exact additive boundary

### 7.1 The same algorithm has at most exponentially many signatures

The main theorem's quasipolynomial bound is already justified. The
same integer signature gives the following parameter-independent bound.
At every microstate in an augmentation phase,

\[
                \sum_i|X_i|\le k<r,
                \qquad\sum_i|Y_i|\le k<r.
\]

Here is why this remains true in a free cascade. Just before the first
free exchange, every stored selected center is blocked, so its total
count is at most the current matching size \(k\). A newly discovered
free candidate is not inserted into a selected set. Every subsequent
exchange in the cascade only removes matching blockers and truncates
selected sets; it never adds a selected center. After the cascade, the
fully blocked invariant is restored before another blocked addition.
That addition again keeps the number of selected centers at most the
number of their distinct matching blockers, which is at most \(k\).
The matching size is constant throughout the phase. Thus both displayed
sums are bounded even before the cascade is settled.

Every completed non-last layer passed the current growth test and
therefore has at least one matching blocker. Those blocking sets are
disjoint. Only the last layer may have lost its last blocker or may be
newly empty. Thus \(\ell\le k+1\le r\) at every microstate; the
analytic logarithmic depth bound is not used here.

For any fixed length \(\ell\le r\), the number of nonnegative
selected-count lists with total at most \(r\) is exactly
\(\binom{r+\ell}{\ell}\), and the same bound holds for blocker lists.
These binomial coefficients are at most \(2^{2r}\). Summing over
\(0\le\ell\le r\) gives at most

\[
                  (r+1)2^{4r}=2^{O(r)}
\]

possible micro-signatures. Allowing arbitrary nonnegative entries in
this count only overcounts the actual signatures; it avoids any reliance
on positivity of a transient last pair. Strict lexicographic descent
was proved for every actual state change in Section 5. Multiplying by
the at most \(r\) augmentation phases and the polynomial work per state
change preserves \(2^{O(r)}\).

Consequently one may take the minimum of this count and the main
quasipolynomial count, without changing the algorithm:

\[
 \mathcal P\,
 \min\!\left\{2^{O(r)},\,
       (r+1)^{O(\varepsilon^{-1}\log(r+1))}\right\}
       \operatorname{poly}(b+\log\mathcal P).
 \tag{A6}
\]

The two big-O constants are absolute constants of this implementation.
This is an upper-bound accounting refinement, not an algorithmic lower
bound or an assertion that a new leading approximation ratio is first
attained here.

### 7.2 Setting epsilon to zero is valid

There is also no limiting argument or numerical approximation needed
to obtain the exact additive boundary. Set

\[
                  \varepsilon=0,\qquad B=(T-u)/3>0.
 \tag{A7}
\]

Keep the same operations and replace the growth test by
\(|Y_i|>0\). All eligibility, exchange, free-cascade and maximality
proofs are independent of a positive epsilon. The star bound remains
strict, and now

\[
                  A=2B+u=T-B>0.
\]

At a completed maximal layer failing the new test, \(Y_i\) is empty,
so \(t=|Y_{\le i}|=w-1\). If \(t>0\), the current star bound gives
\(v(F_i)<A(w-1)\); if \(t=0\), the resource cover is empty. In both
cases,

\[
 v(F_i)\le A(w-1)<Aw
       \le (T-B)\bigl(r-|I\setminus\operatorname{owners}(Y_{<i})|\bigr).
 \tag{A8}
\]

Together with maximality outside the corresponding closure flat,
(A8) is the same explicit infeasibility certificate as before. Under
LP feasibility every completed layer therefore has at least one
blocker. There are at most \(k\) such layers and at most one temporary
last layer. The composition count from Section 7.1 applies unchanged;
the logarithmic-depth estimate is simply not asserted for epsilon zero.

Thus the same deterministic algorithm returns a basis allocation with
value at least \((T-u)/3\), or a verified infeasibility certificate for
\(Q(T)\), in

\[
               \mathcal P\,2^{O(r)}
               \operatorname{poly}(b+\log\mathcal P)
 \tag{A9}
\]

time and independence-oracle calls, using polynomial space. Exact
rational comparisons and inclusion minimality give the strict inequality
needed at the boundary. No assumption about a generic perturbation of
values, a positive slack parameter, or a supplied feasible fractional
solution is introduced.

### 7.3 The ground-set size does not reappear in the exponential factor

The rank refinement is algorithmic, not just a replacement of variables
in a layer count. Compute rank by a greedy scan of the \(q\) players,
using \(q\) independence tests on sets of size at most \(r+1\). In
each subsequent microstate, compute the relevant eligibility flat by
one independence test per player. Each query uses the fixed independent
set \(I\setminus Y_{<i}\), of size at most \(r\), together with
that player. Copying and constructing these query sets costs at most
\(O(qr)\) elementary operations.

After eligibility is known, one pass over the explicit liking lists
tests the available-value sums. A successful player's bundle is formed
and pruned in at most one further pass over its list. Resource masks
and current blocker-owner tables use resource IDs, so the forbidden
set is assembled from the stored bundles, not by repeatedly rescanning
all player pairs. The matching bundles are disjoint, and the selected
bundles are disjoint; each collection therefore has at most \(|J|\)
stored resource incidences. A fundamental circuit needs at most \(r\)
oracle tests and \(\operatorname{poly}(r)\) set operations. Updating
layer indexes, blocker pointers, and the independent owner set likewise
costs \(\operatorname{poly}(r)\) times the relevant explicit inventory.

Thus all work between successive charged signature changes is bounded
by

\[
       \mathcal P\,\operatorname{poly}(r)\,
                         \operatorname{poly}(b+\log\mathcal P).
\]

There is no additional quadratic enumeration of the \(q\) players.
The polynomial factor in \(r\) is absorbed into either bound in (A6)
and into (A9). Rank zero is returned immediately after the rank scan.
This validates the rank-sensitive minimum bound and the rank-parameter
fixed-parameter guarantee at the exact additive boundary.

## 8. Audit conclusion and exact limitation

The earliest exchange preserves retained eligibility, the new bundle
creates no hidden old blocker, and every lower maximality statement
retains the same eligibility and forbidden-resource sets. Current star
value accounting and the compact fractional rank bound prove current
growth. The integer signature counts every greedy addition, swap,
cascade and resumed search. No unresolved local or iteration-accounting
gap remains in the audited text.

The largest-item term remains material. For small resources with
\(u=o(T)\), the guarantee approaches one third. With a generic cutoff
\(u\le\theta T\), it is only \(((1-\theta)/3-\varepsilon)T\).
A separate large-resource reduction is needed for an unrestricted
allocation application; the standard balance gives a value near one
quarter. None of this audit supplies a below-four restricted-Santa-Claus
approximation or a polynomial-time one-third matroid theorem.
