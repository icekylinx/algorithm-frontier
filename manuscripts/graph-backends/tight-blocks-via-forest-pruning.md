# Tight blocks through witness-forest pruning

Status: proved static characterization and preprocessing algorithm. It is
not a dynamic pair-action algorithm and does not improve the general
maximum-matching exponent by itself.

## Setup

Bins D and rows A form an incidence hypergraph: each row r has a nonempty
neighbor set N(r) of at most three bins. Suppose

    h(X)=|X|-|{r:N(r) subseteq X}| >= 1

for every nonempty X subseteq D. A settled zero-debt OAI ledger implies the
stronger inequality L*h(X)>=w(X)>0.

Suppose T is an undirected forest on D with exactly one labeled edge e_r
per row r, whose two distinct endpoints both belong to N(r). Such a forest
is supplied by the global single-free construction: the edge for each
assigned bin joins it to its selected parent and is labeled by its assigned
row. Rerooting only changes the row assignment, not these undirected edges.

## Lemma 1: tight sets are connected in every witness forest

If h(X)=1 then X has |X|-1 captive rows. All their selected edges lie in
T[X]. Since T is acyclic, T[X] has at most |X|-1 edges. Therefore it has
exactly these edges and is a spanning tree on X. In particular every tight
set is connected in T, and every T-edge with both endpoints in X is labeled
by a captive row.

## Lemma 2: deterministic pruning recovers all maximal tight sets

Start with T'=T. Repeatedly remove an edge e_r from T' if at least one bin
in N(r) is outside the current component containing e_r. At termination,
the components of T' are precisely the inclusion-maximal tight sets.

Proof: Maintain that every tight set is connected in T'. Initially this is
Lemma 1. A removed edge e_r cannot be internal to any tight set X: if it
were, Lemma 1 would imply N(r) subseteq X, and connectivity of X in T'
would place all those neighbors in e_r's current component, contradicting
the deletion condition. Thus the invariant survives.

Now let X be a final component. All |X|-1 selected row edges in its tree
have their full neighbor sets inside X, so at least |X|-1 rows are captive.
The global hypothesis h(X)>=1 gives at most |X|-1 captive rows. Thus
h(X)=1. Since every tight set stayed connected throughout, it is contained
in one final component. The final components are therefore maximal.

## Static implementation

Initially check every row edge and queue violations. When an edge is
removed, identify the smaller component by number of abstract bins.
Scan its vertices and physical row incidences. Only rows having an endpoint
in this smaller component can acquire a new violation; queue such rows and
recheck their selected edge's component and all at-most-three neighbors.
Rows whose selected edges have already been removed are ignored.

Each bin lies on the smaller side at most logarithmically many times, and
each of its physical incidences is scanned only on those occasions. The
physical graph's maximum degree is three, so total incidence
scanning is O(N log N), plus ordinary dynamic-forest connectivity and
dictionary factors. An explicit implementation can maintain component
labels by relabeling the smaller component and discover it by simultaneous
traversal from the two endpoints, stopping the search on the larger side
once the smaller side is exhausted; standard forest data structures also
suffice. Bin weights remain fixed during this static preprocessing.

To obtain the **parallel levels** used by the exchange algorithm, use
two deduplicated queues rather than assigning deletion indices. All
initial violations enter the current queue with level 1. During round
j, delete all and only the edges in the current queue. A previously
unmarked surviving row first found to violate after one of these cuts
enters the next queue with level j+1, together with a currently exterior
neighbor. Do not process it during round j. Once the current queue is
empty, swap the queues and advance the round. A violation persists under
later cuts, so no queued edge becomes valid again. Its stored neighbor
is still exterior at the beginning of its deletion round. Consequently
the recorded level is exactly the ordinary synchronous pruning round,
and its witness is outside the component in T_{>=level}.

Only a row incident to both sides of a newly performed cut can acquire
a violation. It has an incidence on the smaller side, so the scans above
find it. For a local query tree, build reverse lists from just that tree's
selected rows, using at most three incidences per row; outside neighbors
are flagged at initialization. Thus unrelated rows incident to a large
physical bin need not be revisited in the pruning stage. Active selected
edge adjacency lists support each cut in constant time, and balanced
traversals of its two sides find and relabel the smaller component in
time proportional to that component. Each original vertex and its
local row-incidence list is charged at most logarithmically many times.
This implements the true parallel levels in O(|C| log |C|) local work
after the query tree C and its selected rows have been enumerated, with
the representation's point-access/dictionary factors added separately.

For the simultaneous searches, interleave individual adjacency-list
entries, not whole vertex expansions. Otherwise one high-degree vertex
on the larger side could cause a large scan before the singleton
smaller side is recognized. Each surviving selected-tree incidence has
an active-list handle, so deleted edges are removed from those traversal
lists immediately. Stop when either traversal exhausts, and finish or
retain only that completed smaller component. In a tree its vertices
and active incidences have comparable total size, so the two interleaved
searches spend O(|smaller component|) work. Scanning that component's
separate ORIGINAL local row-incidence lists then charges each incidence
to its endpoint's component-size halving, at most O(log |C|) times.

## A parallel-round bound

For a current component X, its |X|-1 remaining row edges include at least

    |X|-1-|A(X)| = h(X)-1 >= w(X)/L-1

violating edges. If w(X)>=2L, at least w(X)/(2L) edges can be removed in one
parallel round. The largest resulting component omits at least one
positive-weight vertex per other component, so its weight decreases by at
least w(X)/(2L). Thus after O(L log N) rounds all components have weight
less than 2L. A non-tight component then loses at least one edge per round
and has fewer than 2L vertices, so the entire process terminates within
O(L log N) parallel rounds.

This is a combinatorial round bound; it does not imply small sequential
dynamic update time or a short pair-exposure witness.

## Output-sensitive minimal tight-set queries

If queried bins i,j belong to the same final tree component, initialize X
to their unique tree path. Whenever a selected row-edge newly enters X,
add every neighbor of that row, together with the unique tree paths needed
to join those neighbors to the connected set X. Continue until no new bin
is added. All additions stay in the same final tight component.

Every tight set containing i,j must be tree-connected by Lemma 1 and must
contain every neighbor of each of its internal selected row-edges.
Induction therefore shows that every set produced by the closure is
contained in every possible tight witness. At termination X is connected
and all its |X|-1 internal tree-edges have captive rows. Global sparsity
then implies h(X)=1. Hence this closure is the unique minimal tight set
containing i,j.

An output-sensitive implementation enumerates each newly added tree edge
only once. Root the tree, use LCA information and per-query path-union
jump pointers (or equivalent dynamic-tree path reporting) to skip edges
already in X, and process at most three neighbors for each new row-edge.
The resulting cost is O(|X| polylog N), including the explicit captive-row
and spanning-tree witness. This query result assumes that the global
witness forest and maximal tight partition are already valid and available.

## Dynamic obstacle

Rerooting an existing witness tree preserves all hypotheses and the tight
partition. Expansions and tight contractions have substantial locality,
though swallowed rows can create new physical incidences. A gain removes
two exposed bins. Rows previously selecting edges incident to those bins
may need new endpoint selections, which can create cycles and require
further exchanges. The pruning procedure only deletes edges from a valid
witness forest; it does not provide the forest repair needed after these
operations. Projection peels must also be charged.

The current application obtains that separate maintenance guarantee
from [persistent-integral-ledger-carrier.md](persistent-integral-ledger-carrier.md). It builds pruning data
only inside the small selected query component and discards those data
after the immediate structural action. This static pruning lemma does
not claim that its old levels remain valid through a graph mutation.

## Source relationship

The h(X) definition and zero-debt inequality are from OAI's September 24,
2026 matching preprint, `03-matching-state.tex`. The forest-pruning
characterization and its direct proof above are deductions made in this
research session. No novelty claim relative to the hypergraphic-matroid
literature is made.

https://github.com/openai/math/blob/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026/build/sections/03-matching-state.tex
