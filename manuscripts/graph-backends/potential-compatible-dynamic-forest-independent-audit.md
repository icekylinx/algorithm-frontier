# Independent audit of the potential-compatible dynamic forest interface

**25 October 2026. Mathematical and data-structure audit completed.**

Audited construction:
[potential-compatible-dynamic-forest-matching-interface.md](potential-compatible-dynamic-forest-matching-interface.md).
This audit checks the local interface for supplied forest repairs. It does
not supply the repairs, bound their number, or improve the global
general-matching exponent.

## 1. Verdict and the exact imported data structure

The construction is valid with the stated fixed semantic interval,
injective allocation-coordinate ownership, tight selected receiving arcs,
and guarded finite-word arithmetic. It searches all directed bin-to-bin
paths of an arbitrary directed forest, rather than only paths from a
chosen root. Its work is

$$
(\nu+J+P+Q+R)\mathrm{polylog}S,
$$

where `P` counts the supplied links and cuts and `R` counts numerical
register events. Both counts must remain in the statement.

The primary source was read directly:
Alstrup, Holm, de Lichtenberg, and Thorup,
*Maintaining Information in Fully-Dynamic Trees with Top Trees*,
<https://arxiv.org/html/cs/0310065v2>.
Theorem 1 and Sections 2.1–2.4 provide logarithmic-height binary clusters
and logarithmically many local joins and splits for each forest operation.
Theorems 2–3 in Section 2.5 provide the exposed-path aggregate and lazy-add
pattern. Theorem 7 explains the mutable boundary-vertex issue. Sections
6–7 distinguish the worst-case implementation from the simpler amortized
one. The local interface may use the former; it is not relying on a
splay-tree height bound.

The directed-path dynamic program is supplied explicitly by the audited
note. It is not attributed as a ready-made matching primitive in the
top-tree source.

## 2. Pendant terminals remove the high-degree price problem

Each bin receives one incoming source-terminal edge of score `sigma` and
one outgoing target-terminal edge of score `-tau`. The two terminal types
are disjoint and immutable. Adding these leaves preserves acyclicity and
adds only a constant amount of inventory per bin.

A source-to-target directed path cannot visit another terminal in its
interior, because that terminal has degree one. Deleting its first and
last edges therefore gives exactly one directed ordinary bin path, and
the sum of its edge scores is

$$
\sigma_a-\tau_b-\sum_{e\text{ donor on }F[a,b]}\bar c_e.
$$

Conversely every permitted ordinary path has this unique augmentation.
The self-pair has negative score and cannot produce a false accepted
transfer. Negative terminal scores do not cause a cycle problem in an
underlying forest.

A change to a bin slack changes two individual edge scores. It does not
require touching every cluster that has that bin on its boundary. The
ordinary incidence degree is irrelevant to this update cost.

## 3. The cluster recurrence is complete and sound

The four state types have distinct purposes: directed boundary-to-boundary
path score `W`, source-to-boundary score `I`, boundary-to-target score `O`,
and complete source-to-target score `F`. Every state uses constant-sized
metadata because a cluster has at most two boundary vertices.

For children intersecting only at `v`, a complete path either stays in one
child or crosses from one child to the other through `v`. The latter cases
are precisely `I_1(v)+O_2(v)` and `I_2(v)+O_1(v)`. A finite cross term
cannot repeat an ordinary vertex: the children share only `v`. Its two
directed legs also have compatible directions by their state definitions.

For a retained boundary `b` in the first child, a source reaching `b`
either lies in that child or reaches `v` through the other child and then
uses the first child's directed `v`-to-`b` path. This gives the displayed
`I` recurrence. Reversing the direction of this reasoning gives the `O`
recurrence. The `W` recurrence follows from uniqueness of an underlying
tree path. Rake joins, a retained common boundary, and root clusters with
zero boundaries obey the same argument.

Base states include the zero-edge paths at a terminal: `I(s)=0` for a
source terminal `s`, and `O(t)=0` for a target terminal `t`, when the
corresponding boundary entry is present. There is no zero-edge complete
candidate because no vertex has both terminal types. Missing paths use an
explicit invalid-state flag, rather than an arithmetic infinity that
could overflow.

The witness metadata consists only of endpoint IDs. A join recomputes the
maximizing endpoint pair, including when a numerical tie occurs. It never
needs to enumerate the represented path.

## 4. Component maxima are an explicit small wrapper

The maximum dictionary is maintained over actual settled underlying
components, not over every temporary root cluster produced while a top
tree is split. Before a cut or link, remove the old affected component
entries; after the operation, find the new components through the known
endpoints and insert their updated root values. Only constantly many
underlying components are involved. A point-price edit affects one
component. An expose changes representation, not the set of ordinary
paths, and can refresh that component's root handle and witness.

Thus even a conservative implementation using an extra logarithmic search
for component handles remains within the claimed polynomial-logarithmic
bound. An isolated row has no candidate; an isolated bin is represented by
its two price leaves and has only the negative self-candidate.

## 5. The allocation watcher is correctly separated from the score DP

The ordinary forest is represented a second time without price leaves.
For a donor, both `x-ell` and the lower guard buffer decrease by `eta`.
For a receiver, both `2ell-x` and the upper guard buffer also decrease by
`eta`. Therefore one exposed-path additive tag updates the two kinds of
buffers uniformly, even when the implementation changes its own root.
Physical donor/receiver roles are immutable until an explicit selected
direction change.

Lazy propagation is restricted to cluster-path children. It does not
affect off-path branches or any price-terminal edge. The ordinary forest
contains each allocation-coordinate ID at most once, so one transfer does
not update multiple aliases of the same primal value.

After a crossing, the watcher recovers the current exact coordinate from
its buffer and old register. Resetting `ell=3x/4` makes the new donor buffer
`x/4` or receiver buffer `x/2`. A donor reset changes one scored edge and
one donor-cost aggregate. A receiver reset affects only its ambient reverse
donor price. The score DP therefore receives only point edits at register
events, not an unproved bulk nonlinear price update.

Cutting an incidence materializes only that coordinate, after pushing its
own lazy ancestry. A later link initializes the new watcher from the
explicit record and reuses the persistent register. This authoritative
ownership convention is sufficient to preserve both exact values and the
history-wide event accounting.

## 6. Ledger conservation and the old labels survive a repair sequence

An ordinary directed path alternates donor and receiving roles. Each
internal row loses and gains the same amount; each internal bin has zero
net load change. The endpoints have the prescribed opposite slack changes.
This does not require the forest to be an out-forest under any root.

During a transfer, every donor coordinate decreases and hence its
conservative price can only increase. A receiving coordinate may lower its
reverse donor price, but the selected receiving arc has equal old endpoint
labels, so the reverse constraint remains valid at any nonnegative price.
Unchanged coordinates retain their old constraints.

At the terminal, pre-step feasibility and the positive path score imply
`D(b)<A-tau_b`. This supplies the same margin against the terminal source
price increase as in the fixed-forest proof. The accepted step size and
rounding allowance are unchanged. Hence the fixed labels remain feasible
for the complete threshold graph, not merely for the selected forest.
The scalar semantic screen changes only in the two endpoint slack terms.

A supplied forest edit itself changes no allocation or label. A newly
selected receiver must pass the equality check; the data structure does
not silently make it tight or refresh its potential.

## 7. Arithmetic and event accounting

The finite-word statement includes polynomially bounded `H,A,D` and the
guarded primal/register values. In particular, arbitrary feasible labels
of unbounded negative magnitude are not accepted as constant-size input
words. Exact SPT labels in the stated nonnegative threshold graph satisfy
the required bound. This explicit premise closes a literal ambiguity in
allowing other feasible initial labels.

All path-score sums contain `O(nu)` polynomially bounded integer terms.
Endpoint reciprocals, the finite-grid step, and buffer tags use only a
constant number of guarded rational values and fixed dyadic denominators.
Consequently their bit operations are covered by `polylog S`.

Between consecutive register resets a coordinate changes multiplicatively
by a fixed constant. Negative allocation log variation is `O(1)` per
accepted numerical step. Positive variation is bounded by negative
variation plus the bounded total log-value range and the explicitly
charged births, deaths, and assignments. Cuts and links neither change a
coordinate nor reset its register. Thus the previous bound

$$
R=O\bigl(J+(N+A_{\rm ext})\log S\bigr)
$$

continues to hold across supplied repair sequences. This does not charge
or bound the work of finding those repairs.

## 8. Precise scope of the result

The new local implementation removes the need to rebuild a static
heavy-light representation for each *supplied* compatible edge
replacement. It also handles arbitrary physical edge orientations in an
underlying forest.

No proof here supplies a useful ambient edge when the forest search is
empty, bounds unsuccessful replacement attempts, handles a nontight new
receiver at zero cost, or bounds global label refreshes. `FOREST-EMPTY`
remains different from semantic `LOW`. The deterministic general-matching
complexity is therefore unchanged by this local lemma alone.
