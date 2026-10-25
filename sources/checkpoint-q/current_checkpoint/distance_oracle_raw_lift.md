# Raw-cycle quality through the 2026 distance-oracle hierarchy

**Status.** Independent proof of the raw-length and cycle-gradient part of
an alternative deterministic backend. Dynamic degree control, recourse,
and numerical parameter choices are audited separately. This note does
not silently substitute a net-circulation theorem for a raw-path theorem.

The preferred fixed-depth numerical theorem and its current matching
composition are assembled in
[distance backend integration](distance_backend_general_matching_integration.md).
That note supplies the degree-sensitive recurrence, explicit uniform
parameters and occurrence-pool implementation used with this lifting proof.

Primary sources:

* Kyng–Meierhans–Probst Gutenberg–Sulser, *A Simpler and Faster Min-Cost
  Flow Solver via Min-Ratio Cycles from Distance Oracles*, arXiv:2609.23852v1,
  20 September 2026: <https://arxiv.org/pdf/2609.23852v1>.
* Kyng–Meierhans–Probst Gutenberg, *A Dynamic Shortest Paths Toolbox:
  Low-Congestion Vertex Sparsifiers and their Applications*,
  arXiv:2311.06402v1, STOC 2024:
  <https://arxiv.org/pdf/2311.06402v1>.

The first paper is abbreviated **DO26** and the second **KMPG** below.

## 1. Corrections that must be made explicit

There are three distinctions that matter for the claimed interface.

1. **Nonloop and loop core edges differ.** KMPG Definition 3.4 measures
   the stretch of an edge inside one forest component by its simple
   fundamental cycle, and an edge crossing components by its two root
   legs and central edge. DO26 Definition 3.11 must be interpreted with
   this cancellation for self-loops. The uncancelled pair of common root
   legs need not fit in the stored length of a loop.
2. **The displayed length inequality in DO26 Lemma 5.4 is reversed for
   the needed use.** We establish the required domination below directly
   from KMPG Lemma 3.21/Algorithm 5 and the core-edge definitions. It is
   not enough simply to cite that displayed inequality.
3. **Gradients of open edges can have gauge terms.** DO26 Section 4.1
   freezes vertex potentials; its zero-length star edges can therefore
   have nonzero stored gradients. The correct invariant is exact
   preservation of the gradient of a *complete circulation*. A gauged
   star edge can have zero physical traversal and still have a nonzero
   stored gradient that cancels against other gauge terms in the cycle.

There is also a displayed approximation-factor issue in DO26
Theorems 3.24/4.5: the proof charges the crude local extraction loss only
once, after the hierarchy reaches the first useful local candidate. One
must not raise that local loss to the number of hierarchy levels.

## 2. Correct elementary edge lifts

Let `F` be one of the maintained rooted forests in a graph `G`, and let
`e=(u,v)` be an oriented edge with positive length `ell(e)`. Write
`r(u)` and `r(v)` for its two roots.

If `r(u) != r(v)`, the corresponding core edge is a nonloop and has the
explicit oriented parent walk

    F[r(u),u] + e + F[v,r(v)].

The two forest legs lie in different components. Its literal parent
length is

    dist_F(r(u),u) + ell(e) + dist_F(v,r(v))
        <= stretch_upper(e) * ell(e)
        = ell_core(e).

This is precisely the second case of KMPG Definition 3.4 and Definition
3.6. The stretch upper estimate stays fixed while the forest loses edges
and remains a valid current upper estimate by KMPG Lemma 3.5.

If `r(u)=r(v)`, the corresponding core edge is a self-loop. Its correct
parent circulation is

    e + F[v,u],

with the simple forest path. It has literal length at most

    ell(e) + dist_F(u,v) <= ell_core(e).

Appending the two root legs and then retaining their common part twice
would be wrong. Their signed cancellation is performed locally in this
one forest before a raw representation is selected. This requires no
global cancellation of a represented physical walk.

If `e` was itself a forest edge, its loop circulation is zero and can be
discarded. If `e` is a physical self-loop, the forest path is empty and the
single physical edge is the representation.

Zero-length star links between copies of the same pivot have empty
physical representations. Their gauge gradients are treated as in
Section 5 below.

## 3. Raw domination for a lifted forest path

The following elementary strengthening of KMPG Lemma 3.21 is useful.

**Raw forest-lift lemma.** Consider the construction of Algorithm 5 in
KMPG, with a forest on the sparsifier whose selected edges have nonloop
core images. A path in its lifted forest, between the designated images
of its endpoints, has literal parent traversal length at most the sum of
the stored sparsifier lengths on the original forest path. This holds
before any cancellation of physical edge images.

**Proof.** For each vertex occurrence of the child forest, Algorithm 5
creates a separate copy of the direct sum of all parent forest components
rooted at that vertex. These component copies are joined only at their
common root. Each child forest edge is represented by one central parent
edge connecting its two assigned copies.

Contract all component copies to their roots. The result is the child
forest. Hence a simple path in the lifted forest traverses the central
edges corresponding to the unique child forest path, in order, with no
extra central-edge detour.

Within an intermediate copy, the path between its incoming and outgoing
attachment points is no longer than the sum of their two paths to the
root. If the attachments lie in different constituent trees, it is exactly
that concatenation; if they lie in the same constituent tree, their common
backtracking is removed inside a tree. Charge each of these root-leg
lengths to its incident child edge. Together with that edge's central
parent edge, the charge is at most its stored nonloop core-edge length by
Section 2. Summing over the child forest path proves the claim.

Different occurrences of a parent edge can project to the same physical
edge. The proof counts every such traversal separately; no subtraction
of opposite physical traversals occurs. This is therefore a raw-length
statement, not merely a statement about the norm of a projected vector.

This is also the segment-by-segment argument in the stretch proof of
KMPG Lemma 3.21, printed page 32. That lemma additionally provides the
explicit forest maintenance and lifetime-fixed vertex maps used by the
dynamic implementation.

### Why the nonloop condition is available

The forests stored at hierarchy levels are genuine subforests of those
level graphs, so they contain no self-loop. A nonloop core edge has a
central preimage joining different parent components and therefore cannot
have a self-loop as that central preimage. Thus iteratively lifting these
level forests does not require treating a self-loop as a forest edge
between two artificial copies of the same root.

Self-loop candidates are treated separately by the second construction in
Section 2. An implementation may omit loops from a distance spanner and
keep their fundamental cycles among local candidates; loops do not affect
distances. It must retain the candidate rather than silently discard its
possible nonzero gradient.

## 4. Compact expansion of a candidate cycle

At a level `ell`, a core edge consists of two parent forest legs and one
central parent edge. The two forest legs can each be represented by one
path in the already lifted copy of that parent forest. Only the central
edge needs to descend further in the hierarchy. Repeating this procedure
gives at most `2 ell + 1` path or physical-edge pieces per nonloop
hierarchy edge, without expanding every edge on each forest leg.

A loop uses one parent forest path and its central edge, so it satisfies
the same upper bound. A null star link uses no physical piece. If a loop
is encountered while processing an entire candidate, apply its simple
fundamental-cycle representation locally; do not treat it as an open path
between two unrelated root occurrences.

For a candidate containing at most `zeta` explicitly listed hierarchy
edges, the resulting description therefore has

    O(zeta * (Lambda+1))

forest-path or physical-edge pieces. This is the intended compactness of
DO26 Lemma 5.4. The path endpoints are sufficient; no physical walk is
enumerated.

At every descent, Section 2 and the raw forest-lift lemma show that the
sum of lengths of all resulting pieces is bounded by the parent's
certified length charge. Induction gives

    physical raw length of the returned representation
        <= sum of stored lengths of the candidate's hierarchy edges.

The chosen abstract candidate can first be made simple. Coalesce its
signed edge-ID circulation, orient each nonzero coefficient positively,
and decompose it into simple directed cycles. Choose the component with
largest signed gradient divided by its positive stored length, allowing
orientation reversal. This takes `zeta^O(1)` time. Its ratio is at least
the original net ratio, and its abstract literal length equals its norm.
Zero-length components have zero physical projection and zero total
gradient after gauges cancel, and can be ignored.

## 5. Cycle gradients, including frozen potentials

For a parent forest, choose a vertex potential `p` making its stored
forest-edge gradients zero. KMPG forests are decremental within an
instance, so their surviving edges retain this property. An old potential
continues to work when a tree splits; new vertices can receive an explicit
potential, and a split vertex's copies receive the same inherited
potential. DO26 Section 4.1 uses precisely this convention.

For an open edge or path, the stored gradient may differ from its literal
parent gradient by an endpoint-potential difference. For a complete
circulation, these differences telescope at every vertex. Thus

    stored gradient of a hierarchy circulation
        = gradient of its signed parent projection
        = gradient of its signed physical projection.

The two expressions for a loop in Section 2 have the same signed vector:
the common root legs cancel inside their forest. Replacing them by the
simple fundamental cycle therefore preserves the gradient. Removing
backtracking in the lifted forest also preserves the signed gradient.

For star edges, the physical map is empty, but their stored potential
differences participate in this same telescoping identity. Requiring
open-edge physical gradient equality for each such edge would be an
unnecessary and generally false strengthening.

Combining this invariant with Section 4, a candidate `C` at any level
satisfies

    |g_physical^T projection(C)| / raw_physical(C)
        >= |g_level^T C| / sum_e ell_level(e) |C_e|,

whenever its numerator is nonzero. The nonzero numerator ensures that
the physical representation is nonempty and has positive raw length.

### 5.1 Correcting retained spanner edges before zero-link contraction

The zero-alias issue can be handled after sparsification, where the degree
and recourse are bounded. It does not require updating all incident edges
of the unsparsified core graph.

Retain for each edge of the intermediate spanner its origin forest index
`i`, its original parent edge `e=(u,v)`, and its current physical root
endpoints `a=r_i(u)`, `b=r_i(v)`. The frozen-gauge core gradient is

    g_i(e) = g_parent(e) + p_i(u) - p_i(v).

When exposing this retained edge to the contracted child graph, give it
the corrected gradient

    h_e = g_i(e) - p_i(a) + p_i(b).

Because the frozen potential cancels the gradient on every surviving
forest edge, `h_e` is exactly the gradient of

    F_i[a,u] + e + F_i[v,b].

For a self-loop, the common root legs cancel and the same identity holds
for its simple fundamental cycle.

This correction is a single vertex-potential shift on the uncontracted
spanner: use potential `psi(a,i)=p_i(a)` on a root alias and zero on its
star center, and subtract the tail potential/add the head potential.
All star gradients thereby become zero. Every complete circulation keeps
the same gradient. Consequently the zero-length star links may now be
contracted safely, and the child graph has the desired literal-path
gradients.

The correction takes constant time per retained edge edit. KMPG Lemma
3.5(3) says that once a vertex becomes a forest root, it remains a root.
Thus an unchanged surviving component does not spontaneously receive a
different physical root. If an edge endpoint acquires a new root after a
forest split, its output edge endpoint changes too, an edit already
included in the sparsifier's exposed update sequence. A forest-instance
rebuild retires the old records. The origin forest index, parent edge ID,
and both physical root IDs are retained as edge provenance; replacing that provenance is an edge
replacement even if endpoint labels happen to coincide.

Therefore an edge's corrected gradient cannot change invisibly between
its existing exposed edits. Only the retained, bounded-degree spanner
edges need this correction. No scan of the potentially `k` incident
unsparsified core edges and no extra factor `k` on child recourse follows
from the gauge correction.

This lemma was checked independently against KMPG's persistent-root
condition and explicit subgraph/edge provenance. It supplies the missing
gradient bridge between the frozen core sum and the zero-contracted
distance sparsifier.

## 6. A direct quality proof for the ASZ/forest dichotomy

This section avoids relying on ambiguous cycle-segmentation notation in
DO26 Definition 3.15. It uses the source's maintained forest-stretch
guarantee for current ASZ paths.

Lengths and stretch averages here count all occurrences in a concatenated
ASZ walk. This convention is supported directly by the weighted-occurrence
proof of KMPG Lemma 3.12: use the number of occurrences of an edge, rather
than merely the number of walks containing it, in the weight supplied to
the low-stretch forest algorithm. Its weighted summation identities then
hold literally. Each ASZ walk is a concatenation of constantly many simple
shortest paths and an edge, so this convention changes neither the path-set
size nor its stated asymptotic construction cost.

Let `A` be the pivot set, let `p(v)` be a nearest pivot, and write
`d(v)=dist(v,A)`. For a simple oriented cycle `C`, either it is contained
in one local ball neighborhood and can be handled there, or perform the
following segmentation.

Start at a vertex `v_0` and walk along the cycle. From a segment start
`v_i`, stop at the first following vertex `v_{i+1}` outside the strict
ball `B(v_i,A)`, unless the return to `v_0` occurs first. Let `Q_i` be
the resulting cycle segment, let `u_i` be its last vertex before the
endpoint, and replace its prefix by a shortest `v_i`–`u_i` path:

    P_i = shortest_path(v_i,u_i) + (u_i,v_{i+1}).

For a nontrivial ball, this is a generating path of the ASZ construction.
Its length is at most `length(Q_i)`. The circulation `Q_i-P_i` lies
entirely inside the local ball neighborhood and has total length at most
`2 length(Q_i)`. Thus all local difference circulations have total length
at most `2 length(C)`.

For every nonfinal segment, its endpoint lies outside the start ball, so

    d(v_i) <= dist(v_i,v_{i+1}) <= length(P_i).

By the triangle inequality,

    d(v_{i+1}) <= d(v_i) + length(P_i),

and its pivot-extended ASZ path has length at most
`4 length(P_i) <= 4 length(Q_i)`.

For a final truncated segment ending at `v_0`, the weaker bound

    d(v_i) <= length(Q_i)+d(v_0)

gives pivot-extended length at most
`2 length(Q_i)+2 d(v_0)`. Because the cycle is not wholly inside the
ball at `v_0`, `d(v_0) <= length(C)`. Consequently the sum of literal
lengths of all pivot-extended paths is at most `6 length(C)`.

If a segment starts at a pivot, its strict ball is empty and its segment
has a single edge. If the other endpoint is not a pivot, the reversed
edge is a valid generating path and its pivot extension is the reversed
ASZ path. If both endpoints are pivots, both are roots in every maintained
forest and the edge has actual forest stretch one. Its FIXED stored
estimate need not be one if the edge is old. Include all initial
singleton edge paths in the original weighted-halving family, as
specified in
[the disconnected-component wrapper](disconnected_component_backend_wrapper.md),
Section 3. One maintained forest then has stored stretch at most
`alpha` for that singleton. Newly inserted edges alone receive fixed
label one because both endpoints are promoted before their birth.
The inventory contains `B(v,A) union {v}`, with no synthetic child
insertions. These cases avoid assuming that a pivot belongs to its own
strict ball or that an old fixed label is silently decreased.

The pivot legs cancel as signed vectors when all extended paths are
concatenated. Hence the original cycle is the sum of the local difference
circulations and this closed collection of ASZ paths.

For each ASZ path, choose a maintained forest in which its weighted
stretch is at most `alpha`. Split its edge projections into:

* simple fundamental cycles for edges whose endpoints lie in one tree;
* nonloop core edges for edges joining different trees.

The projection telescopes along the path because its endpoints are
pivots, and hence roots. Joining the selected core copies through star
links gives a circulation in the core-graph sum. The combined length
charge of the fundamental cycles and core edges is at most
`alpha` times the total ASZ-path length, hence at most
`6 alpha length(C)`.

All numerators add exactly. The combined positive denominator charge is
at most

    2 length(C) + 6 alpha length(C) <= 8 alpha length(C),

using `alpha>=1`. Averaging proves the desired local/fundamental/core
dichotomy with loss at most `8 alpha`; the more conservative source
constant `20 alpha` is therefore safe. This argument uses the simple
fundamental-cycle length for internal edges, not uncancelled root legs.

An explicit spanner gives the usual analogous dichotomy: either a local
correction cycle has a comparable ratio, or the projected circulation in
the spanner does. A conservative factor `3 rho`, for stretch `rho`, is
enough. Explicit correction walks can be cycle-decomposed as in Section 4.

## 7. The extraction loss occurs once

Let `A_i` bound the vertex- and edge-sparsification loss at level `i`.
Follow the good-circulation alternative until the first level that yields
a local ball, a forest cycle, a spanner correction, or the final small
graph. Every preceding level contributes its factor `A_i`. At the final
chosen location, use its explicit simple cycle, or invoke a crude local
cycle extractor once.

The MST fundamental-cycle argument of DO26 Lemma 3.23 gives loss at most
the number of vertices in that terminal local graph. Calling this bound
`B_loc`, the total loss is

    Q <= B_loc * product_{i=0}^{Lambda-1} A_i.

It is **not** `(B_loc * max_i A_i)^(Lambda+1)`. A local extraction stops
the descent; it is not performed and paid again at every level.

For the source hierarchy parameters, both this loss and the explicit
candidate size are subpolynomial in the physical master size. In a
constant-depth variant, the same formula is the one that must be used
when choosing the size-reduction parameter and the local extraction
budget. Degree-dependent local-ball factors belong in `B_loc` and are
charged once as well.

## 8. Consequence and remaining boundary

Subject to the separately verified dynamic hierarchy and forest recourse
bounds, the candidate selected by the DO26 hierarchy has a succinct
physical representation satisfying the OAI **raw** quality requirement.
No expensive post hoc decomposition of the physical projected walk is
required. The only decomposition is on a short, explicitly listed cycle
inside a hierarchy graph.

The forest lifting uses the constructive KMPG Lemma 3.21, whose vertex
maps are fixed for a record's lifetime and whose maintenance exposes
actual changes. This is a substantially more direct route to the required
interface than inferring it from a generic net-ratio oracle.

This note proves the quality/lifting part. It does not independently
certify the dynamic hierarchy's degree-control feedback, recursive edit
counts, or finite-word parameter recurrence. Those are separate
obligations and should remain explicit before replacing the backend in
the main matching composition.

In particular, KMPG's zero-length alias contraction must be implemented
with the retained-edge correction in Section 5.1. Discarding the frozen
gauge offsets before that correction would be incorrect. The correction
uses existing exposed retained-edge edits; the degree and recourse audit
must retain explicit provenance for those records.
