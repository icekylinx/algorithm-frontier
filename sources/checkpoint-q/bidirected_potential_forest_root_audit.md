# Root audit: bidirectional potential-compatible forest paths

**25 October 2026. Completed internal mathematical review.**

## Accepted local statement

The construction in
`bidirected_potential_compatible_forest_matching_interface.md` correctly
extends the accepted directed-forest interface. Its underlying graph
remains an undirected forest of unique physical allocation-coordinate
IDs. Each incidence permits its donor direction, and also permits its
receiving direction when the fixed feasible labels are equal at its
endpoints. Different accepted paths may use the same incidence in
opposite directions without an intervening cut, link, or register reset.

For supplied labels and initial forest, the total local work remains

\[
 (\nu+J+P+Q+R)\operatorname{polylog} S,
 \qquad
 R=O\bigl(J+(N+A_{\rm ext})\log S\bigr).
\]

The symbols count the same numerical steps, supplied forest edits,
additional queries, and history-wide register events as in the directed
version. This is not a bound on ambient edge discovery or label refresh.
The arbitrary general-graph matching exponent remains four fifths.

The independent review is
`bidirected_potential_forest_independent_audit.md`. The underlying public
top-tree interface was directly checked in the root audit of the
directed version. This document checks the additional bidirectional
arguments rather than repeating that primary-source review.

## 1. Two directed arcs do not duplicate a physical coordinate

The score graph may display two opposite arcs on one underlying edge.
The path domain is still the unique underlying simple path between its
chosen endpoints. An edge can therefore occur at most once in one
accepted path. A two-arc out-and-back walk is outside that domain.

This distinction is enough for exact row and bin conservation. At each
internal row, the actual traversal enters through one physical donor
and leaves through one physical receiver. Its allocation sum is
unchanged. Internal bin loads cancel, and the two endpoint slacks have
the usual opposite changes. Allowing an incidence to be used in the
opposite direction on a later path does not change this argument.

The score DP keeps directional boundary entries. Both W(d,r) and W(r,d)
may be finite for a tight incidence. The constant-size join formulas
remain valid because the two child clusters share exactly one vertex
and have disjoint edge sets. A crossing candidate uses one path in
each child, meeting at that shared vertex only. It cannot introduce a
cycle or a repeated-coordinate update.

The pendant source and target leaves remain one-directional. Thus an
endpoint price is included once at its intended end, and never as an
interior reward. The negative self-pair still cannot pass the threshold.

## 2. The two watcher buffers have the required opposite response

At a physical incidence, write

\[
 w_D=x-\ell,\quad w_R=2\ell-x,
 \qquad
 g_D=x-\chi,\quad g_R=U-x.
\]

If the incidence is used as a donor, x decreases by eta. Its donor
buffers decrease by eta and its receiving buffers increase by eta.
For a receiving traversal the two changes are reversed. Consequently,
along an ordered returned path, every forward buffer decreases by eta
and every backward buffer increases by eta, regardless of the row/bin
roles of the individual edges.

This identity justifies two directional minima and a signed lazy tag
on a path cluster. Adding delta in its stored boundary order subtracts
delta from its forward minima and adds delta to its backward minima.
The reverse traversal is the same operation with negative delta.

When a parent cluster splits, its traversal order specifies whether
each path child's local boundary order agrees or disagrees. Propagate
the tag with that sign, and propagate nothing to off-path children.
At a join, choose the relevant directional field of each path child
before taking a minimum or adding donor costs. These are constant-size
updates. The physical donor direction never changes merely because the
top tree reroots or stores a different boundary order.

## 3. Guard checks and event discovery are complete

Before a numerical step, query the guard minimum for the actual
returned direction and check both endpoint slack guards. A failed
check returns its witness before any allocation is changed.

At a settled state, both register buffers are positive at every edge.
During one accepted path update, the backward buffers only increase
and off-path buffers remain unchanged. Therefore all newly violated
register inequalities are found by searching only the forward minimum
on the updated path. There is no unreported reverse-direction event.

At a discovered edge, recover its exact x, reset ell to 3x/4, and set
both new buffers to x/4 and x/2. Then update the unique donor score in
the scored forest and the directional donor sums in the watcher.

The latter notification is required even when the step used the edge
as a receiver. In the bidirectional representation the reverse donor
arc is present in the maintained score DP; its decreased price is not
an off-forest bookkeeping detail. The main construction explicitly
includes this work for every reset.

## 4. Fixed-label compatibility survives direction changes

An incidence with unequal fixed labels has only its donor direction
available. Its allocation can only decrease while selected, so its
donor price can only increase. On an equal-label incidence, the
receiving direction is also available. Any decrease of its reverse
donor price remains feasible because its old potential difference is
zero and the price is nonnegative.

Thus changing a coordinate's direction of motion on later paths does
not require a monotonic-price assumption. Every price decrease is
individually justified by fixed-label tightness.

Along any accepted available path,

\[
 D(b)\le D(a)+\bar L(a,b)<A-\tau_b.
\]

The same endpoint margin pays for the terminal source-price increase.
The start's source constraint becomes more permissive. All other
source constraints are unchanged. Hence the complete threshold graph,
not just its selected forest, retains the old feasible labels.

The one-sided ratio, finite-grid step, constant log-slack progress, and
semantic LOW screen depend only on that feasibility, the endpoint
slacks, and the path's donor sum. They therefore carry over unchanged.

## 5. Ownership, arithmetic, and variation accounting

Each cut materializes the one selected coordinate through a point
query, then removes its two representations. A new link uses that
explicit native value and the persistent ell. The ownership table
continues to forbid independently authoritative copies.

An internal operation below a tagged cluster first splits and pushes
that cluster. Between clearing a cluster's tag and its next push, all
unpropagated updates act on the same cluster path. The signed tag is
therefore the net coordinate change along that path, with fixed local
orientation signs. Guarded magnitudes and the fixed dyadic grid bound
its word length; repeated reversals do not introduce denominator growth.

A reset still requires a constant absolute log change since the last
reset. Switching direction does not reset the anchor or erase that
history. One accepted path has O(1) negative allocation-log variation,
while the established sum-log potential accounts for positive
variation plus explicit coordinate lifecycle changes. The same
history-wide bound on R follows.

## 6. Consequence and remaining boundary

The new interface searches every potential-compatible simple path on
the current physical forest. In particular, a path can leave a bin by
reversing a formerly selected tight receiving edge, enter its parent
row, and continue into another branch. The directed-tree exhaustion
construction is bypassed in this way without rebuilding the tree.

This local improvement does not prove that a useful path always exists
on the current physical forest, or even in the entire graph restricted
to old-label-tight receiving arcs. A useful ambient direction may
require a new physical edge or a non-tight receiving edge. Discovering
such directions and paying for the required label changes remain the
global questions.
