# Reconstructing real-edge provenance from a cover's vertex map

**Status: source-to-export wrapper theorem candidate, 24 October 2026.**
This note supplies an explicit real-edge identity and gradient map for
the rounded SNC export. It does not assume that a vertex-map-only
flatness statement already distinguishes parallel input edges or real
loops from null connectors. The source metric convention used below
is stated separately. The existing safe master-backend versions are
not silently changed by this note.

The primary source is
[Chen et al., arXiv:2311.18295v1](https://arxiv.org/abs/2311.18295v1),
Theorem 4.1, Section 4.2 item 4, and Theorem 6.2. Source Definition
2.3 gives topological flatness through a vertex map. Section 4.2
assigns a forest edge its real preimage's gradient and a no-shorter
length, and Theorem 6.2 explicitly gives the mapped input-edge
length convention. The wrapper below needs only the corresponding
MINIMUM-preimage metric inequality, not a source-supplied stable
choice of a parallel edge ID.

## 1. Remove genuine immediate loops first

At each degree-three general-cycle instance, maintain an exact heap
of its genuine input self-loops, keyed by `|g_e|/ell_e`. Remove those
loops from the graph sent to the SNC. Each loop keeps its own real
edge and price-lifetime IDs and can be returned as one oriented
single-edge candidate.

This does not change the approximation problem. A circulation is
the sum of its loop coordinates and its nonloop restriction, on
disjoint supports. Its ratio is at most the larger of the best
loop ratio and the best nonloop ratio. Conversely either optimum
is an available circulation. Thus the original optimum is exactly
their maximum. Heap updates and candidate comparison take only
ordinary logarithmic work, including parallel loop identities.

Call the remaining loopless graph G. It can have parallel edges,
but has degree at most three. An edge whose projection to some
EARLIER ancestor graph is null is still a genuine G edge here.
Only self-loops in the immediate G vertex set are removed to this
heap. This distinction is necessary in the recursive construction.

## 2. Private rounded graph and the precise source metric premise

Fix one cover radius D and a fixed local inventory of at most m
vertex slots. Let `delta=D/m^4`. The private graph Q_D contains:

* every current genuine nonloop G edge e with `ell_e<=D`, with
  rounded integer length `w_e=ceil(ell_e/delta)<=m^4`;
* a permanent simple path through the declared slots, whose fresh
  artificial edges have length `m^8`.

Q_D is loopless, connected, and has degree at most five. Genuine
and artificial edges may be parallel. The source receives only
edge insertions/deletions on these fixed slots, at requested
diameter parameter m^4. All its lengths are in `[1,m^8]`.

Let F be its explicitly maintained forest with vertex map pi and
marked set S_F. Let its occurrence/diameter/recourse factor be
gamma, with `gamma<=m^3/2` at the eventual parameter range. The
metric premise used is:

> If a forest edge f has distinct images u,v, then Q_D has at
> least one edge between u and v, and the source forest length
> of f is at least the minimum current Q_D length between u,v.

This is weaker than knowing which real preimage edge the source
chose. It follows from the no-shorter real-preimage convention
above. A purely topological vertex map WITHOUT this metric
premise would not suffice to prove the marked diameter below.

Because Q_D has no self-loop, a source forest edge with equal
mapped endpoints can only be a true-null connector under the
flat-map contract. This endpoint test is justified ONLY at this
loopless private interface; it is not used as a generic test at
later lifts.

## 3. Canonical real representatives

For each unordered distinct slot pair `{u,v}`, define r_D(u,v)
to be the current G edge between u,v of minimum ORIGINAL length
among edges satisfying `ell_e<=D`, breaking ties by lifetime ID.
If there is no such edge, leave r_D undefined. Only current
ADMISSIBLE edges are considered. In particular, an unavailable
edge of length greater than D is never chosen.

For each current source F edge f:

1. If its endpoint images agree, register it as
   `TRUE_NULL(input_slot)`.
2. If the images are distinct and r_D is defined, register it
   as `REAL(r_D, orientation, endpoint_correspondence,
   price_lifetime)`, with exported length `ell_(r_D)` and signed
   gradient `g_(r_D)`.
3. If the images are distinct and r_D is undefined, exclude f
   from the export. Topological flatness then implies that its
   current private preimage can only be an artificial path edge.

Then contract the registered true-null forest edges, as in
[local-length-aspect-preservation.md](local-length-aspect-preservation.md). Every retained real record
keeps its explicitly chosen edge ID. A real loop returned by the
separate heap never enters this contraction.

The minimum-original-length choice also minimizes rounded length,
since the ceiling map is monotone. If r_D exists, every artificial
parallel edge is longer than it. Hence for the source metric L_F,

    ell_(r_D) <= delta w_(r_D)
               = delta min_(e between u,v in Q_D) w_e
               <= delta L_F(f).                           (1)

This remains true if the source internally intended f to use an
artificial edge or a different genuine parallel edge. Choosing a
shorter available real representative only decreases the exported
metric. Its gradient is assigned from that chosen representative;
the source SNC algorithm itself does not inspect gradients.

If r_D does not exist, the same metric premise gives

    L_F(f) >= m^8.                                        (2)

No path between two marked vertices of one source tree can
contain such an edge: its source length is at most
`gamma m^4<m^8`. Removing all records of type (3) therefore
does not separate any two old marked vertices in the same
source tree. It may create extra unmarked components.

## 4. Cover, raw length, and exact gradient identities

For an original G ball of radius `D/(2gamma)`, every shortest
path is simple, has at most m edges, and uses only admissible
genuine edges. Its rounded length is at most

    m^4/(2gamma)+m <= m^4/gamma.

The private source cover therefore contains the ball in one
marked tree. Its artificial path cannot shorten any path at this
scale because every artificial edge has length m^8. By (2), all
those marked vertices remain together after filtering, and true-
null contraction preserves their physical images. The original
ball is still covered.

By (1), a quotient marked-tree path has original-real length at
most its source path length multiplied by delta. Its diameter
is at most gamma D. Occurrence multiplicity does not increase
under filtering or contraction. The quotient is a forest.

The registered edge map P sends each oriented retained real
occurrence to its chosen signed unit G edge and every null edge
to zero. It respects endpoint incidence, so the image of any
circulation is a G circulation. Define the exported gradient by
this map. For every edge/path vector z, exactly

    g_export^T z = g_G^T Pz.                              (3)

Raw physical length counts each selected real traversal with
its original ell, including repetitions; null traversals cost
zero. No cancellation is used in (1) or in this raw charge.

Choosing a different parallel representative can change the
individual exported gradient, but (3) remains exact because the
edge map and gradient change together. The HRG routing proof only
needs such a valid physical path map. In particular, for its
linear routing R, the circulation projection is `I-R B_G^T`,
which acts as the identity on G circulations. It does not require
the SNC's originally intended parallel-edge choice. All original
nonloop G edges remain available in E_graph, so parallel-edge
cycle directions are not discarded by this representative rule.

## 5. Updates even when the source forest topology does not change

Maintain an index of source F occurrences over each input slot,
and of source F edges by unordered pair of endpoint images.
For distinct u,v, the latter list has at most `2gamma-1` edges:
they lie in the forest induced on the two occurrence fibers.
The equal-image list is part of that one slot's true-null forest.

On EVERY parent G edge insertion, deletion, or price-lifetime
replacement at u,v, mark this pair dirty at this cover radius.
This is done even when its rounded price does not change, even
when it crosses the admissibility boundary, and even when the
source reports no forest topology change. The canonical
representative or its gradient/lifetime can change in all these
cases. Refresh every affected source occurrence over that pair.
All relevant G parallel edges can be inspected from the degree-
three endpoint adjacency, so selecting r_D costs O(1) local work
apart from dictionary operations.

Also mark the old and new endpoint images of every changed
source forest/map record. Source vertex IDs are augmented with
birth generations if the native implementation recycles names.
An actual image change is processed as old-record retirement and
fresh-record birth. Each changed source record therefore affects
only a constant number of slot fibers or endpoint pairs.

For the null quotient, all incident source F edges of a v-fiber
lie over v and its at most five private-graph neighbors. The
forest induced on these at most `6gamma` occurrence vertices
has O(gamma) edges. Thus a local scan of the fiber, its null
components, and its incident real candidates costs O(gamma),
or O(gamma^2) with conservative metadata maintenance. The source
never forces a global scan of all F edges to refresh one pair.

If q source logs are produced by one parent transaction, the
wrapper needs at most

    O((q+1) gamma^2 polylog m)

local work and explicit output logs. Since q has the source
amortized gamma bound, this is only a fixed local power of
gamma per parent update. Initialization visits the actual
source records in `m gamma^O(1)` work. These costs are absorbed
by the same local A in the master recurrence; no factor k is
put on recursive child updates or child forest logs.

### Deletion-first ordering

A parent edge operation and all its cover/quotient consequences
form one no-motion transaction.

1. Preserve the old registered real representatives, old input
   price data, source images and quotient endpoints. Register
   the parent endpoint pair as dirty before changing current
   private adjacency.
2. Submit the appropriate private rounded-edge changes to the
   source, and collect its explicit old-to-final forest/map/mark
   logs. A gradient-only change may leave that private topology
   untouched, but the explicit pair refresh is still required.
3. From the dirty fibers/pairs, remove old exported attachments
   and real records, propagating their full recursive retirement
   callbacks. Flush both signed and absolute motion before
   discarding any old selected-edge or endpoint metadata.
4. Using the FINAL current private input and source forest,
   choose r_D, rebuild the affected true-null quotients, and
   create fresh registered records and immutable maps. Install
   their attachments only after the old ones have been cut.
5. Finish all child logs, marked-root changes and pool changes,
   publish the settled export, and only then release old metadata
   and service queued refresh flags. Do not use an old answer
   path after these replacements.

No intermediate source state is required to admit a current
canonical representative for an old record: its old registered
choice remains available until retirement. Source input data may
change internally, but the wrapper retains the needed old logical
data and numerical-coordinate associations throughout this batch.

## 6. Slots, ghosts, and the scoped wrapper conclusion

The private backbone and native SNC vertex slots are fixed within
one local instance. Reserve and count enough local slots for its
bounded period. A client logical vertex lifetime must exist before
activation exposes its slot's occurrences. An unused slot exposes
nothing. After genuine incidences retire, suppress the remaining
null components of an inactive logical lifetime, while retaining
native slots and tombstone associations until the local instance
is discarded.

A quotient representative can retire logically without assuming
a native DeleteVertex operation. Downstream isolated slots or
internal null port trees may remain allocated. Count all of them
in the nominal size allowance. Their real path pools retire and
flush before their exported inactive images are suppressed; old
associations are checked before any retired mapping lookup.

At most m wrapper events occur in a local cover period before
the prescribed restart. Total source/quotient births and private
history are therefore `m gamma^O(1)`, counted in local A. A
capacity overflow is handled by the charged period/size restart
or suspends the branch. There is no master-S-sized padding and
no unlimited free ghost history.

Under the explicit source metric premise in Section 2, this
construction provides a flat quotient forest with ORIGINAL
integer real lengths, exact chosen-edge gradients, stable real
edge identities, cover radius `D/(2gamma)`, marked diameter
at most `gamma D`, and occurrence bound gamma. It uses only
the source's explicit vertex-map/forest logs, the current local
input adjacency, and local fixed-power overhead.

It therefore resolves the real-preimage identity ambiguity for
the length-preserving SNC wrapper without presuming that a
vertex-map-only theorem already emits stable parallel-edge IDs.
The metric domination premise is still essential and remains
an explicitly cited constructive source property.
