# Routing from covers with arbitrary original length range

This lemma supplies the analytical routing step for
[the growing-depth backend](growing_depth_aspect_exploration.md).
It uses the hierarchical routing graph topology of
[Chen et al., arXiv:2311.18295v1, Definitions 4.2–4.3](https://arxiv.org/abs/2311.18295v1),
but proves the routing estimate directly. The argument accommodates
disconnected graphs and clusters that already contain a whole
connected component. Its distributions are used only in the proof;
the dynamic algorithm does not compute them.

## 1. Cover hypotheses and scale separation

Let \(G\) have positive edge lengths at least one. Write \(d_G\) for
its shortest-path metric, allowing infinite distance between distinct
connected components. Let \(\Gamma\ge3\), \(\rho\ge8\Gamma^2\),
\(D_i=\rho^i\), and \(h\ge2\). At each level
\(1\le i\le h\), suppose a collection of clusters \(\mathcal C_i\)
has these properties:

1. Each vertex lies in at most \(\Gamma\) clusters.
2. Every ball \(B_G(v,D_i/\Gamma)\) is contained in some cluster.
3. Each cluster has diameter at most \(\Gamma D_i\).
4. Each cluster lies inside one connected component and has a chosen
   root belonging to the cluster.

Repeated clusters can be treated as distinct records; the first
condition counts their multiplicities. Suppose the final level has,
for each connected component \(A\), a designated cluster containing
all of \(A\). Condition 4 makes its vertex set equal to \(A\).
This is supplied, for example, by the last cover radius in the
growing-depth note.

Cluster labels index the analytical transitions below. If several
clusters choose the same physical root at the same level, their root
labels are identified with the one corresponding vertex of the source
HRG. It includes a directed upward edge from the root of \(C\) at
level \(i-1\) to the root of \(C'\) at level \(i\) whenever
\(C\subseteq C'\); using the full source HRG can only add edges.
Such an edge has length \(\Gamma D_i\). Different labelled transitions
may use the same actual abstract edge; summing them can only decrease
the weighted absolute-flow norm. No maintained vertex is required for
each cluster label. Level zero consists of the singletons \(\{v\}\),
with their actual vertices as roots.

For the source HRG, \(C\subseteq C'\) guarantees that the root of
\(C\) has an occurrence in the marked tree representing \(C'\).
The upward edge is therefore realized by its two linking edges and
the marked-tree path between them. Its literal length is at most
\(3\Gamma D_i\), and its physical projection joins the correct
root images.

## 2. Finite weights and their Lipschitz bound

For \(1\le i<h\), define
\[
 p_{i,C}(v)=\max\left\{0,
       \min\left\{1,\frac{d_G(v,V\setminus C)}{D_i}\right\}
                           -\frac1{4\Gamma}\right\},
 \qquad W_i(v)=\sum_{C\in\mathcal C_i}p_{i,C}(v).            \tag{1}
\]
The convention is \(\min\{1,\infty\}=1\). If \(C\) contains the
entire component of \(v\), its weight is thus finite. If \(v\notin C\),
its weight is zero. A covering cluster has weight at least
\(3/(4\Gamma)\); hence
\[
             \frac3{4\Gamma}\le W_i(v)\le\Gamma.             \tag{2}
\]
Define the probability vector
\(a_i(v)_C=p_{i,C}(v)/W_i(v)\). Let \(a_0(v)\) be the point mass
on the singleton \(\{v\}\), and let \(a_h(v)\) be the point mass
on its designated whole-component cluster.

Fix vertices \(u,v\) in the same connected component and write
\(\delta=d_G(u,v)\). Each clipped distance in (1) is
\(1/D_i\)-Lipschitz within this component. If the relevant outside
set is unreachable, the clipped distance is identically one on the
component, so the same statement holds. At most \(2\Gamma\)
coordinates are nonzero at either endpoint. Therefore
\[
       \|p_i(u)-p_i(v)\|_1\le\frac{2\Gamma\delta}{D_i}.       \tag{3}
\]
For nonnegative vectors \(p,q\) of positive sums \(P,Q\),
\[
 \left\|\frac pP-\frac qQ\right\|_1
 \le \frac{\|p-q\|_1+|P-Q|}{P}
 \le \frac{2\|p-q\|_1}{P}.
\]
Applying this and (2)–(3) gives
\[
 \boxed{\qquad
 \|a_i(u)-a_i(v)\|_1
       \le\frac{16}{3}\Gamma^2\frac{\delta}{D_i}.
 \qquad}                                                    \tag{4}
\]
The left side is also at most two. At level \(h\), it is zero
because \(u,v\) belong to the same connected component.

## 3. Every supported consecutive pair is available

Suppose \(a_{i-1}(v)_C a_i(v)_{C'}>0\) with \(i<h\). Then
\[
 d_G(v,V\setminus C')>\frac{D_i}{4\Gamma}
       \ge2\Gamma D_{i-1}.                                 \tag{5}
\]
Also \(v\in C\), and every point of \(C\) is within
\(\Gamma D_{i-1}\) of \(v\). Consequently \(C\subseteq C'\).
For \(i=1\), the previous cluster is the singleton \(\{v\}\),
and the containment is immediate. For \(i=h\), the final cluster
is the entire connected component, so containment is again immediate.

Thus independently sampling one cluster from \(a_i(v)\) at each
level gives a distribution on valid upward root-to-root paths. Every
such path starts at \(v\) and ends at the same designated root for
its connected component. The stronger scale separation
\(\rho\ge8\Gamma^2\) explicitly accounts for the factor
\(\Gamma\) in cluster diameter.

## 4. Cost of routing one edge demand

The expected upward flow at transition \(i\) for a unit at \(v\)
is the tensor-product probability vector
\[
                  a_{i-1}(v)\otimes a_i(v).
\]
For probability vectors \(a,b,c,d\),
\[
 \|a\otimes b-c\otimes d\|_1
       \le\|a-c\|_1+\|b-d\|_1.                            \tag{6}
\]
For an input edge \(e=(u,v)\), route its unit incidence demand by
subtracting the upward distribution of \(v\) from that of \(u\).
The common terminal root cancels. For interior transitions, (4)
and (6) bound the absolute edge mass by
\(O(\Gamma^2\delta/D_{i-1})\).

At the bottom transition, the two singleton distributions differ
by at most two. For distinct endpoints, \(\delta\ge1=D_0\),
because all input lengths are at least one; the same bound therefore
holds there. A loop has equal endpoints and zero routed demand.
At the final transition, the last probability vectors are identical,
so only the preceding level contributes.

Multiplying by the transition length \(\Gamma D_i\) gives cost
\(O(\Gamma^3\rho\delta)\) per level. Summing the \(h\) levels
and using \(\delta\le\ell_e\),
\[
       \text{abstract routing length for the edge demand}
            \le O(h\Gamma^3\rho)\,\ell_e.                  \tag{7}
\]
Replacing every abstract edge by its HRG realization costs at most
another factor three, including literal traversal multiplicities.

By linearity and the triangle inequality, the same operator norm
bound holds for any demand decomposed into input-edge flows. Adding
the original edge to its oppositely oriented routed demand yields
the cycle projection estimate
\[
                    1+O(h\Gamma^3\rho).                    \tag{8}
\]
This is within the looser \(O(\kappa\Gamma^6\rho)\) allowance
used by the existing HRG-to-cycle reduction, with \(h=\kappa-1\).

## 5. Interface consequences

The proof uses the cover, diameter and occurrence properties,
the number of levels, and the geometric scale ratio. It does not
require polynomial original edge lengths. The entire original
aspect enters only through the choice of the last radius and of
\(\rho\). No shortest-path query, cluster-distance calculation,
or probability normalization from (1) is part of the maintained
algorithm.

The dynamic HRG still maintains precisely the source forest copies,
marked memberships and linking edges. Clipping the analytical
weights changes none of these records, and the stronger choice of
\(\rho\) changes only the supplied radii and stored labels. Thus
these two repairs add no uncharged recourse or initialization work.
Isolated vertices are valid singleton components; the argument
never routes demand between distinct components.

## 6. A finite connected private graph for each rounded cover

The radius wrapper can invoke the published cover primitive without
using an infinite-length convention for disconnected inputs. Fix one
local cover instance and let \(m\ge2\) be a nominal bound counting
its resident vertex slots and genuine edges, enlarged by a fixed
constant factor for the private graph below. All its vertex slots are
fixed during this instance. Source-factor envelopes are evaluated at
this enlarged size; their fixed constant-factor changes are absorbed
by the declared \(\Gamma\) envelope.

For a requested original radius \(D\), set \(\delta=D/m^4\),
discard genuine edges longer than \(D\), and replace each remaining
genuine length by \(w_e=\lceil\ell_e/\delta\rceil\le m^4\).
Add a permanent path through every fixed vertex slot, using fresh
artificial edge IDs of length
\[
                              H=m^8.
\]
The private graph is connected under every genuine-edge update.
Its degree is at most five when the genuine graph has degree at
most three, so it still satisfies the source's constant-degree
hypothesis. Its size is \(O(m)\), including isolated genuine
vertices, and its lengths lie in \([1,m^8]\). The cover call uses
radius \(m^4\), with the usual factor \(\gamma\le m^3/2\) after
the eventual size threshold.

Maintain the source primitive unchanged on this private graph.
From its exported forest, exclude every edge occurrence whose
source image is one of the artificial path edges. Keep the
remaining occurrence vertices, genuine edges and null edges, and
the marked set. This is an output filter, not a deletion supplied
to the source data structure.

To prove correctness, every source forest edge mapping to an
artificial edge has length at least \(H\). Any path between two
marked vertices in one source tree has length at most
\(\gamma m^4<H\). Such a path therefore contains no excluded
edge. All the marked vertices of a source tree remain in the same
filtered tree, and their diameter bound is preserved. Also a
private-graph ball of radius \(m^4/\gamma<H\) cannot traverse an
artificial edge. Consequently the same covered balls are present
in the genuine rounded graph. The filtered forest is a flat
embedding of that graph; extra unmarked components may simply
remain as dormant records.

Scale genuine exported lengths by \(\delta\), and give retained
null edges length \(\delta\), exactly as in the radius wrapper.
The rounding and positive-null-length proofs are unchanged.
Artificial path edges have never been genuine matching edges or
raw-cycle input edges, and **no artificial occurrence is output
as a real physical traversal**. They carry no numerical flow
counter in the exported structure.

Filtering costs at most constant work per explicitly reported
source record change. It neither duplicates occurrences nor
adds a scan on a genuine update. Initialization and storage are
\(O(m\gamma)\), with the usual logarithmic bookkeeping overhead.
The larger fixed polynomial length exponent eight changes no
subpolynomial source exponent.

### Reserved slots and small inputs

If isolated-vertex births are needed, a local instance can reserve
\(O(m)\) private slots at initialization and end after at most
\(m\) wrapper events. A birth activates one unused slot; a true
retirement suppresses its now entirely null exported fiber only
after every formerly real incident occurrence has completed its
signed and absolute retirement transfers. An unused slot's
occurrences stay private. Since all its genuine incidences are
absent and all artificial occurrences are filtered out, its
remaining forest components are null fibers, disjoint from any
active marked-tree path. Activation or suppression visits only
the \(O(\gamma)\) occurrences of that slot and gives newly
exposed records fresh immutable image lifetimes. The primitive's
own vertex set and permanent path remain fixed; no unsupported
source vertex-insertion or vertex-deletion operation is invoked.
All reserved slots and private occurrences are counted in \(m\)
and its initialization allowance.

A period's reserved capacity can be chosen as a constant multiple
of its initial resident size. A period restart or an ordinary
size-doubling rebuild supplies later capacity, charged to the
intervening local events. The master-size construction uses its
direct cycle solver when the actual local graph is below the
base threshold. It never pads a small root to size \(S\) merely
to initialize this private backbone or its cover routine.
