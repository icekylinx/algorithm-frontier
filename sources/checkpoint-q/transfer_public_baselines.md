# Public baselines and candidate transfers

Research audit dated 25 October 2026. All bounds below distinguish published
results from candidate consequences of the current raw-cycle construction.
Write

\[
U=\log(m+2),\qquad h=\log\log(m+4),\qquad
E(m)=\exp O(U^{4/5}h^{1/5}).
\]

The current matching checkpoint supplies a research-proof candidate for a
deterministic raw minimum-ratio-cycle backend whose time, inverse quality,
piece count, and flat occurrence multiplicity all fit a fixed power of
\(E\). It does not automatically supply every optimization client below.

## 1. Ranked transfer candidates

The audit now distinguishes a paper's printed specialization from a
stronger consequence obtainable by composing or reparameterizing its
public ingredients. In particular, the static-flow comparison changed
during this research round; it must not be reported as a unique new
four-fifths consequence of our primal router.

| Priority | Problem | Printed public bound | Stronger public-framework comparison | Current candidate and boundary |
|---|---|---|---|---|
| 1 | Incremental directed \((1+\varepsilon)\)-SSSP, explicit all-target estimates | Liu25: exponent \(335/336\) in its Section 4 final remark | Composing the public \(20/21\) raw engine with Liu25's original detector gives exponent \(41/42\), subject to the usual raw-interface check | The new frozen-barrier detector proposes exponent \(4/5\) with the current raw backend, for constant or inverse-polylogarithmic accuracy. The detector and outer proof have independent audits; the additional active-tree-segment construction gives simple-path reporting in \(O((k+1)\operatorname{polylog}N)\), with \(k\) the final path length. |
| 1 | Incremental directed thresholded min-cost flow | KMGS26 Theorem 1.4: \(m\exp O(U^{20/21}\log U)\) | No stronger unrestricted public incremental bound identified in this audit | Candidate \(mE(m)^{O(1)}\), through the separately audited general incremental flow client. This is threshold crossing, not maintenance of every exact optimum value. |
| 2 | Exact static directed min-cost flow, polynomial integral data | BCK+24: deterministic \(m\exp O(U^{5/6}\log U)\) | This round derives a public dual tree-cut reparameterization giving \(m\exp O(U^{4/5}h^{1/5})\), using the named CGLNPS/PS/FO24 decomposition wrapper audited in the accompanying notes | The new primal client also targets \(mE(m)^{O(1)}\). It should be described as an independent route with useful interfaces, not as uniquely surpassing all public-framework consequences. |
| 3 | Incremental directed cycle detection | CKLMP24 Theorem 1.7: exponent \(167/168\) | KMGS26's threshold flow already gives \(20/21\) directly | Candidate \(mE(m)^{O(1)}\) after the incremental threshold-flow proof closes; unit capacities, costs \(-1\), and threshold \(-1\). |
| 2 | Incremental SCC maintenance | CKLMP24 Theorem 1.8: exponent \(167/168\) | Composing the later raw engine with its white-box contraction client gives the relevant \(20/21\) comparison; this does not follow from a threshold-flow headline alone | `log_barrier_incremental_scc.md` gives a new simplified conditional client at \((n+m)E^{O(1)}\): one-sided logarithmic barriers, exact high-flow contraction, paid endpoint retargeting, and explicit component labels. The public high-flow contraction principle is credited to CKLMP24. |
| open interface | Incremental topological ordering | SCC and cycle-detection headlines do not supply an order; the public source explicitly separates the problems | No unrestricted almost-linear ordering theorem was identified in the current primary-source audit | LOW gives an existential ordering potential. `topological_order_transpose_interface_gap.md` isolates the unproved dynamic transpose interface; no ordering theorem is claimed. |
| separate public retuning | Decremental SCC / decremental thresholded flow | BCK+24: deterministic exponent \(5/6\) | The same audited public dual reparameterization gives the derived \(4/5\) comparison | This is a different, dual min-ratio-cut interface. Credit the public framework and the quantitative retuning; do not attribute it to an automatic primal incremental transfer. |
| separate recent public result | Decremental directed all-target distance estimates | Li26, arXiv:2610.07468v1, Theorem 1.1: almost-linear total time; Proposition 2.1 uses the public \(5/6\) cut engine | The audited public dual retuning should give the explicit \(4/5\) overhead for fixed accuracy and polynomial weights; the reduction has no recursive loss amplification | This October 2026 paper already supplies the decremental numerical SSSP result. Liu25's earlier open-problem remark is therefore not a current novelty baseline. Fast path reporting is excluded by Li26. |
| new audited transfer | Decremental undirected strong SSSP forest; exact deterministic Gomory--Hu tree | KMG24 strong forest: exponent \(83/84\); AKL+25 already gives deterministic almost-linear exact Gomory--Hu trees | Joint provider reconstruction and direct node inventory in the existing public Algorithm 5 give \(\exp O(U^{8/9}h^{1/9})\). This supersedes the restricted \(62/63\), \(26/27\), and \(10/11\) comparisons; it is derived here, not a printed theorem or claimed global optimum. | Uncontracted compressed cores and colored full-forest pools give \(\exp O(U^{6/7}h^{1/7})\), improving the previous \(7/8\) research bound. The accepted implementation has no recursive degree resets. Fixed canonical nodes, current-edge embeddings, all unused nodes, historical cover overlap, and explicit recourse have root and two independent audits. The separately checked GH adapter still pays all degree, MWU, skeleton, guide-family and recursion factors. |
| new time--stretch point | Fully dynamic undirected numerical APSP | KMG24 Theorem 4.1: stretch \(\exp O(U^{6/7}h)\), worst-case update factor \(\exp O(U^{20/21}h)\) | Joint reconstruction of the public static provider and repair gives amortized \(\exp O(U^{6/7}h^{1/7})\) overhead at stretch \(\exp O(U^{5/7}h^{2/7})\). This supersedes the earlier restricted \(59/63\) composite. HLS24 and KMZ25 supply different tradeoffs; global optimization of all public constructions is not claimed. | At that same \(5/7\) stretch scale, the research construction gives \(\exp O(U^{23/28}h^{5/28})\) overhead. The earlier \(11/14\) and \(3/4\) points also hold. Actual-sized positive port trees handle arbitrary degree; numerical queries are polylogarithmic. These are amortized APSP bounds, not exact matching exponents or worst-case update guarantees. |

**Checkpoint H additions.** The independent-transversal current-blocker
certificate preserves Graf--Haxell's full total-domination and constellation
alternative with uniform time
P(q+1)^{O(epsilon^{-1}log(2+r/epsilon))} times the bit factor.
The same adjacency implementation gives the named public layer comparator
P(q+1)^{O((r/epsilon)log(2+r/epsilon))}. Both may use the separately
derived public P exp O(q) fallback, obtained by counting compositions
of positive blocker counts in the elementary source procedure. Because
r<=q+1 may always be used, the new arbitrary-partition specialization
is quasipolynomial in q for fixed positive slack. This is a full
certificate task; the failure alternative can coexist with an IT.
Harris's deterministic polynomial degree/block-size theorem remains
stronger on its different promised domain. See
**independent_transversal_public_uniform_baseline_audit.md** and
**independent_transversal_elementary_exponential_fallback.md**.

A late primary-source check also adds Krampl's July 2026 deterministic
weighted dynamic-spanner thesis. Its displayed worst-case update
formulas have powers of n strictly above one; its small-stretch and
weighted guarantees are different from the subpolynomial amortized
checkpoint objectives. The exact comparison and source boundary are
**dynamic_spanner_krampl_2026_baseline_audit.md**. The thesis is not
excluded on publication-format grounds, and no all-parameter
domination claim is made.

**Checkpoint G additions.** The direct tracked-terminal flat-forest
spanner has stretch and n-based density exp O(U^(4/5)h^(1/5)), with
total work and ordinary recourse (n+m_0+I+D) times that overhead.
Its direct public-provider comparator uses the same observer and an
explicit elementary zero-link extension of the public Algorithm 5
full-copy lift; it does not claim that a numerical oracle alone supplies
flat paths. At common logarithmic stretch U^(5/7)h^(2/7), the derived
public work/density exponent is 6/7 and the research exponent is 23/28.
The focused interface audit is
**tracked_terminal_spanner_public_flat_comparator_audit.md**. This
comparison is a named reconstruction, not a global optimality claim.

The weak-Haxell reanalysis has uniform exponent
O((r/epsilon)log(2+r/epsilon)), improving the rank-squared exponent
obtained by a length-aware count of the checked public formulas.
Annamalai already supplies the qualitative algorithm and certifying
alternative; Graf--Haxell also covers the same promise through its
constellation certificate. The new current-blocker lemma, both counts,
and precise attribution are in **weak_haxell_current_blocker_growth.md**
and **weak_haxell_public_parameter_comparison.md**, with root and
independent audits. Neither addition changes the exact general-matching
exponent or claims an optimized frontier for all public algorithms.

**Checkpoint F additions.** The explicit full-horizon dynamic spanner
in **fully_dynamic_spanner_five_sixths.md** has stretch and current
size overhead exp O(U^(5/6) h^(1/6)), total work
(n+m_0+I+D) exp O(U^(5/6) h^(1/6)), and total output recourse
(n+D) exp O(U^(5/6) h^(1/6)). It applies to arbitrary-degree
undirected graphs, including polynomially dense inputs; its update
work is amortized. The same public KMZ batching framework with the
jointly retuned public APSP core gives the matched-final-output
time overhead exp O(U^(31/36) h^(5/36)). Its balanced time/output
point is six-sevenths. These are derived-public comparisons, not
printed theorems or global optimality claims. Both public and new
cores have legitimate clipped-path implementations. The trivial
H=G construction wins whenever the live input itself fits the target
size. The full comparison and independent source audit are in
**dynamic_spanner_public_baseline_audit.md** and the two completed
full-horizon audit notes.

The source audit also establishes a **public-framework** deterministic
worst-case exact dynamic MSF envelope exp O(U^(2/3) h^(1/3)). Its
operative proofs are **dynamic_msf_formal_pruning_substitution_audit.md**
and **dynamic_msf_public_baseline_root_audit.md**, using the actual
weighted NSW certificate and explicit worst-case batch reduction.
It is not an exclusive new application of the research router. The
informal original-MSF-plus-published-edges sketch was rejected, and
the newer tagged-triangle alternative is not needed for this baseline.
Classical polynomial-logarithmic amortized MSF is a separate stronger
guarantee in that different update model.

The ranking concerns research routes with the proof status and imports
specified in their individual notes. A subpolynomial-factor improvement is
a quantitative change, but it must not be described as the first
\(m^{1+o(1)}\) algorithm for these problems.

For the SSSP proposal, the precise current bound is
\[
(n+m)\exp O\!\left(U^{4/5}h^{1/5}
 +\sqrt{U\bigl(h+\log(1/\varepsilon)\bigr)}\right).
\]
See `frozen_barrier_distance_detector.md` and
`frozen_detector_incremental_sssp.md`. Simply replacing the raw engine
inside the unmodified public detector would instead give exponent
\(9/10\). The removal of the engine loss from cumulative reporting is
the new technical assertion.

### Additional checkpoint D comparison: explicit hypergraph matching

Bucić, He, Huang, and Saranurak, *Disjoint Paths in Expanders in
Deterministic Almost-Linear Time via Hypergraph Perfect Matching*,
SODA 2026, [Theorem 1.5 and Lemma 3.3](https://arxiv.org/html/2511.02214v1),
give the displayed explicit-volume bound

\[
 p\exp O\!\left(\frac{\log(p+4)}{\sqrt{\log\Delta}}\right)
\]

under the strong Haxell condition
\(\tau(E_S)\ge\Delta r^2|S|\) for every left set \(S\), with
\(\Delta\ge4\). The checkpoint D fixed-certificate algorithm uses
the same condition and gives

\[
 O(|A|+|B|)+p\exp O\!\left(
   \frac{\log(p+4)\log(2+\log\Delta)}{\log\Delta}\right).
\]

It also returns an explicit violation of that sufficient condition
if a growth test fails. This qualitative matching-or-violation
alternative already appears in Annamalai's earlier work; the
contribution here is the sharper time bound and its complete
fixed-certificate proof. For \(\Delta\ge p^\epsilon\), with fixed
\(\epsilon>0\), the new overhead is polynomial in \(\log p\).
The arbitrary-input certificate does not certify the absence of
a perfect matching. These are hypergraph promises, and do not
replace the unrestricted general-graph maximum-matching target.

**Public-algorithm reanalysis completed in this round.** The same
sharper rate also holds for the original BHHS Algorithms 1--3.
A layer has only constantly many adopted superpositions, since
each multiplies its size by \(1.1\) while its lifetime size ratio
is bounded by ten. Splitting the child sequence into these epochs
extends the weighted count. Historical certificates from actual
extension attempts establish the needed growth invariant. The
proof is **public_hypergraph_algorithm_weighted_reanalysis.md**,
independently checked in **public_haxell_weighted_reanalysis_audit.md**.
Thus this row is a quantitative strengthening of the public analysis
as well as a guarantee for the simpler new implementation. It is
not a speed separation from the optimized public explicit algorithm.

**Further checkpoint E refinement.** Write \(q=|A|\),
\(s=\log\Delta\), and
\(a=\min\{\log(2+s),\log(2+\log(r+2))\}\).
The rank-sensitive analysis in **rank_sensitive_layer_count.md**
bounds the number of layer builds by
\[
 O(\min\{\log(q+1),1+s/a\})
       \exp O(a\log(q+1)/s).
\]
This also extends to the public algorithm. Take the minimum with
the elementary linear-time regime \(q\le\Delta r\); after the
whole-set certificate check, \(\Delta^2r^3\ge|B_{\rm used}|\)
is another sufficient condition for that regime. In particular,
\(\Delta\ge\sqrt p\) is already linear-time. Rank one has the
stronger Hopcroft--Karp bound
\(O(p(1+\log(q+1)/\log\Delta))\), plus vertex-list reading.
These corrections prevent a favorable but elementary parameter
range from being reported as a new algorithmic breakthrough.

The same public paper already establishes qualitative almost-linear
edge-disjoint routing and spanning-expander packing. The new routing
notes quantify the separated APSP overhead, the destructive support
cost, and the stronger outer count. They do not claim the first
almost-linear algorithm for either problem.

## 2. Exact source locations

### BCK+24: the relevant static and decremental comparison

Jan van den Brand, Li Chen, Rasmus Kyng, Yang P. Liu, Simon Meierhans,
Maximilian Probst Gutenberg, and Sushant Sachdeva,
*Almost-Linear Time Algorithms for Decremental Graphs: Min-Cost Flow and
More via Duality*, FOCS 2024, arXiv:2407.10830v1.

Primary source: <https://arxiv.org/html/2407.10830v1>.

Section 1.2 states the static min-cost-flow consequence and Theorem 1.6
states decremental thresholded min-cost flow. Their randomized overhead is
\(\exp O(U^{3/4}\log U)\); their deterministic overhead is
\(\exp O(U^{5/6}\log U)\). Theorem 4.4 gives the deterministic dynamic
tree-cut sparsifier. Theorems 1.8 and Corollary 1.9 give deterministic
decremental SCCs and single-source reachability with the same \(5/6\)
overhead. The SCC statement does not provide efficient path-reporting
queries between vertices in an SCC; the paper expressly separates that
issue.

**Reparameterization discovered in this audit.** The printed \(5/6\)
specialization does not exhaust the public construction. The notes
`public_dual_reoptimization.md` and
`public_dual_uniform_wrapper_audit.md` keep
construction work separate from exported tree-edit count and output
quality. With \(t=(U/h)^{1/5}\), the proposed choices
\(p=L=t\) and \(s=t^3h\) give logarithmic overhead
\(O(U^{4/5}h^{1/5})\). The uniform parameter substitution is
reconstructed in the independent audit: CGLNPS's linear-quality
cut/witness construction feeds PS's fixed-power witness pruning in
FO24's existing refining, vertex-split, and self-loop wrapper. The
source numerical implementation remains an import, as made explicit
there. This is a derived public-framework specialization, not a newly
located printed headline theorem. It must be included in a fair
novelty comparison.

### KMGS26: the current primal incremental comparison

Rasmus Kyng, Simon Meierhans, Maximilian Probst Gutenberg, and Aurelio Sulser,
*A Simpler and Faster Min-Cost Flow Solver via Min-Ratio Cycles from
Distance Oracles*, arXiv:2609.23852v1, 20 September 2026.

Primary source: <https://arxiv.org/html/2609.23852v1>.

Theorem 1.4 gives total time \(m\chi\), where
\(\chi=\exp O(U^{20/21}\log U)\), for incremental thresholded directed
min-cost flow with polynomially bounded capacities and costs. A feasible
flow meeting the threshold can be returned in an additional \(m\chi\)
time. Section 5, especially Definition 5.1 and Theorems 5.2--5.3, exposes
the flow-maintenance and IPM interfaces.

This improves the primal/incremental route. The public dual static
route has a better printed exponent, and the further retuning above
is a separate comparison.

### CKLMP24: incremental clients and their exact boundaries

Li Chen, Rasmus Kyng, Yang P. Liu, Simon Meierhans, and Maximilian Probst
Gutenberg, *Almost-Linear Time Algorithms for Incremental Graphs: Cycle
Detection, SCCs, s-t Shortest Path, and Minimum-Cost Flow*, STOC 2024,
arXiv:2311.18295v1.

Primary source: <https://arxiv.org/html/2311.18295v1>.

Relevant locations are Definition 3.7 (flow-maintaining solver),
Theorems 3.10--3.11 (static and incremental optimization clients),
Claim 8.11 (operation counts), and Section 8.3 (SCCs).

Its exact incremental problem is a fixed-threshold crossing problem. It
must not be renamed exact dynamic maintenance of the entire optimum.
Theorem 1.6 maintains an approximation for positive costs by running
geometrically spaced thresholds; its inverse-accuracy dependence is
linear, up to the displayed subpolynomial overhead. The all-SCC client
requires a white-box argument; the existence of a black-box threshold
solver alone does not prove its running time.

### Liu25 / STOC26: all-target incremental SSSP

Yang P. Liu, *Incremental Shortest Paths in Almost Linear Time via a
Modified Interior Point Method*, arXiv:2506.19207v1, 24 June 2025;
STOC 2026.

Primary source: <https://arxiv.org/html/2506.19207v1>.

Theorem 1 maintains explicit \((1+\varepsilon)\)-approximate distances
from one fixed source in incremental directed graphs with integral
lengths in \([1,W]\), and supports reporting a path in time proportional
to its output length. The headline theorem has
\(m^{1+o(1)}\log W\) total time for
\(\varepsilon\geq\exp(-U^{0.99})\). The final remark of Section 4
gives the more explicit exponent \(335/336\) when
\(\varepsilon\geq\exp(-O(U^{167/168}))\).

Theorem 2 is the important reusable interface: a detector for distance
decreases has a small *cumulative* set of reported vertices, not merely
a small simultaneous set. The proof uses a modified barrier with power
\(p=\Theta(\log m)\). Section 4 turns that detector into SSSP.

The arXiv abstract/history page checked in this round lists only v1.
The author's research page and the STOC 2026 proceedings identify the
same work; no more recent unrestricted deterministic incremental SSSP
theorem with a better explicit exponent was identified in the current
primary-source search. The public \(20/21\) raw engine changes the
composable comparison to \(41/42\), because the original outer balance
is \(\sqrt{U\log\kappa}\) and \(\log\kappa=O(U^{20/21}\log U)\).

Primary confirmation pages:
<https://arxiv.org/abs/2506.19207>,
<https://yangpliu.github.io/research.html>, and
<https://acm-stoc.org/stoc2026/toc.html>.

## 3. Public developments checked that do not remove these targets

**Recent decremental SSSP correction.** Hanqing Li,
*Almost-Linear Decremental Single-Source Distance Estimates in Directed
Graphs via Cut Balance*, arXiv:2610.07468v1, 5 October 2026, Theorem 1.1,
already gives deterministic almost-linear decremental all-target
numerical estimates, with exact unreachability detection, positive
integer edge weights, deletions, and weight increases. It does not
give fast path reporting. Its Proposition 2.1 imports FO24's dynamic
minimum-ratio-cut interface; Section 5 pays a fixed power of the cut
quality per step. Consequently the public dual reparameterization
above is also the relevant candidate quantitative comparison for this
recent reduction. This does not remove the incremental frozen-barrier
target: the paper explicitly separates its decremental cut method
from Liu25's incremental primal method.
Primary source: <https://arxiv.org/html/2610.07468v1>.
The current arXiv history lists only v1.

The 2026 paper *A Practical Combinatorial Interior Point Method for
Minimum-Cost Flow* (arXiv:2610.18328) studies an implementation and
empirical scaling. Its abstract does not claim a smaller worst-case
subpolynomial exponent.

The 2026 paper *Incremental Strongly Connected Components with Predictions*
(arXiv:2604.26062; SWAT 2026) uses a predicted edge-arrival sequence and
has prediction-error-dependent time. Its Section 1 comparison still
quotes the \(167/168\) worst-case IPM SCC result. Its stronger favorable
prediction bounds are not worst-case bounds without such predictions.

Chang--Huang--Su, *Deterministic Expander Routing: Faster and More
Versatile* (arXiv:2405.03908v1, PODC 2024), already supplies deterministic
distributed preprocessing/query tradeoffs of the form
\(n^{O(\epsilon)}+\log^{O(1/\epsilon)}n\) preprocessing and
\(\log^{O(1/\epsilon)}n\) query rounds. The current sequential router
must therefore be credited for its fully charged sequential construction
and its downstream use; its superficial tradeoff expression is not by
itself a new public routing bound.

**Strong forest and Gomory--Hu comparison.** KMG,
<https://arxiv.org/pdf/2311.06402>, Theorems 4.1 and 4.9 give fixed
base envelopes; Theorems 5.3, 5.12, 5.14 and Claims 5.15--5.17 expose
the outer free parameters. The note
`public_strong_forest_retuning_baseline.md` derives the historical
\(62/63\) comparison using those parameters alone. Joint provider
retuning and the direct vertex inventory in
`public_forest_direct_vertex_inventory.md` now strengthen the
public comparison to \(8/9\). The research \(6/7\) construction is
compared with that stronger derived bound as well as the printed
\(83/84\). The deterministic GH framework is
<https://arxiv.org/html/2507.20354v1>.

The fixed-\(k\) guide-tree mincut import needed an additional check:
the two public contraction presentations do not directly share the
same aggregate-instance recurrence. The explicit repair in
`deterministic_fixed_k_tree_mincut_adapter.md` changes the leaf
maximizer to include the source arm and chooses one or two disjoint
same-\(k\) children accordingly. It has an independent correctness
and inventory audit in
`fixed_k_global_max_leaf_independent_audit.md`. Thus the quantified
GH composition cites that repaired adapter explicitly.

**Fully dynamic APSP tradeoffs.** The new note
`apsp_time_stretch_tradeoff.md` keeps maintenance work separate from
metric stretch. It also checks KMG Theorem 4.1, KMZ's ESA 2025 paper
and full version <https://arxiv.org/html/2408.11375v1>, HLS24's latest
v2 <https://arxiv.org/pdf/2402.18541>, and CZ23
<https://arxiv.org/pdf/2304.09321>. A public statement permitting
\(n^\epsilon\) time only for \(\epsilon\ge\log^{-c}n\), with
unspecified sufficiently small \(c\), does not authorize a numerical
substitution \(\epsilon=U^{-3/14}\). Likewise the new amortized
APSP points must not be described as an identical-interface improvement
of KMG's worst-case update guarantee.

The strongest current KMG-based comparison in this research is now
the joint reconstruction in **public_apsp_joint_retuning_audit.md**,
with logarithmic work \(O(U^{6/7}h^{1/7})\) and logarithmic stretch
\(O(U^{5/7}h^{2/7})\). Its independent audit checks actual local
parameter domains, loopless degree bands, weighted witness ports,
stage counts, selected recourse, and deamortized work budgets.
**same_stretch_apsp_comparison_and_root_audit.md** derives the research
\(23/28\) work point at precisely that stretch scale. Neither the
reconstructed public bound nor the research bound is a printed
headline theorem.

Two later-looking faster GH reductions do not supply current proved
runtime bounds: <https://arxiv.org/abs/2509.02520> and its deterministic
follow-up <https://arxiv.org/abs/2510.27330> were both withdrawn in v2
on 24 April 2026. Their official notices identify a runtime-analysis
gap; the second depends on the first. They must not be used as a
polylogarithmic reduction baseline without repairing that gap.

## 4. Source-interface corrections that a transfer must make explicit

Several literal source formulas should not be copied without reconciling
their conventions:

1. With a loss factor \(\rho\geq1\), an approximate ratio oracle returns
   a negative ratio at most \(r^*/\rho\). Failure to find a ratio at
   most \(-q\) can exclude \(r^*\leq-\rho q\), not
   \(r^*\leq-q/\rho\). The printed solver definitions in CKLMP24 and
   KMGS26 use the latter expression while later parameter choices use
   a large loss factor. The quantitative transfer should state one
   consistent convention and derive its threshold implication directly.
2. The KMGS26 flat-lift statement and surrounding explanation use a
   length direction that needs checking against its actual overestimate
   invariant. Our raw denominator must be computed from all traversals;
   cancellation in the projected circulation cannot pay for refreshes.
3. Liu25's solver definition normalizes by weighted \(\ell_1\) motion,
   whereas CKLMP24 normalizes by gradient decrease. The detection proof
   can instead be stated using an upper bound on raw weighted motion
   and a proportional lower bound on gradient progress. This adaptation
   is written in the frozen-detector note; its exact raw-interface
   import and independent audit remain explicit hypotheses.
4. The Section 4 runtime sentence in Liu25 writes
   \(\alpha=m^{1/B}\); the phase/shrink definition requires the small
   quantity \(\alpha=m^{-1/B}\). The displayed runtime balance makes
   the intended sign unambiguous.

These observations concern precise transfer interfaces. They are not a
claim that the published headline theorems are false.
