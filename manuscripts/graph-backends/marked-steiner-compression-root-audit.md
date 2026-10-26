# Dynamic compression of marked subtrees: a local root audit

**25 October 2026.** This note independently proves the combinatorial
compression step proposed for a new low-congestion forest lift. It
does not by itself assert a new strong-SSSP or Gomory--Hu exponent.
The copy-pool lift, update accounting, and outer composition are
separate obligations.

## 1. Interface and exact object

Let <code class="math">F</code> be a forest of an actual native graph. Within one generation,
its edges only disappear and new vertices enter as isolated vertices.
Each living edge has a fixed positive integer length. Let <code class="math">Z</code> be a
changing set of marked vertices, maintained with reference counts.
Different reasons for marking the same vertex count once in <code class="math">Z</code>.

For each component containing marks, let <code class="math">S</code> be the minimal subtree
spanning those marks. For one mark it is a single vertex; for no marks
it is empty. Its compressed representation retains every marked
vertex and every unmarked vertex of degree at least three in <code class="math">S</code>.
Maximal paths between retained vertices are represented by single
virtual edges. Their lengths are the sums of their physical edge
lengths in <code class="math">F</code>. They retain physical endpoint identities and a
dynamic-tree path handle.

The virtual edges have pairwise disjoint physical edge interiors
within this one forest. A physical vertex internal to a virtual edge
is internal to exactly one such edge. Retained vertices may be shared
endpoints of several virtual edges. The number of retained vertices
and virtual edges is <code class="math">O(&#124;Z&#124;)</code>, summed over marked components.
Each retained vertex has virtual degree at most its degree in <code class="math">F</code>.

These statements follow directly from suppressing unmarked degree-two
vertices in a tree. No metric approximation is introduced.

## 2. Required ordinary dynamic-tree operations

Use an ordinary dynamic-tree representation of the full forest <code class="math">F</code>,
and a component aggregate that can return any marked vertex in a
component. The operations needed here are:

* cut a physical edge;
* expose the path between two vertices in the same component;
* assign one bit to every vertex of an exposed path, excluding a
  specified endpoint when needed;
* assign one virtual-edge identifier to the physical edges of an
  exposed path;
* query the first vertex with bit one on an oriented exposed path;
* query a physical edge's current virtual-edge identifier;
* obtain a path length and the first physical edge on an oriented
  nonempty path.

Link-cut trees with lazy path assignment provide the path operations.
An Euler-tour forest with a marked-vertex aggregate provides the
component operation. The two structures process the same physical
cuts and mark changes. All these operations take polynomial
logarithmic time and actual linear storage. The vertex bit is one
exactly on the current minimal marked subtree <code class="math">S</code>; physical edges
outside <code class="math">S</code> carry a null virtual-edge identifier.

Only the virtual representation is reported to the caller. Lazy
updates to a long physical path are not reported as changes to all
its internal vertices or edges.

## 3. Inserting one mark

If the component has no other mark, create its one marked virtual
vertex and set its active bit. Otherwise obtain any old marked
vertex <code class="math">t</code>. The path from the new mark <code class="math">v</code> to <code class="math">t</code> first meets
the old subtree <code class="math">S</code> at a unique vertex <code class="math">w</code>.

Find <code class="math">w</code> by the first-active-vertex query on that path. This does
not require a nearest-mark computation. If <code class="math">w</code> is internal to a
virtual edge, split that virtual edge at <code class="math">w</code>, using its stored
identifier. Explicit records distinguish retained virtual vertices.
For an internal <code class="math">w</code>, the first physical edge of <code class="math">w\leadsto t</code>
has the required identifier; this path is nonempty because the
old mark <code class="math">t</code> is retained. If <code class="math">v\ne w</code>, add the virtual edge for <code class="math">v\leadsto w</code>.
Set the bits and identifiers along the affected physical paths by
lazy path assignment. If <code class="math">v=w</code>, it is enough to mark or split at
that existing vertex.

At most a fixed constant number of virtual vertices and edges
change. The union of <code class="math">S</code> and <code class="math">v\leadsto w</code> is exactly the new
minimal marked subtree, proving correctness.

## 4. Deleting one mark

The reference count must first become zero. If the virtual vertex
has degree at least two, the physical subtree does not shrink.
An unmarked degree-two virtual vertex is suppressed by merging
its two virtual edges. A vertex of higher degree remains a
branching vertex.

If the old mark has degree one, remove its virtual edge to the next
retained vertex <code class="math">w</code>. Clear active bits on that path except at
<code class="math">w</code>, and clear the removed edge identifiers. If <code class="math">w</code> is now an
unmarked degree-two vertex, suppress it. No further pruning chain
of virtual vertices is possible: before the deletion every
unmarked retained vertex had degree at least three, and only this
one neighbor loses an incident virtual edge.

An isolated sole mark is simply removed. Again only constantly
many virtual records and path assignments change.

## 5. Deleting one physical forest edge

If its virtual-edge identifier is null, the edge lies outside the
old minimal marked subtree. That subtree needs no change. A newly
designated root of a detached component can subsequently be added
as a mark by Section 3.

Otherwise the deleted edge lies on a unique virtual path
<code class="math">u\leadsto v</code>. Remove that virtual edge. On each side, discard
the now-unused tail between the cut location and its old virtual
endpoint. Both old endpoints have marks somewhere on their
remaining sides: each was either marked itself or an unmarked
branching vertex with at least two remaining directions toward
marks. Thus the two discarded tails contain no still-needed
branch or mark.

Clear the two tails by path assignment in the resulting physical
components. An unmarked endpoint whose degree drops to two is
suppressed once. All other virtual incidences are unchanged.
This is the minimal marked subtree in each resulting component.
The physical cut therefore creates only constantly many virtual
record changes and path operations.

The special cases in which the cut is adjacent to <code class="math">u</code> or <code class="math">v</code>
have an empty tail and require no extra operation. A batch of
physical cuts is processed sequentially. Marking its newly
designated roots is charged separately and explicitly.

## 6. Initial construction and lifetime cost

The initial marked subtree and its suppressed representation can
be built by pruning unmarked leaves and traversing the surviving
forest. This costs linear time in the actual initial forest.
Initialize its path data structures from that same inventory.

Afterward, <code class="math">q</code> physical cuts and changes of marked status take
polynomial logarithmic time per event and report <code class="math">O(q)</code> virtual
edge/node edits. New isolated vertices are charged when they are
created. A generation replacement pays for its actual old and
new forest inventories.

In the intended application, every stable core root is marked,
as is every physical endpoint of a currently selected core edge.
There is no need to mark the junctions of one core in every other
core. Each compressed core forest supplies its own paths, and
only its exposed equal-physical-image junctions are identified.
Connections omitted at unexposed internal coincidences are not
needed to reconstruct a selected core edge's root-to-root route.

## 7. What remains outside this lemma

This compression lemma does not make a long virtual path a flat
edge. Expanding or deleting all physical edges of that path on
every virtual edit would lose its time advantage. A complete
strong-forest construction must implement the separate pool
mechanism that changes only a few cuts and equal-image joins.

It must also count all unused vertices in those pools, all
copies of stable forests, the coloring work, fixed canonical
node identities, and each recursive graph-edit transcript.
Low embedding congestion alone is not an update-time proof.
