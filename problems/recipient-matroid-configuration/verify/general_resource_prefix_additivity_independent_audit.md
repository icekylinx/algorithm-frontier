# Verification note

**Curated source path:** `sources/checkpoint-o/general_resource_prefix_additivity_independent_audit.md`

The source audit follows.

# Independent audit of prefix rank additivity and eager release

**25 October 2026. Mathematical review of the new resource-matroid construction.**

This review concerns `general_resource_prefix_additivity_four_candidate.md`.
It is independent of the construction's author and checks the proof as a
resource-matroid theorem. It does not constitute external peer review or
formal verification. The review finds no unresolved mathematical gap in
the invariant, exchange, normalization, current-cover, or stated time
arguments of that draft.

The model remains one service per player-resource pair, arbitrary
independence-oracle player and recipient matroids, and common intrinsic
resource values. The main factor is 4-3/r, with its positive-error
rank-quasipolynomial alternative. A separate proof is required before
extending these statements to recipient polymatroids.

## 1. The stronger invariant is genuinely prefix-local

For each ordered center prefix S, W consists of the selected recipients
and matching recipients designated by S, while U consists of all other
matching recipients. The statement

\[
 r(W\cup U)=r(W)+|U|
\]

is maintained even for prefixes ending inside a layer. This qualification
is essential: after an exchange, the outgoing record may be designated
by a later center of the last retained layer and hence be unmarked for
an earlier internal prefix.

At completion, moving A from U to W preserves independence of U-A after
contraction. At a used nonproblematic resource the new recipient is
outside the span of W union U, so adjoining it also preserves this
independence. At a problematic resource every member of U is moved,
making the remaining additivity assertion vacuous. No unproved
relationship between different recipient matroids is used.

## 2. Strong freedom follows from an actual current rank comparison

For a stored center c, let V be the preceding W plus the current
designated-group recipients. If c's owner p is outside cl(V), the
prefix invariant after c gives

\[
 r(V+p+U)=r(V)+1+|U|,
 \qquad r(V+U)\le r(V)+|U|.
\]

Thus p is outside cl(V union U), which is exactly the span of the
current matching recipients and all preceding selected recipients.
This remains true when V is dependent. An empty group passes the
test because inherited availability is maintained for the current
preceding prefix.

The test is deliberately applied to every retained center, not only
the center whose designated group lost a member. Removing a matching
record may destroy a later dependency witnessed through the preceding
prefix. The full normalization scan is therefore necessary.

## 3. Every retained internal prefix survives an exchange

The earliest player-circuit rule places the outgoing record in layer
h strictly before the incoming center's layer i. Hence every retained
center precedes the incoming center, including all centers in layer h.
The strong span test therefore applies to every retained prefix.

For a fixed prefix, deleting the outgoing recipient either deletes
an element from W or an element from U. In the former case, contracting
a smaller flat cannot destroy independence of U. In the latter case,
deletion preserves it directly. The incoming recipient is outside the
span of the entire old W union U and so may be added to U after this
deletion.

This also accounts for records released from discarded higher layers:
they were already in U for every retained prefix. Their allocation
records do not change, and their release requires no new rank argument.
The newly inserted matching record has no inherited designated-group
flag, even when its owner appeared earlier.

Universal simultaneous reservations are preserved independently:
strong freedom permits adjoining the incoming service to any retained
reservation before deleting the old service. Removing the outgoing
record from both the matching and its group does not reintroduce a
service previously excluded by that group.

## 4. Old certificates and progress accounting remain valid

The inherited-availability set before a retained center can only lose
records; new centers are appended after it. Its original availability
continues to hold. The established earliest player-exchange lemma
preserves the eligibility flat of every retained layer.

Below h, both selected and designated matching records are literally
unchanged. Their old available sets and completed maximality
inequalities remain true. Layer h is refreshed, as required by the
existing algorithm.

Eager release is not a standalone removal of a center or release of
its blockers. It performs the existing atomic exchange and higher-layer
truncation. At the earliest affected layer h, X_h is unchanged and
Y_h loses exactly the outgoing matching record. Therefore the old
integer micro-signature decreases. An augmentation ends the phase.

Each normalization episode strictly reduces the last retained layer
whenever it exchanges. Full scans use polynomially many rank queries
on O(r)-element sets and occur only between charged mutations. At a
normalized state every group is nonempty and the groups are disjoint,
so the existing rank-bounded signature count applies. The proof does
not hide a scan loop at an unchanged state.

## 5. The rank saving is current, not historical

The telescoping cover charges a center together with its current
designated group relative to its current ordered predecessor prefix.

* A singleton center of value at least B has singleton blockers at
  the same resource. Its surviving dependency saves the center's one
  rank increment, giving at most u per blocker.
* A nonsingleton center has only resources below B. Every blocker
  sharing one of those resources is also nonsingleton and contains no
  resource of value at least B. With t at least two blockers, the
  total-value charge is below (t+1)(B+a), where a=min(u,B), and this is
  at most t(2B+a).
* For a singleton blocker group, normalization supplies a current
  shared-resource dependency. It saves that resource's intrinsic
  value from the separate count of both bundles. Minimality of the
  blocker gives value(blocker)-value(shared resource)<B, yielding
  charge below 2B+a.

Thus the stated coefficient

\[
 C(B,u)=\max\{u,\ 2B+\min(u,B)\}
\]

follows for arbitrary recipient matroids. The previous birth-saving
counterexample does not satisfy normalized stability: its retained
center becomes strongly free and must be processed.

## 6. Wrapper and positive-error arithmetic

For tau=1/lambda, rho=(r-1)/r, and d=tau+3rho, the fat threshold
B0=T/d leaves u<B0. At B=B0 the sharp coefficient is at most 3B0,
which proves the exact boundary.

For eta0=min(eta,1) and B=T/(d+eta0), one has B>=B0/2. Hence
u<B0<=2B and C(B,u)<=3B. The slack is at least eta0 B, giving
slack/cover at least eta0/3. This proves the advertised uniform
rank-quasipolynomial exponent, including the absence of an additional
inverse-lambda factor in that exponent.

The configuration-LP fat decomposition, dual/union costs, finite
target search, and local feasible-bundle interface are unchanged from
the audited main manuscript. This review does not infer an unrestricted
compact-LP comparison after arbitrary large items are introduced.

## 7. A downstream integer-quantum caution

If every small resource has unit value u and the bundle threshold is
b u for an integer b>=1, every minimal bundle has exactly b units.
The same normalized rank charge sharpens further to

\[
 C_b=(2b-1)u.
\]

For b=1 this is the singleton case. For b>=2, a singleton blocker
group saves one unit, while t>=2 gives
(t+1)b<=t(2b-1). A failed exact scan has value at most (b-1)u.

This is enough for an exact-boundary rank-exponential quota theorem.
It does not, by itself, give a rank-quasipolynomial uniform
(3+eta)-approximation for every integer quota. At target k=4 units
and requested output b=2, the lower-cover coefficient and limiting
upper coefficient both equal 3 units; the residual slack is only
3/r. Positive multiplicative approximation error below one does not
permit rounding the requested output down to one unit. This discrete
case must be handled explicitly in any stronger time claim.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
