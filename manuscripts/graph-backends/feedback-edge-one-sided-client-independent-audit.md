# Independent audit of the feedback-edge one-sided client

**25 October 2026. Full mathematical and event-accounting audit passed.**

This audit checks [feedback-edge-one-sided-client.md](feedback-edge-one-sided-client.md) for the complete
ambient ordinary allocation graph, decomposed into a spanning forest
and at most <code class="math">k</code> chord incidences. It confirms the stated
<code class="math">(k+1)\mathrm{polylog}S</code> per-query/update cost and the total
work bound. It does not assert that general matching ledgers have
sublinear feedback count.

## 1. The small core has the required exact interface

Marking every chord endpoint gives at most <code class="math">2k</code> distinct marked
vertices. In each forest component, the minimal marked subtree has
only <code class="math">O(k)</code> marked or branching vertices after suppressing
unmarked degree-two vertices. Its virtual paths have disjoint
interiors, and a chord endpoint cannot lie in such an interior.

Each virtual edge's two directional costs are exactly the current
donor-price sums on its underlying forest path. Repricing all of them
costs <code class="math">O(k)</code> dynamic-tree queries. The topology compressor uses hop
lengths and is unaffected by numerical prices. No long path is
enumerated during repricing.

For any ordinary path using chords, its source-to-first-chord and
last-chord-to-target pieces are forest paths. The source and target
offers read at those marked endpoints dominate these particular
pieces. Every intervening forest piece is represented exactly in the
virtual forest. Thus the directed nonnegative core loses no passing
ordinary path. Pure forest paths are handled separately by the
existing maximum-score tree query.

The artificial source edge has nonnegative cost because
<code class="math">I_T(v)\le\max_a\sigma_a\le A</code>. There is no requirement that
the two directions of a virtual forest edge have the same cost.
Dijkstra can use the usual settled-order predecessor rule to return
a simple predecessor path even in the presence of zero receiving
costs: equal-distance updates must not introduce predecessor cycles.
This is a deterministic implementation choice with no additional
asymptotic cost.

## 2. Two trimming operations suffice and are cheap

A simple core predecessor path expands to a simple ordinary path:
virtual interiors are pairwise disjoint and do not contain any chord
endpoint. Therefore only its source and target forest attachments can
cause repetitions.

Let the initial attachment run from <code class="math">a</code> to the start of the middle
path <code class="math">M</code>. Choose the last vertex of <code class="math">M</code> that lies on that
attachment. Replacing the two prefixes by the attachment prefix to
that vertex removes a directed closed walk. The remaining middle
suffix has no vertex on the attachment, so the resulting path is
simple. Next choose the last vertex of the target attachment that
lies on this simple path. Keep the old prefix to this vertex and the
final attachment suffix. Again a directed closed walk is removed,
and the resulting ordinary path is simple.

Both deleted walks have nonnegative cost. Source and target prices
are unchanged, so positive conservative score survives both operations.
The two attachments and the <code class="math">O(k)</code> middle pieces are represented
paths throughout; no length-proportional traversal is used.

The stated tree-path intersection formula is exact. The projections
of two endpoints onto another tree path bound their intersection if
they differ. If they coincide, the projected vertex belongs to the
second path exactly when its two endpoint distances add to that
path's length. Component checks handle disjoint components, and the
same rule handles zero-edge paths. Hop-based selection and distances
therefore locate the required last intersection in polylogarithmic
time per represented piece. A chord is tested only through its two
endpoints, since the other attachment lies in the forest.

## 3. Complete LOW and the rounding scope

Failure of both the tree-only and core tests excludes every positive
conservative ordinary path. A hypothetical strong true one-sided path
can first be taken simple, so it has at most <code class="math">\nu-1</code> ordinary
incidences and obeys the previously proved rounding budget. No
<code class="math">\nu</code>-edge rounding bound is applied to an untrimmed repeated walk.

Sign-compatible decomposition of a feasible allocation difference
gives auxiliary-vertex cycles plus ordinary-only cycles. The latter
have zero slack gain. A simple auxiliary-vertex cycle yields a simple
ordinary bin path, even when the ambient graph itself has cycles.
Thus excluding every strong ordinary path is a complete LOW
certificate for the ambient graph, not merely for the chosen forest.

## 4. Atomic updates do not multiply variation by the number of pieces

After trimming, all represented forest pieces and chord incidences
belong to one simple physical path. Their incidence IDs are disjoint.
Computing the donor sum and guards over these pieces costs
<code class="math">O(k)</code> aggregate queries. The same transfer is applied to every
piece with its actual direction, and only the two endpoint slacks
change. Internal pieces may end at rows or bins; conservation is
asserted after the complete atomic transaction, as required.

All coordinate, register and price records remain uniquely owned.
Discovered register crossings are settled before another numerical
query. The total negative allocation log variation is bounded for
the whole simple path. It is not charged separately as an independent
constant per piece. Consequently the global register-event bound
remains <code class="math">O(J+(m+A_x)\log S)</code>, without a new multiplicative <code class="math">k</code>.
The per-step query and update work does contain the stated <code class="math">k+1</code>.

The unrestricted-receiver forest client's minimum-slack and donor
floor proofs depend only on positivity, a simple path, and the step
normalization. They apply unchanged after trimming.

## 5. Dynamic topology and the total bound

Deletion of a tree edge creates two tree parts. Scanning the at most
<code class="math">k</code> chords either supplies a replacement crossing those parts or
certifies that the ordinary component has disconnected. Promoting
one chord transfers its current coordinate and existing register to
the forest watcher; this is a change of representation, not free
primal progress. Endpoint reference counts change only constantly
many marks per edge operation. All compressor edits and promotions
are charged to explicit structural records.

Retargeting is deletion followed by insertion. Retiring a vertex must
enumerate its incident deletions. Cuts before new links avoid a
temporary union-graph cycle-rank spike. The theorem explicitly bounds
the actual intermediate feedback count; it does not rely only on the
two endpoint states of a structural batch.

The static objective width gives <code class="math">J=O(\nu\log S)</code>, and the
register bound above then yields
<code class="math">(m+\nu(k+1))\mathrm{polylog}S</code>. Substituting the explicit
<code class="math">A_T,A_x,A_s</code> ledger bounds gives the dynamic total stated in the
main note. Initial core construction, chord scalar records and all
forest initialization fit this accounting.

The subcubic example in Section 8 has exactly <code class="math">4q+1</code> vertices,
<code class="math">5q</code> edges and cycle rank <code class="math">q</code>. Its chord-free chain assignment
has every nonroot slack <code class="math">2C</code>; the four-incidence perturbation in
each block preserves every row sum and bin load and makes the chord
positive. This correctly rules out inferring a small feedback count
from degree three or from the ordinary allocation equations alone.

No remaining local correctness, completeness or event-accounting gap
was found within the declared feedback-edge interface.
