# A combinatorial central-edge recourse bound under native splits

**Separate positive interface lemma, 24 October 2026.** This note
shows that small selected-central-edge recourse is not, by itself,
the obstruction to replacing the serial repair layers. Exact greedy
repair has very small edge-ID recourse even under native vertex
splits. Its straightforward implementation is too slow and its
current route records can change too often. No improved matching
running time follows from this lemma.

The edge-deletion version is the elementary greedy observation in
[Kyng, Meierhans and Zöcklein, A Simple Dynamic Spanner via APSP,
ICALP 2025, Section 4.1](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.111/LIPIcs.ICALP.2025.111.html).
The proof below explicitly includes incidence-partition vertex
splits and distinguishes edge membership from endpoint changes.

## 1. The algorithm as a combinatorial object

Let an unweighted loopless-or-looped native multigraph $`G`$ undergo
edge insertions/deletions and vertex splits. A split partitions
incidences between two descendants and preserves each real edge ID.
It never identifies distinct vertices. Initially or later isolated
vertices are allowed.

Fix an upper bound $`n_*\geq2`$ on the number of resident vertices
over the finite run, and an integer $`b\geq1`$. Start with the empty
selected graph and maintain a subgraph $`H\subseteq G`$. An
initial nonempty input is processed by the same insertion rule.
After each native edit, first apply it to the
selected edges. Then, while some nonloop $`e=uv\in E(G)`$ has
```math
\mathrm{dist}_H(u,v)>2b,
 \tag{1}
```
insert that CENTRAL native edge ID into $`H`$. A loop never needs
insertion. Continue until no such edge exists.

The algorithm can be made literal by scanning all current native
edge IDs and performing an exact breadth-first search truncated
at depth $`2b`$ for each test. Adding an edge can only improve
other distances, so a single scan after the native edit suffices.
This is a finite deterministic algorithm, albeit generally slow.

At settlement every original edge has a selected route of length
at most $`2b`$; substituting these routes in an arbitrary path gives
a $`2b`$-spanner.

## 2. Splits preserve the girth invariant

Every selected insertion satisfying (1) creates no cycle of length
at most $`2b+1`$. Deletions create no cycles.

A vertex split also cannot create a shorter cycle. If a cycle in
the split graph is mapped back by identifying its two descendants,
its edge IDs form a closed trail in the pre-split graph. This trail
contains a cycle of no greater length. Therefore a graph of girth
greater than $`2b+1`$ retains that property after splitting.

Parallel selected edges are impossible because the second such
edge has endpoint distance one. Selected loops are absent. Thus
the ordinary simple-graph girth argument applies to $`H`$, despite
parallel and loop IDs in the native input.

## 3. Explicit size and edge-ID recourse

A graph on at most $`n_*`$ vertices and girth exceeding $`2b+1`$
has at most
```math
2n_*^{1+1/b}
 \tag{2}
```
edges. Here is a sufficient elementary estimate. If a graph had
average degree exceeding $`4n_*^{1/b}`$, repeatedly removing
vertices of degree below half that average leaves a nonempty
subgraph with minimum degree greater than $`2n_*^{1/b}`$.
A breadth-first search of depth $`b`$, with no cycle of length at
most $`2b+1`$, would then contain more than $`n_*`$ vertices.
This contradiction gives (2), with harmless slack for constant
sizes.

A selected native ID leaves $`H`$ only when that native edge is
deleted. In particular, a vertex split changes endpoints but does
not delete selected memberships. If the whole run has $`D_{\rm del}`$
native edge deletions, then the number of selected membership births
is at most
```math
2n_*^{1+1/b}+D_{\rm del},
 \tag{3}
```
and selected births plus deaths are at most
```math
2n_*^{1+1/b}+2D_{\rm del}.
 \tag{4}
```
These bounds are independent of the number of native edge
insertions and of how many input incidences a split moves.

Taking $`b=\lceil\log_2 n_*\rceil`$ gives stretch
$`O(\log n_*)`$, selected size $`O(n_*)`$, and total selected
edge-ID recourse
```math
O(n_*+D_{\rm del}).
 \tag{5}
```
Equations (3)--(5) also hold for every finite prefix when its
resident-vertex bound is used.

The count $`n_*`$ includes actual split descendants and genuine
resident vertices. It must not silently include a much larger
unused private universe when applying this statement to a shrinking
backend. A separate active-instance adapter is required there.

## 4. Small selected degree does not bound route congestion

There is an explicit obstruction to inferring the needed route
congestion from the preceding girth and degree bounds.

Let $`q\geq2`$ be a power of two. Take two full balanced binary
trees, each with $`q`$ leaves, and join their roots by one central
edge. Call the resulting tree $`T`$. It has
```math
N=4q-2,\qquad
              \Delta(T)=3,\qquad
              \mathrm{diam}(T)=2\log_2q+1.
 \tag{6}
```
Choose $`1\leq D\leq q`$. Between the two leaf sets add a simple
$`D`$-regular bipartite graph, for example the $`D`$ distinct cyclic
shift matchings. Let $`G`$ be the tree plus these $`Dq`$ cross
edges. Its native maximum degree is
```math
\Delta(G)=\max\{3,D+1\}.
 \tag{7}
```

Run the greedy algorithm with all tree edges first and
$`b=\lceil\log_2 N\rceil`$. Every tree edge is inserted because
its endpoints are then in different components. Every later cross
edge is omitted, since its tree distance is at most
$`\mathrm{diam}(T)\leq2b`$. Thus the final selected graph is
exactly $`H=T`$.

For every cross demand the unique simple selected route uses the
central edge. Every endpoint-preserving walk in $`T`$ must also
use that edge. Consequently its edge-occurrence congestion, and
the occurrence congestion at either central endpoint, is at least
```math
Dq=\Omega(N\Delta(G)).
 \tag{8}
```
The asymptotic equality includes $`D=1,2`$, because the maximum
degree in (7) is then an absolute constant.

Here the selected graph already has maximum degree three, linear
size, infinite girth, and logarithmic stretch. Its large congestion
therefore cannot be repaired by selected-degree feedback alone.
Nor can a different choice of routes inside this SAME selected
tree help: the central cut has only one selected edge.

This example refutes the implication for arbitrary-order greedy
selection. It does not refute a different sparse-support algorithm
that uses congestion when deciding which additional edges to
retain. Such a procedure would need a joint sparsity, membership
recourse, and route-reporting proof.

## 5. Why this does not close the numerical backend

The small membership count is only one part of the needed interface.

First, a native split can move many selected incidences, even if it
creates no new selected ID. Publishing those changes as ordinary
child edits requires the selected-degree cap and settled
old-to-final transcript already used by the matching backend.

Second, finding the violating edges in (1) by repeated exact BFS
can scan essentially the whole selected graph for each native
edge. Its work is not covered by the desired local
subpolynomial update bound. The APSP reduction in the cited paper
addresses this computational issue for edge updates, using a
separate dynamic distance oracle. Its stated theorem is not,
without an adapter, a native-split theorem at the quantitative
parameters sought here.

Third, maintaining arbitrary short paths for all nonselected
demands can have large vertex congestion. A native deletion can
invalidate many such records. Small recourse of the SELECTED set
does not bound the cost of reporting all route changes, refreshing
correction scores, or maintaining inverse route-occurrence lists.

Finally, the projected multiple-origin operation in
[initial-route-projection-updates.md](initial-route-projection-updates.md)
is not a native split. Applying the girth argument directly to that
projected topology would therefore be unjustified: identifying
extracted groups can create short cycles. The argument applies to
the original CENTRAL native graph, whose legal operations are
actual splits and edge edits.

## 6. A precise possible replacement interface

A stronger primitive would maintain the central greedy support, or
some other support with the same asymptotic bounds, while providing:

* sufficiently fast approximate distance/path tests for the actual
  native edit transcript;
* bounded total explicit current-route and inverse-index work;
* a constructive selected-degree repair with an ordinary settled
  child transcript;
* fixed physical edge/vertex lifetimes and the existing
  deletion-first raw-lift metadata discipline.

Such a primitive could improve the serial quality recurrence.
Equations (2)--(5) show that combinatorial edge-ID recourse alone
does not prohibit it. They do not supply its computational or
route-congestion clauses.
