# A constant-degree geometric bridge for the recursive cycle backend

**Abstract.** We prove a geometric reduction from a bounded-degree tree-cycle instance to a degree-three recursive input. Retained portal aliases are coalesced at their original endpoints, compressed Steiner paths provide their tree legs, and bounded port fibers reduce degree. Input-edge path pools make recursive forest-log work independent of the expanded path length.

The reduction assumes the [portal-period theorem](portal-alias-api-reconstruction.md), the [disconnected-component decomposition](disconnected-routing-components.md), and the [explicit lifetime interface](numerical-backend-lifetime-and-loops.md). The latter keeps dormant copies on signed and absolute-motion lists and completes retirement before invalidating their provenance. These are stronger requirements than a scalar cycle approximation. The [main matching proof](../../problems/general-matching/proof.md) retains complete raw-backend realization as Contract R.

## 1. Source boundary and notation

The source is Chen, Kyng, Liu, Meierhans and Probst Gutenberg,
*Almost-Linear Time Algorithms for Incremental Graphs: Cycle Detection,
SCCs, s-t Shortest Path, and Minimum-Cost Flow*, arXiv:2311.18295v1:
<https://arxiv.org/abs/2311.18295v1>.

We use Theorems 4.1 and 4.5 **only on degree-three inputs**, and use the
tree collection and off-tree edges of Definitions 4.28--4.30 and Lemma
4.32. The legal dynamic spanner API is Theorem 5.13. No invocation of an
unstated arbitrary-degree neighborhood-cover theorem is made.

Let M be the outer power-of-two size bound and let `k=M^eta`, rounded
up, for a fixed positive eta. Each local portal period starts with size
m and contains at most `Q<=m/k` parent updates. All static and dynamic
sizes count vertices as well as edges. Let A denote an enlarged local
subpolynomial factor, absorbing fixed powers of source parameters,
polylogarithms, and the computable port capacity specified below.
In particular, after introducing that capacity we use an enlarged
factor of the form

    A_star = exp(O_a((log M)^(167/168) log log(M+4))) = M^{o_a(1)},

and may write A for A_star. It cannot be absorbed into the source's
smaller exponent `83/84`. Products of these factors remain subpolynomial
here because the recursion depth is fixed for each parameter value;
we are not reusing the source's growing-depth exponent calculation.

**Theorem 1 (conditional geometric bridge).** Suppose the cover/HRG instances have the explicit flat-edge provenance, degree and occurrence bounds below; the portal layer supplies its immutable alias transcript; and the recursive child supports the stated forest logs and retirement callbacks. With all local factors absorbed into $`A`$, the reduction maintains these invariants:

* every recursive general-cycle graph has degree at most three;
* its tree-cycle subinstances have degree at most A;
* a tree-cycle subinstance reduces to a degree-three general graph of
  size `m A/k`, with only `(m/k+Q) A` child updates;
* its exported flat forest has occurrence multiplicity at most A times
  the child's multiplicity, and has no k factor on recursive log volume.

## 2. Degree of a tree-cycle instance from a degree-three input

**Lemma 2.** For a degree-three general input, one HRG tree-cycle instance has maximum degree at most $`4\kappa(\gamma+1)+2\gamma+3`$.

**Proof.** Let G be the degree-three input to the source's hierarchical routing
construction. Write gamma for the routing-forest vertex-congestion
bound and kappa for the number of routing levels. The vertex map of
one hierarchical routing tree T into G has congestion at most

    B = kappa (gamma+1).

This counts the kappa copies `V_i` and the routing forests `F_i` in
Definition 4.2. A vertex x of T maps to some vertex v of G. Every
neighbor of x in the forest T maps either to v or to one of v's at most
three neighbors. There are at most `4B` possible neighboring occurrence
vertices. Since T is a forest, it has no parallel edges between a
fixed pair of its vertices. Therefore

    deg_T(x) <= 4B.

The off-tree set has two parts, as in Definition 4.28.

1. `E_graph` contains one copy of each input edge on `V_1`, so its
   degree contribution is at most three.
2. An edge of `E_pair` joins two out-neighbors in `F_i` of the same
   vertex of `V_i`. A fixed endpoint x can be an out-neighbor of only
   the unique `V_i` vertex with the same physical image. That vertex
   has at most gamma out-neighbors. Thus `E_pair` contributes at most
   a constant multiple of gamma to x's degree, allowing both
   orientations in a conservative count.

Consequently the full tree-cycle input `J=T union E_off` has

    maximum degree D <= 4B + 2 gamma + 3 = M^{o(1)}.

This conclusion does not assume that an arbitrary flat graph has low
degree. It uses the explicit forest and off-edge construction of this
particular routing reduction. The same bound applies throughout its legal update transcript, with a constant-factor allowance for a deletion-first transaction. ∎

## 3. The retained geometric graph

Fix the period's potential pi on the parent graph J, and write

    bar_g(e) = g(e) + pi(tail(e)) - pi(head(e))

for EVERY current parent edge, both tree and off-tree. Initial T0
edges have zero residual; a new tree-edge lifetime has its actual
residual in this same frozen gauge. Lengths below are the real original
positive lengths, with no gauge change.

Use the portal alias construction on J. It maintains a physical portal
set P, an auxiliary spanner H, and for each retained alias its original
off-edge lifetime `e=(u,v)`. Such an alias has a current physical walk

    p --T--> u --e--> v --T--> q

with stored length lambda at least the raw length of this walk. Its
gradient is the fixed-gauge value `bar_g(e)`. An H tree-path edge is a
current path of T between portals.

For each original off-edge lifetime e maintain a reference count of
its retained H aliases. Define E_star to contain e exactly when this
count is positive. **All aliases of e are coalesced into this one
central edge**, at the original endpoints u and v, with its actual
original length `ell_e` and gradient `bar_g(e)`. Parallel original
edges keep distinct original lifetime IDs.

Let the terminal set Z consist of every permanent portal and every
endpoint of an edge in E_star. Let K be the compressed minimal Steiner
forest of current T on Z: retain the terminal vertices and the necessary
branch vertices, and replace each intervening degree-two path by one
oriented edge f=(x,y). If P_f is its oriented current T path, its two
labels are explicitly

    ell_S(f)   = sum_(e traversed by P_f) ell_J(e),
    bar_g_S(f) = sum_(e traversed by P_f) sign(P_f,e) * bar_g_J(e).

In particular the K path uses the SAME frozen-gauge residuals as the
central edges. Mixing original tree gradients with gauged central
gradients is incorrect. The geometric graph S is

    S = K union E_star.

The degree of a vertex of K is at most its degree in T. Coalescing the
aliases means that E_star is a subset of the original off-edge set.
Hence

    maximum degree of S <= D,
    |V(S)|+|E(S)| = O(|H|+|P|).

H endpoint remaps do not change a central edge of S: its endpoints are
always the original u and v. They can change H's explicit route data,
but produce no geometric edge update merely by moving a portal endpoint.

### Circulation-preserving geometric lift

**Lemma 3.** Every circulation of the retained portal graph has a circulation lift in the geometric graph with the same frozen-gauge numerator and no larger literal length.

**Proof.** For a retained H alias of e, both its portal endpoints and u,v are
terminals. Its two current dangling legs are therefore present in K.
Map that H edge to its two K legs and central edge e. The resulting
walk has the same RESIDUAL gradient and length at most lambda. Map an H
tree-path edge to its corresponding K path.

Extending linearly, every circulation in H maps to a circulation in S
with the same numerator and no larger norm. After lifting that complete
circulation to J, the potential terms telescope, so its residual
numerator equals its ORIGINAL physical-gradient numerator. This equality
is asserted for a circulation, not for each individual open lifted leg.
Therefore an approximate
cycle oracle on S is a sufficient replacement for the child oracle on
H in the spanner decomposition. S can contain additional useful cycles;
all of them have actual current J walks as lifts. ∎

The full net/raw comparison, including an explicit counterexample to
mixed gauges and the effect of coalescing repeated alias centers, is in
[alias-geometric-raw-bridge.md](alias-geometric-raw-bridge.md).

## 4. Maintaining K using a fixed initial forest

Freeze the initial tree forest T0 for the portal period. Every endpoint
of a tree edit is promoted before that edit, and portals are permanent
through the period.

Maintain the compressed Steiner forest K0 of T0 on the dynamic terminal
set Z, using fixed DFS order and LCA information in each initial T0
component. If an initial T0 edge has ever been retired, both of its
endpoints are permanent terminals. It is consequently a **direct edge
of K0**, with no other vertex in its compressed interior, for the rest
of the period. Mark that direct edge absent from the current geometric
forest. Insert each new current tree-edge lifetime separately as a
direct edge between its terminal endpoints. Thus

    K = (K0 with retired T0 edges suppressed)
        union current noninitial tree-edge lifetimes.

A repriced or reinserted old edge is a new lifetime in the second term;
its obsolete initial lifetime stays suppressed.

This expression is a subforest of current T. Inside each component
obtained by deleting the retired T0 edges, K0 restricts to the correct
terminal Steiner tree: every cut boundary is itself terminal. New
tree links join terminal vertices directly. It follows that K contains
every current T path between terminals in the same current component.

No current-tree Euler renumbering is needed. A host-tree edit changes
only one direct compressed edge after its endpoint promotions. A
terminal insertion/deletion is handled in the fixed T0 virtual tree.

### Explicit virtual-tree update bound

**Lemma 4.** A terminal insertion or deletion in the compressed Steiner forest of the fixed initial tree has constant structural recourse and logarithmic search/update work, assuming the stated ordered-set, LCA, and dynamic-path primitives.

**Proof.** A terminal insertion has constant structural
recourse. In the cyclic DFS order, find its predecessor and successor
among the existing terminals of that initial component. The projection
of the new terminal onto the old minimal Steiner subtree is the median
of these three vertices, computable from their LCAs. If it lies inside
one compressed edge, split that edge. Attach the new terminal by its
one path to this projection; if the terminal already lies in the old
Steiner subtree, only the possible edge split and marking are needed.
The predecessor/successor fact follows from the contiguous DFS interval
of the branch leading from the projection to the new terminal: that
interval contains no old terminal, and its two cyclic neighbors give
the relevant boundary path.

To locate the compressed edge containing an unrepresented projection
y, expose the K0 path between those two old terminals and select the
edge at prefix distance `dist_T0(predecessor,y)`. Store the number of
physical tree edges in every compressed edge as an additional path-sum
weight. Static T0 LCA data gives that distance, and ordinary dynamic-tree
path selection gives the edge in logarithmic time. Thus finding the
split location does not scan the expanded length-k path. Coincident
predecessor/successor and already represented projections are handled
directly.

On deletion, unmark the terminal. A nonterminal leaf is removed, and a
nonterminal degree-two vertex is suppressed. Only its former neighbor
can newly have degree two; after that one suppression the other degrees
are unchanged. A branching vertex stays. Singleton components are
handled directly. Balanced ordered dictionaries and static LCA queries
therefore give `O(log m)` time and at most `O(log m)` edge/vertex edits
per terminal update; the weaker logarithmic recourse bound is enough. ∎

Reference counts avoid unnecessary terminal deletions while another
retained original off-edge still uses the same endpoint. Portals have
permanent terminal marks. A geometric anchor vertex gets one stable
logical ID for its **parent DTC vertex lifetime**, even if it later
ceases to be a terminal or Steiner branch and then reappears.

### Length of an expanded compressed edge

All portals belong to Z. Therefore a compressed K0 edge has no portal
in its interior. It lies in one of the initial `O(k)`-volume pieces,
or in an initially portal-free component of that size. Its physical
path has `O(k)` vertices. New tree edges are direct. The initial piece
volume includes tree vertices, not just off-edge incidences.

## 5. A computable degree-three port expansion

Let `M=2^u` and choose the fixed integer capacity

    C = 2^ceil(u^(167/168)).

The integer exponent can be computed by integer power comparisons; no
real-number oracle or asymptotic constant is required. Check that the
actual DTC degree and every geometric degree are at most C. Suspend
this fixed-parameter branch on overflow. For each fixed outer parameter,
the source degree bound has the form

    exp(O_a(u^(83/84) log(u+2))),

which is eventually smaller than C. Thus the guard does not alter the
eventual fixed-parameter running time or correctness assertion. It
does protect the stated finite port invariant.

When a parent vertex lifetime first becomes a geometric anchor,
allocate one complete binary tree with C leaves. All its nodes map to
that same parent vertex. Keep the tree for the rest of the local period.
It has a stable pool of leaf ports. Each incident geometric edge takes
a distinct free port, and returns it on deletion; a geometric self-loop
takes two distinct ports. No new fiber is allocated merely because a
vertex disappears and reappears as an anchor. Capacity is checked
before assigning a port.

Replace each geometric edge by an edge between its two assigned leaf
ports. All binary-tree connectors remain. The resulting recursive
general graph B has maximum degree three under every intermediate
edge insertion/deletion, not just at settled states. A new fiber can
be inserted as isolated slots followed by its tree edges, preserving
that bound. Retired anchor fibers may remain internally as isolated
null trees; their physical export is controlled in Section 8.

There are only `O((m/k+Q) A)` anchor births during a period, because
each is an initial anchor or appears in a virtual-tree update charged
to a retained H edge or a new portal. Multiplication by C is another
subpolynomial factor. Therefore all allocated fibers, including the
historical inactive ones, fit in `m A/k` child size during the period.

### Positive null lengths and finite precision

Use the integral parent scale. Multiply the length **and gradient** of
every nonfiber geometric edge by `H_scale=M^10`, and give every binary
fiber connector length one and gradient zero. Its physical lift is
null. Consequently all child lengths are positive integers.

A passage through a fiber uses at most `2 log_2 C` connector edges.
Every geometric edge has original length at least one. Routing a
circulation through the fibers therefore adds at most

    2 log_2 C * sum_e |d_e|
      <= 2 log_2 C * sum_e ell_e |d_e|

to its scaled length. Since `H_scale` dominates `2 log_2 C`, the total
length is at most twice the scaled geometric length. Its gradient is
exactly `H_scale` times the geometric gradient. Conversely every child
cycle projects with that same gradient factor and no more than its
length divided by `H_scale` in physical raw length; fiber traversals
project to zero. Thus this expansion loses only a constant in quality.

The returned raw certificate is rescaled explicitly: if the child
returns numerator N_child and denominator U_child, the parent uses
`N_child/H_scale` and `U_child/H_scale`. Keeping U_child unchanged
would incorrectly lose a factor H_scale. These are exact dyadic
quantities because M is a power of two. One can equivalently maintain
a common explicit scale through the constant-depth recursion.

For a complete child circulation z, its signed physical projection c
satisfies `g_child^T z = H_scale * g_parent^T c`: the frozen gauge
telescopes, and fiber connectors contribute zero. Therefore a selected
nonzero child numerator cannot project to zero. It also implies positive
physical raw length because every real parent edge has positive length.
A purely null cycle has numerator zero and cannot supply a nonzero
ratio certificate. A real loop is kept as a real edge identity, even
when its physical endpoints agree; it is not converted to a null edge.

At constant recursion depth, the scaling adds `O(log M)` bits per
level. Parent tree-path sums and frozen gauge potentials have polynomial
magnitude. All arithmetic still uses `O_a(log M)` bits. If a different
fixed dyadic parent unit is used, first clear that declared period-wide
unit; future allowed insertions use the same unit.

## 6. Input-edge path pools, not per-log path expansion

The edges of B come in three types:

* a central selected original off-edge, whose physical lift is one
  parent edge;
* a compressed K edge, whose physical lift is its `O(k)`-vertex
  parent-tree path;
* a fiber connector, whose physical lift is null.

Let Gamma denote the uniform vertex-occurrence bound of the recursive
child's flat forest for analysis. For each current nonnull B input edge
f, maintain a pool of disjoint copies of its physical path, with stable
endpoint correspondence and images. One can preallocate `2 Gamma`
copies at the input-edge birth if a declared bound is supplied. The
preferred executable version starts with one canonical copy and doubles
the pool whenever no free copy remains. It does not need Gamma as
advice. All copies remain part of the parent's exposed forest even
while unused, as isolated path components.

A forest with at most Gamma occurrences of each B input vertex has
at most `2 Gamma-1` forest edges mapping to a fixed B input edge with
distinct endpoints: the relevant edges form a forest on at most
`2 Gamma` occurrence vertices. With doubling, the total number of
copies ever allocated during this fixed input lifetime is less than
twice the maximum of one and the largest simultaneous requirement,
and hence at most `4 Gamma`. The cumulative copying work, even when
performed late, is therefore `O(Gamma)` times this one physical path's
size. It is charged to that INPUT lifetime, rather than once per child
forest log. Initially present input lifetimes have this initialization
credit even if their copies are materialized lazily. An explicit final
occurrence-budget guard can still stop a finite branch on overflow.

When a child forest edge mapping to f is born, take one free path copy
and connect its endpoints to the two corresponding child occurrence
vertices by two null edges. On removal, delete those two null
connections and return the copy to the pool. Its internal edges and
their accumulated signed/absolute motion are retained; they are not
silently reset. A child edge mapping to a fiber connector, or a true
null child edge, becomes a direct null parent edge and needs no long
path pool.

Contracting each assigned path copy with its two endpoint attachments
gives the child forest; unused copies are disjoint trees. The result is
therefore a forest. An entire child forest path lifts to one parent
forest path between the corresponding occurrence endpoints. A queried
single nonnull B input edge can use any one of its pool paths, by its
own two pool endpoints, with the requested orientation. Its current
assignment status is irrelevant to that path's physical projection.

Only when the **B input-edge lifetime** f is retired must its entire
pool be flushed and removed. First retire all old child connections
and reconcile the child forest logs, then flush the path copies before
invalidating their physical metadata. A no-parent-query transaction
permits this deletion-first ordering. The old parent graph data remains
available throughout retirement.

This distinction is essential. Expanding a length-k path afresh on
every child forest-edge log would put a factor k on recursive log
volume. Here the expensive `O(k Gamma)` work is charged only to births
and deaths of geometric B **input edges**, whose count is controlled
by H/virtual-tree recourse. Each recursive child forest log needs only
constant additional parent forest edits.

## 7. Occurrence bounds of the geometric lift

The interiors of distinct compressed K paths are disjoint. At a parent
vertex v that is an anchor, the number of incident geometric edges is
at most D. Their path-pool endpoints contribute `O(D Gamma)` copies of
v. A nonanchor v lies in the interior of at most one K path and thus
has `O(Gamma)` pool copies. Selected central off-edge pools contribute
at most `O(D Gamma)` endpoints at any v.

The child occurrence vertices themselves map through the fixed port
fiber. A parent vertex has at most `2C-1` such B input slots, including
all historical inactive slots of its one fiber. Their occurrences add
at most `O(C Gamma)` copies. Direct null child edges add no vertices.

Thus, for active parent vertex lifetimes,

    parent occurrence multiplicity <= O((C+D+1) Gamma) <= A Gamma.

This bound includes the unused path pools. There is no factor equal
to a high-degree portal's number of aliases, no duplication of an
entire dangling tree per child occurrence, and no factor k.

The initial total physical length of all nonnull input-edge pool paths
is `O(m Gamma)`: compressed K paths form a subforest of T with disjoint
interiors, and central edges are a subset of the original off-edge
set. The extra endpoint/port records contribute `m A Gamma/k`, which
is absorbed in `m A Gamma`.

## 8. Retired parent images and harmless internal ghosts

A stable anchor ID is tied to a **parent DTC vertex lifetime**, not to
its image in the next outer graph. The HRG can retire an occurrence
and later create a different occurrence with the same outer image.
Keeping all old exposed fibers forever would incorrectly accumulate
outer congestion.

Whenever a parent vertex has current total degree zero, or its lifetime
is explicitly retired, suppress the exported child components lying
over that parent image. The entire fiber is physically null and no
current nonnull geometric edge or path can leave it. Fiber connectors
may still give its child slots positive *child* degree, so the test is
the parent image's status, not the degree of an individual port slot.
The relevant geometric test is absence of every active real geometric
incidence; a real geometric self-loop counts as such an incidence even though both
of its port endpoints lie inside the fiber. Internal positive-length,
zero-gradient port connectors alone do not prevent suppression.
An otherwise unused fiber can also be suppressed under this test even
while its parent vertex remains active elsewhere; suppression on parent
retirement is the case needed for the lifetime congestion argument.

There are only `O(C Gamma)` child occurrence and null-edge records over
that fiber, and nonnull pools have already retired with their input
edges. Retire/omit these exported records in `A Gamma` local work,
while retaining internal child metadata if its API has no vertex
deletion. If that same parent lifetime later becomes active again,
materialize its bounded current fiber before installing the new
connections. The source's explicit occurrence map supplies the needed
lists. Charge each transition to the parent endpoint update.

Keep an inactive status and the fiber-to-parent-lifetime association
until the child instance is discarded. Test this status before looking
up any retired physical mapping or path metadata. A query path in an
omitted null fiber is recognized from that retained association and
dropped without dereferencing the old parent occurrence. These status
records are charged to the same already counted anchor/fiber births.

Every child forest component in a suppressed fiber has zero physical
projection. A returned path wholly in it is omitted. A child forest
path involving an active parent image cannot pass through it: there
is no current input edge leaving the fiber, and null flat edges keep
their input image. Thus suppression does not break a nonzero lifted
path or change any returned physical circulation.

Apply this discipline at every recursive lift and at the assembly of
the HRG tree family. It is what makes the occurrence bound depend on
current parent lifetimes, rather than the number of historical HRG
occurrences that once had the same final physical image.

## 9. Dynamic costs and the constant-depth recurrence

Over one portal period, the alias construction supplies

    B_H = (m/k+Q) A

H membership changes. Reference-count changes of original off-edges
cause at most this many central-edge and endpoint-terminal changes.
There are `Q A` new permanent portals. Virtual-tree updates have
polylogarithmic recourse, and first-use fixed fiber births cost C each.
Therefore the total ordinary B input edits, including all allocated
slots and inactive historical fibers, are

    R_B <= (m/k+Q) A.

The size of B is `m A/k` throughout a period. H endpoint remaps have no
additional central-edge effect; the source route/correction bookkeeping
already pays for them locally.

This size statement does not assume that T has O(m/k) components.
The terminal set for the compressed Steiner forest is only P together
with original endpoints of retained H aliases. Components with no
terminal contribute no anchor or fiber; components with one terminal
contribute one anchor and no compressed edge. Thus the compressed
forest has O(|P|+|H|) size even if there are Theta(m) dormant T components.
Their local fundamental cycles are retained in the parent's O(m)-size
heap and T copy. If the terminal set is empty, no recursive child
instance is created. Dormant activation and period rebuilding are
counted explicitly in [disconnected-routing-components.md](disconnected-routing-components.md).

Initial pool work costs `m A Gamma`. Each geometric edge birth/death
costs at most `k A Gamma` local work, and there are only R_B such events.
Parent-image suppression costs `A Gamma` per parent endpoint transition.
The alias/spanner local maintenance costs `m A + Q k^2 A`. Thus the
nonrecursive work has the conservative bound

    initialization: m A Gamma,
    per parent edit, amortized: k^2 A Gamma,

plus the usual amortized charge for rebuilding the size-`m A/k` child.
Most importantly, child input updates have factor A and child forest
logs have factor A; neither is multiplied by k. The extra factor k is
only in the cost of local input-edge pool lifetime changes.

Write Gamma_i for the exported occurrence bound at level i. The lift
and the subpolynomial HRG family give

    Gamma_i <= A Gamma_(i+1).

With an exact base of size at most `k A`, the number of pieces is at
most `k A^{O(D_depth)}`, and the base time is at most
`k^3 A^{O(1)}`. For fixed eta, the reduction size `m A/k` gives constant
depth `D_depth=O(1/eta)` once M is sufficiently large. Therefore

    Gamma_0 = A^{O(D_depth)} = M^{o(1)},
    update/query time <= k^{O(1)} A^{O(D_depth)}.

A concrete safe polynomial envelope is `k^10 A_star^{O(D_depth)}`.
To see that the k exponent is absolute rather than depth-dependent,
let `J_i=I_i/m_i` be the normalized initialization allowance. At a
base instance of size at most `k A_star`, direct exact cycle work gives
`T_base<=k^3 A_star^{O(1)}` and `J_base<=k^2 A_star^{O(1)}`. Above it,
local initialization and pool credits give

    J_i <= A_star Gamma_(i+1) + (A_star/k) J_(i+1).

The current period restart costs `k A_star Gamma_(i+1)`, and its child
restart costs `A_star J_(i+1)` per parent edit amortized. Together with
the local alias/spanner term and low child recourse,

    T_i <= A_star T_(i+1)
           + O(k^2 A_star Gamma_(i+1) + A_star J_(i+1)).

Enlarge A_star once to include the HRG tree-family multiplicity and
fixed local powers. These recurrences yield
`J_i<=k^2 A_star^{O(D_depth)}` and
`T_i<=k^3 A_star^{O(D_depth)}`. The larger displayed exponent ten also
covers conservative scalar/path bookkeeping envelopes. Accordingly
the root initialization is at most
`M k^10 A_star^{O(D_depth)}`, and amortized edits and queries are at
most `k^10 A_star^{O(D_depth)}`. In particular no `k^D_depth` term
has been hidden in path-pool creation or recursive forest logs.

The explicit capacity C contributes only another local
subpolynomial factor; `C^{O(D_depth)}=M^{o(1)}` at fixed depth. All
finite capacity/size/word-range checks are part of the fixed-parameter
branch. The verified portfolio, if used, treats a suspended branch as
unavailable and never trusts its output without the final exact
matching check. The asymptotic assertion still requires the
eventual correctness of the imported constant-degree primitives.

## 10. Conclusion and realization boundary

The degree estimate, circulation lift, fixed-tree update lemma, port expansion, pool accounting, and recurrences in Sections 2–9 prove Theorem 1. They show why coalescing aliases at their geometric endpoints controls occurrence multiplicity, while expanding an entire path on every recursive forest log would not give the stated recurrence. ∎

The theorem is a reduction under explicit operations. It does not supply a standalone implementation of every cover/HRG, provenance, spanner, and retirement interface. In particular, stable path images and signed/absolute transfers must hold for every exposed lifetime, including dormant records. The current complete matching theorem therefore continues to assume Contract R rather than treating this local geometric argument as a proof of that contract.

The local structural lemmas apply at fixed recursion depth as stated. Growing-depth use requires the depth-independent recurrence and finite-bit hypotheses recorded in [the master-size analysis](growing-depth-metric-recurrence.md).
