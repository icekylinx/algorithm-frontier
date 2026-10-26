# Preserving the master length aspect through the cycle recursion

**Abstract.** We prove a local metric transformation with length-bit increment $\log_2 k+O(\log U)$ per outer recursion. It contracts only true-null edges of the immediate flat map, retains original integer lengths on real edges, and uses a small integral port scale. Frozen gradient gauges remain separate and may have larger bit length. Under the complete uniform dynamic realization specified in Section 7, the transformation yields the conditional backend exponent $167/168$.

This metric argument does not establish every dynamic geometry and lifetime interface required by a full solver. Those remain explicit here and in Contract R of [the current main matching proof](../../problems/general-matching/proof.md).

The constructive published imports are the constant-degree sparse
neighborhood cover and the legal dynamic spanner of
[Chen et al., arXiv:2311.18295v1](https://arxiv.org/abs/2311.18295v1).
The exact interfaces are those identified in
[Growing-depth recurrence bounds with controlled numerical aspect](growing-depth-metric-recurrence.md),
[portal-alias-api-reconstruction.md](portal-alias-api-reconstruction.md),
[constant-degree-steiner-bridge.md](constant-degree-steiner-bridge.md), and
[numerical-backend-lifetime-and-loops.md](numerical-backend-lifetime-and-loops.md).

The typed real-edge records used below can be constructed from the
source's explicit vertex map and metric convention by
[snc-provenance-from-vertex-maps.md](snc-provenance-from-vertex-maps.md). That wrapper removes genuine
immediate loops to the separate exact heap, chooses a current
admissible parallel representative, and refreshes its gradient and
lifetime even when source topology does not change.
The consistent frozen-gauge labels and complete raw lifting argument
are stated in [alias-geometric-raw-bridge.md](alias-geometric-raw-bridge.md).

## 1. Contract only true-null edges of an immediate cover map

**Lemma 1 (typed null quotient).** Suppose a flat forest has explicit real-edge and true-null records, at most $\Gamma$ occurrences per input vertex, and a degree-three immediate input graph. Contracting the true-null components preserves the marked cover, produces a forest, retains every real edge identity, and can be maintained with $\Gamma^{O(1)}$ local work and logs per reported source update, provided the stated retirement transactions are available.

**Proof.** Consider one SNC forest F after the artificial heavy-backbone
occurrences have been filtered out. Its map into the CURRENT
degree-three general-cycle input G has at most Gamma occurrences
of every G vertex. Each F edge has an explicit type:

* a real occurrence of a particular current G input edge, with
  its oriented endpoint correspondence; or
* a true-null forest edge joining equal images in G.

Contract every connected component consisting of true-null F
edges. A contracted vertex maps to their common G vertex and is
marked if at least one of its old vertices was marked. Keep every
real F edge, with its input edge ID and orientation.

The word "null" refers to this IMMEDIATE map into G. A genuine
G input edge can have zero gradient, be a loop, or project to zero
under an earlier map toward the final numerical graph. None of
those properties makes its F occurrence a true-null edge for
this contraction. In particular, genuine port connectors and
genuine loops retain their real input identities.

The quotient is a forest. Contracting forest edges cannot create
a cycle. A surviving real edge cannot become a loop of the
quotient: its endpoints would otherwise already be joined by a
true-null F path, making a cycle in the original forest. Two
distinct quotient vertices may still have the same physical G
image, and a real G-loop occurrence can join them; its real
identity is preserved.

### Dynamic cost and immutable lifetimes

For a fixed G vertex v, its true-null subforest has at most Gamma
vertices. Moreover all real F edges incident to that fiber have
their other endpoints over v or one of v's at most three physical
neighbors. They belong to the forest induced on at most 4 Gamma
occurrence vertices, so there are O(Gamma) such incident records.
The weaker O(Gamma^2) bound is sufficient even under conservative
bookkeeping.

Maintain the source-occurrence and incidence lists for each input
vertex. A source forest/mark log touches at most two such fibers.
Reconstruct their true-null components locally, retire the old
quotient vertices and incident real-edge representations, and
create fresh quotient records and attachments. This uses
O(Gamma^2 polylog m) work and explicit logs per source log. The
factor is a fixed local power of Gamma, not a recursion-depth
factor. No other physical fiber is scanned. Marks are maintained
by component counts or minima.

All old quotient records keep their physical map and endpoint
correspondence until their deletion-first retirement has completed.
When a quotient representative changes, the affected edge is a
replacement lifetime even if its underlying G edge ID is the
same. Old metadata remains available while every recursively
exposed real copy transfers its signed and absolute counters.
New records get fresh immutable image lifetimes. The source SNC
state is unchanged; this is a wrapper on its explicitly reported
forest, map and marked-set changes.

Reserved inactive slots remain entirely private. After filtering
the artificial backbone, an inactive slot has no genuine incidence;
its remaining components are isolated vertices or true-null trees
whose immediate image is that slot. None is exposed, since an
inactive slot need not yet name an existing client vertex. First
create the client vertex lifetime and its legal physical image,
then activate the reserved slot and expose fresh quotient lifetimes.
Conversely, a client vertex is retired only after its genuine
incidences and all their recursively exposed real pools have
completed both signed and absolute retirement transfers. The
remaining null components can then be suppressed before the client
image becomes invalid. Old associations remain private tombstones
until the corresponding source/child instance is discarded; they
are never silently reused as a live exposed map.

All resident and reserved source slots are counted in the local
nominal capacity and initialization cost. Reserve only a constant
multiple of that local capacity, restarting under the existing
local-period or capacity-doubling rule when it is exhausted. A tiny
actual root uses the base solver; use of a large master parameter
does not allocate a master-sized slot array. Since an inactive slot
has no retained genuine incidence, activating or suppressing its
O(Gamma) source occurrences cannot alter a marked path belonging
to a different active physical fiber.

The forest, marking, incidence, and transaction arguments prove Lemma 1. ∎

## 2. Export original integer lengths, without clearing m^4

For a radius D, the cover wrapper still runs the source on its
polynomial integer metric

    delta = D/m^4,
    w_D(e) = ceil(ell_e/delta) <= m^4

for genuine edges of length at most D. Its artificial fixed-slot
backbone has length m^8 and is omitted from the exported forest.
No marked-to-marked source path uses an artificial edge.

After contracting true-null forest edges, give each retained real
edge its ORIGINAL CURRENT INTEGER length ell_e and its original
gradient. This differs from exporting delta*w_D(e). Term by term,

    ell_e <= delta*w_D(e),

and the source's supplied real forest metric dominates w_D(e).
Thus a quotient marked-tree path has length at most the source
marked-tree path scaled by delta. True-null edges have disappeared,
so no positive null-length correction is needed. The cover and
diameter guarantees are at least those of the radius wrapper,
with `gamma_HRG=2 Gamma` a safe common allowance.

All retained edge lengths are already positive integers. There is
no multiplication of the whole HRG by m^4, and no tiny dyadic
exported null edge whose denominator must be cleared. The source
itself still sees only its fixed polynomial integer length range;
the original metric can have a polynomial MASTER aspect much
larger than a fixed polynomial in the local graph size.

## 3. Cheap stored HRG linking and paired edges

Use the same HRG topology, marked-root attachments, scale radii,
and tree family as in the parameterized construction. Set the
STORED length of every linking edge to one, and that of every
paired off-tree edge to two; their gradients are zero. Original
graph edges and retained real cover edges keep their actual
integer input lengths and gradients.

This is a metric variant, so the published HRG theorem with its
prescribed linking lengths is not invoked verbatim. Instead
consider, only in the proof, the same graph with the source's
analytical lengths:

    linking length at scale i = gamma_HRG D_i,
    paired length             = 2 gamma_HRG D_i.

All stored lengths are at most their analytical counterparts.
The direct cover-routing lemma
[hrg-routing-from-rounded-covers.md](hrg-routing-from-rounded-covers.md) applies to that analytical
metric. An abstract edge is realized by a marked-tree path and
two linking edges; its stored length is at most

    gamma_HRG D_i + 2 <= 3 gamma_HRG D_i.

The source monotone-cycle decomposition is analyzed using these
geometrically increasing ABSTRACT lengths. It yields a comparison
fundamental cycle in the same tree family. Replacing analytical
linking/paired lengths by their smaller stored values can only
improve that candidate's ratio. No probability or distance-to-
cluster value is computed by the maintained algorithm.

Every stored linking or paired edge projects to zero under the
immediate map into G and has zero gradient. Every real edge has
its exact G length and gradient. Hence every returned cycle has
an actual physical circulation with the same numerator and raw
physical traversal bounded by its stored denominator. A nonzero
numerator cannot be supported only on the null projections.

In particular, if ell_max is the largest parent G length, every
tree-cycle input J=T union E_off now has

    max_length(J) <= max(ell_max,2).

The possibly much larger analytical radius D_i is metadata for
the cover/routing proof. It is not a metric value carried into
the next recursive child.

## 4. Geometric path length and small port scaling

**Lemma 2 (one-step metric growth).** Under the geometric path and port interfaces, the transformed child satisfies
$$
\ell_{\max,\mathrm{child}}
\le c_K kH\max\{\ell_{\max,\mathrm{parent}},2\},
$$
and preserves the cycle numerator after division by $H$, with at most a factor-two quality loss. Here $H=2^{\lceil\log_2(4(h+1))\rceil}$ and $h$ is the port-tree height.

**Proof.** The portal/Steiner construction retains the original central edge
of each selected off-edge lifetime and the compressed Steiner
forest K of the current T. Every K path has O(k) TREE EDGES,
not merely O(m) edges:

* every permanent portal is a terminal of K;
* a compressed path therefore has no portal in its interior;
* an unedited initial-tree interior belongs to one initial piece
  of O(k) incidence-and-vertex volume;
* endpoints of every edited or new tree edge are promoted first,
  so such an edge is direct between two K terminals.

This is exactly the fixed-initial-tree argument in Section 4 of
[constant-degree-steiner-bridge.md](constant-degree-steiner-bridge.md), including dormant components,
retired initial edges, and arbitrary legal tree exchanges. A
conservative constant c_K gives

    max_length(K union E_star)
          <= c_K k max(ell_max,2).

Aliases with old, larger lengths do not invalidate this bound.
The geometric child coalesces aliases to the ACTUAL original
central edge and actual K paths; their old alias prices remain
only in the parent spanner/comparison metadata.

All geometric gradients use ONE frozen parent gauge. A central
edge carries `bar_g(e)=g(e)+pi(tail(e))-pi(head(e))`, and an
oriented compressed K path carries the signed sum of these SAME
bar_g values along its current parent-tree edges. It does not
sum ungauged g while central edges use bar_g. Old unchanged T0
edges have residual zero; a newly inserted tree edge retains its
actual, possibly nonzero, residual. The gauge terms telescope
only on a complete circulation.

Let C_port be the declared maximum degree of this geometric graph,
and let h=ceil(log_2 C_port) be its port-tree height. Replace the
old S^10 common factor by the dyadic integer

    H = 2^ceil(log_2(4(h+1))).

Then `4(h+1)<=H<8(h+1)`. Give each geometric edge length H times
its old length and gradient H times its old gradient. Give every
binary port-fiber edge length one and gradient zero.

To lift a unit simple geometric cycle, route between its two
ports at each vertex through at most 2h fiber edges. If it uses
t real geometric edges, this costs at most 2ht additional length.
Since all geometric lengths are at least one,

    child_length <= H parent_length + 2h t
                 <= 2H parent_length.

Its numerator is H times the parent numerator. Thus the port
expansion loses at most a factor two. Conversely, every child
cycle projects to the parent with the same numerator divided by
H and raw length at most its child denominator divided by H.
Divide BOTH scalar quantities on lifting. The physical traversal
coefficients themselves stay integral and unit per listed piece.

Consequently every recursively created input edge satisfies

    ell_child <= c_K k H max(ell_parent_max,2).
                                                            (1)

This includes central edges, compressed tree paths, and fiber
connectors. Their identities and lifetimes are unchanged from
the existing path-pool construction. Smaller H does not change
which copy is retained, reused, or retired. ∎

## 5. Separate length and gradient bit bounds

Use one master U and one k throughout the outer recursion. Let
the root input lengths have at most c0 U bits. Since H is a
fixed power of U up to constants, (1) gives

    B_len(i+1) <= B_len(i) + log_2 k + O(log U).

The standard reduction has at most `O(U/log k)` levels. Therefore

    B_len(max) <= c0 U
                 + O((U/log k)(log k+log U))
               = O_c0(U).                                 (2)

This is a local recurrence; it does not assume that every deep
metric edge already has a root-level canonical pool path. No
bound on a not-yet-built root forest is used to justify its own
construction. The same proof can be guarded by
`ceil(8U/log_2 k)+10` levels and a sufficiently large fixed
multiple of U length bits; the eventual size shrink proves that
these guards are not reached.

Retain the frozen gradient gauge. In particular,
a new tree-edge lifetime keeps its actual frozen-gauge residual;
it is not silently assigned zero. A gauge potential can sum
O(m A) parent gradients, and a compressed path can sum O(k) such
residuals. Thus the conservative gradient recurrence remains

    B_grad(i+1) <= B_grad(i)+O(U),

giving `B_grad=O_c0(U * depth)`. This is harmless for the metric
balance. The cover and dynamic spanner inspect lengths, not
gradients; gamma_diam is chosen using B_len only. Gradient sums,
raw-score comparisons, and the direct Bellman--Ford base use exact
multiword arithmetic of fixed polynomial cost in B_grad. No
large-gradient value is fed as an edge LENGTH to a cover or
spanner primitive.

The common port scalings have product with logarithm at most
`O(depth log U)`. Exact dyadic division on lifting is therefore
within the same arithmetic allowance. Final physical numerators
on the original integral input remain integral and polynomially
bounded through the unit-piece/forest-size argument; the frozen
gauges telescope on every circulation.

## 6. Parameter balance with exponent 167/168

Set

    p=41/42,           alpha=167/168,
    t=1/84,           beta=83/84,
    L_U=ceil(log_2(U+4)),
    k=2^ceil(U^alpha L_U),
    Gamma=2^(ceil(U^p) L_U^2),
    kappa=max(3,ceil(U^t/L_U)),
    C_port=2^ceil(U^beta),
    A=2^(ceil(U^beta) L_U^2).

The previous larger port exponents must NOT be retained in this
variant. The new C_port still dominates the actual HRT degree,
whose logarithm is `O(U^p L_U^2)`.

For a nonbase local instance `log m>=log k`, choose the analytical
HRG ratio by

    log_2 gamma_diam
       = ceil(max(log_2(8 gamma_HRG^2),
                  (B_len+2 log_2 m+log_2 gamma_HRG)/(kappa-1))).

By (2), the aspect term has logarithm

    O(U/kappa) = O(U^(1-t) L_U)=O(U^beta L_U).

The tree-family logarithm is

    O(kappa log Gamma)=O(U^(p+t) L_U)=O(U^beta L_U).

Both fit the computable `log A=Theta(U^beta L_U^2)` with slack
for fixed hidden coefficients. The true-null contraction costs
only another fixed local power of Gamma. Source length buckets,
alias inventories, and exact scalar arithmetic have polynomial
bit factors. No new factor k multiplies recursive child edits
or child forest logs.

The extra L_U in log k balances the two logarithmic costs. The
same absolute recurrences give depth
`O(U^(1/168)/L_U)` and common backend envelope

    k^10 A^O(depth)
       = exp(O_c0(U^(167/168) log U)).

Indeed `log k=Theta(U^alpha L_U)`, while
`depth*log A=O(U^(beta+1-alpha)L_U)=O(U^alpha L_U)`.
The strict exponent gap beta<alpha still gives
`log A<=(1/2)log k` eventually. The length-bit bound uses
`depth*log k=O(U)` and is unchanged.

The separate gradient bit bound is

    B_grad = O_c0(U^(169/168)/L_U),

or conservatively `O_c0(U^(169/168))`, while B_len remains
O_c0(U). These exponents must not be
conflated. The master-size initialization, polynomial master
lifespan through local restarts, actual-record retirement, unit
pieces, and finite guards are inherited from the explicit
recurrences, with the metric modifications proved above.

This is a conditional backend bound: Lemmas 1–2 supply the metric changes, while the complete realization and depth-independent operation interfaces are the hypotheses of Section 7. An outer matching bound additionally requires its own uniform phase composition. The parameter-model calculation in
[backend-exponent-balance.md](backend-exponent-balance.md) explains why 167/168 is the natural
balance once the new length-aspect invariant is available.

## 7. Conditional master backend theorem and interface accounting

### 7.1 Hypotheses and theorem

Assume a complete implementation of the portal, Steiner, null-quotient, provenance, and lifetime interfaces, whose elementary records and transactions obey Sections 7.2–7.4 with constants independent of depth. In particular, the implementation must supply typed edge records, complete old-to-final retirement, local polynomial source histories, and the displayed aggregate recurrences. A vertex map or scalar ratio oracle alone does not supply these data.

Fix an absolute integer c0. For a master `S=2^U`, consider an
arbitrarily changing degree-three undirected multigraph, with fixed
reference orientations, real input-edge lifetime IDs, and positive
integral lengths and integral signed gradients bounded in magnitude
by `S^c0`. Loops are handled by the exact loop wrapper, preserving
their edge IDs. The number of resident vertices and edges is at
most S^2. Allow any fixed polynomial master lifespan, for example
S^200 external edge, vertex-lifetime, price-replacement and query
operations.

Here `OPT=max |g^T d|/||ell d||_1` over nonzero circulations d,
with value zero if all circulation gradients vanish or the graph
has no nonzero circulation.

**Theorem 3.** Under the complete realization hypothesis above and the stated cover/spanner primitives, the metric transformation and parameters give, for all sufficiently large $S$, the common deterministic factor

    E(S)=exp(O_c0(U^(167/168) log(U+4))).             (3)

Its outputs and bounds are as follows.

1. It exposes a forest whose vertices have stable current input
   slot images. Every forest edge has registered real-input-edge
   provenance with orientation and endpoint correspondence, or
   is a true-null edge between equal input images. Every input
   vertex has at most E(S) exposed occurrences, including dormant
   path-pool copies.
2. A query returns at most E(S) oriented single input edges or
   endpoint-specified paths in the final settled exposed forest.
   Each listed piece has coefficient +1 or -1; repeated traversal
   is counted in the list. Its signed physical projection c is a
   circulation. If OPT>0, it has nonzero numerator and literal raw
   length V>0 satisfying `|g^T c|/V >= OPT/E(S)`.
   An optional certified denominator U_cert>=V can be supplied
   with the same bound after enlarging E by an absolute constant.
3. Initialization on actual root size m costs `(m+1)E(S)`;
   amortized edits, queries and their complete explicit forest
   logs cost E(S), with the corresponding prefix allowance.
   Root storage is `(m+1)E(S)` at a fixed nominal size. Root size
   changes use charged doubling/halving periods. No S-sized
   allocation is made for a small local instance.
4. Length arithmetic uses O_c0(U) bits. Internal gradient and
   exact ratio arithmetic uses at most
   `O_c0(U^(169/168))` bits, with fixed-polynomial multiword cost
   charged in E(S). Final physical numerators and rounded raw
   certificates use O_c0(U) bits.
5. Old input data, maps and provenance remain available until
   every affected real-copy retirement has transferred both
   signed and absolute motion. Queries and primal motion occur
   only between completed old-to-final transactions.

The theorem is conditional on complete realization of its explicit interfaces. The local metric proofs and parameter calculations do not establish that realization. Its asymptotic adequacy uses the primitive guarantees and the displayed guards. Finite
size/degree/bit checks can suspend a branch but are not themselves
a min-ratio quality proof. The complete matching algorithm's exact
optimality verifier handles exceptional finite candidate outputs.

### 7.2 Registered provenance at every new quotient transaction

**Proof of Theorem 3, under the realization hypothesis.** The null quotient requires more than endpoint equality in a
vertex-map-only definition of flatness. Use the constructive
edge-lift records: a birth made by copying an actual input edge
registers `REAL(edge_id, orientation, endpoints, price_lifetime)`;
a connector created without an input edge registers
`TRUE_NULL(input_vertex_slot)`. These tags are carried through
every explicit source lift. A real loop has the first tag even
though both mapped endpoints coincide. Equal endpoints, zero
gradient, or a null projection several levels higher never infer
the second tag.

This is the same real-preimage convention used by source Section
4.2, item 4, when it assigns an input gradient and a no-shorter
input metric to a forest occurrence, and by Theorem 6.2's mapped
edge-length convention. It is supplied by the constructive lift
records, not deduced solely from source Definition 2.3. Recording
the already chosen edge identity is constant work per source edge
birth and is included in the explicit log interface.

For one quotient update, first collect the affected physical
fibers and their old incident quotient records while all old
metadata is live. Remove old attachments and propagate all
retirements. Recompute true-null connectivity and marked flags
inside those fibers. Then allocate fresh representatives with
the SAME immediate physical input image, register the retained
real edges with their original current input lengths/gradients,
and install the new attachments. A batch affecting both endpoints
of a real edge replaces that edge only once. Finally publish the
new quotient and release old metadata after all recursive copies
have retired. A source mark toggle needs only the corresponding
fiber's marked aggregate and upward-root selection.

Each touched fiber has O(Gamma) vertices and real incidences;
the conservative O(Gamma^2) update/log bound follows. The quotient
keeps no old representative exposed after its lifetime ends.
Private inactive-slot records have no numerical counters; real
registered pools retire before a remaining isolated null fiber
is suppressed. These rules provide stable IDs even when null
components repeatedly split and rejoin.

### Logical retirement does not assume a native DeleteVertex

A fresh quotient representative is a new LOGICAL parent lifetime.
After its incident real records have retired, that lifetime can
be marked inactive even if a downstream primitive has no vertex
deletion operation. Its native isolated slots remain allocated
until that primitive's bounded-size period ends. If the slot has
already been expanded into a binary port tree, the remaining
internal connector tree may also remain; this is an entire
physically null inactive fiber, not necessarily a set of native
degree-zero vertices.

Count all such native slots, connector records, master ancestries,
and tombstone associations in the nominal size and initialization
allowances. A local cover period has at most m wrapper events.
Each source log creates at most Gamma^O(1) quotient/attachment
records, and the source contributes Gamma^O(1) logs per event.
Thus all history born in that cover period totals
`m Gamma^O(1)` records. HRG family copies and port expansion
multiply this only by the already declared local A factors.
Private metadata is also counted and is discarded only when its
own instance ends.

Before suppressing an old parent image in the EXPORTED forest,
retire every formerly real geometric/input-path pool with its
signed and absolute transfers. The remaining child components
over that inactive lifetime have purely null parent projection;
omit their exposed lift while keeping the child-native records.
Retain the inactive association until child disposal and test it
before dereferencing the retired parent mapping. This is the
active-image rule of Section 8 of the Steiner bridge, applied
explicitly to every new quotient lifetime.

Only currently active logical lifetimes are exposed through their
own records; their number at one input image is bounded by the
current quotient's Gamma occurrence bound. Old native ghosts cannot
therefore accumulate physical occurrence congestion across null
splits/merges. Suppression/reactivation costs A times the child
occurrence bound per affected parent lifetime, within the local
copy term in Section 7.4. At a period restart all native ghosts
and associations are actually discarded, after retirement; no
unsupported DeleteVertex call or free infinite history is used.

### 7.3 Three distinct metrics and fixed allowed ranges

The construction keeps the following metrics separate.

| Metric | Values | Purpose |
|---|---|---|
| Private SNC metric | Rounded genuine integers at most m^4; fixed artificial backbone m^8 | The literal polynomial-length source call |
| Analytical HRG metric | Original real lengths; links gamma_HRG D_i and pairs 2 gamma_HRG D_i | The routing and monotone-decomposition existence proof only |
| Stored recursive metric | Original real lengths; links 1 and pairs 2; geometric path sums followed by H scaling | Actual portal/spanner input, child graph, and returned certificates |

The source's private state is never repriced to the analytical
or stored metric. Analytical labels do not enter recursive input
edges or numerical flow counters. Stored real-edge lengths dominate
their literal immediate physical traversal, and stored synthetic
null projections have positive length and zero physical charge.
This supplies the raw upper bound before cancellation.

All analytical scales are fixed during a local instance. In
particular choose them from a DECLARED allowed length-bit bound,
not the currently observed largest edge. One executable choice is

    d_guard = ceil(8U/log_2 k)+10,
    b_star  = (c0+100) U.

Use b_star in every local definition of gamma_diam. The actual
one-step length increase is `log k+O(log U)`, which is at most
`2 log k` eventually. Over d_guard steps this adds fewer than
100U bits eventually. Thus every permitted recursive insertion
stays under b_star, independently of whether the actual maximum
length subsequently increases within that allowed range.

The finite branch checks its size, one-step path/length budget,
depth and allowed bit caps before publication. An overflow
suspends that branch or is handled only at an already charged
period/size restart. It never silently increases all cover radii
or reprices all analytical scale labels. Restarting an instance
may select a new nominal local size and its associated scales;
the initialization and old-forest retirement are then charged.

Gradient ranges can likewise use a fixed declared cap such as
`(c0+100 d_guard)U` bits. Their exact values do not determine
gamma_diam. The local multiword arithmetic is charged against
this cap, rather than evaluated as an unbounded atomic operation.

### 7.4 Explicit change to the master recurrences

The metric variant changes the local work in exactly two ways.
First, filtering and quotienting each source cover log multiplies
the cover/HRG log volume by at most `Gamma^O(1)`. Second, smaller
port scaling changes only fixed edge labels and their bit bounds.
The HRG tree family, portal origin inventories, legal spanner
transcript, compressed Steiner topology, and input-edge path-pool
mechanism otherwise have the same explicit operations.

After absorbing that FIXED local power of Gamma into A, the sum
of nominal sizes of all recursive children of size m is at most
`m A/k`. Their total input recourse is at most A per local parent
edit in the amortized/prefix sense. Source quotient changes may
cause many local edits, but the factor is Gamma^O(1), not k.

For remaining depth r, exposed multiplicity G_r, normalized
initialization J_r and combined edit/query/log allowance T_r,
the complete recurrences are

    G_r <= A(G_(r-1)+1),
    J_r <= A(G_(r-1)+1) + (A/k)J_(r-1),
    T_r <= A T_(r-1)
           + O(k^2 A(G_(r-1)+1) + A J_(r-1)).

The k^2 term pays local alias work and O(k)-edge pool birth/death
work. A recursive FOREST edge log only attaches/detaches an
existing pool path, so it has no additional k factor. Actual
INPUT-edge lifetime changes have low child recourse and receive
their own O(k G_(r-1)) pool credit. Quotient-induced endpoint
replacements are ordinary local inputs to this same mechanism;
they do not cause a scan of every child occurrence forest.

The base on actual size t writes O(t) records and performs direct
cycle work in O((t+1)^3 poly(bits)); it has no mandatory k-cubed
startup. Quality and piece recurrences have one aggregate local
A factor. These equations have absolute constants, independent
of r. They give `k^10 A^O(r)` as a common safe envelope.

Every cover/alias instance has a local polynomial horizon under
the fixed-slot and period restarts. A master lifespan S^200 is
handled by repeated local instances, with actual forest retirement
and initialization charged to their edits. Inactive historical
slots are counted until the relevant instance is discarded.
The bounds therefore do not assume a small local primitive can
survive S^200 updates in one invocation.

Finally `log A=o(log k)` gives
`r=O(U^(1/168)/L_U)`, within the declared guard. Substituting
the parameters into these explicit recurrences proves (3).
The length and gradient bit estimates in Section 5 validate their arithmetic allowance simultaneously. This proves the conditional bound and its stated output interface. ∎
