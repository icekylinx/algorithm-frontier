# A simple-graph interface for degree-proportional token routing

**Separate research interface, 24 October 2026.** This note checks the
graph-model, token-load, conductance, and parameter boundaries of using
[Chang, Huang and Su, arXiv:2405.03908](https://arxiv.org/pdf/2405.03908)
as a static routing primitive. It does **not** infer sequential work
from CONGEST round complexity. The source permits unbounded local
computation, and the required constructive work bounds for its local
cut player and leaf sorting embeddings remain separate obligations.
The existing $`6/7`$ construction does not depend on this proposal.

## 1. A loopless multigraph becomes a simple bounded-degree expander

Let $`G`$ be a loopless undirected multigraph without isolates, with
$`m`$ edge IDs and conductance at least $`\phi>0`$. For each vertex
$`v`$, make one port for each of its $`d_v=\deg_G(v)`$ incidences.
Inside this fiber, place a simple graph of fixed maximum degree
$`D_0`$ and fixed positive edge expansion $`\alpha_0`$.

Such internal graphs follow from the explicit constant-degree
expander construction of
[CGLNPS, arXiv:1910.08025v2, Theorem 2.4](https://arxiv.org/pdf/1910.08025).
Dropping loops and retaining one of each parallel pair loses only
a fixed factor, since the degree bound is fixed. Treat fibers of
size one and two directly. A size-one fiber has no internal edge,
and a size-two fiber has one internal edge; the required inequality
```math
|\partial_{X_v} A|\geq\alpha_0\min\{|A|,d_v-|A|\}
```
still holds with a common fixed $`\alpha_0>0`$.

For every original edge ID $`e=uv`$, join its own port in $`u`$'s
fiber to its own port in $`v`$'s fiber. Distinct parallel original
edges have distinct ports. Consequently the resulting graph
$`G^\diamond`$ is SIMPLE. It has $`2m`$ vertices, $`O(m)`$ edges,
maximum degree at most $`D_0+1`$, and minimum degree at least one.
Keep the original ID on each external edge. Internal edges have
an explicitly typed null projection into the original graph.

### Conductance proof

Consider any port cut $`S`$. Write $`a=|S|`$, $`b=2m-a`$, and let
$`x_v`$ be the number of $`v`$'s ports in $`S`$. Round each fiber
to its majority side and put
```math
I=\{v:x_v\geq d_v/2\},\qquad
 z=\sum_v\min\{x_v,d_v-x_v\}.
```
Ties may be resolved arbitrarily. Internal crossing edges contribute
at least $`\alpha_0z`$. The whole-fiber cut corresponding to $`I`$
has original volume on its two sides within $`z`$ of $`a,b`$.
Thus its original crossing count is at least
$`\phi(\min\{a,b\}-z)`$. Changing from the rounded cut to $`S`$
can change external-edge crossing status at most $`z`$ times,
because every misclassified port has exactly one external edge.
Therefore
```math
|\partial_{G^\diamond}S|
 \geq
 \max\{\alpha_0z,\ \phi\min\{a,b\}-(1+\phi)z\}.
```
If $`z\geq\phi\min\{a,b\}/(2(1+\phi))`$, the first term is
at least a fixed constant times $`\phi\min\{a,b\}`$.
Otherwise the second term is at least
$`\phi\min\{a,b\}/2`$. Since port degrees are at most $`D_0+1`$,
```math
\Phi(G^\diamond)\geq c\phi
```
for an absolute $`c>0`$.

This proves the model reduction directly for parallel edge IDs.
No native multigraph extension of the distributed router is needed.
The actual hosts used in the proposed static sparsifier are
loopless by construction. Real loop demands, when present in an
outer distance problem, retain their empty-route endpoint records
outside this interface.

## 2. Turning degree-proportional load into one-token batches

Suppose the token list has $`M`$ directed source-destination pairs
and satisfies
```math
\#\{\text{tokens starting at }v\}\leq Dd_v,\qquad
 \#\{\text{tokens ending at }v\}\leq Dd_v
```
for an integer $`D\geq1`$. Assign starting tokens cyclically to
the source ports and destination tokens cyclically to the
destination ports, using fixed token-ID order. Each port is now
the source of at most $`D`$ tokens and the destination of at most
$`D`$ tokens. Source and destination port choices are independent.

Form the bipartite token multigraph whose left vertices are source
port copies and whose right vertices are destination port copies.
Its edges are the token IDs and its maximum degree is at most $`D`$.
It can be split deterministically into fewer than $`2D`$ matchings
in $`O(M\log(D+1))`$ work:

1. In each current bipartite graph, add dummy edges to make all
   degrees even, using at most two dummy vertices if necessary.
2. Alternate colors along its Euler tours. Every tour has even
   length because the graph is bipartite.
3. Drop dummy edges and recurse on both colors.

Each retained degree is at most the ceiling of half its old
degree. After $`\lceil\log_2D\rceil`$ levels every color class is a
matching. The total real edge count per level is $`M`$; the
dummy inventory is $`O(M)`$ per level and does not require a scan
of unused ports.

In one color class, every port is the source of at most one token
and the destination of at most one token. Thus it is a literal
load-one instance of CHS Definition 4.1 on the simple
bounded-degree graph $`G^\diamond`$. The router can be
preprocessed once and reused for every batch.
Within one batch, label a token by its unique source port and
use the destination port's local ID. Both labels have
$`O(\log(m+2))`$ bits, as required by CONGEST. A separate
charged lookup table maps these local labels back to the
outer token and edge-lifetime IDs. Large master IDs need
not be transmitted as one local message.

## 3. Exporting actual paths

This paragraph requires an explicit store-and-forward
implementation or an equivalent constructive per-token route
trace. It is not a consequence of an arbitrary communication
algorithm's round bound alone.

If one batch executes in $`Q`$ rounds with a constant number of
token packets per edge per round, its recorded token trajectories
have at most $`Q`$ hops each and edge congestion $`O(Q)`$.
Internal fiber moves project to no original edge; external moves
retain the unique original edge ID. Erasing internal steps and
then closed subwalks gives an original path with at most $`Q`$
edges. Across fewer than $`2D`$ batches, original edge congestion
is $`O(DQ)`$. A coarse original vertex-congestion bound is
$`O(DQd_v)`$, including token endpoints.

All route records are charged to their explicit lengths. The
path projection does not identify different original parallel
edge IDs. If an application subsequently simplifies the path
in a different ambient graph, that is an additional explicit
operation; it must preserve the endpoint annotation and be
charged to the input path-list size.

## 4. The literal dependence on conductance

CHS Property 3.1 gives a hierarchy of depth $`O(1/\epsilon)`$.
Its union of child embeddings has a polynomial dependence on
the input inverse sparsity at the root. At every deeper level,
that dependence is only polylogarithmic in the graph size.
Corollary 3.4 therefore bounds the flattened path quality by
```math
\mathrm{poly}(\psi^{-1})
                         \log^{O(1/\epsilon)}n.
```
It does not multiply $`\psi^{-1}`$ once per hierarchy level.

The query recurrences in Section 6.5.2 explicitly upper-bound
their nonrecursive terms by
```math
L\,g(\psi^{-1},\log^{1/\epsilon}n)
```
for one fixed polynomial $`g`$. The recursive coefficients are
polylogarithmic and have depth $`O(1/\epsilon)`$, giving another
fixed polynomial in the same two quantities. Thus the source's
claimed query envelope has fixed-power dependence on
$`\psi^{-1}`$, not an unmentioned exponent depending on
$`1/\epsilon`$.

On the constant-degree split graph, sparsity and conductance
are within fixed factors. Writing $`p=1/\epsilon`$, and taking
$`\phi^{-1}=2^{O(r\log(U+2))}`$, the intended query/output
envelope is
```math
Q=2^{O((p+r)\log(U+2))}.          \tag{1}
```
This verifies a parameter dependence of the constructive
interface. It does not certify the source's zero-round local
computations as efficient sequential procedures.

## 5. Actual-size clipping of the router parameter

CHS Appendix D simplifies its preprocessing bound under
```math
\epsilon=\Omega\!\left(
                    \sqrt{\frac{\log\log n}{\log n}}\right).
```
Let $`v=\lceil\log_2(n+2)\rceil`$ and
$`h_v=\lceil\log_2(v+2)\rceil`$. For a master target $`p`$,
use a local integer parameter bounded by
```math
p_{\rm loc}
          \leq \min\{p,\ c\sqrt{v/h_v}\},
```
with a sufficiently small fixed $`c>0`$. Integer square-root
comparisons implement the bound. Instances below the fixed
constant-size range needed for $`p_{\rm loc}\geq p_0`$ are
handled directly, for one fixed $`p_0`$.

Clipping only improves the $`\log^{O(p)}n`$ output factor.
When clipping occurs,
```math
n^{O(1/p_{\rm loc})}
             =2^{O(\sqrt{v h_v})}
             \leq 2^{O(p\log(U+2))}
```
provided $`n\leq2^{O(U)}`$. When clipping does not occur,
the same term is $`2^{O(U/p)}`$. Thus the intended
preprocessing-round envelope is safely
```math
2^{O(U/p+(p+r)\log(U+2))}.              \tag{2}
```
The split graph has only $`O(m)`$ actual records; no
master-sized padding is involved.

Using BFS for every graph up to
$`\log n=O(p^2\log U)`$ would instead give an unwanted
$`2^{O(p^2\log U)}`$ query factor. The clipping rule avoids
that loss.

## 6. The outstanding sequential interface

Before (1)--(2) can be used as a sequential static primitive,
the following source steps need constructive replacements
with the advertised total work:

* Appendix B.1 searches all disjoint pairs of cluster sets;
  this is exponential in the cluster count despite requiring
  no additional CONGEST rounds after the topology is known.
* Section 6.4 computes an embedded leaf sorting network by
  invoking an existence result with zero-round local work.
* Every actual token's physical trajectory and all associated
  preprocessing paths must be explicitly available at the
  claimed work and word cost.

In addition, the expectation identity in the displayed proof
of Lemma B.2 should not be applied without accounting for
the projection-dependent sets and matching choices. A
constructive cut-player replacement that loses only a
polylogarithmic factor in shuffler quality would suffice
for the intended output envelope, but that replacement
is a separate lemma.

Until those obligations are closed, this note supplies the
graph-model and parameter adapters only. It establishes no
new matching exponent.
