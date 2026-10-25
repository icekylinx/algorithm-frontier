# Independent audit of the bidirectional matching forest interface

**25 October 2026. Completed mathematical and data-structure review.**

Audited note:
`bidirected_potential_compatible_forest_matching_interface.md`.
The bidirectional extension passes the independent audit. It retains one
physical forest edge and one authoritative allocation per incidence, while
allowing that edge's two physical directions when their separate
compatibility conditions hold. This is a local implementation result;
there is still no global bound on useful forest repairs or potential
refreshes.

The primary top-tree interface is the one directly checked in
`potential_compatible_dynamic_forest_independent_audit.md`:
Alstrup, Holm, de Lichtenberg, and Thorup,
<https://arxiv.org/html/cs/0310065v2>, Theorems 1–3 and 7.
The extra directional state described below is the present construction's
augmentation of that public interface.

## 1. One edge with two directional scores does not duplicate an allocation

For an incidence `(r,d)`, the underlying object has one undirected edge.
Its bin-to-row donor direction has score `-bar c`; its row-to-bin
receiving direction has score zero only when `D(r)=D(d)`.

All searches use the unique underlying simple path between their
endpoints. Therefore an allocation ID is used at most once in a returned
path. Having both directional scores present is not the same as inserting
two underlying parallel edges or two lazy copies of the primal variable.
The explicit identity check on a link is essential.

The two pendant terminal edges per bin remain distinct, degree-one
gadgets. They create a bijection between admissible ordinary bin paths and
scored source-terminal to target-terminal paths. Their scores contribute
only the requested two endpoint prices.

## 2. The directed cluster DP still describes exactly the simple paths

In a base cluster, either one or both directional boundary scores may be
finite. The diagonal zero-edge state and the terminal endpoint states
remain unchanged. All other states have their previous meanings.

If two children share only `v`, a finite cross candidate consists of one
path ending at `v` in the first child and one path starting there in the
second child. Their edges are disjoint. The concatenation is therefore a
simple underlying path, regardless of whether some constituent edges
would also permit reverse traversal. A path lying in one child is covered
by that child's inductively correct state. This proves the complete-path
recurrence and excludes an implicit two-edge return walk.

The same decomposition proves both boundary-to-boundary and one-terminal
recurrences. They require only unique tree paths and directional
availability, not a rooted orientation or a prohibition against storing
the reverse score of an edge.

The maximum dictionary uses the previously audited settled-component
wrapper. Edge-price changes in either sign are ordinary point updates to
the scored tree. In particular, no monotonicity assumption about a
selected donor price is needed by this DP.

## 3. The two directional watcher states refer to the same exact value

The identities

\[
 w_D=x-\ell,\quad w_R=2\ell-x,\quad w_D+w_R=\ell
\]

and

\[
 g_D=x-\chi,\quad g_R=U-x,\quad g_D+g_R=U-\chi
\]

are exact. If a transfer traverses the edge as a donor, the first state in
each pair decreases by `eta` and the second increases. For a receiving
traversal the roles exchange. Hence, relative to the actual ordered path,
every forward buffer decreases by the same amount and every backward
buffer increases by that amount. Mixed physical edge roles along the
path do not invalidate the uniform update.

For a two-boundary cluster the note fixes a local boundary order, for
example by immutable vertex IDs. Store separate forward and backward
path minima and a signed tag. On a split, send that tag only to path
children, negating it exactly when the child's fixed order opposes the
parent traversal. On a join, use the appropriately ordered child fields
and start the new tag at zero.

This is sufficient to handle rakes and changes of internal implementation
root. A point child has no path edge to update. A boundary-set change uses
the top-tree split/join discipline, so an old signed tag is not silently
reinterpreted on a new path. If an implementation instead chooses a
mutable boundary ordering, it must swap the directional fields and negate
the tag when it reverses that ordering; the fixed-ID convention avoids
that extra case.

The watcher excludes price-terminal edges. Its updates therefore have
exactly the intended ordinary-coordinate support.

## 4. Forward crossing discovery is exhaustive

In a settled state, both register buffers are strictly positive. During
one committed ordered-path transfer, only the forward buffer decreases;
the backward buffer increases and off-path edges are untouched. Thus
every newly violated register condition occurs among the forward minima
of that exposed path.

At a reported edge, the point query pushes the needed lazy tags and
recovers one exact `x`. Resetting `ell=3x/4` gives

\[
 w_D=x/4>0,\qquad w_R=x/2>0.
\]

The reset does not modify the guard buffers, since it does not modify
`x`. It does modify the one donor cost. The note correctly updates both
the scored physical edge and the watcher's directional donor-cost sums
even when the path just used the receiving direction. Treating that
price change as exclusively off-forest would be incorrect in this
bidirectional interface; the operative construction does not do so.

Repeating the forward-minimum search until no violation remains settles
every selected register. No positive buffer or unaffected branch needs
to be enumerated.

## 5. Cuts, links, and numerical transactions preserve ownership

A cut materializes the coordinate from its watcher before destroying the
two representations of that physical edge. A link reads the explicit
native coordinate and reuses its persistent register. There is never a
second authoritative allocation value associated with the reverse
direction.

The scored tree, watcher, endpoint prices, and component dictionary are
settled before another external query is answered. A provisional witness
need not remain maximizing while a numerical transaction is processing
several register events; the returned settled witness is recomputed.
The already committed numerical step was certified using its pre-step
data, so subsequent point-price changes do not invalidate its proof.

## 6. The potential proof is stepwise, which is enough

Every ordinary directed bin path enters an internal row as a donor and
leaves it as a receiver. The corresponding allocation changes cancel at
that row, and they cancel at each internal bin. Endpoint slacks change by
opposite amounts. Coordinate injectivity prevents hidden double updates.

For an individual donor traversal the allocation decreases and any reset
can only raise its donor price. For an individual receiving traversal a
reset can lower that price, but availability requires equal endpoint
labels. The full-graph donor inequality therefore remains valid in that
case as well. These arguments may be reapplied at each step even when
the same edge alternates roles over its lifetime.

The source inequality at the terminal follows from

\[
 D(b)\le D(a)+\bar L_F(a,b)<A-\tau_b.
\]

The imported finite-grid step and rounding allowance pay the ensuing
source-price change. The start's source cost increases, and the usual
maximum-reciprocal bound keeps `A` valid. No label refresh is hidden in
these operations. The semantic scalar changes only in its two endpoint
terms.

## 7. Bit bounds and the event ledger survive reversals

A cluster's unapplied signed transfer is the net coordinate change along
any edge of its nonempty path, up to that edge's fixed sign relative to
the cluster order. The guarded coordinate range bounds this net value.
Repeated changes of direction neither create growing denominator depth
nor require storing the entire history. Register replacement uses the
same fixed dyadic grid as before.

Each reset still requires a constant amount of absolute log variation
since the preceding reset. Merely reversing the next traversal direction
does not reset the register. The sum of negative allocation log changes
is `O(1)` per accepted step. Telescoping the total allocation-log potential
then bounds positive variation using the explicit external-event and
guard-range ledger.

Consequently the existing bound

\[
 R=O\bigl(J+(N+A_{\rm ext})\log S\bigr)
\]

remains valid independently of the number `P` of supplied physical
repairs. Each numerical step, supplied link/cut, extra query, and reported
reset requires only polynomial-logarithmic local work, after the supplied
initialization.

## 8. What this audit does not establish

The extension permits switching the direction used on a tight physical
edge without paying an artificial cut/relink event. It searches all
potential-compatible simple paths supported by the maintained physical
forest.

It does not find useful off-forest incidences, make an incompatible
receiving direction tight, bound failed repair searches, or bound global
potential refreshes. An empty forest search remains weaker than the
semantic LOW certificate. No new global general-matching time bound is
claimed.
