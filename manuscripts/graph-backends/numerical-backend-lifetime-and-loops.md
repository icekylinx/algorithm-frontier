# Numerical lifetime discipline and a loop wrapper for flat cycle oracles

**Research interface lemma, 24 October 2026.** This note specifies the
common interface between the deterministic flat-cycle constructions and
the numerical client in OAI Section 5. It applies to the
[constant-degree Steiner bridge](constant-degree-steiner-bridge.md)
and the [distance-based construction](distance-backend-general-matching-integration.md).
It supplies explicit implementation conditions; it does not enlarge
any cited routing, distance, or spanner theorem.

The numerical source is
[OAI, Almost-Linear-Time Maximum-Cardinality Matching in Sparse General
Graphs, September 2026, Section 5](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026),
especially the exact-value and drift-detection subsections.

## 1. Every exposed copy belongs to its physical coordinate

A nonnull edge of the exposed forest has an immutable physical edge
identity and endpoint correspondence during its lifetime. A physical
edge belonging to a numerical variable also identifies that variable.
A priced port connector is a genuine graph edge with its prescribed
length, but carries no primal-variable counter. A true null forest
edge has no physical edge and contributes neither gradient nor
physical traversal length.

For every physical edge maintain its complete list of current exposed
copies. In particular, **an unused path-pool copy or an unassigned
root-pool copy remains on this list**. Dormancy changes its role in
representing a child occurrence; it does not remove the copy from the
numerical state. All occurrence and per-edge-copy bounds include these
copies, even when they lie in isolated forest components.

For each copy $`c`$ of a real numerical coordinate $`e`$, keep two
different counters:

```math
h_c=\text{signed physical increment accumulated in that copy},
 \qquad
 A_c=\text{absolute motion since its last coordinate reset or birth}.
```

The sign of $`h_c`$ uses the fixed physical orientation, independently
of the current rooting of the forest. Maintain

```math
f_e=b_e+\sum_{c\mapsto e}h_c.
 \tag{1}
```

Every exact point read or setting uses this full sum. Every coordinate
anchor resets the absolute counter of **every** current copy, including
dormant copies, and resets the coordinate's absolute-motion bucket.
Every price/threshold sweep likewise visits the full physical-copy
list. A dormant copy cannot retain an obsolete threshold or old
gradient after the coordinate's price transaction has settled.

The list size is bounded by the same occurrence argument used for the
exposed forest. These requirements cost the already charged
$`O(D)`$ point operations per coordinate sweep when there are at most
$`D`$ current copies. They introduce no scan of unrelated coordinates.

## 2. Retirement and refresh ordering

A representation transaction consists of a finite, explicitly exposed
batch of forest removals, births, and attachment changes. Throughout
that transaction the old edge identities, endpoint correspondences,
and physical coordinate records remain available.

Use the following order.

1. Finish the entire current circulation update, including its absolute
   counters and pending threshold flags. No numerical motion is
   interleaved with representation maintenance.
2. Before any old real-copy record disappears or its physical
   interpretation changes, read it and transfer **both**
   $`h_c`$ to $`b_e`$ and $`A_c`$ to the absolute-motion bucket of $`e`$.
   Remove the record from the copy list only after these transfers.
   Test the bucket, retaining a coalesced pending flag on the
   coordinate rather than on the disappearing copy.
3. Process the deletion-first lift changes while preserving the old
   metadata needed by all remaining removals. A surviving dormant
   internal edge retains both counters. A newly born real copy starts
   with zero counters and receives the current coordinate price and
   threshold before it can be used.
4. Finish all pool cuts, root identifications, attachments, and
   replacement records. Only then invalidate retired metadata.
   During this batch do not expose an outer cycle query, perform a
   path update, return a numerical pricing answer, or recursively
   service a newly flagged coordinate. Flags raised by retirement
   remain queued. Internal combinatorial work needed to construct the
   new representation may proceed.
5. Once the representation is settled, service pending coordinates
   using the OAI order: exact point read; reset **all** current
   absolute counters and the bucket; reenable copies and clear the
   old flag; install the new anchor, prices, and thresholds
   consistently; then process the resulting backend replacement as
   another no-motion transaction. Other coordinates flagged by its
   removals are serviced later, after that transaction. Drain this
   queue before the next numerical pricing call.

Thus an anchor's own old-copy removals flush zero absolute mass for
that coordinate. A representation change may reveal old mass, but
does not create new mass or erase a required refresh. The signed
transfer proves (1); the separate absolute transfer preserves

```math
|f_e-\widehat f_e|
 \leq {\rm bucket}_e+\sum_{c\mapsto e}A_c.
 \tag{2}
```

The source's disjoint-motion charging argument therefore applies to
arbitrary pool reuse and retirement.

A transient record born and removed entirely inside a no-motion
transaction may be reconciled without exposing it only if it never
received a numerical update and inherited no charged counters.
An old record cannot be silently dropped merely because the final
topology resembles the initial topology. It must either retain its
identity, physical map, and counters, or undergo the two transfers.

### A query answer must survive until it is consumed

A backend query may itself expose a no-motion old-to-final forest
transaction. Process all its logs with the preceding signed and absolute
transfers before reading the returned path list, which must refer to
the query's final forest. Those transfers can raise coordinate refresh
flags by concentrating old absolute mass into a bucket.

Treat the query logs and the use or discard of its answer as one atomic
numerical transaction. Defer the newly raised refresh flags until the
answer has been applied completely or discarded; a refresh can reprice
and rebuild the forest and must not invalidate a path list still waiting
to be used. The pre-query register bound remains valid during this
deferment: representation churn changes neither physical values, anchors,
input prices nor descriptors. Its newly concentrated bucket mass does
not create new physical drift. All new copies already have the current
prices and thresholds before the answer is read.

After applying or discarding the answer, drain all flags before the
next query. Alternatively, discard the answer, refresh, and make a new
query; never apply the old list after those replacements. The first
ordering adds no query and leaves the existing raw-motion and refresh
charges unchanged. Ordinary no-motion representation transactions with
no pending answer retain the service order above.

## 3. Why the two pool constructions satisfy this interface

In the Steiner bridge, all currently allocated copies of a nonnull
input-edge path remain in the exposed forest. Releasing a child
attachment leaves the path and its counters intact. When the
underlying input-edge lifetime ends, retire its child attachments,
then retire **every** path copy using Section 2, and only then discard
the old parent path and edge metadata.

In the distance construction, all common-index copies of the current
root-pool family remain exposed, including unused indices. Releasing
a child occurrence makes its index dormant; it does not reset its
internal edge records. Root splitting, identification, capacity
doubling, and complete instance retirement use the same ordered
callbacks. A newly created index layer has zero counters. Surviving
old layers preserve their counters.

The numerical client has one mutable exposed-forest history. The
separately persistent integral-allocation carriers do not fork this
mutable numerical forest or its amortized dynamic-tree state.

## 4. Suppressing a null fiber cannot suppress real motion

The Steiner construction may omit a child component lying entirely
inside a physically null port fiber, but only after every nonnull
geometric input-edge pool incident to that fiber has retired using
the preceding rules. The suppression test counts a real geometric
self-loop as a nonnull incidence even though its endpoints have the
same parent image.

At this point every remaining exported edge of that component has
always had zero physical projection during its current lifetime:
it is a fiber connector or a true null flat edge. It carries no
counter of a real numerical coordinate. Removing these records
therefore changes neither (1) nor (2). Any formerly real record
already transferred both counters during its retirement.

Zero gradient, coincident endpoint images, or cancellation in a
particular cycle is **not** a sufficient suppression criterion.
A real edge whose current gradient is zero may still carry signed
or absolute motion. An edge cannot change from real to null while
retaining a lifetime identity. Such a change requires retirement.

Keep the inactive-fiber status and its parent-lifetime association
until the child instance is discarded, so that later internal null
queries can be recognized without dereferencing retired metadata.
Reactivation creates only null exported records before any new
nonnull attachment. Real records obtain fresh identities and zero
counters; old real motion is already in its coordinate bases and
buckets.

## 5. Positive-length input self-loops can be handled separately

Let $`G`$ be an oriented undirected multigraph with strictly positive
edge lengths. Let $`E_{\rm loop}`$ be its input self-loops and let
$`G_0=G-E_{\rm loop}`$. Define

```math
R_{\rm loop}=\max_{e\in E_{\rm loop}}\frac{|g_e|}{\ell_e},
```

with the empty maximum equal to zero. For a nonzero circulation $`z`$,
split its coordinates as $`z=z_0+z_{\rm loop}`$. A loop has zero
incidence column, so both parts are circulations. The triangle
inequality gives

```math
|g^{\mathsf T}z|
 \leq {\rm OPT}(G_0)\sum_{e\notin E_{\rm loop}}\ell_e|z_e|
      +R_{\rm loop}\sum_{e\in E_{\rm loop}}\ell_e|z_e|.
```

Each separate optimum is also available in $`G`$. Consequently,

```math
{\rm OPT}(G)=
             \max\{{\rm OPT}(G_0),R_{\rm loop}\}.
 \tag{3}
```

Maintain the loops in a deterministic maximum heap keyed by the exact
ratio $`|g_e|/\ell_e`$, with stable edge IDs and deterministic tie
breaking. Compare keys by cross multiplication, not floating point.
An insertion, deletion, or price replacement costs $`O(\log M)`$
heap operations with the same polynomial bit sizes as its edge data.

Run the chosen routing or distance primitive on the loopless graph
$`G_0`$. Compare its returned raw-certificate ratio with the best
loop ratio, and return the better. If its quality is $`\rho\leq1`$,
the resulting quality is at least $`\rho\,{\rm OPT}(G)`$, by (3).
A selected loop is a one-edge circulation at this input level,
oriented according to its gradient. It requires no maintained
forest-copy pool. Its numerical update uses the source's explicit
single-edge signed-base and absolute-bucket operations.

This is an external wrapper, so neither route needs to assert that
a published primitive has a broader self-loop interface than its
statement supplies. The DO26 update definition explicitly permits
self-loops; the wrapper remains valid independently of that fact.
Parallel nonloop edges retain their individual identities.

At a recursive level, a real input loop may represent a nontrivial
closed walk in its parent. Its one-edge certificate must use the
already proved parent lift, with that lift's literal length and
gradient. It is not necessarily one edge in the final physical
graph. In particular, a core loop uses its simple fundamental-cycle
lift after canceling the common root legs, as specified in the
distance raw-lift construction. It must not be mistaken for a
null alias connector.

A zero-length, zero-gradient artificial alias connector is not a
positive-length input loop for (3). Its justified contraction or
null treatment belongs to the corresponding gauge/lift construction,
not to division by $`\ell_e`$ in the loop heap. Real coordinate
motion is never discarded by that operation.

If a topology change turns an ordinary input edge into a loop, or
the reverse, perform it as the retirement and replacement of the
old edge lifetime: first reconcile all old exposed copies and
transfer both counters; then create the replacement record in its
new owner. No loop/nonloop classification change may bypass the
transaction discipline.
