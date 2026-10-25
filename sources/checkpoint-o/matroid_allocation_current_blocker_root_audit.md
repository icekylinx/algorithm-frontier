# Root audit and scope of the rank-sensitive matroid allocation theorem

**25 October 2026. Root proof review completed.**

Audited main construction:
`matroid_allocation_current_blocker_quasipolynomial.md`.
Two separate reviewers checked the exchange, freshness, growth,
signature and explicit-input implementation arguments; their notes
are included in this checkpoint. This is mathematical review, not
formal verification, peer review, or a computational benchmark.

## 1. Accepted result

Let a matroid of rank r on q players be given by an independence
oracle. Resources have player-independent positive rational values
and explicit liking incidences. Let u be the largest item value and
let P be the explicit input volume. For T>u and
0<epsilon<(1-u/T)/3, the deterministic algorithm returns either:

* a matroid basis, supplied with disjoint liked-resource bundles of
  value at least (T-u)/3-epsilon T for each selected player; or
* an explicit certificate that the compact fractional relaxation
  Q(T) displayed in the main note is infeasible.

The time and independence-query count are

\[
 P\min\{2^{O(r)},(r+1)^{O(\epsilon^{-1}\log(r+1))}\}
                  \operatorname{poly}(b+\log P).
\]

At epsilon zero the exact value (T-u)/3 is obtained, with the same
infeasibility alternative, in P times 2^{O(r)} times the numerical
bit-cost factor. Both versions use polynomial space. Rank zero is
handled immediately after the greedy rank computation.

The algorithm does not need a feasible fractional solution as input.
Returning a lower-valued integral allocation does not certify that
Q(T) itself is feasible. The implication is in the other direction:
if Q(T) is feasible, the failure outcome cannot occur.

## 2. The crucial matroid invariant

A candidate owner in layer i must lie outside the closure of the
current independent owner set after removing the earlier blocking
owners. Several selected bundles may have the same player. Their
joint independence is neither required nor used.

For a new owner in the span of the current set, choose an exchangeable
blocker in the earliest layer represented in its fundamental circuit.
For each retained prefix, that entire circuit lies in the prefix's
independent set plus the new owner. Exchanging within that circuit
preserves the closure of that independent set. Thus every retained
eligibility set is exactly unchanged. An owner already in the current
set is handled separately by replacing that player's old bundle;
eligibility forces that bundle to be in an earlier blocking layer.

This is stronger than merely preserving independence of the new
matching. It also excludes a hidden repeated-owner failure: a newly
inserted owner cannot simultaneously have been an eligible selected
owner in a retained lower prefix whose span contains it.

## 3. Freshness is maintained in the current state

All selected bundles are physically resource-disjoint. Every current
matching blocker has a unique selected owner, and every blocker of
every retained selected bundle is explicitly stored. A free incoming
bundle is disjoint from every selected bundle that survives the
exchange. Hence it creates no unrecorded old blocker.

Removing one blocker can free only its unique selected owner. That
already stored candidate is processed immediately. Each further
nonaugmenting exchange moves to a strictly earlier layer; the cascade
cannot loop within one layer.

For every retained layer below the exchange layer, both its eligibility
set and its forbidden-resource set are literally unchanged. Its old
maximality assertion is therefore still true. Only the last surviving
layer is refreshed, before another growth test or append. There is
no reliance on a property that held only at a layer's birth.

## 4. Resource and rank accounting

An inclusion-minimal B-bundle has value less than B+u. A minimal
blocker has less than B value outside any selected bundle it meets.
At a fully blocked current prefix, distinct blockers cover all
selected bundles, so a selected count a and blocker count t satisfy
a<=t and

\[
                 v(F)<(B+u)a+Bt\le(2B+u)t.
\]

Repeated player names do not affect this resource statement. A large
item exceeding B is also permitted: a minimal bundle containing it
is a singleton. The argument does not assume u<=B.

For the complement U of the relevant closure flat, the base-polytope
constraint gives x(U)>=r-k+|Y_previous|. Fresh maximality limits
available value outside F to less than B per eligible player.
The individual constraints y_pj<=x_p then bound outside fractional
value by B x_p. Summing resource capacities proves
v(F)>=(T-B)x(U). These are exactly the stated compact-LP constraints;
an ordinary assignment LP without y_pj<=x_p would not suffice.

Combining the two inequalities proves current blocker growth by
epsilon times one plus the earlier blocker count. On a failed growth
test, the independent set, its closure and F form an explicitly
checkable infeasibility witness.

## 5. Rank dependence and exact boundary

In a phase, k<r matching bundles exist. The sums of all selected
counts and all blocker counts are at most k even in a free cascade:
new free candidates are processed without insertion, and a cascade
only truncates selected sets. All non-last layers have a positive
blocker count. The depth is thus at most r, and for positive epsilon
also O(epsilon^{-1} log(r+1)).

The integer signature (-|X_1|,|Y_1|,...,-|X_l|,|Y_l|,infinity)
strictly decreases at every append, blocked addition and free exchange.
The logarithmic-depth count gives the quasipolynomial term. Counting
the two lists as weak compositions of at most r gives at most
(r+1)2^{4r} signatures, proving the exponential term for the same
algorithm. At most r rank-augmentation phases occur.

At epsilon zero, 2B+u=T-B. A completed maximal layer with no new
blocker gives v(F)<(T-B)(r-|J_0|), including the empty-cover case.
Every passing layer therefore has a blocker and the composition
count still applies. This proves the exact additive guarantee without
taking a limit.

The q players only require a linear number of oracle queries per
scan. Each query set has O(r) elements, circuit discovery has at
most r queries, and resource processing scans explicit liking lists.
There is no hidden enumeration of pairs of players. The remaining
polynomial factors depend on r and are absorbed in both displayed
state-count bounds. Fixed rational subset sums have polynomial bit
length in the total numerical input encoding.

## 6. Public comparison and limits

The current printed comparison is Davies--Rothvoss--Zhang v4,
Theorem 2, with (T-u)/5-epsilon T in polynomial time for fixed
epsilon. Its Section 4 explains a correction to an earlier analysis.
Earlier versions and the Davies dissertation contain one-third
claims with different hypotheses or largest-item penalties. The
separate public-comparison note records that history. No assertion
of global priority for the numerical coefficient is made.

A proposed algebraic retuning of the public framework has a separate
unclosed exchange-interface question and is not promoted to a proved
baseline in this checkpoint. This does not negate the printed theorem.

The independently checked compact Santa Claus reduction gives value
(1-3epsilon)T/4, and exactly T/4 with the exponential variant. It
does not beat the known polynomial 4+delta result for ordinary
restricted Santa Claus, or the nonconstructive topological gap bound.

The accepted contribution is a fully specified, rank-sensitive
quality/time bound for the general player-matroid allocation problem,
with a current-state proof and a checkable fractional-infeasibility
alternative. It has no implication that the original arbitrary
general-graph matching exponent has improved below 4/5.

Primary comparison:
<https://arxiv.org/html/1807.07189v4>.
