# Independent audit of destructive APSP support extraction

**25 October 2026. Status: passes with the explicit source and version
conditions below.** The audited construction is
`destructive_apsp_path_support_extractor.md`. The oldest-center tie rule,
positive polynomially bounded input lengths, and edge-based treatment of
the arbitrary-degree adapter were clarified during this audit and are
incorporated into the main construction.

This audit checks the path-support bridge and its approximate half-layer
interface. It does not assert the separate expander outer parameters or
an improvement to the general-graph matching exponent.

## 1. The additional representation is necessary

The numerical APSP answer alone does not give a cheap literal path.
There can be many repeated real edges and many connector edges that
project to nothing. Likewise, the nearest-pivot forests alone do not
represent an exact shortest path between two vertices in one strict
pivot ball.

The audited family therefore contains, at each nonbase level, both
the nearest-pivot forest and one strict-ball shortest-path tree for
each source. The base retains all-source shortest-path forests.
Every member has its own occurrence identities; different trees are
not identified merely because some of their vertices have the same
physical image.

Each query leg is a path in one of these local forests. The arbitrary
forest lift then gives an endpoint-preserving root-flat forest path
whose projected physical length is no greater than the correctly
rescaled local length. This is stronger than the raw-cycle lift and
uses the independently audited metric-forest interface.

## 2. Inverse clusters, rather than ball sizes alone, pay for the family

The required center contract is the constructive one in
`current_checkpoint/uniform_source_interfaces_for_4_5.md`, Section 2:
both strict balls and inverse clusters have size
\(k\operatorname{poly}(U)\). This is an actual retained source
interface from the center construction, not an inference from small
balls.

For every shortest path from a source \(v\) to a vertex in its
strict ball, all intermediate vertices are also in that strict ball:
positive edge lengths make every proper prefix shorter. Consequently
a physical vertex \(w\) lies in the ball trees of at most
\(|C(w,A)|\) sources, plus a possible isolated self-root record.
This proves a local pointwise occurrence bound
\(k^{O(1)}\operatorname{poly}(U)\).

The initial candidate counterexample using a binary tree with long
outward edges does not contradict this contract. It can make many
small balls contain the root, but then its one-center set violates the
inverse-cluster bound. The safe center construction adds centers in
that situation. This distinction must remain explicit.

The main construction correctly uses the nearest-pivot forest when a
query terminates at its pivot. Its strict-ball trees thus do not need
an extra boundary vertex. If one instead included the initial pivot
in each source tree, the constant-degree input would also pay for
those boundary copies: each final pivot predecessor is in the strict
ball, and there are only constantly many predecessor neighbors.

Small initial components have at most the declared threshold of
vertices, so their one-center treatment satisfies the same coarse
inverse bound. New isolated vertices are their own centers.

## 3. Promotions, ties, and current witnesses

Before a physical edge changes, its endpoints are promoted. A strict
ball path cannot cross that edge: it would first encounter a pivot
before reaching a strict-ball target. A nearest-pivot leg likewise
cannot cross the changed edge after those promotions; reaching its
first endpoint already provides a strictly shorter pivot destination.
Hence surviving exact local paths come from the initial future-path
inventory for that parent period.

There is a boundary case for equal real distances. Give initial
centers a fixed order, and place each later promoted center after all
older centers. Resolve equal nearest-pivot distances by this order.
A new center can then change an existing vertex's pivot only if it
is strictly closer. The changed vertex belongs to the old inverse
cluster of that new center, so the same local inventory pays for its
update. Internal shortest-path ties can use the existing consistent
symbolic convention independently.

The rule still defines a valid global nearest-pivot forest. If a
proper suffix vertex on a chosen path preferred a closer center, or
an equally close older center, the original path source would have
the same improvement, a contradiction. Parent pointers therefore
remain consistent.

Shrinking a source's strict ball keeps a prefix-closed part of its
old shortest-path tree. Explicitly updating its at most
\(k\operatorname{poly}(U)\) records is local polynomial-in-\(k\)
work. At most that many sources are affected by one promotion, using
the inverse-cluster bound. Rebuilding every affected local tree is
therefore still within \(k^{O(1)}\operatorname{poly}(U)\) work.
Actual-size base trees may also be rebuilt as part of update work.

Removing an isolated center cannot enlarge another vertex's ball in
its connected component: it has no such component neighbor. Parent
period restarts rebuild their own source inventories and are charged
as restarts, rather than treated as free monotone ball changes.

## 4. The occurrence multiplier is additive at birth, not multiplied at every level

Let

\[
                  b_*=k^c\operatorname{poly}(U)
\]

be a fixed polynomial upper bound for a local family's occurrence,
including a base family. For the disjoint union of all families born
at or below a level, the lift recurrence has the form

\[
                G_j\leq b_*+P(G_{j-1}+1).
 \tag{1}
\]

The local family is added at that level. It is not copied afresh at
each ancestor of every already lifted local family. Thus

\[
                    G_d\leq b_*(cP)^{O(d)},
 \tag{2}
\]

and the sharper separate-birth summation gives
\(O(d b_*P^d)\) under a common normalized \(P\). Both have
logarithm \(O(x+d\log P+h)\). There is no \(k^d\) term.

The preallocated pool mechanism is essential here. Claiming a child
vertex occurrence claims a distinct existing pool index; changing a
child forest edge changes one connecting record. It does not copy a
whole stable parent tree for every child edit. Changes to a parent
stable tree are a separate source-sized charge to its pool copies.

For clarity, enlarge the local work envelope once to
\(W'=k^{O(1)}W\) to include the local tree family. The safe
initialization/update recurrence can be retained as

\[
\begin{aligned}
 J_j&\leq O(W'+P(G_{j-1}+1))
                +(P/k)(J_{j-1}+T_{j-1}),\\
 T_j&\leq O(kW'+kP(G_{j-1}+1))
                +O(P)(J_{j-1}+T_{j-1}).
\end{aligned}
 \tag{3}
\]

The \(T_{j-1}\) term in the initialization line retains the late
spending of initial selected-edge credit. With
\(Z_j=J_j+T_j/k\), equations (1)--(3) yield

\[
 Z_j\leq O(W'+P(G_{j-1}+1)+PZ_{j-1}).
\]

Solving this recurrence introduces the local \(k^{O(1)}\) only
once, in the inhomogeneous work and occurrence terms. The resulting
history cost has the stated exponent

\[
                 B=O(x+f+Kg+d\log P+h).
\]

This calculation uses actual allocated occurrences, including dormant
pool capacity. Retired occurrences are removed from registries; pool
indices can be reused only after their former connections are retired.

## 5. Descriptors use current forest-local handles

A query has at most two nearest-pivot legs at each nonbase level and
one final strict-ball or base path. It therefore has at most
\(2d+1\) root-flat forest-path segments. The lookup of a flat
endpoint may follow its at most \(d\) current ancestor maps; even
that direct implementation remains polynomial logarithmic. No local
ball or base graph is searched during a numerical query.

Each segment uses handles for one current forest version. Adjacent
segments may have different occurrence handles with the same original
physical image. Their projected walks still concatenate. No global
identification of equal-image aliases is required.

The graph and all these handles are frozen while the descriptor is
consumed. A later restoration or permanent deletion may retire every
old handle; it occurs only after the support has been materialized.
Querying a mixture of retired and new versions would be invalid, even
if the corresponding seen flags happened to be zero.

## 6. Zero connectors and repeated real edges are skipped without expansion

Each current root-flat forest edge is either a copy of one immutable
original real edge or a typed connector. Assign a one-bit dynamic-tree
weight to an unconsumed real-edge copy and zero to all connectors.
On finding an unconsumed original identifier, mark all its allocated
occurrences zero using its registry. New occurrences inherit the same
global flag.

A dynamic-tree path aggregate can detect and find a positive edge
without traversing zero-weight portions. Repeated occurrences of an
already found real edge are also skipped. The cost is logarithmic
per discovered original identifier and per final empty segment, plus
the explicitly charged registry updates.

For arbitrary original degrees, the occurrence estimate is applied
first to the degree-three proxy graph. Each original real edge has
one current proxy real edge, so its registry still has the required
bound. An original vertex can have many port images; the extractor
never scans all of them merely to identify a support edge. It uses
immutable real-edge endpoints to build its small extracted subgraph.

The support contains a projected source-target walk. Its own DFS
therefore returns a simple path, in time linear in the distinct
support. Positive original lengths imply

\[
 |S|\leq\sum_{e\in S}\ell_e\leq\operatorname{len}(W),
 \qquad
 \operatorname{len}(P)\leq\sum_{e\in S}\ell_e.
\]

Permanently deleting every edge of \(S\), including unused DFS
edges, is essential. It gives \(\sum|S|\leq m\). Without that
consumption rule, the same large repeated-walk representation could
be charged again on the next query.

## 7. Own-matching-path exclusions have a persistent failure charge

For an active group with its own matched simple path \(P_a\), a
query must exclude equality with that hyperedge. If \(P_a\) is
still entirely present, scan its edges with a persistent pointer.
Temporarily delete the current edge, settle the hierarchy, and query.

A failed trial proves that the permanently retained graph minus that
edge has no comparison-length path. Because the permanent graph only
shrinks, that failure remains valid after later successes by other
groups. Advance the pointer only after failure. The total number of
such failures is at most

\[
                       \sum_{P_a\in M}|E(P_a)|\leq m,
\]

since the input matching paths are edge-disjoint.

A successful trial returns a support omitting the temporarily deleted
edge, so its simple path is different from \(P_a\). Materialize the
support before restoring the edge. Restore using the same immutable
original identifier, even if the proxy lifetime changes, and only
then make the permanent consumption transaction. Each success uses a
new nonempty support, so there are at most \(m\) successes.

If every scan edge fails, every distinct simple source-target path is
excluded: a simple path different from \(P_a\) must omit an edge
of \(P_a\). If part of \(P_a\) was permanently removed already,
an ordinary query cannot return it and needs no temporary exclusion.
Each such group has at most one terminal ordinary failure. Thus all
queries and temporary updates total \(O(m+|A'|)\), even for a
large degree quota.

## 8. The half-layer charge is actually R+1

Let \(R=\lceil\Gamma h_0\rceil\). After a successful support
\(S\), remove it and every input matching path it touches. This
enforces that no two outputs touch the same matching path.

For a comparison half layer, saturated groups contribute at most the
number of returned paths. Every unsaturated comparison path must hit
a permanent removal set, by the failure certificates above.

Partition the removal caused by \(S\) into atoms: each support edge
outside the matching support is one atom, and every matching path
touched by \(S\) is one atom. There are at most \(|S|\) atoms.
A comparison half layer has at most one path hitting each singleton,
by resource disjointness, and at most one path hitting each whole
matching-path atom, by the half-layer blocker condition.

Hence one output accounts for at most \(|S|\leq R\) unsaturated
comparison paths, and

\[
                         |Z'|\leq(R+1)|Z|.
\]

This is stronger than the coarser separate charge \(2R+1\). It
does not multiply by the lengths of the touched matching paths.
Those paths are scanned and permanently removed at most once, with
total physical edge inventory at most \(m\).

## 9. Retained limits

The bridge is valid for the existing positive polynomially bounded
integer-length APSP interface. A comparison threshold can be capped
at \((n-1)\max_e\ell_e\), since it concerns simple paths. The
unweighted expander application satisfies these numerical conditions.

The time is \((n+m+|C|)\exp O(B)\); no additional multiplicative
metric-stretch factor is paid for support extraction. The approximation
and allowed path length still contain \(R\), and the strong-Haxell
outer theorem must pay for them. This audit does not convert the
destructive interface into unrestricted output-sensitive path queries,
and it does not remove the outer dependence on conductance or the
comparison path-length bound.
