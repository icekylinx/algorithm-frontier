# Disconnected inputs in the routing, portal, and Steiner backend

**Scope.** This note supplies explicit component accounting for the
primary routing/portal/Steiner reconstruction. It does not use an
assertion that an arbitrary spanning forest has only `O(m/k)`
components. There may be Theta(m) small components. Their local
records are retained at the parent, and they produce no recursive
vertices merely by existing.

The tree-cycle subproblem has the scope of source Definition 3.2:
it compares only current fundamental cycles `e+T[v,u]` for off-tree
edges whose endpoints are connected in T. It is not itself an oracle
for every cycle in `T union E_off`. The outer HRG comparison guarantees
that a suitable fundamental cycle exists in at least one member of
its tree family when the general-cycle optimum is nonzero.

The relevant primary source is Chen et al., arXiv:2311.18295v1,
<https://arxiv.org/abs/2311.18295v1>, Definitions 4.2 and 4.12,
Lemma 4.32, and Section 5. The weighted portal construction below
is stated directly so its use does not depend on extending a
connected spanning-tree decomposition theorem without accounting
for the number of connected components.

## 1. A weighted portal decomposition with dormant components

Let T be an arbitrary forest, let E_off be its off-tree edge set,
and let

    m = |V(T)| + |E(T)| + |E_off|.

Off-tree edges can join different T components. Give every vertex
the positive integer weight

    omega(v) = 1 + number of old off-edge endpoint incidences at v.

Thus total weight `W<=2m`. A loop has two endpoint incidences.
Fix `k>=2`; calls below the ordinary recursive base threshold are
handled directly.

### Lemma

In `O(m)` time one can find a branch-free portal set P of size
`O(m/k)` and a collection of initial pieces with the following
properties.

1. Every component of `T-P` has interior weight less than k and
   is incident to at most two portals.
2. Pieces with at least one portal boundary are connected and
   edge-disjoint, have at most two boundary portals, and have
   `O(k)` interior vertex/off-edge-incidence volume. There are
   `O(m/k)` such active pieces.
3. Every remaining original T component has no portal and weight
   less than k. It is a dormant piece. There can be arbitrarily
   many dormant pieces, but their total size is O(m).
4. Old off-edge endpoints at portals are owned by fixed root
   buckets of at most k endpoint IDs. The total number of buckets
   is `O(m/k)`.

### Construction and proof

Root each T component temporarily. In a bottom-up pass, accumulate
the residual weights of children that have not already been cut off
by a marked vertex. If a vertex's accumulated weight, including its
own weight, is at least k, mark that vertex and pass residual weight
zero upward. Otherwise pass the accumulated weight upward.

Each mark can be charged to a disjoint set of at least k weight
units, namely the residual units consumed at that mark. Hence the
initial marked set P0 has at most `W/k` vertices. Every component
of `T-P0` has weight less than k: its highest vertex passed precisely
its component's residual weight upward without being marked.
This rule also handles a vertex whose own off-edge degree exceeds k;
that vertex is marked immediately.

Within each T component, take the minimal subtree connecting P0
and add to P0 every branching vertex of that subtree. A tree with
r marked vertices has at most r-2 additional unmarked branch
vertices when r>=2; with zero or one marked vertex nothing is added.
The resulting set P has size at most `2|P0|` and is branch-free.
Adding portals cannot increase the weight of a component of `T-P`.
This closure and the preceding pass both take linear time.

Consider the components of `T-P`.

* A component with two portal neighbors, together with its two
  boundary edges, is one active piece. There are at most `|P|-1`
  such pieces: contracting them to portal-to-portal connections
  gives a forest. Direct T edges between portals have the same
  O(|P|) count and form zero-interior active pieces.
* At a fixed portal p, group the components with exactly that one
  portal neighbor. Accumulate their weights until a group first
  reaches k, and then begin the next group. Every component has
  weight less than k, so a completed group has weight less than
  2k; the final group has weight less than k. A group plus its
  shared portal p is connected. The number of these groups is at
  most `W/k+|P|`.
* A component with no portal neighbor is an original T component
  with no portal. Its weight is less than k and it stays dormant.

Different active pieces share only their boundary portals and have
disjoint tree edges and interior inventories. Tree-edge volume is
also O(k) per nontrivial piece: in a forest it is bounded by the
number of interior vertices plus the constant number of boundary
vertices. Finally, splitting each portal's old off-edge incidences
into groups of at most k uses at most

    |P| + sum_(p in P) deg_off(p)/k = O(m/k)

buckets. Boundary incidences are not counted again as interior
inventory in every adjacent piece. This proves the lemma.

## 2. Initial auxiliary and recursive size

Build the balanced hierarchy of
`balanced_two_boundary_hierarchy.md` for every active or dormant
piece. All hierarchy and old-edge metadata together costs
`O(m log(k+2))` space and time. This includes metadata for every
dormant component; it is parent initialization work.

Allocate auxiliary target origins only for boundaries of active
pieces and the root buckets. A dormant piece has no targets and
allocates no auxiliary slot. Initial compressed portal-to-portal
tree paths number O(|P|), even if the original forest has many
components. Thus

    n_aux(initial) = O(m/k).

An off-tree edge with a dormant endpoint has no routed target pair
until both endpoint inventories become active. This is intentional.
If its endpoints lie in different current T components, it has no
fundamental T cycle to represent. If both endpoints lie in one
dormant component, its simple fundamental cycle is stored in the
local candidate heap.

The selected spanner H has `O((m/k) A)` edges. The Steiner bridge
uses terminals consisting only of P and original endpoints of
retained H aliases, not all vertices and not one root for every T
component. Its compressed forest K consequently has

    |V(K)|+|E(K)| = O(|P|+|E(H)|) = O(m A/k).

A T component with no terminal contributes nothing to K. A component
with one terminal contributes one anchor and no compressed tree
edge. The number of such one-terminal components is at most the
number of terminals. Fixed port fibers therefore also number only
`O(m A/k)`; no hidden component-count term enters the child graph.

If P and H are empty, the recursive graph is empty and no child
instance needs to be initialized. Any nonzero fundamental-cycle
comparison for this tree-cycle instance can then come only from the
local candidates, which are fully maintained. A cycle formed solely
by off-tree edges crossing distinct T components is outside this
subproblem's comparison objective; it is not asserted to be absent
from the full graph.

## 3. Local zero-portal and one-portal cycles

Maintain one disjoint copy of the entire current forest T at the
parent, including its dormant components. Its total size is O(m).
For every off-tree edge with endpoints in the same T component,
test the number of portals on its unique tree path. If that count
is zero or one, keep its exact simple fundamental-cycle numerator
and literal length in the local heap.

The heap can have Theta(m) keys; this is part of parent storage and
initialization, not recursive size. This rule includes cycles in
small disconnected components and cycles joining two hanging
pieces through their sole shared portal.

A promotion affects a previously local key only if an endpoint
of its off-tree edge belongs to the promoted piece's interior
inventory. If neither endpoint does, a simple path entering and
leaving a two-boundary piece already contains its two old portals.
For a one-boundary piece it cannot enter and leave through that
same boundary on a simple path. Thus the O(k)-inventory scan finds
every affected local key.

Before a tree-edge cut or repricing, both endpoints are promoted.
Every local cycle whose path uses that edge then has at least two
portals, so the preceding inventory scans remove it from the local
heap and install the relevant routed variants. A tree link cannot
alter an existing path within one old component. A newly created
fundamental path crosses the link's two portal endpoints and is
already a routed comparison, rather than a missing local key.

## 4. Activating a dormant component

Before a requested promotion in a dormant component, use its stored
O(k)-weight hierarchy to promote the necessary ancestors. Scan its
old endpoint inventory and create the targets that have actually
become active. This costs `k polylog(m*aspect)` local work and only
polylogarithmically many origin-slot births and native split/birth
API calls.

Many edge aliases can be inserted during this activation. They use
the legal ordinary `InsertEdge` operation with the cumulative master
degree bound from the alias note. They do not each contribute to
the source spanner's expensive-update recourse count.

If a tree link connects two formerly distinct components, promote
both link endpoints before linking. Any old off-tree edge which now
has a fundamental path crosses that link. At each end of its path,
the required first portal is either already an active boundary or
was installed by the local activation of a formerly dormant
component. An edge whose other endpoint is still dormant cannot
yet require a routed comparison through that untouched component.
No global scan of formerly crossing off-tree edges is needed.

There are only O(Q) requested endpoint/vertex promotions over Q
ordinary parent edits, up to the explicit logarithmic hierarchy
factor. Therefore activation does not add the number of initially
dormant components to either the auxiliary birth count or the
recursive edit count.

## 5. Period accounting and HRG componentwise validity

At a nonbase call, take a nominal starting size m and a period of
at most `floor(m/k)` ordinary input edits, with ordinary constant
allowances for endpoint promotions. Current size stays O(m).
The hierarchy bookkeeping and aliases give, including all retired
isolated auxiliary slots,

    n_aux = O(m/k+Q polylog(m)),
    q_bad = Q polylog(m*aspect),
    child size = m A/k,
    child input edits = (m/k+Q) A.

Rebuilding retires the old child and its real pools using the
already specified retirement discipline. Its O(m A Gamma) parent
work is charged to the period, giving O(k A Gamma) amortized work.
When m is below the recursive base threshold, use the direct base
algorithm instead of a fractional-length period. The initial local
T copy and local heap are rebuilt by an O(m A) scan. No per-dormant-
component child initialization is performed.

The preceding argument applies to each HRG tree-cycle instance.
The HRG itself is also componentwise: source Definition 4.12 chooses
a final covering cluster separately for each connected component A
of the input graph, and Theorem 4.9 routes that component's demands
to its own representative. Its tree-family enumeration uses one
global family of choices; it does not multiply its size by the
number of connected components. Each member can be viewed as a
forest, as expressly permitted by the tree-cycle interface.

All routing forests and component metadata have their usual total
O(m A) size. Applying the portal decomposition above to each such
forest leaves the primary recurrence unchanged. Thus disconnected
general input, including arbitrarily many small components, does
not require the impossible bound `cc(T)=O(m/k)`.
