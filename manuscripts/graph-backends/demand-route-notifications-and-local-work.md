# Demand-route notifications and local correction work

**Constructive interface lemma, 24 October 2026.** This note examines
one specific dependency of the proposed 14/15 backend: whether the
large `gamma^(O(K^2))` cost of changing spanner demand routes must also
multiply the recursive updater. It does not independently certify the
whole matching algorithm or implement the data structure. The main
candidate is [the degree-three reset construction](distance-degree-reset-candidate.md).

**Lemma.** With the explicit route-record instrumentation in Section
4 below, demand-route maintenance costs a fixed polynomial in the
local source parameters times `gamma^(O(K^2))`, and produces no
recursive input edit unless the underlying selected core edge itself
changes. No demand-route event by itself changes a recursive input edge.
The small selected-edge transcript does not suffice to maintain local
correction candidates, and the set `D` in the spanner theorem does not
by itself enumerate those candidates. Treating either statement as a
complete implementation would leave a gap. The underlying constructive
batching reduction supplies the missing enumeration at the larger
LOCAL cost, without changing the selected graph or its transcript.

## 1. Sources and the exact distinction

The primary sources used for this interface lemma are:

* KMPG, [arXiv:2311.06402v1](https://arxiv.org/abs/2311.06402v1),
  Theorem 3.7, Algorithms 2--4, Claim 3.18, and the proof of Theorem
  3.1 on printed page 29.
* DO26, [arXiv:2609.23852v1](https://arxiv.org/abs/2609.23852v1),
  Sections 4.1 and 4.3, especially the gradient discussion and the
  proof of Theorem 4.5.
* van den Brand et al.,
  [arXiv:2309.16629v1](https://arxiv.org/abs/2309.16629v1),
  Theorems 8.1--8.2 and the proof of Lemma 5.17.
* Chen et al., [arXiv:2203.00671](https://arxiv.org/pdf/2203.00671),
  Section 5.1, Algorithm 1, and Claims 5.7--5.9. The deterministic
  paper explicitly applies this batching reduction to its deterministic
  static sparsification primitive. No randomized primitive is used here.

Use different symbols for three objects:

1. `C_i`: one current positive core graph, with one edge ID `(i,e)`
   for the appropriate original parent edge `e`;
2. `H_i subset C_i`: selected core edges retained by the spanner;
3. `Pi_i(f)`: a route in `H_i` for an INPUT DEMAND edge `f` of `C_i`.

The recursive graph `S` consists of the selected edges in the `H_i`,
after the stated root-alias gradient correction and identification.
It is not a graph whose edges are the demand routes `Pi_i(f)`.

This is a construction-level fact, not an interpretation inferred from
distance approximation. Theorem 3.7 explicitly returns a subgraph and
its selected update transcript. In the underlying batching algorithm,
line 15 inserts original input edge IDs corresponding to selected
auxiliary edges; line 19 separately constructs demand routes. Thus a
selected edge's physical origin is its own core edge ID, even if the
embedding routine also supplies a nonidentity route for that edge as
an input demand. Internal membership in a batching level is not part
of the selected edge's physical provenance.

Theorem 8.2's set `D` has a different purpose: it identifies retained
edges which may have acquired new users under the demand embedding.
Its size and the demand congestion can contain the larger
`gamma^(O(K^2))` factor. They are not bounds on changes to the
selected edge's original ID, length, or endpoints.

## 2. What a recursive edge actually depends on

Fix one source period. Let `F_i` be a stable core forest and fix the
potential `p_i` for the entire period so that

    g(e) + p_i(u) - p_i(v) = 0

on every surviving forest edge `e=(u,v)`. Edges whose input price or
gradient changes are deleted and reinserted. New input edges never
join these decremental forests. The surviving forest identities and
the frozen potential therefore remain compatible.

For a selected core edge `(i,e)`, with original orientation
`e=(u,v)` and current roots `a=r_i(u)`, `b=r_i(v)`, the external
selected-edge record stores

    provenance = (source period, i, parent edge lifetime, a, b),
    length     = the fixed integral core stretch label for (i,e),
    gradient   = g(e)+p_i(u)-p_i(v)-p_i(a)+p_i(b).          (1)

The gradient in (1) is exactly the gradient of the parent walk

    F_i[a,u] + e + F_i[v,b].                              (2)

It does not contain `Pi_i`, a demand count, an inverse-route load, or
the batching level that currently selects `(i,e)`. The length is the
stable core overestimate; it does not change when a demand is rerouted.
The binary port layer multiplies this length and gradient by its one
fixed scale `H`, which also does not change within the period.

### No invisible change of a surviving root leg

Suppose the parent edge lifetime, core index, and root IDs in (1)
are unchanged through a settled source update. A leg in (2) can change
only if a forest edge on that leg is removed. But then its endpoint
would be separated from its old root. Since `F_i` only loses edges,
it cannot reconnect by a different path while keeping the same root.
The selected core endpoint must consequently change. That event is a
native core split, and any moved retained incidence is included in the
fully encoded selected transcript.

Thus an unchanged selected record has an unchanged physical walk.
This uses root identities in the IMMEDIATE parent graph. Distinct
immediate vertices must remain distinct even if their eventual images
in a higher ancestor happen to coincide.

A parent input gradient change cannot silently alter (1): it is an
input edge replacement. If it was a forest edge, deleting it first
cuts the forest and promotes the affected endpoints. A temporarily
isolated parent vertex retains the same source generation and frozen
potential until the period ends. A full potential renewal occurs only
at a complete source restart, whose initialization and retirement are
already charged.

### A precise selected-edge replacement rule

Replace the exposed child edge if any field in its provenance or either
numeric label changes. This includes changes with identical endpoint
coordinates or identical numeric values. Conversely, changing only an
internal spanner-level membership or a demand route does not replace
the record. Multiple internal selections of the same core ID may be
kept by a reference count, or the source's already bounded ordinary
edge transcript may be used directly. Parallel core IDs are never
silently coalesced.

## 3. Why the older hidden-stability construction forwards D

There is a superficially contrary source passage which must not be
omitted from the argument. The proof of Lemma 5.17 in
arXiv:2309.16629 explicitly appends `D` to the recursive update batch.
The older CKL22 Algorithm 4 makes the same forced-reinsertion choice.

Those algorithms propagate a hidden width defined from the SUM of
widths of demands currently routed through a retained edge. A new
demand user can increase that width without changing the retained
edge's metric or physical identity. Forced reinsertion makes their
hidden-stability predicate true after such an increase.

The present backend has no recursively propagated demand-width state.
Its recursive oracle is required to approximate the best circulation
for the current explicit lengths and gradients, for every such
circulation and under adaptive edits. Its child input is precisely
the explicit port-expanded `S` graph. The priced client stores primal
motion in the exposed physical forest, not in a sum over spanner-demand
users. It therefore has no hidden-width predicate that would require
these artificial reinsertion events.

This is why the older forced reinsertion cannot simply be imported,
and also why omitting it here is legitimate. A future implementation
that reintroduces a demand-dependent child weight or a hidden-stable
flow oracle would have to revisit the bound: it could no longer use
this locality conclusion unchanged.

## 4. Constructive enumeration of changed local correction routes

### 4.1 What is insufficient

It is not enough to receive `D subset E(H)` and declare all affected
correction candidates known. A newly routed demand may use an edge
of `D` which was absent from its old route; an old inverse list at that
edge does not identify the new user. A full scan of all current demands
after every update would not fit the claimed local time.

DO26's proof of Theorem 4.5 invokes explicit embedding maintenance.
The following instrumentation identifies the concrete route records
and its cost, instead of deriving that assertion from `D` alone.

### 4.2 Native route records

In CKL22 Section 5.1 the global embedding is called implicit because
for each demand it uses the largest batching level `j` currently
having a record `Pi_j(f)`. It is not necessary to treat an arbitrary
unreported change of a compressed mapping as one constant-time event.
Algorithm 1 explicitly creates a new `Pi_j(f)` for each affected
input demand in lines 16--19, and clears the domains of higher-level
maps in lines 5--6. The deterministic static replacement in
arXiv:2309.16629 changes the local path/congestion bounds, not these
owner IDs or the batching rule.

For every route-record birth store:

* its input demand lifetime, batching level, and fresh record lifetime;
* its explicit oriented edge-ID array, flattened at its birth;
* inverse incidence entries at the vertices and edges occurring in that
  array, with handles allowing deletion, including the demand endpoints
  and the base vertex of an empty loop route;
* its local correction candidate, when it is the highest active owner
  for its demand.

Keep the route records belonging to every currently live batching
level, including inactive records below a higher owner. A vertex split
or an edge deletion updates the explicitly incident records; a stored
lower-level record may temporarily be a broken path, just as in the
source construction. Its remaining incidence pieces can be kept and
indexed. An update only removes or separates pieces of a record;
it does not introduce an uncharged long replacement path.

Maintain the highest active owner for each demand by its finite
level-indexed record list. On a record birth, replacement, or clear,
invalidate the old candidate before retiring its metadata. A clear
enumerates its actual domain records and removes their inverse
entries; each such retirement is charged to that record's earlier
birth. Equal old and new edge arrays do not permit lifetime reuse
without this invalidation. All candidate evaluation waits until the
whole source transaction settles.

For an affected-set computation at a level `j`, enumerate inverse
vertex lists of the touched set and retain only records which are
the highest owner below `j`. Duplicate demand IDs are removed with a
timestamp. Hence the affected-set loop does not scan unrelated demands.
Scanning all live levels gives at worst an additional factor `K`.
An empty route remains registered at its base vertex. A native split
which turns an old input loop into a nonloop demand therefore finds
that record through the touched-vertex inventory; it is not lost
because its edge array was empty.

### 4.3 Quantitative accounting

Let `n_c,m_c,Delta_c` denote one positive core-spanner instance. Use

    rho = gamma^(O(K))
    Xi  = Delta_c gamma^(O(K^2))

as bounds on a route's explicit cardinality and the number of route
records of one level incident at a vertex, respectively. These bounds
apply at record creation. Subsequent deletions and splits cannot
increase a record's cardinality or the per-new-vertex congestion.
Keeping all levels costs a further factor polynomial in `K`.

At a level-`j` rebuild, the touched set has size
`O(n_c^(1-(j-1)/K))`. Its inverse lists therefore enumerate at most
that size times `poly(K) Xi` demand records. Flattening and indexing
each new record costs `O(rho)` plus dictionary factors. The rebuild
interval is `Theta(n_c^(1-j/K))`; the ratio of the two sizes is
`O(n_c^(1/K))`. Summing over levels and charging every record clear
to its creation gives a total local allowance of the form

    (m_c + t n_c^(1/K))
      poly(K,log m_c,log L) Delta_c gamma^(O(K^2))          (3)

through `t` elementary source updates, with initialization and final
record retirement included. An encoded vertex split can additionally
scan its moved incidence list; this only contributes the already
allowed fixed powers of `Delta_c`. The deterministic spanner's own
static work is charged separately by its stated bound and has the
same larger exponential form.

The same instrumentation can be applied to each background copy of
the deamortized selected-spanner construction used in KMPG Theorem
3.7. It does not change when a selected graph is committed. Activating
a completed copy or clearing an old one enumerates only route records
whose construction or retirement has already been charged. We retain
KMPG's selected-degree and selected-transcript guarantees; we do not
replace its selected updater by an unproved amortized degree-control
routine.

In the present application `Delta_c=O(k)` up to the declared local
factors, and the number of core graphs and length buckets is
polynomial in the master bit parameter. Composing (3) with the source
core-edit transcript, evaluating each correction from its explicit
array, and maintaining its priority key therefore fit

    W = k^O(1) R^O(1) gamma^(O(K^2)) poly(U).              (4)

Flattening contributes `gamma^(O(K))`, not a new recursive power of
`gamma^(O(K^2))`. Any fixed polynomial number of such local scans
only changes the absolute constants in (4).

### 4.4 Price changes and changed physical forest legs

Route-record replacement is not the only notification. An actual
core-edge length or gradient replacement must also invalidate every
local correction using that edge, even when its route's edge-ID
sequence would otherwise be unchanged. Use the edge inverse lists
for this purpose. The demand edge's own key is separately registered.
All label replacements are modeled by deletion and fresh insertion,
so an old record cannot silently read a new label.

For a direct, conservative implementation one may additionally store
the LOCAL physical expansion of every current correction record:
expand each core edge into its central parent edge and two `F_i`
root legs, with the stipulated fundamental-path convention for a
core loop. Store inverse entries by the immediate parent edge
lifetime and forest index. These are ordinary metadata arrays, not
new copies in the exported forest. Their length is `O(k rho)` up to
the local degree and logarithmic factors because a stable core-forest
component has `O(k)` parent incidences when the parent degree is three.

A cut of an `F_i` edge invalidates all entries at that old edge before
its metadata expires. It can affect root legs of only `O(k)` core
edge IDs incident to the old forest component. Each such ID is either
the demand itself or is used by at most `poly(K) Xi` retained route
records. Thus at most

    poly(K) k (1+Xi)

records need regeneration; recomputing each in `O(k rho)` time remains
within the fixed-power local envelope (4). If the change is an input
length or gradient replacement, invalidate its central occurrences
as well as all its forest-leg occurrences. There are only the declared
polylogarithmic number of core forests. This also covers an induced
core cut during degree feedback.

No path can acquire an unreported new root leg while avoiding every
changed forest edge: Section 2's decremental-forest argument rules
that out. An old-to-new component split can therefore be processed
from the old inverse lists, without scanning unrelated corrections.
Keep old arrays and physical lifetime metadata until notifications
and numerical retirements have been consumed, then regenerate dirty
records using the settled forests. Repeated invalidations in one
transaction can be deduplicated.

This stronger physical index is optional if the implementation proves
that its core-label notifications and route notifications already
suffice for every stored key. It supplies a simple explicit upper
bound here and avoids relying on a silent equivalence between stored
core scores and changing physical path records. Its initialization,
space, and disposal acquire only another fixed power of `k` and
`gamma^(O(K))`, still inside `m W` and the `k W` restart charge.
The resulting rescoring is local. Actual selected core/end-point
replacements continue to be emitted separately through the smaller
`R` transcript.

## 5. Correction candidates do not create demand-specific forests

For a demand edge `f`, the local correction is the signed circulation
`f-Pi_i(f)` in its core graph. Evaluate it after net cancellation by
CORE EDGE ID, and decompose it into simple core cycles if necessary.
At least one nonzero component has at least the ratio of the whole
net circulation. A positive core loop uses its fundamental parent
cycle, with common root legs canceled inside that one forest.

The selected component's numerator is computed with the same frozen
core gauge as all its edges. Potential terms telescope. Its positive
core length is an upper bound for the literal parent lift supplied by
the core forests. This is the already proved raw-lift interface; it
does not use the demand congestion as an occurrence bound.

Maintain one ordinary local copy of each stable `F_i` for such local
candidates. A route of at most `rho` core edges is returned as explicit
central edges and paths in these copies. Do not allocate a new family
of parent trees for every demand, every route, or every correction
candidate. Demand records and candidate keys are local ordinary
metadata, not vertices of the exposed occurrence forest and not
vertices of the recursive graph.
Their inverse indexes are separate from the priced client's lists of
exposed physical edge copies. They carry no signed or absolute primal
motion counter, so their creation, invalidation, or deletion is not a
numerical forest-retirement event.

Consequently reembedding a demand can change a local candidate's
answer and priority key while making ZERO changes to the exposed
forest. A query can return a different existing path list. The
transaction/certificate rule forbids subsequently changing its edge
or path metadata before the direction has been applied or discarded.

The local metadata's space and eventual cleanup belong to `m W` and
the corresponding `k W` restart allowance. The recursive graph's size
continues to count only the selected port graph and its resident
native history. This separation is necessary for the shrinking
recurrence.

## 6. Exhaustive classes of possible propagation

| Event | Local consequence | Recursive consequence |
|---|---|---|
| Only `Pi_i(f)` changes | Retire/rebuild affected correction records under Section 4 | None |
| A retained core ID enters or leaves `H_i` | Update source metadata and correction records | Birth/death of that selected edge and its port record |
| A core forest is cut | Native core split, local route repairs, pool cuts/joins | Only moved retained incidences, encoded by the source's selected degree bound |
| A parent edge length or gradient changes | Delete/reinsert that parent lifetime; invalidate local users | Its selected copies and endpoint changes already in the selected transcript |
| A selected core edge gets a new original ID or core index | Retire old provenance even if labels agree | Explicit selected replacement |
| A batching map is cleared or rebuilt but the selected union is unchanged | Candidate ownership and route metadata change | None |
| A frozen potential is renewed | Complete source-period rebuild and old-record retirement | Initialization of the rebuilt child, paid in the restart recurrence |
| A physical parent lifetime ends | Flush real pools, retain counted tombstones, suppress the inactive null fiber | Existing charged incidence/lifetime edits; no demand-based new fiber |

KMPG Claim 3.18 bounds stable core-forest edits and selected native
edits without a demand-congestion factor. Its proof of Theorem 3.1
then multiplies by the selected degree to encode moved retained
incidences. The separate shortest-pivot forest can have `O~(k)`
changes and remains local. Adding the correction instrumentation
does not change source degree feedback: it depends on selected
incidences, not on correction keys or demand loads.

The parent physical pool changes caused by a stable core cut cost
the declared small local pool factor times the CHILD OCCURRENCE
bound. A demand reroute does not cut these pools. Thus no product
`gamma^(O(K^2)) * G_child` is introduced by demand-specific tree
copies, and no product `gamma^(O(K^2)) * T_child` is introduced by
demand-specific child edits.

## 7. A concrete diagnostic example

Let the retained graph be the square with paths `a-b-c` and `a-d-c`,
and let a nonselected demand be `f=(a,c)`. Set the gradients of
`a-b,b-c,f` to zero and those of `a-d,d-c`, oriented from `a` to
`c`, to one. All lengths may be one.

Changing the demand route from `a-b-c` to `a-d-c` changes its
correction numerator from zero to minus two while leaving every
selected edge, selected length, selected gradient, and selected
physical representation unchanged. The set `D` can contain `a-d`
and `d-c` because they acquired this demand. It does not describe
an intrinsic change of either selected edge.

This example detects two invalid implementations: one that forgets
to update the local correction, and one that unnecessarily interprets
the new demand as a child edge replacement. Section 4 fixes the first;
the explicit selected provenance in Section 2 avoids the second.

## 8. Consequence for the recurrence

The demand-route construction introduces no propagated
`gamma^(O(K^2))` term in the degree-reset backend. This conclusion
depends on four explicit choices:
selected edges remain actual core IDs; gauges and stretch labels are
frozen for their declared lifetimes; correction routes are enumerated
through the constructive per-level records; and no demand-specific
physical forest is exported. The local cost (4) must include those
enumerations and their complete retirement.

With those choices, the large factor is additive local work in the
recurrence. The smaller selected recourse, selected degree, and stable
core-forest transcript determine the factor that multiplies recursive
updates and occurrence copies. This is a proof-interface conclusion,
not an experimental or external correctness certificate.
