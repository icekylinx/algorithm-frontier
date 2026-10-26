# A complete one-sided client parameterized by feedback-edge count

**Research theorem, 25 October 2026. Root review and two independent mathematical audits completed.**

The reviews are [feedback-edge-one-sided-client-independent-audit.md](feedback-edge-one-sided-client-independent-audit.md)
and [feedback-edge-client-independent-audit.md](feedback-edge-client-independent-audit.md). The parameter
restriction and the lack of a new unrestricted matching exponent
are part of the accepted statement.

Let the entire ordinary allocation graph be a spanning forest T plus
at most k additional physical incidences. The unrestricted-receiver
forest client extends to a complete client on this graph. A query,
a represented simple-path update, and its guard checks cost
(k+1) polylog S, plus discovered register events. On a fixed
polynomial-range ledger the total work is
```math
(m+\nu(k+1))\mathrm{polylog}S. \tag{1}
```

This is a parameterized interface. General bounded-degree allocation
graphs can have k=Theta(nu); substituting that value does not improve
the general-matching four-fifths theorem.

The proof uses complete_unrestricted_forest_one_sided_client.md and
only the topology portion of the already audited
dynamic_marked_forest_short_path_union.md. No short-path list is
exposed or enumerated in the present application.

## 1. Forest and chord ownership

Choose a spanning forest T of the whole ordinary row/bin graph G.
Let X be the remaining incidence IDs, with |X|<=k. Every coordinate
belongs to exactly one of these two sets.

Coordinates on T are represented by the unrestricted bidirectional
forest watcher. Chord coordinates are explicit scalar records.
Both kinds have the same persistent register ell and conservative
donor price ceil(H/(4ell)); every receiving direction is available
at price zero.

The forest DP gives the best tree-only path score. At any ordinary
vertex v it also supplies
```math
\begin{aligned}
 I_T(v)&=\max_{a\text{ bin}}\{\sigma_a-\bar L_T(a,v)\},\\
 O_T(v)&=\max_{b\text{ bin}}\{-\tau_b-\bar L_T(v,b)\}
 \end{aligned}                                                   \tag{2}
```
in its T component, with a maximizing bin witness. Expose(v) reads
the relevant boundary entries without scanning the component.

## 2. An O(k)-size exact core

Mark all endpoints of chord incidences. There are at most 2k marks.
Maintain the minimal marked subtree in each component of T, suppressing
unmarked degree-two vertices. The resulting virtual forest C has O(k)
vertices and edges. Each virtual edge is an actual T-path.

These virtual paths are edge-disjoint and have disjoint interiors.
All chord endpoints are retained vertices. Therefore a chord cannot
attach to the interior of a virtual edge.

Use unit hop lengths for this topology compressor. Numerical price
changes do not alter it. At every search, read the two current
directional donor-cost sums of each virtual T-path from the watcher.
This reprices O(k) virtual arcs, in (k+1) polylog S time, without
enumerating any long path.

Add each chord in both directions, with zero receiving cost and its
current donor cost. This produces a directed nonnegative-cost core
with O(k) vertices and arcs. Disconnected ordinary components are
handled separately inside the same small core.

For each marked terminal v, add an artificial-source edge of length
A-I_T(v), where A>=max sigma_d. This length is nonnegative.
The exit value at terminal v is O_T(v). Both values and their endpoint
witnesses take O(k polylog S) total query work.
Omit a source or exit record whose offer is minus infinity.
In the stated settled allocation graph a chord's spanning-tree
component contains bins, but this convention also covers a
generic empty-offer dynamic-programming record.

The two directional distances along a virtual edge need not be equal.
The core is a directed graph, even though its virtual underlying part
is a forest.

## 3. Exact separation by a small Dijkstra computation

First check the best tree-only score. If it is positive, use that path.

Otherwise run Dijkstra from the core's artificial source. A terminal
v passes when
```math
\mathrm{dist}(v)<A+O_T(v).       \tag{3}
```
This computation takes O((k+1) polylog S) bounded-word work.
Keep a simple predecessor path and the maximizing starting and
ending bin identities.
Use settled-order predecessors: assign or improve an unsettled
vertex only from a settled vertex, and do not redirect a settled
vertex to a later vertex on a zero-cost tie. The predecessor
chain is then simple even in the presence of zero receiver costs.

Why is the test complete? Any ordinary G path with a chord has a
first chord endpoint and a last chord endpoint. Its initial and
final pieces lie in T. Between chord incidences, its T pieces lie
in the marked subtree and are exact concatenations of virtual
edges. The offers (2) can only improve the chosen source and
target pieces. Thus a positive-scored G path implies a positive
test (3), unless it was already caught by the tree-only search.

Conversely, a positive test produces a directed walk whose score
is positive, consisting of:

1. one T path from a source bin a to a marked terminal;
2. a simple core path;
3. one T path from a marked terminal to a target bin b.

All ordinary costs are nonnegative. Its source and target prices
are counted only once. Section 4 turns this represented walk
into a simple path without increasing its cost.

If neither test passes, the full graph has no positive conservative
threshold path. In particular it has no true one-sided path of
ratio above one half. The sign-compatible circulation decomposition
of the forest client then proves complete LOW on this general
ordinary graph as well: ordinary-only cycles have zero slack gain,
and a simple auxiliary-vertex cycle yields a simple bin path.

## 4. Loop erasure in O(k) tree-path queries

### 4.1 The middle expansion is already simple

A simple core path expands to a simple ordinary path M. Distinct
virtual edges have disjoint interiors, and every endpoint of a chord
is a retained core vertex. Hence an expanded virtual interior cannot
meet a different core edge or chord endpoint. The core predecessor
path does not repeat a vertex.

M has O(k) pieces, each a T path or a single chord. The initial
source path A_0 and final target path B_0 are the only possible
sources of repeated vertices in the whole represented walk.

### 4.2 Two trimming operations suffice

Let A_0 go from a to the first vertex s of M. Find the last vertex
z along M that lies on A_0. It exists because s is such a vertex.
Keep the prefix of A_0 ending at z and the suffix of M starting
at z. Call the resulting path Q.

Q is simple: the retained M suffix after z has no vertex anywhere
on A_0, by the choice of z. The removed portion was a closed walk,
so its removal does not increase cost.

Next let B_0 go from the last vertex t of Q to the desired target b.
Find the last vertex y along B_0 that lies on Q. It exists because
t lies on both. Keep the prefix of Q ending at y and the suffix of
B_0 starting at y.

The result is a simple a-to-b path. Its remaining final suffix has
no intersection with Q, and another nonnegative-cost closed walk
was removed. Its conservative threshold score is therefore still
positive.

Each trimming operation costs O(k) path-intersection queries:
scan the O(k) pieces of M or Q, treating a chord only through its
two endpoints. The resulting representation still has O(k)
tree-path pieces and chord incidences. No erased long path is
enumerated.

### 4.3 Dynamic-tree intersection queries

All tree pieces use the same current T. Two paths can be intersected
using a constant number of hop-distance and path-selection queries.

For P=T[a,b], project a vertex c onto P. Its distance from a is
```math
\frac{\mathrm{hop}(a,b)
                         +\mathrm{hop}(a,c)
                         -\mathrm{hop}(b,c)}2 .
```
Select that vertex along P by its hop index. For Q=T[c,d], let
p,q be the projections of c,d onto P.

If p differs from q, the intersection is T[p,q]. If p=q=z, the
intersection is {z} exactly when
hop(c,z)+hop(z,d)=hop(c,d); otherwise it is empty.
Components are checked first. The formula also handles a
zero-edge path.

Hop counts and selection are ordinary dynamic-tree aggregates.
Directional order within an intersection is determined by hop
distance from the desired path's first endpoint. Thus the last
intersections required above take polynomial logarithmic time
per piece, even when the represented paths are long.

All topology and prices remain frozen during this search and
trimming transaction.

## 5. Apply the final path atomically

Read the final path's donor sum from its O(k) forest pieces and
explicit chords. Its score remains positive after trimming, so
the standard finite-grid step
```math
V_{\rm up}=1/s_a+1/s_b+4\bar L(P)/H,\qquad
             1/512\le\eta V_{\rm up}\le1/256
```
is valid.

Check all forward guard minima of those pieces and the explicit
chord values before committing. Apply the same eta to every
piece and chord in its actual orientation. Update only the two
endpoint slacks.

The whole operation is atomic. A forest piece may end at a row
or at an internal bin; conservation is asserted only after all
pieces and chord changes have been applied. No structural action,
new query, or incompatible cache read interrupts that transaction.

The final path is simple, so its pieces use disjoint physical
incidences. No coordinate receives two independent changes in
one step. Chords are updated explicitly; forest pieces use the
bidirectional lazy watcher. Settle all register events and both
endpoint price updates before the next search.

The price-event bound remains
```math
R=O(J+(m+A_x)\log S).
```
One accepted simple path still has O(1) total negative allocation
log variation; using several represented pieces does not multiply
that quantity by k.

The same minimum-slack and donor-lower-bound argument excludes
numerical guard obstruction on a static polynomial-range input.

## 6. Static work and word bounds

One search, loop erasure, donor-sum computation, guard check, and
ordinary path update costs (k+1) polylog S plus its register
notifications. No factor of the final path's length occurs.

The objective width gives J=O(nu log S). Combining this with the
global register bound proves (1). The core and temporary path
descriptors use O(k) space; the forest and native records use
O(m+nu) space.

All directional costs are polynomially bounded integers. A core
shortest path has O(k) arcs, and each virtual arc has at most nu
ordinary occurrences. Its cost therefore has O(log S) bits.
After trimming, the actual path has at most nu-1 incidences and
the standard threshold rounding analysis applies.

The complete LOW implication uses that standard analysis on a
hypothetical simple strong path. It does not incorrectly apply
the nu-edge rounding count to an untrimmed walk with repeated
tree edges.

## 7. Dynamic structure with bounded current feedback count

The decomposition can be maintained explicitly under structural
graph edits while its current cycle rank stays at most k.

* Insert an incidence into T if its endpoints were in different
  T components; otherwise retain it as a chord.
* Delete a chord directly.
* After deleting a T edge, scan the current chord list and, if
  possible, promote one chord joining the two resulting parts.
  If none does, the ordinary graph has really disconnected there.

A scan costs O(k polylog S). At most one chord is promoted per
tree-edge deletion. Promotion transfers its unique coordinate
ownership to the forest watcher using its current value and
existing register.

Reference counts at chord endpoints maintain the marked set.
Each edge insertion, deletion, or promotion changes O(1) marked
records. The audited marked-forest compressor handles the
corresponding forest cut/link/mark changes in polynomial
logarithmic structural work. Numerical steps do not change its
unit-hop topology; the next query simply reprices its O(k)
current virtual paths.

Explicit high-degree vertex deletion must enumerate its incident
edges. Retargeting is deletion plus insertion. New or externally
set coordinates and changed slacks are charged by the same
A_x,A_s transcript as in the complete forest client.

For J steps, Q additional queries and A_T topological records,
a conservative total bound is
```math
\bigl[m_0+\nu_0+(J+Q+A_T)(k+1)+A_x+A_s+R\bigr]
                              \mathrm{polylog}S.      \tag{4}
```
With the objective/variation accounts substituted, this is
```math
\bigl[m_0+\nu_0+A_x+A_s
       +(k+1)(\nu_0+A_s+A_T+Q)\bigr]\mathrm{polylog}S.
```
The parameter bounds the actual intermediate graph ranks as
well as the settled ones; using cuts before insertions in a
structural replacement batch avoids an unnecessary union-graph
rank spike.

This pays explicit general graph edits. It does not assume that
the numerical path itself is installed in T by basis pivots.

## 8. Why degree three does not make k small

There is a simple subcubic family with linearly many feedback
edges. Start from a bin b_0. In block i introduce rows r_i,s_i
and bins a_i,b_i, with incidences
```math
r_i b_{i-1},\quad r_i a_i,\quad r_i b_i,\quad
 s_i a_i,\quad s_i b_i .
```
For q blocks, the graph has 4q+1 vertices, 5q edges, and cycle
rank q. Every row has degree at most three and every bin has
degree at most three.

These graphs also admit positive allocation ledgers of the
ordinary kind. Delete each chord r_i b_i to obtain the alternating
chain with 2q rows. Let every nonroot bin have slack 2C and
capacity L-C. Along chain row j, give its parent
3C(2q-j+1) and its child the complementary amount. The free
root then has slack L-(6q+1)C>0 for sufficiently large L.

For each block add a small epsilon on chord r_i b_i, subtract
epsilon on r_i a_i, add epsilon on s_i a_i and subtract epsilon
on s_i b_i. This preserves every row sum and every bin load.
All incidences become positive, all slacks stay unchanged, and
the cycle rank is still q.

This is enough to exclude a structural inference that row degree
three or the allocation equations force a small feedback set.
A separate general-graph decomposition or basis-exchange theorem
would be needed to use the parameterized client at smaller k
throughout the matching algorithm.

## 9. Next general-graph question

A possible next step is to cover the relevant directions by
several low-feedback subgraphs, or to maintain a changing
allocation basis with small explicit feedback. Either method
must preserve the full-graph separation guarantee and pay
its reconstruction or pivot work.

Cancelling ordinary allocation cycles preserves the slack
objective, but it can change allocation prices without earning
objective progress. The present register accounting does not
make those pivots free. Zero off-basis incidences also remain
available as receiving directions, so ignoring them is not a
valid LOW certificate.

Those issues are outside the theorem proved here.

