# Root audit of forest pivots, heavy carriers and bounded witness updates

**25 October 2026. Internal mathematical review completed.** This
audit covers three separate matching-client developments. It does not
certify a new unrestricted general-graph matching exponent.

## 1. One floor-preserving forestification batch is paid

In `allocation_forestification_and_pivot_accounting.md`, processing
each incidence once maintains a forest of already processed edges
whose allocation exceeds epsilon. On a closing cycle, the chosen
circulation decreases the new edge and the alternating donor edges
of the unique forest path. The minimum donor residual ensures that
every coordinate stays above its floor and at least one reaches it.

All row sums and bin loads are unchanged. Reporting every newly
floored forest edge before cutting any of them avoids querying a path
after it has been disconnected. Once a processed edge reaches its
floor, this batch never touches it again. Hence the number of actual
links, cuts and reports is linear in the number of incidences.
Directional dynamic-tree minima and signed adds implement the batch
without expanding its long cycles. Its final materialization and
price-register initialization are explicitly charged.

The positive-support forest is not the whole search graph. An
epsilon incidence cannot donate on a sufficiently strong path when
epsilon is below the stated slack scale, but it can still receive.
The generic owner-star construction correctly exposes the remaining
directed route-discovery problem. That construction is not asserted
to be a reachable matching ledger or a complexity lower bound.

The cycle example also checks algebraically. Each row sends L,
each cycle bin receives L-3C, and every cycle-bin slack is 2C.
Decreasing all a_i and increasing all b_i preserves those loads.
Only a_0 reaches epsilon, while linearly many other donors undergo
large relative changes. Thus neither zero slack-objective progress
nor a single support deletion pays those price notifications.
The example does not force every carefully chosen pivot policy to
make this move. Repeated forestification remains an unpaid step until
a specific pivot rule and its total work are bounded.

## 2. A constant heavy threshold is not an injective carrier

`heavy_allocation_threshold_hall_obstruction.md` gives an exact
Hall obstruction. For S rows, S-1 internal bins, and one private bin
per row, the prescribed internal allocations sum to (S-1)a at each
row and Sa=L-2C at each internal bin. The private allocation is
L/S+2C(S-1)/S. At the matching phase scale and the chosen S it is
strictly below gamma L.

After deleting allocations below gamma L, all S rows have neighbors
only among S-1 internal bins. No row-saturating matching survives,
even though the full ordinary support is a tree and the private
incidences give an immediate row matching before deletion.

The physical realization is also consistent: the stated seven-cycle
is odd; all physical degrees are at most three; the displayed path
augments the current matching once. The vertex cover consisting of
the rows together with u,v has size S+2, proving exact gap one.
Finite dyadic top coordinates and the separately defined integral
lower ledgers satisfy their row and residual requirements. The large
private contact slacks are explicitly acknowledged, so this is not
being used as a false stalled-numerical-search example.

The conclusion concerns a universal constant threshold. Adaptive
weighted carriers and thresholds depending on a relevant set size
are not refuted.

## 3. Bounded witness patterns avoid hidden path materialization

The construction in `bounded_interface_witness_pattern_updates.md`
and its independent audit passed the following main checks.

At every hierarchy node, physical coordinate ownership is unique.
Coordinates are bucketed by their signed membership in the current
q selected path witnesses. A pending tag means an update already
included in the parent minima but not yet in its children. Pushing
it through the old composition matrix preserves its increment on
every physical edge exactly.

Before a family or composition changes, its old tag is pushed. After
the affected children are current, every new parent witness is a
composition of current child witnesses. Therefore an entire child
bucket maps into one new parent bucket. Merging its minima is exact;
its potentially large set of physical edges is never enumerated.
The zero-use bucket must be retained. An edge later entering a route
is distinguished by a changed descendant family, propagated upward
from its unique leaf.

The source/target and boundary shortest-path tables suffice for each
merge. Every physical path decomposes into child segments, and every
auxiliary composition expands to a physical walk. If an optimal
expansion repeated a vertex, removing its positive-cost ordinary
cycle would produce a strictly better physical route with another
auxiliary representation. Hence the chosen expansions are physically
simple. This supplies, rather than assumes, the signed-use bound
in {-1,0,1}. Empty auxiliary detours are removed by the tie rule.

All crossed registers remain visible in the bucket minima, even if
intermediate witness families change. A step installs its old route
update first and settles every register and endpoint price before
another numerical step. Accessing a leaf materializes its own pending
scalar before a reset. Source and target price leaves have unique
owners, so endpoint edits are not replicated at every separator.

Historical tags have polynomially bounded grid magnitude: a simple
historical path cannot use one fixed nonempty child route twice, and
a family change pushes its history below it. Linear dependencies
between route vectors do not justify discarding tags. Their actual
history and the supplied numerical range pay their bit length.

Thus the finite-interface lemma has the claimed
3^q poly(q) times hierarchy-height cost per notification or point
edit, and no physical-path-length cost per transfer. The static
client's register and slack-progress bounds remain applicable because
its accepted paths are physically simple.

## 4. Scope of the separator corollary

A supplied tree decomposition can be converted to an edge-owning
display tree and a balanced top-tree hierarchy. Running intersection
places every shared graph vertex in a separator bag. A cluster has
at most two display boundary vertices, giving O(w+1) graph boundary
names and O((w+1)^2) selected witnesses.

Pruning empty branches and suppressing degree-two display nodes do
not create new physical routes. The decomposition's original input
size and edge-assignment work are separately charged. The resulting
static exponential-width client is a valid parameterized interface.
It does not pay for arbitrary matching contractions, support changes,
or finding and maintaining a new decomposition.

The public bounded-treewidth min-cost-flow comparison is recorded in
the independent audit and has a better width dependence for its own
stated problem. The new note is not presented as a flow record.
An overlapping general-graph router cannot simply replace the
edge-partition hypothesis: unique coordinate ownership, the number
of selected witnesses and all composition maps would need proofs.

## 5. A valid strong step can force long neutral correction

The additional note
`forced_forestification_motion_after_strong_step.md` strengthens
the pivot-accounting example. Its initial row sums, all listed bin
loads and positive slacks check directly. The large-coordinate support
is a tree, with exactly one epsilon off-basis receiver.

For the two-incidence path a to e to v_k, the ratio is bounded below
by (8-1.601)/(8+1.601+1.6)>0.57. The initialized conservative price
and the stated finite-grid step also satisfy the permitted charge
interval. It is a passing path with one actual donor and constant
positive slack-objective progress.

After that step, fixed row and bin margins leave only one scalar
cycle-correction degree of freedom. Its feasible interval is exactly
[-3L/8+2epsilon, eta]. At one endpoint the new receiver returns to
epsilon and every left chain coordinate decreases by eta, giving
at least k/2560 additional negative log variation. At the other
endpoint the old e-v_0 edge reaches epsilon and all k right chain
coordinates cross their old hysteresis anchors. An interior correction
leaves the cycle active, so cannot be the required forestification.

All correction moves keep the new slacks fixed. The two-copy physical
realization has the stated exact matching gap one, integral lower
ledgers and only low-slack remainder contacts. Thus an already eligible
structural expansion is not being ignored before the numerical move.
The construction need not be chosen by every maximum-score policy;
it witnesses a move admitted by the declared numerical contract.

This proves a failure of the old per-step negative-variation charge
under mandatory forestification. It still does not prove a superlinear
history-wide lower bound: the initialization budget can pay one such
episode, and a different amortization or pivot policy remains possible.

## 6. Main objective remains open beyond the accepted exponent

These developments identify valid local implementations and rule out
specific unproved shortcuts. The accepted research bound for exact
deterministic maximum matching on arbitrary general graphs remains
the 4/5-exponent bound documented in the main checkpoint. A paid
general-support path and update mechanism is still needed to improve
that exponent.
