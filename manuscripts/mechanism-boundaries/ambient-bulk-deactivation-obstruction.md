# A normalized-image obstruction to bulk ambient deactivation

**A mechanism boundary, 24 October 2026.** This note examines one concrete
congestion-aware modification of a greedy spanner. It does not give a lower
bound for ambient-aware sparsification, and it does not claim that an
arbitrary dynamic matching trajectory realizes the construction.

The failed rule is: once an ambient resource reaches its load threshold,
remove from the **active** graph every selected native edge whose fixed
ambient image uses that resource, while retaining the selected edges and
the already assigned demand routes in the output. The example below uses
loads of the **loop-erased ambient routes**. It is not a counterexample
that depends on counting canceled traversals.

## 1. The precise rule

Let $`J`$ be a loopless native multigraph. Its edge IDs are distinct even
when their endpoints agree. Each native edge $`e=uv`$ has a fixed simple
path $`\Pi(e)`$ in an ambient graph, from the image of $`u`$ to the image
of $`v`$. Write
```math
\Delta=\max_v\deg_J(v),\qquad
 C_0=\max_x|\{e:x\in\Pi(e)\}|.
 \tag{1}
```
Endpoints are included in vertex congestion.

The algorithm maintains an active native graph $`F`$, a retained selected
graph $`H\supseteq F`$, and one assigned route for each processed native
edge. Initially both graphs are empty. On processing $`e`$:

1. If its endpoints have an $`F`$-path of at most $`b`$ edges, use such a
   path. Otherwise select $`e`$, insert it into $`F`$ and $`H`$, and use
   its identity route.
2. Concatenate the fixed ambient images of the chosen native path, then
   erase loops before adding its vertex loads.
3. At a resource whose load first reaches $`\tau`$, deactivate every edge
   of $`F`$ whose fixed image contains that resource. Deactivation does
   not remove an edge from $`H`$ or change earlier assigned routes.

Take any fixed integer $`c\geq1`$ and integer quality parameter
$`\gamma\geq1`$, with the prescribed scalar threshold
```math
\tau=c\gamma(C_0+\Delta).
 \tag{2}
```
The same scalar threshold may also be imposed on ambient edges. The
example has no earlier edge-threshold event.

The construction works for every $`b\geq3`$. In fact every active graph
that occurs is a forest, so no choice between different active native
paths is involved.

## 2. Native graph and exact threshold calibration

Choose an integer $`s\geq64c\gamma`$. Let $`A,B`$ be disjoint sets of
size $`s`$, so the native vertex count is $`n=2s`$. Put
```math
P=\left\lfloor\frac{s}{16c\gamma}\right\rfloor,\qquad
 D=4s,\qquad
 q=8c\gamma-2.
 \tag{3}
```
Choose distinct centers $`a_j\in A,b_j\in B`$, for $`1\leq j\leq P`$.
For phase $`j`$, create a cross double-star
```math
T_j=\{a_jb:b\in B\}
       \ \cup\ \{ab_j:a\in A\setminus\{a_j\}\}.
 \tag{4}
```
It has $`2s-1`$ edges, diameter three, and every edge joins $`A`$ to $`B`$.
All occurrences in different phases have distinct native IDs. In
particular, two different double-stars can contain parallel IDs on
$`a_i b_j`$; these IDs must not be silently identified.

Following the tree edges of phase $`j`$, create
```math
T=qs+1
 \tag{5}
```
cross-demand IDs. They consist of $`q`$ perfect matchings between $`A`$
and $`B`$, followed by one extra edge. The $`Pq`$ full matchings can be
chosen edge-disjoint, since $`Pq<s/2`$. The extra edges can have distinct
endpoints across phases. Parallel IDs with tree edges remain allowed.

A center has at most $`s+P-1`$ tree incidences across all phases. Every
vertex has at most $`Pq+1`$ incidences in the full-matchings-plus-extra
demands. Thus every degree so far is less than $`2s`$. Add a final group
of parallel padding IDs on any one native pair, all processed after the
phases, until the larger endpoint degree equals $`D`$. This takes
$`O(s)`$ IDs, gives exactly
```math
\Delta=D,
 \tag{6}
```
and does not affect any phase. The smaller endpoint degree remains at
most $`D`$.

There are
```math
m=P(2s-1+T)+O(s)=\Theta(s^2)
 \tag{7}
```
native edge IDs. Constants may depend on the fixed $`c`$, but not on
$`s,\gamma`$.

## 3. Ambient images and their normalization

For each phase add a private ambient hub $`x_j`$. Its incident ambient
edges join it to all native vertices. Map every ID $`uv\in T_j`$ to
```math
u-x_j-v.
 \tag{8}
```
Every matching-demand and padding ID gets its own direct ambient edge
between its native endpoints.

The input paths are simple. No native vertex is an internal vertex of
an input path. Hence its input congestion is exactly its native degree.
The input congestion of $`x_j`$ is $`2s-1`$, and all other relevant
resources have smaller congestion. Therefore
```math
C_0=D.
 \tag{9}
```
The declared threshold is consequently the exact integer
```math
\tau=2c\gamma D=8c\gamma s.
 \tag{10}
```

For a native path lying in $`T_j`$, its concatenated ambient walk lies
entirely in the star centered at $`x_j`$. Every intermediate native
vertex produces a return excursion from $`x_j`$ and back. Loop erasure
therefore gives exactly
```math
u-x_j-v
 \tag{11}
```
for the demand's endpoints $`u,v`$. In particular, $`x_j`$ receives
**one**, rather than three, new units from a length-three native route.
The same conclusion holds for all identity routes of $`T_j`$.

## 4. Every phase deletes its entire active tree

At the start of a phase the active graph is empty. Every edge of $`T_j`$
is selected, because every proper initial subset of a tree has
disconnected endpoints for its next edge. The $`2s-1`$ identity routes
give $`x_j`$ that initial load.

The following $`T`$ cross demands have unique active paths of at most
three edges. Thus none is selected. By (11), each gives exactly one
unit to $`x_j`$. Equations (3), (5), and (10) yield
```math
\begin{split}
  (2s-1)+T
     &=(2s-1)+(8c\gamma-2)s+1\\
     &=8c\gamma s=\tau.
 \end{split}
 \tag{12}
```
The hub reaches its threshold precisely on the last demand.

There is no earlier ambient vertex event. A native vertex receives load
only when it is the endpoint of a processed native demand; its total
load throughout the whole run is at most its native degree, at most
$`D<\tau`$. Other hubs have disjoint phase roles. An arm $`vx_j`$ receives
at most the current hub load, and in fact strictly less than $`\tau`$:
its phase load is at most $`s+q+1`$, whereas
$`\tau=8c\gamma s`$.

At the event in (12), every edge of $`T_j`$ has a fixed image containing
$`x_j`$. The rule therefore removes the whole tree from $`F`$. It keeps
all $`2s-1`$ edges in $`H`$, with their already assigned routes. This
establishes the induction needed to start the next phase with empty
active graph.

After the $`P`$ phases,
```math
|H|\geq P(2s-1)=\Omega\!\left(\frac{n^2}{c\gamma}\right).
 \tag{13}
```
Processing the final padding cannot remove these retained IDs.

For example, with $`\gamma=\lceil\log_2 n\rceil`$, the rule keeps
$`\Omega(n^2/\log n)`$ IDs on an input with $`m=\Theta(n^2)`$, despite
normalized ambient paths of constant length and threshold
$`\Theta(\gamma(C_0+\Delta))`$. This is much larger than
$`n\mathrm{polylog}n`$. The active high-girth invariant provides
no bound on the inactive inventory: every active graph here is a tree.

## 5. Degree-three ambient variant with short simple input paths

The hubs' large physical degrees are not necessary. For each phase,
replace its star by a balanced binary tree $`X_j`$, with $`s`$ leaf
positions for $`A`$ in its left half and $`s`$ leaf positions for $`B`$
in its right half. Attach each native vertex to its phase leaf.
Map an edge of $`T_j`$ to the unique path between its two attached
native vertices.

Because every edge in (4) joins $`A`$ to $`B`$, every such input path
uses the central edge $`f_j`$ of $`X_j`$. Every subsequent cross-demand
route, after loop erasure inside this one tree, is its unique
endpoint-to-endpoint tree path and also uses $`f_j`$. No noncentral
resource gets more phase load than $`f_j`$; the two central endpoint
vertices have the same full phase load. Thus the scalar threshold
event again deactivates all of $`T_j`$, no later than the event in (12),
and no earlier resource can change the active support: a resource
reaching the scalar threshold must already have accumulated the full
hub-equivalent count.

Replace each native vertex's physical incidence list by its own
balanced binary port tree. The canonical native image is its root;
one port is used for each phase-tree attachment and each direct-demand
incidence. Input paths start or end at this root. When a composed
$`T_j`$-walk visits an intermediate native vertex, the two traversals
of its same phase-attachment path cancel. Therefore the normalized
route is still the unique path through $`X_j`$, with only its two
endpoint port-tree paths.

All physical degrees are at most three, input path lengths are
$`O(\log n)`$, and the total ambient size is $`O(m)`$.
The input congestion of a port fiber is at most the corresponding
native degree; the central resources of $`X_j`$ have congestion
$`2s-1`$. Hence $`C_0=D`$ still holds. Native-fiber query loads are
endpoint loads and remain at most $`D`$. The same exact scalar
threshold and retained-ID lower bound follow.

This version is still a statement about the specified fixed-image
rule. Loop erasure is permitted; arbitrary replacement of a route by
a different ambient path is a different algorithm.

## 6. What would have to change

The failure is already static. It is not caused by dynamic route
notifications, moving endpoints, amortized update credit, or a failure
to implement short native path queries.

The input is a generic fixed-image native/ambient interface. This note
does not assert that each image contains a distinct own central
physical edge, that it is generated by a first-touched projection, or
that a particular matching-backend initializer produces the table.
Those are separate reachability restrictions. The present conclusion
is the exact failure of the stated bulk-deactivation template on its
advertised general ambient input.

The obstruction does not exclude a rule that:

* retains only a carefully chosen subset of the edges using a saturated
  resource;
* selects new native edges according to the ambient capacity they add,
  rather than merely abandoning all current images through the resource;
* reroutes earlier demands and proves a joint bound on its new selected
  inventory and the work of those reroutings; or
* computes paths in a richer ambient network instead of concatenating
  fixed images of the currently active native support.

Such a repair needs an additional theorem. The active native girth
bound and the threshold $`\Theta(\gamma(C_0+\Delta))`$ alone do not
prove sparse retained support. In particular, replacing a native-edge
congestion counter by a literal ambient congestion counter does not,
by itself, close the ambient-aware low-recourse interface needed by
the matching backend.
