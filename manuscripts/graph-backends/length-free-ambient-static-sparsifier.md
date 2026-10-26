# A static subgraph sparsifier with length-free ambient congestion

**Research construction, 24 October 2026.** This note composes the
deterministic unit-token router in
[the threshold-routing note](deterministic-token-routing-by-thresholds.md)
with [sparse weighted path selection](deterministic-weighted-path-selection.md).
The router uses the already reconstructed CS21 decremental expander
path oracle. It does not depend on a sequential interpretation of
the Chang--Huang--Su distributed routing algorithm.

The result is a research proof assembly from the explicitly named
interfaces. It is not an externally verified or implemented theorem.
A new matching exponent also requires the complete dynamic and
numerical composition, separately documented.

## 1. The unit-token router used here

Let H be a loopless undirected multigraph with m actual edge IDs,
no isolates, and conductance at least phi. Let U be a master
logarithmic bound and h = ceil(log_2(U+2)). Use the independent
integer parameters q >= 2 and r >= 1 from
[the separated static parameter reconstruction](separated-static-sparsifier-parameters.md),
with q,r <= U and q r h <= U. Its decremental path oracle gives

$$
\Lambda=2^{O(qrh)},\qquad
 F=2^{O(U/q+U/r+r^2h+qrh)},\qquad
 \phi^{-1}=2^{O(rh)}.                                  \tag{1}
$$

The threshold-routing note derives the following STATIC query
algorithm from that oracle. Given M token pairs, with at most
D deg_H(v) starts and at most D deg_H(v) destinations at every
vertex, it produces an explicit simple path for each token with

$$
\text{length}\leq\Lambda,\qquad
 \text{edge-occurrence congestion}\leq D Q,
 \quad Q=\Lambda\phi^{-O(1)}\mathrm{poly}(U).
                                                        \tag{2}
$$

The work, including its O(log(M+2)) fresh oracle rounds, is

$$
(mF+M\Lambda)\mathrm{poly}(U).
                                                        \tag{3}
$$

All hidden constants are fixed independently of q and r. The
algorithm handles the aggregate endpoint load D in one query.
It does not run D separately initialized copies of the expensive
oracle. Assigned paths remain valid in the unchanged original H
when their edges are later deleted from a temporary round oracle.
Parallel host edge IDs are preserved. The simple-graph subdivision
adapter, current live roots, bottom pruning, and actual-size bases
are those of the separated-parameter reconstruction.

## 2. Input normalization and the exact output type

The input consists of a demand graph J and annotated ambient paths
Pi(e), with matching endpoints, in an ambient graph H'. Parallel
demand edges have distinct IDs. Ambient congestion counts repeated
vertex occurrences, including annotated endpoints. Put

$$
L_0=\max\{1,\max_e |\Pi(e)|\},\quad
 C_0=C(\Pi),\quad \Delta=\Delta(J).
$$

For every nonloop demand edge, first erase closed subwalks from its
individual ambient image. Denote the resulting SIMPLE path by
Pi'(e). Use an explicit stack and a deterministic vertex dictionary;
the work is proportional to the supplied path-list size up to
logarithmic factors. Equality in loop erasure uses the IMMEDIATE ambient
vertex IDs of H', including their current native lifetimes. It never
uses eventual physical/root images. Distinct native aliases can have
the same physical image while carrying different frozen potentials;
a path between them is not an ambient closed walk. In particular,
null physical images do not authorize deleting an open native path.
Then

$$
L(\Pi')\leq L_0,\qquad C(\Pi')\leq C_0.                \tag{4}
$$

The output type includes this normalized edge-route table. The
congestion bound proved below is for Pi' composed with the new
subgraph embedding. It is NOT a statement about composing with an
arbitrary unchanged, nonsimple original Pi. Equivalently, callers
may supply simple input images after this explicit normalization.

In the touched-set distance application, an input projected edge
has an ambient path in the existing lower repair layers together
with, at most, its own central original edge. Loop erasure preserves
that property and the endpoints. Selecting the projected edge still
adds just that central original ID. If erasure removes the central
edge, this addition is harmless and can be unnecessary; it is never
necessary to add the old prefix/suffix edges again.

This normalization is distance-based. It does not preserve the
gradient of each individual edge image. The distance-cycle backend
uses its explicit correction circulation e minus the current route;
that correction must use the NEW normalized route. A separate
gradient-preserving interface cannot silently use this normalization.

Loop demands retain local, endpoint-annotated empty-route records
where the distance application permits this convention. They are
not passed to the nonloop expander hosts. Isolates are processed
at their actual bookkeeping cost and do not create a dense ambient
allocation.

## 3. Degree bands and a balanced weighted witness

Use the loopless degree bands in Section 2 of the separated static
parameter reconstruction. Its parameter r gives a dyadic common
threshold phi = 2^{-O(rh)}. The demand edge set is partitioned into
a residual J_0 of at most |V(J)| edges and band graphs J_i. Every
nontrivial component of J_i has conductance at least phi and
minimum degree at least phi 2^i. No maximum-degree promise is used.

All decomposition and pruning work is bounded by

$$
|E(J)|\,2^{O(U/r+r^2h+rh)}\mathrm{poly}(U).
                                                        \tag{5}
$$

For a component in band i put rho_i = phi 2^i. The balanced-port
witness construction gives a loopless constant-conductance
multigraph W_i with fresh edge IDs and

$$
\deg_{J_i}(v)\leq\rho_i\deg_{W_i}(v)
                  \leq D_w\deg_{J_i}(v),                 \tag{6}
$$

where D_w is one absolute constant. Every witness edge in this
component has weight rho_i. Direct residual edges have weight one
and keep their own identity routes. In particular,

$$
\begin{split}
 \sum_{i>0}|E(W_i)|&\leq O(|V(J)|\phi^{-1}U),\\
 \sum_{i>0}|E(W_i)|&\leq O(|E(J)|\phi^{-1}),\\
 \sum_{i>0}\rho_i|E(W_i)|&\leq O(|E(J)|),\\
 \phi\leq\rho_i&\leq\Delta.
 \end{split}                                            \tag{7}
$$

The last inequality follows from the minimum-degree property in
any nonempty component. Thus every constructed record inventory
has size 2^{O(U)} in the stated parameter range. The actual-size
construction does not allocate that upper bound.

## 4. Route witness tokens through their demand band

For every witness edge g of weight rho_i, make
Q_g = ceil(rho_i) directed tokens with the same endpoints. Fix an
orientation for g. The total number of these token records is at
most

$$
\sum_i(\rho_i+1)|E(W_i)|=O(|E(J)|/\phi).                 \tag{8}
$$

At each band vertex, the number of starts or destinations is at
most

$$
\lceil\rho_i\rceil\deg_{W_i}(v)
 \leq D_w\frac{\lceil\rho_i\rceil}{\rho_i}\deg_{J_i}(v)
 \leq \frac{2D_w}{\phi}\deg_{J_i}(v).                   \tag{9}
$$

The router therefore supplies all token paths with length at most
Lambda and total per-demand-edge occurrence load at most O(Q/phi).
All J_i edge sets are disjoint. The same global edge-congestion
bound holds for the union of all token families, even though a
vertex may occur in several different bands.

For one token path in J, compose its edges with their SIMPLE
ambient images Pi'. Its ambient occurrence at one vertex is at
most O(Lambda+1). It need not be a simple composed ambient walk.
The sum of ambient occurrences over all candidate token paths is
at most O(Q C_0/phi) at every ambient vertex.

Apply the sparse deterministic path-selection lemma globally to
these groups. Keep one token path P_g for each witness edge g and
give it the original weight rho_i. In that lemma,

$$
B\leq O((\Lambda+1)(\Delta+1)).                         \tag{10}
$$

It follows that the WEIGHTED ambient congestion of the selected
witness embedding is at most

$$
C(\Pi'\circ\Pi_{W\to J})
 \leq O\!\left(
     QC_0/\phi+\Lambda(\Delta+1)\log(N_{\rm amb}+2)
       \right)
 \leq Q\phi^{-O(1)}\mathrm{poly}(U)(C_0+\Delta).
                                                        \tag{11}
$$

N_amb counts only explicitly used ambient vertices; it is at most
2^{O(U)} in the master interface. Nonempty J has Delta >= 1.
The directly retained residual contributes at most C_0 and fits
the same bound.

The removed L_0 factor is accounted for precisely: one INDIVIDUAL
simple Pi'(e) visits an ambient vertex at most once, so the maximum
single-choice load is O(Lambda Delta), even if that path is long.
Reading and constructing its entire occurrence list still costs
O(L_0). No such work is declared free.

## 5. Route each original demand through the witness

For each edge of J_i make one token with its original endpoints,
now using W_i as the host. From (6) the start and destination load
at a vertex is at most rho_i deg_W_i(v). Use
D_i = max(1,ceil(rho_i)) in the routing interface.

The returned path of each demand has at most Lambda witness edges.
Every witness edge has unweighted load O(D_i Q). Dividing by its
weight rho_i gives normalized load

$$
O\!\left(Q\frac{\lceil\rho_i\rceil}{\rho_i}\right)
                       \leq O(Q/\phi).                  \tag{12}
$$

A large D_i does not multiply the expensive F term. The aggregate
router's work on this component is
(|E(W_i)|F+|E(J_i)|Lambda) poly(U). Summing the actual host sizes
uses (7). This is a direct aggregate query, not D_i separately
initialized queries. Even the more conservative load-one batching
work would have affordable output cost, since

$$
|E(W_i)|D_i
   \leq O\!\left(|E(J_i)|
                 \frac{\lceil\rho_i\rceil}{\rho_i}\right)
   \leq O(|E(J_i)|/\phi).                               \tag{13}
$$

Each token's path length is Lambda, independent of D_i. This is
necessary both for sparsity and for the recursive stretch bound.

## 6. Select an actual subgraph and compose

Let tilde J contain J_0 and all ORIGINAL demand-edge IDs used by
the one selected path P_g of each nonbase witness edge. Refcounts
deduplicate support while preserving the individual selected route
records. From (7),

$$
|E(\widetilde J)|
    \leq |V(J)|+\Lambda\sum_i|E(W_i)|
    \leq |V(J)|\Lambda\phi^{-1}\mathrm{poly}(U).    \tag{14}
$$

Compose the J-to-W paths from Section 5 with the selected W-to-J
paths from Section 4. This gives an explicit embedding of every
original demand into tilde J. Its length measured in J edges is
at most Lambda^2. Its ambient length is at most Lambda^2 L_0.
Weighted composition of (11) and (12) gives

$$
C(\Pi'\circ\Pi_{J\to\widetilde J})
   \leq Q^2\phi^{-O(1)}\mathrm{poly}(U)
                                      (C_0+\Delta).     \tag{15}
$$

Optional loop erasure of the final route IN J only removes edge
occurrences and their ambient expansions, so it cannot increase
any bound. The route can remain an ambient walk; no gradient
identity is inferred from geometric simplification.

With one common structural envelope

$$
\Gamma=2^{O(qrh)},                 \tag{16}
$$

the output satisfies

$$
\boxed{
 \begin{aligned}
 |E(\widetilde J)|&\leq |V(J)|\Gamma\mathrm{poly}(U),\\
 L(\Pi_{J\to\widetilde J})&\leq\Gamma,\\
 L(\Pi'\circ\Pi_{J\to\widetilde J})&\leq\Gamma L_0,\\
 C(\Pi'\circ\Pi_{J\to\widetilde J})&\leq
                       \Gamma(C_0+\Delta).
 \end{aligned}}
                                                        \tag{17}
$$

## 7. Work, words, and distance-layer compatibility

All host constructions, queries, deterministic selection, and
explicit path-list processing fit

$$
|E(J)|F^{O(1)}\Gamma^{O(1)}(L_0+1)
                       \mathrm{poly}(U),           \tag{18}
$$

plus actual input vertex bookkeeping. For token generation and
all-round work use (3), (7)--(9), and the aggregate query bound.
For ambient processing use the FULL length of every composed
candidate walk. Selection uses only positive sparse sums and
finite relative-precision arithmetic as proved in its separate
note. The dyadic witness weights, integer ceilings, parallel IDs,
and local endpoint maps have O(poly(U)) bit descriptions. No
common denominator over unrelated path choices is formed.

In a repair layer, the output memberships are still only the
selected central original edge IDs. All newly stored normalized
routes receive complete owner and inverse-occurrence records. An
event invalidating a used edge or vertex retires that current
record with its old metadata before replacement. An erased
unused subwalk needs no callback for the current route. Empty
routes retain endpoint records, so later native splits cannot
silently move their ends.

Consequently the membership recourse proof is unchanged, whereas
the local congestion recurrence becomes

$$
L_j\leq O(\Gamma)L_{j-1},\qquad
 C_j\leq O(\Gamma)(C_{j-1}+\Delta_j).                     \tag{19}
$$

The degree bound for projected inputs is paid by the maintained
incident-route congestion and selected-degree cap. Over K repair
levels, including one fresh-base initialization, this gives
length Gamma^{O(K)} and congestion
k poly(U) Gamma^{O(K)}. Explicit local work therefore has
Gamma^{O(K)} in place of Gamma^{O(K^2)}. The complete transaction,
native feedback, and raw-lift proofs remain necessary; this
static construction does not replace them.

## 8. Dependency boundary

This construction uses the degree-band and decremental path
reconstruction already named in the 6/7 checkpoint, the explicit
threshold token router, and sparse deterministic path selection.
Its normalization is a declared part of the distance interface.
It needs neither an efficient sequential CHS hierarchy nor an
unproved equality between fixed original and normalized images.

The next composition must count the accumulated inverse quality
d K log(Gamma) across d recursive backend levels. Removing the
L_0 factor from local congestion does not eliminate this stretch
cost and does not by itself justify the naive fastest balance.
