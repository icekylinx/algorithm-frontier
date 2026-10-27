# Exact realization of ordered resource reservations

The implementation in [reference/reservations.py](reference/reservations.py)
realizes the resource invariants of the [main proof](proof.md), independently
of the player-side choice of layers and bundles. This note makes its executable
boundary explicit and supplies the accounting omitted by an abstract rank
oracle interface.

## Contract

The input gives a finite player ground, one recipient-matroid rank oracle per
resource, and an initial matching with distinct owners and independent recipient
columns. Each bundle has a nonempty explicit set of resource IDs. Resource
matroids may have loops, parallel elements and any rank. Each player-resource
pair supplies at most one service. The backend checks the input column ranks;
it assumes the supplied functions are matroid rank oracles.

The state stores an ordered list of centers, disjoint designated groups of
current matching record IDs, and immutable matching bundles. The empty state
has the universal reservation invariant (P4), every prefix rank-additivity
identity (P5), and the inherited availability invariant (P6).

**Realization theorem.** Every successful call sequence preserves (P4), (P5),
(P6), disjoint designated groups and distinct services. A successful
`releasable` test implies strong resource freedom (P13). An exchange keeps the
specified prefix and deletes only the outgoing record's designation. These
claims hold for every supplied recipient matroid; representability is not
required.

**Proof.** A completion checks (P7). It explicitly rejects reuse of a current
matching service by the same owner: a full allocation algorithm already
excludes that case by player eligibility, but the standalone resource interface
must enforce it. Previously selected copies of that service are excluded by
the closure check. For each problematic used resource, completion moves every
unmarked matching recipient into the new designated group, exactly as (P9).
Other groups are untouched and all new blockers share a used resource.

For a reservation containing the new center, the problematic resource loses
all unmarked recipients, and the resulting old reservation is an independent
subset of the selected-plus-marked closure. Availability extends it. At a
nonproblematic resource the incoming owner is outside the span of the entire
old matching and selected recipients. A reservation omitting the new center
is unchanged. This proves all subset instances of (P4) at once.

For the new prefix, moving some unmarked recipients into the marked set
preserves independence of the remaining unmarked recipients after contraction.
A nonproblematic incoming service is independent even over the entire old
span. A problematic used resource has no unmarked recipient left. These are
the three cases in Section 3, proving (P5). Earlier prefixes are unchanged.
The new availability check establishes (P6).

The `releasable` test is (P12), evaluated on the current state, including every
remaining record of a conservative nonempty group. Prefix additivity (P5)
then shows that the center raises the rank even after all unmarked recipients
are restored. This is precisely the rank-increase argument of Section 4 and
proves (P13); no dependence witness from the center's birth is reused.

Before exchange, the implementation directly checks that each incoming service
is outside the span of the old matching together with all retained selected
recipients. It also prevents duplicate matching owners. Thus every retained
reservation can receive the new service before deleting the outgoing one.
Deleting the outgoing service from the matching and its old designation
preserves (P4). For each retained prefix, deletion either removes an element
from its marked span or from its independent unmarked set; both preserve
(P5). Inserting a service outside the whole old span restores the required
unmarked independence. Retained preceding marked sets only shrink, so (P6)
persists. The new record is unmarked and has a fresh identity. Augmentation
discards all centers and leaves feasible actual recipient columns. This proves
the induction. The reasoning does not use a particular representation of a
recipient matroid. End of proof.

## Paid oracle and representation costs

Let `m` be the number of resource oracles, `k` the current number of matching
records and `c` the number of stored centers. Every designated record appears
in at most one group. Each of `available`, `complete`, `releasable` and
`exchange` uses at most a constant times `m` original rank calls on at most
`k+c+1` player names. A conservative ordinary-work bound is
`O(m*(k+c+1))` set operations plus the actual oracle work; Python hash-table
operations use their usual expected-time implementation. Resource IDs, player
names and record counters additionally incur their ordinary bit costs.

Stored bundle incidences and group memberships take
`O((k+c)*m+k+c)` words, in addition to the caller's oracle workspace. Immutable
snapshots have the size of the records they expose. New record IDs are
monotonically increasing; after `a` accepted changes they need
`O(log(k+a+2))` bits. Under the main search's proved signature bound this is
polynomially many bits. Rational bundle-value arithmetic belongs to the caller
and is not hidden in these bounds.

Repeated all-center normalization is a caller operation: a scan invokes
`releasable` on every current center and pays its cost. The resource backend
does not itself prove that arbitrary caller-driven exchanges terminate, select
an original player basis, or attain a value approximation. Those conclusions
use the main proof's player-eligibility, earliest-layer and signature arguments.
The local availability optimizer and polynomial matroid-union decomposition
remain separate paid components.

## Independent evidence

[check_reservations.py](verify/check_reservations.py) evaluates universal
reservations by enumerating every subset of selected centers and evaluates
rank by enumerating binary spans, independently of the Gaussian elimination
used by its supplied rank oracles. It checks every internal prefix, distinct
services, shared-resource designation and the strong-freedom implication.

The suite combines all one-resource binary representations on three players,
a specific nonempty-group eager-release example, and seeded multiresource
traces with exact rational minimal bundles. At normalized states it also
checks the sharp current rank-cover coefficient (P19). The program permits
resource-valid transitions that are more general than a player-layer search;
it does not treat those traces as complete allocation executions. Finite
examples support the symbolic proof and do not exhaust all matroids.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
