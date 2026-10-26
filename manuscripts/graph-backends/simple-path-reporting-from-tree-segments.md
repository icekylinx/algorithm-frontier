# Simple-path reporting from a logarithmic number of tree segments

**25 October 2026. Constructive improvement of the SSSP output interface.**

This note strengthens the expanded-walk interface in [incremental sssp proof](../../problems/incremental-sssp/proof.md). Under the same recursive construction, a query can return a simple directed path with approximation guarantee at most the maintained distance estimate, in

$$
O\!\left((k+B^2)\operatorname{poly}(\log N)\right)
$$

time, where `k` is the number of root edges actually returned and `B=O(log N)` is the recursive depth. The preprocessing adds only a polynomial logarithmic factor to the already charged Dijkstra and leaf computations. In particular this is `O((k+1) poly(log N))`, and does not enumerate a potentially much longer walk before deleting its cycles.

The construction is deterministic. Its tree-intersection index is described directly below, without requiring a black-box geometric data structure. It uses the special feature of this recursion that all new edges are source edges; every edge with a non-source tail is a copy of a root graph edge.

## 1. Tree versions and a required estimate policy

At the beginning of each nonleaf phase, retain the exact shortest-path tree used to compute that phase's frozen anchors. A leaf retains its exact tree from its most recent complete Dijkstra computation. Every such tree is directed away from the common source. All its vertices carry their original root vertex identities.

Use the following estimate policy. An old vertex outside the exceptional set uses its phase anchor. An old vertex inside the exceptional set uses the smaller of its frozen phase anchor and its current child's estimate. A new vertex has no phase anchor and uses its child's estimate. A leaf uses its exact current distance.

All these estimates are costs of available walks. The minimum does not weaken the approximation guarantee. Values can be made nonincreasing between vertex birth and owner retirement: a phase restart recomputes exact distances in an incremental graph, so its new exact value is at most the previous available-walk value. Induction gives the same property for child values.

This policy needs no historical minimum over arbitrarily old child versions. Each stored choice refers either to the owner's current immutable phase tree, or to the current vertex record of its one active child. Equal-value ties may be resolved toward the current version. A restart overwrites the owner's records before its old child and phase tree are retired. A query is issued only after that transaction and all ancestor notifications settle.

Consequently a query descends along one active owner chain until it reaches an exact phase-tree or leaf-tree value. Every proxy in that tree refers to one of the active ancestor phase trees. It never needs an index involving an unrelated retired tree version. If an implementation elects to retain arbitrary historical witness pointers instead, it must retain the corresponding indices and charge their lifetimes; the simpler policy above avoids that obligation.

## 2. The expanded walk has only `O(B)` native pieces

Consider an exact tree path from the source to a queried vertex in a local graph. Since all lengths are positive, the source occurs only at the beginning. Every newly constructed non-native edge has the source as its tail. Thus the tree path contains at most one non-native edge, and it is its first edge. Its remaining suffix is a directed ancestor path of native root edges in that local shortest-path tree.

A non-native source edge has one of these origins:

* An old-vertex anchor of cost `D(v)`, represented by the parent phase-tree path to `v`.
* A proxy of cost `D(u)+ell(u,w)`, represented by the parent phase-tree path to the old outside tail `u`, followed by the original root edge `(u,w)`.
* A copy of a parent's existing source edge, carrying its unchanged provenance.

In the second case, `u` is not the source because the source is always exceptional. Therefore `(u,w)` is a native root edge. A copied source edge can be resolved to its creator by following its provenance; each such step moves strictly upward in the owner chain. The total number of such upward steps for a query is `O(B)`.

Expanding the first source edge and repeating in the ancestor tree therefore produces at most `B+1` directed native tree-path segments, together with at most `B` single native connector edges. Zero-length-in-edges segments may be omitted. The total number of pieces is `O(B)`, although the number of root edges represented by those pieces can be much larger.

The connector edges must be counted explicitly: the edge `(u,w)` in a proxy need not be an edge of either shortest-path tree. Ignoring it would be an incorrect claim that there are only tree-path pieces. Handling a single edge separately is straightforward in the intersection and cycle-removal procedure.

Store a root edge identity directly on every native edge record. Then enumerating a retained native tree segment requires no further recursive expansion of its individual edges.

## 3. Intersection of two directed ancestor paths

Let `T_1,T_2` be two immutable rooted shortest-path trees. Their vertex sets may differ. For each vertex present in both, form the four-dimensional point

$$
x\longmapsto
 (\operatorname{tin}_1(x),\operatorname{tout}_1(x),
  \operatorname{tin}_2(x),\operatorname{tout}_2(x)).
$$

Use inclusive DFS subtree intervals. Let `P_1=T_1[a,b]` and `P_2=T_2[c,d]`, where the first endpoint of each is an ancestor of the second. A common vertex `x` belongs to both paths exactly when

$$
\begin{aligned}
 \operatorname{tin}_1(a)\leq\operatorname{tin}_1(x)&\leq\operatorname{tin}_1(b),&
 \operatorname{tout}_1(x)&\geq\operatorname{tin}_1(b),\\
 \operatorname{tin}_2(c)\leq\operatorname{tin}_2(x)&\leq\operatorname{tin}_2(d),&
 \operatorname{tout}_2(x)&\geq\operatorname{tin}_2(d).
\end{aligned}
\tag{1}
$$

The upper bound on `tin(x)` and the lower bound on `tout(x)` say that `x` is an ancestor of the path's lower endpoint. Along that ancestor chain, `tin(x)>=tin(a)` clips it precisely at `a`, since `a` is an ancestor of `b`. Thus (1) is one orthogonal box query in fixed dimension four. A depth coordinate is unnecessary for membership.

Among the points in the box, minimum or maximum depth in either tree returns the first or last intersection along that tree's directed path. A witness vertex identity is retained with each extremum. It is not necessary that the endpoints themselves belong to both trees.

### 3.1 A self-contained sparse index

All coordinates lie in an integer universe of size `O(N)`. For each of the four coordinates, use the implicit complete dyadic interval tree on that universe. A coordinate value belongs to `O(U)` ancestor intervals, where `U=log_2N`. For every common vertex, enumerate the Cartesian products of its four ancestor-interval lists. There are `O(U^4)` such four-interval cells.

Store only nonempty cells in a deterministic balanced dictionary keyed by their four interval identities. Each cell stores minima and maxima of both tree-depth values and a witness vertex for each extremum. Inserting one point takes `O(U^5)` time, including dictionary lookup. An index on `q` common vertices therefore uses

$$
O(qU^4)\text{ space and }O(qU^5)\text{ construction time}.
\tag{2}
$$

For a query, decompose each of its four coordinate intervals into `O(U)` disjoint dyadic intervals. Their Cartesian products form `O(U^4)` cells. Look up their stored extrema and combine them. The cells are disjoint and cover precisely the query box, so the result is exact. Query time is `O(U^5)`.

No full four-dimensional grid is allocated. Empty tree intersections are represented by an empty dictionary. The intervals and dictionary keys have `O(U)` bits, and the number of coordinates is the fixed constant four. The polynomial exponents here are deliberately conservative; faster standard range-searching indices are optional and unnecessary for the claimed graph exponent.

For two pieces in the same tree, either use the same index with `T_1=T_2`, or answer directly using ancestor/LCA information. Including a self-index in (2) is sufficient.

### 3.2 Single native edges

A single directed connector edge has only its two endpoint vertices. To intersect it with a tree segment, test each endpoint using the Euler-interval conditions above. To find the last intersection along a tree segment, compare the depths of the qualifying endpoints. To find the last intersection along the edge, prefer its head when both endpoints qualify. Two single edges require only endpoint identity comparisons.

These cases take constant time given local tree lookup, or `O(U)` time with deterministic dictionaries. They do not require constructing an index for a temporary two-vertex tree.

## 4. Preprocessing the tree pairs without repeated large scans

When a new shortest-path tree `T` is built, compute its DFS intervals, depths, and parent pointers. Build an intersection index between `T` and each active ancestor phase tree, as well as the optional self-index.

To find common vertices, iterate over the vertices of `T` and perform membership lookups in the ancestor tree. Do not scan every ancestor's entire vertex set. Thus an owner with local allowance `M` and at most `B` ancestors spends

$$
O(BM\operatorname{poly}(U))
\tag{3}
$$

extra time when its exact tree is created. This is only a polynomial logarithmic factor over that Dijkstra computation. At a leaf the same work is charged after each recomputation, within the previously allowed `M^2 poly(U)` lifetime cost.

An ancestor phase tree remains immutable for the lifetime of every descendant that may refer to it. If that ancestor restarts, its descendants are retired before new descendants are queried. Every pair of trees that occurs in one query is therefore either an ancestor/descendant pair indexed when the lower tree was created, or the same tree. Tree indices may be retired with their actual tree version, with cost charged to their previous construction.

The factor `B<=O(U)` in (3) is computational overhead. It changes neither the detector reporting bound nor the child inventory multiplier. It is absorbed into the polynomial logarithmic work factor, without creating an extra raw-oracle loss at every recursive depth.

## 5. Removing cycles from the whole walk by segment operations

Let the native pieces in root-to-target order be `P_1,...,P_t`, where `t=O(B)` and every piece is simple. Adjacent pieces have matching endpoints. Maintain a simple directed path `Q` for the already processed prefix, represented as a list of clipped tree segments and single edges. Initialize it with the source alone.

To append a new piece `P`:

1. Initialize the candidate intersection to the current endpoint of `Q`, which is the first vertex of `P`. This also handles the initial path consisting only of the source, or a path truncated back to that single vertex. For every stored nonempty piece of `Q`, find the last vertex along `P` that also lies in that stored piece. Use the range index when both are tree paths and the endpoint tests otherwise.
2. Among the default candidate and all returned answers, choose the vertex `v` latest along `P`. The default candidate guarantees existence even when `Q` has no stored edge piece.
3. Truncate `Q` just after `v`, deleting all later pieces and clipping its last retained piece if necessary.
4. Append the suffix of `P` after `v`. Omit empty pieces and repeated boundary vertices.

The result is a simple directed path. Indeed, `Q`'s retained prefix is simple, the suffix of `P` is simple, and no vertex of that suffix belongs to the old `Q` by the choice of the last intersection. Their only common vertex is the joining vertex `v`.

The operation preserves the current target and cannot increase total cost. It removes the closed directed walk consisting of `Q`'s old suffix from `v` to the old endpoint, followed by `P`'s prefix back to `v`. Every removed edge has nonnegative cost. This procedure need not produce the same path as a vertex-by-vertex chronological loop erasure; equality with that particular output is neither claimed nor needed.

The representation remains closed under truncation. A clipped directed ancestor path is another directed ancestor path in the same immutable tree. A clipped single edge is either the edge or an empty piece. After processing `i` pieces, at most `i` nonempty pieces remain. There are consequently `O(t^2)` pair-intersection queries, plus `O(t^2)` conservative bookkeeping.

The final simple path can now be enumerated. A tree segment `T[a,b]` is output by following parents from `b` to `a` and reversing that list. This visits precisely the edges that will be returned. Single connector edges are output directly by their root identities. Therefore the query cost is

$$
O(t^2\operatorname{poly}(U)+k\operatorname{poly}(U))
 =O((B^2+k)\operatorname{poly}(U)).
\tag{4}
$$

No root edge lying only in a deleted long segment is enumerated. This is the distinction that permits the bound to depend on the final simple-path length rather than the length of the original expanded walk.

## 6. Approximation and supported output

The initial compressed walk has cost equal to the selected available-walk estimate. Every segment-level deletion removes a closed directed walk of nonnegative cost. The returned simple path consequently has cost at most that estimate, and at least the true source distance. Its approximation guarantee is the same as the distance estimate's guarantee.

For a nonnegative-integer input reduced using a fixed positive perturbation, the same path is valid in the original graph and deleting cycles cannot increase original cost. The original integer cost is at most the rescaled perturbed upper estimate, and hence at most its floor if an integer estimate is returned. A zero-distance query obtains an original zero-cost path whenever the rescaled bound is below one.

The source query returns the empty path. An unreachable query returns the existing unreachable indication. For every other reachable target, (4) gives an explicit simple directed path with original edge identities in `O((k+1) poly(log N))` time. The statement is not the literal `O(k)` path-query bound of the public Liu theorem, but it supplies output sensitivity up to a fixed polynomial logarithmic factor with a complete construction.
