# Deterministic local tight-set discovery from directed 1-edge-out search

**Status:** A concrete reduction to a published deterministic primitive. This removes the randomness in the OAI manuscript's *small tight-set discovery* step. It does not by itself derandomize joint freeing, the numerical backend, or the whole matching algorithm.

## Published primitive

Shiri Chechik, Thomas Dueholm Hansen, Giuseppe F. Italiano, Veronika Loitzenbauer, and Nikos Parotsidis, *Faster Algorithms for Computing Maximal 2-Connected Subgraphs in Sparse Directed Graphs*, arXiv:1705.10709v1, 30 May 2017, Section 3.1, Lemma 3.5 and Procedure `1EdgeOut` (PDF pages 6–11).

Primary source: <https://arxiv.org/pdf/1705.10709>.

The deterministic primitive takes a digraph, seed `u`, and budget `Delta`. In `O(Delta)` time it either returns a set containing `u` with at most one outgoing edge and at most `2 Delta` induced edges, or correctly certifies that no such component with at most `Delta` induced edges exists. The paper expressly notes that exponential search in `Delta` makes discovery output-sensitive.

The mechanism is a truncated DFS, followed by reversal of the DFS heavy path and a second bounded search. This chooses an escaping path deterministically, replacing the random endpoint in the OAI local-cut procedure. It is not a claim that arbitrary local directed cuts admit near-linear deterministic search for unrestricted cut size.

## Matching-state assumptions

Let `D` be the bins, `A` the rows, and `mu:A -> D` an injection using a row incidence. Each row has at most three incidences. For nonempty `X subset D`, put

\[
A(X)=\{r:N(r)\subseteq X\},\qquad h(X)=|X|-|A(X)|.
\]

Assume the settled state has `h(X)>=1`. Assume every tight set, meaning `h(X)=1`, has `|X|<=L`; OAI in fact supplies the stronger physical-weight bound `w(X)<=L`.

Given distinct bins `i,j`, OAI's Hall argument establishes the alternative: either they can be freed jointly, or there is a unique inclusion-minimal tight set `X` containing both. The job here is to distinguish the alternatives and return the latter set when it exists.

## Split digraph

Introduce a query source `q` and a real sink `t`. Each bin has vertices `d_in,d_out` and one directed split edge `d_in -> d_out`. Add two parallel arcs for each of the following:

* `q -> i_in` and `q -> j_in`;
* `d_out -> e_in` for every incidence from the row assigned to `d` to a neighboring bin `e`;
* `d_out -> t` for each free bin `d`.

Thus capacity-two arcs in the manuscript become two unit arcs. Each
original output has at most six outgoing arcs; each input has one.
We retain the individual arc identifiers. The source's proof uses
only DFS tree edges, counts of traversed arc IDs, unique outgoing
edge cuts, and reversal of the individual arcs on one simple tree
path. None of its Lemmas 3.1--3.5 assumes distinct endpoint pairs.
Parallel arcs are examined and reversed separately; an opposite
arc already present is not canceled or identified with the newly
reversed arc. Thus the same proof applies to this directed
multigraph. No subdivision gadget or simplicity assumption is
needed.

### The local adjacency interface

The graph is generated through OUTGOING adjacency only. At a bin
output, query its inverse assignment and then the assigned row's
at-most-three physical incidences; do not enumerate all rows incident
to the bin. Each input has only its split arc. The source and padding
vertices have constant outgoing degree. A bin input or the real sink
may have arbitrarily high indegree, which this interface never scans.

For the second search, keep the first search's heavy path in a
temporary overlay: suppress each reversed arc ID in its original
outgoing list and add that ID, with reversed orientation, to its new
tail's overlay list. A simple path supplies at most one added outgoing
arc at each vertex. The residual outgoing degree is therefore still
constant. Creating and discarding the overlay takes linear work in
the traversed path length. Dictionaries and visited sets are initialized
only for visited IDs, not by clearing an array over all current bins.
Assignment and row-neighborhood accesses use the same frozen settled
version throughout the trial.

The real sink is reachable from `q`: otherwise the nonempty reachable bins would all be assigned and their assigned rows would have all their neighbors inside the reachable set, contradicting `h>=1`.

For a tight set `X` containing `i,j`, exactly `|X|-1` bins of `X` are occupied by captive rows; let `b` be its remaining bin. The vertex set

\[
S_X=\{q\}\cup\{d_{\rm in}:d\in X\}
       \cup\{d_{\rm out}:d\in X\setminus\{b\}\}
\]

has exactly one outgoing arc, the split edge of `b`. Its induced edges number at most

\[
4+(|X|-1)+6(|X|-1)\le 7|X|+4.
\]

Any minimal one-edge-out component contained in this set has no greater volume. Therefore the published primitive must discover a source-side one-cut once `Delta >= 7|X|+4`.

## Preventing a false return that contains the real sink

A generic one-edge-out procedure has no designated forbidden sink. If run on the unmodified split network, it might return an exhausted region containing `t`; that output is not a tight-set certificate.

Fix the largest trial budget `Delta_max`, at most a fixed constant times `L`. Append a directed chain

\[
t=z_0\longrightarrow z_1\longrightarrow\cdots\longrightarrow z_T
\]

with **two parallel arcs per link**, where `T > 2 Delta_max + 1`. Generate this chain lazily, so a trial costs only its exploration budget.

Every vertex set with at most one outgoing arc that contains `t` must contain every chain vertex. It consequently has at least `2T > 2 Delta_max` induced edges. No returned set of the published size guarantee can contain `t`.
The padding also makes at least `2 Delta+1` arcs reachable from `q`,
and in particular satisfies the source's stated `Delta < m/2`
premise, so the first DFS does not take the exhausted-search branch. The
published primitive itself permits that branch; padding is needed
here to exclude a sink-containing answer. It leaves all source-side
cuts that avoid `t` unchanged. A padding vertex is just an index
in `[0,T]` with a formula for its at-most-two outgoing arcs. Allocating
the entire chain at every doubling trial would defeat output
sensitivity and is not part of the algorithm.

## Projection and exact refinement

Let `S` be a returned one-edge-out set containing `q`. Explicitly replace
it by the vertices reachable from `q` in the ORIGINAL digraph induced by
`S`, using the unmodified arc orientations. There is no original arc
from that reachable subset to its complement inside `S`, so this
replacement cannot increase the number of outgoing arcs or the induced
volume. The two truncated traversals explicitly discover at most
`2 Delta+2` and `Delta+2` vertices, respectively: every newly discovered
vertex other than the source requires a newly traversed tree arc.
Thus the returned vertex list has O(Delta) size even before the
original-graph reachability replacement, independently of its
possibly large incoming boundary. Its constant outgoing degree makes
this extra search cost O(Delta). We henceforth call
the resulting reachable set `S`. This step avoids relying on an
implementation returning an inclusion-minimal set or on reachability
in a temporarily reversed DFS graph.

1. It avoids `t`, by padding.
2. No doubled arc crosses its boundary, since both parallel arcs would cross. Thus `i_in,j_in` belong to `S`.
3. The boundary cannot have zero edges: `q` reaches `t` in the original graph. Its unique edge must therefore be a bin split edge.
4. Every included output has its corresponding input inside, because
   the split edge is its only incoming original arc and the set is
   now explicitly reachable in the original induced graph.
5. Let `X'={d:d_in in S}`. Every bin of `X'` except the unique crossing-split bin has its output inside. Those outputs cannot be free, and their assigned rows have all neighbors inside `X'`. They supply `|X'|-1` distinct captive rows. Strict Hall supplies the reverse inequality. Consequently `h(X')=1` and `i,j in X'`.

The following explicit refinement finds the unique minimal tight
`X subset X'` containing the pair in O(|X'|) work, up to dictionary
factors. Enumerate the captive rows of X' through the assigned rows of
its bins, checking each row's at-most-three neighbors. There are exactly
|X'|-1 captive rows, and their current assignment occupies that many
bins of X'. Treat its one remaining bin b as free in this restricted
instance, even if b has an incoming noncaptive assignment in the full
instance.

Build the same split digraph on X', using only these captive rows and
the single free bin b. Its size is O(|X'|). The source reaches its sink:
otherwise a nonempty closed reachable set of assigned bins would violate
strict Hall in the restricted instance. That instance inherits strict
Hall, because for Y contained in X', its captive rows with neighborhood
inside Y are precisely the original rows with neighborhood inside Y.
The one free-bin split edge bounds maximum source-to-sink flow by one,
so one path augmentation produces a maximum integral flow. Obtain its
residual-reachable source side.

Every doubled arc retains positive forward residual capacity after a
unit flow. Thus both query inputs belong to the source side, and the
unique original outgoing capacity is one bin split edge. If an output
is reached by a reverse arc, its positive outgoing flow implies positive
flow on its own split edge; that edge's reverse residual arc reaches
the corresponding input. The same projection argument therefore makes
the input-bin set a tight witness containing i,j.

Residual reachability gives the inclusion-smallest source-side minimum
cut. Conversely each tight Y contained in X' and containing i,j induces
the one-cut set constructed above, using the restricted injection.
Therefore the returned bins are contained in every such Y and form the
inclusion-minimal tight witness. This is also the full-instance minimal
witness: tight sets containing the pair are closed under intersection.
Indeed h is submodular and strict Hall holds on their nonempty
intersection, forcing the union and intersection of two such tight sets
to be tight. Hence the global minimal witness lies in the already
discovered tight X'.

There is a useful size accounting detail: a reachable component with `k` induced arcs has at most `k+1` vertices. Therefore projecting and refining a returned component costs `O(Delta)`, even though the primitive's guarantee counts edges rather than vertices.

## Deterministic doubling and its bound

Run budgets `Delta=1,2,4,...` up to the first power of two at least `7L+4`, stopping at the first returned set. Use fresh temporary DFS and reversal overlays, so the represented matching state is not mutated by trials.

* If the pair is tight, a trial must return by the first budget at least `7|X|+4`. The total cost, including all failed budgets and exact refinement, is `O(|X|+1)` up to dictionary factors.
* If no trial returns, there is no tight set containing the pair, because every such set has at most `L` bins. The total cost is `O(L)` and the conclusion is exact.

If an earlier trial happens to find a larger tight witness before the threshold for the minimal set, its volume is still `O(Delta)=O(|X|)` at that stopping time, so output sensitivity remains valid. Unlike a randomized cap, failed trials cannot falsely declare a tight pair freeable.

### Composed structural cost

Run this detector before enumerating a selected component. On a tight
answer, its output consists of abstract bin IDs, captive row IDs, and
their bounded physical incidence witnesses. It does not enumerate the
physical interior or the full incoming incidence list of a heavy bin.
The work is O((|X|+1) polylog N), irrespective of w(X). Because the
queried bins are distinct, |X|>=2 and this is also
O((|X|-1) polylog N), which is the contraction-arity charge.
Physical endpoint retargeting at the contraction is a separate
small-to-large charge of the structural representation.

On a certified freeable answer, the failed doubling trials cost
O(L polylog N). The balanced-tree exchange then costs another
O(L polylog N) and is consumed immediately by one gain. Thus a
structural transcript with tight witnesses X_1,...,X_c and G such
gain actions has pair work
\[
 O\!\left(
   \left[\sum_{\nu=1}^{c}(|X_\nu|-1)+LG\right]
   \operatorname{polylog}N
 \right).
\]
This count does not assume that every failed small-budget trial
corresponds to a distinct structural event. All trials of one query
are already summed geometrically. It also does not claim this
transcript bound for arbitrary repeated read-only freeability queries;
the immediate gain is the required client-side charging event.

## Consequence and remaining work

The local *decision / tight witness* interface can be made deterministic with the same polynomial exponent and the same continued-contraction charging as the OAI randomized routine. At most a constant/logarithmic factor is changed. This is a substantive local derandomization, but not yet a new general matching exponent.

When a pair is certified freeable, this cut detector alone does not
produce the two paths to actual free bins: its heavy path may terminate
at an arbitrary vertex outside a small cut. The separate construction
in `balanced_forest_pair_oracle.md` and `static_pair_exchange.md` supplies
the reassignment on the O(L)-volume selected components maintained by
`persistent_integral_ledger_carrier.md`.
