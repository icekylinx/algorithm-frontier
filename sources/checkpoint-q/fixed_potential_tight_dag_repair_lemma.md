# Decremental tight-arc repairs during one fixed-potential interval

**25 October 2026. Research lemma; root and independent mathematical reviews completed.**

The independent review is **tight_dag_and_directed_epoch_independent_audit.md**.
The transaction order in Section 5 is part of the accepted interface.

This note supplies a limited repair mechanism for
`bidirected_potential_compatible_forest_matching_interface.md`.
For one fixed feasible potential, its tight-arc graph only loses edges.
We can maintain an exact old-label shortest-path forest on the vertices
still reachable in that graph with linear total graph work and linear
total supplied forest edits. The remaining obstruction is the vertices
that become unreachable: their labels need to rise, and no bound on the
cost or number of such potential intervals follows here.

## 1. Fixed-interval setting

The ambient graph has `nu` row/bin vertices and `m` allocation incidences.
No coordinate birth, ledger edit, external assignment, or label change
occurs during this interval. All numerical steps satisfy the preceding
compatible-forest contract, including the guarded step size, persistent
registers, and receiver tightness.

Normalize the artificial source label to zero. For incidence `(r,d)`, the
receiving arc `r -> d` has length zero, the donor arc `d -> r` has length

\[
 c_e=\left\lceil H/(4\ell_e)\right\rceil\ge1,
\]

and the artificial source has an arc to bin `d` of length `A-sigma_d`,
where

\[
 \sigma_d=\left\lfloor\frac{3H}{4s_d}\right\rfloor,
 \qquad
 \tau_d=\left\lceil\frac{5H}{4s_d}\right\rceil.
\]

The fixed integer labels `D` are feasible for all of these current arcs.
Call an arc `u -> v` **tight** when `D(v)=D(u)+length(u,v)`.
Let `Z` be the subgraph of all tight arcs, including tight source arcs.
The supplied initial labels need not be exact; bounded-word arithmetic
and all semantic conventions are imported from the preceding note.

## 2. The tight graph has a fixed topological order

A tight donor satisfies `D(r)=D(d)+c_e>D(d)`.
A tight receiver satisfies `D(r)=D(d)` and goes from row to bin.
Thus sorting ordinary vertices by `(D, row-before-bin)` is a topological
order. Put the artificial source first; it has no incoming arcs. This
works even if some initially supplied ordinary labels are negative.

Parallel incidence identities cause no issue: an arc still respects the
same order. There is no directed tight cycle, including a two-arc cycle
on one physical incidence, because the donor cost is strictly positive.

## 3. No new tight ordinary arc can appear

The tightness of a zero-length receiver depends only on the fixed two
labels, so its status is constant.

For a donor there are two cases.

1. If `D(r)=D(d)`, its positive cost prevents it from ever being tight,
   regardless of how far a receiving traversal lowers that cost.
2. If `D(r)>D(d)`, the receiving direction is forbidden by compatibility.
   This coordinate can only decrease during a numerical step. Its
   register cost is therefore nondecreasing. Feasibility already gives
   `c_e >= D(r)-D(d)`. A strict inequality cannot become equality, while
   an equality may be destroyed by a cost increase.

Forest cuts and links change neither primal values nor register costs.
They do not change this conclusion. Hence ordinary tight arcs can only
be deleted during the interval.

## 4. No new tight source arc can appear

Only the two endpoint slacks change in a numerical step. At the starting
bin, slack increases, so `sigma` cannot increase. Its source-arc length
can only increase; a nontight source arc cannot become tight there.

At a terminal `b`, acceptance gives

\[
 D(b)<A-\tau_b.
\]

Write `alpha=1/s_b` before the step. The accepted step satisfies
`eta alpha <= 1/256`, so its new reciprocal is at most
`alpha/(1-1/256)`. Consequently

\[
 \tau_b-\sigma_b^{\rm new}
 \ge
 H\alpha\left(\frac54-\frac{3/4}{1-1/256}\right)
 =\frac{169}{340}H\alpha>0.
\]

The new source arc is therefore strictly slack. This also shows that an
initially tight source arc cannot be used as a terminal before it has
ceased to be tight. Unchanged bins preserve their source-arc status.

Thus every arc of `Z` is either present from the interval's beginning or
absent forever. The current `Z` is a deletion-only subgraph of its initial
version, even though other ambient prices may both increase and decrease.

## 5. Reachability and parent repairs in linear total graph work

Initialize source reachability in `Z` by a graph traversal. For each
currently reachable ordinary vertex maintain the list of its remaining
tight incoming arcs whose tails are reachable. A list record belongs to
one arc identity. Store one such arc as its parent.

When a tight arc is deleted, remove its list record if its tail is still
reachable. If a vertex loses its last such incoming arc, mark it
unreachable and remove its outgoing tight arcs' records from their heads'
lists. Continue this propagation. The source itself is permanently
reachable. Because `Z` is a DAG, a nonsource vertex is reachable exactly
when it has a reachable predecessor. No unreachable vertex becomes
reachable under these deletions.

Each ordinary vertex is removed from the reachable set at most once.
Each initial tight arc is removed from an incoming list at most once,
whether because the arc itself disappears or because its tail becomes
unreachable. Doubly linked lists or equivalent indexed records support
these removals and the choice of a replacement parent in constant time.

If a parent's arc is removed while another incoming record remains,
replace the parent by any remaining record. If none remains, remove its
parent. The chosen parent arcs are acyclic by the fixed topological order;
following parents backward from a reachable vertex ends at the artificial
source. Thus they form an exact old-label source tree on the reachable
vertices.

Remove the artificial source and its selected arcs to get an ordinary
compatible out-forest. Every receiving edge is tight and every donor
edge is tight, so the forest meets the numerical interface's requirements.
At most a constant number of ordinary cuts/links accompany each removed
parent record. The total supplied ordinary-edit count is

\[
 P=O(m+\nu).
\]

This bound counts the repairs emitted by this particular parent
maintainer. It does not absorb arbitrary additional caller-requested
forest pivots.

Scanning the initial graph, maintaining reachability, and detecting lost
tightness from the `O(J)` endpoint updates and `R` register notifications
costs

\[
 O(m+\nu+J+R)
\]

bounded-word operations, apart from the polynomial-logarithmic numerical
and dynamic-forest operations already charged by the interface.

This is immediately composable when this maintained parent forest is the
one used for numerical path transfers. The reachability statement itself
also holds under compatible transfers found elsewhere, but that fact does
not provide free synchronization of multiple independent lazy allocation
watchers for the same primal coordinates.

The composition uses a transaction boundary after each numerical path
step. Keep the ordinary forest fixed while applying the entire lazy path
update, finding and processing every register reset on that path, and
updating its endpoint prices. During this transaction, collect the IDs of
arcs that have lost tightness without repairing parents immediately.
Once all these numerical updates have finished, delete the collected
arcs from the tight DAG, propagate lost reachability, and emit the
resulting ordinary cuts and links before allowing another path query.
This order preserves the path on which remaining register resets must
be searched. A donor edge that has just become nontight remains a
compatible selected donor, so postponing its removal until the end of
the transaction is valid. No new numerical step is taken with stale
tight-parent information.

## 6. What an empty search certifies on reachable bins

Let `R_bin` be the currently tight-reachable bins, and set

\[
 \pi_b=(A-D(b))/H,
 \qquad
 E_R=\sum_{b\in R_{\rm bin}}(s_b\pi_b-5/4)_+.
\]

For every reachable bin `b`, let `a` be the first bin on its maintained
source-tree path. The source arc to `a` is tight, and every following arc
is tight. Therefore

\[
 D(a)=A-\sigma_a,
 \qquad
 \bar L_T(a,b)=D(b)-D(a).
\]

The score of that ordinary root-to-`b` path is exactly

\[
 \sigma_a-\tau_b-\bar L_T(a,b)
 =A-D(b)-\tau_b=H\pi_b-\tau_b.
\]

If the compatible forest search returns EMPTY, this value is nonpositive
for every reachable `b`. Since `tau_b <= 5H/(4s_b)+1`,

\[
 E_R\le\frac{\sum_{b\in R_{\rm bin}}s_b}{H}
 \le\frac{T_{\rm slack}}H\le N
\]

under the imported rounding budget. An EMPTY result is different from a
guard failure; the argument uses the actual absence of a positive scored
path.

Equivalently, if global `E>5N` at this point, more than `4N` of that excess
comes from tight-unreachable bins. The maintained old-label tree has
already accounted for the reachable part.

## 7. The remaining boundary is a potential refresh, not parent selection

Feasibility makes `D(v)` a lower bound on the current source distance.
A tight source path attains that bound. Conversely, any path attaining
`D(v)` has zero total reduced cost and hence consists entirely of tight
arcs. Thus tight-reachable vertices are precisely the vertices whose old
label is still exact, whenever the source distance is finite.

For a tight-unreachable bin the source distance must exceed its old label.
The lemma does not raise that label, process a new tight graph after a
label change, or bound how many such intervals are needed. Reinitializing
this structure after every potential refresh can still cost `Theta(m)`
per refresh. The scalar `E` and the bounded register-event count do not
by themselves pay that work.

In particular, replacing the fixed labels by a merely local approximate
Bellman inequality is not justified: cheap positive cycles may support
labels far from a source-rooted distance certificate. A source-rooted or
cycle-elimination argument is still required. This note therefore does
not change the global four-fifths general-matching bound.
