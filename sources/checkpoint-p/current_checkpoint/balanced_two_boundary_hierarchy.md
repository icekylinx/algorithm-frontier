# A balanced promotion hierarchy with at most two boundaries

**Auxiliary mathematical construction for the portal-alias backend.**
This note isolates the static tree geometry used by
`portal_alias_api_reconstruction.md`. It does not assume a dynamic
spanner operation beyond the separately stated alias interface.

## 1. Input and desired interface

An initial portal decomposition supplies connected edge-disjoint pieces
of a forest. A piece has at most two boundary portals and O(k) interior
volume, counting tree vertices, tree edges and old off-tree endpoint
incidences. Off-edge inventories already at a portal are placed in
separate fixed buckets; they do not count repeatedly in each incident
piece. The forest-safe initial decomposition is proved directly in
`disconnected_routing_components.md`, with arbitrary small components
kept dormant. It supplies the tree-portal properties used in
Chen et al., arXiv:2311.18295v1, Section 5:

<https://arxiv.org/abs/2311.18295v1>.

Give each interior vertex weight one plus its number of owned old
off-edge endpoint incidences. Existing boundary copies have weight zero.
The total weight W of a piece is O(k).

We construct a constant-branching hierarchy of refinements. Every
frontier piece has at most two boundary portals. Every two refinement
stages reduce interior weight by at least a factor two. An arbitrary
requested interior vertex becomes a portal after O(log(k+2)) stages,
and every possible separator target for an old interior endpoint is
on its O(log(k+2)) ancestor chain. All inventories belong to a fixed
hierarchy node before any dynamic promotion occurs.

## 2. One balanced refinement

Choose a weighted centroid c of the piece. If it has two old boundaries
p,r and c lies outside the path T[p,r], also select the projection d
of c onto that path. Otherwise c is the only new separator. Splitting
at these at most two vertices leaves components of weight at most W/2:
each is contained in one component after deleting the weighted centroid.

The two-boundary assertion can be checked directly. If c is off the
old boundary path, d separates p from r. The component between c and d
has precisely those two as new boundaries. Every other component has
one new boundary and at most one old boundary. If c is on the old
boundary path, its removal already separates the old boundaries.
With zero or one old boundary, no projection is needed.

High degree at a separator need not give high branching in the
hierarchy. Keep the constant number of components involving an old
boundary or the path between the two new separators separately.
All other components hang from just one new separator. At each new
separator, keep a hanging branch of weight at least W/4 separately;
there are at most constantly many. Group smaller hanging branches
until the total first reaches W/4, then start another group. A completed
group has weight below W/2 and at most one remaining group is lighter.
The total weight of all groups is at most W, so there are constantly
many groups.

A group is connected after its shared separator is included as a
zero-weight boundary. Different groups are edge-disjoint and share
only that boundary. Thus each child is a valid connected piece with
at most two boundaries and at most half the interior weight. The new
separator's own off-edge inventory becomes a fixed root inventory;
its removal from descendant interior weights is legitimate.

## 3. Legal staging of two separators

When both d and c are selected, promote d first, then c. After promoting
d, keep the unique branch toward c as one intermediate piece. The
other already final child groups can be formed immediately. Refining
the intermediate piece at c produces the remaining final groups.
Every stage is a refinement of the preceding stage; no inventories
are merged.

The intermediate piece can have weight exceeding W/2, but the two
stages together achieve the required halving. Every intermediate piece
still has at most two boundaries: the projection promotion separates
the old boundary path before the off-path centroid is promoted. Thus
branch-freeness is preserved after each actual promotion, not merely
at the end of a simultaneous macro-operation.

For alias construction, both planned separators of a macro-refinement
use the SAME frozen parent endpoint inventory. Instantiate a separator's
aliases only after that separator is actually promoted. This is a
uniform overinsertion convention: a side child's path toward the second
separator may already encounter the first separator, so the extra
target can be redundant. It is nevertheless valid and supplies one
simple macro-ancestor inventory rule, with only constantly many target
origins per macro and no change to the logarithmic ancestry bound.

## 4. Depth, work and ancestor closure

Recurse on child pieces. Stop at zero or constant interior weight and
promote any remaining interior vertices explicitly. Positive integer
interior weights and halving every two stages give depth
O(log(k+2)). Repeated centroid computations and grouping cost
O(k log(k+2)) per initial piece. At each depth, interior inventories
are disjoint; boundary copies occur only constantly many times at
each hierarchy node. The construction therefore does not hide a
large collection of zero-weight boundary records.

Maintain a frontier in this fixed hierarchy. To promote an arbitrary
interior vertex v, refine the nodes on its ancestor chain until v is a
boundary. There are only O(log(k+2)) stages, with constantly many new
pieces at each. Promotions remain permanent during the portal period.
Refining a group at a boundary that already exists is a virtual
inventory refinement, not another physical portal birth.

For any old endpoint u, reserve targets at the at most two initial
boundaries and at every separator on u's macro-ancestor chain. There
are O(log(k+2)) targets. If an old initial-tree path from u meets a
current permanent portal, the first such portal is witnessed by one
of these targets: the first refined hierarchy region that separates
u from that portal has an ancestor separator on that path. If no
refinement separates them before leaving the initial piece, their
path meets an initial boundary. All required ancestor separators
were promoted before descendant regions were refined.

The alias note uses the first current portal on the FIXED initial-tree
path from u to each target. It does not require the entire target path
to survive later tree cuts. Before a physical tree edit its endpoints
are promoted, so every retained endpoint-to-first-portal leg remains
valid and can only shorten. This last dynamic step is proved in the
alias note; the present hierarchy supplies its fixed targets,
bounded ancestry and legal promotion order.
