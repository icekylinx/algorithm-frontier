# Clipped walk reporting and a deterministic dynamic-spanner transfer

**Research proof assembly, 25 October 2026. Clipped reporting and the
full-horizon application have completed root and independent audits.**

This note adds a bounded-length path-reporting interface to the numerical
APSP hierarchy. It then substitutes that interface into the public
dynamic-spanner reduction of Kyng--Meierhans--Zoecklein (KMZ),
[A Simple Dynamic Spanner via APSP, ICALP 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.111/LIPIcs.ICALP.2025.111.html),
Sections 3--4. The reduction asks for paths only after their stored
distance estimate is at most a declared threshold. This weaker interface
is sufficient for its actual analysis.

The resulting time has two terms. If the numerical hierarchy has update
factor `exp O(B)` and a common stretch/reporting envelope
`Gamma = exp O(A)`, the transfer costs

$$
\operatorname{poly}(U)\bigl(m\Gamma+n\Gamma\exp O(B)\bigr),
 \qquad U=\log(N+4),\quad h=\log(U+4).                 \tag{S1}
$$

More precisely, let `gamma_0` be the concrete numerical stretch and
`Q_path` the reporting factor beyond a clipped length cap and polynomial
logarithms. Choose `Gamma >= gamma_0 max(1,Q_path)` as the common
envelope, but continue to use **gamma_0** in the actual acceptance
threshold. The positive no-reset implementation has `Q_path=poly(U)`;
the positive-port implementation below has `Q_path=exp O(dh)`. Both
have the stated logarithmic envelope `A` at the chosen parameters.

Here the input is initially empty, has a fixed set of `n` vertices,
receives at most `m >= n` edge insertions and at most `n` deletions,
and has polynomially bounded history under the declared master `N`.
The maintained unweighted spanner has stretch, size, and total recourse
bounded respectively by

$$
O(\Gamma\log(n+4)),\qquad
 O(n\Gamma\log(n+4)),\qquad O(n\Gamma\log(n+4)).        \tag{S2}
$$

No ordinary simple-path query with time proportional only to the final
simple path length is asserted. Nor is the first term of (S1) replaced
by `m` when comparing two different stretch choices. The public
comparison and current-literature check are separate obligations in
Section 8.

## 1. A positive native hierarchy

Use the uncontracted Steiner-core graphs `J` from
[decremental strong forest proof](../../problems/decremental-strong-forest/proof.md), Sections 2--5, for the numerical
APSP hierarchy. The full-forest pools in that note are unnecessary here.
The native child graph has only two kinds of edges:

* a selected real parent edge at its physical parent endpoints, with
  its actual parent length;
* a compressed path in a stable parent forest, with its exact path
  length and current path descriptor.

Every native edge consequently expands to a **nonempty** parent path.
There are no native null edges and no inter-level port resets. The typed
nulls of the strong-forest lift are not edges of these numerical graphs.
Every native edge has a lifetime ID. A changed compressed path retires
its old ID; its path is immutable while that ID remains alive.

Child vertices use parent native identities. A period keeps at most one
child identity per parent identity, including isolated retained ghosts.
An original root degree at most three gives

$$
\Delta_j\le 3Q^j,\qquad \log\Delta_j=O(jh),
 \qquad Q=U^{O(1)}.                                  \tag{S3}
$$

These claims include active-root inventory, first-touch activation of
initially small components, and the actual-size base case. In particular,
one does not expose every private root of every untouched small component.
The relevant current exact local paths are those described next.

### 1.1 Local query witnesses

At a nonbase level retain its nearest-pivot forest and a shortest-path
tree for each strict pivot ball. At an actual-size base retain one exact
shortest-path forest per source, or equivalent next-hop tables. Initially
small untouched components have their own exact tables and paths.

The current-checkpoint center interface bounds both strict balls and
inverse clusters by `k poly(U)`. The future-path inventory, endpoint
promotion, and oldest-center tie convention maintain these local trees
in `k^{O(1)} poly(U)` additional local work; see
[destructive-apsp-path-support-extractor.md](destructive-apsp-path-support-extractor.md), Section 2.1. This is a local
family, not a family recursively copied at every level. Native degree
costs are conservatively paid by fixed powers of `Delta_j`.

A distance query uses the KMG Algorithm 6 logic. It follows the two pivot
chains, and terminates when one endpoint is in the other's strict ball,
at a local untouched-component case, or at the exact base. Along with
the estimate, retain the at most `2d+1` oriented native tree-path
descriptors: the pivot legs and the terminal exact path. Their total
expanded root length is at most the estimate. A strict-ball terminal
path must come from its own stored shortest-path tree; it is not silently
substituted by a path in the nearest-pivot forest.

The descriptors take `poly(U)` time to obtain. Their paths can be
enumerated one native edge at a time with polynomial-logarithmic overhead
per edge, by parent pointers, exact next-hop tables, or ordinary dynamic
tree path iterators. No fresh `k`-vertex search is done during a query.

## 2. Clipped reporting lemma

**Lemma.** On a settled hierarchy with positive integral root lengths,
given a query estimate `Dhat <= R`, the represented root walk and a
literal simple path between the query endpoints can be reported in

$$
(R+1)\operatorname{poly}(U) . \tag{S4}
$$

The simple path has length at most `Dhat`. Equal endpoints return the
empty path. Disconnected pairs have no finite accepted estimate.

**Proof.** Enumerate each of the local descriptors from Section 1.1.
Expand a native edge above the root through its stored nonempty parent
path, recursively. Consider the resulting expansion forest, whose
leaves are individual root-edge occurrences. Every internal edge
occurrence has at least one child occurrence. Every leaf has at most
`d` ancestors. Charging each internal occurrence to any descendant
leaf, at its own level, bounds the number of expansion records by
`(d+1)` times the number of root-edge occurrences. Descriptor headers
add `O(d)` records. Since every root edge has length at least one,
the number of root occurrences is at most the walk length, hence at
most `Dhat <= R`.

Maintain a stack of the walk's visited root vertices and a deterministic
dictionary from currently stacked vertex IDs to their positions. If
the next vertex already occurs on the stack, remove the resulting
closed suffix. Each input occurrence is pushed and removed at most
once. This deterministic loop erasure produces a simple path, preserves
its endpoints, and cannot increase its positive length. Its work is
linear in the enumerated walk up to dictionary logarithms. This proves
(S4).

Queries see one settled version. No structural update runs while its
descriptors are being enumerated. Old edge metadata remains available
until the update transaction retiring that edge and all dependent
records has finished; no descriptor is reused after that transaction.
One therefore needs neither a path valid across future updates nor a
global persistent copy of every historical forest.

The reported simple path may be much shorter than its represented walk.
Equation (S4) deliberately pays for the accepted length budget, not only
for the final path's cardinality.

## 3. Numerical maintenance and the two retained implementations

For the positive no-reset hierarchy of Sections 1--2, retain the
conservative old `K^2 g` repair work already audited in
[decremental strong forest proof](../../problems/decremental-strong-forest/proof.md). Its selected transcript
and all stable-forest cut/root logs fit
`P_j = P Delta_j^{O(1)} poly(U)`, where

$$
g=O((p+r)h),\quad
 f=O(U/p+U/r+r^2h+(p+r)h),\quad
 \log P=O(U/K+g+h).                                  \tag{S6}
$$

The numerical recursion pays local tree paths and actual base tables
once in local work, and retains the initial selected credit that may
become child edits after initialization. The same coupled recurrence
as Section 13 of that note gives

$$
\begin{aligned}
 B_{\rm noreset}&=O\bigl(x+f+K^2g+d(U/K+g+h)+d^2h\bigr),\\
 A&=O(dKg+dh),\qquad d=O(U/x).
 \end{aligned}                                             \tag{S7}
$$

The term `d^2 h` pays all fixed native-degree powers from (S3).
There is no full-forest-pool copy factor here, because only native
query descriptors are retained. With `p=r=t`, `K=t^2`,
`x=Theta(U/t)` and `d=O(t)`, this gives

$$
B_{\rm noreset}=O(U/t+t^5h),\qquad
               A=O(t^4h).                              \tag{S5}
$$

This is sufficient for the fully dynamic five-sixths application in
[dynamic spanners proof](../../problems/dynamic-spanners/proof.md). That main application does not
require a new high-degree normalized-repair adapter.

For the stronger deletion-bounded time/stretch curve in Section 7,
instead use the already audited normalized **positive-port** APSP
hierarchy from [apsp frontier proof](../../problems/apsp-frontier/proof.md) and
[same-stretch-apsp-comparison-and-root-audit.md](same-stretch-apsp-comparison-and-root-audit.md). Its proven envelopes are

$$
B=O(U/t+t^3h),\qquad A=O(t^4h).          \tag{S8}
$$

That implementation has intermediate positive connectors, so its
reporting uses the scaled enumeration lemma in Section 8, with the
additional factor `Q_path=exp O(dh)`. This is smaller than its
logarithmic stretch term. It does not require applying normalized
repair at growing native degrees. All size-shrink guards retain slack
at the displayed parameter choices.

## 4. Arbitrary degree at the outermost graph

The spanner's oracle graph need not have bounded degree. At its root
apply the current-incidence positive binary-tree adapter from
[apsp frontier proof](../../problems/apsp-frontier/proof.md), Section 5, once. Each original vertex
has a permanent query handle; its actual current incidences are leaves
of a balanced binary tree. Connectors have unit length. Original
unweighted edges become leaf-to-leaf edges of a common length `H`,
where `H` is a power of two at least `C log N`.

The native maximum degree is three. One oracle edge update changes
`poly(U)` native records. Current live port trees use only their actual
incidences. Rotations reuse their internal nodes; births and retired
isolates are charged to their actual creation and eventual period
replacement. If a lower provider retains a retired isolated native ID
until its next replacement, that retained ID is charged too; it is not
included in any positive query path. There is no master-sized port tree
for each original vertex.

For distinct connected original endpoints,

$$
d_{\widehat H}(u,v)
 \le H^{-1}d_{G_0}(q_u,q_v)
 \le2d_{\widehat H}(u,v).                              \tag{S9}
$$

The first inequality projects away connectors. A simple original
`b`-edge path uses `O(b log N)` connectors when lifted, proving the
second. Scale the numerical answer down by `H` and absorb the factor
two in `Gamma`. A clipped query with scaled estimate at most `R`
expands a native walk of length at most `H R`; (S4) is therefore still
`(R+1) poly(U)`. Project away connectors, then loop-erase using original
vertex IDs. Its resulting simple original path has length at most the
scaled estimate.

This single root adapter has no connection to the internal typed-null
forest edges of the strong-SSSP construction. Its positive connectors
are enumerated and paid, and disappear only in the final projection.

## 5. An explicit low-recourse spanner implementation

The following is the public KMZ greedy/congestion reduction, with its
route retirement and a harmless integer threshold made explicit. Let

$$
L=2\lceil\log_2(n+4)\rceil,\qquad
 R=\lceil\gamma_0 L\rceil,\qquad
 \tau=\lceil m/n\rceil+1\ge2.                         \tag{S10}
$$

Maintain `H` and its eligible subgraph `Hhat`. Every live input edge
has one stored simple embedding path in `H`, of at most `R` edges.
Each edge of `H` maintains the inverse list of these current paths.
An edge in `Hhat` has load strictly below `tau`. Once its load reaches
`tau`, remove it from `Hhat` for the remainder of its physical lifetime;
keep it in `H`. Decreasing load does not reactivate it.

**Assign an edge.** Query the numerical oracle on `Hhat`. If its estimate
is at most `R`, use the clipped reporting interface and store its simple
path. Increment the path's edge loads and remove newly saturated edges
from `Hhat`. Otherwise insert this edge into `H` and `Hhat`, and store
its one-edge identity path. Its initial load is one, below `tau`.
The path query and subsequent saturation deletions are sequential; the
path is completely materialized before the oracle changes.

For the girth argument one can equivalently test against the unrounded
threshold `gamma_0 L`. We use that threshold for the decision and `R`
only as an integral reporting bound. Thus insertion into `Hhat`
certifies that its pre-insertion true endpoint distance exceeds `L`.

**Delete an external edge.** First obtain all still-live input edges
whose routes use it. Remove the deleted edge's own route and, if it is
in `H`, all affected routes from their inverse lists. Delete the
physical edge from `H` and `Hhat` where present. Then reassign the
affected still-live edges, each once. If the deleted edge was outside
`H`, only its own route must be retired. A different edge already in
`H` has its identity route, so cannot be among the affected reassignment
requests. Load decrements do not reintroduce blocked edges.

All names refer to physical edge lifetimes. Parallel edges are distinct;
an input self-loop may be discarded because it does not affect positive
distances. Standard dictionaries maintain route lists and inverse lists
in polynomial-logarithmic time per changed incidence.

These details implement the prose and analysis of KMZ Section 4.
In particular `Hhat` insertion adds to its current eligible subgraph;
it does not replace that subgraph by all of `H`. Physical deletions
really remove the edge from both maintained graphs. Old routes are
retired even on deletion of an edge outside the spanner.

## 6. Complete count for the deletion-bounded interface

Every eligible edge has load below `tau` before a new simple route is
installed. That route increases its load by at most one. A saturated
edge is never again used by new routes during its lifetime. Thus every
spanner edge has load at most `tau`, even after it becomes ineligible.
For `D <= n`, the total number `Acall` of assignments satisfies

$$
Acall\le m+D\tau\le4m.                                \tag{S11}
$$

At most `R Acall` route-edge incidences are ever installed. Each edge
lifetime that becomes blocked has received `tau` incidences before
its first blocking event. Charging those incidences at that event gives
at most `R Acall/tau=O(nR)` blocked lifetimes in total. The eligible
graph has girth greater than `L`: a new edge enters it only when its
true endpoints were farther than `L`, and subsequent eligibility
changes are deletions. The elementary high-girth bound therefore
gives `O(n)` eligible edges at every time. Consequently

$$
|H|=O(nR),\quad
 \#\text{insertions into }H=O(nR+n),\quad
 \operatorname{recourse}(H)=O(nR).                      \tag{S12}
$$

Here only the at most `n` external deletions remove edges from `H`.
Each `H` edge enters the oracle's eligible graph once and leaves it
at most once. Thus there are `O(nR)` oracle edge updates. The initial
empty oracle with its `n` vertex handles is charged `n exp O(B)`.
Each assignment has one numerical query and at most one clipped path
report, costing `R Q_path poly(U) <= Gamma L poly(U)`. Every installed route incidence is later
retired at most once, so inverse-list and load maintenance has the same
total bound. This proves (S1)--(S2), including initialization.

The smaller recourse bound is the one proved by the published KMZ
**Corollary 10**. Its **Lemma 11** gives the corresponding time bound
for a general congestion threshold. The published Theorem 12 displays
an additional update-factor multiplier in its recourse statement;
(S12) uses the direct counting argument and Corollary 10, rather than
needing that looser displayed expression.

The root oracle's positive active graph has `O(n)` edges throughout.
Its current-incidence adapter has `O(n)` live port records. Actual
retired isolates and all internal update records are additionally
charged through their births and replacements. The total native
oracle transcript is `O(nR poly(U))`; using `N^c` rather than `N`
as an encoded-history cap, for a fixed constant `c`, covers it.
Every structural length has polynomially many bits in `U`: tree-path
sums through `d` levels use `O(Ud)` bits. All such arithmetic and
length-bucket overhead is included in `poly(U)`.

### 6.1 Weighted graphs

For positive integer edge lengths in a fixed polynomial range, use
dyadic weight classes and run an unweighted spanner independently in
each class. The union has twice the unweighted stretch, and pays the
number of classes in size, recourse, initialization and time. A route
with `b` edges in the class of an original edge `e` weighs at most
`2b length(e)`. This avoids reporting a weighted walk by paying a
pseudopolynomial factor equal to its numerical length. All clipping
queries remain in the unweighted class graph, with cap `H R` after
the one root degree adapter. KMZ's published Remark 3 allows this
standard extension.

## 7. Explicit deletion-bounded tradeoffs

At the common stretch scale

$$
A_0=U^{5/7}h^{2/7},
$$

take `t=Theta((U/h)^{5/28})` in (S8). The research hierarchy gives

$$
A=O(A_0),\qquad B=O(U^{23/28}h^{5/28}).                \tag{S13}
$$

The resulting total spanner time is

$$
m\exp O(A_0)+n\exp O(U^{23/28}h^{5/28}),              \tag{S14}
$$

with size and recourse `n exp O(A_0)` and stretch `exp O(A_0)`.
The `A_0` contribution to the second exponent is of smaller order.
All suppressed factors are polynomial logarithms or fixed constants.

At `t=Theta((U/h)^{1/5})`, (S8) instead gives

$$
A,B=O(U^{4/5}h^{1/5}),
$$

so time is `(m+n) exp O(U^{4/5}h^{1/5})` and size/recourse are
`n exp O(U^{4/5}h^{1/5})`. This is a balanced point, not an automatic
improvement over (S14) on dense update sequences: the first term of
(S14) can be much smaller. Both statements here retain `D <= n`.

## 8. Public clipped-path comparison

The reconstructed public numerical APSP hierarchy from
[public-apsp-joint-retuning-audit.md](public-apsp-joint-retuning-audit.md) uses positive port adapters at
its recursive boundaries. Its native connectors project to empty
parent walks, so Section 2's nonempty-expansion proof does not apply
literally to that hierarchy. It still has a sufficient clipped bound.

Let `H_j=poly(U)` be the fixed positive scale at boundary `j` and
let `sigma_j=product_{a<j} H_a`. An accepted numerical answer is a
sum of positive local leg lengths divided by the appropriate `sigma_j`.
When a higher-level path is expanded one level, its total lower-level
length is at most its length divided by that boundary scale; connector
projection deletes a nonnegative contribution. It follows by induction
that the aggregate native walk enumerated at level `j`, including
all local query legs at that level, has length at most `sigma_j R`.
All native lengths are positive integers. Therefore

$$
\#\text{enumerated native records}
       \le R\sum_{j=0}^d\sigma_j\operatorname{poly}(U)
       \le R\exp O(dh).                                \tag{S15}
$$

The same local exact ball/base trees and selected-core physical
root-leg witnesses are already present in the public source interfaces:
KMG Theorem 3.1, property 5 in its proof, and Algorithm 6. Each witness
is enumerated in time proportional to its current native output length.
The source's Claim 4.4 supplies the small descriptor query. Stable
lifetimes and settled-version enumeration work exactly as in Section 2.
After final loop erasure (S15) is a public clipped-simple-path bound.
It does not rely on the new colored pool lift.

The eligibility threshold uses the oracle's actual numerical stretch.
The extra factor in (S15) enters reporting work, not a second artificial
increase of that threshold. At the level of asymptotic envelopes it is
smaller than the relevant stretch term.

For the derived public point `d=O((U/h)^{1/7})`, the extra `dh`
in (S15) is smaller than its logarithmic stretch `A_0`. Thus the
fair public transfer is

$$
m\exp O(A_0)+n\exp O(U^{6/7}h^{1/7}),                 \tag{S16}
$$

with the same size, recourse, stretch scale, and deletion horizon as
(S14). The two hidden stretch constants can be matched against a
common specified envelope by the fixed parameter constants.

The trivial spanner `H=G` already wins whenever the actual living-edge
cap `M` fits the allowed `n exp O(A_0)` output size. Thus the case
`m=Theta(n)` by itself is not a meaningful new spanner improvement.
For a nontrivial deletion-bounded comparison, one can consider a
history reaching density `M/n` with logarithm much larger than `A_0`
but much smaller than `U^{23/28}h^{5/28}`. The output is then actually
sparser than the input, while the improved second term of (S14)
still determines its work. For polynomially dense insertion histories,
the common first term may instead dominate. The unrestricted-deletion
comparison is proved separately in [dynamic spanners proof](../../problems/dynamic-spanners/proof.md).

This is a **derived public composition**, not a printed theorem or
a claim of the best possible public parameter choice. The independent
current-literature check is [dynamic-spanner-public-baseline-audit.md](dynamic-spanner-public-baseline-audit.md).
The published KMZ batching extension is treated explicitly next.
