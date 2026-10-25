# Independent audit of binary-capacity current-blocker allocation

**25 October 2026. Independent representation and relaxation audit.**

This audit concerns the new representation in
binary_resource_capacities_compressed_current_blocker.md. It imports,
rather than re-proves, the accepted earliest-circuit exchange rule,
current-layer maximality proof, sharp star charging, and rank-only
micro-signature count. Its purpose is to check whether binary supplies
or per-player type quotas invalidate those imports, or introduce a
hidden dependence on the expanded number of copies.

The representation and the mathematical reduction pass this audit.
The finite implementation conventions in Section 7 should be explicit.
No claim for arbitrary resource-specific matroids follows.

## 1. The exact quotient represented by the cell table

Fix one conceptual set U_j of c_j units of type j. This set is used
only for an existence proof; the implementation stores binary counts.

At every settled state, matching bundles are disjoint, selected
bundles are disjoint, and a unit can have at most one owner of each
kind. Consequently the pair of labels (matching owner, selected owner)
partitions U_j. The numbers z_j[a,b] therefore specify an exact
intersection table, not a relaxation of simultaneous bundle ownership.

Conversely, every nonnegative integer table with sum c_j can be
realized by a partition of this fixed U_j. The required dynamic
realization is stronger than this isolated observation:

* splitting a cell chooses a subset of the units already in it;
* moving a matching row changes only matching-owner tags;
* moving a selected column changes only selected-owner tags;
* merging cells takes their disjoint union.

These operations can be realized inductively without changing a
unit's identity, type, value, or eligibility. In particular, no global
permutation of resource copies is needed to make later cell tables
consistent with earlier ones.

A reused label slot must first have all its old counts moved out and
its blocker/owner metadata cleared. This prevents an old blocker flag
from being inherited by an unrelated new matching bundle.

The bound of at most r matching labels and r selected labels is
inherited from the microstate proof. A fresh free candidate is
provisional and is not inserted into X. A previously stored center
that becomes free was already counted, and a cascade truncates
selected sets rather than adding new ones. Binary capacities do not
change these counting facts.

## 2. Availability must include undiscovered matching rows

For a current forbidden set F=R(X union Y), a unit is available
precisely when its selected label is zero and its matching label
is either zero or not flagged as a blocker in Y. Thus

A_j = sum_{a=0 or a not in Y} z_j[a,0]

is exact.

A unit in an undiscovered matching bundle is intentionally available.
Selecting it is how the algorithm discovers a new blocker. The draft
does not make the invalid simplification of treating all matching
units as forbidden.

Because all copies of a type have identical value and player
eligibility, a player p can take exactly min(a_pj,A_j) units of that
type from the available set. Its maximum available value is therefore

V_p(A) = sum_j v_j min(a_pj,A_j).

The optional quota is imposed on each individual bundle. Different
selected bundles may have the same player label; their quotas need
not be combined because they are alternatives, not simultaneous
output bundles for that player.

## 3. The aggregate relaxation supplies the required strict bound

Let (x,y) be any feasible point of the aggregate perspective
relaxation. For c_j>0 put y_pj/c_j on every conceptual unit of type j.

For each unit, the sum over players is at most one. For each player
the assignment to a unit is at most x_p, because y_pj <= a_pj x_p
and a_pj <= c_j. Its total value is exactly the aggregate fractional
value, so the lift satisfies every demand inequality.

For a forbidden set leaving A_j units of type j, the fractional
outside value of player p is

sum_j v_j A_j y_pj/c_j.

For each type,

A_j y_pj/c_j
 <= x_p A_j a_pj/c_j
 <= x_p min(a_pj,A_j).

The second inequality uses both A_j<=c_j and a_pj<=c_j. Zero-supply
types contribute zero and never require division.

Thus V_p(A)<B implies strictly less than B x_p outside F whenever
x_p>0. The strictness needed by the accepted rank-mass certificate
survives compression.

For clarity, the stand-alone compressed infeasibility certificate is
an independent player set J_0, its closure predicate, counts
0<=A_j<=c_j, and the checks

V_p(A)<B for every p outside cl(J_0),

sum_j v_j(c_j-A_j) <= (T-B)(r-|J_0|),

with r-|J_0|>0. Every feasible base vector has at least r-|J_0|
mass outside that closure. Summing the strict outside-value bounds
then forces strictly more fractional value inside F than the second
display permits. A verifier needs only the counts and matroid
queries, not a listing of the conceptual copies or an execution
history.

## 4. Batched construction really produces a minimal bundle

A type is visited once during initial construction. The number taken
is capped by the player's quota, the available count, and the number
needed to reach B. The current total can be computed exactly on a
common rational grid. If V_p(A)>=B, this process reaches B.

During pruning, removing

min(n_j, floor((V-B)/v_j))

units preserves V>=B. If any unit of the processed type remains,
then V-B<v_j after its pruning step. All later pruning only reduces
V, so removing any remaining unit of that type would still drop the
value below B. This proves inclusion-minimality after one pass.

Deleting units preserves all upper quotas. Consequently the accepted
minimal-bundle facts still apply: a non-singleton minimal B-bundle
contains only units of value below B, and a minimal bundle meeting
a singleton of value at least B is that singleton. The sharp star
coefficient uses the largest unit value, not the aggregate value
of a type.

Counts can be taken from or returned to at most r+1 represented
matching rows per type. There is no loop whose length is the number
of units selected or removed.

## 5. Exchanges preserve the old physical forbidden sets

A newly selected blocked candidate is chosen from the available
cells, so all its matching blockers lie outside the old Y.
A blocker discovered earlier cannot intersect it: all units of that
matching bundle were already forbidden. Thus each discovered blocker
still belongs to exactly one selected center.

A free candidate contains only units with matching label zero.
Removing one old matching bundle changes that row to label zero.
Its unique selected owner is the only stored center that can become
newly free; all other ownership relations are unchanged.

Now consider an earliest-layer exchange at layer j and a strictly
lower retained layer h<j. The removed matching bundle is outside
Y_<=h and cannot intersect X_<=h. Its removal therefore does not
change any unit's membership in the lower forbidden union.
The incoming free bundle avoids all retained selected resources,
and its new matching label is not assigned an earlier blocker flag.
Higher selected columns may be retired, but none belonged to the
lower prefix. The original lower forbidden set is literally the
same subset of the fixed conceptual universe after the exchange.

Eligibility preservation is the imported earliest-circuit span lemma.
Together with the literal resource-set preservation, this retains
the lower layer's old maximality statement. Only the last surviving
layer needs a fresh greedy extension, exactly as in the original
algorithm.

For a stored free candidate, an implementation can assign its
selected column to the new matching row before retiring that higher
column. Alternatively it can save its per-type provisional counts
first. The selected column must not be cleared before its candidate
is recovered. This is an atomic transaction convention, not an
additional combinatorial operation or signature change.

## 6. Fat types and the configuration comparator

For a fat type j, only one unit is required by each chosen fat player.
The corresponding independence system is the capacitated bipartite
transversal matroid with player capacity one and type capacity c_j.
Replacing c_j by min(c_j,q) preserves every query. A standard integral
capacitated bipartite flow graph has one type vertex, rather than c_j
vertices, and polynomial size and numerical encoding.

A per-player type quota matters here only through a_pj>=1. The
decomposition supplies either a small bundle or a single fat unit
to a player, not both. Deleting players in the dual-basis extension
preserves every type capacity and individual quota.

For the configuration-LP comparison, configurations are quota-feasible
integer count vectors. Selecting one fat unit from every fat
configuration gives a fractional capacitated matching. The all-small
marginal for type j is bounded by a_pj times the all-small player mass.
The same scaling to the derived player basis therefore gives the
aggregate small relaxation, including its perspective quotas.

No configuration or copy expansion is required by this existence
argument. The claimed oracle overhead for the union wrapper is a
polynomial full-input multiplier, as stated, rather than a free
unit-cost derived oracle.

## 7. Numerical size, target search, and verdict

The numerical parameter b should retain the main theorem's meaning:
the total bit length of the numerical input. Equivalently one may
include the common-denominator bit length explicitly. The product of
input value denominators has bit length at most the sum of those
input lengths. Counts, value sums, exact ceilings/floors, and target
grid indices consequently have polynomial encoding length.

Put V=sum_j c_j v_j. As in the accepted target-search note, a guaranteed
failed upper target is U_0>V/a when a is the returned-value fraction.
V itself is not necessarily a failed target: success above the
configuration optimum is permitted. The factor 1/a and the common
grid still have polynomial encoding, so the number of target trials
is polynomial even for exponentially large supplies.

Each charged microstate uses a polynomial number of operations in
the explicit types, incidences, players, and at most r owner labels.
The rank-only state count does not depend on expanded supplies.
The input multiplier and bit cost therefore have no hidden factor
sum_j c_j.

Subject to these explicit finite implementation conventions, the
binary-capacity extension passes this independent audit. Its resource
constraints are identical-type supplies and per-player type upper
quotas. It does not provide an oracle or exchange theorem for arbitrary
resource-specific matroids.

