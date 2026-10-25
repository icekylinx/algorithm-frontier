# A legal-API reconstruction of the portal length-decrease layer

**Status: research proof draft, 24 October 2026.** This note isolates one
specific issue in the deterministic backend. Claim 5.16 of Chen, Kyng,
Liu, Meierhans and Probst Gutenberg decreases several portal-edge
lengths, whereas their Theorem 5.13 lists no length-decrease operation.
The construction below replaces those decreases by legal insertions of
parallel aliases. A controlled hierarchy and immutable endpoint origins
bound the cumulative master degrees and the number of expensive updates.
An additional inventory of ancestor targets makes the construction
robust to tree exchanges that retain off-tree edges.

This note supplies the portal layer. The current routing construction
combines it with `constant_degree_steiner_bridge.md` to control recursive
degree and physical occurrences, and with
`disconnected_routing_components.md` for arbitrary forest components.
The general-cycle reduction's cover/HRG primitives are imported only on
their stated degree-three inputs. This portal argument alone is not a
replacement for those primitives or for the separate lift proof.

## 1. Scope and the imported spanner API

The primary source is:

> L. Chen, R. Kyng, Y. P. Liu, S. Meierhans and M. Probst Gutenberg,
> *Almost-Linear Time Algorithms for Incremental Graphs: Cycle Detection,
> SCCs, s-t Shortest Path, and Minimum-Cost Flow*, arXiv:2311.18295v1,
> <https://arxiv.org/abs/2311.18295v1>.

We use its Theorem 5.13 exactly as stated. For an auxiliary graph with
positive lengths in a fixed aspect range, it supports:

* `InsertEdge`, provided the degree of each master, **ignoring all
  previous deletions and splits**, stays at most a declared bound Delta;
* `DeleteEdge`;
* `SplitVertex`, including the specified treatment of self-loops;
* `InsertVertex`.

Write rho for its stretch, explicit-path-length, and recourse factors,
enlarging it by constant factors if necessary, and let

    b = 1 + ceil(log_2(length aspect)).

Here the aspect range includes routed walks, whose lengths are at most
`(2m+1)` times the largest parent-edge length, and the fixed smallest
positive unit. It is not just the aspect ratio of individual parent
edges. At constant recursion depth with polynomial input aspect this
still gives `b=O(log M)` with parameter-dependent constants.

The relevant guarantees are:

    |E(H)| <= n_aux polylog(size * aspect),
    H membership changes <= rho (n_aux + q_bad) b,

where `q_bad` counts deletions, splits, and vertex insertions, but not
arbitrarily many legal edge insertions. Each auxiliary update costs
`Delta rho b` amortized time. Explicit embedding-path changes total at
most `rho Delta q_all b`, and each returned route has at most rho edge
records. Its weighted length is bounded as used by source Lemma 5.14.

The initial decomposition is the explicit weighted-forest construction
in `disconnected_routing_components.md`. It gives the properties of
the source's tree decomposition while separately accounting for
arbitrarily many small forest components; it does not import a false
`O(m/k)` bound on their total number. We also use the elementary
balanced two-boundary hierarchy proved in
`balanced_two_boundary_hierarchy.md`. The hierarchy is summarized
below so that the new counting argument is self-contained.

### Scoped conclusion

Consider one period containing at most `Q <= m/k` edits of a forest T
and an off-tree edge set, where m counts vertices and edges. Edge prices
are fixed during a lifetime; repricing means deletion followed by a new
lifetime. The endpoints of a tree edit are promoted before the edit.
The construction produces a graph on physical portals, with edge lifts
into the current original graph, such that:

1. every current fundamental tree cycle with at least two portals has
   a comparison circulation with the same gradient and at most twice
   its length;
2. every edge of the maintained graph has a valid current physical walk
   whose raw length is at most its stored length;
3. its sparsifier has `m A/k` size and receives only `(m/k+Q) A`
   ordinary vertex/edge changes;
4. the local work is `m A + Q k^2 A`.

Here A absorbs fixed powers of polylogarithms, rho, and the other local
subpolynomial factors. In the constant-depth backend, `A=M^{o(1)}` for
the outer size M. Crucially, the child edit bound has **no factor k**.

The comparison assertion only concerns off-tree edges whose endpoints
currently lie in one T component. Other retained aliases still have
valid lifts, and any cycles they help the child return are valid graph
cycles. Thus retaining off-tree edges across a tree exchange does not
invalidate this portal-layer statement.

## 2. Initial pieces, dormant components, and the hierarchy

At the period's beginning freeze the initial forest `T0`. Decompose its
large components into connected, edge-disjoint pieces with at most two
boundary portals and `O(k)` interior incidence volume. Initial portal
incidences are owned by root buckets, not charged repeatedly to all
adjacent pieces. The total number of initial active pieces and portals
is `O(m/k)`.

For a direct proof, assign each vertex weight one plus its old off-edge
endpoint count. A bottom-up threshold marking consumes at least k
disjoint weight units per mark; add only branch vertices of the marked
Steiner forest to make the portals branch-free. The unmarked components
have weight below k. There are O(m/k) two-boundary components, and
one-boundary hanging components are grouped at their common portal into
pieces of weight below 2k. Zero-boundary components remain dormant.
The full proof and all recursive-size counts are in
`disconnected_routing_components.md`.

Small T0 components of total incidence volume `O(k)` may have no portal.
Their hierarchies and old edge records are stored in the ordinary
`O(m polylog m)` initial metadata, but they create no auxiliary vertices
until a portal is actually requested. This distinction is necessary
when T has many small components. A component containing a vertex with
large old off-edge degree promotes that vertex initially and buckets
its incidences. The weighted decomposition applies to the remaining
interiors. Off-tree edges between different T components simply
contribute endpoint weights; they do not need to be tree edges.

For each initial piece, fix a constant-branching hierarchy. At a node
choose an interior-weight centroid. If it lies off the path between
the two old boundaries, also choose its projection onto that path.
Promote the projection first and then the centroid. The resulting
pieces have at most two boundaries. Hanging branches at one separator
are grouped into constantly many connected pieces of at most half the
old interior volume; the constant number of pieces involving old
boundaries are kept separately. A two-stage macro has the half-volume
property even if its first stage alone does not. The depth is

    h = O(log(k+2)).

This construction handles a high-degree star by grouping branches;
it does not create one auxiliary piece per leaf. A refinement at an
already present boundary is a virtual subdivision and need not create
a new portal.

The active pieces form an ancestor-closed frontier. To promote an
arbitrary interior vertex, refine its ancestor chain until it becomes
a boundary. This uses `O(h)` constant-branching refinements. Maintain
branch-freeness after each individual physical promotion, including
the two stages of a centroid/projection macro.

Newly inserted isolated vertices are initially dormant singleton
components. Before they participate in an edge edit they are promoted.
There are at most Q such births in a period.

## 3. Lazy ancestor targets and valid dangling prefixes

An old off-tree endpoint u has a finite target inventory. Initially its
targets are the at most two boundary portals of its initial piece. If
u is itself an initial portal, use only the fixed target u. A portal-free
piece initially gives its endpoints no targets.

Whenever an actual hierarchy separator s is promoted in a refinement
of a current piece C, create a target origin for s owning the old
endpoint IDs in the interior of C at the start of that refinement.
Each such endpoint acquires the target s. Endpoints already at fixed
physical portals need no new targets. Only actually promoted separators
create auxiliary origins; the precomputed future hierarchy creates none.

For a two-separator macro, perform its two stages consecutively and
give both separators the macro-parent's endpoint inventory, activating
each origin only after that separator is actually promoted. The
off-path centroid's origin may consequently own IDs in a side piece
whose first portal toward it is the projection separator. These extra
variants can be redundant and are harmless. This is a uniform
overinsertion convention, not a claim that the smaller intermediate
inventory necessarily fails. It avoids an ambiguity about
whether the centroid is an ancestor only of the intermediate child
that contains it. It adds only constantly many origins per macro;
one slot for each of its constantly many frontier children is enough.

Consequently an old endpoint has at most `h+2` targets. Every boundary
of its current frontier piece is one of those targets. The set of
*potential* future targets may be read from the fixed hierarchy for
degree accounting, but no graph vertices are allocated for inactive
targets.

For a target s of u, define

    p(u,s) = the first current portal on the FIXED T0 path from u to s.

If u is a portal this is u. This is deliberately a prefix of an
initial-tree path, not a current-tree path all the way to s: a later
tree cut may separate s from u.

### Prefix validity invariant

The path `T0[u,p(u,s)]` is a current dangling leg. It contains no portal
other than its final endpoint, apart from the zero-length case. No
deleted or repriced T0 edge lies on it. Indeed, both endpoints of every
such edited edge were promoted before that edit, so traversal from u
would meet one of those permanent portals before entering the edited
edge. A subsequently inserted tree edge also has two portal endpoints,
and therefore cannot appear inside a dangling leg.

As portals are added, each fixed-target leg only shortens. The target
s itself need not remain connected to u in current T. The surviving
prefix stops before any intervening cut. All physical edges inside
that prefix are unchanged T0 lifetimes.

Since current nonportal interiors still lie within the initial pieces,
the current first portal toward s is the unique boundary of the current
piece in that direction. For every current frontier piece and inherited
target origin, there is therefore one well-defined endpoint slot.

## 4. All target pairs, geometric aliases, and a fixed gradient gauge

For each old off-tree edge lifetime `e=(u,v)`, maintain every active
target pair `(s,t)` from its two endpoint inventories. There are at most
`O(h^2)` pairs. The corresponding variant is the actual current walk

    p(u,s) --T0--> u --e--> v --T0--> p(v,t).

The two legs may overlap after projection, but the stored denominator
charges the full literal walk. Distinct variants and aliases retain
distinct edge IDs, even when they have the same physical image.

Let r be the current raw length of this variant. At its birth insert
one alias of length

    lambda = 2^ceil(log_2 r),       r <= lambda < 2r.

Use a declared fixed positive dyadic unit valid for the **whole period**,
including future permitted insertions, when clearing scales. Do not
rescale using the minimum length of the currently present edges.
If a later promotion decreases the rounded value, insert the new
shorter alias and retain all older aliases. Do not insert intervening
unused buckets. A fixed pair has at most b aliases over the period.
Every older alias remains valid because its actual legs only shorten.

Thus an old edge has at most `O(h^2 b)` alias records. A true deletion
removes only that many records. There is no `DecreaseLength` call and
no deletion when merely shortening a route.

### Gauge and newly inserted tree edges

At the period's beginning choose a potential pi on every T0 component
so that

    bar_g(e) = g(e) + pi(tail(e)) - pi(head(e)) = 0

on every initial tree edge. Keep pi fixed throughout the period, and
give new isolated vertices potential zero. Every alias of an unchanged
off-tree edge has the immutable gradient `bar_g(e)`, because both of
its current dangling legs consist of unchanged zero-gradient T0
edges. The gradient of a newly inserted tree edge is its **actual**
residual `bar_g(e)`; it is not silently set to zero. Such an edge joins
portals directly. Existing compressed T0 path edges have gradient zero.
Potential terms telescope on every returned circulation.

An input gradient or length replacement retires the old edge lifetime
and inserts a new one after promoting its endpoints. It therefore
never changes the stored numerical label of an old auxiliary edge.

### Tree-path edges

For each maximal current path between consecutive portals, maintain its
compressed tree-path edge with the actual path length and residual
gradient. Place it in an isolated auxiliary component with two fresh
root copies. A spanner must retain that bridge, and identification of
portal copies later gives precisely the desired tree-path edge. Each
promotion changes only constantly many such edges. A tree edit, after
endpoint promotion, changes a direct portal-to-portal edge. Retire the
old tree-path lifetime rather than retaining an invalid historical
path.

This accounts for `O(m/k+Qh)` additional vertex/edge lifetimes. Their
masters have constant cumulative degree.

## 5. Why the target inventory preserves current comparisons

Let e have endpoints in one current T component, and suppose its
fundamental path has at least two portals. Its first portal p from u
is a boundary of u's current frontier piece, or is u itself. Its last
portal q is similarly available at v. Both are active endpoint targets.

The variant indexed by those targets has exactly the two end segments
of the current fundamental cycle. The intervening segment is a chain
of current compressed tree-path edges. The latest alias has length
less than twice its current end-segment-plus-e length; the middle
segment has its actual length. Hence the resulting circulation has
the original gradient and total stored length at most twice the
original fundamental-cycle length. No cancelling detour is used in
this particular comparison, although other stored variants may have
detours.

This argument remains valid after a tree exchange. All newly inserted
tree edges have portal endpoints, so a current fundamental path can
change its route through the portal skeleton while its two local
nonportal end pieces remain valid. Every possible boundary of those
pieces belongs to the ancestor inventory. A single fixed target from
the old fundamental path would not give this guarantee.

### Dormant components and newly connected fundamental cycles

Before a tree link, promote both endpoints, including the necessary
hierarchy ancestors. If an endpoint lies in a previously portal-free
small component, scan its `O(k)` old endpoint inventory and activate
the newly available targets and pairs. If an old off-tree edge crosses
two T components and becomes internal after the link, its new
fundamental path contains the two link-endpoint portals. At each end,
the correct first/last boundary target is now present. Thus that edge
already has the needed variant, or obtains it during one of these
local activation scans. A global scan of all formerly crossing
off-tree edges is unnecessary.

An edge whose other endpoint remains in a dormant component has no
routed pair yet. It cannot already require a two-portal comparison
through that component without a prior tree edit having activated the
appropriate boundary. It remains an ordinary edge record until both
target sets are nonempty.

## 6. Immutable origin slots and legal split operations

Each target origin owns the old endpoint IDs that were interior to its
birth piece. It has at most `O(k)` such IDs. Its descendants consist of
one slot per current descendant piece, plus fixed root slots for
preimage vertices that have become portals.

All variants having the same endpoint ID and own target use this same
current origin slot, regardless of their partner target. In fact all
IDs of that origin within one current piece share its slot. There is
no separate vertex for every target pair or every edge.

When a piece is refined, partition each inherited slot's inventory
among the constantly many child pieces and newly exposed root
vertices. Use `SplitVertex` to move these inventories into fresh slots.
Keep the old slot for at most one child whose physical portal image
is unchanged; otherwise leave it isolated. Every slot's physical
image is immutable throughout its lifetime. No merge or image-renaming
operation is used.

For a self-loop, if both endpoint inventories move to the same new
slot, use the API's ordinary moved-edge set; if only one endpoint
moves, use its crossing-self-loop set. If the two endpoints eventually
move to different new slots, perform the two corresponding splits
sequentially. These are precisely the legal operations of Theorem 5.13.

Only origins born on the current piece's hierarchy ancestor chain,
plus its at most two initial boundary origins, can occur in that piece.
There are `O(h)` such origins. A refinement therefore needs `O(h)`
splits or isolated vertex births; a requested promotion needs `O(h^2)`.
New roots split from an old origin retain that origin's master
ancestry. They are not incorrectly counted as fresh independent
degree budgets.

Initial physical-portal incidences are partitioned into root buckets
of at most k old endpoint IDs, using `O(m/k)` initial buckets. A
genuinely new off-tree edge, whose endpoints are promoted before its
birth, receives two **fresh singleton root masters**. Repeated births
at the same physical portal never reuse one old master. There are at
most Q such lifetimes per period. Deleted IDs are not recycled.

Reserved empty slots may remain while they own potential endpoint
IDs. A completely retired slot remains an isolated graph vertex until
rebuild. No unsupported `DeleteVertex` operation is needed, and all
these vertices are included in the birth count below.

### Cumulative master degree

Fix an old origin. It owns `O(k)` endpoint IDs. Each such ID has at most
`O(h)` potential partner targets over the entire fixed hierarchy,
including targets that are still dormant. Each own-target/partner-
target pair creates at most b geometric aliases. Therefore, even when
all deletions and all splits are ignored,

    deg_master <= O(k h b).

This is a bound on the sum of insertion lifetimes, not merely on a
current degree. Initial root buckets obey the same bound. A true new
singleton master has an even smaller bound because its preimage is
already a permanent portal. One may declare a larger constant multiple
of `k h b` uniformly. Thus every alias insertion satisfies the stated
Theorem 5.13 precondition.

## 7. Size, local work, and child recourse

There are initially `O(m/k)` auxiliary slots. Over Q edits there are
`O(Qh)` refinements and `O(Qh^2)` origin-slot/root births. Consequently,
including all retired isolated vertices,

    n_aux = O(m/k + Q h^2).

An actual old edge death removes `O(h^2 b)` aliases. Refinements and
root births contribute only polylogarithmically many other expensive
API calls per parent edit. Tree-path lifetimes were counted above.
Hence

    q_bad = Q polylog(m * aspect).

The number of ordinary alias insertions is larger: a promotion scans
the `O(k)` old endpoint inventory of its affected initial piece and
processes the relevant target pairs and rounded buckets. Over one
parent edit this is `k polylog(m * aspect)` edge insertions and local
record operations. These insertions are legal but do not individually
enter the spanner's low-recourse bound. Multiplying their total by the
API's `Delta rho b` local update bound gives

    local work <= m A + Q k^2 A.

Initialize scores and explicit route records in `m A` time, allowing a
full expansion of the bounded-length spanner routes if required.

The spanner has `m A/k` size because `Q<=m/k`. Its total number of H
membership births and deaths is

    B_H <= (m/k + Q) A.

### Expanding projected endpoint changes into ordinary child edits

An auxiliary split may leave an edge's alias ID in H while changing its
physical portal endpoint. Such a change must be sent to a child that
supports only edge insertion/deletion; it is not a free vertex rename.

Index H membership by the persistent alias edge ID. During a refinement
enumerate only the affected alias inventories, already covered by the
local `k polylog` work. For each affected alias currently in H, compare
its old and new physical endpoints. Emit an ordinary child deletion
and insertion only if an endpoint actually changes. No scan of all H
edges, and no scan of all edges incident to a high-degree physical
portal, is used.

Perform this with a deletion-first transaction. Before an affected
retained edge changes its physical image, snapshot its old endpoint and
lift metadata and retire its old projected child record, including the
required old-lift flush. Then perform the auxiliary split and reconcile
the source's H membership changes with this local overlay. Reinsert the
moving edge only if it belongs to the resulting H. An already retired
record is not deleted a second time when the source also reports its
membership removal. Other H membership changes are forwarded normally.
The old metadata remains immutable until all required retirements have
finished. The parent is queried only after this transaction settles.

For a fixed old endpoint-target record, its containing piece only
descends its fixed hierarchy. Its physical image can therefore change
at most `O(h)` times during the **entire period**. Each alias endpoint
inherits this bound. In particular, during any one H membership
lifetime it changes at most `O(h)` times. Sum this bound over membership
lifetimes, not over parent splits:

    extra child endpoint edits <= O(h) B_H <= (m/k+Q) A.

True-birth root aliases never move. Tree-path aliases have fixed
endpoints for their lifetimes and are deleted/recreated as already
counted. Auxiliary vertex copies are identified only in the projected
child graph, whose vertices are physical portals; separate auxiliary
origins never require a child merge operation.

This is the main reason an `O(k)` affected-edge scan is compatible with
low recursive recourse. The scan is local scalar/bookkeeping work.
Only retained edge membership and bounded geometric endpoint motion
produce recursive graph edits.

## 8. Explicit routes, correction scores, and real loops

Identification of auxiliary copies need not preserve all auxiliary
distances. It suffices that every alias has its own explicit
auxiliary-endpoint route in H. After identification that route is a
walk between the correct physical portals, with the same edge labels
and no greater length. This is the per-edge property used in the
spanner decomposition argument.

Every existing auxiliary edge's gradient and length are immutable.
Thus a correction score changes only when the edge is born/deleted or
its explicit spanner route changes. Instrument the source's explicit
route-change transcript. Recompute each affected numerator and raw
route sum in `O(rho)` work and update a comparison heap. By Theorem
5.13 the total is bounded by

    O(rho^2 Delta q_all b) <= m A + Q k^2 A.

No new inverse-route-incidence structure is needed for numerical
repricing, because there is no numerical repricing of retained alias
records. A physical endpoint move alone does not change their labels.
Its effect on legal auxiliary routes is already in that transcript.

For an alias e outside H use the actual correction walk
`e - Pi(e)` and the denominator `lambda_e + length(Pi(e))`. The
standard averaging proof underlying source Lemma 5.14 applies to
these raw sums. The child circulation and one correction together
account for the comparison numerator, with only a constant multiple
of rho loss. Cancellation is never used to shrink the certificate's
denominator. One can instead perform the small selected-correction
simple-cycle extraction described in the main backend note.

A projected alias with equal portal endpoints is a **real input loop**
and may have nonzero gradient. It is not a null forest connector.
Preserve its edge ID and raw certificate. If the recursive child
interface omits real loops, maintain the projected H loops' best score
in a direct heap and pass only nonloop H edges to that child; taking the better of
the direct-loop candidate and the child candidate loses no quality.
Transitions between loop and nonloop status are charged to the same
bounded endpoint-motion count. True null forest connectors have zero
gradient and zero physical charge and remain a distinct record type.

## 9. Local fundamental cycles without a global scan

Keep one additional disjoint copy of current T for local certificates.
Initialize a heap of all old off-tree edges whose endpoints lie in
one T component and whose fundamental path contains fewer than two
portals. This includes both zero-portal and one-portal cycles. Store
their exact simple-cycle numerator and length.

Every promotion changes the local/routed status only of edges with an
endpoint in its refined initial piece. To see this, if a new portal s
is internal to an off-edge's tree path and neither endpoint is in that
piece, the path must already enter and leave the piece through its two
old boundary portals. It was already routed. For a zero- or one-boundary
piece, a simple path cannot enter and leave through distinct old
boundaries unless an endpoint is inside. Hence the `O(k)` endpoint
inventory scan, with polylogarithmic target bookkeeping, finds every
local key that must be removed or refreshed.

Before a tree-edge deletion or repricing, promote its two endpoints.
Any currently local fundamental cycle that could use that edge now
has at least two portals and is removed by the preceding local scans.
All remaining local cycles keep their paths and keys. A new tree link
cannot change a path that already existed within one old component.
Any newly created fundamental path between previously distinct
components uses the new edge's two portal endpoints and is routed,
not a new local key. Apply this reasoning to each elementary tree edit
in a batched exchange; retaining crossing off-tree edges is harmless.

An off-tree insertion/deletion updates its own record. A new off-tree
edge has promoted endpoints and is therefore routed unless it is a
real self-loop, which is handled directly. These rules give an exact
local heap without an unstated arbitrary-tree locality assumption.

## 10. Alternative dangling-subtree lift and its import boundaries

This section records the source-style dangling-subtree lift for comparison.
The current geometric Steiner route uses Sections 1--9 of this note and
the input-edge path pools in `constant_degree_steiner_bridge.md` instead.
Its recursive occurrence and retirement bounds do not depend on the
alternative whole-dangling-subtree maintenance described below. Keeping
the two constructions separate avoids combining incompatible lift costs.

Every alias endpoint leg is inside the current dangling subtree of
its physical portal. Therefore the static lift of source Definition
5.6 applies to every variant: attach one dangling subtree to each
current child-forest vertex occurrence and lift an alias by its
central original edge between the appropriate two dangling copies.
Contracting those copies gives exactly the child forest. Branch-
freeness still bounds a physical vertex by at most two portal dangling
subtrees. The alias variant count does not multiply this vertex
congestion bound.

An arbitrary returned alias edge uses its two dangling legs and one
central input edge; a returned forest path lifts to the corresponding
path in the expanded forest, with backtracking deleted if necessary.
The stored certificate continues to upper-bound its raw traversal.
Real portal loops retain their central-edge identity, as explained
above. Tree-path edges use the corresponding current tree path.

The dynamic lift uses the occurrence pools explicitly allocated by
source Algorithm 1, lines 13--15 and 32, and its forest-change log
interface. The initialization allocates the declared number Gamma of
dangling copies for each portal. An occurrence born at an old high-degree
portal takes a preexisting copy; it does not rebuild the portal's whole
dangling tree.

For each physical promotion use a no-parent-query transaction. Preserve
the old lift metadata while the auxiliary edits and corresponding child
edits run, collecting their explicit forest logs. Finalize by retiring
the affected old connecting records, editing the `O(k)` removed regions
in the old dangling pools, preparing the new portal's `O(k)` dangling
region in its Gamma copies, and installing the final child connections.
Every connection incident to a removed region is an alias whose
endpoint moved, or a tree-path edge that was replaced; both already
have replaced child input lifetimes. Null connectors touch only roots.
Unchanged connections are outside the removed regions. Temporary child
records born and removed within the transaction never receive a parent
cycle update and may be omitted after their logs have been reconciled.
Finalize promotions separately, so old/new pool overlap is only a
constant factor at one time. The cost is `O(k Gamma polylog m)` plus
the child forest-log volume per promotion, already within the local
bound after the hierarchy factor is included.

During a partially processed promotion an old alias may still use its
old T0 prefix while a moved alias uses its new shorter prefix. All such
walks remain physically valid: the actual tree edit happens only after
the endpoint promotions finish. The settled prefix and branch-free
statements above apply before the next parent query. Retire old records
and flush their accumulated motion before invalidating their metadata.

This uses the explicit occurrence-pool and forest-log component of
source Lemma 5.9 and the separately audited stable-lifetime wrapper.
It does not infer dynamic occurrence maintenance merely from a
top-level min-ratio guarantee, or introduce a black-box image-renaming
operation.

At a fixed recursion depth, an outer reduction factor `k=M^eta` and
local factor `A=M^{o(1)}` give child size `m A/k`, local work `k^2 A`
per parent edit, and only A recursive edits per parent edit, with the
usual `m/k` initialization charge. The exact base uses at most `k^3`
times polylogarithmic work. For constant depth `D=O(1/eta)`, products
of local A factors remain `A^{O(D)}=M^{o(1)}`; the local k powers are
additive work and do not become a k factor at every recursive level.
The loose bound `k^{10} A^{O(D)}` is more than sufficient for the
previous fixed-parameter matching composition.

What is resolved here is the concrete length-decrease/master-degree/
auxiliary-split/child-endpoint-recourse layer. The construction still
uses the published dynamic spanner as a theorem, the static weighted
tree decomposition, and the flat-lift component. The fully independent
general-cycle degree-normalization bridge and the surrounding OAI
numerical analysis remain distinct imported proof dependencies.
