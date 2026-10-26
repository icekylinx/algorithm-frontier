# Separating the output quality and construction work of deterministic sparsifiers

**Research derivation, 24 October 2026.** This note reconstructs a parameterized
version of the deterministic static sparsifier used by the distance backend.
The reconstruction keeps the input-path-length factor in the published ambient
congestion theorem. Its different point is that the work of constructing short
paths need not be used as an upper bound on the lengths of those paths.

The existing 14/15 checkpoint is unchanged. The final section records a candidate
parameter balance for a separately composed backend; it is not an independently
implemented or externally verified algorithm.

## 1. Primary statements and parameters

The constructive dependencies are:

* [Chuzhoy, Gao, Li, Nanongkai, Peng and Saranurak,
  arXiv:1910.08025v2](https://arxiv.org/pdf/1910.08025), Theorem 1.6,
  Theorem 5.1, and the balanced-cluster recursion in the proof of Corollary 6.1.
* [Chuzhoy and Saranurak, arXiv:2009.08479v1](https://arxiv.org/pdf/2009.08479),
  Appendix B.4, Theorem 3.7, and the actual stage and path recurrences in
  Section 3.2, especially Lemmas 3.10 and 3.11.
* [van den Brand et al., arXiv:2309.16629v1](https://arxiv.org/pdf/2309.16629v1),
  Algorithm 4 and its proof, Theorem 8.1, and Appendix B's degree-band reduction.

Let $U\geq 2$ be a master logarithmic size bound; all graphs in the following
static computations have at most $2^{O(U)}$ explicit records. Put

$$
h=\lceil\log_2(U+2)\rceil.
$$

There are two independent integer parameters:

* $r\geq 1$, the recursion parameter of the deterministic cut player;
* $q\geq 2$, the number of levels in the decremental expander path oracle.

They are distinct from the later touched-set batching depth $K$ and the
numerical hierarchy's size-reduction parameter $k$. We use them only in a
range where $r,q\leq U$ and $qrh\leq U$. The latter condition keeps
all constructed witnesses within $2^{O(U)}$ records; it has ample
slack for the parameters in Section 6. Fixed constants in the bounds below come from the
named constructive algorithms, not from a choice depending on the input.

For sufficiently large fixed constants, define a common conductance threshold
and a cut-player work factor by

$$
\phi^{-1}=2^{O(rh)},\qquad
 F_r=2^{O(U/r+r^2h)}.                                      \tag{1}
$$

Their roles are different: $\log\phi^{-1}=O(rh)$, whereas
$\log F_r=O(U/r+r^2h)$. The latter is not raised to the path-oracle
depth in the stage-count argument below.

## 2. Expander decomposition with separate conductance and work bounds

CGLNPS Theorem 5.1, with its parameter denoted here by $r$, returns a cut
of size at most $\theta\mathrm{vol}(G)$. Either both sides have
constant-fraction volume, or one constant-fraction side has conductance at
least

$$
\theta/(\log m)^{O(r)}.
$$

Its time is

$$
m^{1+O(1/r)}(\log m)^{O(r^2)}/\theta^2.       \tag{2}
$$

Run the ordinary balanced-cluster recursion with
$\theta=\varepsilon/(c\log(m+2))$. A balanced return recurses on both
sides; an expanding return finishes its large side and recurses on the other.
Every active cluster's volume falls by a constant factor at each iteration.
There are $O(\log m)$ iterations, their graphs are edge-disjoint within an
iteration, and their cut budgets sum to at most $\varepsilon m$, after
adjusting $c$. The resulting pieces have conductance at least

$$
\varepsilon\,2^{-O(rh)},
$$

and total work $mF_r\mathrm{poly}(U)/\varepsilon^2$.
This uses Theorem 5.1's actual output guarantee. The larger $r^2$ exponent
printed in the packaged Corollary 6.1 is not needed in this recursion.

When a recursive cluster is too small for a given source parameter $r$, use
$r'=\min\{r,\lfloor\log |E|/c_0\rfloor\}$, with a constant-size base
case. The source's absolute cutoff is met by a sufficiently large fixed $c_0$.
The output guarantee only improves. Its time still fits the master envelope:
when $r'<r$, $\log |E|/r'=O(1)$, and
$(r')^2\log\log(|E|+2)\leq O(r^2h)$. No small invocation is padded
to master size.

### Actual-size degree bands without artificial self-loops

In the degree-band reduction, start with the nonisolated vertex count $n$ and
edge count $m$, and set

$$
\ell=\max\{0,\lceil\log_2(2m/n)\rceil\},\qquad G_\ell=G.
$$

The invariant is $|E(G_i)|\leq 2^i n$. No maximum-degree condition is
needed. At stage $i>0$, apply the preceding loopless decomposition with
crossing-edge budget at most $|E(G_i)|/4$, obtaining components of
conductance at least $\phi$. In each nontrivial component $C$, initialize
CS21 Theorem 3.7's deterministic expander-pruning structure.
For a loopless multigraph, use the simple subdivision and projection
adapter proved in Section 4 for pruning as well as for path queries.
Fix an absolute constant $c_{\rm pr}$ covering this adapter: up to
$\phi |E(C)|/c_{\rm pr}$ original-edge deletions, it removes
original volume at most $c_{\rm pr}t_C/\phi$, leaves a strong
$\phi/c_{\rm pr}$-expander with respect to the original component,
and has work $O(t_C\mathrm{poly}(U)/\phi^2)$.
All constants below use this literal simple-graph reduction.

Fix an absolute constant $C_b$, sufficiently large, and put

$$
\delta_i=\phi 2^i/C_b.
$$

While a surviving vertex has positive current degree smaller than
$\delta_i$, choose it and explicitly request deletion of all its current
incident edges. Settle the pruning structure before choosing the next
vertex. A chosen vertex becomes isolated and never acquires an edge again;
there are at most $n$ choices. Thus the number $t_i$ of explicitly
requested edge deletions, summed over all initial components of the band,
satisfies

$$
t_i<\delta_i n.
$$

Move to the next residual graph every explicitly deleted edge and every
original component edge incident to a pruned vertex. The latter includes
edges on an earlier pruning boundary, not only edges present when that
vertex is finally processed. The pruning theorem bounds this count by the
initial volume of the pruned set, at most $c_{\rm pr}t_C/\phi$ in a component
with $t_C$ explicit requests.

If a component's next request would exceed its allowed budget
$\lfloor\phi |E(C)|/c_{\rm pr}\rfloor$, count that first excess request and
move the whole remaining component to the residual graph. Its original
edge count is then smaller than $c_{\rm pr}t_C/\phi$. This convention also
handles a quota below one: the first actual edge-deletion request pays
for discarding the component. Already moved edges are counted only once.
Therefore, for an absolute constant $c_b$,

$$
|E(G_{i-1})|
   \leq |E(G_i)|/4+c_b t_i/\phi
   \leq 2^i n(1/4+c_b/C_b)
   \leq 2^{i-1}n.                                      \tag{2a}
$$

Choose $C_b\geq 4c_b$. The retained graph $J_i$ is the union of
the final surviving component graphs. Every nontrivial component has
conductance at least $\phi/c_{\rm pr}$ and minimum degree at least
$\delta_i$. Zero-edge isolates are omitted. The final residual
$G_0$ has at most $n$ edges and is retained directly.
For Algorithm 4's interface, use the common parameter
$\bar\phi=\phi/\max\{c_{\rm pr},C_b\}$. Then both required properties hold
literally: conductance at least $\bar\phi$ and minimum degree at least
$\bar\phi 2^i$. Below, $\phi$ may denote this smaller common
parameter; all displayed envelopes are unchanged by this fixed factor.

A heap or degree bucket detects low-degree vertices. Each moved edge is
scanned only a constant number of times within its band. Pruning and
whole-component quota handling cost
$O(|E(G_i)|+t_i\mathrm{poly}(U)/\phi^2)$, in addition to the
decomposition. Since $2^\ell n\leq 4m$,

$$
\sum_{i=1}^{\ell}2^i n=O(m).
$$

Consequently all band construction work is
$mF_r\mathrm{poly}(U,\phi^{-1})$, and there is no
$n\Delta$ padding cost. High-degree vertices remain permitted. The
witness size for a band is bounded through its total degree:
$|E(G_i)|/(\phi2^i)=O(n/\phi)$.

This loopless construction replaces the artificial-loop degree-band step
of the packaged static sparsifier. It invokes CGLNPS Theorem 5.1 only on
inputs covered by its literal loopless-multigraph convention.

### Loopless weighted witnesses in the degree bands

Algorithm 4 needs a constant-conductance witness with degrees comparable to
$$
w_v=\deg_{J_i[X]}(v)/(\phi2^i)\geq1.
$$
These weights are balanced: because the component is loopless,
$w_v\leq\sum_{u\ne v}w_u$. Put $p_v=\lceil w_v\rceil$ and
$N=\sum_v p_v$. Then $p_v\leq\sum_{u\ne v}p_u$, so every
fiber has at most $N/2$ ports.

Apply CGLNPS Theorem 2.4 to $N$ ports, obtaining a graph of fixed
maximum degree $D_0$ and fixed positive edge expansion $\alpha_0$.
Group $p_v$ ports into the fiber for $v$, contract each fiber,
and discard all edges internal to a fiber. Retain parallel crossing
edge IDs. For one fiber its boundary has at least $\alpha_0p_v$
edges. Replicate every remaining edge a fixed integer
$c_w\geq1/\alpha_0$ times. The resulting loopless multigraph has
$$
w_v\leq p_v\leq\deg_W(v)
       \leq c_wD_0p_v\leq 2c_wD_0w_v.
$$
For any union of vertex fibers, its crossing edge count is at least
$c_w\alpha_0$ times the smaller port-side cardinality, while each
side's witness volume is at most $c_wD_0$ times its port cardinality.
Thus $W$ has conductance at least $\alpha_0/D_0$.

This construction takes $O(\sum_v w_v)$ time and space, with fixed
constant factors. It gives exactly the degree comparisons needed in
Algorithm 4's two routing tasks. It does not require an arbitrary-weight
loopless version of the packaged witness theorem. Every graph sent to
the path oracle remains loopless; parallel edges use the subdivision
adapter below.

## 3. A terminal expander with a cheap output and more expensive construction

CGLNPS Theorem 1.6 is a cut player on graphs of maximum degree
$O(\log |T|)$. Its certificate has sparsity
$(\log |T|)^{-O(r)}$, and its time is
$|T|^{1+O(1/r)}(\log |T|)^{O(r^2)}$. Run the cut-matching game
of CGLNPS Theorem 2.5, using the following explicit moves. If the cut player
returns a sparse cut $A_i,B_i$ with
$|T|/4\leq |A_i|\leq |B_i|$, **extend**
$A_i\subseteq A_i'$ to a balanced partition
$(A_i',B_i')$; the matching player supplies a perfect matching between
those two sides. If the cut player instead certifies an expanding set
$S$ with $|S|\geq |T|/2$, supply one final matching from
$T\setminus S$ into distinct vertices of $S$. CGLNPS Observation 2.3
then extends the certified sparsity to all terminals. These are the moves
specified in the primary CGLNPS proof; they avoid the reversed inclusion
and final-side typographical errors in CS21 Appendix B.4.

The game has $O(\log |T|)$ rounds. Its final terminal graph has maximum
degree $O(\log |T|)$ and conductance $2^{-O(rh)}$. If the terminal
cardinality is odd, run the even game on all but one terminal and attach
the last terminal by one additional matching edge; the same bounds hold.

The matching player is CS21 Theorem B.9. In an input expander of conductance
at least a fixed positive constant times $\phi$, it constructs each matching with paths of length
$O(U/\phi)$, edge congestion $O(U^2/\phi^2)$, and time
$m\mathrm{poly}(U)/\phi^3$. Unioning the matchings gives the
safe bounds

$$
\lambda=O(U/\phi),\qquad
      \eta=O(U^3/\phi^2),                                \tag{3}
$$

for the terminal embedding. We use the proof's $U^3$ congestion bound;
Theorem 3.8's displayed $U^2$ bound omits the union over matching rounds.
The construction time is at most

$$
m F_r\mathrm{poly}(U)/\phi^3.    \tag{4}
$$

In particular $F_r$ changes the cost of building this object, not its
$\lambda,\eta$ or its output conductance.

For a simple-graph implementation of the subsequent path oracle, deduplicate
parallel witness edges after the whole cut-matching game. Their multiplicity
is at most $O(\log |T|)$. Keeping one edge and its associated embedding path
loses at most that factor in conductance, while decreasing embedding
congestion and maximum degree. This loss is absorbed when choosing the
common $\phi=2^{-c rh}$. Do not deduplicate during the game itself.

## 4. A parameterized decremental expander path oracle

Take an initially $\phi$-expanding graph of actual size $m$.
Use the CS21 Section 3.2 hierarchy with $q$ levels and nominal level sizes
$m^{i/q}$, rounded by integer ceilings. At each stage, construct the
next smaller terminal expander by Section 3. Its output conductance is at
least the common $\phi$, independently of the larger work factor
$F_r$. Expander pruning is CS21 Theorem 3.7, whose update work is
$O(tU/\phi^2)$, removed original volume is at most
$O(t/\phi)$, and surviving conductance is at least
$\phi/c_{\rm pr}$ after the multigraph adapter.

The top input may be a loopless multigraph. Subdivide every input edge once,
retaining its original edge ID on the two-edge representation. This gives a
simple graph of constant-factor size and constant-factor smaller conductance.
An original deletion gives two subdivision-edge deletions. Expose only pruned
original vertices, and project returned subdivision paths to original edge
IDs. The removed original volume is bounded by the removed subdivision
volume. The returned paths exist in the original graph with its pruned
original vertices removed. Strong expansion also projects: extend any
cut of surviving original vertices by placing a surviving subdivision
vertex with its same-side endpoint, or with either endpoint when that
edge crosses the cut. The subdivision cut is no larger than the
corresponding original cut, and the original-subdivision volume of
each side is at least the original volume of its original vertices.
Internal witness graphs can be simple by the
deduplication just described. Original input loops have empty routes and are
handled outside this path oracle.

### Current roots and deletion order

The ES tree at level $i$ is rooted at the CURRENT surviving vertices of the
level-$(i-1)$ expander, not the terminal set as it stood at that expander's
birth. Represent these roots by super-source edges. When a lower terminal is
pruned, delete its super-source edge. On a stage restart install the new root
set and rebuild the corresponding ES tree. These are deletion-only changes
within a stage and cost at most one root-edge deletion per terminal.

Complete parent-edge deletions, all embedding-preimage deletions, all
resulting lower prunings/restarts, and all super-source root-edge deletions
before answering a query. Thus the two ES legs always end at living lower
terminals, and the recursive middle query is legal. Parent-pruned endpoints
also remove the associated embedded lower edges before querying. These
explicit steps repair an ambiguity in the source's abbreviated pseudocode
without changing its stage bound.

Apply pruning at the bottom level $G_1$ as well. After a settled
bottom edge deletion and its pruning output, recompute a BFS tree on
the surviving bottom expander, rooted at any surviving vertex.
Remove pruned bottom vertices from the parent ES root set before
queries. The printed $i=1$ deletion branch omits this pruning
operation, although the accompanying proof assumes that every
current $G_i$ is pruned; simply recomputing a tree in an unpruned
graph could leave an isolated terminal unreachable. A base stage
has $O(m^{1/q}\mathrm{poly}(U))$ edges and at most that
many deletions, so these BFS recomputations cost
$m^{2/q}\mathrm{poly}(U,\phi^{-1})$, already covered by
the $i=1$ case of (5).

Whenever a stage is rebuilt, retire its old embedding and deletion
queue records by generation. A callback from an old generation
cannot delete an edge of a newly built child. Finish the replacement
and all current-generation prune/root changes before queries.

### Small instances

If $\log(m+2)<c_1qrh$, use ordinary expander pruning and perform a
direct BFS for each query. This costs at most $2^{O(qrh)}$ per query, and
the initialization plus all pruning costs are $m2^{O(qrh)}$. Otherwise
the smallest nominal terminal set has logarithmic size at least
$c_1rh$. It satisfies the cut-player cutoff
$|T|^{1/r}\geq N_0$, and consecutive hierarchy sizes have enough
slack to dominate the $O(U)$ maximum degree and pruning losses. This is an
actual-size base case, not a master-sized allocation.
In particular, choose $c_1$ large enough that
$m^{1/q}\geq U^{c_2}\phi^{-c_2}$ for the fixed constants used
in the stage proof. Then the smallest nonbase stage has a positive
deletion budget and enough surviving vertices to supply the next
terminal set. Integer floors in the quota and hierarchy sizes
change only fixed factors.

### Stage work and stage counts

Let $B=\mathrm{poly}(U,\phi^{-1})=2^{O(rh)}$. A single
level-$i$ stage costs at most

$$
m^{(i+1)/q}F_r B                      \tag{5}
$$

apart from recursively charged lower stages. This includes one terminal
expander construction, its explicit inverse embedding lists, its ES tree,
pruning, and processing the at most $\eta$ immediate preimages of
each deleted edge.

One stage at level $i+1$ causes at most

$$
m^{1/q}B                       \tag{6}
$$

level-$i$ stages. This is exactly the source's counting argument: pruning
removes at most a $1/\phi$ multiple of deleted-edge volume, the
embedding amplifies deletions by at most $\eta$, and a child stage
requires a $\phi$ fraction of its initial edges to disappear.
Only output congestion and conductance occur in $6$. **The construction
factor $F_r$ does not occur in the number of stages.**

Multiplying $5$ by the number
$m^{(q-i)/q}B^{O(q-i)}$ of level-$i$ stages and summing gives

$$
\boxed{
    \text{initialization plus all deletion work}
      \ \leq mF,
    \qquad
    F=2^{O(U/q+U/r+r^2h+qrh)}.
 }                                                         \tag{7}
$$

For queries the source recurrence is

$$
L_i\leq O(U/\phi)\,[1+L_{i-1}],
$$

so a returned simple path and its computation have size at most

$$
\Lambda=2^{O(qrh)}.             \tag{8}
$$

The path is made simple by deleting closed subwalks in linear time in its
explicit length. Only the final simple path is charged to ambient vertex
congestion in the static sparsifier.

The source and multigraph adapter support at most
$\phi m/c_{\rm pr}$ original-edge deletions before the top
expander is exhausted. At the first request beyond that budget, declare every
remaining original vertex pruned and stop that oracle. This costs $O(m)$
once and keeps removed volume $O(t/\phi)$, after increasing the absolute
constant. It supplies the all-deletion convention used by Algorithm 4.

## 5. Consequences for the literal ambient static sparsifier

Let $J$ be the demand graph and $\Pi:J\to H$ an explicit ambient
embedding. Let $L_0\geq1$ be its maximum path cardinality and $C_0$ its
vertex congestion. Apply the degree-band decomposition from Section 2 and
Algorithm 4 of van den Brand et al., using Section 4's oracle.

Here is an explicit weighted version of the two charging arguments.
It is useful because the published proof has a few numerical slips that
are immaterial to its asymptotic conclusion but should not be copied.
Count repeated ambient path occurrences in $C_0$ and in the maintained
loads; this is at least the number of distinct demand IDs using a vertex.

Give every witness edge in band $i>0$ weight
$\rho_i=\phi2^i$, and give the directly retained $J_0$ edges weight
one. The weighted witness degrees obey
$$
\deg_{J_i}(v)\leq \rho_i\deg_{W_i}(v)
                      \leq D_w\deg_{J_i}(v)
$$
for a fixed $D_w$. The nonbase witness edge IDs are fresh and distinct
from all demand IDs, even when their endpoint pairs agree.

**Route the witness into $J$.** In each round, initialize a fresh
path oracle on each band component. Route every still-unrouted witness
edge whose endpoints survive, using a simple path in its own band.
Retain the route permanently once assigned. At ambient vertex $x$,
maintain the weighted, occurrence-counted load of the composed routes
$\Pi\circ\Pi_{W\to J}$. In round $j$, when that load reaches
$j\tau_1$, delete from the current oracles every original demand edge
whose input path uses $x$, where
$$
\tau_1=c_1'\Lambda(L_0+1)(C_0+\Delta(J))/\phi.
$$
Use a sufficiently large fixed $c_1'$.

One newly assigned witness route increases any one ambient load by at
most $\Delta(J)\Lambda(L_0+1)$, because its edge weight is at most
$\Delta(J)$. Thus the overshoot is at most $\tau_1/2$. Each
ambient vertex disabled in a round has accumulated at least
$\tau_1/2$ new load in that round. If $B$ is the weighted mass of
witness edges assigned during the round, total new ambient load is at
most $\Lambda(L_0+1)B$. The total number of original demand edges
explicitly deleted from all band oracles is therefore at most
$$
2C_0\Lambda(L_0+1)B/\tau_1.
$$
Pruning removes initial band volume at most a fixed constant times this
quantity divided by $\phi$. Every witness edge left unrouted has a
pruned endpoint. Its total weighted mass is at most $D_w$ times the
removed initial band volume. Choosing $c_1'$ sufficiently large makes
that remaining mass at most a fixed multiple of $B$, and even at most
$B/2$ if desired. Consequently each round makes constant-factor
progress. This is the correct constant-fraction conclusion; the
factor $18$ is reversed in one displayed deduction of the source's
Claim 8.7, without affecting this argument.

The total initial weighted mass is $O(|E(J)|)$; every positive
witness weight is at least $\min\{1,\phi\}$. Hence the number of
rounds is $O(\log(|E(J)|+2)+\log(1/\phi))=O(U)$.
The final weighted ambient congestion is $O(U\tau_1)$.

**Route $J$ into the witness.** Define normalized witness-edge load
as the number of assigned unit-demand routes using that edge, divided
by its weight $\rho_i$. In round $j$, use a fresh path oracle in
each witness component and delete an edge from that round's oracle
when its normalized load reaches $j\tau_2$, where
$$
\tau_2=c_2'\Lambda/\phi.
$$
Every new simple route increases the load of an edge by
$1/\rho_i\leq1/\phi$, so a sufficiently large fixed $c_2'$
again bounds the overshoot by $\tau_2/2$. The increase need not be
at most one; this is the normalized-weight correction to the
published Invariant 2.

If $B'$ demand edges are assigned in a round, the sum of
$\rho_i$ times the new normalized edge load is at most
$\Lambda B'$. Thus the total weight of explicitly deleted witness
edges is at most $2\Lambda B'/\tau_2$. The witness weights are
uniform within each component, so ordinary pruning bounds the
removed weighted volume by a fixed constant times this deleted
weight divided by $\phi$. The degree lower bound
$\rho_i\deg_{W_i}\geq\deg_{J_i}$ shows that the number of still
unrouted demand edges is no larger than that removed weighted
volume. For a sufficiently large fixed $c_2'$, each round again
makes constant progress. There are $O(\log(|E(J)|+2))$ rounds,
and the final normalized edge congestion is $O(U\tau_2)$.

The directly retained $J_0$ edges use their own identity routes;
they fit the initial-load bounds and require no path-oracle call.
For the other edges, both witness-routing steps have maximum path
length $\Lambda$. Weighted composition of the two embeddings gives
ambient congestion
$$
O(U^2\tau_1\tau_2)
 =O\!\left(
  U^2\Lambda^2\phi^{-2}(L_0+1)(C_0+\Delta(J))
 \right).
$$
Because $L_0\geq1$, the factor $L_0+1$ is absorbed by $2L_0$.
With a common output envelope

$$
\Gamma=2^{O(qrh)},              \tag{9}
$$

the resulting selected subgraph and explicit embedding satisfy

$$
|E(\widetilde J)|\leq |V(J)|\Gamma\mathrm{poly}(U),
 \qquad L(\widehat\Pi)\leq\Gamma,\qquad
 L(\Pi\circ\widehat\Pi)\leq\Gamma L_0,
$$

$$
C(\Pi\circ\widehat\Pi)
       \leq \Gamma L_0[C_0+\Delta(J)].                    \tag{10}
$$

For example, the source proof gives a congestion factor proportional to
$\Lambda^2\phi^{-2}\mathrm{poly}(U)$, and path factor
$\Lambda^2$; both fit $9$. The selected witness-path count and total
support also fit that envelope. Every representative selected edge remains an
actual demand-edge ID, as required by the later core-edge lift.
If an interface requires each final route in $\widetilde J$ to be
simple, erase closed subwalks in that graph in time proportional to
the explicit route length. This only deletes occurrences from its
ambient expansion and cannot increase any of the stated bounds.

The initialization and all adaptive path-oracle deletions cost at most a fixed
multiple of the actual host size times $F$, for each of the $O(U)$
rounds. Explicit path output, ambient inverse indexing, and
edge updates contribute fixed factors of $\Gamma$ and $L_0$.
Thus a safe runtime is

$$
|E(J)|\,F\,\Gamma^{O(1)}
                      (L_0+1)\mathrm{poly}(U).    \tag{11}
$$

An ambient graph is represented by the union of the supplied explicit paths
and relevant central edges. Unrelated ambient isolates are not scanned. The
same conventions on parallel IDs, loop demands, original endpoints and
explicit route-owner records apply as in
[demand-route notifications](demand-route-notifications-and-local-work.md).

Formula $10$ is **not** the unsupported length-free restatement. The new
separation is between the larger local work factor $F$ and the smaller
output factor $\Gamma$.

### Finite arithmetic and primitive boundaries

Choose the common $\phi$ as a reciprocal power of two below the
proved conductance threshold, for example
$2^{-c_\phi r h}$ for a sufficiently large fixed integer
$c_\phi$. The component quotas, witness port counts, normalized
loads, and threshold comparisons then use integers or dyadic
rationals. The positive weights have logarithmic magnitudes
$O(U+rh)$, and input-path indices and explicitly generated path
records are charged at their actual lengths. Floors and ceilings of
the hierarchy sizes $m^{i/q}$ are computed by integer power
comparisons. No real-arithmetic oracle or uncharged implicit path
enumeration is required.

The source algorithms are used with their constructive cut-player,
matching-player, pruning, and ES-tree procedures. Fixed constants
such as the cutoff $N_0$ and the large absolute constants in this
note belong to a fixed finite program or to its enumerated
constant-parameter family. They are not input-dependent advice.
For the growing parameters of Section 6, all declared counts and
integer bit lengths are $2^{O(U)}$ and $O(\mathrm{poly}U)$,
respectively; the master backend charges their arithmetic and may
guard the corresponding explicit bounds.

The result proved here is a STATIC subgraph and explicit-routing
primitive. It does not by itself provide a native split data
structure, a fully dynamic cycle oracle, or a matching algorithm.
Those interfaces are the separate constructions named below.

## 6. Candidate balance after short-period batching and degree reset

This section assumes the separately documented
[amortized static-base distance sparsifier](amortized-static-base-distance-sparsifier.md)
and its complete degree-reset/raw-lift interfaces. It uses that construction's
own integer batching clock, not the different KMPG black-box restriction on
$K$. The original length-sensitive recurrence gives local work
$\Gamma^{O(K^2)}$, while selected recourse remains a fixed power of
$\rho\Gamma\mathrm{poly}(U)$, where
$\log\rho=O(U/K)$.

Writing $x=\log k$, a safe prospective total logarithmic overhead is

$$
O\!\left(
 x+U/r+U/q+r^2h+qrh+K^2qrh
       +\frac{U^2}{Kx}+\frac{Uqrh}{x}
       +\frac{UKqrh}{x}
 \right).                                                 \tag{12}
$$

Here the work factor $F$ is local/additive. It is not inserted into the
selected-degree cap, the recursive update multiplier, or the exposed forest
occurrence cap. The last term explicitly charges the raw-quality loss:
each numerical level may lose $\Gamma^{O(K)}$, across
$O(U/x)$ levels. When $K^2qrh=o(U)$, the one-level path-quality factor
$\Gamma^{O(K)}$ is also bounded by a fixed power of the recourse
envelope, so its multiplication through the hierarchy is included.

The power/logarithm balance suggested by $12$ is

$$
r,q=\Theta(U^{1/7}h^{-1/7}),\qquad
 K=\Theta(U^{2/7}h^{-2/7}),\qquad
 x=\Theta(U^{6/7}h^{1/7}).                                \tag{13}
$$

It gives $\log\Gamma=O(U^{2/7}h^{5/7})$,
$\log F=O(U^{6/7}h^{1/7})$, and makes every term in $12$ at most
$O(U^{6/7}h^{1/7})$. For instance
$K^2qrh=\Theta(U^{6/7}h^{1/7})=o(U)$,
while $\log R=O(U^{5/7}h^{2/7})=o(x)$.

This is a proposed composition rate to audit, not a claim that merely replacing
a printed $2/3$ by a smaller number proves a matching theorem. The
short-period selected transcript, delayed-initial-credit accounting, master
bit and horizon guards, complete raw certificates, exact projection recovery,
and final optimality verification must all be carried through a separate
composition. None of those obligations is replaced by the static result here.
