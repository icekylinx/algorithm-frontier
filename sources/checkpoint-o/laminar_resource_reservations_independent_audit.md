# Independent audit of laminar resource reservations

**25 October 2026. Mathematical and implementation audit.**

This audit checks laminar_resource_current_blocker_reservations.md.
The new reservation, availability, cover, and fat-wrapper interfaces
pass. The accepted player-matroid earliest-exchange and signature
proofs are used as imports after verifying their physical-set
hypotheses below. This is not a claim of priority against all public
algorithms for the laminar resource subclass.

## 1. Token feasibility is exact

For a fixed resource j, a service to player p chooses one token
from each capacity pool on p's root-to-leaf chain. Simultaneous
services have disjoint token supports.

If the receiving set Z admits these paths, at most b_(j,S) services
can pass through a pool S. Therefore every laminar capacity holds.
Conversely, if all capacities hold, each pool can independently
assign distinct token labels to the services passing through it.
The labels at different levels need not be connected by additional
constraints. These independent choices realize all service paths.

This equivalence is sufficient even when capacities are not
monotone along the tree, or when some constraints are redundant.
A zero-capacity pool simply excludes all players below it.
Added singleton capacity-one pools enforce at most one service of
a resource to a particular player. Adding a root of capacity equal
to its ground-set size does not change feasibility.

All capacities can be truncated to the size of their represented
player set. The total number of tokens is consequently polynomial
in the explicitly supplied laminar input and player count. There
is no expansion of an exponentially large binary integer in this
model.

The value of a whole service is v_j, independent of its path length.
Treating each of its reserved tokens as an extra valued item would
not represent the intended allocation problem.

## 2. Exact availability and persistent one-blocker witnesses

Let F contain all selected-center tokens and all tokens of matching
bundles already discovered as blockers. A new service (p,j) is
available exactly when every pool on its chain has an unused token
outside F. Tokens owned by undiscovered matching bundles are
allowed, since they are precisely how new blockers are discovered.

Different resources use disjoint pools. A candidate player can
therefore take any subset of its available resources without a
reservation conflict between those distinct services. Its maximum
available additive value is the sum of their intrinsic values.
Greedy selection followed by deletion of whole services produces
an inclusion-minimal bundle above B.

For the stronger one-blocker rule, take the deepest chain node S
without a matching-free token outside F. An outside-F token at S
belongs to a matching service at resource j for some player b.
That matching bundle is not a prior blocker, and none of its
tokens meets any selected center; either event would have put
the entire bundle in the forbidden set.

The player b belongs to S. Its old service path therefore supplies
outside-F tokens at every ancestor of S. Use these tokens above
and including S, then use matching-free outside-F tokens below S.
The deepest-node choice guarantees the latter. The new service
meets at most that one matching bundle.

No matching reservation is rerouted in this argument. In particular,
the proof is not a collection of separately realizable local
exchanges that fail to coexist.

The one-blocker witness is a useful strengthening, but the main
cover proof needs only full persistent token ownership and the
usual unique selected owner of each discovered matching blocker.

## 3. The earlier-layer invariants really remain physical invariants

All matching bundles are mutually token-disjoint, and all selected
centers are mutually token-disjoint. A newly constructed candidate
avoids the full old X union Y support. Thus a matching bundle
newly discovered by it could not also meet an older selected center:
that bundle would already have been in Y and all of its tokens
would have been forbidden.

A free candidate is token-disjoint from the entire current matching.
The earliest player-circuit exchange removes one matching bundle
and inserts the candidate with its already chosen reservations.
The new matching is token-disjoint, hence resource-feasible.
The candidate is also disjoint from every retained selected center,
so it cannot introduce a new blocker of a retained layer.

Removing a matching bundle can free only its unique selected owner.
The same immediate old-free-center cascade and strict decrease in
the chosen exchange-layer index apply.

For every strictly lower retained layer, its old selected bundles
and old matching-blocker bundles are the same physical token sets.
Removing a blocker from a higher layer does not remove a token
from that lower forbidden set. Nor is the new matching bundle
inserted into the earlier blocker prefix. Higher selected layers
may be released, but their tokens did not belong to the lower
prefix. Therefore lower availability is literally unchanged.

The imported earliest-circuit lemma separately preserves the lower
player flats. These two facts together preserve old maximality.
Only the last surviving layer is refreshed. No fresh resource
matching, fundamental circuit, or token reassignment is invoked
to reinterpret an earlier availability assertion.

As an implementation convention, an old selected center that
becomes the free candidate keeps its token-ID list through the
higher-layer truncation. Insert that same reservation into the
matching, or save its list before releasing its selected label.
Releasing it and choosing unrelated tokens again would not be the
proved transaction.

## 4. The saturated antichain removes the depth factor

For a resource j, choose all F-saturated pools with no saturated
proper ancestor. Their player sets form an antichain. A declared
eligible player lacks an outside-F reservation exactly when its
chain meets one of these pools, so their union is exactly the
unavailable receiving set. Players outside the resource ground set
have zero column marginal and need not be covered.

Any feasible fractional column puts at most b_(j,S) mass in such
a set S. Since the antichain sets are disjoint, unavailable
fractional value is at most

v_j sum_(S in A_j(F)) b_(j,S).

Every saturated pool contains exactly b_(j,S) forbidden tokens.
Every one of these tokens belongs to a selected service or a
matching-blocker service, possibly both. A single service path
meets the antichain at most once. Charging the forbidden token to
one containing service therefore proves

Phi(F) <= sum_(C in X) v(C) + sum_(D in Y) v(D).

There is no charge proportional to the number of nodes traversed
by a service. Shared resource names across different stars do not
invalidate this argument: the counted objects are reserved token
occurrences on a single antichain.

At a fully blocked state, unique blocker ownership gives |X|<=|Y|.
Minimality then supplies the coarse coefficient 2(B+u).

The sharper coefficient

max{2u, 2B+2 min(u,B)}

also follows. A singleton center using a resource of value at
least B can meet only singleton minimal blockers using that same
resource. Its center-plus-blockers total is at most 2u times
its blocker count. A nonsingleton center has only resources below
B. Every blocker meeting it contains such a resource, so a
minimal blocker cannot simultaneously contain an item of value
at least B. All bundles of this star have value below
B+min(u,B), and their number is at most twice the blocker count.

No claim that the stars are disjoint in resource indices is needed.

## 5. The strict fractional certificate survives

At a completed last layer, write J_0 for the independent player
set defining eligibility, and w=r-|J_0|>0. Every base-polytope
point has at least w player mass outside cl(J_0).

For an eligible player, the available-resource sum is below B.
The perspective bounds y_pj<=x_p give strictly less than B x_p
fractional value on available resources whenever x_p>0. Its total
demand is at least T x_p. Summing over positive eligible mass
therefore requires strictly more than (T-B)w value on unavailable
services.

The antichain calculation bounds all such unavailable value by
Phi(F). Hence

Phi(F)>(T-B)w

for every feasible relaxation point. The strictness remains valid
at B=T. A weak reverse inequality supplies the claimed
infeasibility certificate, verifiable from the explicit saturated
antichains, values, availability checks, and original player-
matroid oracle.

Using s/w<=(r-1)/r, the sufficient exact boundary

B + ((r-1)/r) C_lam(B,u) <= T

is consequently sound. The old rank-only signature proof applies
because all of its resource-ownership and maximality invariants
have now been re-established for token supports.

## 6. Fat resources and reconstruction

For fat resources, their union matroid N is on the player ground
set. An independent set of N has an explicit decomposition into
sets independent in individual fat resource matroids. Giving a
player the resource named by its part supplies one fat unit of
utility. Distinct parts do not give a player two assignments.

An integral comparator yields the same forward promise by keeping
one fat resource for every fat-supplied player. The resource
receiving sets remain independent after this deletion. The
established union with M*, dual-basis extension, and complementary
small-player basis argument is therefore valid, with derived rank
at most r.

After the inner algorithm succeeds, the union decomposition and
the subsequent dual-basis extension may discard some previously
supplied players. Downward closure of every resource matroid
ensures that this only relaxes resource feasibility. Every retained
player already has its small bundle or one decomposed fat resource;
no allocation must be invented for a newly retained player.

For u<B_0 and B_0=T/(5-4/r), the small coefficient is at most
4B_0. Thus the exact boundary follows directly. The factor-one
rank-one case is consistent with the explicit independent-service
model.

The positive-error calculation also checks: with
rho=(r-1)/r and d=1+4rho, its cover gap is
(1+2rho) epsilon T. Dividing by 2B+2B_0 yields at least
min{eta,1}/16, so the chosen current-growth threshold
min{eta,1}/32 has the required constant slack.

## 7. Configuration and optional local-family extensions

From a fat-containing configuration, selecting one fat resource
produces a resource-column vector dominated coordinatewise by
the original column. Independent-set polytopes are downward closed.
The chosen vectors therefore remain in their individual resource
matroid polytopes, and their sum, bounded by x<=1, belongs to the
union matroid polytope.

The derived small player vector x' is dominated by the all-small
configuration mass h. Scaling each all-small player row by
x'_p/h_p preserves every resource column coordinatewise and
preserves the corresponding perspective demand. The zero-h case
has x'_p=0. This proves the stated configuration-LP comparator
without enumerating configurations.

A player-local downward-closed family is compatible with deleting
whole services. Restricting its configurations to the available
resource list preserves that family. With a lambda-factor
availability oracle, the strict available-value bound changes from
B to B/lambda and no token-cover term changes. Feasible singleton
tests permit the stated restriction of each fat resource matroid.
For 0<lambda<=1, the resulting denominator
lambda^(-1)+4-4/r and its positive-error algebra are consistent
with the same proof.

All oracle, path-list, token-pool, and union operations are paid
by a polynomial factor in the explicit input and numerical
encoding. No depth term enters the approximation denominator.

## 8. Verdict and limits

The complete laminar reservation adapter passes this independent
audit. It gives a valid joint physical representation, a strict
relaxation certificate, and the stated rank-dependent small-to-fat
composition.

It does not furnish the corresponding interface for arbitrary
resource matroids. Laminarity is used in both the single-chain
reservation structure and the highest-saturated-node antichain.
Likewise, this audit establishes mathematical correctness of the
construction; it does not establish that its numerical
approximation ratio is absent from the public literature for the
same subclass.

