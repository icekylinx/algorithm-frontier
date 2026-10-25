# Independent audit of lazy updates through a bounded witness interface

**25 October 2026. Mathematical and primary-interface audit passed.**
The operative manuscript is
`bounded_interface_witness_pattern_updates.md`. This review checks the
finite buckets, lazy history, shortest-path compositions and supplied
tree-decomposition conversion. It does not infer an improvement for
general matching or for the best known bounded-treewidth min-cost-flow
algorithm.

## 1. The invariant needed to avoid materializing a bucket

For a fixed hierarchy node \(C\), let \(E_C\) be its uniquely
owned physical allocation coordinates and let \(\chi_C(e)\) be
the vector of signed use by its currently stored witnesses. The
following invariant is sufficient:

* Its nonempty buckets partition \(E_C\), including the zero-use
  bucket, and are indexed by the **current** vectors \(\chi_C\).
* Every bucket's four minima describe the true logical coordinate
  values, including all updates already applied at \(C\).
* A pending tag \(t_C\) denotes precisely those updates already
  included in the bucket minima but not yet included in child minima.
* The current composition maps satisfy
  \(\chi_C(e)=A_i\chi_{C_i}(e)\) on each child edge set.

No claim is made that two edges in one bucket must remain
indistinguishable forever. They are indistinguishable for all current
witnesses, which is the exact property needed by the next update.

For a transfer vector \(t\), every coordinate of a bucket gets the
same increment \(t\cdot\chi\). Its two lower buffers increase
by that scalar and its two upper buffers decrease by it. Thus each
stored minimum and its physical witness ID are updated exactly.

## 2. Why old transfers survive a changed witness family

Before changing a family's witnesses or composition, push the old
tag to both children using the **old** matrices. For an edge in child
\(i\), the increment represented by this push is

\[
       (A_i^{\mathsf T}t_C)\cdot\chi_{C_i}(e)
          =t_C\cdot A_i\chi_{C_i}(e)
          =t_C\cdot\chi_C(e).
 \tag{1}
\]

Hence clearing the parent's tag changes only the location of its
representation. It does not change any coordinate's logical value.
Pushing an ancestor before the descent into a changed child, and then
pushing that child's own tag before its recomputation, ensures that
no pending ancestor increment is ever interpreted in a new family.

Only a root-to-leaf chain is traversed. Pushing at one node updates
both child summaries; the sibling's descendants need not be visited.
The sibling retains its pending tag in its unchanged witness basis.
At an accessed allocation leaf, fold the final pending scalar into its
explicit \(x_e\) and clear its leaf tag before changing its
register or externally setting the coordinate.

The resulting historical-update interpretation is exact even when
different updates used different shortest paths or opposite directions
of the same physical incidence. The data structure does not retarget
an old update onto the latest shortest path.

## 3. Why regrouping needs only child buckets

After the affected child has been recomputed, every **new** parent
witness is composed of the child's **current** stored witnesses.
Therefore its new signatures obey

\[
              \chi_C^{\rm new}(e)
                   =A_i^{\rm new}\chi_{C_i}^{\rm current}(e).
 \tag{2}
\]

If two child coordinates have the same current child signature, (2)
gives them the same new parent signature. A child bucket consequently
maps wholly into one new parent bucket. Taking the minimum of the
four corresponding child minima gives the exact parent minima; no
physical coordinate of that bucket is enumerated.

This also handles edges absent from all former witnesses. If a new
parent route uses one of them, either its current child signature
already distinguishes that use, or the changed child family has just
been rebuilt from its own children. Induction down to single-coordinate
leaves supplies the necessary finer distinction. Keeping the zero-use
bucket is essential for this argument.

The children partition physical coordinates, so their contributions
are never duplicate primal variables. At most \(3^q\) groups per
child are processed, irrespective of how many edges one group holds.
An arbitrary matrix would not justify this bound: the map is the
actual route-composition map and its resulting signatures belong to
\(\{-1,0,1\}^q\) by physical simplicity.

## 4. Exact shortest-path composition and physical simplicity

The stored entries are all ordered boundary distances, all best
source-to-boundary offers, all best boundary-to-target exits, and the
best internal source-target pair. For \(b\) boundaries this is
\(O(b^2)\) routes. The merge graph has the union of the two child
boundary sets and the abstract source and target; its size is
\(O(b)\).

Every physical parent path splits into child subpaths at shared
boundaries. The relevant child entry is no worse than each subpath.
Conversely, each auxiliary route expands to a physical walk with
exactly its stored cost. These two implications establish equality
between the auxiliary optimum and the physical walk optimum. They do
not assume that separately chosen child routes are initially disjoint.

In this numerical client, every nonempty closed ordinary directed walk
contains a donor arc of cost
\(\lceil H/(4\ell_e)\rceil\ge1\). All other ordinary arc
costs are nonnegative. Source-price leaves have no incoming arcs and
target-price leaves have no outgoing arcs, so they cannot participate
in a repeated ordinary cycle of a valid source-target route.

If an optimal auxiliary expansion repeated a physical vertex, deleting
the intervening positive-cost ordinary closed walk would give a
strictly cheaper physical route with the same type of endpoints.
Splitting that route into child pieces would give an auxiliary route
of no larger cost, contradicting auxiliary optimality. Thus the chosen
expansion is physically simple. The same argument applies to
boundary-to-boundary and one-ended entries. Minimum-hop auxiliary ties
remove empty identity detours.

This supplies the simplicity assumption required by (2), rather than
silently assuming a bounded overlap of path embeddings. It uses the
strictly positive ordinary-cycle property of the donor/receiver
network. A general graph with arbitrary zero-cost directed cycles
would need an additional physical-length tie rule or another argument.

## 5. Dirty registers, endpoint prices and transaction order

The root bucket minima detect all crossed registers, including an edge
whose route membership later changes. Its physical witness ID specifies
the unique leaf to access. A root-to-leaf push, one leaf reset and a
bottom-up recomputation restore exact summaries in
\(3^q\operatorname{poly}(q)h\) work. A reset can change a
donor price in either direction; the affected leaf and its ancestors
are still the only DP entries requiring recomputation.

Other dirty coordinates remain represented by minima while this
happens. During that temporary state the stored donor prices remain
positive integers, so the shortest-path compositions are defined even
if the register-to-coordinate approximation is not yet settled.
They are not used for another numerical transfer before all dirty
registers and endpoint-price changes are processed.

A numerical step must first apply its selected old root witness as a
lazy primal update. It then performs all register notifications and
both endpoint slack/price updates as one transaction, settling the
structure before another query can produce a numerical step. The
push-before-remap rule handles any intermediate witness replacement;
the original long path is never needed explicitly.

Guard minima are queried only in buckets with the correct nonzero
signed coordinate for the selected route. Endpoint slack guards are
handled directly. The source and target prices reside on unique
private pendant edges, so changing a high-degree bin's price is a
constant number of point edits rather than a change at every boundary
occurrence.

## 6. Finite tags and cost accounting

An actual simple parent path cannot use a fixed nonempty child route
twice: doing so would repeat a physical allocation edge. More
generally, a single historical root transfer contributes at most once
to a fixed nonempty descendant route before that route's family is
changed. Before a family change, its pending history is pushed below
it. Empty-primal routes can be omitted from tag propagation.

Thus a tag coefficient is a sum of polynomially many bounded grid
steps under the declared history bound. Matrix composition does not
create an uncharged exponential numerical magnitude. The integer
prices, path sums, tag values and minima use the declared
\(O(\log S)\)-bit range, with absent routes/buckets represented by
explicit infinity flags.

Each accepted numerical path is physically simple. Consequently the
conservation, positive-slack objective gain and total negative
allocation log-variation arguments from the unrestricted client apply
without an ambient-forest assumption. Ordinary-only comparison cycles
have zero slack gain; a comparison cycle through the auxiliary slack
vertex gives a simple bin-to-bin path, exactly as in the full-graph
separation proof. Hence an exact nonpositive root score supplies LOW.

Initialization, point edits, register reports and endpoint edits cost
the claimed exponential interface factor per affected hierarchy node.
There are \(O(J+m\log S)\) register events and
\(J=O(\nu\log S)\) accepted steps on the fixed ledger. The
claimed

\[
       (m+\nu)\exp(O(b^2))\,h\,\operatorname{polylog}S
\]

total follows. This does not pay for an arbitrary later replacement of
the graph support or its separator decomposition.

## 7. Supplied tree decomposition to the edge-partition hierarchy

Assign each physical graph edge to a supplied bag containing its
endpoints, and attach a private display leaf owning that edge. Refine
high-degree bag nodes by copies of their own bag. Assigned pendant
price edges are treated as private local leaves; their only shared
graph endpoint is the bin.

The running-intersection property implies that any graph vertex
occurring on both sides of a display-tree cut belongs to its separator
bag. Removing unused branches is harmless. Suppressing a degree-two
display node is also safe: any vertex shared across the suppressed
path occurs in every bag along that path, and hence in its surviving
endpoint bags.

The primary top-tree source is Alstrup, Holm, de Lichtenberg and
Thorup, *Maintaining Information in Fully-Dynamic Trees with Top
Trees*, [arXiv:cs/0310065v2](https://arxiv.org/html/cs/0310065v2),
Section 2 and Theorem 1. Its definition gives binary merges of
edge-disjoint connected clusters, each with at most two display
boundary vertices. Theorem 1 gives logarithmic height and linear
space. Building it by a sequence of links, if necessary, adds only
the allowed logarithmic initialization factor.

A graph vertex with assigned physical edges both inside and outside a
cluster must occur in a bag at one of its two display boundary
vertices. Thus a union of those bags is a valid graph-boundary
superset of size \(O(w+1)\). Empty physical display clusters and
unused boundary names contribute only identity routes for the same
physical vertex, not edges between different vertices. Child clusters
still partition physical coordinate owners.

After pruning and suppression, there are \(O(m+\nu)\) retained
display nodes. The original decomposition must be read and processed;
charge its full representation size and polynomial-width edge
assignment work separately. For the degenerate width-zero case,
\(\exp(O((w+1)^2))\) is an unambiguous form of the dependence.
No decomposition-finding algorithm is supplied for free.

## 8. Comparison boundary

The independent baseline check confirms that Dong and Ye's
[ESA 2024 min-cost-flow result](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.49)
has a much better width dependence for its stated problem and input
model. The present result is a specific deterministic lazy
coordinate-update interface with explicit path-history ownership.
It is not advertised as a new bounded-treewidth flow record, nor as
a way to substitute an overlapping general-graph router for the
edge-partition hypothesis.

