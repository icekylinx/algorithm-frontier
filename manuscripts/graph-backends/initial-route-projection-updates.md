# What changes when all repairs use the initial route table

**Separate interface analysis, 24 October 2026.** A possible route
to better dynamic quality is to retain one initial short route table,
keep all touched vertices since its creation, and maintain its
projected demand graph dynamically. If that projected graph could be
handled with little selected-central-edge recourse, its preliminary
ambient images would retain the initial length bound. This note
identifies the exact update operation that needs a new theorem.
It does not rule out such a theorem and does not change the reviewed
$4/5$ construction.

## 1. The proposed benefit

Let $R_0(e)$ be a fixed initial route of length at most $\Lambda$
for each input edge $e$. Current insertions may separately receive
their identity routes. At time $t$, keep every native vertex
touched since initialization. For a surviving input edge, take the
first touched anchor from each current endpoint of its old route,
using the split/deleted-path convention of
[normalized-projected-route-composition.md](normalized-projected-route-composition.md).

The preliminary image of the resulting projected edge consists of
two still-valid exterior prefixes and the current central input
edge. Its length is at most $2\Lambda+1$, independently of how
many later static repairs have occurred. A sufficiently strong
dynamic sparsifier on this projected graph could therefore give
quality controlled by $\Gamma\Lambda$, rather than by
$\Gamma^{O(K)}$.

This observation alone is not an update algorithm. The current
projected graph is not, in general, an insertion-only graph with
ordinary native vertex splits.

## 2. A constant-length example of multiple-origin extraction

Fix an integer $s\geq2$. Let the original graph have a hub $h$,
sets
$$
W=\{w_1,\ldots,w_s\},\qquad
             A=\{a_1,\ldots,a_s\},
$$
every star edge $hw_i,ha_j$, and every edge
$$
e_{ij}=w_i a_j.
 \tag{1}
$$
All edge IDs are distinct, and the graph is loopless and simple.
It has $\Theta(s^2)$ edges and maximum degree $2s$.

Take the star as the initial selected base. Every demand in (1)
has the two-edge initial route
$$
w_i-h-a_j.
 \tag{2}
$$
Star edges have their identity routes. Thus the initial route
length bound is the absolute constant two.

First, for each $j$, split $a_j$ into $a_j^B$ and $a_j^D$:
put the edge $ha_j$ at $a_j^B$, and all edges $e_{ij}$ at
$a_j^D$. Both new endpoints are touched. These are genuine
native splits; they do not introduce new edge IDs.

The initial route of $e_{ij}$ is now broken. From its $w_i$
endpoint, its first touched anchor is $a_j^B$; from its current
$a_j^D$ endpoint, the first anchor is $a_j^D$ itself. Hence all
edges $e_{1j},\ldots,e_{sj}$ currently project to parallel edges
$$
a_j^B a_j^D.
 \tag{3}
$$
The hub is not touched by these splits.

Next split one $w_i$ into $w_i^B,w_i^D$, leaving $hw_i$ at
$w_i^B$ and all $e_{ij}$ at $w_i^D$. Its current endpoint is
touched, so the projected graph now replaces, simultaneously,
$$
a_j^B a_j^D
                    \quad\hbox{by}\quad
             w_i^D a_j^D
                \qquad (j=1,\ldots,s)
 \tag{4}
$$
for the central IDs $e_{ij}$.

Before the last such operation, each $a_j^B$ still has other
projected incidences from rows not yet split. Operation (4)
extracts proper subsets of incidences from $s$ different old
vertices and identifies those extracted endpoints with ONE new
physical anchor $w_i^D$. It is not one native vertex split.

The example uses actual broken initial paths. It is not caused
merely by deciding to repair a still-valid path after an unrelated
touch.

## 3. Why ordinary splits do not implement this operation

Under insertions of vertices and ordinary vertex splits, with no
edge deletion/reinsertion or vertex identification, every current
vertex has a unique ancestral vertex. Distinct old ancestry classes
never combine. This is an immediate induction: a new isolated vertex
starts a new class, and splitting partitions one existing class.

The endpoint in (4) combines incidences whose old endpoint vertices
were the distinct $a_j^B$. Therefore preserving all projected edge
IDs and all physical anchor identities requires at least one
operation outside that insertion/split-only interface:

* endpoint relocation through edge deletion and reinsertion;
* identification of the $s$ extracted endpoint groups; or
* distinct auxiliary copies that are identified only after the
  auxiliary sparsifier.

The third option is legitimate in principle, but requires a size
bound. In this example, retaining immutable old-origin identities
creates one $w_i^D$-copy for each old $a_j^B$-origin. After all
$s$ row splits there can be $\Theta(s^2)$ such origin slots,
despite only $O(s)$ actual touched anchors and initial base size
$O(s)$. The slots arise even though every original route has
length two. Thus the total number of initial route occurrences is
not an adequate substitute for the small-child vertex bound.

This count applies to that straightforward immutable-origin
adapter. It is not a proof that every auxiliary representation
needs so many slots.

## 4. Central memberships and projected endpoints are different

The current child graph contains selected CENTRAL native IDs,
with their native physical endpoints. It does not contain every
current projected endpoint pair. Thus all movements in (4) may be
processed as local projected-graph work while the same selected
central IDs remain selected. A large number of anchor changes does
not by itself imply equally many child edge changes.

The example intentionally does not prove a large selected-membership
lower bound. Its final projected graph contains a complete
bipartite pattern, which has easy sparse spanning supports. Suitable
membership choices can add only a few central edges per new row.
Consequently it would be incorrect to infer impossibility from
Section 3.

What is missing is a constructive theorem that maintains a sparse
selected CENTRAL-ID set under these multiple-origin refinements,
with both:

1. short explicit current projected routes and low ambient
   occurrence congestion; and
2. selected-ID births and deaths bounded by a subpolynomial factor
   per actual touched-anchor event, independent of the native
   degree $s$.

Its local work may scan all affected initial-route occurrences,
as long as the total work over the parent period is paid. A
$k$-sized local scan is permitted by the existing numerical
recurrence; a $k$-fold multiplier on propagated child membership
changes is the dangerous term.

## 5. A positive local-work bound and two accounting distinctions

Assume the initial table has length at most $\Lambda$, current
ancestor vertex-occurrence congestion at most $C_0$, and the
current native degree is at most $\Delta$. Dead input demands
are removed from its inverse lists; later edge births get identity
routes. At a current split descendant, the retained initial records
still contribute $O(C_0)$: a fixed old occurrence has at most its
two path-side incidences and any endpoint annotation. Splitting
partitions these incidences rather than manufacturing additional
live sides. Current identity-route records contribute $O(\Delta)$.

Maintain inverse occurrence and endpoint lists on those CURRENT
native identities. One native deletion or split can enumerate
all affected old route IDs through its constantly many touched
vertices and incidences. Deduplicate the IDs, then scan each
affected route's at most $\Lambda$ original positions, with its
current split/deletion annotations, to recover both first anchors.
This deliberately simple implementation costs
$$
O((C_0+\Delta)(\Lambda+1)\mathrm{polylog}m)
 \tag{5}
$$
per native edit, plus that edit's explicit native incidence
transcript. It includes anchor changes that leave the path position
fixed but change its descendant ID. All resulting projected
endpoint replacements can be reported at this cost.

For the proposed parent period, if
$$
C_0\leq k\Gamma,\quad \Delta=O(k),\quad
 \Lambda\leq\Gamma,\quad q_{\rm native}\leq(m/k)\mathrm{poly}(U),
$$
then initialization plus all these anchor updates costs
$$
m\Gamma^{O(1)}\mathrm{poly}(U).
 \tag{6}
$$
No monotone-position proof is needed for this conservative bound.
It is local projected-graph work. A theorem about its selected
memberships is still needed before feeding changes to the recursive
child. In particular, (6) assumes the stated native edit bound; it
does not establish a new degree-feedback termination argument.

### Monotone positions versus native descendant identities

With no native splits, a newly marked vertex can only move the first
anchor toward the original endpoint along a fixed initial route.
Each route has at most $\Lambda+1$ positions. Native splits add a
distinct issue: the anchor's position can stay fixed while its
current descendant identity changes. A bound on position changes
does not count those updates. They must be charged to a concrete
split-incidence implementation, or maintained implicitly with an
explicit query and output transcript.

The example already exhibits many position changes with
$\Lambda=2$, but its total explicit route inventory is
$\Theta(s^2)$, so linear work in that inventory remains feasible.
It is the selected-membership/auxiliary-size requirement that
needs an additional proof.

### Total work is not prefix recourse

A bound of $O(m\Lambda\mathrm{polylog}m)$ on all initial
anchor records over a period is compatible with amortized local
work $k\Lambda\mathrm{polylog}m$ when that period has
$\Theta(m/k)$ parent updates. It does not imply the needed
selected-child prefix bound
$$
O(mR/k+Rq)
$$
after $q$ actual updates. That prefix, including its single
initial credit, remains a separate interface obligation.

The global-initial-route idea therefore remains a meaningful
candidate. The exact new operation is multiple-origin incidence
extraction with physical identification, not ordinary insertion
and vertex splitting.

The follow-up [ambient bulk-deactivation example](../mechanism-boundaries/ambient-bulk-deactivation-obstruction.md)
also isolates a separate support problem: simply capping normalized
ambient loads and deactivating every image using a saturated resource
can retain quadratically many selected IDs, even on a static input.
That counterexample concerns the generic fixed-image rule; it is not
asserted to be an actual first-touched matching trajectory.
