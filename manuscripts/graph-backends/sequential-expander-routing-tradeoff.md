# Sequential expander routing with linear parameter dependence

**Research proof assembly, 24 October 2026.** This note supplies the
sequential routing provider used by the separate 4/5 composition.
It composes explicit constructions. It does not identify sequential
work with distributed rounds, or claim external verification.
The delivered 5/6 threshold-router construction is independent.

## 1. Literal interface

Let G be a connected loopless undirected multigraph with m genuine
edge IDs, no isolates, and conductance at least 0 < phi <= 1.
Parallel IDs remain distinct. Let p >= 1 be an integer, U >= 2 a
master logarithmic bound, and h = ceil(log_2(U+4)). Input, token,
and exported record inventories have at most 2^{O(U)} entries.
The supplied lower bound phi has polynomially many bits in U.

The construction preprocesses the ACTUAL host in
```math
P\leq m\exp O(U/p+ph+\log\phi^{-1})\mathrm{poly}(U). \tag{1}
```
A query consists of an explicit ordered token list whose starts and
destinations separately have multiplicity at most D deg_G(v) at v,
where D >= 1 is an integer. A real load bound can be rounded up,
at a factor of at most two. It returns one simple path per token with
```math
Q=\exp O(ph+\log\phi^{-1}),\qquad
 \text{length}\leq Q,\qquad
 \text{edge-occurrence congestion}\leq DQ,                  \tag{2}
```
and query work
```math
mDQ\mathrm{poly}(U).          \tag{3}
```
This is an mD-volume bound, including dummy tokens, not a sparse
token-list-only bound. Preprocessing is paid once per host.
All polynomial degrees and constants are independent of p.

## 2. Degree reduction and original edge IDs

Use the incidence-port construction in
[degree-split-token-routing-interface.md](degree-split-token-routing-interface.md).
A vertex has one port per incident edge ID, joined by an explicit
constant-degree fiber expander, with separate constant-size cases.
An original edge joins its own two ports. The port graph is simple,
has n=2m vertices and O(m) edges, and bounded maximum degree.

For a port cut S, let z count minority ports in their fibers.
Internal fiber edges give at least alpha z crossings. External
edges give at least phi min(|S|,|S^c|)-(1+phi)z. These two bounds
prove port-graph conductance at least c phi for a fixed c>0.
No degree beyond the actual incidence inventory is allocated.

Assign starts at v cyclically among its ports, and independently
assign destinations. Each port has at most D of either. Thus it
suffices to route per-vertex load D on this bounded-degree graph.
Internal fiber moves project to empty moves at the original vertex;
external moves project to their one genuine original edge ID.

There is also a fully elementary alternative in
[hypercube-port-adapter.md](hypercube-port-adapter.md): round each
actual degree up to a power of two and use that hypercube as its
fiber. It has at most 4m vertices, O(m log(m+2)) edges, maximum
degree O(log(m+2)), and conductance at least phi/O(log(m+2)).
The hierarchy below permits this polynomial-logarithmic root degree;
only nonroot matching-graph hosts use the fixed nonroot degree bound.
All extra factors enter the already charged polynomial(U) work and
the one root embedding, so (1)--(3) are unchanged. This alternative
does not require a separate constant-degree expander-family theorem.

The old distributed parameter clipping discussed in the port note
is not used here. The explicit actual-size rule below replaces it.

## 3. Actual-size recursion and temporary precision

For the ACTUAL port graph put
```math
v=\lceil\log_2(n+2)\rceil,\quad
 k_{\rm route}=2^{\max\{5,\lceil v/p\rceil\}},\quad
 \lambda_{\rm cap}=C_\lambda(v+1)^2.                         \tag{4}
```
One fixed sufficiently large constant, for example the audited
energy-drop bound with C_lambda at least 10^7, is chosen once.
Stop recursion when the actual host has at most
```math
C_{\rm leaf}k_{\rm route}^5
                                        \lambda_{\rm cap}^2 \tag{5}
```
vertices. This is a threshold, never a padding request.

The hierarchy has depth d=O(log(n+2)/log k_route)=O(p).
Each internal terminal set is a fixed fraction of its host, and its
t<=k_route parts have size Theta(|X|/k_route). For fixed sufficiently
large C_leaf, (5) supplies exactly
```math
\min_i|Y_i|\geq8\lambda t^2,\qquad
 n'_X=6|X|/k_{\rm route}\geq\lambda t^2,\quad
 \lambda\leq\lambda_{\rm cap}.                              \tag{6}
```
No k_route>=lambda requirement or CHS epsilon clipping is needed.

All leaves have polynomial(k_route,v) vertices. A whole small host
declared a leaf is processed at its actual size. When k_route=32,
the actual depth still is O(p). Thus every parameter case has a
finite literal algorithm.

The exact local PSD test, energy conditional expectations, and leaf
walk moments may use multiword temporary integers with polynomial
dependence on k_route, v, log(phi^{-1}), and where needed inverse
local expansion. Their complete bit work is included in preprocessing.
These integers are not stored numerical-client lengths or gradients.
Only IDs, subsets, matching pairs, and explicit route lists are exported.

## 4. Virtual hierarchy and exact root coverage

[virtual-expander-hierarchy-reconstruction.md](virtual-expander-hierarchy-reconstruction.md)
proves the hierarchy using
[sequential-short-path-matching.md](sequential-short-path-matching.md)
and [sequential-fresh-cut-matching-adapter.md](sequential-fresh-cut-matching-adapter.md).
The corrected success-coverage interface is proved separately in
[explicit-virtual-cut-balance-wrapper.md](explicit-virtual-cut-balance-wrapper.md).
Every weak success, including a spectral leaf reached after earlier
cuts, retains at least a 1-beta fraction of its current host, for
the fixed beta=1/1000. Its explicit cut-union wrapper consequently
retains more than two thirds of the wrapper's input on success.
Only the last successful hierarchy is retained. This fixed-constant
repair does not add another geometric composition.

The short-path primitive is explicit truncated decremental BFS.
Every round begins with an empty excluded set. Repeated calls use the
FULL unchanged host. In outer round j use cut threshold psi/(16j^2);
old failure cuts are bookkeeping only. Summing their boundaries
certifies the final union and preserves failed-part terminal coverage.
Exact single-color saturation supplies the covering matching, or an
actual sparse cut containing every uncovered source. There is no
unaccounted leftover set.

The continuing abstract cut player uses balanced-cut sparsity at most
1/8, with a matching covering at least half its smaller side.
[half-matching-entropy-progress.md](half-matching-entropy-progress.md)
proves entropy gain at least 5N/1024 per continuing round and the
explicit cap 512 ceil(log_2(N+2)). Retain every matching occurrence
as a distinct multigraph edge; deduplication would invalidate its
crossing-mass bound. This replaces the source's larger-threshold
half-matching calculation. The abstract 1/8 threshold and the
embedding-host psi/(16j^2) cut budget are distinct parameters.

The coarse-cut primitive tests an exact rational Laplacian inequality
on a weighted mean-zero subspace. A negative vector yields a weighted
median sweep cut; a positive test certifies expansion. It has fixed
polynomial block work and does not enumerate subsets.

Every successful node exports an explicit graph H_X on EXACTLY X.
Its parts Y_i=X_i disjoint-union B_i partition X; covering matchings
inject B_i into good children X_i. Interior vertices of embedded paths
do not silently enlarge X. Parent graphs include H_{X_i} and covering
edges literally, with their IDs. Indeed H_X[X_i]=H_{X_i}: newly added
host edges join distinct parts. Thus every good-node graph is induced
in the ROOT VIRTUAL graph, not asserted induced in the physical graph.

Continued cut-matching hosts are unions of O(v) matchings. A successful
virtual output is not inserted into a continuing host. Host degrees
therefore are O(v), virtual degrees O((d+1)v), nonroot expansion is
v^{-O(d+1)}, and root expansion is phi^{O(1)}v^{-O(d+1)}.
Only the original root uses the original inverse phi.

At that root every cut threshold is below true expansion. Hence no
root failure cut exists, exact covering covers every remaining
vertex, and a nonempty respecting coarse cut is impossible. The
primary root terminal set is ALL physical vertices.

The provider constructs ONE root map
```math
f_0:H_{\rm root}\longrightarrow G^\diamond
 \quad\hbox{with length and congestion }\phi^{-O(1)}v^{O(p)}.
                                                               \tag{7}
```
Only the top construction level pays inverse phi; other levels pay
polynomial v. Child query paths are first viewed as paths in H_root
by literal inclusion. The map f_0 is then applied once.

## 5. Postprocess only the retained hierarchy

First finish the hierarchy construction and retain its final nodes.
Discard failed candidate hierarchies. Only THEN construct the
shufflers and leaf circuits described below. Full query routers are
not recursively rebuilt inside every trial of the cut player.

[polynomial-energy-cut-player.md](polynomial-energy-cut-player.md)
chooses the required separated terminal sets by deterministic
conditional expectations of even moments, in polynomial block work.
Exact saturation in the current virtual expander supplies genuine
matching paths. After lambda=O(log(t+2)log(n+2)) rounds, the lazy
symmetric matrices satisfy
```math
|(Q_\lambda\cdots Q_1)[i,j]-1/t|\leq1/(100t).                 \tag{8}
```
Here Q_a[i,j]=p^a_{ij}/(2n'_X) off the diagonal, counting actual
matching portals. Unequal part sizes are explicitly allowed.

[sequential-leaf-routing-and-chs-work.md](sequential-leaf-routing-and-chs-work.md)
constructs bounded-load matching paths with a symmetric lazy random
walk distribution and exact moment conditional expectations.
This is deterministic polynomial-work selection of explicit paths.
Output quality is polynomial in inverse expansion and logarithmic
leaf size; it has no polynomial k_route factor.

Precompute the cross-block matching paths of a bitonic network.
For load L use power-of-two-rounded block length. Comparator
distances below that length stay within the block. The
O(log^2(leaf size)) cross-block matching patterns are independent
of L. The full-router note proves this literal scalar-network
implementation, so no new network preprocessing is charged per load unit.

Union all shuffler, folding, and elementary leaf paths in H_root.
At one depth, good-node vertex sets and their induced edge sets
are disjoint, so congestion takes their maximum. Sum over depths
and circuit layers. The virtual union has length and congestion
phi^{-O(1)}v^{O(p)}. Apply (7) ONCE to obtain
```math
A=\phi^{-O(1)}v^{O(p)}                   \tag{9}
```
for the entire physical primitive family. Original phi is not
raised to the depth. Actual list construction is charged.

## 6. Direct full-query induction

[conditional-full-router-from-shufflers.md](conditional-full-router-from-shufflers.md)
proves the query; Sections 3--5 supply ALL its hypotheses.

A part router folds bad endpoints into good children, invokes a
strictly smaller full router, and unfolds the exact destination.
Folding fibers have size at most two. At shuffler step a, color ell
moves exactly floor(p^a_{ij} N_{i,ell}/(2n'_X)) tokens to part j.
Cyclic assignments to genuine portals and part-router paths implement
these moves. Per-color rounding error is at most t per step; (6)
pays the accumulated error and bounds endpoint load by O(L lambda).

Scatter real tokens colored by destination part. Separately scatter
2L dummy tokens from EVERY vertex, colored by origin part. In each
current part and color there are more dummies than real tokens.
Match reals injectively to dummies, route to their current locations
within the part, then reverse the recorded dummy traces. Reals
reach their correct parts at load at most 2L. A final part-router
call supplies their exact requested destinations.

There is no same-level recursion. Every reversed trace is explicit,
and dummy assignment is injective. Nested copying of returned traces
has its fixed multiplicity per level in the recurrence. If V_j is
the sum of actual vertex-count times load over invocations at depth j,
```math
V_0=nL,\qquad V_{j+1}\leq c(\lambda+1)^2V_j.                 \tag{10}
```
The same factor bounds total usage of each fixed primitive. Therefore
```math
\begin{aligned}
 \text{length}&\leq A(c(\lambda+1))^{d+1},\\
 \text{congestion}&\leq LA(c(\lambda+1)^2)^{d+1},\\
 \text{work}&\leq nLA(c(\lambda+1)^2)^{d+1}
                       \mathrm{poly}(\log(nL+2)).
 \end{aligned}                                               \tag{11}
```
This applies the flattened A once, not once per level.

Sorted portal groups allow quota enumeration in
O((M+t^2)polylog(nL)) work per step: each positive quota consumes
a token, plus one failed stopping test per nonempty part/color.
Since t^2<=|X|, this and ALL dummy inventories fit (10).
Immutable concatenation records avoid repeated prefix copying;
final materialization is charged to its actual occurrences.

Project port routes back to G, then erase closed subwalks using
ORIGINAL-HOST vertex IDs with their lifetimes and distinct edge IDs.
A stack and deterministic position dictionary cost the explicit list
length. Endpoints are preserved; every load and length decreases.
Empty routes retain endpoint annotations. This proves (2)--(3).

This is separate from normalizing a later ambient route table.
Distinct native aliases are never merged merely because their
eventual physical images coincide.

## 7. Sequential preprocessing work

The short-path and hierarchy notes give the explicit recurrence
```math
T(N,j)\leq v^{c_1}\sum_i T(N_i,j-1)
       +Nk_{\rm route}^{c_2}v^{c_3}
                         \mathrm{poly}(\psi_{\rm cut}^{-1}),
 \qquad\sum_iN_i\leq c_4N,                                  \tag{12}
```
with absolute constants. Only polynomial-v repeated-attempt costs
multiply across recursion. The local k_route^{c_2} cost is additive
at every host, not a multiplier on child recursion. Original phi
occurs only in the first host's threshold.

Shuffler and leaf preprocessing occurs afterward on retained nodes.
Their same-depth actual edge inventories are disjoint and total
O(npv). Polynomial local work, exact arithmetic, and explicit path
output are bounded by
```math
nk_{\rm route}^{O(1)}\phi^{-O(1)}v^{O(p)}.              \tag{13}
```
Leaf polynomial size is used only in preprocessing, never in output
quality. Since log k_route=O(1+v/p), this is
```math
n\exp O(v/p+p\log(v+2)+\log\phi^{-1}).                 \tag{14}
```
Use n=2m and v=O(U) to get (1). Separate expander components are
initialized at their own actual sizes; the master bound is never
used as an allocation size.

## 8. Static application parameters

For a degree-band decomposition with independent parameter r,
phi^{-1}=exp O(rh). The router has
```math
\log Q=O((p+r)h),\qquad
 \log(P/m)=O(U/p+(p+r)h).                                   \tag{15}
```
[linear-parameter-static-sparsifier.md](linear-parameter-static-sparsifier.md)
combines this with degree-band work exp O(U/r+r^2h).

The cited construction notes, rather than a blanket import of CHS,
provide this result. Exact-output checking in a later matching
algorithm does not certify these work bounds; their proof is the
explicit composition above.
