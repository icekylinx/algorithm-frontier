# Direct vertex inventory in the public core-forest lift

**Independent source reconstruction, 25 October 2026.**

This note sharpens the accounting of the existing public construction
in KMG, without using compressed Steiner cores, a colored path pool,
degree reset, or a new static provider. It proves that the original
Algorithm 5 can propagate an explicit **vertex occurrence capacity**
with only a polynomial logarithmic multiplier. Its selected graph can
still have large degree, and its update work retains the previously
audited degree factors.

The resulting derived public strong-forest bound is

\[
 (m+n)\exp O(U^{8/9}h^{1/9}),\qquad
 U=\log(N+4),\quad h=\log(U+4),                            \tag{1}
\]

under the public-provider and outer-wrapper interfaces already audited
in this checkpoint. This is a new analysis of public constructions,
not a claim that (1) is a theorem printed in the source or an optimum
over all public algorithms.

## 1. Primary source and the unnecessary degree conversion

The primary source is [KMG, arXiv:2311.06402v1]
(https://arxiv.org/pdf/2311.06402v1), Lemma 3.21, Definition 3.22,
Algorithm 5, and the accompanying proof on pages 30--32. Relevant
local text is in `sources/dynamic_shortest_paths_toolbox.txt`.

Let \(G\) be the current native graph and \(H\) its public selected
core graph. Let \(F_1,\ldots,F_b\) be the stable native forests,
where \(b=\operatorname{poly}(U)\). The source uses an incoming
flat forest \(\mathcal F\) embedded in \(H\). It allocates

\[
 \gamma'_{\rm cong}
   =\gamma_{\rm edge}\,\Delta\,\gamma_{\rm recVS}
\]

copies of each rooted direct-sum tree. The paragraph before Algorithm
5 explicitly explains this choice: edge congestion multiplied by
maximum degree bounds the number of incoming forest nodes at one
vertex of \(H\). No later structural step needs that particular
product. It only needs enough distinct slots for those incoming
nodes.

Instead assume and maintain the direct invariant

\[
 \bigl|\{y\in V(\mathcal F):\pi(y)=v\}\bigr|\le C
 \quad\text{for every }v\in V(H).                         \tag{2}
\]

Every living input node counts in (2), including isolated designated
nodes and unused nodes in a previously lifted forest. Consequently
there is no inference of a node bound from edge congestion and no
exception for isolated nodes. An arbitrary external forest must
supply this bound; the recursively constructed native forests start
with one node per native vertex, so the hierarchy does supply it.

## 2. The existing construction with C slots

For a physical root \(v\), let \(T_v\) be the direct sum of all
components of the \(F_i\) rooted at \(v\), identifying their root
aliases as in Definition 3.22. For a retained isolated child root
with no nontrivial component, use a singleton. Allocate exactly
\(C\) copies \(T_{v,j}\), \(1\le j\le C\).

Assign each input node at \(v\) a distinct slot \(j\). A surviving
designated input node keeps its slot and its root-node identifier.
Each input edge is processed exactly as in Algorithm 5: retain its
selected core provenance, take the literal native edge corresponding
to that core edge, and connect the corresponding endpoint in the
first assigned root-tree copy to the endpoint in the second copy.

The collection of root-tree copies is initially disjoint. Replacing
each node of the forest \(\mathcal F\) by its assigned tree, and
each input edge by its projected physical edge, gives a forest.
Unused copies remain additional disjoint forest components. Between
two assigned root nodes, the root-leg/native-edge/root-leg route has
length at most the stored core-edge length. The source metric proof
therefore applies unchanged.

### Parallel edges and selected ownership

Native parallel edges have distinct physical edge identities. For a
fixed identity \(e\) and fixed core \(i\), the core graph contains
at most one corresponding edge identity. The public selected graph
is a subgraph of that core union; its fully dynamic repair layers
select an identity rather than manufacture additional native edges.
Repeated internal ownership can be represented by a reference count.
Equivalently, retaining a polynomial number of explicitly indexed
bucket or core aliases only changes the polynomial below.

Thus one physical edge has at most \(b_0=\operatorname{poly}(U)\)
living selected aliases. This statement does not bound the number of
*different* native edges incident to a high-degree root by a constant.
It does not require such a bound.

For any fixed nonloop child edge identity \(uv\), all incoming
occurrences have endpoints among at most \(C\) nodes mapped to
\(u\) and \(C\) nodes mapped to \(v\). They form a subgraph of
the forest \(\mathcal F\), so there are at most \(2C-1\) such
occurrences. This remains true with parallel physical edges: two
parallel occurrences joining the same pair of input nodes would
already be a cycle in the input multigraph forest. Core loops are
discarded as in the positive-length selected interface.

The projected physical edges consequently have edge congestion at
most \((2C-1)b_0\). No independent incoming edge-congestion
parameter is needed once (2) is available.

## 3. All simultaneous vertices and edges are counted

Fix a physical vertex \(x\in V(G)\). In any one native forest
\(F_i\), it belongs to exactly one component and hence to exactly
one rooted tree contributing to the collection \(\{T_v\}_v\).
It has one copy in each of the \(C\) slots of that component.
Summing over all cores gives at most \(bC\) occurrences. Identifying
root aliases can only reduce this number. Any explicit singleton
root convention adds at most \(C\) occurrences for the physical
vertex, rather than an amount depending on its degree.

Projected edges introduce no new nodes. Thus the output forest has

\[
 C'\le (b+1)C                                              \tag{3}
\]

nodes at each physical vertex, including all unused copies and all
isolated nodes. The forest-copy edges have at most \(bC\) copies
of each native edge. Together with the projected-edge calculation,

\[
 \operatorname{econg}(\mathcal F'\to G)
       \le C\operatorname{poly}(U).                       \tag{4}
\]

There is no selected-degree factor in (3) or (4). A large degree
increases the number of incidences of a copied root, not the number
of copies of that root.

## 4. Stable roots, cuts, and full rebuilds

Use one fixed slot capacity for an entire private period. The
identifier and transaction rules are the public ones completed in
`public_strong_forest_marks_anchor_focused_audit.md`, Sections 2--5.
For clarity, the essential cut argument is repeated here.

Suppose a native core-tree cut detaches a piece from root \(v\)
and gives it a new root \(u\). First remove the projected input
incidences whose selected core endpoint changes. These changes are
in the actual child edit transcript, because each incidence retains
its core provenance. The detached copy in slot \(j\) now has no
remaining attachment to an input node assigned to the old root and
no designated mark of that old node. Its root can be identified with
the slot-\(j\) root of \(T_u\), retaining the existing designated
root identifier when present. Then insert the new input incidences.

No full tree is newly copied at this cut: the copies of the detached
piece already exist. The operation merely cuts physical forest
edges, joins equal-image root aliases, and updates the reported
projected incidences. The detached piece has no surviving projected
attachment when it is joined, so the join cannot create a cycle or
merge two distinct designated input nodes. The settled state is
again precisely Algorithm 5 with \(C\) slots.

Root-alias joins can require \(C\operatorname{poly}(\Delta,U)\)
work and actual incident-edge edits. This is a work charge, not an
increase in the simultaneous occurrence bound (3). Core provenance
and cuts-before-reinsertions are required; ignoring the input edit
transcript would not justify a stable-map claim.

Private retained ghosts keep their native identity within their
period. A rebuild retires its private copies and publishes new copies
using the old identifiers for surviving designated root terminals.
The full old and new inventories are paid. The final original
canonical identifiers persist throughout. This is the existing
copy-and-identify construction, with no typed-null edge or permanent
port gadget.

## 5. Recursion: small occurrence, unchanged conservative work

Each native nearest-pivot forest and each exact base shortest-path
forest has one node at every native vertex, including its isolated
vertices. Lift each family and perform the source's prescribed root
joins. Those joins identify nodes and cannot increase node inventory.
The union of at most \(d+1\) lifted native families therefore has

\[
 \exp O(dh)
\]

vertex and edge occurrences per root native vertex. Equivalently,
an induction of the form \(C_{j+1}\le Q(C_j+1)\) with
\(Q=\operatorname{poly}(U)\) yields the same bound. This is
valid for the **unreset** public hierarchy: a child native vertex
is a single physical root identifier in its parent graph. It is not
a claim that an arbitrary high-degree port expansion has this
property. That different interface is addressed by the new
uncontract-and-compress construction elsewhere.

The selected graph degree can still grow as \(P^{O(j)}\) at
level \(j\), and converting splits into explicit child edits still
costs its degree. Keep all those already audited charges. With

\[
 \begin{aligned}
 g&=O(qrh),\\
 f&=O(U/q+U/r+r^2h+q^2rh),\\
 z&=O(U/K+g+h),\qquad d=O(U/x),
 \end{aligned}
\]

the safe public envelopes become

\[
 \boxed{\quad
 a=O(dKg+dh),\qquad c=O(dh),\qquad
 B=O(x+f+K^2g+d^2z+d^2h+h).
 \quad}                                                    \tag{5}
\]

The added \(d^2h\) permits even a conservative product of all
copy factors while forwarding work. Since \(z\ge h\), it may
also be absorbed in \(d^2z\). The improvement is to \(c\);
this note does not silently replace the public \(d^2z\) work
by \(dz\).

## 6. Public strong-forest 8/9 parameter point

The public outer copy accounting, independently checked in
`strong_forest_mechanism_comparison.md`, uses

\[
 \begin{aligned}
 K_{\rm cov}\Lambda(a+O(h))&\le c_0U,\\
 Z&=O\bigl(B+U/\Lambda+U/K_{\rm cov}
              +\Lambda U/K_{\rm cov}+\Lambda c+h\bigr).
                                                               \tag{6}
 \end{aligned}
\]

The local forest's explicit recourse is included in \(B\) once;
the outer copy inventory uses \(c\), not that whole work bound.
Take

\[
 t=(U/h)^{1/9},\quad q=r=d=\Theta(t),\quad
 x=\Theta(U/t),\quad K=\Theta(t^3),\quad
 K_{\rm cov}=\Theta(t^2),\quad\Lambda=\Theta(t).             \tag{7}
\]

Writing \(U=t^9h\) gives the following charged quantities.

| Quantity | Logarithmic order |
|---|---:|
| \(g\) | \(t^2h\) |
| \(f\) | \(t^8h\) |
| \(z\) | \(t^6h\) |
| \(K^2g\) | \(t^8h\) |
| \(d^2z\) | \(t^8h\) |
| \(a\) | \(t^6h\) |
| \(c\) | \(th\) |
| \(B\) | \(t^8h\) |
| \(K_{\rm cov}\Lambda(a+O(h))\) | \(t^9h\) |
| \(U/\Lambda\), \(\Lambda U/K_{\rm cov}\) | \(t^8h\) |
| \(\Lambda c\) | \(t^2h\) |

Choose fixed constants in the cover parameters so the first line of
(6) holds. Their effect on all work bounds is only a fixed factor in
the exponent. The public provider's small-instance cutoff
\(q^2rh=O(t^3h)\) is below the nonbase size scale
\(x=\Theta(t^8h)\). Initialization credit, fixed maps, and the
forced-anchor metric completion are the same previously audited
interfaces. Equations (5)--(7) prove (1).

## 7. What this comparison changes

The earlier public \(10/11\) reconstruction is valid but weaker.
Its factor \(c=d^2z\) arose from using the printed edge-to-vertex
congestion conversion at every level. The source itself states why
that conversion is used; maintaining the direct node inventory
removes it without changing the copy construction.

The new colored-pool proposal must therefore be compared with this
\(8/9\) public baseline, not just the printed \(83/84\), the
common-factor \(26/27\), or the intermediate \(10/11\) bound.
Its substantive additional interface is a compressed, low-overlap
child graph that also controls recursive native degrees and port
aliases. The direct public node count does not by itself establish
that new interface or its candidate \(6/7\) application.
