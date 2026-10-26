# A standalone dynamic integral-allocation theorem

**Mathematical component of the general-matching candidate.** This note
states the carrier result without assuming the OAI phase algorithm or a
numerical cycle backend. It identifies exactly the representation freedom
needed by the application. It makes no claim of publication priority.

## 1. Model and permitted updates

Let B be a bipartite incidence multigraph with row vertices R and bin
vertices D. Every row has degree at most three. Give each bin a positive
integer weight w_d and fix a positive integer L. An actual allocation x
is nonnegative integral and has row sums

$$
\sum_{e\ni r}x_e=L.
$$

At designated settled states it additionally satisfies

$$
\mathrm{load}_x(d)\le L-w_d.             \tag{1}
$$

The client permits the representation to replace x by any nonnegative
integral allocation with the same row and column margins. A point read
returns the CURRENT represented allocation. Later coordinate updates
are specified relative to this current vector; there is no separate
prescribed vector that must remain coordinatewise equal to x.

A batch consists of q identified final-coordinate changes, incidence
births/deaths or endpoint changes, and any accompanying explicitly
listed vertex changes. It gives a legal nonnegative final vector with
the prescribed row sums once the whole batch has been applied. All
old values needed for the batch are read before normalization. The count
q charges every affected incidence and every explicitly changed vertex
or weight record. Deleting or merging a high-degree bin is not a
unit-cost update when it changes many incidences.

Assume an ordinary finite-word model for IDs and integer values. Let S
bound the current graph size and all integer magnitudes by fixed powers,
and let H be the total charged computation/history size. The bounds
below allow polynomial-logarithmic factors in S+H. In the matching
application all relevant guarded histories are polynomial in S.

## 2. The maintained object

There is a deterministic fully persistent representation with:

1. An acyclic bipartite carrier F containing every positive incidence;
   zero-allocation carrier edges may remain.
2. Exact point access to the current allocation and carrier topology.
3. At every settled state, an implicit row-covering injection mu and
   its inverse, each accessible in polynomial-logarithmic time.
4. At every settled state, an implicit selected bin forest with one
   row-labelled edge per row, one free bin in every component C, and

   $$
w(C)<2L.                            \tag{2}
$$

Initialization takes O((|V(B)|+|E(B)|) polylog(S+H)), including isolated
bins. A q-record batch takes
O((q+1) polylog(S+H)), with space proportional to the charged persistent
work. Forking a stored version takes constant time. These claims concern
the current vector after margin-preserving normalization.

## 3. Sparse normalization proof

Remove carrier edges that disappear or change endpoints and retain
their values for listed reinsertion attempts. Apply every final setting
to the unaffected carrier and to a temporary dictionary before pivoting.
All positive incidences outside the surviving forest are among the
O(q) listed records.

For a pending incidence e=(r,d), link it if its endpoints are in
different trees. Otherwise traverse the unique carrier path from r
to d and orient all incidence edges from row to bin. Let theta be the
minimum allocation among path edges agreeing with the traversal.
This class is nonempty: the path starts at a row and ends at a bin.

Increase x_e by theta, subtract theta on agreeing path edges and add
theta on disagreeing ones. This circulation preserves every row and
column margin and nonnegativity. Cut one minimizing agreeing edge,
whose value is now zero, and link e. Leave other newly zero edges in
the carrier. The operation is valid even when theta=0.

Each pending edge requires only constantly many path/link/cut operations.
An earlier pivot touches only the current forest and its own pending
edge; it cannot change a still-unprocessed pending value. A processed
edge may later be cut at value zero, but need not be processed again.
Thus O(q) pivots suffice independently of the number of coordinates
changed along their implicit paths. Distinct parallel incidences retain
distinct IDs; a parallel pair is a valid two-edge transportation cycle.

## 4. A persistent implementation with worst-case operations

Use the worst-case top-tree implementation of Alstrup, Holm,
de Lichtenberg and Thorup, *Maintaining Information in Fully-Dynamic
Trees with Top Trees*:

<https://arxiv.org/pdf/cs/0310065>.

For a path cluster keep separate minimum/argmin and lazy-add fields
for edges agreeing and disagreeing with the cluster orientation.
Path reversal swaps the classes; joining oriented child paths combines
their corresponding summaries. This gives the signed pivot operations
with constant-size summaries.

Internal connector edges used to reduce the implementation's vertex
degrees are excluded from allocation minima and updates, and have zero
original-edge count. Parent/jump queries skip them to return genuine
carrier incidences. Only original bins participate in component minima.

Simulate all memory of the ordinary worst-case algorithm through a
persistent balanced address-to-word dictionary. Reads are lookups;
writes path-copy dictionary nodes. A version is its dictionary root.
This handles arbitrary pointer fan-in and arbitrary forks, adding a
logarithmic factor. It does not assume that amortized splay costs remain
valid across branches. A representation-changing query on an old version
can use and discard a temporary persistent branch.

Store every row's FULL physical incidence list, including zero
noncarrier incidences, its carrier membership, and all endpoint witnesses
in the same version. Version bin adjacency dictionaries as well when
offering enumeration or pair queries on stored versions. Each row list
has at most three entries, and every listed incidence/topology edit
changes only constantly many persistent dictionary records. Store the
minimum bin ID in each carrier component. A parent query uses that
component's canonical minimum-bin root. Old queries therefore do not
accidentally read a new physical neighborhood array.

Versioning only positive or carrier incidences would be insufficient:
deleting a zero noncarrier incidence can change a pair's Hall obstruction
without changing its allocation or carrier. The sparse batch cost above
includes these physical-neighborhood records.

## 5. Small selected components

Condition (1) forces every row to have at least two positive incidences:
a single positive incidence would put its full L units in one bin.
Since row degree is at most three, its carrier degree is two or three.

Root each carrier component at a bin. Keep both incidences at a
degree-two row. At a degree-three row keep its two child incidences and
omit its parent. Suppress row vertices to obtain a bin forest with one
edge per row.

Every selected component has at most one internal row with allocation
outside the component: the degree-three row at its top. All lower
internal rows keep every incidence within the selected component.
The top row exports less than L, since at least one retained child
incidence is positive. If in>=0 is allocation from external rows and
out<L is this export, then

$$
\mathrm{load}(C)=L(|C|-1)-\mathrm{out}
                                      +\mathrm{in}.
$$

Summing (1) and rearranging proves

$$
w(C)\le L+\mathrm{out}
                                  -\mathrm{in}<2L.
$$

This proof permits zero carrier edges. Requiring the carrier to be
exactly the positive support would unnecessarily expose potentially
large support recourse.

## 6. The canonical injection

Assign a degree-two row to its sole child. Assign a degree-three row
to one deterministically chosen child, for example the child incidence
with smaller edge ID. Only a bin's parent row can choose it, so the
assignment is injective. Its inverse follows from the bin's parent
and that row's choice, using only constantly many tree and incidence
queries.

A bin-top selected component is rooted at that bin. A component with
a degree-three top row is rooted at its unchosen child. The row
assignment is the orientation away from this free root. There is
exactly one unassigned bin per selected component.

Changing the carrier can change many of these canonical assignments
implicitly. The theorem guarantees forward and inverse point access,
not an explicit short list of all changed assignment values. A client
that requires such a list has a different interface.

## 7. Pair-query consequence with bounded incidence volume

Suppose additionally that the number of physical incidences at a bin
is O(w_d), as in the subcubic odd-bin application. A selected component
can then be enumerated in O(L polylog(S+H)) time, including all alternatives
of its rows. The deterministic pruning/exchange lemma in
[static-pair-exchange.md](../graph-backends/static-pair-exchange.md) frees any jointly freeable pair by changing
rows in at most two original selected components. Pair queries refer
to two distinct bins in one settled version.

If a pair is not jointly freeable, the independent output-sensitive
detector in [deterministic-local-tight-discovery.md](../graph-backends/deterministic-local-tight-discovery.md) returns its minimal
tight witness in O((|X|+1) polylog(S+H)) work. The detector queries bins
through their assigned row and therefore need not scan a heavy bin's
physical interior. Its output lists abstract bin IDs and captive rows;
it does not enumerate every physical member of a weighted bin. Run that
detector first, so tight contractions retain
their arity charge while successful pair actions pay O(L polylog).

The pair-freeing assignment is a temporary valid injection. It is not
required to arise as the orientation of another feasible carrier basis.
An application may consume it during a frozen transaction and publish
the next settled carrier's canonical injection afterward.

## 8. Exact scope

The theorem is an independent data-structural and combinatorial component.
Its integration into maximum matching still requires the phase's sparse
batch accounting, valid factor-critical operations, numerical progress,
and exact output materialization. Those obligations are supplied by the
separate integrated candidate and its stated imports.

The result would not apply to a client demanding coordinatewise equality
with a separately maintained shadow vector, explicit enumeration of
every support transition, or an explicit list of every canonical
assignment change. None of these stronger interfaces is asserted here.
