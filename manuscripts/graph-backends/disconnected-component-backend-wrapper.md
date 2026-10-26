# A disconnected-component wrapper for the distance cycle backend

**Research construction, 24 October 2026.** This note repairs a literal
scope problem in the distance route: a spanning forest of a graph with
many small connected components cannot have only $O(m/k)$ components.
It also makes the pivot interface and resident isolated vertices
explicit. The construction is for arbitrary undirected multigraphs.

This is a wrapper around the named constructive low-stretch and
spanner algorithms. Its spanner conventions are stated in Section 4;
a black box that only returns an arbitrary sparse subgraph, with no
native-split or constructive initialization interface, is not sufficient.

The relevant primary sources are:

- [CKL+22, arXiv:2203.00671v2](https://arxiv.org/pdf/2203.00671):
  Definition 6.4, Lemma 6.5, and Appendix B.3, especially equation (56).
- [KMPG, arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402v1):
  Theorem 3.1, Lemma 3.5, Theorem 3.7, and Algorithms 2--4.
- [vdBCK+23, arXiv:2309.16629v1](https://arxiv.org/pdf/2309.16629):
  the constructive static sparsifier and its dynamic reduction in
  Section 8, and the empty self-loop embedding convention in
  Appendix A.3.
- [DO26, arXiv:2609.23852v1](https://arxiv.org/pdf/2609.23852v1):
  the local cycle alternatives and Lemma 4.1.

The root-pool lift, exact gauges, integral lengths, and numerical
callbacks remain those of
[the distance integration](distance-backend-general-matching-integration.md)
and [the lifetime interface](numerical-backend-lifetime-and-loops.md).

## 1. Size, component types, and the actual difficulty

At the start of a local instance let
$$
n_0=|V(G_0)|,\qquad e_0=|E(G_0)|,\qquad m_0=n_0+e_0.
$$
Every actual resident input vertex is included, even if it is isolated.
The graph has degree at most a declared $\Delta\geq1$, and $k\geq2$.

Partition the **initial** graph into connected components. Call a
component small if it has fewer than $k$ edges, and large otherwise.
An isolated vertex is small. Every nontrivial small component has at
most $k$ vertices; every large component pays at least $k$ initial
edges. Consequently the number of large components is at most
$e_0/k$. This partition is fixed for this instance: it is not
recomputed after each graph update.

The correct componentwise low-stretch initialization has
$$
O(m_0\,\mathrm{polylog}M/k)
       +\#\{\text{initial small components}\}
 \tag{1}
$$
roots in each forest. The second term cannot be discarded from the
parent's storage or numerical occurrence accounting. Instead, initially
small components contribute only core loops and isolated roots to the
recursive graph. Those loops are served locally and the isolated roots
are not yet inserted as child input vertices.

This is a recursive-input construction, not a claim that all internal
root records have disappeared.

## 2. A whole-tree initialization for each small component

Fix one actual vertex $r_C$ in each small initial component $C$.
Every forest in the source's logarithmic family uses this same root
within $C$, although its weighted low-stretch spanning tree may differ.

For each weighted low-stretch call, compute its tree $T_C$ and
auxiliary ancestor hierarchy $T_{H,C}$ as in CKL+22. Use the root set
$\{r_C\}$, so the initial maintained forest is the whole tree $T_C$.
This common-root choice is supported by the constructive primitive:
the proof of CKL+22 Lemma B.9 starts with a tree having an arbitrarily
chosen root, preserves that root in $T_{H,C}$, and forces the
minimum-depth node to be the root of each heavy-chain search tree.
Thus the singleton $\{r_C\}$ really is ancestor-closed in every
weighted call; it does not hide a separate logarithmic set of roots
inside each small component.
For an edgeless component this is its trivial one-vertex tree; no
replica or weight-normalization formula is applied.
No component-volume cut is necessary: at every later time a surviving
forest component remains a subset of $C$, has at most $k$ vertices,
and is incident to at most $k\Delta$ current graph edges.

Here is the precise stability argument. The fixed stretch labels of
CKL+22 equation (56) have the form
$$
\widetilde{\mathrm{str}}(e)
    =2\sum_{j=0}^{h}
       \mathrm{str}_{F_T(B_j,\pi)}(e),
       \qquad h=O(\log^2|C|).
 \tag{2}
$$
Their weighted-sum bound is proved before choosing the initial
ancestor-closed root set. The singleton hierarchy root is
ancestor-closed. On an inserted or deleted edge $uv$, add the
hierarchy ancestors of $u$ and $v$ to the root set, as in the
source proof. Required extra forest cuts use the same closure rule.

The validity proof at the end of CKL+22 Appendix B.3 applies unchanged.
If $u,v$ remain in the same forest tree, their forest path is their
initial tree path and its stretch is bounded by (2). Otherwise each
current endpoint root agrees with its root in one of the hierarchy-level
forests used in (2). The two current root-leg lengths are therefore
bounded by the corresponding two summands. In either case the fixed
label dominates the current stretch.

Thus the whole-tree initialization preserves the source's fixed-label
and weighted-stretch guarantees, with the constant enlargements in
Section 2.1 below. Each endpoint promotion introduces
only a polylogarithmic number of roots/cuts. A new graph edge joins
vertices made roots before insertion and has stretch label one.
Forest edges are never inserted, so initial small trees never merge
even when the input graph's connected components merge.

There is also no hidden high-stretch initialization cut in a small
component. Use its **own** edge count $e_C$ in the weighted replica
normalization: with positive weights of total $W_C$, create
$\lceil e_C v_e/W_C\rceil$ copies of edge $e$. There are at most
$2e_C<2k$ replica edges, and each physical edge has at least one
copy. CKL+22 equation (57) bounds the total unweighted fixed stretch
over these replicas by
$O(e_C\gamma_{\rm LSST}\log^2(|C|+2))$. Every individual label
is therefore already $O(k\gamma_{\rm LSST}\log^2 M)$, below a
compatible choice of the source's $O(k\gamma_{\rm LSST}\log^4 M)$
high-stretch cutoff. That cutoff introduces no additional small
roots. Using a global edge count in the replica normalization would
not give this immediate conclusion.

Large initial components use the ordinary source initialization.
Their initial root and cut counts sum to
$O(m_0\mathrm{polylog}M/k)$, because their number is also
$O(m_0/k)$. Newly born input vertices start as singleton forest trees.

The weighted family construction may use one common global parameter
and sum componentwise bounds. For zero-weight edges, the usual
nonnegative-weight extension can be made explicit: if the total weight
in a component is $W>0$, add $W/e_C$ to every edge weight in that
component and absorb the resulting factor two in the average-stretch
constant. A component with $W=0$ has no path-preservation obligation
for that call; use uniform positive weights to choose its low-stretch
tree and fixed labels. This does not change the number or form of
forest updates.

There is no large rational denominator in this modification. In our
integer-length realization the original weights are integers
$w_e=\mathrm{econg}(\widetilde{\mathcal P}_i,e)\ell_e$.
Here the count is the total number of **edge occurrences** in the
concatenated inventory walks, including repetitions. A concatenation
of shortest-path legs need not be simple; counting only whether a
walk contains an edge would not give the exact weighted-sum identity
used by path halving. Occurrence counting is obtained while explicitly
constructing the same inventory and changes none of its size bounds.
Use the equivalent positive integer weights
$v_e=e_Cw_e+W$, whose total is $2e_CW$, and compute the
replica counts by integer ceiling division. All these integers have
$O(\log e_C+\log W)$ bits. This is only a common rescaling of
$w_e+W/e_C$, so both the weighted-stretch factor and the bound of
$2e_C$ replica edges are unchanged.

### 2.1. A finite-bit congestion ordering and the effective stretch constant

Integer replica weights alone do not settle every arithmetic operation
in CKL+22 Appendix B.3. Its Definition B.5 orders tree edges by
$$
c_f=\sum_{e:\,f\in T[e]}r_e/\ell_e ,
$$
where $r_e$ is the replica multiplicity. Arbitrary integer lengths
can give these exact rational sums a large common denominator. We
replace only this ordering calculation; the input metric and all
tree-path lengths remain their original positive integers.

Put $B=\lceil\log_2 L_{\max}\rceil$ and
$$
a_e=2^{-\lceil\log_2\ell_e\rceil},\qquad
 \widehat c_f=\sum_{e:\,f\in T[e]}r_ea_e .
 \tag{2a}
$$
Then $c_f/2\leq\widehat c_f\leq c_f$. Sort the tree edges by
$\widehat c_f$, resolving ties by their fixed IDs, and keep this
total order $\pi$ throughout the forest lifetime. If $f$ is the
first edge of an adjacent-root path in this order, every edge $g$
of that path satisfies $c_f\leq2c_g$.

This gives the following direct variant of CKL+22 Lemma B.6:
$$
\sum_{e\in E(G_v)}\mathrm{str}_{F_T(R,\pi),\ell}(e)
 \leq3\sum_{e\in E(G_v)}\mathrm{str}_{T,\ell}(e).
 \tag{2b}
$$
Indeed, the source's equation (55) bounds the left side by the
tree-stretch sum plus $\sum_{f\in E_{\rm cut}}L_f c_f$, where
$L_f$ is the length of the adjacent-root path containing its
chosen cut edge $f$. Those root-to-root paths are edge-disjoint
because $R$ is branch-free. On each such path $c_f\leq2c_g$;
hence the extra sum is at most
$2\sum_{g\in E(T)}\ell_gc_g$, which is at most twice the
tree-stretch sum. This is the only change to the average-stretch
proof: its constant three replaces the source's constant two.

The fixed-label domination proof does not need an exact congestion
order. Lemma B.9, items 3 and 4, applies to **any fixed total order**
$\pi$. Thus the same ancestor hierarchy, equation (56), and the
last paragraph of the source's Lemma 6.5 proof still dominate every
later forest/root-leg stretch. The forest remains decremental.
Equation (57)'s total unweighted fixed-label bound increases by at
most $3/2$. Increase the absolute constant in the high-stretch
cutoff by the same factor. Its Markov bound and subsequent ancestor
closure still introduce $O(m/k)$ roots in a large component.
For a small component the replica graph has at most $2e_C<2k$
edges, so every individual label is still
$O(k\gamma_{\rm LSST}\log^2 M)$; the compatible enlarged
$O(k\gamma_{\rm LSST}\log^4 M)$ cutoff introduces no roots.

For explicit downstream constants, let $\gamma_{\rm src}$ be a
common upper bound for the source's **weighted fixed-label** average
stretch, including its hierarchy logarithms. The dyadic ordering is
covered conservatively by
$\gamma_{\rm ord}=2\gamma_{\rm src}$. Positive-weight smoothing
then gives
$$
\sum_e w_e\widetilde{\mathrm{str}}(e)
 \leq \gamma_{\rm eff}\sum_e w_e,\qquad
 \gamma_{\rm eff}=2\gamma_{\rm ord}=4\gamma_{\rm src}.
 \tag{2c}
$$
The KMPG future-path halving test must consequently use
$2\gamma_{\rm eff}$, not the original $2\gamma_{\rm src}$.
Equivalently, after naming the dyadic-order bound as the source
envelope, smoothing doubles that envelope and the test doubles it
once more. Markov's inequality now discards at least half of the
remaining total path-length weight in every round. Every later
path-preservation or distance-comparison constant uses this same
enlarged envelope. This changes neither its polylogarithmic order
nor any parameter exponent.

The ordering can be constructed with short integers. Multiply (2a)
by $2^B$: each summand becomes
$r_e2^{B-\lceil\log_2\ell_e\rceil}$, and the total over all
replicas has $O(\log e_C+\log L_{\max})$ bits. One LCA query
per physical edge, equal additions at its two endpoints and subtraction
of twice that amount at its LCA,
followed by a tree postorder sum, compute all tree-edge loads.
Sorting them takes $O(e_C\log(e_C+2))$ comparisons of these
integers. Formula (56) is subsequently stored as
$\ell_e\widetilde{\mathrm{str}}(e) =2\sum_j(\ell_e+P_j)$, using only integer path lengths.
No least common multiple or exact reciprocal sum is formed. This
closes the normalization and Appendix B.3 ordering arithmetic;
the deterministic weighted low-stretch-tree construction remains
the named source primitive.

For the finite-bit original-edge tree interface in
[the AN adapter](an-weighted-finite-bit-adapter.md), the complete
integration is given in
[the polynomial-bit stable-forest lemma](polynomial-bit-stretch-stable-forest-integration.md).
Its fixed-polynomial dependence on the length bit count changes
only the effective stretch and fixed polynomial master factors.
The exported label remains the integer path sum above: its
$O(\log^2 n)$ summands are the hierarchy levels of ONE tree,
not the number of weighted halving calls. Temporary petal
coordinates are not exported as core lengths.

## 3. Logical pivots, balls, and direct terminal edges

For every small component set its initial logical center set to
exactly $\{r_C\}$, with the root chosen in Section 2. Run the source
center construction on each large component, adding one actual local
pivot if it returns no center there. In large components these extra
roots and their ancestor closures cost only
$O(m_0\mathrm{polylog}M/k)$ in total.

Every vertex now has a genuine closest logical pivot. No distance to
a nonexistent pivot is queried. The logical pivot set may have
$$
O(m_0\mathrm{polylog}M/k)
       +\#\{\text{initial small components}\}
 \tag{3}
$$
vertices initially. We do not claim the original $n_0/k$ bound
for this enlarged set.

An isolated input vertex born later immediately becomes its own
logical pivot and its own root in every forest. It does not acquire
a recursive child slot until a retained nonloop edge actually uses
that physical root.

Adding centers only shrinks strict balls and inverse clusters. The
source's local ball/cluster bounds therefore remain valid. A small
component's balls contain at most $k$ vertices in any event.
All logical pivots are roots in every maintained forest.

Before an input edge update, promote its endpoints into the logical
pivot set and into the forest root sets. The nearest-pivot distance
cannot increase: if an old shortest pivot path is broken, the first
newly promoted endpoint on that path is at least as close as the old
pivot. A strict-ball path contains no pivot. A shortest path to a pivot
cannot traverse a newly inserted edge, because its first endpoint is
already a pivot and all edge lengths are positive. Hence all finite
shortest local-ball paths and closest-pivot legs remain inside initial
components and use surviving initial edges. The generating middle edge
of a new ASZ path may cross two initial components; both its endpoints
are already pivots, so this case is exactly its label-one singleton
path. The source precomputation and monotonicity argument still applies.

There is a separate strict-ball convention to make explicit. At a
terminal $v\in A$, the strict ball $B(v,A)$ is empty. In the
generating-path inventory use
$$
B^+(v,A)=B(v,A)\cup\{v\}.
 \tag{4}
$$
This adds at most one entry to a ball or inverse-cluster count.
In particular it includes each direct terminal-to-terminal edge.
Include all initial singleton edge paths in the future-path family
before its weighted-halving construction. This adds only
$O(e_0)$ paths. A later terminal-to-terminal OLD edge has actual
stretch one in every forest, but its fixed stored estimate need not
be one. The singleton-path preservation guarantee supplies a forest
whose stored estimate is at most the same $\alpha$ used for the
other inventory paths. A newly inserted edge, by contrast, has
stored estimate one in every forest because both endpoints were
promoted before its birth.

Store a singleton-path record for each direct edge and update its
terminal status when an endpoint is promoted. Enumerating the
incident edges of a promoted input vertex costs $O(\Delta)$
local work. A fresh input edge has two terminal endpoints
immediately. These records do not synthesize extra core or child
edge lifetimes: the edge is already present in every applicable
source core graph. Initial inventory work is linear up to source
factors, and local work per endpoint promotion is absorbed in the
existing polynomial in $k,\Delta$.

The local-cycle versus core-cycle comparison uses this enlarged
inventory. A cycle contained in a small neighborhood is still a
local candidate. When projected into a small initial whole-tree
component, its core contribution consists of real self-loops, which
are covered by the fundamental-cycle candidates below. No center-free
component or direct terminal edge is omitted from the comparison.

## 4. Constructive spanner conventions

The following conventions of the constructive spanner are used here.

**Positive metric calls and external alias gluing.**
Run the positive-length spanner construction on each core, using its
positive length buckets. The zero alias connections are separate
union/gluing records; they are not zero-length inputs to a primitive
whose interface requires positive lengths. Retain the gluing of
aliases of the same physical root explicitly.

If the per-core stretch is $\rho$, each positive core edge $e$
has a same-core replacement path of length at most $\rho\ell_e$.
Replacing the positive edges of any core-sum walk, while keeping its
zero gluing steps, proves the same $\rho$ upper bound for that
walk. This edgewise bound is sufficient for the cycle decomposition
and its raw length charge. It does not assert that this particular
same-core route approximates a possibly shorter cross-core distance
between the edge's endpoints.

Apply the KMPG degree-feedback routine to the retained positive
edges in each core, exactly the core intersections used by its
Algorithms 2--4. The feedback proof uses the per-core sparsity
and native-split edit bounds; zero gluing edges are not part of that
degree test. There are $\lambda=\mathrm{polylog}M$ cores.
Summing their work and recourse and then identifying equal physical
roots multiplies the degree and edit bounds only by this source
factor, absorbed in $R$. A new root alias changes only
$\mathrm{polylog}M$ external gluing records. Frozen-gauge
values on the gluing links are corrected to zero before their
contraction, as in the integration note.

Distinguish selected-edge recourse from demand-route congestion.
An unsparsified core vertex can have $O(k\Delta)$ incident demand
edges. Their embeddings may all meet that vertex, so we do not use
a $k$-free bound on this congestion. Empty loop embeddings also
retain their base vertex for touched-incidence bookkeeping; their
contribution is bounded by the full registered core degree.
The corresponding $k\,\mathrm{poly}(\Delta,A)$ route and
incidence work is part of the local envelope $W$. The bounds
required without a $k$ factor are the selected spanner's controlled
degree and its emitted child-edit count. Physical flat-forest
multiplicity is proved from the direct pools, independently of
demand-route congestion.

**Positive loop inputs remain registered, with empty embeddings.**
A positive self-loop is never selected as a distance-spanner edge.
Its distance embedding is the empty path. All input loop identities
and incidences remain registered in the native core-graph splitter.

The exact primary convention appears immediately before Definition A.1
in vdBCK+23 Appendix A.3: a core self-loop has an empty path embedding.
Its input identity is still retained. The empty **edge list** has its
base vertex $v$; that vertex and the original endpoint incidences
remain indexed for the touched-vertex and native-split operations.

For static sparsification, remove positive loops from the metric
subproblem and give their registered IDs the empty embedding. Run the
static sparsifier on the remaining edges. This preserves every
distance, embedding-length, and congestion guarantee. It also prevents
a directly retained base set from containing a positive loop.

This convention is compatible with the actual dynamic reduction, not
just with a static metric. CKL+22 Section 5.1 maintains touched vertex
sets $S_j$; a split touches both resulting vertices. Its repair
graph $J$ is formed on $S_j$, and an affected input edge is
projected onto those touched vertices. An old loop that becomes a
nonloop is included because its endpoint was split, even though its
old path edge list was empty. For a single split of one vertex,
all such newly crossing loop IDs are projected between the two
touched split vertices. The routine may scan their incidences, but
sparsifies a repair graph whose vertex count depends on the touched
set, not on the number of crossing IDs.

vdBCK+23 Theorem 8.1 supplies the deterministic static repair, with
output size proportional to $|V(J)|$ times the declared source
factors. The paragraph introducing its Theorem 8.2 explicitly applies
the CKL+22 Section 5.1 reduction. Thus one native split may require
$O(k\Delta)$ local incidence work without generating that many
selected output edges. In KMPG's variant the corresponding split
is forwarded to the selected spanner; its later endpoint emulation
uses the selected graph's controlled degree.

We do not replace a native split by $k$ synthetic input-edge
insertions. Merely post-filtering an arbitrary black-box spanner
that had retained the old loops would not prove this bound.

Looplessness persists under the actual update sequence. Forests only
lose edges, so an existing nonloop core edge cannot become a loop.
Every newly inserted nonloop parent edge has distinct root endpoints
and is nonloop in every core. Genuine physical input loops use the
separate loop wrapper. An old core loop may become nonloop after a
native split, but it was never a selected spanner loop beforehand.
All static repairs use the same empty-loop convention. Therefore
the selected spanner does not accumulate positive loops between
initializations.

**Initialization respects initial connected blocks.**
There is a precise initialization interface in that same reduction.
CKL+22 Section 5.1 initializes only $H_0,\Pi_0$ by one static
sparsification; all $H_j,\Pi_j$ with $j>0$ and all touched sets
start empty. For each initial block $C$, use the deterministic
static sparsifier to obtain $H_{0,C},\Pi_{0,C}$, with common
global upper bounds on its approximation parameters. Set
$$
H_0=\bigcup_C H_{0,C},\qquad
              \Pi_0=\bigcup_C\Pi_{0,C}.
$$
All paths remain within their initial blocks. The static size and
work bounds sum; vertex congestion and stretch take their maxima
over the disjoint blocks. The full static initialization contract
therefore holds, with the additional per-block bound
$$
|E(H_{0,C})|=\widetilde O(|V(C)|\gamma_\ell).
$$

After initialization run **one** global updater. Its data are
$H_j,\Pi_j,S_j$, not independently running dynamic instances that
would later need merging. CKL+22 Lemma 5.9 bounds initial sparsity
using only the $H_0$ static guarantee, and bounds each later repair
by the size of the touched set $S_j$. Its proof does not require
one monolithic initial sparsifier call or recomputation of initial
connected components. Replacing that one call by the union above
therefore leaves the native-split recourse proof unchanged. Weighted
length buckets use the same convention separately in each bucket.

A block containing only aliases of one physical root has only zero
alias gluing links and positive loops. Keep its necessary external
zero connections and empty loop embeddings; it has no selected
positive nonloop edge in any positive-metric spanner call.
The local degree-control routine counts retained edges of the core,
not zero alias links. It therefore makes no extra initial forest cuts
in an untouched small whole-tree component.

The initialization sparsity argument for the large blocks consequently
uses only their own $O(m_0\mathrm{polylog}M/k)$ core roots.
An arbitrarily large collection of isolated small blocks cannot
subsidize extra selected edges or extra initial degree-control cuts
elsewhere.

These are constructive normalization requirements, rather than
consequences of the sentence that some sparse spanner exists.
They preserve all input identities needed by later splits and all
source embedding certificates. The source algorithms and their
native-split recourse remain named dependencies.

## 5. Local loops and the resident child graph

Maintain the source's local fundamental-cycle candidates, including
every real core loop, whether or not it is retained by a distance
spanner. For a parent edge $e=(u,v)$ whose endpoints lie in one
forest tree, its candidate is the simple cycle
$$
e+F[v,u].
 \tag{5}
$$
Use its actual signed gradient and literal path length. Common
root legs are canceled within this one forest before presenting
the certificate. The fixed stretch length dominates (5).
A real physical loop is its one-edge candidate.

Initially, every positive core edge of a small whole-tree component
is a loop. Thus no cycle information is lost when its root has no
recursive nonloop incidence. Subsequent root changes and edge updates
refresh the affected local candidates using the source's already
charged local work. One may also compute an exact cycle-ratio answer
on an initial small component in polynomial-in-$k$ local time,
but this is not needed for recursive activation.

Apply the frozen retained-edge gauge correction, contract the justified
zero alias connections, and classify every retained positive edge by
its **current physical root endpoints**.

- A nonloop edge is inserted into the recursive child with its stable
  ID and provenance.
- A real loop is served by its local closed-walk lift and is not
  inserted into the recursive nonloop graph.
- Zero alias links are handled by the justified contraction and are
  not positive child edges.

Insert a physical root as an actual child vertex only when it first
becomes an endpoint of a retained positive nonloop edge. Use a
dictionary from current physical-root identity to its child slot.
Once inserted, **keep that actual child slot until the parent
instance is rebuilt**, even if all its child edges are later deleted.
It is then a resident isolated input vertex, not private metadata.
This rule needs no DeleteVertex operation.

A root never inserted into the child has only a private activation
record, together with its parent forest/root data. This record is not
a child input vertex. On the first nonloop edge insertion, emit at
most two actual isolated-vertex insertions before the edge insertion.
A loop/nonloop transition of a retained edge is an exposed edge
retirement/replacement, not a silent endpoint rewrite.

## 6. Quantitative child size and update count

Let $R\geq1$ be the conservative source factor bounding retained
edge/endpoint changes and degree, including the logarithmic forest
family, gauge corrections, and zero-alias quotient bookkeeping.
Use the explicit degree/recourse caps in the integration note; their
slack absorbs fixed constants below.

At initialization, positive nonloop retained edges occur only in
the large-component portion. Its source construction has
$$
E_{\rm child}(0)+V_{\rm child}(0)
                   =O(m_0R/k).
 \tag{6}
$$
There are no actual child vertices for the untouched small-root
blocks.

Suppose $t$ parent edits have occurred. The source supplies at most
$O(Rt)$ emitted retained-edge and endpoint edits in that prefix.
The filter forwards at most constantly many edge edits per such
record. Every new actual child slot is charged to the first nonloop
edge insertion that uses it, and costs one isolated-vertex insertion.
Therefore
$$
\begin{aligned}
 \#\text{child edits through }t&=O(Rt),\\
 |V_{\rm child}^{\rm resident}(t)|+|E_{\rm child}(t)|
               &=O(m_0R/k+Rt).
 \end{aligned}
 \tag{7}
$$
The first line excludes the separately charged initialization.
The second includes **all** resident isolated child slots.

No scan or activation of all vertices of a small component is
performed when it first interacts with another component. Its
core split may inspect $O(k\Delta)$ physical incidences locally,
as allowed by the source primitive, but only the source's bounded
retained-edge transcript reaches the child.

Use the period
$$
Q=\left\lfloor {m_0\over4k\Delta}\right\rfloor
 \tag{8}
$$
when $m_0>4k\Delta$, and use the explicit terminal cycle solver
otherwise. Since $m_0\leq(1+\Delta/2)n_0$, (8) is at most the
source horizon $n_0/k$. By (7), throughout the period the child
size is $O(m_0R/k)$, including retained isolates.

At each recursive initialization and restart, define its local
$m_i=n_i+e_i$ using **all currently resident input slots and
edges**. Ordinary input updates can create only constantly many
new slots per elementary update, so the initial capacity with a
fixed safety factor bounds the period. A burst from the parent is
processed as its explicit sequence of child edits; a child may
restart within that sequence without an intervening numerical query.

Actual input slots are never excluded merely because they are
isolated. Private tombstones or activation records that were never
inserted may be excluded from $n_i$, while their processing is
charged to parent initialization or explicit births. Complete parent
rebuilds discard the old child instance and create a new one; this
is the already charged restart operation, not an unsupported vertex
deletion API.

## 7. Root pools and numerical counters

The parent's direct-sum trees $T_v$ exist for its actual forest
roots, including roots that have no child slot. Root-only trees,
private unused index layers, and dormant assigned copies are all
included in the physical occurrence accounting.

With a common pool capacity $C$, a physical parent vertex occurs
in at most one tree of each source forest and hence in at most
$O(\lambda C)$ exposed pool copies. There is no factor equal to
the number of small components. Late capacity doubling copies the
current entire forest family; its geometric sum is charged to the
instance initialization allowance.

The addition or release of a child occurrence changes its pool
assignment. It does not erase a surviving internal pool edge.
Dormant real edges stay exposed, stay on their physical coordinate
lists, and keep both their signed increments and their absolute
motion counters. A complete instance retirement transfers both
quantities before parent path or endpoint metadata is invalidated.
No path update, outer query, or coordinate refresh is serviced
during a partial retirement/rebuild transaction.

Thus keeping isolated child slots does not hide physical history,
and omitting a never-inserted child root does not suppress real
motion in the parent's separately exposed local forests or pools.

The fixed-slot matching client can retain all of its input vertex slots
until the whole instance is discarded. If a more general caller
explicitly retires an isolated parent vertex lifetime, handle that
case without requiring a child DeleteVertex operation. Since
$F_i\subseteq G$, each $F_i$ component containing that parent
vertex is now a singleton. All real incident records have already
retired and transferred both counters. Suppress the remaining
$O(\lambda C)$ exported root-only/null records, while keeping the
actual isolated child slot and a slot-to-retired-parent tombstone
until child disposal. Test that status before dereferencing physical
metadata. A query wholly in that isolated null fiber is omitted;
an active path cannot enter and leave it because it has no nonnull
input incidence. Charge this work to the explicit parent-lifetime
retirement. It adds no factor $k$, and prevents historical parent
lifetimes with the same next-level physical image from accumulating
exported occurrences.

## 8. Effect on the recursive bound and remaining imports

The wrapper adds $m_0\mathrm{poly}(k,\Delta)$ local
initialization work and $\mathrm{poly}(k,\Delta)$ local
update work within the existing envelope $W$. Its child terms
remain
$$
I_{\rm child}=O(m_0R\,W/k),\qquad
       R\,T_{\rm child}.
 \tag{9}
$$
In particular it does **not** replace $R\,T_{\rm child}$ by
$kR\,T_{\rm child}$.

The fixed-depth degree, recourse, and pool recurrences are unchanged
after absorbing constants and logarithmic factors into their
declared caps. The exact source statements concerning initial
$O(m/k)$ roots and $|A|\leq n/k$ are used only on the large
component portion; equations (1) and (3) state the full parent
bounds. Equations (6)--(7), rather than an impossible total-root
claim, provide recursive shrink.

The remaining imported fast-time facts are the constructive weighted
low-stretch routine, the path-based dynamic spanner with native
splits and the conventions in Section 4, and the local maintenance
bounds already listed in the distance integration. This note does
not claim that a final matching verifier can replace any of those
time guarantees.
