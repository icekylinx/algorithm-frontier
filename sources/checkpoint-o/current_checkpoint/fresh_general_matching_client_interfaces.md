# Exact interfaces from arbitrary general matching to priced circulations

**Mathematical interface reconstruction, 24 October 2026.** This note
states the matching-side implications used by the current deterministic
research candidate. It treats the complete deterministic raw-cycle
backend as an explicit hypothesis. It does not infer its performance
from an output verifier, from a static ratio oracle, or from an
approximately feasible flow.

The state framework is OAI Sections 3--5:
[primary source](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026).
The exact source interfaces relevant here are the Section 3 **Ledger
invariant**, **Bottom surplus**, structural preserving-deletion formulas,
and **Exact exchange projection**; the Section 4 phase-debt and
no-false-stall arguments; and the Section 5 priced-step interface.
The replacements below specify where their implementation or scope
differs from the original perfect-matching presentation.

## 1. Required numerical hypothesis

For master \(S=2^s\), suppose one finite deterministic backend has a
computable subpolynomial cap \(E(S)\). On every actual priced instance
of size at most \(S^2\), it supplies:

* initialization per actual record, edits, queries, and complete
  representation logs within the declared cap;
* an explicit circulation represented by unit signed real edges and
  forest paths, with inverse approximation factor at most \(E(S)\)
  relative to the **sum of all mapped traversals before cancellation**;
* stable immediate endpoint and edge-lifetime images, complete old
  metadata through retirement, counted dormant occurrences, and
  complete signed and absolute-motion transfers;
* finite-word implementation and the polynomial master histories
  used by the clients.

Its promise includes disconnected instances, parallel edge IDs,
genuine loops and bounded local base cases. A net-norm cycle answer
alone is insufficient.

Set
\[
 D=\operatorname{pow2ceil}(\max\{16,4E(S)\}),\qquad
 q=(16D)^{-1},\quad
 \delta=S^{-1000},\quad \varepsilon=S^{-3000}.
\]
The priced-client proof, with its direct master price cap, gives
LOW impossibility whenever a circulation has
\[
       g^{\mathsf T}d>\tfrac12\sum_e\lambda_e|d_e|.
 \tag{1}
\]
Otherwise it returns LOW or an exactly conserved grid step with
relative absolute motion at most \(q/100\) and objective increase
\(\Omega(q^2)\). A failed prerequisite suspends the branch; it is
never interpreted as LOW. The full proof and cost are in
[the priced-step reconstruction](priced_logarithmic_steps_from_raw_cycles.md)
and [the decoupled client](decoupled_numerical_client.md).

## 2. Exact reduction and decoding require no perfectness

After one linear input cleanup, let the simple nonisolated graph have
\(r\) vertices and \(m_s\) edges. Replace a degree-\(d_v\) vertex by
an odd path with \(2d_v-1\) vertices, using its odd positions as
incidence ports. The resulting graph is subcubic. Put
\[
 A=2m_s-r,\qquad N=4m_s-r.
\]
Every original matching lifts to a matching with \(A\) additional
internal edges.

Conversely, let \(Q\) be any gadget matching, and let \(F\) be its
external-edge subgraph on the original vertices incident to at least
one such edge; isolated original vertices are excluded from \(V(F)\).
If \(t_v\) external
ports are occupied at \(v\), the internal matching has at most
\(d_v-\max\{1,t_v\}\) edges. Therefore
\[
        |Q|\le A+|V(F)|-|F|.
 \tag{2}
\]
Each tree component of \(F\), all of which have an edge, contributes one to
\(|V(F)|-|F|\); every other component contributes at most zero.
One edge from each tree component is a matching, of cardinality
at least \(|Q|-A\). It is found by ordinary component traversal.
Thus
\[
                    \nu(J)=A+\nu(G),
 \tag{3}
\]
and **every** maximum gadget matching decodes to an original maximum
matching. Its internal form need not be canonical. Odd \(N\) is
permitted.

## 3. What a current injection represents

Bins are disjoint factor-critical odd blocks of size \(2w_d-1\).
Rows are singleton physical vertices, each assigned injectively
along a real incidence to a bin. The rest consists of explicitly
matched pairs and unmatched blockers. For an injection \(\mu\),
the represented matching has cardinality
\[
       \sum_d(w_d-1)+|\mathcal A|+|U_{\rm paired}|/2.
 \tag{4}
\]
Every assigned bin exposes its assignment contact and matches its
row there. Every free bin exposes one unmatched physical vertex.

Equation (4) is independent of which valid injection is used.
Consequently changing a settled canonical injection may change many
physical matching edges while preserving one exactly specified
matching and its cardinality. This fact does not permit overwriting
creation-time contraction witnesses.

An inclusion-minimal tight set containing a physical bin/bin edge
contracts to a factor-critical block. The Hall proof also gives a
constructive materialization procedure with at most two local
bipartite augmentations per contraction record. Summed over its
record tree, materialization is linear in its physical volume up
to logarithmic indexing. See
[factor-critical contractions](factor_critical_contractions.md).
An arbitrary tight superset would not suffice for the swallowed-row
exposure argument.

## 4. Actual ledgers, persistence, and transaction order

For each level \(j\), the literal source invariant is
\[
 \sum_{e\ni r}x^j_e=L,\qquad y^j_d=L-\operatorname{load}^j(d),
 \qquad p^j_d\ge0,\qquad y^j_d+p^j_d\ge c_jw_d.
 \tag{5}
\]
The top also has positive incidence and slack coordinates. Lower
levels are integral; the settled bottom has floor one and zero debt.
No source inequality in (5) compares individual coordinates of
two different integral levels.

The persistent carrier stores the **actual** integral allocation.
Each transportation cycle pivot preserves all row sums and column
loads, hence every \(y,p\) and (5). It does not normalize a private
shadow while leaving a separate official vector unchanged.

For a sparse batch, read all required old values from its prescribed
version and coalesce writes before pivoting. Cut dead or retargeted
carrier incidences; retain unaffected zero carrier edges. Each new
positive off-forest edge creates one fundamental transportation cycle.
Push in the direction that increases that new edge, cut one zero
minimizer, and insert the new edge. All other zero edges may remain.
This gives constant topology recourse per batch entry even if many
path values simultaneously become zero.

The persistence construction uses a deterministic **worst-case**
dynamic forest, simulated by a persistent address-to-word dictionary.
It does not branch an amortized splay potential. The primary top-tree
interface is [Alstrup et al., Theorem 1 and Section 6.2](https://arxiv.org/html/cs/0310065v2):
logarithmically many cluster changes per operation, with the
unbounded-degree reduction supplied by its topology-tree
implementation. Two orientation-sensitive minima and two lazy tags
implement the signed transportation path operation. Internal
degree-reduction connectors are excluded from allocation minima.

The following old-to-final discipline is essential.

1. Freeze the pre-event bottom assignment oracle. Record expansion,
   contraction, pair exchange and deletion changes in one sparse
   forward/inverse overlay.
2. Save captive-row physical assignments before contracting them.
   Reusing a largest live bin ID does not overwrite its immutable
   old child record or historical endpoint tables.
3. Every assigned-row deletion in the event, its peel, and all
   preserving-ledger edits uses that same oracle plus overlay.
4. Freeze a reset parent through every threshold, lock, capacity
   query and final flow/cut recovery. Apply the complete final
   exchange batch and all deleted-row load releases to a child
   before its normalization.
5. Publish the new bottom canonical injection only after every
   ledger transaction is settled.

The physical matching remains implicit between actual erasures and
phase boundaries. Expansion needs only explicit paired-remainder
mates; contraction needs local captive assignments; deletion
materializes only charged erased volume. There is no required
global physical-mate rewrite when a carrier root changes.

## 5. Bottom surplus and local pair work

For bins \(X\), let \(A(X)\) be the rows all of whose neighbors lie
in \(X\), and let \(h(X)=|X|-|A(X)|\). Equation (5) at the bottom
implies
\[
                  Lh(X)\ge y(X)\ge w(X)>0.
 \tag{6}
\]
Thus \(h(X)\ge1\), every bin has weight at most \(L\), and every
tight set has weight at most \(L\).

Root an acyclic carrier at a bin. A carrier row has at least two
positive incidences. Keep both incidences of degree two; for degree
three keep its two children and omit its parent incidence. The
selected row forest has one row-labelled edge per row. Each component
has at most one internal row exporting allocation, and that export
is less than \(L\). Summing column capacities gives component
weight less than \(2L\), including when some carrier edges are zero.

The deterministic split-network reduction to
[Chechik et al., Lemma 3.5](https://arxiv.org/pdf/1705.10709)
finds an inclusion-minimal tight witness in output-sensitive work,
or certifies joint freeability in \(O(L\operatorname{polylog}N)\)
work. It uses outgoing adjacency and the assigned row's three
incidences, never a heavy bin's incoming adjacency.

On a freeable pair, local pruning and descending-level exchanges
touch at most two original selected trees. Their \(O(L)\) physical
volume pays for the explicit assignment overlay used by the
immediate gain. No old pruning certificate is reused after mutation.
These interfaces are proved in
[local tight discovery](deterministic_local_tight_discovery.md) and
[the balanced pair oracle](balanced_forest_pair_oracle.md).

## 6. The arbitrary-optimum-gap implication

Start a phase with matching size \(q_0\), target
\(1\le K\le\lfloor N/2\rfloor-q_0\), and
\[
 C=s+1,\quad L=\lceil10000CN/K\rceil,\quad
 g_*=\max\{1,\lfloor K/(100C)\rfloor\}.
\]
Impossible larger targets return LOW before initialization.

Suppose \(\nu(J)\ge q_0+K\). After \(i<g_*\) gains, comparison
with a matching of that size gives at least \(K-i\)
vertex-disjoint augmenting paths for the **current represented**
matching. The top debt budget leaves at most \(2C(g_*-1)\)
blockers, so discarding paths meeting blockers leaves at least
\(K/2\) paths.

At a settled state without a distinct-bin edge, orient each remaining
path from an unmatched endpoint. It starts at a free bin's exposed
base. Its first exit is nonmatching. If that exit meets a row,
the next matching edge is the row's assigned incidence and enters
the next bin at its unique base. The crossing matching edge is
now already used, so a simple path can leave that bin only by a
nonmatching edge. Before encountering the paired remainder, every
subsequent bin entry is therefore through its unique base.

Such a prefix cannot terminate in an assigned bin or enter a new
free bin through an assigned row. It must reach a remainder contact.
Vertex-disjoint physical paths cannot use the same unique bin base;
their prefixes are disjoint in bins and rows. Reassign each prefix
row to the preceding bin. The simultaneous injection frees at least
\(r_0\ge K/2\) distinct remainder-contact bins.

Scale that conceptual injection by \(L\). The top column capacities
are \(L+p_d-Cw_d\), nonnegative by the existing feasible top state.
Clipping removes at most \(CN\) total mass. Feasible completion
exists because the actual top allocation fills every row under
those capacities. Simple residual source-to-sink augmentations
never decrease a column's sink flow. Thus the initially empty
contact columns receive at most the removed \(CN\) mass. The
alternative slack satisfies
\[
                       s'(Z)\ge Lr_0-2CN.
 \tag{7}
\]
This is an existence proof for a direction, not an executed max-flow
subroutine.

When no expansion is eligible, every contact slack is at most \(5C\).
The alternative-minus-current vector is a circulation in the top
graph: allocation arcs and slack arcs both enter each bin, the latter
from their common auxiliary source. Every negative logarithmic
directional contribution is at least \(-1\), because the alternative
coordinates are nonnegative. At most \(4N\) such terms occur.
The positive sum is at least
\[
              \frac{Lr_0-2CN}{5C}-N>12N.
 \tag{8}
\]
Its signed-to-absolute derivative ratio exceeds one half. Therefore
(1) forbids LOW. Bounded objective range and positive priced-step
progress also forbid endless pricing.

The perfect-matching assumption in the original source is used
only to obtain the comparison paths. It is replaced here by
\(\nu(J)\ge q_0+K\). Odd order, disconnected components and many
permanently unmatched vertices do not affect (6)--(8).

## 7. Exact recovery has no uncharged feasibility solver

For an exactly conserved rational flow with integral demands and
integral arc bounds, total bound violation below one can be removed
constructively. Restrict each coordinate to its floor/ceiling
interval. On this box the original violation is an affine function
with integer constant and coefficients in \(\{-1,0,1\}\). Fundamental
cycle rounding in a nonincreasing-cost direction preserves demands
and produces an integral vector. The remaining fractional support
cannot be a nonempty forest, by its leaf divergence. Integral total
violation below one must be zero.

The implementation freezes each coordinate once and uses
\(O(m\log(m+2))\) charged scalar/dynamic-tree work. It masks all
simultaneous path minimizers before cutting them. It requires exact
conservation and a common dyadic denominator; small constraint
violation alone is not a substitute.

For local threshold recovery, success at \(b\) rounds to a true
flow of value \(b\). A valid failure at \(v+1\), when the optimistic
integer optimum is \(v\), has return value \(z>16v-8\): otherwise
the return derivative alone defeats the at most \(2000(P+1)\)
negative ordinary contributions and violates (1). Removing sink
locks, dividing by 16 and rounding gives an optimistic maximum
flow of value \(v\).

The lock comparator is proof-only. Its existence follows because
positive lower bounds occur only on sink-entering arcs; simple
augmenting paths never use their reversals. No algorithmic maximum
flow is called to find that comparator.

An optimistic residual minimum cut has no unexpanded boundary,
whose sink capacity would exceed \(v\). Its outgoing full arcs
are therefore represented, so it is the same capacity-\(v\) cut
in the full exchange network. Unioning the true-success and
optimistic-failure regions recovers the complete full residual
peel: no residual arc can leave this full minimum-cut side.
All residual searches omit the numerical return arc.

These are the explicit rounding and cut arguments in
[near-feasible exact recovery](near_feasible_rounding_and_exact_projection.md).
The older exact-flow import is not silently used by the current
binary-ledger composition, including at level one.

## 8. Uniform outer and recursive accounting

Use \(a=s\), floors \(c_j=s+1-j\), and periods
\(b_j=2^{s-j}\). Preserving deletion has debt change at most
\(Lh(R)-c_jw(R)\); a failed projection to floor \(c\) has
\(Lh(R)<cw(R)\). Every preserved coarser floor therefore pays
at least \(w(R)\) debt. This proves the erased-volume and
blocker bounds without coordinatewise cross-level assumptions.

The explicit structural budget is \(O(sS)\). For a reset at \(j>1\)
the unreset parent debt obeys
\[
 P\le(s+3)b_{j-1}.
 \tag{9}
\]
Large \(L\)-tick gain jumps either satisfy this same coarser-interval
bound or select a coarser reset. The sum of all higher-reset
\((P+2)\)-volumes is \(O(s^3S)\), and there are \(O(s)\)
global resets per phase. Applying a structural batch to \(s\)
levels is an additive factor, not recursive numerical composition.

The direct master priced client costs
\[
             O(MD+QD+D^2J)\operatorname{poly}(s),
 \tag{10}
\]
where \(Q\) excludes internal refreshes. Objective progress bounds
local accepted steps by \((P+1)D^2\operatorname{poly}(s)\).
Consequently a local or all-expanded recovery costs actual volume
times \(D^4\operatorname{poly}(s)\). Complete phases and the
gap driver cost \(SD^4\operatorname{poly}(s)\).

This uses direct master caps, not a fixed-\(a\) theorem evaluated
at a growing \(a\). In particular the old nominal constraint
\(R+B\le S^{1+2/a}\) and rounding by \(2a^2\) are removed.
Current numerical instances have actual nominal size at most
\(S^2\), fixed \(O(s)\)-bit root prices, and separately charged
internal word lengths.

For a recursive backend with initial child-update credit \(mP/k\),
that credit may occur late and costs child UPDATE time. The valid
coupled recurrence includes
\[
 \begin{aligned}
 J_d&\le W+P(G_{d-1}+1)+(P/k)(J_{d-1}+T_{d-1}),\\
 T_d&\le O(kW+kP(G_{d-1}+1))+O(P)(J_{d-1}+T_{d-1}).
 \end{aligned}
 \tag{11}
\]
Setting \(\mathcal H_d=J_d+T_d/k\) gives
\(\mathcal H_d\le O(W+P(G_{d-1}+1))+O(P)\mathcal H_{d-1}\).
Thus the initial credit is not falsely equated with child
initialization, and there is no unaccounted \(k\) factor per
recursive level.

All these costs apply to guarded prefixes plus the first attempted
batch. Loose polynomial history caps first bound positivity debt
and pad violation; the sharper locality/objective counts then show
that favorable subpolynomial-backend branches do not reach those
caps. This order avoids using completed fast running time to
justify its own precision prerequisites.

## 9. Driver, finite program, and remaining proof boundary

Maintain an integer upper bound \(U_{\rm gain}\ge\nu(J)-|Q|\).
For \(U_{\rm gain}>0\), set \(K=\lceil U_{\rm gain}/2\rceil\).
Success subtracts its gain count. LOW after \(i\) gains replaces
the bound by \(K-1-i\), using integrality and the implication
proved in Section 6. There are \(O(s^2)\) phases. At zero upper
bound, materialization and (2)--(3) return an original optimum.

For finite exceptional sizes, interleave fixed computable backend
constant tuples and a classical deterministic fallback. Charge
every instruction, allocation, multiword operation and verifier
within its worker. A fixed favorable tuple has constant share.
The fallback bounds actual memory/address sizes and guarantees
termination. Each proposed matching is validated and subjected
to one deterministic augmenting-path search before acceptance.
All workers and verifiers use the shared compact exact-preserving
graph, or the trusted cover kernel; only the winner's original
edge IDs are translated once.

Acceptance proves output correctness. The improved time still
requires the complete favorable backend hypothesis of Section 1
and its exact lifetime/initial-credit implementation. The
matching-side argument does not replace it with perfectness,
random initialization, uncharged integral feasibility, or the
verifier. Conversely, none of those four assumptions is needed
by the displayed reduction, carrier, gap, recovery, or uniform
outer implications.

The current conclusion remains a research proof assembly. Its
most demanding algorithmic boundary is the supplied dynamic raw
backend with complete occurrence and retirement histories; an
error there would invalidate the fast-time bound even though the
independent verified fallback would still return a maximum matching.
