# Independent audit of the fully dynamic APSP time--stretch curve

**25 October 2026. Audit status: passes with two explicit interface/accounting
clarifications incorporated into the main note.** The object audited is
`apsp_time_stretch_tradeoff.md`, including its numerical query interface,
arbitrary-degree adapter, growing parameters, and derived public comparison.
This is an independent proof audit of the research construction. It is not
an implementation, an external verification, or a claim that all public
dynamic shortest-path tradeoffs have been optimized.

Put

\[
 U=\log(N+4),\qquad h=\log(U+4),
\]

where \(N\) bounds initial vertices and edges plus external elementary
updates. The audited guarantees are deterministic, fully dynamic, numerical
distance queries on undirected graphs with positive polynomially bounded
integer lengths. Initialization plus all updates costs the actual initial
inventory plus the actual update count, multiplied by the displayed factor.
The update guarantee is amortized. The distance-query guarantee is worst-case
polynomial logarithmic time in \(N\).

The two principal points are

\[
\begin{array}{c|c}
 \text{amortized work factor}&\text{distance stretch}\\ \hline
 \exp O(U^{11/14})&\exp O(U^{6/7}h)\\
 \exp O(U^{3/4}h^{1/2})&\exp O(U/h).
\end{array}
\tag{A1}
\]

The first has the same displayed stretch scale as the KMG theorem used for
the direct comparison. The second has a coarser, still subpolynomial,
stretch. Neither is a constant-factor approximation, a worst-case update
bound, an exact-matching improvement, or a fast simple-path reporting
theorem measured only by the final projected path size.

## 1. Proof dependencies that were actually checked

The audit uses the separated local envelopes and metric construction in
`separated_metric_forest_and_strong_sssp.md`, Sections 2--7. The relevant
checkpoint imports are:

* `current_checkpoint/linear_parameter_static_sparsifier.md` for the
  independent parameters \(p,r\), explicit static construction work, and
  actual-size operation;
* `current_checkpoint/normalized_projected_route_composition.md` and
  `amortized_static_base_distance_sparsifier.md` for the repaired dynamic
  metric sparsifier and its normalized, linear-in-\(K\) stretch exponent;
* `current_checkpoint/demand_route_notifications_and_local_work.md` and
  `distance_degree_reset_candidate.md` for emitted edits and recursive
  inventory, including late spending of initial selected-edge credit;
* `current_checkpoint/disconnected_component_backend_wrapper.md` for
  small components, inactive roots, and isolated vertex inventory;
* `current_checkpoint/uniform_source_interfaces_for_4_5.md` and
  `polynomial_bit_stretch_stable_forest_integration.md` for uniform
  elementary source interfaces and finite arithmetic.

The last audit has a title referring to the older \(4/5\) choice. Its
construction-level arguments distinguish fixed polynomial elementary
operations from the old complete dynamic-spanner theorem; those arguments
apply to the new parameters after the checks in Section 5 below. The title
alone is not a license to invoke the old complete theorem at a larger
repair depth.

For the public comparison and query design I independently read KMG,
[*A Dynamic Shortest Paths Toolbox*, arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402v1),
in particular Theorem 3.1, Theorem 3.7 and its preceding weighted-bucketing
discussion, Theorem 4.1, Algorithm 6, and Claims 4.3--4.6. The local source
copy is `sources/dynamic_shortest_paths_toolbox.txt`. These statements give
the precise maintained data needed for a small query, rather than merely
a graph whose shortest path could be computed on demand.

## 2. The query does not perform a hidden \(k\)-sized search

At a nonbase hierarchy level, the maintained data include the current
nearest-pivot pointer \(p(v)\), the exact distance to \(p(v)\), and the
exact distances to vertices in the strict pivot ball. KMG Theorem 3.1,
items 2--4, explicitly maintains these objects. Their enumeration and
updates have polynomial dependence on \(k\); that dependence belongs to
maintenance, not to a query.

The current query has one pair \((u_i,v_i)\) at level \(i\). It performs
the following actions.

1. If the vertices are equal, return zero. If the pair is disconnected,
   use the local component/base convention and return infinity.
2. If \(v_i\) is in the explicitly maintained strict ball of \(u_i\),
   or is its pivot, return the stored exact distance.
3. Otherwise read the two stored pivot legs, look up the two current
   child canonical roots, and make one recursive query between them.
   Divide that child answer by the stored reset scale \(H_i\), then add
   the two parent legs.
4. At an actual-size base instance, read an entry of the exact APSP
   table maintained after each settled encoded update.

Ball membership may be implemented with a deterministic balanced
dictionary keyed by a vertex identifier. It costs \(O(\log N)\) rather
than requiring randomized hashing or the source's unit-cost lookup
convention. No ball enumeration occurs during a numerical query. The
current pivot pointer and child-root pointer are maintained records.

The base table is computed as update work. An actual base has at most
\(k^{O(1)}\operatorname{poly}(U)\) records, so even a direct cubic APSP
computation after each encoded edit costs \(\exp O(x)\operatorname{poly}(U)\)
when \(k=2^x\). That is within the charged local work. Computing a
shortest path afresh at query time would not establish the theorem and is
not the algorithm being audited.

For depth \(d\), the numerical query therefore takes

\[
              O(d\operatorname{poly}(U))=\operatorname{polylog}N.
\tag{A2}
\]

This is the same structural reason as KMG Claim 4.4: that claim explicitly
reads the precomputed base table. Its argument does not scan the base
graph. The current construction retains this query contract while changing
the maintenance primitive.

### Metric correctness and the reset scales

Write \(D=d_{G_i}(u_i,v_i)\). If the local query does not terminate, then

\[
 d(u_i,p(u_i))\le D,\qquad
 d(v_i,p(v_i))\le 2D,\qquad
 d(p(u_i),p(v_i))\le4D.
\tag{A3}
\]

The selected graph is an upper metric approximation on pivot pairs with
factor \(\rho=\exp O(Kg+h)\). The positive port reset, after division by
\(H_i\), has an additional factor at most two. Thus, if the recursive
stretch is \(\gamma_{i+1}\), the returned value is at most

\[
        3D+8\rho\gamma_{i+1}D
            \le 11\rho\gamma_{i+1}D.
\tag{A4}
\]

Every selected edge represents an endpoint-preserving parent walk whose
literal length is bounded by its label, and the positive connector reset
preserves that domination after division by its scale. The exact legs and
the child walk concatenate to a valid parent walk. This proves that the
returned estimate never underestimates distance. Iterating (A4) yields

\[
               \log\gamma=O(dKg+dh).
\tag{A5}
\]

Dividing by the internal scale is essential: the child's labels are not in
the parent's units. This operation has been made explicit in Section 4 of
the main note. The outer arbitrary-degree adapter has its own final scale
division as well.

## 3. Stable roots and disconnected instances

The exposed query handle of an original vertex is its permanent node
\(q_v\), retained for that vertex's lifetime. Rebalancing its incidence
tree changes connector edges and, if necessary, the edge from \(q_v\) to
the current tree root. It never changes \(q_v\).

At an internal degree reset, \(q(a)\) is stable throughout the actual
parent vertex's lifetime in the current parent period. A query uses the
current pointer of its current pivot. When a period is rebuilt, all old
child records are retired and the newly built hierarchy is published as a
settled state. No query sees a mixture of the old and new parent periods.
The numerical interface does not require an internal child node to survive
an ancestor restart; only the exposed original query handles must remain
valid. Recomputing the corresponding pointer is part of restart work.

The disconnected-component adapter is relevant here. Small initial
components have a local pivot and are stored at their actual size. Pairs
whose chain meets the same unexported pivot can finish locally. Distinct
pivots connected by a genuine parent path have a child representation; a
nontrivial inter-pivot query cannot be silently dropped as an isolated
ghost. Endpoints are promoted before a joining inserted edge is processed.
Isolated physical query handles are counted once and are not rescanned at
every active-component restart. Infinity answers do not require a search
over the whole current graph.

These conditions are weaker than the fixed canonical maps of the later
flat-forest theorem, but they must still be stated. A raw-cycle projection
alone would not supply them. The present metric hierarchy supplies them
independently.

## 4. Arbitrary degree: current incidence, atomic edits, and lifetime counts

The main note uses a current-incidence, leaf-oriented balanced binary search
tree at each original vertex. Its leaves are exactly the current edge
incidences and retain their incidence identities during rotations. Parallel
edges use distinct lifetime identifiers. The stable \(q_v\) attaches above
the tree root. With one real edge at each incidence leaf, all expanded
degrees are at most three.

A rotation changes a constant number of connector edges. Insertion and
deletion use \(O(\log N)\) such elementary edits. New tree nodes are
inserted while isolated, and retired nodes are deleted only after their
incident edges have been removed. Delete all changed old connectors before
adding the changed new connectors. During the removal phase the graph is a
subgraph of the old degree-three graph; during the addition phase it is a
subgraph of the final degree-three graph. The source therefore never sees
an intermediate degree violation. Temporary disconnection is permitted.
External queries observe the final settled state of an original update.

This is an ordinary dynamic degree reduction, and does not require a tree
with \(N\) leaves at every vertex. At any settled time the representation
has \(O(n+m)\) nodes and edges. Every inserted incidence creates only a
constant number of tree nodes; rotations create no new nodes. Consequently
there are \(O(N)\) vertex births in the entire external history.

There is a small but real distinction between node births and edge
lifetimes: connector rewiring creates new connector edge lifetimes. Their
total number is \(O(N\log N)\), the same as the encoded edit transcript.
The original sentence calling all record births \(O(N)\) has been
corrected in the main note. A polynomially larger internal master cap, for
example \(N^2\), dominates this history. Its logarithm is \(\Theta(U)\),
so no claimed logarithmic exponent changes. This is a parameter cap, not
permission to allocate \(N^2\) graph records.

All connectors have length one and all real edges have length
\(H\ell_e\), for one fixed power of two \(H\ge C\log N\). A projected
walk discards nonnegative connectors and divides its real-edge lengths by
\(H\). Conversely, a simple original path with \(b\ge1\) edges lifts
using \(O(b\log N)\) connectors. Positive integer original lengths imply
its original length is at least \(b\), so

\[
 d_G(u,v)\le H^{-1}d_{G'}(q_u,q_v)\le 2d_G(u,v).
\tag{A6}
\]

The proof uses a simple shortest path only to establish this metric
inequality; it does not enumerate that path during a query. Equal endpoints
return zero. Separate original connected components remain separate.

## 5. Growing parameters and actual-size validity

The local work and metric envelopes are

\[
\begin{aligned}
 g&=O((p+r)h),\\
 f&=O(U/p+U/r+r^2h+(p+r)h),\\
 \log P&=O(U/K+g+h),\\
 B&=O(x+f+Kg+d\log P+h),\\
 \log\gamma&=O(dKg+dh).
\end{aligned}
\tag{A7}
\]

The source-independent normalized repair supplies the \(Kg\) term. The
old complete KMG dynamic-spanner theorem has a restriction on \(K\) and
is not invoked with the new \(K=t^2\).

For

\[
       p=r=\Theta(t),\quad K=\Theta(t^2),
       \quad x=\Theta(U/t),\quad d=O(t),
\tag{A8}
\]

the static provider's declared range \(1\le p,r\le U\) and
\((p+r)h\le U\) holds for both points in (A1), with considerable slack.
The provider is applied to actual local inputs. If a small component does
not meet a displayed asymptotic parameter regime, its direct exact or
full-edge representation is within the local factor; it is not padded to
the master size.

The size-reduction condition also has slack:

\[
 \frac{x}{U/K}=\Theta(t)\longrightarrow\infty,
 \qquad
 \frac{x}{th}=\Theta\!\left(\frac{U}{t^2h}\right)
                  \longrightarrow\infty.
\tag{A9}
\]

Thus \(x\) exceeds a sufficiently large fixed multiple of \(\log P\).
The actual recursive depth is controlled by \(U/(x-O(\log P))\), which
is \(O(t)\). A finite number of small master sizes is handled by the
direct exact algorithm.

Elementary center, path-inventory, stable-forest, tree-partition, and
notification operations have fixed polynomial degrees in \(k,U\) and the
stored bit length. Their polynomial degree is not chosen as a function of
\(p,r,K\). The only growing-parameter exponential dependencies charged
here are the displayed factors in (A7).

The initial selected inventory is an allowance
\(O(m_0P/k)\), not merely an initial-time cost. It may become child edits
later in a parent period and is included in the chronological recurrence
that proves (A7). Restarting after \(\Theta(m_0/k)\) parent edits charges
this allowance to the period. Repeating the recurrence amplifies child
maintenance by \(P\); it does not raise the entire static construction
factor to the number of hierarchy levels.

### Bit lengths

The positive scale multiplications and native core length formulas add
\(O(U)\) stored bits at each level. The finite-bit stable-forest adapter
keeps this statement independent of the approximation factor: an exported
core label is bounded by a polynomial in the actual vertex count times a
parent length, rather than by repeatedly multiplying every stored value by
the global stretch. Hence

\[
                 b_*=O(U(d+1))=\operatorname{poly}(U).
\tag{A10}
\]

Both choices have \(t\le U^{1/4}\), so a conservative bound is
\(O(U^{5/4})\) bits. Stored reset scales are powers of two; cumulative
scale denominators also have polynomially many bits. Weighted construction
work, dictionary operations, exact additions/comparisons, and the query
arithmetic therefore cost only polynomial logarithmic factors. The audit
does not infer bit complexity merely from a magnitude assertion.

## 6. Recalculation of the new curve

Substitution of (A8) gives

\[
\begin{aligned}
 f&=O(U/t+t^2h),\\
 Kg&=O(t^3h),\\
 d\log P&=O(U/t+t^2h),\\
 B&=O(U/t+t^3h),\\
 \log\gamma&=O(t^4h).
\end{aligned}
\tag{A11}
\]

At \(t=\Theta(U^{3/14})\), the work-leading term is \(U^{11/14}\).
The other term \(U^{9/14}h\) is asymptotically smaller. The logarithmic
stretch is \(O(U^{6/7}h)\). This proves the first point of (A1), without
dropping an iterated logarithm on a term of equal leading power.

At \(t=\Theta((U/h^2)^{1/4})\), the two work terms are
\(U^{3/4}h^{1/2}\) and \(U^{3/4}h^{-1/2}\), while the logarithmic
stretch is \(O(U/h)\). This proves the second point.

The general fixed-\(a\) and slowly growing-\(\omega\) versions in the
main note follow from the same substitution. They remain numerical distance
tradeoffs. No flattening recurrence or cycle-quality factor is silently
removed from a different application.

## 7. The stronger public \(59/63\) composite is legitimate

The main comparison does not stop at the printed KMG exponent. I checked
that its derived public composite uses only the old local KMG theorem plus
an ordinary dynamic binary-tree degree reduction.

KMG Theorem 3.1 gives, with

\[
       g_0=O(U^{2/3}h),\qquad q=O(U/K+g_0+h),
\tag{A12}
\]

child inventory and edit expansion \(\exp O(q)\), local update work
\(\exp O(x+q+K^2g_0)\), and pivot metric stretch
\(\exp O(Kg_0)\). Its graph-degree factor is reset to a constant by
applying the current-incidence binary-tree adapter to every child, not just
to the original input. That adapter costs polynomial logarithmic work per
child edit and a constant metric factor. The source permits exactly the
edge and isolated-vertex operations required by its rotations.

For a parent period, current and retained child records are counted as
\(O(mP/k+Pz)\), with \(P=\exp O(q)\). Retired-but-retained source
vertices remain actual records until the period restart. Reinitialization
after \(\Theta(m/k)\) parent edits and an actual-size exact base give the
amortized recurrence

\[
 B_{\rm pub}=O(U/d+K^2g_0+dq),\qquad
 a_{\rm pub}=O(dKg_0+dh).
\tag{A13}
\]

The base APSP and query structure are the same as in Section 2. This
derived recurrence is not the degree-growing worst-case recurrence printed
in KMG. In particular, it does not assert that the public theorem itself
prints \(59/63\), or that this ordinary wrapper preserves its worst-case
update guarantee.

Set

\[
 d=\Theta(U^{4/63}),\qquad K=\Theta(U^{8/63}),
 \qquad x=\Theta(U^{59/63}).
\tag{A14}
\]

Then

\[
\begin{aligned}
 U/d&=\Theta(U^{59/63}),\\
 dU/K&=\Theta(U^{59/63}),\\
 K^2g_0&=O(U^{58/63}h),\\
 dg_0&=O(U^{46/63}h),\\
 dKg_0&=O(U^{54/63}h)=O(U^{6/7}h).
\end{aligned}
\tag{A15}
\]

The \(U^{58/63}h\) term is smaller than \(U^{59/63}\). Therefore the
claimed public composite is

\[
       \exp O(U^{59/63})\text{ amortized work},
       \qquad \exp O(U^{6/7}h)\text{ stretch}.
\tag{A16}
\]

### The old parameter restriction is satisfied locally

Unlike the new construction, this composite really does invoke the complete
old theorem, so its range must be checked at every nonbase call. That
theorem requires

\[
          K=o\!\left(\frac{(\log m_{\rm local})^{1/6}}
                                  {\log\log m_{\rm local}}\right).
\tag{A17}
\]

Before entering the base case, \(\log m_{\rm local}\ge c x\). The
right-hand side consequently has leading power at least
\(U^{59/378}\), up to logarithms; the selected \(K\) has power
\(U^{8/63}=U^{48/378}\). The strict gap of powers verifies (A17),
including at the smallest nonbase instances. A check only against the
top-level \(U^{1/6}\) would have been insufficient.

The public Theorem 3.7 explicitly allows quasi-polynomially bounded lengths
and states the weighted-bucketing extension in its preceding paragraph.
Recursive length growth uses \(O(Ud)\) bits, which is a fixed polynomial
in \(\log m_{\rm local}\) throughout the nonbase regime. Thus its
length buckets and finite arithmetic incur polynomial logarithmic factors,
not an uncharged exponent. This check does not import the new normalized
router into the public baseline.

Finally, the old KMG Claim 4.6 has a heading inconsistent with its own
proof. Theorem 4.1, its printed parameters, and the proof use \(20/21\),
whereas the heading says \(14/15\). The main note correctly uses the
supported theorem/proof value and separately presents (A16). It does not
promote the isolated heading to a stronger public theorem.

## 8. Remaining scope and further transfers

No unresolved interface obstacle was found for the numerical APSP theorem
under the named research-proof imports. The two small clarifications made
by this audit are the explicit internal scale division/base-table lookup
and the \(O(N\log N)\) connector edge-lifetime accounting.

The \(59/63\) comparison is a proved derived public composite, not a
claim of global optimality over public APSP methods. Other public
tradeoffs have independent approximation regimes and parameter restrictions;
the primary-source checks in Section 6.3 of the main note must remain part
of any broader novelty discussion. Our \(11/14\) guarantee is amortized,
whereas the directly printed KMG bound is worst-case.

Restricting a numerical all-pairs oracle to one fixed source immediately
gives the same coarse-stretch numerical single-source query interface. That
observation alone is not a significant new decremental \((1+\epsilon)\)
SSSP theorem. The strong-forest application pays for metric stretch in its
covering scale condition and for explicit forest congestion in its
flattening recurrence. The APSP curve cannot simply be substituted while
discarding those costs. The separately proved \(7/8\) strong forest and
Gomory--Hu construction retain their own jointly balanced parameters.

Likewise, a promised short-hop or short-simple-path oracle cannot be
replaced merely by a coarse numerical distance estimate. Any such transfer
must establish its approximation tolerance, its literal path-output cost,
and its resource accounting independently. This is the boundary relevant
to the next proposed expander-routing application.
