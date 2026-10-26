# A degree-three reset between distance-sparsifier levels

**Separate research candidate, 24 October 2026.** This note investigates
an interface change to the distance-oracle numerical route. It does not
alter any frozen 335/336, 209/210, or 167/168 construction. The first
claim is a local degree-reset and flat-lift lemma. Its quantitative
consequences are stated separately, with their exact source dependencies.
No implementation or external verification is claimed.

The relevant existing proofs are
[the distance backend integration](distance-backend-general-matching-integration.md),
[raw distance lifting](distance-oracle-raw-lift.md),
[the disconnected-component wrapper](disconnected-component-backend-wrapper.md),
and [the numerical lifetime interface](numerical-backend-lifetime-and-loops.md).
The primary numerical inputs are KMPG,
[arXiv:2311.06402v1](https://arxiv.org/abs/2311.06402v1),
and DO26,
[arXiv:2609.23852v1](https://arxiv.org/abs/2609.23852v1).

## 1. Where the reset is inserted

Let the current parent graph G have maximum degree three. Apply the
constructive one-level KMPG/DO26 routine, including its native core
splits, degree feedback, empty-loop convention, and the existing
disconnected wrapper. Let S be its **selected and degree-controlled**
child graph after equal physical roots have been identified. Every
vertex of S has the identity of one actual parent vertex lifetime.

Use the retained-edge gradient correction from the integration note.
An oriented selected edge a=(r_i(u),r_i(v)), originating from parent
edge e=(u,v) in forest F_i, has the immutable current representation

    F_i[r_i(u),u] + e + F_i[v,r_i(v)],

and its stored gradient is the exact parent gradient of that walk.
Its positive stored length dominates the literal walk length. Positive
core loops are covered by the local fundamental-cycle candidate; they
need not be selected into S. Any genuine immediate input loop is
handled by the separate exact loop heap.

Suppose that a one-level source envelope R bounds:

* the maximum selected degree of S;
* its initial resident size by O(m R/k), with m counting all parent
  vertices and edges, including isolated resident slots;
* its cumulative emitted edge and vertex births/edits through t parent
  edits by O(Rt), after initialization;
* changes to the stable CORE forests F_i, up to a fixed source
  polynomial factor included in R.

For degree-three G, the literal conservative DO26 envelope is

    R = poly(log m, log L) m^(4/K) gamma_l^O(1),
    gamma_l = exp(O(log(m)^(2/3) log log(m+2))).             (1)

Here K is the spanner parameter. The source's much larger
gamma_l^O(K^2) factor is in its local running time, not in the
displayed selected-degree/recourse envelope. This separation is
essential to the later calculation.

The necessary construction-level notification argument is given in
[demand-route notifications and local work](demand-route-notifications-and-local-work.md).
It instruments explicit per-demand records and their reverse indices,
including physical forest-leg and price changes. The spanner theorem's
reembedding set by itself is not assumed to enumerate those records.
Only genuine selected-edge provenance changes propagate recursively;
all correction-record rebuilding is charged to the larger local work.

The fully encoded interpretation of R is explicit in the proof of
KMPG Theorem 3.1, printed page 29. Claim 3.18 supplies both native
selected recourse and selected degree
O~(Delta m^(2/K) gamma_l^2). The proof then emulates a selected
vertex split by its affected retained incidences, multiplying those
two bounds and obtaining O~(Delta^2 m^(4/K) gamma_l^4) elementary
child edits. We use that squared, fully encoded bound, with Delta=3.
We do not infer a small encoded transcript solely from DO26's count
of native core updates. The genuine unsparsified core split still
stays native inside the source until this selected-output step.

Do not include KMPG Theorem 3.1 item 3's separate shortest-pivot
forest in that last R item. That forest can have O~(k) changes per
parent edit. Its maintenance belongs to local W. It is not one of the
stable core forests used for the descendant-copy pools below.
If a direct copy is exposed for a local path candidate, there is only
one such copy, with additive occurrence contribution and O~(k) local
logs; neither its copies nor its updates multiply the child solver.

The reset is inserted ONLY after this source output. In particular it
does not replace one native split of an unsparsified O(k)-incidence
core vertex by k synthetic edge updates. All such native splits and
loop identities are still processed by the source spanner first.

### Actual edge counts and isolated physical slots

The primary source states its parameter range using an edge count.
At the raw root, do not reinterpret an arbitrarily large set of
physical isolates as that many edges. Keep their physical lifetime
records in a private inventory. Initialize each source period ONLY
on the maintained list of currently nonisolated endpoints. When a
previously absent parent vertex first acquires an incident edge,
insert its source generation before the edge. If it later becomes
isolated, RETAIN that source slot until the period is discarded.
Reactivation during the same period reuses that same generation.
There is one source generation per actual parent vertex lifetime per
period, and no mid-period DeleteVertex call is required.

The private source graph may consequently contain a bounded number
of isolated slots in addition to the current nonisolated graph. They
have no effect on cycles and are counted as resident source records.
An actual parent vertex deletion marks its retained root-only slot
inactive after all real records retire. Keep its association as a
tombstone and suppress its exported physical image. Do not reuse its
generation for a new actual parent lifetime.

At the period boundary, discard the entire bounded native source and
descendant history. Reinitialize from the explicitly maintained
nonisolated list, without traversing all private physical isolates.
The source's isolated-vertex INSERTION API is sufficient. Although
KMPG Theorem 3.1 also advertises isolated-vertex deletion, this primary
adapter does not need it or an inner-spanner deletion extension.

Consequently at a fresh nonbase period, n<=2e and m=n+e=Theta(e).
The allowed O(m/k) elementary edits can change only O(m/k) incidences
or resident slots, so this relation holds up to a constant factor
through that period. Port-expanded children already have this property:
each entire resident port tree, including an inactive ghost tree,
contains O(1) edges per vertex. They are not removed from the child
size accounting. Transient isolated births while constructing a port
tree are ordinary charged edits, inside the same bounded period.

Distinguish a source activation generation from the actual parent
vertex lifetime. The external selected-root identity and its port
fiber are keyed by the ACTUAL parent lifetime. If that same parent
vertex temporarily becomes isolated and is later reactivated during
this parent period, reuse BOTH its source generation and its external
fiber. Its source-root records map to that stable external root
identity. While isolated its parent forest trees are root-only, and
the same frozen potentials remain valid. A new source generation in a
later period is created only after the old period's complete retirement.

Only deletion of the ACTUAL parent vertex lifetime makes its fiber
permanently inactive and ineligible for reuse. Storage-address reuse
creates a new actual lifetime ID. The old source-generation tombstones
are inactive and counted; they are not extra exposed port fibers.

Every active period, base threshold, and source restart uses its
initial nonisolated size m_act. Its resident slots may then include
the counted O(m_act/k) newly isolated or inserted slots, as above.
The private physical-isolate inventory
persists outside those restarts and is touched only by actual lifetime
or incidence events. A period reset retires its active source, its
activated external port fibers, and its counted descendant history;
it does not rescan or rebuild all private isolated slots. This avoids
an otherwise invalid ratio between a large external inventory and a
tiny active source instance.

## 2. A fixed port graph and its legal edit transcript

Fix a power-of-two capacity C>=R for the entire parent instance.
Use a fixed full binary tree P_v with C leaves for each logical
vertex v of S that is ever activated. All its vertices map to v.
Different logical vertex lifetimes get disjoint port trees. Let
h=log_2 C and choose the integer scale

    H = 2^ceil(log_2(4(h+1))).                              (2)

Each current incidence of S at v owns a distinct leaf of P_v.
For an edge a=(v,w) of S, put one real edge between its two assigned
leaves. Give it length H ell_S(a) and gradient H g_S(a).
Every internal port-tree edge has length one and gradient zero.
Call the resulting graph B. Internal binary-tree vertices have
degree at most three; an occupied leaf has degree at most two.
Thus B has maximum degree three at every settled time.

Port nodes and connector edges are actual B input records. Their
positive lengths are supplied literally to the next numerical level;
they are not zero-length edges hidden inside a positive-metric call.
Their projection to S is separately typed as null.

### Stable identity and leaf reuse

Within one parent instance, keep one port tree for a parent vertex
lifetime, even if its selected S degree becomes zero and later becomes
positive again. Reuse its free leaves. Do not allocate a new fiber
whenever the selected star empties. Source root sets only grow until
the corresponding parent vertex is deleted; this stable keyed record
is therefore compatible with their identities.

A deleted edge's leaf is reusable only after the old B input lifetime,
its exported child records, and their numerical retirement callbacks
have settled. A replacement with different provenance is a deletion
and fresh insertion even when its endpoints and numeric labels agree.

If S emits an isolated vertex birth, creating its port tree takes
O(C) actual vertex/connector insertions. One ordinary selected edge
insertion/deletion or price replacement requires O(1) B edge edits.
A source-selected vertex split has already been expressed using the
source's degree-controlled output incidences, within the fully encoded
R bound just cited. Its new vertex gets a
fresh port tree, and each exposed moved selected edge is replaced.
The B updater is never asked to support an unadvertised native split.

All new B vertices are inserted before their incident connector or
real edges. Delete old real edges before recycling leaves. These are
ordinary isolated-vertex and edge edits accepted by KMPG Theorem 3.1.
No intermediate degree exceeds three. Intermediate graphs may be
queried internally by the next source routine, but the parent exposes
no useful direction until its complete transaction settles.

### Size, recourse, and histories

There are O(C) B records per activated S vertex plus one per selected
S edge. Hence the initial child size is O(m R C/k). Through a prefix
of t parent edits, there are O(R C t) B edits and births. With C a
fixed constant-factor envelope for R, both are bounded using R^2
instead of R, with no factor k:

    |B| <= O(m R^2/k + R^2 t),
    emitted B edits through t <= O(R^2 t).                (3)

Here a large prefix-amortized source batch is allowed. A per-batch
guard R is not substituted for a prefix-total guarantee.

If a parent vertex lifetime ends, first retire every real selected
incidence and all real physical pool records. The now isolated
connector tree may remain in the native B instance until that instance
is discarded. Count all its vertices and edges in the actual resident
size. Retain its lifetime association and an inactive status. Never
reuse that fiber for a different parent vertex lifetime.

The parent lift suppresses the remaining components whose B images
lie entirely in such an inactive fiber. They have no real edge leaving
the fiber and project only to the retired parent vertex. Their stored
gradient is zero on every circulation. This is a condition on the
WHOLE fiber, not a test that an individual B vertex has degree zero:
its internal connector edges are still present. Check this inactive
association before accessing a retired parent image.

The local parent period has O(m/k) parent edits. Consequently the
initial records plus all historical port-tree births are O(m R^2/k).
Ghost trees do not introduce an uncharged master-length history.
The disconnected-component wrapper continues to count the parent
records of such tree components while keeping their initially loop-only
recursive core data local.

## 3. Cycles, exact gradients, and raw comparison

For every S circulation, route its flow between incident leaves inside
each port tree. Equivalently, first decompose it into sign-compatible
simple cycles and route each cycle. A unit simple S cycle uses at most
2h connector traversals per real edge. Since ell_S>=1 and H>=4(h+1),
its B traversal has length at most

    H ||L_S z||_1 + 2h |supp(z)| <= 2H ||L_S z||_1,

and gradient exactly H g_S^T z. Therefore

    OPT(B) >= OPT(S)/2.                                   (4)

The port lift preserves edge orientations and edge IDs. Contracting
the port fibers takes every B circulation to an S circulation. A
circulation using only port edges is zero, because each fiber is a
tree; more generally its gradient is zero. Hence a B answer with
nonzero numerator cannot project to a zero S circulation.

Suppose a recursive answer on B has numerator N_B and certificate
U_B dominating its literal B traversal, before cancellation. Replace
each real B edge by the current parent walk of its S edge, and each
connector by a null traversal. Then

    N_G = N_B/H,
    raw_parent_length <= U_B/H.                            (5)

Both scalar certificate quantities are divided by H. The path
coefficients remain unit signed integers; they are not divided by H.
The corrected retained gradient is what makes (5) an exact complete-
circulation identity. Frozen core gauges are not recomputed when a
forest splits.

The local ASZ, fundamental-cycle, and correction alternatives remain
the ones in the raw-lift audit. If the comparison reaches S, equation
(4) adds only a factor two before invoking the recursive B solver.
Extra useful B cycles are harmless because of (5).

## 4. A flat lift with no factor k on child forest logs

Let F_1,...,F_lambda be the current parent core forests. For each
physical root v let T_v be the direct sum of the forest trees rooted
at v, identifying only those trees' root vertices. A parent vertex
belongs to at most lambda such constituent trees.

For an activated external root whose actual parent lifetime survives,
keep its canonical trivial root while it is isolated. Its retained
source generation and all its forest trees are then root-only. A
reactivation within the period uses those same records and pool roots.
Actual parent-lifetime deletion instead makes the whole root/fiber
association inactive, with the suppression discipline below. Any
additional private canonical root records change the count by at most
the harmless replacement of lambda with lambda+1.

Assume the recursive flat forest over B has at most G simultaneous
occurrences per B input vertex, including isolated occurrences. A port
tree has fewer than 2C vertices, so at most 2CG child occurrences map
to any one logical S root v. Reserve that many copies T_{v,j}, using
common copy indices across all roots. Assign each child occurrence
over any port of v a distinct index j.

For each child forest edge:

* If its B input image is the real edge for a selected S edge with
  provenance (i,e=(u,w)), connect the u occurrence in its tail pool's
  F_i tree to the w occurrence in its head pool's F_i tree, using
  the central parent edge e.
* If its B input image is a connector edge within P_v, connect the
  two assigned pool roots by a true-null parent edge.
* If it is an immediate true-null child forest edge, perform the same
  root-to-root attachment. Its two endpoint occurrences have the same
  B image and thus the same logical root v, but distinct pool indices.

The second and third cases have different registered provenance. An
edge that is real in B and null only after projecting to S must not
be mislabeled as an immediate child-null edge.

Contracting every assigned T_{v,j} to its root recovers the child
forest. Unassigned pool copies are separate trees. The constructed
parent graph is therefore a forest, and its occurrence multiplicity is

    O(lambda C (G+1)).                                    (6)

Additional disjoint copies of the local F_i serve local candidates
and fit the additive one in (6). Isolated and dormant pool copies are
included, rather than inferred from an edge-congestion bound.

A child forest-edge birth or death inserts or deletes ONE connecting
record in this parent lift. A child vertex occurrence claims or
releases one existing pool index. It does not copy or traverse the
O(k)-vertex parent tree. Thus child logs cost O(1) local records each,
up to ordinary dictionary/dynamic-tree overhead.

### Why parent forest changes are different charges

A cut in some F_i splits all its pool copies. A new physical root may
join the same-index direct sums from other F_j. As G has degree three,
each such local root identification redirects only O(1) edges of that
constituent tree per copy. Repeating over lambda and the reserved
indices costs poly(lambda) C(G+1), times the explicitly exposed
parent-forest update count. This is local work, not a multiplier on
the recursive child's running time or log count.

Use deletion-first ordering. Before changing a pool region's root or
provenance, cut its affected old selected-edge attachments while old
physical data remain available. Those attachments are exactly the
selected incidences replaced by the source's root/split transcript.
Then cut or join the same-index pool trees, and finally install the
new child attachments. An unchanged null attachment meets an old pool
root, not an interior region newly separated by a cut. No parent path
update occurs inside this transaction.

Released copies remain dormant with BOTH their signed and absolute
counters. Their surviving physical edges stay on the appropriate
coordinate-sweep lists. Only an actual record retirement flushes and
disposes of those counters.

### No unknown occurrence cap is executable advice

Use one common observed capacity over logical roots, initially one.
Whenever the required simultaneous number of occurrences exceeds it,
double the common index capacity and allocate the new index layers of
the current forest family. Existing and dormant copies remain.
The total construction cost in this instance, even with late doubling,
is O(m lambda C(G_max+1)), because the geometric sum of new layers is
at most twice the largest required capacity. This is charged to that
instance's initialization/restart budget; it is not asserted to be
constant time for the event that triggers a doubling.

Common indices allow newly split root pools to be joined consistently.
Retired parent lifetimes are suppressed only after all real records
flush, as in Section 2. Every native ghost and association record stays
counted until its containing instance is discarded.

The enumeration for a doubling is ONLY the current active forest
family and external roots having a resident port fiber in THIS parent
period. Its size is bounded by that active period's counted records.
It never traverses the private historical isolate inventory. A private
canonical root with no current forest or port fiber keeps only a lazy
common-capacity/index marker. Allocate its actual root copies when it
is activated or first needed by a child occurrence. Creating these
trivial copies costs O(C(G+1)) up to local factors and is charged to
that explicit root/fiber birth, in the P(G+1) term of (9). An old-period
private isolate does not acquire new copies merely because an unrelated
current pool capacity doubles.

## 5. Raw domination of lifted forest paths

Consider a simple path in the child occurrence forest. For each real
B edge, charge its central parent edge and both parent root legs to
that edge's stored unscaled S length. Inside a pool, the actual path
between consecutive attachment vertices is no longer than the two
root legs. Connector and immediate-null attachments are at pool roots
and have zero parent charge.

Summing these charges gives raw_parent_length<=length_B/H. Repeated
uses of one parent edge in different pool copies are charged separately.
There is no appeal to cancellation across those copies.

A returned isolated real B edge can be expressed by its two root legs
and central parent edge. A connector contributes nothing. Following
only the central edge recursively gives at most 2d+1 forest/edge pieces
per selected explicit edge at depth d. Each local forest path already
has its maintained parent occurrence-forest representation. The pool
substitution therefore retains the raw certificate without expanding
all physical paths.

## 6. Separating local work from propagated recourse

This section states the arithmetic consequence of the local lemma;
it does not import DO26's full-depth theorem or its squared-degree
recurrence. Every graph to which the local source is applied now has
maximum degree three.

Use a common master S_b=2^U, with root actual size at most S_b^2 and
root prices/gradients of O(U) bits. Let

    gamma = exp(O(U^(2/3) log(U+2))),
    log R = O(U/K + U^(2/3) log(U+2)).                     (7)

Polynomial factors in U, in the number of forests, and in the length
bit bound are included here. Let P=R^O(1) poly(U) bound the reset
size factor, its child-input recourse, and its local pool factor.
Section 2 gives only an extra fixed power R^2, and Section 4 gives
only fixed powers of R and polynomial factors in lambda. In particular
P contains no gamma^O(K^2) factor.

The one-level source and candidate work has an envelope

    W = k^O(1) R^O(1) gamma^O(K^2) poly(U).                (8)

The O(1) exponents here are absolute implementation constants,
independent of K and depth. Initial future-path enumeration and local
ball candidates use a fixed power of k. The separate shortest-pivot
forest's O~(k) edits likewise belong here, not to R or P. Explicit spanner-route
maintenance has the source gamma^O(K^2) work and gamma^O(K)
route cardinality. A fixed polynomial overhead on the route logs or
selected candidates keeps (8), since it only changes those absolute
constants. It does not make a new recursive child update.

This last distinction can be checked directly in the primary spanner
dependency, van den Brand et al.,
[arXiv:2309.16629v1](https://arxiv.org/abs/2309.16629v1), Theorem 8.2.
Its item 1 gives the smaller selected-edge recourse, whereas item 3's
re-embedding set and its running time can contain gamma^O(K^2).
The latter records announce changes in the routes of INPUT DEMANDS
through retained edges. They do not, by themselves, replace the retained
edge as an actual core-edge ID. Our real B edge uses that retained
core edge's own central-parent-edge/root-leg provenance, rather than
the demand embedding through the spanner. Consequently a changed demand
route refreshes local correction candidates but does not reprice or
retire an unchanged child edge or its physical pool. Actual changes of
the retained core edge, its root endpoints, or its gauge labels are
already in the smaller selected-edge transcript. Charging every demand
re-embedding as a child edit would invalidate (12); this construction
does not do so.

Let G_r be parent occurrence multiplicity with r remaining recursive
levels, J_r initialization work per actual nominal record, and T_r
amortized work per parent edit/query. With the base conditions below,
the construction has the conservative recurrences

    G_r <= P(G_(r-1)+1),
    J_r <= W + P(G_(r-1)+1) + (P/k) J_(r-1),
    T_r <= P T_(r-1)
           + O(k W + k P(G_(r-1)+1) + P J_(r-1)).          (9)

For the last line, include the CURRENT level's own restart, not just
the child's restart. A nonbase degree-three instance of resident size
m uses a period floor(m/(12k)), which is at most n/k because
m=n+e<=5n/2. Its whole initialization costs m J_r; amortizing that
over its period contributes O(k J_r). Substituting the preceding line
gives (9). Complete old-instance retirement obeys the same bound.

The child-input size is at most mP/k, including its ghost slots.
When P<=sqrt(k), size decreases by at least sqrt(k). Thus a root of
size at most S_b^2 reaches the base after

    d = O(U/log k).                                       (10)

The base is chosen when the active numerical size is at most 24k.
Initialization touches only those actual active records. The external
physical-isolate inventory is separate, as in Section 1. A direct cycle
query costs a fixed polynomial in their count and price bits; a
loose k^O(1) upper bound is allowed for a query, not as an allocation
of k records when the actual root is tiny.

Solving (9) gives, for an absolute c,

    G_r <= (2P)^(r+1),
    J_r <= O(W) + (2P)^(r+2),
    T_r <= k^c W (4P)^(r+c).                              (11)

The important form is

    log E = O(log k + K^2 log gamma + d log R).            (12)

W is a local additive cost in (9). It is NOT raised to depth d.
The copy multiplicity, complete pool retirement, and global observed
capacity doubling have been accounted for through G and J instead.

Raw quality has at most one terminal/local extraction loss k^O(1)
and a per-level factor poly(U) gamma^O(K), including the port loss two.
The actual parameters below satisfy K^2 log gamma=o(U), and hence
K log gamma=o(U/K). This, rather than the weaker condition
K<U^(1/6) alone, makes the per-level quality factor smaller than R
up to a fixed power. The answer-piece count has the same loose
envelope E. All four exported quantities therefore fit (12).

## 7. Aspect, weighted path inventories, and source horizons

The reset does not require the stronger original-length SNC argument
used in Route A. The original exact integer realization of the stable
core labels suffices:

    ell_core(e) = 2 sum_j (ell_e + P_j),

where there are O(log^2 n) terms and each P_j is at most 2n times
the maximum parent length. Consequently

    L_(i+1) <= O(n_i log^2(n_i+2)) H L_i.                  (13)

Frozen potentials and the retained-edge correction increase gradient
bit counts by at most the same O(U) per level. Thus length and gradient
bits are O(U(d+1)). These are polynomial in U for the parameter choices
below and are charged as ordinary multiword arithmetic.

There is a necessary correction to a polynomial-length shorthand in
the source. KMPG Lemma 3.12 halves TOTAL WEIGHT of the future-path
inventory, not the number of paths. If that inventory has polynomially
many paths of O(k poly(U)) edges, integer minimum length one, and maximum
edge length L, its forest count is

    lambda = O(log m + log k + log L + log poly(U)).       (14)

It need not be O(log m) when L is quasipolynomial. Equation (14) is
still polynomial in U, so its appearance in degree feedback, pool
counts, initial path preprocessing, and recourse is absorbed into
the polynomial factors of (7)--(9).

The weighted calls also have a direct polynomial-bit realization.
The source assigns w_i(e)=econg(P_i,e) ell_e, rather than a reciprocal
path-length weight. The inventory contains O(m k^3 poly(U)) explicitly
represented paths, each with O(k poly(U)) edge occurrences, so its
nonnegative integer incidence counts have O(log m+log k+log U) bits.
Here econg counts OCCURRENCES, including any repeated use of an edge
in a concatenation of shortest-path pieces. Mere membership of an
edge in the resulting walk would not give the required weighted-sum
identity. Enumerating those occurrences is already included in the
displayed inventory bound.
Consequently each w_i(e), and their sum, have
O(log L+log m+log k+log U) bits. Removing a discarded path decrements
these integer counts. For a nonempty connected component with total
weight W>0, replace w_e by the equivalent positive integer weights
e_C w_e+W; this implements the usual addition of W/e_C to every edge
with no rational denominator and increases the average-stretch loss
by at most two. Replica counts are computed by integer ceiling
division and total at most 2e_C. If W=0, use unit weights. Thus neither
the halving inventory nor weighted replica normalization introduces
a hidden least-common-multiple or input-wide denominator cost.

There is a separate reciprocal sum in CKL+22 Definition B.5; it is
not covered merely by the preceding integer-weight argument. Use
the finite-bit ordering proved in Section 2.1 of
[the disconnected-component wrapper](disconnected-component-backend-wrapper.md):
order each tree edge by the sum of the dyadic proxies
2^(-ceil(log2 ell_e)) over its crossing replica paths. CKL Lemma B.6
then has stretch factor three instead of two; Lemma B.9 and its fixed
labels hold for any fixed total order, so domination and decremental
updates are unchanged. All proxy sums have one power-of-two
denominator and O(log m+log L) bits. If gamma_src denotes the original
weighted fixed-label envelope, use gamma_eff=4 gamma_src to cover
both this ordering and positive-weight smoothing, and use the
halving threshold 2 gamma_eff throughout. The enlarged high-stretch
cutoff preserves the source root count. No parent metric label is
rounded or rescaled by this arithmetic wrapper.

KMPG Section 2 explicitly allows an arbitrary length bound at an
additional O(log L) cost. Its Theorem 3.7 explicitly permits
quasipolynomially bounded lengths. The stable-tree primitive imported
from CKL+22 starts with positive real lengths and the usual weighted
LSST guarantee (CKL+22 Theorem 3.2 and Lemma 6.5); the integer formula
above fixes the arithmetic realization. No common denominator over
all edges is taken.

The finite-bit original-edge tree interface of
[the AN adapter](an-weighted-finite-bit-adapter.md) can be substituted
at this boundary as detailed in
[the stable-forest integration lemma](polynomial-bit-stretch-stable-forest-integration.md).
The magnitude recurrence (13) holds for ANY returned original-edge
tree and therefore precedes the use of its poly(bit-count) stretch
and work bounds. Its hierarchy height is independent of the number
lambda of weighted calls. This prevents a recursive bit-length
self-reference; temporary portal grids never become core labels.
Frozen potential magnitude bounds use the maximum admitted parent
gradient over the instance's lifetime, including birth-time values,
not merely the current gradient after a possible decrease.

All nonbase calls have log m>=log k. For the displayed parameter
choice, O(U(d+1)) is a fixed polynomial in log m, so every such source
metric has quasipolynomial aspect in its own local size. The spanner
parameter condition K=o((log m)^(1/6)/loglog m) is checked at this
smallest local scale, not only at the root.

Declare the length/gradient bit caps in advance from a computable
depth guard, for example ceil(8U/log k)+10. A violation suspends the
candidate; it does not silently retune all source length buckets.
The bound (13) proves that an adequate fixed coefficient in that
declared O(U(d_guard+1)) cap eventually suffices.

The source period is shortened to floor(m/(12k)); this is within
the literal n/k horizon. A local instance may be discarded before
the nominal period ends. Count the work of all its old pool records
when doing so. Recursive restarts, port births and ghost histories
are covered by (9). No primitive is expected to endure a polynomial
MASTER lifespan inside a single tiny local invocation.

## 8. Candidate parameter balance and its current meaning

At the level of exponents, set K=U^t and log k=U^a. Equations
(7), (10), and (12) give the three possible dominant exponents

    a,             2/3+2t,             2-a-t.             (15)

They balance at

    t=2/15,       a=14/15.                               (16)

This is the optimum balance within this particular separated-cost
model. Indeed, if r bounds all three exponents, then a<=r and
t<=(r-2/3)/2, while r>=2-a-t gives
r>=7/3-3r/2 and hence r>=14/15. The choices in (16) attain equality.
This is not a lower bound for other numerical constructions.

Keeping the leading logarithms, take

    K = Theta(U^(2/15)/(log(U+2))^(2/5)),
    log k = Theta(U^(14/15)(log(U+2))^(1/5)).              (17)

Then each of the three terms in (12) is
O(U^(14/15)(log U)^(1/5)). Also

    K^7 = o(log k),

which is a simple sufficient eventual check for the source parameter
range at every nonbase level. The length/gradient bit bound becomes
O(U^(16/15)/(log U)^(1/5)+U). It is quasipolynomial in every nonbase
local size, since log m>=Theta(U^(14/15)(log U)^(1/5)).

A computable program can round these parameters by integer power
comparisons and enumerate adequate fixed constants for gamma, R,
local resource guards, and the outer client. That uniform acceptance
wrapper is not re-proved here. The fixed-constant portfolio mechanism
already has a separate proof; it must be instantiated with these
new bounds before making a final matching-time claim.

In particular the numerical bound alone does not imply the same
matching exponent. Retaining the older deterministic exact-flow
subroutine would leave its larger O(U^(17/18) log U) logarithmic
overhead. The separate
[near-feasible exact recovery proof](near-feasible-rounding-and-exact-projection.md)
removes that dependency, and the separate
[14/15 matching composition](quantitative-matching-14-15-composition.md)
checks the resulting outer parameter and acceptance program. Those
are additional proof obligations, rather than conclusions of this
local degree-reset argument.

## 9. Literal parameter family and guards

Here is one executable version of (17), using only integer power
comparisons. For a master integer U>=2, write

    L_U = ceil(log_2(U+4)),
    r_5 = ceil(L_U^(1/5)),
    K = max{1, floor(floor(U^(2/15))/r_5^2)},
    b_k = ceil(U^(14/15)) r_5,
    k = 2^b_k.                                            (18)

For example floor(U^(2/15)) is obtained by comparing integer fifteenth
powers against U^2. No real-number oracle is used.

For an enumerated positive integer c_C, set

    b_C = c_C(ceil(U/K) + ceil(U^(2/3)) L_U + L_U),
    C = 2^b_C,
    P = C^16.                                            (19)

Fix one ordinary computable implementation of the cited constructive
local primitives. Their absolute constants are fixed program constants,
not input-dependent advice. For an adequate fixed c_C, (19) eventually
dominates their actual selected degree, fully encoded recourse, and
forest update counts, uniformly in every local nonbase instance. The
constant tuple can be enumerated by the already proved verification
portfolio; an inadequate tuple is permitted to suspend.

Use C leaves in every port fiber, and compute H by (2). This capacity
is fixed throughout a parent instance. It is not the observed current
maximum degree, and it does not grow silently when a degree guard
fails. In particular no global repricing of all real B edges is hidden
in a change of H.

The P=C^16 bound is deliberately loose. The encoded source transcript
contributes at most C, port-tree birth contributes at most C, one
logical root has fewer than 2C ports, and its forest count lambda is
at most C eventually. Parent forest changes therefore use at most a
fixed C^4 factor on descendant copies, even including ordinary
dictionary and polynomial-bit work (each is at most C eventually).
The child-input edit count is only C^2. A child forest log creates one
attachment, with at most an additional C factor for its ordinary
metadata operations. Initialization and complete retirement have
the corresponding fixed-power bounds. C^16 simultaneously dominates
these explicitly separate counts; it does not absorb W or a K-dependent
power of C.

Use the depth and bit limits

    d_* = ceil(8U/b_k)+10,
    b_* = (c_0+100) U(d_*+1),                              (20)

where c_0 is the fixed root price/gradient bit bound. The same b_* is
an allowed bound for each local instance's entire lifetime. The
source length buckets can be fixed from it at initialization. Check
actual values against it, and suspend on failure. From (13), each
level adds at most O(U) bits; an absolute coefficient below 100 is
eventually enough, since n<=S_b^2 and log H=O(log U) at each level.
Thus (20) is an eventual bound on the entire guarded recursion.

Before a nonbase invocation on its actual nominal m, let e_0 be its
initial active edge count and v_0=floor(log_2(max{2,e_0})). Check

    m>24k,
    P<=sqrt(k),
    K^7 <= v_0,
    b_* <= v_0^2.                                        (21)

The last inequality is a sufficient literal quasipolynomial-aspect
condition for the local source. All conditions eventually hold:
log P/log k tends to zero, and the active-size adapter gives
v_0=log_2 m-O(1), while
K^7/b_k=O(L_U^-3), and
b_*=O(U^(16/15)L_U^(-1/5)+U)=o(b_k^2).
An actual root whose active size is at most 24k is processed by the
direct base, with actual-active-size initialization; it is not padded
to k or S_b. Its private isolate inventory is initialized once and
thereafter touched only on its own events.

For every source instance separately, count selected degrees,
postinitialization fully encoded output edits, stable core-forest
changes, actual
resident child slots, and births. Check their declared C and mC/k
prefix/size allowances with fixed generous literal multipliers.
Check all ghost slots and port connector records after the reset
against the mP/k allowance. These are prefix-total counters, not an
incorrect constant cap on one amortized burst. Also impose an ordinary
instruction counter for each promised local work budget when using
the final acceptance portfolio. None of these resource checks is
used as an exact LOW or optimality certificate.

For every fixed adequate tuple, (7)--(12) and (18)--(21) give

    E_b = exp(O(U^(14/15)(log(U+2))^(1/5))).               (22)

Initialization costs (actual_size+1) E_b; edits, queries, exported
logs, occurrence multiplicity, answer-piece count, and inverse raw
quality are all bounded by E_b in their established amortized or
current-state sense. A polynomial master horizon is supported by
successive counted local periods and their complete retirements,
not by assuming an unlimited horizon for one source invocation.

Two other workstreams independently reviewed the legal reset,
root-pool/raw lift, source selected-edit boundary, separated recurrence,
active-isolate costs, and parameter/aspect guards. They reported no
remaining blocker under the named constructive primitives. This is
an internally reviewed mathematical assembly, not an implementation
or external certification. Its resource guards alone are not finite-
size correctness certificates; the separate acceptance proof still
checks final exact outputs.
