# Lazy path updates through a bounded witness interface

**Research construction, 25 October 2026. Internal root and independent
reviews completed.**

This note gives a possible extension beyond the forest representation.
It is stated first as an explicit finite-interface data-structure lemma,
then applied to a fixed graph with a supplied bounded-width separator
hierarchy. The claimed dependence on the width is exponential. No
general-graph matching exponent improvement is asserted.

The main distinction from an ordinary point-update shortest-path DP is
that one selected path can contain many physical incidences. The
construction applies its allocation transfer lazily and discovers
register crossings without expanding that path.

## 1. An edge-partition hierarchy with explicit witnesses

Fix a binary hierarchy of height h. Its leaves own distinct physical
incidences or endpoint-price gadget edges. Every physical allocation
coordinate has exactly one leaf owner. The two children of a node
partition its edges; they do not contain aliases of the same coordinate.

At a node C maintain at most q directed path witnesses. A witness is
simple in the physical graph. Each parent witness is an explicit
concatenation of selected child witnesses. The two child families and
their composition records determine it without expanding its edges.

For physical allocation edge e, let
$$
\chi_{C,j}(e)\in\{-1,0,1\}
$$
be its signed use by witness j: +1 for receiving row-to-bin use,
-1 for donating bin-to-row use, and zero if it is absent.
Endpoint-price gadget edges have no primal allocation coordinate.

A composition record supplies a matrix A_i for each child C_i:
$$
\chi_C(e)=A_i\chi_{C_i}(e)
                         \qquad(e\in C_i).                   \tag{1}
$$
The records are not an arbitrary matrix promise. They come from the
actual child-path concatenation. For nonempty selected paths a child
witness cannot be used twice in one simple parent witness.
Empty primal subpaths can be omitted from update propagation.

Assume a point price edit recomputes only the leaf's ancestor families,
and a node's family and composition records can be recomputed in
poly(q) operations. Section 6 gives such a shortest-path construction
when the boundary size is bounded.

## 2. Group coordinates by their current signed-use vector

At each node C, partition its allocation coordinates by
$$
\chi_C(e)=(\chi_{C,1}(e),\ldots,\chi_{C,q}(e)).
$$
There are at most 3^q possible nonempty groups. A group may contain
many physical edges, but they receive the same allocation change
under every linear combination of the current witness updates.

For each group store minima, with physical edge witnesses, of
$$
x_e-\ell_e,\qquad 2\ell_e-x_e,\qquad
 x_e-\underline x_e,\qquad \overline x_e-x_e .                \tag{2}
$$
These are the two register and two guard buffers. Retain the zero
signed-use group too: an edge absent from all current witnesses
may appear in a later recomputed witness family.

The local state is finite and explicit, using
3^q poly(q) words. No coordinate is copied into two groups of one node.

## 3. A lazy vector of path transfers

Node C also keeps a vector t_C, initially zero, recording transfers
on its current selected witnesses that have not been propagated
to its children.

To apply a transfer eta to witness j, add eta to t_(C,j).
A group with signed-use vector chi has allocation increment
$$
\Delta x=\eta\chi_j .
$$
Its first and third minima in (2) increase by Delta x, and its
second and fourth decrease by Delta x. Thus the entire path
update is performed in 3^q poly(q) time without reading its edges.

More generally, an accumulated vector t changes a group by t dot chi.
Only fixed-grid addition and multiplication by small integer
composition coefficients are used.

Before splitting a node's state, inspecting a descendant coordinate,
or replacing any witness family or composition map, push the old
tag through the old maps:
$$
t_{C_i}\mathrel{+}=A_i^\mathsf{T}t_C. \tag{3}
$$
Update each child's group minima by the corresponding dot products,
then clear t_C. Equation (1) proves that every physical coordinate
receives exactly its pending increment.

This push-before-remap rule is essential. A historical transfer
follows the witness that was selected when it occurred; it is
not silently reassigned to a newly selected shortest path.

## 4. Recompute groups after a witness change

After children are settled and the parent family has been recomputed,
map every child group through its new matrix in (1). Merge its four
minima into the resulting parent group. The physical edge IDs
attaining the minima are carried as tie-broken witnesses.

Although a general integer matrix could produce larger coordinates,
the actual mapped vectors are again in {-1,0,1}^q: each parent
witness is a simple physical path. This is an invariant supplied
by the witness construction, not an arithmetic clipping operation.

The children have disjoint physical edge sets. Therefore mapping
and merging their groups cannot count one allocation twice.
The work is 3^q poly(q) per recomputed node.

An external point allocation setting first pushes tags down to
its leaf, then updates its physical value and register as an
explicitly charged record. A merely changed route witness does
not reset its coordinates' registers.

At a leaf, fold its pending scalar allocation increment into the
explicit value x before a point read, reset, or external setting,
and then clear that leaf tag. This is a materialization of the one
owned coordinate, not an enumeration of an ancestor path.

## 5. Guard and register discovery

For a selected root witness j, query its guard by taking the
minimum of x-lower over groups with chi_j=-1 and upper-x over
groups with chi_j=+1. Groups with chi_j=0 are irrelevant.
The endpoint slack guards are handled directly.

After a path update, any nonpositive register minimum in (2)
identifies a dirty coordinate. Push tags while descending to
one such leaf, recover its exact x, and reset ell=3x/4.
Update its conservative donor price and recompute ancestor
families and groups, always using the push-before-remap rule.

Other dirty coordinates remain represented in the group minima;
repeat until the state is settled. The temporary shortest-path
families recomputed while some other registers are still dirty
are not used for a new numerical transfer. Their costs remain
nonnegative, so their physical path witnesses are still defined.

One numerical transaction first applies its lazy primal transfer,
then settles all register events and both endpoints' price edits.
No new transfer is issued until the entire transaction is settled.

Each reported register event, point price edit, or endpoint-price
edit takes
$$
3^q\mathrm{poly}(q)\,h        \tag{4}
$$
work. A path transfer and its guard query have no dependence
on the physical path length.

The history-wide register-event proof is unchanged: numerical
paths are physically simple and therefore change each coordinate
at most once. Their one-sided negative log variation is O(1).
No extra witness copy creates another primal change.

Tag values use O(log S) bits under the declared polynomial history
bound. One root transfer uses a given nonempty child route at
most once, because otherwise a physical edge of that route would
repeat. Empty primal routes are omitted. An unpushed coefficient
is consequently a sum of at most polynomially many bounded
step sizes. Linear dependencies between route vectors do not
justify cancelling or ignoring tags; the explicit history bound
pays their representation.

## 6. Exact threshold witnesses from small boundaries

Suppose a hierarchy node has at most b boundary vertices, and its
children share only boundary vertices. Store:

* all ordered boundary-to-boundary ordinary shortest paths;
* the best source-price-leaf-to-boundary path for each boundary;
* the best boundary-to-target-price-leaf path for each boundary;
* the best source-price-leaf-to-target-price-leaf path.

Thus q=O(b^2). Source and target prices live on private pendant
edges as in the unrestricted forest client. No mutable endpoint
price is duplicated on every boundary occurrence of its bin.

Build an auxiliary graph on the union of the child boundaries,
plus an abstract source and target. Child boundary distances give
ordinary nonnegative-cost arcs. Child source offers, target exits
and internal best pairs give the source/target arcs. Its size is
O(b), and exact min-plus or max-plus closure computes all parent
entries in poly(b) work with explicit child-route composition
records. Missing routes have infinite distance or minus-infinite
score.

Every physical ordinary directed cycle has positive cost: a
nontrivial cycle contains a donor of positive integer cost.
Source-price leaves cannot be entered, and target-price leaves
cannot be left. Hence all complete route values are attained
by simple physical paths.

More explicitly, any physical parent path splits into child
segments at shared boundaries. Replacing those segments by
optimal child paths cannot worsen its value. Conversely, an
auxiliary route expands to a physical walk. If an optimal
expansion repeated a vertex, deleting the resulting positive-cost
ordinary cycle would give a strictly better physical path, which
also has an auxiliary representation. That contradicts optimality.
Choose minimum-hop deterministic ties to remove empty identity
detours in the auxiliary graph.

This proves the physical simplicity required in Sections 1--4.
The parent composition uses only O(b) child route records.
No unproved bounded overlap of arbitrary route embeddings is used.

## 7. A complete static numerical client on the supplied hierarchy

At the root, the best selected source-to-target path is exactly
the maximum conservative threshold score in the whole graph.
Its endpoint bin IDs and score determine its donor cost sum:
$$
\bar L=\sigma_a-\tau_b-\mathrm{score}.
$$
The ordinary physical path remains implicit.

If the score is positive, the standard finite-grid step applies
to that root witness by Section 3. Endpoint slacks change
explicitly. If the score is nonpositive, the full-graph
sign-compatible circulation argument gives LOW.

The static positivity guards, constant slack-objective progress
and global register count are those proved in
complete_unrestricted_forest_one_sided_client.md. They use simple
accepted paths, not acyclicity of the ambient graph, and therefore
remain valid here.

For a fixed polynomial-range graph,
$$
J=O(\nu\log S),\qquad R=O(J+m\log S).
$$
With q=O(b^2), the resulting total work is
$$
(m+\nu)\exp(O(b^2))\,h\,\mathrm{polylog}S,
                                                               \tag{5}
$$
and the space bound is
$$
(m+\nu)\exp(O(b^2)).
$$
The initialization term includes building all group records.
These bounds are for a fixed edge-partition hierarchy and fixed
physical support. They do not automatically maintain a new
decomposition after a matching contraction or expansion.

## 8. Obtaining a balanced hierarchy from a supplied tree decomposition

There is an elementary conversion when a width-w tree decomposition
is supplied with its full input size D charged. Its preprocessing
cost is an additional O(D poly(w+1)); it is not hidden in the
graph-edge term when the supplied decomposition is larger.

Assign each graph edge to one bag containing its endpoints.
Refine a high-degree bag node into a binary tree of copies of that
same bag, and attach its assigned edges as private leaves.
The running-intersection property ensures that, across every
cut of this display tree, the shared graph vertices lie in
the corresponding separator bag of size at most w+1.

Private endpoint-price leaves can be attached locally to a bag
containing their bin. They do not require a large new interface.
Prune unused display branches and suppress unneeded degree-two
nodes; retain the assigned physical-edge leaves.

Apply the standard balanced top-tree hierarchy to this degree-three
display tree. A connected top-tree cluster has at most two display
boundary vertices. Any graph vertex incident to an assigned edge
inside and an assigned edge outside that cluster belongs to a bag
at one of these two boundary vertices, by running intersection.
Thus the associated graph-edge cluster has boundary size at most
2(w+1), using boundary supersets when convenient.

Children partition the assigned input edges even when a display
cluster contains no such edge. Extra boundary names may be treated
as isolated vertices, with only the zero-edge identity route;
they create no false physical path or source offer. The balanced
hierarchy has logarithmic height.

The top-tree balancing interface is the same primary-source
Theorem 1 already used in the earlier forest notes:
Alstrup, Holm, de Lichtenberg and Thorup, arXiv:cs/0310065v2,
https://arxiv.org/html/cs/0310065v2 .

This gives a static parameterized client with exponential
O((w+1)^2) dependence, plus the charged decomposition-input work.
The claim is the explicit path-update interface, not a new
best-known bounded-treewidth min-cost-flow bound. In particular,
the public ESA 2024 paper Faster Min-Cost Flow and Approximate
Tree Decomposition on Bounded Treewidth Graphs gives an expected
nearly-linear-in-m times sqrt(w) min-cost-flow bound with a supplied
decomposition:
https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.49 .

## 9. Why this does not yet remove the general-graph barrier

A bounded-degree graph can have large separator width. The
exponential factor in (5) is not subpolynomial on arbitrary
matching allocation graphs.

Nor can an overlapping router family simply be substituted for
the edge-partition hierarchy. The proof requires unique physical
coordinate ownership in the children and an explicit finite
signed-use vector for each edge. Copies, hidden alias multiplicity,
or an unbounded number of local route alternatives can invalidate
both the group count and the lazy-update map.

A general-graph application would need a new decomposition or
a much smaller sufficient witness interface, with its actual
construction, update and ownership costs proved. This note does
not assume such a result.

