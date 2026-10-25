# Verification note

**Curated source path:** `sources/checkpoint-o/tracked_terminal_flat_spanner_root_audit.md`

The source audit follows.

# Root audit: the direct four-fifths dynamic spanner

**25 October 2026. Mathematical proof assembly accepted after root and
independent internal audits.**

This audit covers the complete construction in
**tracked_terminal_flat_spanner_four_fifths.md**, Sections 1--9,
the local compression lemma in
**dynamic_marked_forest_short_path_union.md**, and the imports named
below. The independent full audit is
**tracked_terminal_flat_spanner_independent_audit.md**.
This is an internal mathematical review of a research construction,
not formal verification, external peer review, or an implementation
benchmark.

## 1. Accepted statement and scope

Put U=log(N+4), h=log(U+4), and

\[
                   E_4=\exp O(U^{4/5}h^{1/5}).
\]

For an arbitrary-degree undirected graph on a fixed set of n original
vertices, initial edge count m_0, and subsequent I insertions and D
deletions within a declared polynomial history cap, the construction
maintains an explicit current-edge spanner with stretch E_4, current
size n E_4, and total initialization/update work

\[
                       (n+m_0+I+D)E_4.
\]

The same expression is a safe bound on total output recourse. The
initially empty specialization is (n+I+D)E_4. Initialization credit
can produce later forest changes, so m_0 cannot simply be removed
from the general recourse expression. This construction makes no
insertion-independent or worst-case per-update recourse assertion.

The main proof is for unweighted graphs. Independent unweighted
dyadic classes extend it to positive polynomial-range integer lengths
with a factor two in stretch and polynomial logarithmic extra work.
Parallel physical edge lifetimes and disconnected graphs are allowed;
self-loops may be ignored. Output is published after an external
update has settled. The result includes polynomially dense input
graphs. If the whole current input already fits the output cap, the
elementary exact spanner consisting of the input itself remains a
better baseline.

This is a separate graph-algorithm transfer. It changes neither the
four-fifths exact general-matching exponent nor the stronger
insertion-independent recourse of the five-sixths spanner.

## 2. The imported forest interface is sufficiently strong

The construction uses the already audited normalized positive-port
numerical APSP hierarchy. It does not depend on an unproved normalized
repair extension for the newer high-degree no-reset hierarchy.
Its parameter bounds are

\[
 k=2^x,\quad x=\Theta(U/t),\quad d=O(t),\quad
 B=O(U/t+t^3h),\quad A=\log\gamma=O(t^4h).
\]

The flat family is the one maintained in
**destructive_apsp_path_support_extractor.md**, Sections 2--2.2,
with **destructive_apsp_independent_audit.md**. It includes every
native nearest-pivot forest, every strict-ball source tree, and
every actual-size base source tree. Exact local trees for initially
small untouched components are explicitly included. Their local
inventory has the same fixed polynomial-in-k allowance.

Each local family is lifted once from its birth level. The recurrence
adds a local k-polynomial term and multiplies already lifted input
only by the lift factor P. It does not multiply by k anew at every
ancestor. The coupled initialization/update analysis retains the
initial selected credit and counts all unused pool copies, auxiliary
nodes, historical isolates, and later generated child edits. Thus the
complete native and flat transcript costs
(n+m_0+I+D) exp O(B).

The arbitrary-forest metric proof in
**separated_metric_forest_and_strong_sssp.md**, Section 5, supplies
one distinguished current handle for each input-node occurrence and
the required path inequality after dividing by cumulative positive
port scales. Equal physical images do not identify distinct forest
occurrences. At the root, actual root-native edges keep their root
lengths: H for an original graph edge and one for a root port
connector. Generated projection nulls have length zero. An
intermediate positive connector that projects away is a generated
null, not an additional positive root edge.

These distinctions ensure that a represented query constituent has
the asserted root-flat length and compatible physical endpoints.
No ordinary output-sensitive simple-path interface is imported.

## 3. Tracking n query traces does not feed back into the hierarchy

The outer degree adapter may have Theta(n+m) current native vertices.
The observer nevertheless starts with only the n permanent original
query handles. At each level a marked nearest-pivot component
contributes at most one exposed child query handle. Hence every
tracked set S_i has at most n vertices.

A membership change in S_i toggles at most one next-level contribution.
A native forest cut, link, exposed-pivot change, or root change affects
only constantly many component contributions. Therefore, if b_i is
the number of membership changes and l_i is the complete native
component/pivot transcript,

\[
                         b_{i+1}\le b_i+O(l_i).
\]

The coefficient on b_i is one. Summing through depth incurs a depth
factor, with no multiplicative branching by k. The observer does not
promote native pivots, change native edges, or rebuild the hierarchy.

A transcript may temporarily contain components with zero or several
pivot labels. The specified observer uses the minimum eligible
exposed pivot, independently of the mark count, until the native
state settles. This preserves one output per positive-mark component
and the same event bound. Exposure is enabled after the child handle
and its observer node exist and disabled before retirement. The
settled component has its intended unique pivot. These private
intermediate choices never feed into the numerical algorithm.

Initially small untouched components can have a private pivot with no
child handle. They terminate in their explicit local exact trees.
Their first real activation exposes the old pivot before propagation
is enabled. No absent child vertex is allocated merely to pretend
that a trace continues.

## 4. Marks count source-tree nodes, with explicit ownership

In a nearest-pivot forest mark each tracked node and its pivot. In an
active local source tree, mark every native node of that tree. At
most n sources are active at a level, and a local tree has only
k^{O(1)} poly(U) nodes. Thus the total marked occurrence inventory is

\[
                       Q_{\rm mark}\le n k^{O(1)}\operatorname{poly}(U).
\]

Marking all nodes of an active source tree avoids maintaining a
moving distance-eligibility set. A source activation or deactivation
pays its actual local tree inventory once. Node births and retirements
read the active-source flag. Flat edge changes require no bulk scan
of a marked component. These observer events multiply the completed
native transcript by at most one fixed polynomial in k, which is
absorbed in B.

The canonical-owner issue is closed explicitly. Releasing an input
node's pool index may leave its physical pool root allocated as an
unused ghost. Its mark and owner tag must disappear on owner release,
not only on physical node retirement. A new owner is installed only
after that removal. The owner claim/release records are already
constant-size consequences of the input-node and pool-assignment
transcript. Only the distinguished handle carries the tag; unused
copies are not silently promoted to additional terminals.

## 5. General dynamic marked-forest compression

The local lemma was checked for both links and cuts. The compressed
minimal subtree connecting marked vertices has O(q) records for q
marks and retains every marked vertex. Its virtual edges represent
edge-disjoint original forest paths.

Insertion of a mark locates its attachment to the old marked subtree
using the first nonzero virtual-edge ID on a path to any old mark.
It may split one virtual edge and add one branch. Deletion removes
one leaf branch or suppresses one degree-two marked vertex, with at
most one further endpoint suppression. A cut inside the marked
subtree retires its unique containing virtual path before the
physical cut; its abandoned unmarked tails need not be traversed.
A cut outside that subtree changes no compressed record. A link
between two marked components can temporarily mark its endpoints,
join them, and demote the temporary marks. If either side has no
marks, the old marked subtree is unchanged. Each operation changes
only constantly many virtual records.

Lazy path IDs, nonnegative path sums, component mark counts, and
first-physical-edge searches are standard deterministic dynamic-tree
fields with polynomial logarithmic overhead. Structural work never
enumerates a long unused path. Temporary structural marks are private
to this data structure and are not query-trace marks in S_i.

Set R=ceil(2H gamma). Expose every virtual path of root length at most
R. Each physical original-edge occurrence costs H positive length,
so the cache contains at most R/H occurrences. Repeated physical IDs
are charged with multiplicity. Root connectors and generated nulls
are skipped with a separate physical-edge aggregate. Retiring a cache
uses its old metadata; enumerating a new cache uses the current short
path. Chronological replay and delayed publication suffice even if a
provider has already computed the new state.

The total cached list size is O(Q_mark R), and each changed compressed
record costs O((R+1) poly(U)). Global physical-ID reference counts
maintain the literal union without paying for duplicate output edges.

## 6. Coverage is simultaneous, without per-input-edge witnesses

For any current original unit edge uv, the root degree adapter gives
distance at most 2H between its original handles. The numerical
estimate is at most 2H gamma. Its witness decomposes into native
pivot legs and one terminal local exact path, all with nonnegative
normalized length contributions. Each constituent therefore has a
root-flat path of length at most R.

Both endpoints of each constituent are marked: pivot-chain nodes
are tracked, their pivots are marked, and every node of an active
terminal source tree is marked. A forest path between marks is a
concatenation of whole compressed edges. Nonnegativity implies that
each such compressed edge has length at most R and is exposed.
Consequently the output contains the physical projection of every
constituent. Their compatible physical endpoints concatenate to a
uv walk of length at most 2 gamma. Replacing the edges of an original
shortest path proves the all-pairs spanner property.

This is an existence proof for all current input edges at once. It
does not maintain a query, routing list, or assignment for every
original edge after each update.

## 7. Parameter and accounting conclusion

Current size is at most n k^{O(1)} R poly(U). Total work and safe
ordinary recourse are at most

\[
                  (n+m_0+I+D)\exp O(B+\log R).
\]

Thus their logarithmic overhead is

\[
                         Z=O(U/t+t^4h).
\]

Choosing t=Theta((U/h)^{1/5}) gives the claimed four-fifths point.
The source shrink condition holds because x=Theta(t^4h) dominates
the O(t^3h) logarithmic lift cost. All additional marking factors
only change fixed coefficients of x. Exact root path sums and all
hierarchy labels fit the stated polynomial-logarithmic bit model.

At logarithmic stretch A_0=U^{5/7}h^{2/7}, choosing
t=Theta((U/h)^{5/28}) yields logarithmic time and density overhead
O(U^{23/28}h^{5/28}). The density exponent at this point is 23/28,
not 5/7: the local source-tree mark inventory contributes k^{O(1)}.

The same-observer public comparison is a derived assembly using the
old full-forest copy lift and public repair parameters, with the
explicit elementary zero-link copy extension checked in
**tracked_terminal_spanner_public_flat_comparator_audit.md**.
Every incoming node retains its independent assigned copy; a projected
connector or incoming null connects the two assigned roots by a zero
link. Contracting assigned trees recovers the input forest. A child
edge log changes O(1) records, while native core edits pay the full
live-copy inventory. Owner release prevents retired port aliases from
accumulating new historical owners. Quotienting connector components
instead would risk a copy-budget multiplier on every child edit and
is not the accepted argument. This elementary extension is an explicit
common adapter, not a printed source interface or an import of the
improved colored-pool lift for free.
Its B_pub=O(U/t+t^6h), A_pub=O(t^5h) give the six-sevenths
time/density point at the common finer stretch A_0. This is a named
pipeline comparison, not a claim of global public optimality.

All accepted bounds preserve the declared output contract and actual
inventory. No new exact general-matching bound follows from this
spanner theorem.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
