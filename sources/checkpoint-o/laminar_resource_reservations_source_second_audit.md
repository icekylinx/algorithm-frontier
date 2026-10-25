# Separate source and invariant audit of laminar resource reservations

**25 October 2026. Reviewer: transfer_baselines.**

This is a separate review of `laminar_resource_current_blocker_reservations.md`.
It is not a duplicate of matching_optimization's
`laminar_resource_reservations_independent_audit.md`. The temporary duplicate
at this filename has been replaced by this review. I read the complete
reservation proof, recomputed its coefficients and wrappers, and checked the
public-model comparison against the primary BLMRS source.

## 1. The mathematical verdict

The laminar adapter passes. The steps needing substantive justification are
joint token feasibility, persistence under a player exchange, charging only
one resource value along a service path, and the fractional fat-resource
reduction. Each holds under the stated model. The already audited player-side
circuit, last-layer refresh, and signature lemmas remain explicit imports;
the new resource construction satisfies their required interfaces.

The result concerns independent receiving sets in each resource matroid,
common intrinsic resource values, and an independently supplied player-selection
matroid. It does not require a receiving basis inside the selected player set.
The latter condition would not follow merely by deleting discarded players.

## 2. A precise reservation check

For a resource j and feasible recipient set Z, assign distinct tokens to
Z intersect S separately at each laminar pool S. Capacity feasibility gives
enough tokens. No cross-pool compatibility between token labels is required.
Consequently these assignments realize all root-to-recipient service paths
simultaneously. Conversely, disjoint service paths immediately imply every
capacity inequality. Added singleton pools ensure one service per player and
resource. Capacity zero produces a loop region; truncating a capacity to
its represented set size prevents expansion of a large binary integer.

For availability, forbidden tokens are the union of selected records and
whole blocker bundles. If a new service chooses a token belonging to an
undiscovered matching bundle, that entire matching bundle is disjoint from
the old selected records: otherwise it would already be a blocker. The
one-blocker construction chooses the deepest pool having no matching-free
outside-forbidden token, copies one matching service's tokens above it, and
uses free tokens below it. The selected matching service lies in the chosen
pool, hence has all of those ancestor tokens. This constructs one persistent
service; it does not reroute the old allocation.

All records of a candidate use different resource indices, so their token
pools are disjoint. Individual reservations therefore combine into a joint
bundle. This would fail if the model allowed repeated use of the same resource
by one player without extra copy bookkeeping; that model is not claimed here.

## 3. Transactions and old maximality

For each free exchange, retain the candidate's exact token IDs through
truncation and install those records in the matching. The candidate avoids
the whole current matching and all retained selected records. Removing its
chosen player-circuit blocker can only delete conflicts, and the inserted
bundle introduces no conflict with retained centers.

A matching blocker has one designated selected owner. Therefore only that
owner can become newly free after a removal. The old-free-center cascade
uses the same transaction. Token reference counts must distinguish selected
ownership and blocker ownership, since one token may have both references.
Deleting one reference cannot erase the other.

At a strictly lower surviving layer, the same records form its forbidden
prefix before and after the transaction. Its set of available services is
literally unchanged. The player-circuit lemma preserves its eligibility flat.
These are the two independent facts needed to preserve an earlier maximality
certificate. It would be insufficient to know only that a new feasible token
assignment exists after the exchange.

## 4. Recomputing the cover, including zero pools

For each resource choose the highest forbidden-saturated pools. Their
recipient sets are an antichain and exactly cover the unavailable players
inside the declared resource ground set. Outside-ground players have zero
fractional column mass. Zero pools are saturated and contribute zero.

The fractional value excluded at resource j is at most
v_j times the sum of these capacities. Each saturated token belongs to a
selected service or a blocker service. One service path meets the antichain
at most once, so charging that token to one containing service yields

    Phi <= value(X) + value(Y).

This is an occurrence argument on a single antichain, not a sum over all
levels of the tree. It remains valid when several stars use the same resource.

Minimality and unique blocker ownership give the coarse coefficient
2(B+u). For the sharper coefficient, a singleton center of value at least B
has only singleton blockers at that resource; the center plus its b blockers
costs at most (b+1)u <= 2bu. A nonsingleton center contains only resources
below B. Any minimal blocker meeting it must also be nonsingleton, with value
below B+min(u,B). There are at most 2b bundles in that star. Hence

    C_lam(B,u) = max{2u, 2B+2min(u,B)}

is valid. Utility is counted once per resource service throughout.

## 5. Strictness and the rank parameters

At a completed scan, eligible player mass is at least
w = r-k+s, where k<r and s counts earlier blockers. Each positive eligible
row has strictly less than B times its player mass on available resources.
Thus a feasible compact relaxation forces Phi > (T-B)w for B<=T, including
the endpoint B=T. With rho=(r-1)/r and s/w<=rho, an empty new layer is
impossible when B+rho C_lam(B,u)<=T.

The count parameter is the selection rank r. Token count, laminar depth,
number q of available players, and all oracle work remain in a polynomial
input multiplier. No step replaces that multiplier by a claim depending
only on r. In particular explicit depth is harmless for the approximation
factor but is still paid in service construction and updates.

## 6. Fat, configuration, and approximate-oracle checks

Fat resources form a union matroid on players. Its independent sets are
precisely the player sets that can be partitioned among fat resources with
independent recipient parts. The accepted M* union N complement argument
therefore applies, and the resulting small selection rank does not exceed r.
At B0=T/(1+4rho), all small values are below B0 and
C_lam(B0,u)<=4B0, giving the exact denominator 5-4/r.

For B=T/(d+eta), d=1+4rho, the conservative coefficient
Cbar=2(B+B0) gives gap

    T-B-rho Cbar = (1+2rho)(B0-B).

Dividing by Cbar yields the claimed positive constant multiple of
min(eta,1). This is sufficient for the stated rank-quasipolynomial count.

The configuration comparator is stronger than the integer comparator.
Selecting one fat resource from each fat-containing configuration yields
individual column vectors dominated by the original matroid columns. Their
sum is in the fat union polytope by the union rank formula. Extending the
combined fat-plus-dual vector to a base leaves a complementary player vector
bounded by the all-small configuration mass. Scaling each small row downward
preserves every resource column and all optional row-perspective constraints.
No exponential configuration list needs to be computed by the algorithm.

For a lambda-factor available-bundle oracle, a failed fresh return below B
implies true available value below B/lambda. Only the lower fractional bound
changes. The same cover proves B/lambda+rho C_lam(B,u)<=T and denominator
lambda^(-1)+4-4/r. A positive singleton test identifies local feasibility
exactly, so restricting fat resource matroids is legitimate. Approximate
failures cannot be cached through arbitrary later searches; the fresh-scan
convention of the imported oracle adapter is required.

## 7. Primary-source comparison and limits

BLMRS, [arXiv:2307.08453v1](https://arxiv.org/abs/2307.08453v1),
Theorem 4, Section 4 and Appendix E, provide the public polynomial
8+epsilon general-value and 4+epsilon two-value resource-matroid results.
Theorem 21 supplies the fixed-player additive-largest-resource rounding
step, while Lemma 22 explains the general-value factor loss. These are
recipient matroids, the correct direction of constraint for this comparison.

The finite huge-resource construction in
`laminar_resource_public_comparison.md` encodes any player-selection matroid
through its dual without changing integer optimum. Thus the general base
model already has a polynomial 8+epsilon public baseline. The new near-five
result is a quality/time and parameter tradeoff. The public four result
must be retained in its two-value compulsory-player domain, and the public
core also gives four for unit values with arbitrary player selection.

The old physical-slot proof covers explicit transversal recipient systems,
not every laminar recipient matroid. Three parallel pairs with a rank-two
root provide a nontransversal laminar example: the three parallel classes
would require three distinct singleton neighborhoods in any transversal
presentation, contradicting rank two. This proves one separation and does
not assert containment in the other direction.

I found no missing mathematical interface in the laminar note. This audit
makes no claim that all public parameter reanalyses have been exhausted,
and does not count a general-resource exponential extension as a second
laminar quasipolynomial theorem.
