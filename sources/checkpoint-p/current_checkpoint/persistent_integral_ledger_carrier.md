# Persistent integral carrier forests and canonical assignments

**Status.** Candidate replacement for the epoch maintenance layer. The
transportation, persistence, and assignment constructions below are explicit.
Their integration uses the OAI integral-ledger interface and its local
projection theorem, plus the independently audited deterministic numerical
backend. This note records the complete proposed interface rather than
silently treating a private rounded vector as the current ledger. The
top numerical ledger is never normalized.

## 1. The change of representation

For every integral level `j>=1`, store its **actual** allocation vector in
a bipartite carrier forest `F_j`. A carrier edge is a genuine current
row/bin incidence. Every positive allocation belongs to the carrier;
a carrier may also contain zero-allocation incidences. Every incidence
outside the carrier has allocation zero.

The other ledger fields, namely column residuals `y`, debts `p`, their
indices, and weights, retain their ordinary persistent point-map
representation. An allocation query is a carrier-edge membership query
followed, when present, by an edge-value query in the dynamic forest.

The carrier is the representation of the actual integral ledger. There
is no separate current integral vector whose sparse increments are
blindly applied to a different rounded vector. In particular, the
negative-coordinate example for such a private-shadow update does not
apply to this interface.

A transportation cycle cancellation changes allocations but preserves
each row sum and each bin load. It consequently preserves every `y`,
every debt `p`, and each inequality `y+p>=c_j w`. All values remain
nonnegative integral and every coordinate remains at most `L`.

The source's ledger invariant in Section 03 requires precisely these
properties. Its top objective depends only on level zero. Its local
projection theorem in Section 04 assumes a parent satisfying the
one-unit stronger floor and point access/sparse updates; it does not
assume coordinatewise closeness to another level. Its reset/debt
accounting uses the debt totals, structural tick increments, and the
floors. Thus margin-preserving normalization of integral levels does
not alter any of those premises or charged quantities.

## 2. Sparse-batch normalization with constant topology recourse

Suppose a carrier represents a nonnegative allocation `x`. A legal
batch supplies final values on `q` incidence coordinates, possibly
together with incidence births, deaths and endpoint retargetings. Let
the resulting nonnegative vector be `x'`. The batch itself may change
row/column margins as prescribed by the structural or projection
operation.

Apply the **whole** batch before starting cycle cancellation. In
particular, do not normalize after one coordinate write and then
interpret later writes as final values from the old vector: an early
cancellation might have changed a later coordinate. Repeated writes
to one incidence can first be coalesced, and all required old values
are read from the prescribed input version.

Cut carrier edges whose physical incidence disappears or whose
endpoint is retargeted. An edge retargeted to a new endpoint is a new
insertion attempt, with the retained allocation as its initial value.
Unaffected carrier edges, including zero edges, remain. Apply all
changed values to the surviving carrier edges. Outside this forest,
only `O(q)` positive incidences can exist: these are changed/born/
retargeted coordinates listed in the batch. Keep their values in a
temporary dictionary while normalization is in progress.

Process those positive off-carrier incidences one at a time. For
`e=(r,d)`:

* If its endpoints are in distinct carrier components, link `e`.
* Otherwise expose the unique carrier path from row `r` to bin `d`.
  Orient every incidence permanently from its row to its bin. Let
  `theta` be the minimum current value among path edges agreeing
  with traversal from `r` to `d`. This class is nonempty because
  the first path edge leaves a row.
* Add `theta` to `e`, subtract it from agreeing path edges, and add
  it to disagreeing path edges. This is a transportation cycle
  circulation, so all row and column margins are unchanged.
* Choose **one** agreeing edge attaining the minimum, cut it, and
  link `e`. The cut edge now has value zero. Leave all other zero
  edges in the carrier.

The minimum is allowed to be zero. In that case the operation merely
replaces a zero carrier edge by the positive new incidence. In every
case the new edge remains positive, and after one cut its endpoints
are disconnected, so linking it preserves acyclicity.

After processing all listed incidences, the carrier contains the
entire positive support. Each insertion attempt causes at most one
path operation, one cut and one link. Therefore the number of
topology changes and path operations is `O(q)`, even if a path
circulation simultaneously drives many coordinates to zero.

The pending list contains distinct incidence IDs that are outside
the carrier after the complete batch. An earlier pivot touches only
current carrier edges and its own processed pending edge. Thus it
cannot change an unprocessed pending entry. An already processed
edge may later be cut when its value reaches zero, but it is not
processed a second time. This establishes the required compatibility
between stored pending values and subsequent path cancellations.

This differs slightly from the static forest-support routine that
deletes every zero edge. Retaining unused zero edges is precisely
what gives a per-batch topology bound without enumerating a long
zero path. It is compatible with the balance theorem in Section 4.

Parallel physical incidences have distinct edge identifiers. A
parallel pair forms a legitimate two-edge transportation cycle;
the same operation removes one zero edge. A carrier forest cannot
contain two parallel edges at once, so its row neighbors are
distinct even when the physical incidence graph is a multigraph.

## 3. Worst-case dynamic trees and full persistence

Use a deterministic **worst-case** dynamic-tree implementation, not
an amortized splay implementation whose potential could be reused
by repeatedly branching from the same old version.

A suitable primary reference is Alstrup, Holm, de Lichtenberg and
Thorup, *Maintaining Information in Fully-Dynamic Trees with Top
Trees*, arXiv:cs/0310065v2 / ACM Transactions on Algorithms 2005:

<https://arxiv.org/pdf/cs/0310065>.

Theorem 1 gives logarithmically many local cluster changes for link,
cut and expose. Theorems 2–3 give path extrema and lazy path addition.
Section 3.3 gives ancestor/jump queries for arbitrary roots; Section
4 explicitly explains recovering a parent from the first edge of a
root path and maintaining component minima. The topology-tree
implementation supplies worst-case bounds and supports arbitrary
vertex degrees through its standard reduction.

The standard degree-reduction gadget is an internal implementation
device. Its connector edges have zero original-edge count and are
excluded from allocation minima and signed allocation additions. A
parent or first-edge query skips these connectors and returns the first
genuine carrier incidence. Component bin minima likewise count only
original bin records. Thus a high-degree implementation does not change
the carrier's combinatorial root, path, or allocation semantics.

For the signed transportation operation, each oriented path cluster
stores two minima and minimizing edge IDs: edges agreeing with its
boundary-to-boundary orientation and edges disagreeing. Reversing
that orientation swaps the two fields. A concatenation combines the
corresponding classes after accounting for child orientation. Two
lazy addition tags support distinct additions to the two classes.
The desired circulation uses additions `-theta,+theta`. These are
constant-size cluster summaries with constant-time join/split rules,
so the worst-case dynamic-tree bound is unchanged.

If the implementation uses internal ternarization connectors to handle
large vertex degree, those connectors are not allocation coordinates.
Exclude them from both signed minima and from allocation additions.
Give each genuine carrier incidence unit counting length and each
internal connector zero counting length when locating the first
original edge on a root path. Thus a parent/jump query returns a real
row/bin incidence rather than an internal implementation connector.

Also store the minimum ID of a bin in each carrier component. Row
IDs are excluded from this minimum. In a completed carrier every
component containing a row contains a bin, because every row has
positive total allocation `L`; an isolated bin is handled directly.
The canonical carrier root is this minimum bin. A first-edge/jump
query toward it gives a vertex's parent incidence. No physical
reroot traversal is needed. During an unfinished batch an isolated
row may temporarily have component minimum infinity; no canonical
assignment query is made against that unfinished version.

### An explicit persistence wrapper

Full persistence does not require an additional specialized dynamic
forest theorem. Simulate the worst-case dynamic-tree algorithm's
random-access memory in a persistent balanced dictionary

    address -> word.

Every memory read is a dictionary lookup. Every write path-copies
the dictionary and returns its new root. Allocation uses fresh global
addresses. A version of the whole dynamic-tree structure is one
dictionary root, so cloning an old version is constant time. This
works for arbitrary pointer fan-in: pointers are simply addresses
stored as words.

If an ordinary dynamic-tree operation uses `O(polylog N)` worst-case
word operations, its persistent simulation uses `O(polylog N)`
time and new space, with one additional logarithmic factor. The
number of addresses is polynomial in the guarded execution length,
so its address length is `O(log N)` for fixed algorithm parameters.
Branches cannot repeat uncharged amortized work because the
underlying operation already has a worst-case bound.

The source keeps only a fixed number of live ledger levels, but the
proof does not rely on that to justify persistence. Keeping every
created persistent node uses no more than total running time; old
versions can optionally be reclaimed. Allocation values and all
other integer fields have polynomial magnitude. This is an ordinary
word-RAM implementation with exact integer arithmetic.

A dynamic-tree query may modify auxiliary cluster representation
even when the logical forest and its edge values are unchanged.
For a frozen-version query, perform those representation changes in
a temporary persistent branch and discard its root after reading
the answer, or retain the resulting logically equivalent version.
The worst-case bound pays for this work on every query. It does not
rely on reusing splay potential across discarded query versions.

## 4. Balance with zero carrier edges

At a settled bottom ledger, every bin satisfies `load(d)<=L-w_d<L`.
Every row therefore has at least two **positive** incidences: a
single positive coordinate would equal `L` and violate that bin's
capacity. Because every physical row has degree at most three, its
carrier degree is either two or three, even though one carrier
incidence might have value zero.

Root every bipartite carrier tree at its canonical bin. For a
degree-two row, retain both incidences. For a degree-three row,
delete its parent incidence and retain its two child incidences.
Suppress the retained degree-two row vertices to get a selected
bin forest `T` with exactly one row-labelled edge per row.

Every selected component has either a bin top, or a unique
degree-three row at its top. All other internal rows keep their
entire allocation inside the component. A top degree-three row
can send only its parent allocation outside. That amount is less
than `L`: at least one of its two retained child incidences is
positive, since the row has at least two positive incidences in
total.

For a component with bin set `C`, let `out` be this one possible
outgoing allocation and `in>=0` the incoming allocations from
external rows. Its internal rows number `|C|-1`, and hence

    load(C)=L(|C|-1)-out+in,
    w(C)<=L+out-in<2L.

Integral weights give `w(C)<=2L-1`. The physical carrier of a
selected tree has `2w(C)-1<4L` vertices, including its internal
row vertices. Thus each selected tree can be enumerated in
`O(L polylog N)` time by physical-incidence traversal and carrier
membership/parent queries.

No selected forest needs to be explicitly rewritten when a carrier
path changes orientation. The following canonical injection makes
the same representation available through point queries.

## 5. Canonical injection and its inverse

For each carrier row `r`, compute its parent bin and its one or two
child bins.

* If the row has carrier degree two, assign it to its sole child.
* If it has carrier degree three, assign it to a fixed deterministic
  choice of its two children, for example the child incidence with
  smaller physical edge ID.

Every row is assigned to a genuine physical neighbor. A bin can
receive an assignment only from its carrier parent row, and that
parent is unique, so this covers all rows injectively.

For an inverse query at a bin `d`, first query its carrier parent.
If `d` is the carrier root, it is free. Otherwise its parent is a
row `r`: `d` is assigned precisely when `r`'s rule selects `d`, and
then the inverse answer is `r`; otherwise `d` is free. No child row
of `d` can be assigned to `d`, since every row is assigned downward
to one of its own children.

This assignment is exactly a rooted orientation of the selected
forest. A bin-top component is rooted at its top bin. A component
whose top is a degree-three row is rooted at that row's unchosen
child; the top row is assigned to its other child, and every lower
degree-two row is assigned downward. There is therefore one free
bin in every selected tree.

Both forward and inverse queries use a constant number of dynamic
tree operations and at most three incidence examinations. All
assignment incidence witnesses are retained explicitly in the
answer. This representation does not promise a short explicit list
of assignments changed by a carrier reroot; it does not need one.

Store, within the versioned carrier memory, each row's full list of at
most three physical incidence IDs (including zero noncarrier choices),
their carrier membership, vertex type/root-minimum labels, abstract
endpoints, and original physical edge/contact witnesses. Version the
bin adjacency dictionary as well for any enumeration on a stored
version. Each listed topology edit changes only constantly many such
records, and each carrier link or cut changes only a constant number
of carrier-membership records.
Thus an old canonical query reads its old carrier degree and old
endpoint records, not a current physical-neighborhood array that
may already have been changed. A current full physical row-neighborhood
query remains the ordinary source operation; a query on an old version
uses that version's full list. Deleting a zero noncarrier incidence can
change joint freeability without changing the allocation or carrier,
so versioning only carrier lists would not support old pair queries.
Vertex/row lifetimes
use distinct identifiers, so a later physical vertex reappearance
cannot overwrite an old version's identity.

## 6. Freeze the assignment oracle during one transaction

Before a structural event, retain the current bottom-carrier
version as a frozen assignment oracle. All assignment queries for
that event, its preserved-ledger edits, its projection, and a
possible peel refer to this frozen oracle plus a sparse overlay.
Do not switch to a newly normalized carrier midway through that
transaction.

The overlay implements the exact same assignment edits as the
source event:

* An expansion adds its new row assigned to its new singleton bin.
* A tight contraction saves the captive-row assignments, removes
  those rows, and retargets the at most one entering exterior
  assignment to the new bin. Unchanged rows retain their assigned
  physical incidences; bin identities are translated by the
  contraction map.
* A successful pair query explicitly orients its two involved
  selected trees toward the two queried bins. Their total physical
  size is `O(L)`, so its final forward/inverse overrides can be
  written in `O(L polylog N)` work. The gain immediately removes
  the two freed bins using this injection.
* A projection peel removes the rows assigned to its bin set using
  the same current overlay. Every surviving assignment remains
  valid.

The old carrier's endpoint records remain available in its retained
persistent version even after the current physical graph changes.
Queries at unchanged live objects use that old version; the
overlay/identity map handles new, contracted and removed objects.
No deleted old endpoint is silently treated as a current valid
assignment.

After the event and its projection have produced a settled bottom
ledger, discard the transient assignment overlay and commit the
canonical injection of the new bottom carrier. That is a valid
row-covering injection of the current graph. Replacing one such
injection by another preserves the represented matching
cardinality. The ledgers and the top objective are attached to
physical row/bin incidences and do not require repricing on this
change of injection.

Factor-critical bins already permit arbitrary prescribed exposure
vertices. A contraction record saves its captive-row assignments at
creation; later outer injection changes do not edit that saved
record. Erased-bin and phase-boundary materialization use the
current assignment oracle and the existing exposure records. Their
cost remains charged to erased physical volume or to one full
phase scan.

## 7. Structural and projection updates to every carrier

Every retained integral level receives the source's structural
allocation batch separately, then the normalization of Section 2.
The number of levels is fixed by the chosen numerical parameters.

At a contraction keep the largest old bin's representative. Retarget
only incidences belonging to moved smaller-bin members and swallowed
row vertices, exactly as in the source implementation. Cut any
affected carrier edge before its endpoint changes and reinsert its
retained positive allocation afterward. Do not scan the unchanged
large representative's incident list. Any cycles caused by identifying
old bin vertices are encountered when these changed incidences are
reinserted, and Section 2 removes them. Zero incidences created by
newly exposed physical contacts need not enter the carrier.

The source's small-to-large physical-volume accounting bounds these
incidence touches. Deletions scan removed bins, their assigned rows
and their affected incidences; expansions introduce constant physical
volume. The carrier normalization adds only a polylogarithmic factor
per already charged touch.

At a reset `j>1`, clone the **current normalized** parent `j-1`
version. Freeze that input version throughout ALL threshold tests,
lock changes, final-flow recovery, and residual-cut extraction for this
projection. Its allocation capacities are read from that same version.
The locks and logarithmic coordinates belong to the separate temporary
exchange-flow engine; carrier pivots are never interleaved with its
tests on the frozen parent. Source Section 04, "Recovering the exact flow and the full
peel", constructs a final region of `O(P+1)` size. The integral
flow on that region explicitly supplies all allocation changes;
the full peel has weight `O(P)`. The order is: apply the whole
exchange-flow batch; delete the returned peel bins and their assigned
rows, including the exterior loads freed by those row deletions;
normalize the resulting child; publish its assignment oracle only
after every ledger's transaction is complete. This order directly
matches the source's flow-and-restriction interface. In fact the
residual set has `load(R)=L|A(R)|`; its captive rows already contribute
that full load, so nonnegative margin-preserving circulation cannot
reactivate incoming allocations from noncaptives. No such extra
claim is needed by the stated order. The normalized final child
preserves exactly the already restricted row/column margins needed
by the source proof. If `P=0` and no allocation change is needed,
cloning alone suffices.

The preserved coarser versions receive their own preserving
deletions and normalization. All deeper fresh levels share the new
child's persistent roots, as in the source. At `j=1`, the source
already pays for a global integral flow; constructing and
normalizing its carrier takes only an additional near-linear scan.

Thus a reset copying a very different parent allocation does not
require scanning its difference from the former bottom allocation.
It copies the parent's whole persistent representation by one root
reference. Subsequent modifications are local in the source's
`O(P)` sense, even though an individual transportation path
cancellation can change many coordinates implicitly.

## 8. Pair actions and the resulting structural accounting

Use the deterministic output-sensitive tight-set detector for a
bin/bin contact. If it returns a tight witness, the contraction
charges are unchanged.

If the pair is jointly freeable, enumerate its first selected tree.
If the two bins already lie in distinct selected trees, enumerate
both and orient them appropriately. Otherwise use the static
pruning/exchange construction on the first tree: every internal
exchange stays inside it, and only the final link reaches a second
original selected tree. Enumerate that second tree when needed.
All physical row alternatives are available during the local scan.
The two trees have total physical size `O(L)`, so preprocessing,
the exchange chain, and the final assignment overlay cost
`O(L polylog N)`.

For precision, a selected-tree traversal scans the physical incidences
of each visited bin, then tests an adjacent row's selected pair using
its at-most-three versioned carrier incidences and its parent query.
Thus the scan is charged to the total physical weight of visited
bins. Only selected edges are followed to a new bin. Pruning the
first tree treats every third-neighbor outside it as already outside;
it does not scan that outside bin's interior. A tight set is connected
in every selected forest, since its `|X|-1` captive rows already
supply a spanning tree on `X`. Consequently every tight set meeting
the first tree lies wholly inside it, and pruning this tree alone
has the correct global tight-block meaning. At most `2L-1` row edges
can be removed, so the local parallel-round depth is `O(L)` without
any global preprocessing premise.

There are `O_a(N/L)` gain events in a phase. Thus gain pair work is
`O_a(N polylog N)`. Tight-contraction work remains output-sensitive
and is charged as in the source. Integral-ledger normalization is
charged to the source's sparse structural/projection record count,
times a polylogarithmic persistence factor. It does not introduce
an epoch term `N^2/(bL)+Nb`.

The provisional conclusion is that, **if every interface above is
accepted**, the structural replacement has near-linear overhead
relative to the existing deterministic numerical/projection phase.
For the fixed-parameter backend this would give a deterministic
general-gap phase with time `N^(1+delta)` for arbitrarily small
fixed positive `delta`, rather than `N sqrt(K)` structural work.
The complete arbitrary-general-graph maximum-matching composition
and its numerical dependency audit belong in the integrated theorem.

## 9. Distinctions from the failed shortcuts

1. This does not apply sparse changes from one allocation vector
   to a different private shadow. The normalized vector is the
   actual integral ledger read by the next projection.
2. This does not force a pair-freeing injection to arise from a
   feasible transportation basis. The temporary pair injection is
   consumed by the immediate gain; the next settled canonical
   injection comes from the repaired ledger.
3. This does not delete whole small selected trees. Only the source
   gain bins and source peel set are deleted, so the quadratic
   top-debt obstruction to bulk deletion is avoided.
4. This does not assume that every changed assignment can be listed
   cheaply. Forward/inverse assignment access is implicit through
   a retained rooted carrier version, with explicit local overlays
   only where an event needs them.
5. This does not apply an amortized dynamic-tree guarantee to a
   branching persistence history. The implementation uses
   worst-case dynamic trees and an explicit persistent-memory
   simulation.
