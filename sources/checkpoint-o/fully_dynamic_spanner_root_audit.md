# Root audit of clipped reporting and the fully dynamic spanner

**Independent mathematical and source audit, 25 October 2026.**

The construction in `fully_dynamic_spanner_five_sixths.md`, Sections
1--6, passes this root audit. It gives the following research envelope
for an arbitrary undirected graph, under the retained research-provider
imports:

\[
 E_5=\exp O(U^{5/6}h^{1/6}),\qquad
 U=\log(N+4),\quad h=\log(U+4).
\]

The maintained explicit spanner has stretch at most E_5 and at most
n E_5 edges. Over an initial graph with m_0 edges and any subsequent
I insertions and D deletions within the declared history cap, total
work is at most (n+m_0+I+D) E_5, while total output recourse is at most
(n+D) E_5. The time assertion is amortized. All guarantees concern
settled states after complete external updates.

This audit supplements `fully_dynamic_spanner_independent_audit.md`.
It does not constitute formal verification or independent external
peer review. The result is a research proof assembly with explicitly
identified public and research dependencies.

## 1. The actual client needs a clipped path interface

The root directly read the published
[KMZ ICALP 2025 paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.111/LIPIcs.ICALP.2025.111.html),
including Lemma 11, Lemma 13, Claims 14--17, and Theorem 18. Its
published Section 5 is more informative here than arXiv v1.

The reduction asks for a path only when its numerical distance estimate
is at most Gamma times a logarithmic threshold. Its running-time proof
then pays for that entire threshold. Therefore reporting a walk within
the accepted budget, followed by explicit loop erasure, suffices. It is
unnecessary to assert time proportional to the size of the final simple
path when that path can be much shorter than the represented walk.

The no-reset numerical hierarchy has only positive native edges. Each
edge maps to a nonempty path in the immediately preceding native graph.
Selected real edges use their own physical parent IDs; compressed stable
forest paths have exact lengths and lifetime-specific path handles.
Typed null edges belong to the separate strong-forest lift, not to these
numerical graphs.

A query is represented by at most O(d) nearest-pivot, strict-ball, and
base shortest-path descriptors. Strict-ball paths use their own exact
local trees. They are not replaced by nearest-pivot paths. The prior
local-tree inventory and inverse-cluster bounds pay for maintaining
these witnesses; no new local graph search is charged to a query.

Expanding an accepted walk of root length at most R creates at most
O(d R) native edge occurrences. At each level, a native occurrence has
at least one original positive-edge descendant; charge it to one such
descendant at that level. There are at most d levels and at most R
original edge occurrences because original native lengths are at least
one. Descriptor headers add only O(d). A stack and a deterministic
dictionary erase loops in time linear in this enumeration up to a
polynomial logarithmic factor.

For an arbitrary-degree oracle graph, the single root degree adapter
has positive unit connectors and real edges scaled by H=poly(U).
An accepted original estimate R has native budget H R. Enumerate that
budget, project away connectors, and erase loops by original vertex
ID. This retains R poly(U) work and an actual current original path.
No recursive reset, empty native edge, or uncharged connector walk is
introduced into this argument.

The public comparator can also supply clipped paths. Its repeated
positive port scales cost an additional exp O(dh) in enumeration.
This factor is explicitly retained in its work comparison. The lack of
a separately stated ordinary path API is not used to disqualify it.

## 2. A single instance has an unconditional transcript bound

Fix a congestion cap K at least two. Every current original edge has
one stored simple embedding path. A path increases a given edge's load
by at most one. Once the load reaches K, that edge leaves the eligible
query graph permanently for its present lifetime. Load decreases do not
reactivate it. Hence deleting one edge invalidates at most K current
routes, regardless of how many routes have existed historically.

For F genuine input insertions, including the initial seeding, and D_0
genuine deletions, the number of route assignments is at most F+K D_0.
Each assignment has at most R incidences. A blocked edge lifetime can
be charged K of these incidences, so the number of blocked lifetimes is
at most R(F+K D_0)/K. Eligible edges have girth greater than the chosen
logarithmic threshold: a numerical rejection implies that their true
pre-insertion endpoint distance exceeded that threshold. The usual
girth bound gives O(n) eligible edges.

Consequently current output size and total output insertions of one
instance are bounded by

\[
 O(n+(R/K)F+R D_0).
\]

The insertion count also pays D_0 genuine removals. Route-list and inverse
list retirement is charged to records when they are created. The inner
APSP structure sees only eligible-edge updates, never every edge of the
possibly dense instance input. Its initialization and update work is
therefore exactly of the form used in (F3) of the main note.

Physical edge lifetimes have distinct IDs. Deleted nonspanner input
edges also retire their own stored routes. Artificial removal of an
entire instance at a rebuild is not recursively treated as genuine
physical deletions. These distinctions are necessary for the count.

## 3. The nested clocks eliminate dense repeated rebuilding

Let M bound the number of simultaneously live original edges. It is
not the cumulative insertion count. Set

\[
 s=\max(1,\lceil\log_K(M/n)\rceil),\qquad
 M'=nK^s,\qquad t_i=M'/K^i.
\]

The final clock is n, and each parent clock is K times its child's.
Each clock counts only original physical deletions. When a clock fires,
retire the corresponding layer and all descendants, and seed their
replacements from actual current parent edges. The number M' is never
materialized as a padded graph.

A parent's rebuild always coincides with a child's rebuild boundary.
Within one child's lifetime the parent therefore only loses edges to
original deletions. Its insertion count, including seeding, satisfies

\[
 \text{initial edges}+\text{later insertions}
   =\text{current edges}+\text{genuine deletions}.
\]

If the current parent cap is V_{i-1}, this bounds every child prefix
by V_{i-1}+t_i insertions and t_i deletions. The single-instance bound
then inductively gives

\[
 V_i=(cR)^i M'/K^i,
 \qquad V_s=n(cR)^s.
\]

This argument also applies while a seed is being inserted. It permits
arbitrarily many insertion-only operations consistent with the live
capacity bound. No insertion-to-deletion balance is assumed.

## 4. The total-volume account pays each actual initialization

Let F_i count all layer-i input insertions over all its incarnations,
and O_i all its output insertions. Each layer has
1+floor(D/t_i) instances; since t_i is at least n, its total vertex
initialization charge is at most order n+D. Summing the unconditional
single-instance bound gives

\[
 O_i\le c[n+D+(R/K)F_i+R D].
\]

The first layer has

\[
 F_1\le m_0+I+(D/t_1)M\le m_0+I+DK.
\]

The initial dense input is paid by m_0. An empty graph has no initial
capacity-sized seed. Every later seed is charged to a completed clock
interval.

For each subsequent layer, ordinary parent insertions are already in
O_i. The first initialization is paid by the parent's actual initial
output. Later seeds contribute at most

\[
 (D/t_{i+1})V_i=DK(cR)^i.
\]

It is safe to count a simultaneous parent/child replacement twice in
this inequality. The resulting recurrence yields

\[
 F_i\le(c'R)^i(m_0+I+n+DK).
\]

Combining this with the single-instance work bound proves

\[
 T\le(n+m_0+I+D)K(c'R)^{O(s)}
             (\alpha+Q_{\rm path})\operatorname{poly}(U).
\]

This pays all dense seed scans, all n-handle numerical initializations,
all stored route incidences, and all retirements. In particular, the
forbidden uncharged term M D/n never appears.

## 5. Output recourse is separate from internal work

The final layer is rebuilt every n original deletions. Between these
rebuilds, it loses an output edge only to a genuine deletion. Its
ordinary output insertions are bounded by its maximum size plus the
number of those removals. A hard rebuild changes at most the sum of
the old and new output sizes. Thus its total recourse is

\[
 (n+D)(cR)^{O(s)}.
\]

This bound is independent of I except through the declared history and
capacity parameters. It is not a worst-case recourse bound per update.
Only actual original graph edges appear in the published spanner;
inner degree-adapter copies are private. Physical parallel edges are
allowed, while two parallel eligible edges would form a forbidden
short cycle. Self-loops can be discarded.

Separate unweighted dyadic classes extend the result to positive
polynomial-range integer lengths. Each original edge is in one class.
Class spanners give an extra factor two in stretch; their union adds
only polynomial logarithmic factors to work, size, and recourse. No
walk is enumerated proportionally to the magnitude of an edge weight.

## 6. The five-sixths parameter balance uses the conservative import

The inner numerical hierarchy can use the already audited conservative
repair term K_repair squared times g. With

\[
 p=r=d=\Theta(t),\quad K_{\rm repair}=\Theta(t^2),
 \quad x=\Theta(U/t),
\]

its logarithmic update overhead and approximation are

\[
 B=O(U/t+t^5h),\qquad A=O(t^4h).
\]

No new extension of the normalized repair to growing native degree is
needed for the main spanner theorem. The internal degree charge d^2 h
is smaller than this B. The external arbitrary-degree adapter is paid
once per numerical instance.

Set t of order (U/h) to the one-sixth power and log K of order U/t.
Then s=O(t), B=O(t^5h), and s(A+h)=O(t^5h). These quantities pay,
respectively, numerical work, the outer clock factor, and cumulative
stretch/size/recourse. They all equal the five-sixths scale.

All local shrink guards and the requirement K much larger than R have
slack for sufficiently large inputs. Actual small inputs are handled
directly. Intermediate record counts fit a fixed polynomial enlargement
of the declared cap, changing U by a constant factor only.

## 7. Meaning of the public comparison

The public numerical family has

\[
 B_{\rm pub}=O(U/t+t^6h),\qquad A_{\rm pub}=O(t^5h).
\]

Using the same outer construction gives a simultaneous six-sevenths
time/stretch/density envelope. At the smaller common final stretch
and density scale U to the five-sixths times h to the one-sixth,
choose t of order (U/h) to the five-thirty-sixths power. Its certified
time envelope becomes U to the thirty-one-thirty-sixths times h to
the five-thirty-sixths. The research bound is five-sixths at that same
final scale. These are asymptotic envelopes, with fixed constants
chosen against a declared admissible output bound.

The variable-parameter lower envelopes in the companion audit concern
only optimization of the displayed positive-charge accounting. They
are not lower bounds for dynamic spanners or for the actual running
time of a public algorithm. Other public guarantees, including
worst-case or much smaller stretch, retain their separate scope.

Finally, if the live graph is already within the permitted output size,
H=G is a trivial exact spanner. Its total recourse is m_0+I+D, at most
M+2D. The nontrivial application is the density regime where the graph
can be larger than the allowed sparse output. The matching objective
remains deterministic exact maximum matching in arbitrary graphs;
this spanner result is a separate transfer and does not change its
four-fifths exponent.

