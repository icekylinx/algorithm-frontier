# Constant-depth deterministic raw-length backend

**Status.** A construction-level strengthening of the published deterministic
minimum-ratio-cycle reductions, used as explicit theorem dependencies.
This proof imports their FULL dynamic maintenance guarantees, including
recourse and gradient-preserving lifts. It modifies candidate scoring,
makes the frozen gradient gauge explicit for newly inserted tree edges,
and exposes stable-lifetime callbacks. It does not claim to reconstruct
all internal distance, degree-normalization, portal, or spanner algorithms
from scratch. The scoped independent replacement of the portal
length-decrease and split layer is in
`portal_alias_api_reconstruction.md`, using the hierarchy in
`balanced_two_boundary_hierarchy.md`. It is not needed for the
main theorem-dependent route here. The length cap proposed in an earlier
note is also not used.

For the current candidate there are now two more explicit numerical
dependency chains, summarized in `numerical_backend_choices.md`.
The alias layer together with `constant_degree_steiner_bridge.md`
reconstructs the routing route while invoking the cover/HRG primitives
only at degree three. The independent alternative in
`distance_backend_general_matching_integration.md` uses arbitrary-degree
local distance-sparsifier interfaces. The full-theorem version developed
in this note remains a scoped alternative and supplies the common raw
quality and constant-depth composition arguments.

Fix the OAI parameter `a` and a positive constant `eta`, for example
`eta=1/(100a)`. Constants may depend on these fixed choices. No parameter
tends to infinity within one execution.

## 1. Imported constructive theorems and target interface

The source is Chen, Kyng, Liu, Meierhans and Probst Gutenberg,
*Almost-Linear Time Algorithms for Incremental Graphs: Cycle Detection,
SCCs, s-t Shortest Path, and Minimum-Cost Flow*, arXiv:2311.18295v1:
<https://arxiv.org/abs/2311.18295v1>.

Its Theorem 3.3 reduces a general minimum-ratio-cycle instance to an
explicit family of flat tree-cycle instances. Theorem 3.4 reduces a
tree-cycle instance of size `m` to an instance of size `m A/k`. Both
are invoked with their stated full dynamic maintenance guarantees,
against adaptive updates. In particular, Theorem 3.4 includes the
handling of decreasing portal lengths and the low recursive edit
recourse; we do not simulate those changes by a new sequence of edge
deletions. All local factors can be bounded by

    A=exp(C_{a,eta}(log M)^(83/84) log log M)=M^o_{a,eta}(1).

The static quality ingredients are Lemma 4.32, Definitions 5.3 and
5.6, Lemmas 5.5--5.9, and Lemma 5.14. The explicit spanner routes
and their change bounds come from Theorem 5.13. The dynamic gradient
preservation and flat-forest maintenance are part of the imported
constructive reductions, not inferred from their top-level ratio
statement alone.

For a degree-three physical input of total current size at most `M`,
with integral gradients and positive integral lengths bounded by
`M^O(a)` and polynomially many adaptive edits, the strengthened
construction gives:

* initialization `M^(1+O(eta)+o_{a,eta}(1))`;
* amortized edits and queries `M^(O(eta)+o_{a,eta}(1))`;
* quality loss and occurrence multiplicity `M^o_{a,eta}(1)`;
* at most `M^(eta+o_{a,eta}(1))` oriented edge/path pieces per answer;
* a certified denominator charging literal traversal before cancellation;
* explicit stable-lifetime forest logs with retirement before old images
  or physical metadata become invalid.

A relaxed update exponent `10 eta+o(1)` is sufficient. The constants
multiplying `eta` are absolute.

## 2. What changes, and what does not change

Source Algorithm 2 produces three candidate types: the already maintained
best NET-ratio spanner correction (line 23), a recursively returned cycle,
and a local fundamental tree cycle. Reuse that existing best-correction
selection unchanged. On the one selected explicit correction, coalesce
its signed edge-ID vector in the current abstract portal graph, decompose
the resulting circulation into sign-compatible simple cycles, and keep
the best component. Its ratio is at least the correction's NET ratio,
while its own raw abstract length equals its norm. A zero net correction
cannot improve a nonzero optimum and can be discarded.

The correction has only `A` listed edges, so even a direct `O(A^2)`
cycle decomposition is local subpolynomial work. Compare this component's
pre-lift certificate against the child's RAW certificate and the local
fundamental tree cycle's ordinary simple-cycle score. The latter is simple
in its abstract tree and therefore has literal length equal to its norm.

No new best-raw-correction heap or per-route scalar keys are maintained.
In particular, the wrapper does not need new inverse route-incidence
lists or degree-dependent refresh work. All maintenance needed to select
the best NET correction is already part of the full published constructive
Theorem 3.4. Only the one selected small correction is postprocessed.
This requires no assumption that its route remains simple after auxiliary
vertex identification.

Candidate postprocessing changes no input edge length, graph topology,
portal promotion, auxiliary vertex operation, recursive edit, or period
boundary. The frozen-gauge correction below specifies the gradient of
each newly born direct portal tree edge; it never reprices an existing
edge and adds no recursive edit. The published maintenance transcript
and edit-recourse count therefore remain the same for any fixed input
update sequence. Adaptivity is allowed by the
imported theorem: the outer client may subsequently react to whichever
candidate is returned.

The extra scalar work therefore consists of `O(A^2)` selected-correction
processing and aggregate queries on the returned child pieces. Enlarge
the local subpolynomial factor `A` to absorb its fixed powers. The child
piece count is an ADDITIVE term in the recurrence, not an additional
recursive graph update. There is no global route scan or artificial
child edit.

The proof uses the full constructive theorem in this way. Merely calling
an arbitrary black-box net-ratio oracle and rescoring its answer would
not work: a cancelling detour can make the raw denominator arbitrarily
large. Likewise, replacing every portal length decrease by a deletion
would not be the imported maintenance algorithm and would invalidate
its recurrence.

## 3. The raw-quality induction

A recursive answer consists of a representation `R`, its signed
projection `c(R)`, and a certified denominator `U(R)` with

    raw input traversal length of R <= U(R),
    |g^T c(R)|/U(R) >= OPT/Q.

A parent compares these certificates without replacing the denominator
by the norm of a cancelled projection.

### Spanner reduction

Let `H` have explicit routes `pi(e)` of length at most `rho ell_e`.
For a non-spanner edge set `z_e=e-pi(e)` and retain that literal route.
For any comparison circulation `Delta`, put

    Delta_H=Delta-sum_{e outside H} Delta_e z_e.

It is supported on `H`, and directly from its coefficients,

    ||L Delta_H||_1 <= rho ||L Delta||_1,
    sum_e |Delta_e| raw(z_e) <= (1+rho)||L Delta||_1.

The numerator splits exactly. Averaging gives a raw correction or a
child optimum with score at least `OPT/(3rho)`. A child loss `Q` gives
loss at most `3rho Q`. If auxiliary vertices are identified, retain
edge identities and the pre-identification route denominator; repeated
vertices in the image walk cause no difficulty.

The primary implementation uses the published NET-ratio Lemma 5.14
directly. Its averaging says either the best NET correction has score
at least `OPT/(3rho)`, or the child optimum does. Apply simple-cycle
extraction only to the already selected best correction. Its best
component has at least that correction's net score and has raw abstract
length equal to its norm. The child supplies its RAW certificate with
loss `Q`. Comparing these two candidates therefore gives loss at most
`3rho Q`. The selected correction is small and explicit, which is
essential; cheap decomposition is not asserted for an arbitrary final
implicit physical walk.

### Flat tree family

Lemma 4.32 compares the optimum to a fundamental cycle in one maintained
abstract tree. That cycle is simple in the tree plus one edge. Real
occurrences have length at least their physical image length; null
occurrences have zero physical gradient and raw charge. The strengthened
tree-cycle oracle therefore preserves the published comparison with its
local factor `A`.

### Portal lift

At a portal period's beginning, fix a potential `pi` on the initial
forest `T_init` such that

    bar_g(e)=g(e)+pi(tail(e))-pi(head(e))=0

on every initial tree edge. Keep this potential fixed; a new isolated
vertex can receive potential zero. Both endpoints are promoted before
a tree-edge edit. Consequently a newly inserted tree edge is a direct
edge between portals and must retain its actual residual gradient
`bar_g(e)`, which need not be zero. Every dangling leg consists solely
of surviving `T_init` edges: a subsequently inserted tree edge has
portal endpoints and cannot lie inside such a leg. Thus unchanged
off-tree edges and all their current portal routes have fixed residual
gradient `bar_g(e)`, initial compressed tree paths have gradient zero,
and newly inserted direct tree edges carry their residual gradients.
Potential terms telescope on every circulation. This is the explicit
dynamic convention needed for Remark 5.4: zeroing every new tree edge
would be incorrect. It changes only values supplied at edge births,
not the number of updates or their topological form.

Use the explicit forest lift in Definition 5.6 and Lemma 5.8. A child
forest path becomes the unique path in the lifted forest after removing
tree backtracking. Its signed projection is unchanged and raw length
cannot increase. An off-tree portal edge adds its two dangling-tree
legs and central parent edge. Consecutive tree legs can be concatenated.
Thus piece count grows by at most an absolute constant per main level.
The imported lift preserves cycle gradients exactly. Portal comparison
cycles partition the corresponding parent fundamental cycles into
successive segments of their actual length.

There are two explicit edge cases. A child null forest edge whose two
endpoints map to the same portal lifts to a null edge between the roots
of their two dangling copies; its physical charge and gradient are zero.
Contracting dangling copies still gives exactly the child forest. A
single child input edge can itself be a portal tree-path edge, not a
portal-routed off-tree edge. Represent it by its one path in the extra
copy of the current parent tree described below. This has exactly its
stored path length and the correct gradient, and adds only one piece.
These cases are needed beyond the routed-edge case spelled out in the
source proof of Lemma 5.8.

Keep one additional disjoint copy of the current parent tree `T` in
each tree-cycle call. It represents the local fundamental candidate
when it contains fewer than two portals, including a portal-free
component. This adds one occurrence per parent vertex and constant
forest changes per tree-edge edit. No claim that every such local path
already lies in the recursive portal lift is needed.

The local-candidate set explicitly includes **one-portal** fundamental
cycles as well as zero-portal cycles. Maintain their keys in a separate
heap. Initialization scans the current off-tree edges. A promotion
changes the local/routed status of only the `O(k)` off-tree edges in
the affected original piece, by the source portal-maintenance bound;
their current simple-cycle gradients and lengths are read from the
extra copy of `T`. An off-tree insertion or deletion changes its own
record. Before any tree-edge edit, both endpoints are promoted. Hence
any old fundamental cycle containing that tree edge already contains
at least two portals and has left this local heap. All remaining old
local cycles retain their tree path and key. New tree edges cannot
change a surviving old off-tree path under the legal tree-cycle edit
contract. Thus the extra heap costs only local `k^O(1) A` work and
creates no recursive graph edits. This supplies the fewer-than-two-
portal case explicitly rather than relying on the source algorithm's
phrase 'contains no portals'.

Here the legal contract is literal Definition 3.2: after every tree
edit, no surviving off-tree edge joins different tree components. The
full constructive Theorem 3.3 is imported as supplying that interface.
The short proof in the source does not independently spell out the
ordering of every HRG tree exchange and off-edge update. Neither this
heap argument nor the optional fixed-target reconstruction silently
extends to arbitrary batched exchanges retaining crossing off-edges.

These three arguments prove the raw-score invariant by induction.
Constant factors only change the local `A` bound.

## 4. Exact base and numerical aspect

Set `k=ceil(M^eta)` using the outer nominal size. Use total active
vertices plus edges for recursive size; isolated slots may alternatively
be stored separately because they cannot occur in a cycle. Stop when
this active size is at most `k`.

Test whether all cycle gradients vanish using a spanning-forest
potential. Otherwise, after clearing common dyadic scales, a simple
cycle has nonzero integral gradient. Its positive optimum is between
`1/(k ell_max)` and `max_e |g_e|/ell_e`.

For a trial `q>0`, give the two orientations of an edge weights
`q ell_e-g_e` and `q ell_e+g_e`. A negative directed cycle exists
exactly when a circulation has ratio greater than `q`. Start at an
upper bound and halve until finding the first negative cycle. The
previous failed trial proves factor-two quality. Bellman--Ford returns
a simple negative cycle. A forward/reverse traversal of the same edge
has zero gradient and positive length and cannot be negative for `q>0`.
The conservative base running time is `k^3 polylog M`, with at most
`k` explicit edge occurrences in the answer.

The main recursion has constant depth. In the HRG step specifically,
the proof of Lemma 4.32 chooses
`gamma_diam=exp(O(log^(83/84) m))`, without a `log log m` in this
exponent, and `kappa_HRG=log^(1/84) m`. Therefore its largest hierarchy
scale `gamma_diam^kappa_HRG` is polynomial; the constants can accommodate
the current fixed polynomial input aspect. Allowing a polynomial increase
in length, gradient magnitude, or inverse connector scale at each
level therefore still leaves polynomial aspect, with constants
 depending on `a,eta`. This is sufficient for the imported distance
primitives to retain local subpolynomial factors. No cap on a deep
edge's length in terms of its final physical lift is required.

The extra raw-score operations use exact sums, differences, path
aggregates, and cross-multiplied ratio comparisons. They require
`O_{a,eta}(log M)`-bit values, or the polylogarithmic precision already
allowed by the imported primitives. Source Remark 1.5 records the
fixed-point precision dependency. This proof does not independently
reprove each numerical subroutine of that framework, and adds no new
real-number comparison oracle.

## 5. Constant-depth recurrence

For sufficiently large `M`, enlarge `A` to absorb all local logarithms
and assume `A^2<=k^(1/2)`. One combined reduction maps size `m` to at
most `m A^2/k<=m/k^(1/2)`. Hence depth `D<=2/eta+O(1)` is constant.
Do not multiply a final global MRC factor at every recursion level.

For multiplicity `F_d`, pieces `P_d`, and quality loss `Q_d`,

    F_d <= A(F_{d-1}+1),       F_0=O(1),
    P_d <= C max(P_{d-1},A),   P_0<=k,
    Q_d <= C A Q_{d-1},        Q_0=2.

Thus `F_D,Q_D<=A^O(D)=M^o_{a,eta}(1)` and
`P_D<=k A^O(D)=M^(eta+o_{a,eta}(1))`.

For initialization, explicitly charge writing the lifted occurrence
forests as well as the imported initialization. After enlarging `A`,

    I_d(m)<=m A(F_{d-1}+1)+A I_{d-1}(m A/k).

The additional factor is necessary if the `F_{d-1}` dangling-copy
records are explicitly exposed rather than represented by shared
templates. The base `I_0(t)<=t k^2 A` still gives
`I_d(m)<=m k^2 A^O(D)`. Rebuilding these local copies once per `m/k`
edits costs `k A(F_{d-1}+1)` per edit, already absorbed by the local
`k^2 F_{d-1}` term after enlarging `A`.
The update recurrence is

    U_d <= A [k^2 F_{d-1}+(k/m)I(m A/k)
              +U_{d-1}+P_{d-1}].

Its terms pay for local portal/spanner work, period rebuilds,
LOW-RECOURSE child edits supplied by the FULL imported Theorem 3.4,
and additional candidate-score access. The second term is
`k^2 A^O(D)`; the `k^3 A` base gives `U_D<=k^3 A^O(D)`.
The relaxed `k^10 A^O(D)` bound allows further constant polynomial
bookkeeping. No factor `k` multiplies the child update term.

## 6. Stable occurrences and actual motion

Source Theorem 4.1 explicitly exposes forest/map changes. Theorems
6.2 and 6.3 give fixed images during an occurrence's lifetime. Lemma
5.9 propagates recursive forest edits through the portal lift. Lemma
2.7 supplies signed path additions, separate positive absolute path
additions, point values, and threshold detection. Theorem 3.6 flushes
motion when a mapped forest edge changes.

Use the preallocation in source Algorithm 1, lines 13--16. For every
current portal `p`, reserve `Gamma_child` dangling copies of `T_p`, where
`Gamma_child` is a fixed valid upper bound for child occurrence
multiplicity during this period. A child occurrence mapped to `p`
attaches to an available copy; it does not construct a whole `T_p` at
its birth. Initially an individual `T_p` can be large at a high-degree
portal, but branch-freeness bounds the TOTAL volume of all `T_p` by
`O(m)`. Thus initial allocation costs `O(m Gamma_child)`, as charged
above. A newly promoted interior portal affects only its old `O(k)`-
volume piece, so preparing its copies and editing old copies is local
`O(k Gamma_child)` work, within the portal budget.

When a child occurrence retires, first retire its actual connecting
edge occurrences, flushing their values. Its reserved dangling copy
then becomes dormant. Keep the internal dangling edges, their physical
images, identifiers, and accumulated signed AND absolute motion alive.
Reusing that copy for a later child occurrence at the same portal does
not reset these counters. It adds future motion to the already recorded
physical motion. Only genuinely deleted internal edges are flushed;
all remaining copies are flushed at the period rebuild, paid by the
`m Gamma_child` initialization/retirement budget. This is precisely the
representation-independent value convention used in OAI05's dormant-arm
discussion after its equation (value-invariant). An old accumulated
increment need not remain a circulation in the current forest; every
NEW update must have a circulation as its physical projection.

An optional explicit implementation avoids needing the hidden constant
in an asymptotic bound for `Gamma_child`. Give each portal a geometrically
growing pool, doubling it when the observed simultaneous child
occurrences exhaust its free copies. Only the newly allocated copies
are built, using the CURRENT `T_p`, with zero counters. Every old and
dormant copy retains its counters. Within a period `T_p` only shrinks:
portals are permanent, and new tree edges join portals. Thus total copy
construction for `p` is at most a constant times its maximum simultaneous
occurrence count times `|T_p|` at its birth. Summed over the period this is

    O((m + Q k polylog m)(F_child+1)),

where `Q` is the number of parent edits so far; the polylogarithm also
allows the optional hierarchy's extra promotions. Initial dangling
volume is `O(m)` and each new interior portal has `O(k)` birth volume.
Pool capacity is at most twice the observed maximum, so dormant pools
increase congestion by only a constant factor. A late doubling can be
large: this is an aggregate/amortized bound, charged to the displayed
initialization allowance and completed-period rebuilding charges, not
an `O(1)` worst-case claim for each child-vertex birth. It changes no
recursive graph update count and gives a directly computable finite
implementation without guessing an asymptotic congestion constant.

Give each actual physical forest-record birth a fresh identifier; merely
reassigning a dormant copy is not such a birth. Every nonnull occurrence also keeps
its actual input edge identifier and endpoint correspondence, inherited
through the constructive lift. A vertex map alone does not distinguish
parallel physical edges. Null records are explicitly tagged. The source
flow-maintenance interface (Theorem 3.6) already requires identifying
the exact input edge image; the wrapper retains that witness and its
old metadata through retirement. Retained records keep their image
and accumulated signed/absolute motion. An endpoint or image change
is retirement followed by a birth. Flush before cutting and before
invalidating old input metadata; new records start at zero. No client
path query occurs inside a deletion-first transaction.

At the final physical level degree is three. A forest occurrence has
at most `O(F_D)` possible neighbors, since their images are its own
slot or one of three neighbors. Expanding a vertex-map replacement
into incident edge retirements adds only a subpolynomial factor.
Retain explicit identities for parallel edges. Flush signed motion
and accumulated absolute motion separately, so cancellation cannot
erase refresh debt.

The exact physical raw score of an answer is obtained through path
aggregates and listed pieces, in `P_D polylog M` time already charged
above. No represented walk is scanned edge by edge. Its physical raw
length is bounded by the recursive selection certificate.

## 7. Fixed-parameter OAI consequence and scope

With `eta=1/(100a)`, eventually multiplicity fits `M^(10/a)/4` and
relative raw quality exceeds `M^(-10/a)`. The relaxed update exponent
is at most `1/(10a)+o_a(1)`; pieces have exponent
`1/(100a)+o_a(1)`. Initialization has the required
`M^(1+O(1/a)+o_a(1))` form. The construction is deterministic against
adaptive clients, with no seed search or stochastic retry.

Standard size/arithmetic guards may remain. At each fixed sufficiently
large `a`, these estimates imply eventual adequacy. A classical exact
fallback at finite exceptional sizes does not change an eventual
asymptotic exponent.

The current `persistent_carrier_general_matching.md` has near-linear
structural phase work and therefore permits every positive fixed
exponent slack. The exact optimum offset and direct gap driver are in
`general_graph_gap_reduction.md`; its graph has size Theta(m_s) after
cleanup. The single uniform program is assembled separately in
`uniform_general_maximum_matching.md`. Earlier one-third compositions
are preserved in the preceding historical checkpoint archives.

**Dependency boundary.** The proof imports the stated arbitrary-graph
constructive Theorems 3.3/3.4, including their internal degree
normalization, decreasing-length handling, low recursive recourse,
and gradient-preserving lifts. An independent reconstruction of all
those published internals is outside this proof. The independent alias
reconstruction in `portal_alias_api_reconstruction.md` gives a legal
spanner-API implementation of the portal layer, including arbitrary
tree exchanges retaining crossing off-edges. It is optional and is
not an additional premise of the present theorem-dependent route.

## 8. Scoped independent portal-layer replacement

The new alias construction replaces the decreases missing from the
displayed spanner API by geometric parallel insertions. Every old
endpoint has only the actually promoted ancestor separators of a fixed
balanced hierarchy as targets. There are `O(log k)` targets and
`O(log^2 k)` endpoint-pair variants per edge. The first current portal
on a fixed initial-tree target path gives a valid, monotonically
shortening dangling leg, even if the distant target is later cut off.

Immutable target-origin slots share all variants with the same own
endpoint and target. Fixed old inventories and fresh singleton masters
for true births bound the master degree even when deletions and splits
are ignored. Expensive spanner operations number only polylogarithmically
many per parent edit. An `O(k polylog M)` local inventory scan does not
emit that many child edits: only actual retained spanner memberships
whose portal endpoints change do so, and each endpoint changes only
`O(log k)` times per membership lifetime.

This gives child size `m A/k`, child edits `(m/k+Q) A`, and local work
`m A+Q k^2 A`, with no factor `k` on the recursive update term.
It also gives an extended tree-cycle interface permitting off-edges
across current tree components. Every returned cycle remains a valid
parent circulation; quality is compared with current fundamental tree
cycles, which have the necessary first/last boundary-target variant.

The reconstruction still imports the dynamic spanner, static weighted
decomposition, and flat-lift maintenance. It does not by itself resolve
the independent arbitrary-degree general-cycle normalization bridge.
Ordinary vertex splitting followed by unrestricted collapse would
multiply vertex occurrence bounds by degree, and that shortcut is not
used as a proof of the required bound. The main route's full
unrestricted Theorem 3.3 import remains explicit.

## 9. Completing the scoped routing reconstruction

The portal layer alone did not control an arbitrary high-degree
vertex's occurrence count. The new
`constant_degree_steiner_bridge.md` addresses that precise boundary.
It proves that the particular tree-cycle instances generated from
degree-three input have subpolynomial degree, coalesces retained aliases
at their original endpoints, and routes their legs in a compressed
Steiner forest. The resulting geometric graph inherits that degree.
A fixed finite port fiber restores degree three for the recursive child.

Compressed physical paths are copied at the lifetime of a child INPUT
edge and reused across its occurrence edits. Lazy doubling of each pool
requires no hidden congestion constant. The lift has multiplicity
A_* times the child's, while an individual recursive forest record
causes only constantly many attachment changes. Expensive path-pool
creation and retirement is charged to the controlled geometric input
edits. The local A_* includes the computable port capacity, for example
exp(C_(a,eta)(log M)^(167/168) loglog(M+2)); using the old 83/84
formula for this enlarged factor would be incorrect.

With the alias reconstruction, this gives an alternative proof of the
scoped interface used here without an unrestricted split-and-collapse
assumption. The constant-degree source algorithms, dynamic spanner,
finite arithmetic guarantees and OAI outer client remain explicit
imports. The second distance-sparsifier route avoids this bridge rather
than relying on its conclusion.
