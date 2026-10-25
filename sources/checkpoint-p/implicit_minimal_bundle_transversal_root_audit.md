# Root audit of the implicit minimal-bundle transversal oracle

**25 October 2026. Mathematical and representation review completed.**

This audit covers `implicit_minimal_bundle_transversal_oracle.md`.
It accepts an implicit implementation of the previously audited full
domination/constellation alternative. The result is not an exact
allocation decision algorithm and does not independently imply a
better Santa Claus approximation factor.

## 1. The implicit graph is finite and its primitive is exact

Vertices represent inclusion-minimal target-B bundles, grouped by
player. Only interplayer resource intersections create edges. The
finite same-class twin count (q+3)(Q+3) exceeds all simultaneously
excluded prefix, candidate and matching records of one class. Choosing
a currently unused twin index avoids any need for a next-distinct-
bundle enumeration oracle.

For a player p, forbidden resources come only from vertices of other
classes. A threshold bundle exists outside them exactly when the
remaining liked-resource total is at least B. Taking a fixed-order
prefix and deleting redundant items in one pass gives inclusion
minimality in the original resource set. No prescribed resource
must remain in the bundle.

The distinction matters: the displayed two-player SUBSET SUM
reduction correctly shows that deciding whether a particular minimal
bundle has any neighbor is NP-hard. A neighboring minimal bundle
containing the shared unit item would have to have remaining total
exactly the specified integer target. The private threshold item
ensures nonempty classes without creating such a neighbor. The
implemented primitive does not solve this problem implicitly.

## 2. Integer effects remove the problematic operations

With mu=rho=epsilon/(100(q+1)), a noncollapsible layer has
U<=mu|X| and |X|-U<=|Y|<=q-1. Therefore U<1 and hence U=0.
All its selected vertices are currently blocked, and their count
is at most q-1. The same injection across the live prefix prevents
a class from reaching the selection cap Q.

A rejected superposed candidate has fewer than mu|X|<1 extras,
so it has none. Retaining the actual most recent candidate makes
the current layer itself maximal; no hypothetical deterministic
rerun or global ordering of exponentially many configurations is
needed. All stable selected vertices already have actual matching
neighbors, so arbitrary-neighbor completion is unnecessary.

The original small-birth exit is also covered at its actual control-
flow position. Its upper bound is below one, so it can fire only
on an empty new candidate, not on a free nonempty configuration
that should first have collapsed. Older layers remain fully blocked.
An isolated configuration may be found during a build, but cannot
remain in a noncollapsible stable layer. Thus no isolated-vertex
preprocessing oracle has been silently assumed.

## 3. The returned certificate is a real minimal-bundle certificate

At the current-blocker stopping check there are no full classes,
extra selected classes or unblocked selected vertices. Consequently
D equals the vertices of the actual induced constellation K.
Current maximality gives domination of every other configuration
in the target classes; centers and blockers dominate each other.

The leaves represent S_0 minus its root, whereas the dominated
set S may omit classes represented only in the last blocker layer.
The distinction S subset S_0 is preserved. The example elsewhere
in the checkpoint shows why one cannot silently identify these sets
when deriving an allocation approximation.

Projection from twins to actual bundles is injective on D. Two
blocked selected twins would share their matching blocker and
violate unique ownership. A selected twin of its own matching
representative would be free, contradicting the stable invariant.
Matching representatives already occupy distinct classes. Projection
therefore preserves the induced constellation and total domination.

For each dominated player, summing its liked resources outside the
other-class resource union of D independently verifies domination
of every unenumerated minimal bundle. An available total at least
B would explicitly produce an undominated witness.

## 4. Cost and limits

Each BuildLayer uses at most q(Q+1) threshold tests. Per-player
availability decreases monotonically, so a failed player need not
be revisited within that build. Resource ownership identifies current
matching blockers; current blocker bundles are disjoint. Scanning
explicit liking lists and retained lists costs P times a polynomial
in q and 1/epsilon per combinatorial iteration.

The audited signature depends on classes and the supplied claw
parameter q+1, not the size of the implicit graph. Substitution
therefore gives the stated quasipolynomial-in-q bound with a linear
explicit-input multiplier and its bit factor. The separately proved
composition count supplies the common exponential fallback. Values
with unrelated rational denominators require a common-denominator
bit-cost analysis, exactly as qualified in the main note.

The optional anchored-family discussion is a separate enlarged
configuration interface: a shared item may be appended to a cached
minimal bundle to construct a neighbor, and value capping bounds
its size. It is not required by the minimal-only theorem and does
not provide an additional approximation guarantee by itself.
