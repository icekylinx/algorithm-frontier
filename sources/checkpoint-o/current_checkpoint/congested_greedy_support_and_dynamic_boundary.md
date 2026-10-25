# Congested greedy support: a static lemma and its dynamic boundary

**Separate mathematical investigation, 24 October 2026.** This note
records a congestion-capped greedy support construction. Its active
and saturated-edge mechanism is a variant of the dynamic spanner in
[Kyng--Meierhans--Zoecklein, A Simple Dynamic Spanner via APSP,
Section 4](https://arxiv.org/html/2408.11368v1).
The native-split accounting and the ambient counterexample below
address the additional interfaces needed here. No novelty claim is
made for the underlying greedy mechanism. It does not replace the
maintained spanner in the 4/5 matching construction.

The construction simultaneously obtains sparse selected support,
short routes, and bounded EDGE congestion in its own native graph.
There is a useful conditional recourse bound under native splits.
Two additional properties needed by the matching backend do not
follow: a low-degree selected-star invariant maintained without
circular feedback, and the stronger arbitrary-ambient congestion
bound. Fast distance queries are a third, separate algorithmic
requirement.

## 1. Static statement

Let \(G\) be an undirected loopless multigraph with explicit edge IDs,
\(n\) vertices, \(m\) edges, and maximum degree at most
\(\Delta\geq1\). Fix an integer \(b\geq1\), and put
\[
               L=2b,\qquad \tau=\lceil4\Delta L\rceil .
 \tag{1}
\]
There is an elementary deterministic construction of a selected
subgraph \(H\subseteq G\) and a simple \(H\)-path \(P_e\) for every
input edge \(e\), with the same endpoints, such that
\[
 \begin{split}
 |E(H)|&\leq 2n^{1+1/b}+mL/\tau,\\
 |P_e|&\leq L,\\
 \max_{f\in E(H)}|\{e:f\in P_e\}|&\leq\tau .
 \end{split}
 \tag{2}
\]
In particular \(b=\lceil\log_2(n+2)\rceil\) gives \(O(n)\)
selected edges, \(O(\log n)\) route length, and
\(O(\Delta\log n)\) native edge congestion. This is an existence
and finite-construction statement. A BFS implementation of each
test is not near-linear.

### Construction

Maintain the output graph \(H\), an ACTIVE subgraph \(F\subseteq H\),
and an integer load counter on each active selected edge.
Initially both graphs are empty. Process input IDs in a fixed order.

For \(e=uv\), find a shortest \(u\)-to-\(v\) path in \(F\).
If its length is at most \(L\), assign it to \(e\). Otherwise
insert \(e\) into \(H\) and \(F\), with counter zero, and assign
its one-edge identity path. Increment the counter of every active
edge used by this route. Once a counter reaches \(\tau\), remove
that edge from \(F\), but RETAIN it in \(H\) and retain all paths
already assigned to it. Process all threshold removals before the
next demand.

Every path is simple. A threshold crossing therefore changes a
counter by one, so a removed edge has exactly \(\tau\) assigned
route occurrences. No later route uses it. This proves the last
two inequalities in (2).

### Active girth and selected size

When a new edge is added to \(F\), its endpoints previously had
distance greater than \(2b\). The resulting graph has no cycle of
length at most \(2b+1\). Deletions preserve this property. In
particular \(F\) is simple even though \(G\) may have parallel IDs.

For completeness, every \(n\)-vertex graph of girth greater than
\(2b+1\) has at most \(2n^{1+1/b}\) edges. If it has \(a\) edges,
successively delete vertices of degree below \(a/n\). Not all
vertices can disappear, since their total removed edges would be
less than \(a\). The remaining subgraph has minimum degree
\(\delta\geq a/n\). If \(\delta\geq2\), a breadth-first ball of
depth \(b\) has no repeated vertices or extra short connections,
and hence
\[
                  n\geq(\delta-1)^b.
\]
Thus \(a\leq n(1+n^{1/b})\leq2n^{1+1/b}\).
The case \(\delta<2\) satisfies the same bound directly.

Every inactive selected edge has received \(\tau\) occurrences.
The total number of assigned occurrences is at most \(mL\).
There are therefore at most \(mL/\tau\) inactive selected edges.
Adding the active bound proves the first inequality in (2).

This also explains precisely why the earlier uncapacitated greedy
counterexample is avoided: a bridge carrying too many cross demands
becomes unavailable to subsequent routes, forcing additional support.
It does not explain how to maintain that support after changes.

## 2. A precise conditional dynamic lemma

Consider one period of a changing native multigraph. Updates may
insert or delete edge lifetimes, insert isolated vertices, or split
one vertex into two by partitioning its current incidences.
An old loop may awaken after such a split; treat its zero-length
route as an endpoint-annotated demand before the split. No vertex
identification is allowed. Let:

* \(n_*\) bound the number of resident native vertex slots;
* \(\Delta\) bound native degree throughout the period;
* \(m_0\) be the initial number of demand IDs;
* \(B\) and \(D\) count genuine native edge births and deaths;
* \(s\) index the native binary splits;
* \(d_s\) be the degree of the split vertex in the FULL selected
  graph \(H\), including inactive selected edges, immediately
  before split \(s\).

Use the same fixed \(b,L,\tau\) throughout the period, with
\(\tau\geq\Delta\). Start by applying Section 1 to the initial
edge IDs. Maintain every current route explicitly together with
current inverse lists.

After an update, first invalidate all affected demand routes and
remove their inverse-list entries. Historical active counters are
NOT decremented. Then reroute every still-present affected demand,
using the same greedy rule. If its own input edge is already an
INACTIVE selected edge, its identity path is always permitted as
a special case. Such an edge receives no new nonidentity route,
and at most its own one current demand uses this exception.

### Current-load bound

Every active edge has current route load no larger than its
historical counter. Once it becomes inactive, no new route of a
different demand can use it. Its current load is consequently at
most \(\tau+1\), including its possible identity exception.
Repeated invalidations of that one identity route do not create
multiple current demands.

An edge deletion invalidates at most \(\tau+1\) paths through that
selected edge, plus the disappearing demand itself, which does not
need rerouting. A split of a vertex of selected degree \(d_s\)
invalidates at most
\[
                      d_s(\tau+1)+\Delta
 \tag{3}
\]
current demands. Indeed every nonempty route passing through the
vertex uses one of its selected incident edges. The extra
\(\Delta\) accounts for endpoint annotations and empty-loop
demands whose own endpoint changes. Enumerating these current
inverse lists, and deduplicating their IDs, is an explicit way
to find the affected set.

Let \(R_{\rm calls}\) count all initial and subsequent route calls.
Then
\[
 R_{\rm calls}\leq
 m_0+B+(\tau+1)D+
               \sum_s\bigl(d_s(\tau+1)+\Delta\bigr).
 \tag{4}
\]
The selected graph itself changes endpoints under the native split;
old path records are retired before those endpoint changes are
published. Queries occur only after rerouting settles.

### Cumulative selected-ID recourse

The active graph still has girth greater than \(2b+1\).
A native split cannot create a new short cycle: a new cycle maps
to a closed trail using distinct old edge IDs, which contains an
old cycle no longer than that trail. Edge removals and saturation
removals are also harmless.

Every saturation event consumes \(\tau\) historical occurrences.
Each route call adds at most \(L\) such occurrences, so there are
at most \(LR_{\rm calls}/\tau\) saturation events over the whole
period. A selected native ID is born at most once during its own
native lifetime; it never leaves the output merely because it
saturates. It dies only when that native edge dies. Therefore the
total number of selected-ID births plus deaths is at most
\[
 \begin{split}
 2n_*^{1+1/b}+2D+\frac{L R_{\rm calls}}{\tau}
 \ \leq\ &
 2n_*^{1+1/b}+2D+\frac{L(m_0+B)}{\tau}\\
 &+2LD+L\sum_s(2d_s+1).
 \end{split}
 \tag{5}
\]
This is a cumulative statement, not a worst-case per-update claim.
It also bounds current support size by the same cumulative
expression; it does not retain the static \(O(n_*)\) size
automatically for an arbitrarily long period.

In particular, if an INDEPENDENT mechanism ensures
\(d_s\leq d_H\), then (5) gives
\[
 O\!\left(n_*^{1+1/b}
       +\frac{L(m_0+B)}{\tau}
       +L(D+(d_H+1)q_{\rm split})\right).
 \tag{6}
\]
Selected endpoint changes at each split are at most \(d_s\) as
well. Thus a subpolynomial \(d_H\), together with an appropriate
period bound, would give the desired form of propagated selected
recourse. Formula (6) is a useful conditional interface.

## 3. Why naive selected-degree feedback does not close the lemma

It is tempting to invoke the existing rule that splits an overfull
selected star at threshold \(z\). But (5) must then also count those
feedback splits. At such a split, \(d_s=\Theta(z)\) is consistent
with the rule, so our current bound allows
\[
                     O(Lz)
 \tag{7}
\]
new selected births funded by that one feedback event.
The ordinary excess-degree potential decreases by only
\(\Theta(z)\). Substituting (7) into the potential inequality
therefore does not yield an absorbing coefficient below one,
regardless of merely increasing \(z\): both sides scale with
the same \(z\).

This is an obstruction to THAT proof, not an example forcing the
algorithm to make \(\Theta(Lz)\) births. A stronger charging
invariant, a partition rule that bounds route breakage independently
of the full selected star, or a separate degree-control mechanism
could change the conclusion. The conditional lemma must not be
presented as having already supplied such a mechanism.

One can also remove a low-load inactive selected edge and reroute
its remaining users. Choosing the eviction threshold
\(\tau/(cL)\) makes each eviction fund at most \(1/c\) additional
saturations. This can control that EVICTION cascade and bound the
number of retained inactive edges by current route mass. It does
not remove the \(d_s\tau\) invalidation term caused by a native
selected-star split, and it does not by itself fix (7).

## 4. Native edge congestion is not the ambient contract

The dynamic repair proof requires more than congestion in \(H\).
Its input graph \(J\) is itself embedded by simple native paths
\(\Pi\) in an arbitrary immediate ambient graph. Writing
\(C_0=\operatorname{vcong}(\Pi)\), the needed output guarantee is
of the form
\[
           \operatorname{vcong}(\Pi\circ P)
                       \leq\Gamma\bigl(C_0+\Delta(J)\bigr).
 \tag{8}
\]
The static greedy lemma only proves, directly,
\[
           \operatorname{vcong}(\Pi\circ P)
                       \leq(\tau+1)C_0,
 \tag{9}
\]
up to the fixed convention for endpoint annotations.
With \(\tau=\Theta(\Delta(J)L)\), this is a PRODUCT of
\(\Delta(J)\) and \(C_0\), rather than their sum. The two may
both be large in a projected instance.

The vertex version in the native selected graph also only gives
\(O(\deg_H(v)\tau)\) from the edge bound. The balanced-tree
counterexample in
[central_greedy_recoursing_under_splits.md](central_greedy_recoursing_under_splits.md)
shows why short routes and sparse, low-degree support alone do
not supply a congestion guarantee; the capacity construction
repairs native edge congestion but does not establish (8).

No lower bound against other ambient-aware algorithms is claimed.
An additional capacity-aware selection or weighted routing argument might
prove (8) for a modified algorithm. The existing static
length-free sparsifier obtains precisely this stronger property
through degree-band witnesses and path selection; it is not a
corollary of the own-graph greedy argument.

### 4.1 A concrete failure of (8), even with selected degree three

Let \(L\geq2\) be even, put \(b=L/2\), and let \(T\) be a full
binary tree of height \(4L\). Write
\[
 n=|V(T)|=2^{4L+1}-1,\qquad
 J=T^L,
 \tag{10}
\]
where distinct vertices are adjacent in \(J\) exactly when their
tree distance is at most \(L\). This is a simple native graph.
Its maximum degree satisfies
\[
        2^L\leq\Delta(J)\leq3(2^L-1).
 \tag{11}
\]
The lower bound follows already from a sufficiently deep radius
\(L\) ball; the upper bound is the usual binary branching count.

Process ALL tree edges first in congested greedy. Every such edge
is selected, since before its insertion its endpoints lie in
different components of the processed tree. Subsequently every
native demand has a unique tree path of length at most \(L\).
For a fixed tree edge, the number of such paths using it is at
most
\[
 \sum_{\substack{i,j\geq0\\i+j\leq L-1}}2^i2^j
   =\sum_{s=0}^{L-1}(s+1)2^s
   <L2^L.
 \tag{12}
\]
Indeed its two sides have at most \(2^i\) and \(2^j\) vertices
at the indicated distances from the edge endpoints. In view of
\(\tau=4\Delta(J)L\), no selected edge ever saturates.
The final output is EXACTLY \(H=T\), with its unique tree routes.
It has selected maximum degree three, \(n-1\) edges, and all the
claimed native congestion and length bounds. Also
\(n^{1/b}=O(1)\) for this choice, so it lies in the linear-size
regime of the static lemma.

Now introduce a new ambient vertex \(x\). Embed every tree edge
\(uv\) as the simple path \(u-x-v\), and every non-tree
native edge \(uv\) as its own direct ambient edge. The ambient
graph contains the necessary star edges and direct non-tree
edges, each with its own identity. Then
\[
             C_0=n-1,\qquad C_0+\Delta(J)=\Theta(n).
 \tag{13}
\]
The first equality counts the \(n-1\) tree-edge images through
\(x\); each other native vertex is only an endpoint of at most
\(\Delta(J)\) input images.

Every selected tree route, after composition, is a walk through
the same hub. Erasing ALL closed subwalks leaves the simple
ambient path \(u-x-v\). Thus the hub occurs in every one of
the \(m=|E(J)|\) normalized demand routes, not merely in a
backtracking representation.

To count \(m\), partition the tree leaves into groups descending
from vertices \(L/2\) levels above them. Every group contains
\(q=2^{L/2}\) leaves, and every pair within a group has tree
distance at most \(L\). There are \(2^{4L}/q\) groups, so
\[
                  m\geq 2^{4L}(q-1)/2
                            =\Omega(n2^{L/2}).
 \tag{14}
\]
Consequently the output ambient congestion exceeds
\(C_0+\Delta(J)\) by a factor \(\Omega(2^{L/2})=
\Omega(n^{1/8})\). A subpolynomial factor \(\Gamma\) cannot
absorb this family. Native edge capacities, a degree-three
selected graph, and complete loop erasure do not imply (8).

### 4.2 The immediate ambient graph can also have degree three

The large degree of \(x\) is not essential. Make one binary tree
\(X\) with one distinct port for every native vertex, allowing
at most a factor-two number of unused leaf ports. Use two
binary halves joined by a distinguished central edge. Assign
half of the leaves from EACH group used in (14) to ports in
each half of \(X\). Distribute all other native vertices among
the remaining ports. Each half needs only \(O(n)\) ports.

Give each native vertex \(v\) a distinct center \(c_v\), joined
to its port in \(X\). Separately attach at \(c_v\) a private
binary port tree for the non-tree native edges incident to
\(v\). Join the corresponding private ports by a genuine
external edge for every such native edge. Trees of zero or
one port use the evident constant-size cases.

Embed a native TREE edge through its endpoint centers and
the unique path in \(X\). Embed a NON-TREE edge through the
two private endpoint port trees and its own external edge.
These are simple paths of length \(O(\log n)\).
Every ambient vertex has degree at most three: a center
has one attachment toward \(X\) and one toward its private
port tree; all other records belong to binary trees or
their leaf attachments.

At any vertex of \(X\), at most \(n-1\) input tree-edge
images occur. At any private fiber or center, at most
\(\Delta(J)\) input images occur. Hence
\[
                         C_0\leq\max\{n-1,\Delta(J)\}.
 \tag{15}
\]
All selected routes still use only tree-edge images, whose
union lies in \(X\) together with its center attachments.
After loop erasure the route from \(c_u\) to \(c_v\) is
the unique path in that tree. Whenever \(u,v\) belong to
opposite halves of one leaf group, this route crosses the
central edge of \(X\).

There are \(q^2/4\) such pairs per group. Their total is
\[
                  (2^{4L}/q)\,q^2/4
                         =\Omega(n2^{L/2}).
 \tag{16}
\]
Thus the SAME polynomial violation of (8) occurs with
degree-three ambient graph and simple, logarithmic-length
input images. All graph sizes remain polynomial in \(n\).
The failure is specific to the congested-greedy support and
route choice, and does not rule out an ambient-aware
construction selecting different native edges.

### 4.3 Direct ambient saturation is not enough by itself

One natural repair is to count normalized AMBIENT loads and, at a
saturated resource, deactivate every selected native edge whose fixed
image uses it. The exact static example in
[the bulk-deactivation obstruction](ambient_bulk_deactivation_obstruction.md)
shows that this rule can retain \(\Omega(n^2/\gamma)\) selected IDs on
\(\Theta(n^2)\) input IDs with threshold
\(\Theta(\gamma(C_0+\Delta))\). Its active graphs are always trees.
The example survives loop erasure and a degree-three ambient
representation with logarithmic-length input paths.

Thus this particular replacement loses the sparse retained-support
guarantee before any dynamic degree feedback is considered. It does
not exclude a different ambient-aware selection or rerouting rule.

## 5. Fast distance tests and route notifications remain separate

A literal BFS test gives a finite algorithm, but may inspect the
whole selected graph per demand. The number of demand reroutes
in (4) may be much larger than the selected-ID recourse in (5).
This separation is useful: a candidate dynamic distance provider
could have cheap path-reporting queries, while only the much
smaller selected/active update stream invokes its expensive
maintenance.

For a provider returning a path of length at most
\(\gamma\operatorname{dist}_F(u,v)\), use route threshold
\(L=2\gamma b\). Rejecting a route longer than \(L\) then certifies
that the true distance is greater than \(2b\), which preserves
the same active-girth bound. All displayed occurrence charges
use this enlarged \(L\). Returned paths must be explicit, and
the provider must support the actual active edge updates and
encoded native splits. A distance estimate without a path is
insufficient.

Neither this interface nor the static result assumes that the
necessary approximate-distance provider, independent degree
controller, and arbitrary-ambient congestion property already
coexist. Establishing their compatible quantitative bounds is
the remaining algorithmic task.
