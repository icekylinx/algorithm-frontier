# Dynamic marked-forest compression and short-path unions

**Root research lemma, 25 October 2026. Independent application and
root integration audits completed.**

This note proves a local data-structure statement for the direct dynamic
spanner construction. It extends the earlier cut-only marked-Steiner
compression to arbitrary forest links, cuts, and nonnegative edge-length
changes. It does not assume that the underlying forest is decremental.

The key selection rule is local: retain every compressed edge whose
represented length is at most R. There is no need to track whether
each marked vertex is currently within distance R of a moving root.

## 1. Interface and statement

Let T be an explicitly maintained forest with immutable node and edge
identities during their lifetimes. Its elementary operations are node
birth, retirement of an isolated node, link, cut, edge-length change,
and insertion or deletion of a marked vertex. Edge lengths are
nonnegative. Each edge has either a current original physical edge ID
or a typed null/connector label. Each physical edge occurrence has
length at least one; in the spanner application its root-native length
is a common positive scale H. Node images and edge maps are fixed
during their lifetimes.

Assume standard deterministic dynamic-forest path and component
operations, including component mark count, one marked-node witness,
path length, and lazy edge-path assignment of a virtual-edge ID or
zero. The usual balanced dynamic-tree implementations support these
fields in polynomial logarithmic time. A path can be searched for its
first edge with a nonzero assigned ID, and for its first physical edge.
Subsequent enumeration of q physical occurrences costs
O((q+1) polylog N), even when the path also has many typed nulls.

Let M be the current marked set. There is a representation C(T,M)
with O(|M|) vertices and edges such that:

1. Its edges are edge-disjoint paths in T, and represent exactly the
   minimal marked subtree of each component that contains marks.
2. Marked vertices are retained. Every other retained vertex has degree
   at least three in that subtree; unmarked degree-two vertices are
   suppressed.
3. One elementary input operation changes O(1) compressed records and
   uses polynomial logarithmic structural work, before path exposure.
4. If every compressed edge of length at most R is exposed as its list
   of physical edge occurrences, the total list length is O(|M| R).
5. Every T-path between two marked vertices with length at most R is
   contained in the union of the exposed paths.

The time to update the exposed lists is O((R+1) polylog N) per changed
compressed record. Across a family of forests, global reference counts
produce the union of physical edge IDs with the same total work bound.
This union is an actual subgraph of the current original graph whenever
the forest edge maps have that property at settled states.

## 2. Static size and the short-edge selection rule

In a component with q marks, its minimal marked subtree has no unmarked
leaf. After suppressing unmarked degree-two vertices, there are at most
q minus two unmarked branch vertices when q is at least two. A component
with one mark contributes only that isolated compressed vertex. Thus
the total compressed size is O(|M|), independent of the total number
of unused forest nodes or the lengths of its suppressed paths.

Each exposed compressed path has nonnegative total length at most R.
Every physical edge occurrence contributes at least one, so its physical
list has at most R entries. A repeated original physical ID on a simple
forest path is counted repeatedly; its copies are distinct forest
occurrences and have positive length. Their total is still bounded.
Typed nulls have no physical output and are skipped using the path
aggregate rather than enumerated one by one.

Now take marked vertices u and v with a T-path of length at most R.
Their entire path lies in the component's minimal marked subtree. Since
both endpoints are retained, the path is a concatenation of whole
compressed edges. Each has nonnegative length at most the total path
length, hence at most R. Every one of them is therefore exposed.

This is why selecting short compressed edges is sufficient. Keeping
only individually short entire root paths would introduce a difficult
bulk-eligibility update when many root distances changed at once. That
different selection rule is not used here.

## 3. Mark insertion and the projection operation

If a component has no mark, inserting v creates its single retained
marked vertex. Otherwise choose any existing marked vertex z in its
component and search the forest path from v to z for its first edge
already assigned a compressed ID.

If such an edge exists, its endpoint nearer v is the projection w of
v onto the old marked subtree. If no such edge exists, use w=z.
This also handles an old subtree consisting of one marked vertex.
If v is already in the old subtree and v differs from z, its first
path edge toward z is assigned; hence w=v. No per-vertex scan of
incident active edges is needed.

If w is internal to an old compressed edge, split that edge at w.
If v is outside the old subtree, add the one compressed path v to w.
Mark v. If v was already a retained branch, only its marked flag changes.
These operations change constantly many compressed records. Finding the
projection, splitting a path, reading its length, and assigning new IDs
to its parts are ordinary dynamic-tree path operations. Long paths are
not enumerated during this structural step.

## 4. Mark deletion

If v is the sole mark in its component, remove its isolated compressed
vertex. Otherwise consider its degree in the compressed subtree.

* At degree at least three, remove only its marked flag; it stays as a
  branch vertex.
* At degree two, suppress v and merge its two incident compressed paths.
* At degree one, remove its entire incident compressed path. Its other
  endpoint w was previously either marked or an unmarked branch. If
  the latter now has degree two, suppress it once. A marked w remains,
  including as an isolated marked vertex if appropriate.

There is no long chain of suppression: degree-two unmarked nodes were
already internal to compressed paths. Thus the operation again changes
O(1) records, with path-ID assignments rather than physical enumeration.

## 5. A forest cut

If the cut edge lies outside the marked subtree, the compressed
representation does not change. A connected marked subtree cannot
straddle a cut that misses it.

Otherwise the cut edge belongs to exactly one compressed path a to b.
Before the physical cut, retire that compressed record and clear its
path assignment. After the cut, every remaining tail of that old path
has no interior mark or branch and is no longer in the minimal marked
subtree. No enumeration of those tails is necessary. Each of a and b
may now be an unmarked degree-two node, in which case suppress it.
Each resulting marked side contains a mark, because the old compressed
endpoints were marks or branch vertices with other marked branches.

Only one old virtual path and constantly many endpoint records change.
Its cached output list, if it was exposed, is retired from old metadata
before the cut. No path query is issued against an already broken path.

## 6. A forest link

Suppose an input link joins u in one tree to v in a distinct tree.

If either tree has no marks, the minimal marked subtree of the newly
joined component is the old nonempty marked subtree, or empty if both
were unmarked. The compressed representation does not change. Component
mark fields are updated by the forest link itself.

If both trees contain marks, use the following constant-length sequence:

1. Temporarily mark u and v wherever they were not already marked.
2. Perform the input link and add its one-edge compressed representation.
3. Remove only the temporary marks, using Section 4.

Temporary marking extends each old subtree to its attachment point.
The link joins these two extensions, so their union is precisely the
new minimal marked subtree before temporary marks are removed. Their
removal performs the necessary suppressions at u and v. Each temporary
operation changes O(1) records, proving the link bound.

Temporary records need not be externally published. Even if their short
lists are charged, the number of such records is constant and the stated
O(R polylog N) allowance pays them. Input forest links are assumed valid
and never create a cycle; this lemma does not process arbitrary graph
links as if they were forest operations.

## 7. Length changes, births, and path-exposure transactions

A length change outside the marked subtree changes no compressed path.
A change inside it affects the length of exactly one compressed path.
Its endpoint topology is unchanged. Recompute its length by a path sum
and update its exposure status. If a previously exposed list must be
retired, use its cached physical IDs. If its new length is at most R,
enumerate its current physical occurrences and install the new list.
Nonnegative edge lengths are needed both for the size bound and for
the short-path containment argument.

An isolated unmarked node can be born or retired without changing the
compressed graph. A marked node must first be unmarked or retargeted
by the caller before it is retired. Those actual mark changes are paid.
No hidden image change of a live marked node is allowed.

For a general transaction, retire old exposed records while their
metadata is available, apply the structural forest and compression
changes, then install new short exposed records. Each exposed path
keeps its physical list, so retirement never scans a long or invalid
path. A long compressed path has no expanded output list.

For the union over many forest records, increment or decrement a
deterministic reference count for each listed physical ID. Only a
zero-to-positive or positive-to-zero transition changes the published
subgraph. Charging every reference operation is conservative and bounds
both work and recourse. An original edge deleted during a transaction
has no positive output reference once all its forest occurrences have
been retired. Statements concern the final settled state.

## 8. Consequence for represented unit-edge query witnesses

Suppose a distance representation has at most q marked terminals over
a family of forests. Assume that for every current unit original edge
uv, its approximate witness is a concatenation of paths in this family,
whose endpoints are marked and whose total nonnegative root-native
length is at most R. The physical union selected above contains each
constituent path, and therefore contains a u-to-v walk of original
length at most the witness bound after projection. Replacing edges
of an arbitrary shortest path proves the same multiplicative stretch
for all original pairs.

The output uses at most O(q R) physical edge occurrences before global
deduplication. If the forest family and marked terminals have total
update transcript W, the additional maintenance costs at most
O((R+1) W polylog N), plus initialization. This is an interface theorem:
the separate tracked-terminal construction must prove its own q and W
bounds, fixed terminal handles, and root-native witness lengths.

There is no insertion-independent recourse assertion. A change in a
tracked terminal or forest path may remove or add output edges even
when the original update is an insertion. The low-recourse five-sixths
batching theorem remains a separate stronger guarantee in that respect.

