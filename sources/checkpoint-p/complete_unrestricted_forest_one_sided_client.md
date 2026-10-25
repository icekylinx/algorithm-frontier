# A complete unrestricted-receiver client on forest allocation graphs

**Research theorem, 25 October 2026. Root review and two independent mathematical audits completed.**

The reviews are **complete_unrestricted_forest_client_independent_audit.md**
and **complete_unrestricted_forest_client_third_audit.md**. The entire
ambient-support forest hypothesis remains essential.

On an allocation graph whose entire underlying ordinary support is a
forest, the one-sided numerical client can be made complete without
maintaining an old feasible distance potential. All receiving directions
are available. A constant-state dynamic-tree search finds a passing path
or certifies the absence of the strong feasible comparison used by the
matching phase.

This is a theorem about the numerical interface under a forest-support
hypothesis. A general degree-three matching allocation graph need not
satisfy that hypothesis, and an ordinary matching expansion can destroy it.
No improvement of the general-matching four-fifths exponent follows here.

The implementation extends
bidirected_potential_compatible_forest_matching_interface.md by dropping
the receiver-tightness restriction. Its DP, coordinate ownership, directional
lazy watcher, hysteretic registers, and finite-word steps are retained.
Only the old-D feasibility and old-D semantic screen are discarded.

## 1. Static input and numerical contract

There is a bipartite ordinary graph with rows R, bins B, and incidence
coordinates x_e>0. Its underlying undirected multigraph is a forest.
In particular, parallel physical incidences forming an undirected
two-cycle are not allowed by this hypothesis.

The exact equations are
\[
 \sum_{e\ni r}x_e=L_r,\qquad
 \sum_{e\ni d}x_e+s_d=b_d,\qquad s_d>0.                       \tag{1}
\]
All row totals, bin capacities, coordinates, and input parameters lie
on the declared common dyadic grid and in a polynomial guarded range.
Row totals are positive; an isolated zero-total row, if supplied,
is removed as a vacuous constraint. Thus each component queried for
a source offer contains a bin.
Let nu bound the number of live row/bin vertices, and let S bound the
word-scale parameters and admitted history length.

The objective is only
\[
                            \Phi=\sum_d\log s_d.             \tag{2}
\]
All receiving arcs row-to-bin have cost zero. Every donor arc
bin-to-row has its conservative cost
\[
 \bar c_e=\left\lceil H/(4\ell_e)\right\rceil,\qquad
                  \ell_e<x_e<2\ell_e.                       \tag{3}
\]
Registers are initialized and reset to ell=3x/4 and persist across
changes in traversal direction.

At a bin put
\[
 \sigma_d=\lfloor3H/(4s_d)\rfloor,\qquad
 \tau_d=\lceil5H/(4s_d)\rceil.                                \tag{4}
\]
Choose fixed polynomial H large enough for the rounding budget
H min_d(1/s_d)>=8(nu+2), throughout the declared range. One may also
impose the semantic rounding bounds of the earlier notes, although
the direct separation proof below does not need an old potential.

The operations return:

* a simple ordinary bin-to-bin path of true one-sided ratio
  greater than one quarter, represented by its endpoints;
* or LOW, certifying that no feasible comparison has one-sided
  ratio greater than one half.

The latter conclusion is about directions preserving (1).
It is not by itself a matching-optimality certificate at a state
where a structural matching action should be processed first.

## 2. Search all ordinary paths, without potential compatibility

On every physical forest incidence retain both directions:
the donor score is -bar c_e and the receiver score is zero.
Attach the two price leaves per bin, of scores +sigma_d and -tau_d.

The directed cluster DP of the preceding note now maximizes
\[
          \sigma_a-\tau_b-\bar L_F(a,b)                       \tag{5}
\]
over every ordered bin pair in one ordinary component. Here the
unique underlying path is always traversable, and bar L counts
its donors in the actual a-to-b direction.

There is no fixed D in the data structure. Every source bin can
start a path. A path need not follow any rooted implementation
orientation. Its physical incidence IDs are distinct.

The existing constant-size join formulas remain valid with both
directions finite at every ordinary base edge. Each cross term
joins disjoint child paths at their unique common vertex, so it
creates no repeated edge or vertex. Ordinary backtracking is not
part of the represented path.

All ordinary arc costs are nonnegative, and any nontrivial closed
ordinary walk contains a positive-cost donor. Removing a
backtrack cannot worsen a shortest-path offer. Thus the maximum
source offer used in this forest DP is also the unrestricted
source offer in the full directed ordinary graph; there are no
additional beneficial walks hidden by the simple-path convention.

The rounding inequalities of the previous interface give:

1. positive score in (5) implies true ratio greater than one quarter;
2. every ordinary path of true ratio greater than one half has
   positive score.

The search therefore supplies the promised path, or excludes
every ratio-above-one-half ordinary path in the ambient support.

## 3. Why path separation is a complete circulation certificate

Let h=(h_x,h_s) be any feasible difference between two vectors
satisfying (1), with the comparison vector nonnegative. Orient
a canonical allocation edge row-to-bin and a canonical slack
edge from an auxiliary vertex z to its bin. The difference h
has zero divergence at every row, bin and z.

Replace each nonzero coordinate by its sign-compatible directed
residual arc with magnitude |h|. These nonnegative arc values
form a circulation and decompose into simple directed cycles.
No decomposition cycle uses both directions of one coordinate:
the residual graph contains just the sign selected by h.

Charge a negative allocation change by 1/x_e, a positive allocation
change by zero, and either direction of a slack change by 1/s_d.
The signed gain is supported only on slack arcs. This decomposition
preserves total signed gain and total one-sided charge exactly.

An ordinary-only cycle has zero signed slack gain. A simple cycle
through z visits it once, and has the form
\[
                      z\to a\leadsto b\to z .
\]
Its ordinary part is a simple bin-to-bin path; in a forest it is
the unique underlying path. Its gain and charge are
\[
 G=\frac1{s_a}-\frac1{s_b},\qquad
 C=\frac1{s_a}+\frac1{s_b}
       +\sum_{\text{actual donors}}\frac1{x_e}.               \tag{6}
\]
A self-pair cannot supply a positive cycle. Nontrivial cycles
have positive charge. Consequently a comparison with G>C/2
would contain a cycle, hence a forest path, of ratio above one half.

An empty search excludes that possibility. This proves LOW directly,
without assuming a still-feasible old label vector or materializing
a new one.

For the genuine matching comparison, let P be positive normalized
slack mass, Q_s negative normalized slack mass, and Q_x negative
normalized allocation mass. Its guarantee
\[
                         P>12N,\quad Q_s\le N,\quad Q_x\le3N
\]
implies
\[
 \frac{G}{C}=\frac{P-Q_s}{P+Q_s+Q_x}
       >\frac{P-N}{P+4N}>\frac{11}{16}>\frac12.              \tag{7}
\]
Thus this numerical client cannot return LOW while the settled
matching comparison applies.

## 4. An optional fresh feasible potential at LOW

If an explicit or queryable dual potential is desired, define for
every ordinary vertex v
\[
 I(v)=\max_{a\text{ bin}}\{\sigma_a-\bar L_F(a,v)\}.           \tag{8}
\]
The source-to-boundary entry of an expose(v) query returns this
value and a witness in polynomial logarithmic time. The endpoint
price leaves ensure that mutable bin prices do not cause a
high-degree update.

Choose A>=max_a sigma_a and put D^*(v)=A-I(v). Ordinary costs are
nonnegative. Extending a source path across one arc and erasing
any resulting backtrack proves
\[
                 I(v)\ge I(u)-\operatorname{length}(u,v).
\]
Also I(d)>=sigma_d at every bin. Therefore D^* is feasible for
the complete current conservative threshold graph.

At LOW, I(d)<=tau_d for every bin, whence
\[
 \sum_d\left(s_d(A-D^*(d))/H-5/4\right)_+
       \le T_{\rm slack}/H .
\]
With the earlier choice of H this is at most N.

The potential can be left as the exact implicit query (8).
Materializing all entries costs nu polylog S once, or can be
done by a static two-pass tree DP. Such a materialization is not
silently performed after each numerical step. The direct LOW
certificate of Section 3 needs no materialization at all.

## 5. Path update, guards, and finite-word arithmetic

For a returned pair a,b, use
\[
 V_{\rm up}=1/s_a+1/s_b+4\bar L_F(a,b)/H,\qquad
                  1/512\le\eta V_{\rm up}\le1/256.           \tag{9}
\]
The fixed sufficiently fine primal grid contains such a step.
Only two slack reciprocals and one integer path sum are combined,
so the computation uses O(log S)-bit arithmetic.

Apply the transfer implicitly on the ordinary a-to-b path.
The directional watcher retains both donor and receiver buffers;
along the actual forward path their minima decrease by eta and
the backward-direction minima increase by eta. Registers are
reset at discovered crossings, and every resulting donor-price
change is sent to the unique physical DP edge, including price
decreases caused by receiving traversals.

Conservation, positivity and constant objective gain use only
(5), (6) and (9). They never used old-D tightness:
\[
                    \Delta\Phi\ge(1/8)\eta V_{\rm up}>0.
\]
The two endpoint slacks are stored exactly and update their price
leaves directly.

There is no numerical floor obstruction on a static positive input
when the guards are chosen below its guaranteed initial range.
Indeed, acceptance implies alpha_a>(5/3)alpha_b. The normalized
step keeps the global maximum reciprocal from increasing, so
the minimum slack never decreases.

For any donor on the accepted path,
\[
          \frac1{4x_e}\le\bar c_e/H<\frac3{4s_a},
          \qquad x_e>s_a/3 .
\]
After the small step its allocation remains above
(255/256)s_a/3. Thus a decreasing allocation is always bounded
below by a fixed fraction of the initial minimum slack. An
allocation below that scale cannot be a donor of an accepted path;
it can only stay fixed or increase.

Choose a declared allocation guard below
min(initial minimum allocation, initial minimum slack)/100,
and a slack guard below the initial minimum slack/100.
No numerical path hits those lower guards. Row totals and bin
capacities give polynomial upper bounds automatically. The
register and guard discovery mechanisms remain explicit; they
are not replaced by a free scan of a long path.

## 6. Total work on a static forest ledger

On a fixed polynomial-range ledger, the objective has width
O(|B| log S). Each accepted step gains an absolute constant,
so
\[
                            J=O(|B|\log S).                 \tag{10}
\]
The allocation log-variation argument remains valid without D.
Every step has O(1) total negative allocation log variation.
Telescoping sum log x bounds total positive variation by that
amount plus O(m log S).

Hysteretic registers require a constant amount of absolute log
variation between resets. Therefore
\[
                          R=O(J+m\log S).                   \tag{11}
\]
The two dynamic trees, all path updates, guard queries, endpoint
edits, and register notifications cost
\[
                       (m+\nu)\operatorname{polylog}S       \tag{12}
\]
in total, including initialization and a terminal LOW query.
Space is linear apart from ordinary dictionary overhead.
Here m<=nu-1 in each nontrivial forest component.

This is a complete static numerical procedure: it either produces
accepted positive steps or returns LOW, and the preceding argument
does not leave an unprocessed numerical guard failure as a third
permanent outcome.

## 7. Dynamic structural batches: exact conditional scope

The same implementation accepts an explicit structural transcript
provided the whole ambient ordinary support is a forest after
each settled batch. A batch may create or retire rows/bins,
cut or link incidences, retarget an incidence, and externally set
explicitly listed primal coordinates or bin slacks.

Before changing a selected incidence, materialize that coordinate
by a point query. Retargeting is a cut followed by a link.
A vertex retirement must enumerate and cut its incident edges;
it does not receive a free high-degree deletion. New bins receive
their two price leaves. Existing registers are reused when an
incidence keeps its value; births or explicit value settings can
reset them as charged external records.

Process all cuts before the links of the new settled forest.
Every intermediate link can then be checked by connectivity.
Equation (1), positivity and the declared polynomial range must
be supplied by the valid structural ledger operation. This note
does not invent a feasible external assignment.

Let A_T count explicit topological records, A_x external allocation
birth/death/set records, and A_s slack birth/death/set records.
The latter include all bins whose slack changes in a structural
batch. Their total possible downward objective change is
O((nu_0+A_s) log S); allocation births and settings contribute
O((m_0+A_x) log S) to the variation account. Thus
\[
 J=O((nu_0+A_s)\log S),\qquad
 R=O(J+(m_0+A_x)\log S),
\]
and total work is
\[
             (m_0+\nu_0+A_T+A_x+A_s)\operatorname{polylog}S. \tag{13}
\]

Exact endpoint slack caches are inexpensive here: only two change
per numerical path. Matching eligibility can therefore use the
actual cached threshold 4C with exact endpoint notifications.
A newly eligible structural action is handled before another
numerical path when the surrounding matching client requires it.

The forest hypothesis is not automatically preserved by all general
matching operations. For example, a degree-three expansion can join
a new row to its new child and to two old bins already connected
by an ordinary forest path. Those last two attachments close a
cycle. This operation is a legal possibility in a general allocation
graph and lies outside the present forest-support theorem.

Deletion of support edges preserves the class, and contraction of
a connected ordinary subtree preserves it. An arbitrary contraction
or retargeting must still be checked against the explicit settled
forest condition; no unstated structural invariant is assumed.

## 8. Relation to the general problem

The forest result shows that maintaining old feasible labels was
not necessary for fast local primal motion. It was needed by the
previous approach's global separation screen. On a full forest
support, direct path separation supplies that screen instead.

It also explains the scope of the non-tight-receiver example.
Opening all receiver directions on its entire ordinary forest
immediately exposes its missed path, without any potential update.

For a general degree-three allocation graph, the missing interface
is full-graph path discovery and separation at comparable cost.
Keeping only a spanning forest does not make Section 3 complete:
a strong comparison can use receiving incidences outside it.
A tree cover, cycle-basis exchange scheme, or other general-graph
representation must pay for those directions and their changing
prices. No such general-graph theorem is claimed here.

