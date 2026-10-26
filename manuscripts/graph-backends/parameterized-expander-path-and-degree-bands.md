# Separating expander-path quality from construction time

**Mathematical derivation, 24 October 2026.** This note isolates the
parameter dependence needed by a proposed sharper static sparsifier.
It reconstructs the relevant source algorithms with separate quality
and work envelopes; it does not read such a separation into a theorem
that packages both quantities into one symbol.

The primary sources are
[Chuzhoy--Saranurak, arXiv:2009.08479v1](https://arxiv.org/pdf/2009.08479),
Sections 3.1--3.2 and Appendix B.4;
[Chuzhoy et al., arXiv:1910.08025v2](https://arxiv.org/pdf/1910.08025),
Theorems 1.6 and 5.1; and
[van den Brand et al., arXiv:2309.16629v1](https://arxiv.org/pdf/2309.16629),
Algorithm 4 and Theorem 8.1. The complete static construction is
developed in
[the separated sparsifier note](separated-static-sparsifier-parameters.md).

Let $U\geq2$ bound the logarithm of every actual graph size used in
one primitive invocation. Let $q\geq2$ and $r\geq1$ be integers.
The useful ranges have $qr\log(U+2)=o(U)$; the construction below
also specifies actual-size fallbacks instead of padding small graphs.

## 1. The cut-player interface retains a free parameter

Theorem 1.6 of Chuzhoy et al. takes a graph on $t$ vertices with
maximum degree $O(\log t)$. Its parameter must satisfy
$t^{1/r}\geq N_0$, for a fixed source constant $N_0$.
It either produces the required balanced sparse cut or identifies
a large induced subgraph with sparsity
$(\log t)^{-O(r)}$. Its time is
$$
t\exp\!\left(O\!\left(\frac{\log t}{r}
                         +r^2\log\log(t+2)\right)\right).
 \tag{1}
$$
The proof's constants are uniform in the integer parameter $r$:
its Theorem 4.1 has a fixed constant multiplying the quadratic
parameter exponent. This is not a fixed-$r$ asymptotic statement.

The cut-matching game in Chuzhoy--Saranurak Appendix B.4.1 has
$O(\log t)$ rounds. Keeping $r$ free therefore yields a witness
of conductance $(\log t)^{-O(r)}$, degree $O(\log t)$, and
construction cost (1), up to fixed polynomial logarithms.
The matching player in Appendix B.4.2 uses an input expander of
conductance $\phi$, and produces paths of length
$$
\ell=O(\phi^{-1}\log m).
 \tag{2}
$$
One round has congestion $O(\phi^{-2}\log^2m)$.
Taking the union over the cut-matching rounds gives the conservative
bound
$$
\eta=O(\phi^{-2}\log^3m).
 \tag{3}
$$
The extra logarithm is present in the Appendix B.4.3 proof even
though the display of Theorem 3.8 states only $\log^2m$.
We use (3).

Choose one common dyadic conductance parameter
$$
\phi=2^{-\lceil c_\phi r\log_2(U+2)\rceil}
 \tag{4}
$$
with a sufficiently large fixed coefficient. All witness graphs
then meet this same initial expansion guarantee. Expansion does not
multiply through the hierarchy: each new witness is certified by a
fresh cut-matching game.

## 2. The hierarchy multiplies quality, not the cut-player running time

Use the $q$-level hierarchy from Chuzhoy--Saranurak Section 3.2,
with level sizes comparable to $m^{i/q}$.
Every embedding between successive levels has length (2) and
congestion (3). The query recurrence is
$$
L_i\leq O(\phi^{-1}\log m)(L_{i-1}+1),
$$
so both the reported path length and its reporting time are bounded by
$$
\Lambda=\exp(O(qr\log(U+2))).
 \tag{5}
$$
Repeated vertices in the reported walk are removed by ordinary
linear-time cycle erasure.

The stage-count argument in Lemma 3.10 uses only the embedding
congestion and the pruning volume bound. In one level-$i$ stage,
the number of level-$(i-1)$ stages is at most
$$
m^{1/q}\mathrm{poly}(U)\phi^{-O(1)}.
 \tag{6}
$$
Consequently there are at most
$$
m^{(q-i)/q}
           \bigl(\mathrm{poly}(U)\phi^{-O(1)}\bigr)^{q-i}
$$
level-$i$ stages. The nonrecursive work of one such stage is at most
$$
m^{(i+1)/q}
 \exp\!\left(O\!\left(U/r+r^2\log(U+2)+r\log(U+2)\right)\right).
 \tag{7}
$$
Multiplying the number of stages by (7) and summing over the levels
gives total work
$$
m\exp\!\left(
 O\!\left(U/q+U/r+r^2\log(U+2)+qr\log(U+2)\right)\right).
 \tag{8}
$$
In particular the $r^2\log U$ cost of constructing a witness is
incurred as a local factor in (7). It is not raised to the hierarchy
depth $q$. The propagation factors in (6) depend on $\eta,\phi$,
not on the time used to construct their embeddings.

### Current terminals and deletion ordering

The ES-tree at level $i$ must have a supersource adjacent to the
**current surviving** vertices of the lower graph. When a lower
terminal is pruned, delete its supersource edge. Otherwise a query
could reach a terminal that no longer belongs to the recursive graph.
Process the parent deletion, all propagated lower deletions and
prunings, and all resulting root-edge removals before answering any
query. Each root edge dies at most once in its stage. Its deletion
is covered by the usual $O(m\cdot\text{depth})$ ES-tree bound.
When the lower graph is rebuilt, rebuild the corresponding ES-tree.

Apply pruning at the bottom level as well. The abbreviated source
case for $i=1$ only recomputes its tree, which by itself would not
remove a newly isolated lower terminal. After each incoming deletion,
prune, propagate all removed base terminals to the parent's root
set, and recompute the base BFS tree on the surviving expander.
Use the same deletion-quota restart rule there. At most the initial
number of base edges can be deleted within a base stage, so these
BFS recomputations cost
$m^{2/q}\mathrm{poly}(U,\phi^{-1})$, within (7) for $i=1$.

The path oracle is retired once its top-level deletion quota is
reached. Reporting every remaining vertex as pruned at that point
preserves $\mathrm{vol}(S)=O(t/\phi)$, with a larger absolute
constant. This supplies the all-deletion interface used by the
static sparsifier; it does not ask the source oracle to exceed its
promised quota.

## 3. Actual-size and graph-model wrappers

The smallest cut-player call cannot be ignored when checking
$t^{1/r}\geq N_0$. If
$$
\log m<Cqr\log(U+2),
 \tag{9}
$$
answer queries by direct BFS on the surviving expander, together
with the ordinary pruning procedure. Its actual size is already
at most the right envelope in (5). Its initialization and update
work fit (8). No array of that envelope size is allocated.
Otherwise the smallest terminal set, of size comparable to
$m^{1/q}$, satisfies the source lower-size condition for a large
enough fixed $C$. It also dominates the logarithmic maximum degree,
so enough surviving vertices remain to choose the next terminal set
after pruning. Integer level sizes can be computed by integer roots
of $m^i$; the intermediate bit length is polynomial in $U$.

The general static sparsifier uses multigraphs, whereas the opening
convention of Chuzhoy--Saranurak is simple graphs. The following
explicit wrapper handles this distinction.

* Input loops are served separately with their empty embedding and
  do not enter the path-oracle graph. Subdivide every remaining
  edge ID once. Parallel IDs now have distinct subdivision vertices,
  so the graph is simple. Conductance changes by only a constant.
  One original deletion becomes two deletions, and paths are projected
  back to their original edge IDs.
  This concerns one static routing call: logical loop IDs and their
  endpoint annotations remain present in the enclosing native splitter.
* The internal cut-matching witness may contain parallel edges.
  Chuzhoy et al. explicitly permit these. Finish that game first,
  then retain one copy, with one chosen embedding path, from each
  parallel class. There are at most $O(\log t)$ copies in a class,
  so this loses only that factor in conductance and never increases
  embedding congestion or degree. The slack in (4) covers it.
  Thus the recursive expander input graphs are simple as well.

Report only original vertices in the projected top-level pruned set.
Their original volume is at most the subdivision volume removed.
For any cut of surviving original vertices, put every surviving
subdivision vertex on a side of one of its surviving endpoints.
This produces a subdivision cut with no more crossing edges than
the original cut, while the reference volume of either side includes
the original degrees on that side. Strong expansion therefore
projects back. Missing subdivision vertices merely delete additional
routing options; any reported projected path is still a valid path
of the original graph.
This adapter also applies when invoking pruning alone in Section 4.
Use a fixed smaller original-edge deletion quota and fixed enlarged
volume/conductance constants to account for the two subdivision-edge
deletions and the constant conductance loss. The literal source
constants $8,10,6$ are not copied unchanged through this adapter.

## 4. Degree bands without artificial loops

The degree-band decomposition required by the static sparsifier can
be reconstructed using only loopless multigraph inputs.
First remove isolates, put $n=|V|$, $m=|E|$, and start at
$$
h=\max\{0,\lceil\log_2(m/n)\rceil\}.
 \tag{10}
$$
Then $m\leq2^hn$, and $\sum_{i=0}^h2^in=O(m)$.
Starting at the maximum degree instead would not give this work
bound on an arbitrary graph.

At band $i>0$, assume its current graph $J_i$ has at most
$2^in$ edges. Compute an ordinary $\phi$-expander decomposition
with at most $|E(J_i)|/4$ crossing edges. This follows directly
by recursively applying Chuzhoy et al. Theorem 5.1 with cut budget
$1/(C_0\log(m+2))$: recursion depth is $O(\log m)$, because
every recursive child loses a constant fraction of the current
volume. The output expansion is $\exp(-O(r\log(U+2)))$, and
the work is
$$
|E(J_i)|\exp(O(U/r+r^2\log(U+2))).
 \tag{11}
$$
An actual connected component too small for the source's parameter
condition can be returned directly: a connected $e$-edge graph
has conductance at least $1/e$, which is more than the chosen
global $\phi$ at this cutoff.

Initialize pruning on each nontrivial expander component, using
Section 3's simple-graph adapter for a multigraph.
Repeatedly choose a current vertex of degree less than
$$
\delta_i=\phi\,2^i/C_1
 \tag{12}
$$
and explicitly delete its current incident edges. Forward these
edge deletions to its pruning instance. Move all newly pruned
original edges to the next band. If a component's permitted
deletion quota is first crossed, discard that entire component
to the next band. Such a discard costs
$O(t_C/\phi)$ original edges, where $t_C$ counts its explicit
deletions, so it obeys the same charge as ordinary pruning.

Each vertex is chosen at most once in this band. Hence the total
number of explicit current-edge deletions is less than
$\delta_i n$, and all pruning/discard movements are bounded by
$$
O(\delta_i n/\phi)=O(2^in/C_1).
 \tag{13}
$$
This counts original component edges, including boundaries removed
by earlier pruning; it does not confuse current degree with original
volume. A chosen vertex that remains only as an isolated record
may be omitted separately, since it has no remaining edge to move.
For sufficiently large fixed $C_1$, (13) plus the decomposition
crossings is at most $2^{i-1}n$. This proves the next-band invariant.

Every surviving nontrivial component has conductance at least
$\phi/c_{\rm pr}$, for one fixed constant $c_{\rm pr}$, and
minimum degree at least $\delta_i$. Both guarantees
hold with one common parameter $\phi'=c\phi$, for a fixed small
constant $c>0$. Band zero has at most $n$ edges and is retained
directly. The pruning time sums to
$$
\sum_i O(2^in\,\mathrm{poly}(U)/\phi)
             =O(m\,\mathrm{poly}(U)/\phi),
 \tag{14}
$$
which fits (11). Degrees and candidate queues can be updated by
scanning each moved edge once per band. No artificial self-loop
extension of Theorem 5.1 is used in this construction.

## 5. A loopless witness for the actual balanced weights

There is one further graph-model detail in the static construction.
An arbitrary prescribed weighted degree vector need not admit a
loopless graph: one coordinate might exceed the sum of all others.
The actual degree-band weights avoid this obstruction. In a
nontrivial loopless component $J_i[X]$, put
$$
w_v=\deg_{J_i[X]}(v)/(\phi'2^i).
$$
The degree-band guarantee gives $w_v\geq1$, and absence of loops
gives $w_v\leq\sum_{u\ne v}w_u$. Set $p_v=\lceil w_v\rceil$.
These integers remain balanced, because
$$
\lceil w_v\rceil
 \leq\left\lceil\sum_{u\ne v}w_u\right\rceil
 \leq\sum_{u\ne v}\lceil w_u\rceil.
 \tag{15}
$$

Construct a constant-conductance expander on
$N=\sum_vp_v\geq2$ ports, with maximum degree $D_0=O(1)$
and minimum degree at least one, using the deterministic
constant-degree expander primitive. Group $p_v$ ports at each
vertex $v$, contract each group, discard its internal edges,
and replicate every remaining edge by one fixed integer
$c\geq1/\phi_0$, where $\phi_0$ is the port expander's
conductance.

Every fiber has at most $N/2$ ports. Its port boundary therefore
has at least $\phi_0p_v$ edges, and the resulting loopless
multigraph $W$ satisfies
$$
w_v\leq p_v\leq\deg_W(v)
                   \leq cD_0p_v\leq2cD_0w_v.
 \tag{16}
$$
For a cut $A,B$ of the grouped vertices, let $p_A,p_B$ be
their port counts. Its boundary is at least
$c\phi_0\min(p_A,p_B)$, while the smaller output volume is
at most $cD_0\min(p_A,p_B)$. Hence
$\Phi(W)\geq\phi_0/D_0$.
The construction takes $O(N)=O(\sum_vw_v)$ time and records,
and only loopless multigraphs are passed to the path oracle.
Ceilings of the dyadic-rational weights use the declared integer
word bounds.

This proves exactly the weighted-witness interface used here.
It does not assert a loopless construction for an arbitrary
unbalanced vector. Together with Section 4, it removes the need
for a self-loop extension of the balanced-cut or path-oracle sources.

## 6. Consequence for the static sparsifier interface

In van den Brand et al. Algorithm 4, the congestion thresholds depend
on the maximum reported path length, the pruning-volume constant and
$\phi^{-1}$. They do not depend on the running time of the path
oracle. The decomposition and path-oracle replacements above
therefore support separate envelopes
$$
\log\Gamma=O(qr\log(U+2)),\qquad
 \log F=O(U/q+U/r+r^2\log(U+2)+qr\log(U+2)).
 \tag{17}
$$
Here $\Gamma$ bounds output sparsity, path length and congestion
factors; $F$ bounds construction work per actual input-path record.
Fixed powers and polynomial logarithms can be included in these
envelopes.

The literal ambient-embedding length factor remains:
$$
C(\Pi\circ\widehat\Pi)
 \leq \Gamma\,L(\Pi)\bigl(C(\Pi)+\Delta(J)\bigr).
 \tag{18}
$$
It must still be multiplied through the touched-set hierarchy.
Separating (17) does not provide a length-free congestion theorem.
The subsequent static-to-dynamic reduction, degree feedback,
root-pool lifetime accounting and matching composition require
their own proofs; the derivation here addresses the source
parameter, graph-model and stage-count interfaces.

Thus the separated static primitive is derived from the cited
constructive balanced-cut, pruning, constant-expander and dynamic-tree
algorithms, using the explicit replacements above and the full
Algorithm 4 reconstruction in the companion note. No additional
unproved self-loop extension is part of this derived interface.
Its source algorithms remain named mathematical dependencies;
an optimality verifier does not establish their running-time bounds.
