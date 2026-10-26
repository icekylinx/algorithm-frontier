# Independent checks of tight-arc repairs and the directed-epoch obstruction

**25 October 2026. Mathematical audit completed, with the transaction
ordering convention stated below.**

This note checks two separate statements:

* fixed_potential_tight_dag_repair_lemma.md;
* Sections 5--8 of any_source_directed_tree_epoch_obstruction.md.

The first supplies a bounded set of actual parent repairs during one
fixed-label interval. The second only obstructs the older single-direction
forest family. Neither proves a bound on potential refreshes or changes
the four-fifths general-matching exponent.

## 1. Tight-arc graph: deletion-only status

For fixed feasible D, an ordinary donor can be tight only if its row
label strictly exceeds its bin label, because every conservative donor
cost is at least one. Its reverse receiving direction is then unavailable
to a compatible transfer. Its allocation can only decrease, so its
register cost is nondecreasing. Tightness can disappear but cannot first
appear.

At equal labels, receiving tightness is permanent and the positive-cost
donor is never tight, even though its price may increase or decrease.
This covers both behaviors in the bidirectional interface; it does not
assume all donor prices are monotone.

Source arcs obey the same deletion-only conclusion. A start increases
its slack and cannot create source tightness. For a terminal,

```math
D(b)<A-\tau_b,\qquad
 \tau_b-\sigma_b^{\rm new}
 \ge H\alpha_b\left(5/4-(3/4)/(1-1/256)\right)
 =169H\alpha_b/340>0 .
```

The floor on the new source offer and ceiling on tau only strengthen
this inequality. Thus the new source arc remains strictly slack.

Sorting by label and putting rows before bins within a label gives
a fixed topological order of ordinary tight arcs; the source is first.
This holds for bounded negative feasible ordinary labels as well.
There is no positive-cost donor cycle at one level.

## 2. Reachability, forest edits, and the transaction boundary

Incoming lists contain exactly still-present tight arcs with reachable
tails. Under deletions each such record is removed at most once,
whether by deletion of the arc or loss of reachability of its tail.
An ordinary vertex loses reachability at most once. Its outgoing
records can therefore be processed in one lifetime scan.

Each reachable nonsource vertex has an incoming record. Choosing one
as parent gives no directed cycle by the fixed topological order.
Following parents reaches the source. In particular, replacement
parents can be supplied as ordinary forest cuts/links without creating
an underlying cycle. A selected ordinary incidence cannot be used in
both directions, because its positive donor and zero receiver cannot
both be tight. Physical coordinate identity is therefore preserved.

Each deleted parent record causes O(1) supplied edits. Total parent
recourse is O(m+nu), and graph bookkeeping costs
O(m+nu+J+R) over one interval. Arbitrary extra edits by a caller are
not covered by this count.

The lazy allocation watcher imposes one important order. Finish the
entire accepted numerical path step, settle every discovered register
reset, and update the endpoint prices before processing emitted parent
repairs that cut or relink its path. The notification queue may record
lost tight arcs during the step, but ordinary forest topology must not
change halfway through that still-being-settled path transaction.
Only after those notifications are complete are the reachability
cascade and its parent edits applied.

This ordering does not change any deletion count. It prevents a
register-discovery walk from accidentally referring to a path whose
forest topology has already changed.

## 3. Scope of the reachable-excess certificate

Every maintained root-to-bin path attains D exactly. Its first bin a
has D(a)=A-sigma_a, and its donor sum is D(b)-D(a). Therefore its
threshold score is exactly A-D(b)-tau_b.

An EMPTY search makes that score nonpositive for every tight-reachable
bin. Its semantic excess is then at most s_b/H. Summing gives
E_reachable<=T_slack/H<=N. If the global E exceeds 5N, more than 4N
lies at tight-unreachable bins.

This is a statement about EMPTY, not about a guard refusal. It also
does not assert that every strong compatible path is a zero-reduced-cost
path or survives after discarding unreachable parent subtrees.

A finite source distance equals its feasible old label exactly when
some source path has zero total reduced cost, equivalently when it is
tight-reachable. The need to repair labels on the remaining bins is
therefore real. The note correctly leaves the number and work of later
fixed-label intervals unbounded.

## 4. Directed-epoch obstruction: old SPT and endpoint inventory

For the separate obstruction note, its Section 5 uses the conservative
register inequalities, not the smaller true reciprocal price. The
largest path contribution is at most 1/(2(7-o(1))) on one branch
incidence, plus the gate contribution O(1/C) and a constant number
of O(1/L) terms. Thus the claimed total below 0.09H and the resulting
source offer above 0.65H have slack for sufficiently large C,H.

Every other direct source has slack at least eight, hence offer at
most (3/32+o(1))H. The new source is unique. The allocation support
is a tree, so the listed orientation follows and all its receiving
arcs are tight in the old exact labels.

In the fixed directed family only the three named bins can increase
their slacks. The proposed first-start argument for W is sound:
before such a first start, all motion into its star crosses the
gate donor, whose entire decreasing allocation is at most 4C.
Large star slacks therefore remain above 0.98L. No terminal free
leaf has reciprocal sufficiently smaller to pass the 5/3 necessary
ratio, while a small leaf has the wrong gain sign.

With only three positive-log slack coordinates, the total objective
increase is O(log L). Constant progress per accepted step gives
O(log L) steps for every allowed choice sequence. Each path has
constant length, so only O(log L) allocation coordinates are touched.
Their fixed direction and polynomial guard range give the stated
O(log L log S) variation bound.

The guard argument also holds. Acceptance forces any used donor
allocation to exceed one third of the start slack. The global
minimum slack does not decrease, and the normalized step changes
each donor by only a small relative amount. Tiny initial receiving
padding either stays fixed or increases. Thus the claimed exhaustion
does not hide a forced floor event.

## 5. Surviving comparison and the compatible repair

The contact a only loses slack, its reverse donor allocation remains
L-O(C), and W retains at least 0.98L slack. The transfer of L/10 on
a-to-r-to-W is feasible. Its positive normalized slack mass exceeds
L/(21C)>12N, and each negative normalized mass is below one.
The physical gap and preparation are supplied by the separately
reviewed preceding sections of that note.

The missing direction reverses the old receiving edge r-to-a, whose
endpoints have equal old labels. The following receiver r-to-W is
also tight. Thus this path is present in the new bidirectional
compatible forest without any potential change.

The note's precise conclusion is correct: it obstructs the older
directed any-source epoch, including intermediate starts. It does
not obstruct the bidirectional interface, and it supplies no lower
bound on the cost of the next potential repair problem.
