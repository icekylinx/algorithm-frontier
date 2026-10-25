# Root audit of laminar reservations and symmetric count families

**25 October 2026. Internal mathematical review completed.** These
are two different representations. The laminar constraints belong to
a resource's receiving-player set. The integral polymatroids in the
symmetric-count extension belong to each player's own type-count
vector. The distinction is preserved throughout the audit.

## 1. Laminar resource reservations

In `laminar_resource_current_blocker_reservations.md`, a service
receives its intrinsic value once and reserves one token at every
node of its resource's root-to-player chain. Independent token choices
at the separate nodes are sufficient: there is no additional path-label
consistency constraint. Counting these tokens is exactly the supplied
laminar feasibility system. Capacities can be clipped at the player
count, so the token representation is polynomial in the explicit
input rather than in a huge numerical multiplicity.

The strongest local witness rule is correct. At the deepest chain
node lacking an available matching-free token, choose an available
token belonging to matching owner b. This bundle is outside Y and
therefore touches no existing selected token. All of b's ancestor
tokens are available. The deeper nodes have matching-free available
tokens by the choice of the node. Thus the service encounters at
most one matching bundle, with no old reservation rerouting.

For the main factor-five bound, this strengthening is not necessary:
arbitrary available tokens still give valid physical ownership and
the coarse cover. It is nevertheless a correct additional interface.

Stored free centers retain their original token identities through
the exchange. A free inserted bundle avoids every retained center,
so it introduces no hidden blocker. The earliest player-circuit
lemma preserves lower eligibility flats, while old lower token sets
remain literally unchanged. These are the two separate conditions
needed to reuse lower maximality.

For each resource, the highest fully forbidden laminar nodes form
an antichain. They cover exactly the unavailable eligible receivers.
The resource-column LP constraints charge their total capacity.
Each selected or blocker service intersects this antichain at most
once, so its intrinsic value is charged at most once. There is no
factor depending on the laminar depth.

The sharper star coefficient follows because a blocker sharing a
token uses the same resource as its center. A singleton center
forces singleton blockers; a nonsingleton center cannot meet a
minimal blocker containing a threshold-sized resource. This proves
max{2u,2B+2min(u,B)} per blocker. The strict LP bound makes the
exact rank-dependent condition valid at equality.

The fat matroid is the union of the actual resource matroids, not
an inferred transversal representation. The usual dual-union basis
selection, resource decomposition and deletion steps remain valid.
For the configuration-LP comparator, designated fat-service marginals
are coordinatewise below the old resource columns. All-small
conditional marginals also only decrease those columns. Downward
closure of resource independent-set polytopes therefore supplies
both required feasibility implications.

The resulting factor is 5-4/r in rank-exponential time and this
factor plus eta in rank-quasipolynomial time. The stated positive
gap calculation is valid also for approximate available oracles,
giving lambda^-1+4-4/r+eta with paid oracle work. Rank zero, rank
one, zero-capacity nodes, looping receivers and the original input
size are handled explicitly.

Finally, the rank-two example with three parallel pairs is indeed
nontransversal. Every nonloop parallel pair would require a unique
single slot; distinct pairs require different slots. Three such
slots would contradict its rank two. This establishes that the
laminar result is not merely the earlier supplied-slot representation,
without claiming containment of all transversal matroids.

## 2. Symmetric local families under binary supplies

In `type_symmetric_downward_closed_binary_allocation.md`, the
uniform unit-copy lift is an existence argument only. It is valid
for every feasible count-vector perspective marginal and for every
fixed forbidden set of physical units. Intersecting each conceptual
sample with the available units preserves the local family by
downward closure, and gives exactly the available marginal in (S4).
The algorithm remains deterministic and never constructs that random
sample or expands the unit universe.

Type symmetry lets the count oracle's output be realized by any
fixed selection of the indicated numbers of available cell units.
The established split/merge operations then preserve actual unit
identities. Batched pruning removes individual units by arithmetic
counts, retaining feasibility and proving minimality without a loop
proportional to capacity. Fat tests skip zero-supply types, and the
largest-unit convention is zero on an empty positive-supply universe.

For the local integral polymatroid, the box-restricted rank

\[
 g_A(S)=\min_{Q\subseteq S}\{f(Q)+A(S\setminus Q)\}
\]

is normalized, monotone, integral and submodular. Uncrossing two
minimizers uses the submodular inequality for f and exact modular
equality for the two A terms. Splitting a feasible vector across
Q and its complement proves P(f) intersect [0,A] subseteq P(g_A);
choosing Q=S and Q=empty proves the reverse inclusion.

The greedy prefix differences therefore form an integral optimizer
for the common nonnegative value objective. Each prefix rank is one
submodular minimization, for a total of O(t) such calls. Their oracle
and numerical encoding costs are charged. This handles cross-type
local constraints, rather than only independent coordinate quotas.

The binary-knapsack chunk construction is also valid. Its subset
sums realize every feasible integer count. A chunk in a representation
of a feasible count vector cannot individually exceed that vector's
budget, so discarding singleton-infeasible chunks loses no feasible
vector. Profit scaling applies to the polynomial number of chunks.
Afterward the allocation algorithm receives counts and prunes in
units, so its star parameter is the unit value, not a large chunk
profit. The FPTAS workspace and inverse-accuracy dependence are paid.

The fat-capacity union reduction and configuration-LP scaling preserve
the perspective families, just as in the explicit-unit model. Thus
the factor remains lambda^-1+3-3/r, with the same positive-error
rank-quasipolynomial term and no expansion by total supply.

## 3. Status and comparison

Both adapters have independent reviews in addition to this root
audit. Their mathematical guarantees do not establish publication
priority. The separate public comparison records the stronger
ordinary all-player special cases and the named general-resource
polynomial baseline. These transfers do not change the accepted
4/5 research exponent for arbitrary general-graph maximum matching.
