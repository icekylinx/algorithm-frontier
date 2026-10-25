# A 5/6 quantitative composition for deterministic general matching

**Research theorem candidate, 24 October 2026.** This note composes
[deterministic threshold token routing](deterministic_token_routing_by_thresholds.md),
[sparse weighted path selection](deterministic_weighted_path_selection.md),
and the resulting
[static sparsifier with length-free ambient congestion](length_free_ambient_static_sparsifier.md)
with the existing dynamic, numerical, and matching constructions.
It gives the parameter balance and a single computable wrapper.
Its dependencies are the named primary-source algorithms and the
mathematical reconstructions cited below. It is not an externally
verified implementation or a claim that an optimality verifier proves
the fast running time.

The target is exact maximum-cardinality matching in arbitrary
undirected graphs. There is no perfect-matching promise, approximation,
bipartiteness assumption, or density restriction. This construction
does not use the Chang--Huang--Su distributed hierarchy. The separate
6/7 construction remains unchanged.

## 1. The static interface, including the normalized-route type

Let \(U\geq2\) be an integer master bound, and put
\(h=\lceil\log_2(U+4)\rceil\). Every actual graph, explicit route
list, and token inventory in a local call has at most \(2^{O(U)}\)
records. This is a bound, not permission to allocate a master-sized
graph. All initializations use actual input records.

The static parameters are integers \(q\geq2\), \(r\geq1\),
with \(q,r\leq U\) and \(qrh\leq U\). The separated source
construction supplies
\[
 \log_2\Gamma=O(qrh),\qquad
 \log_2F=O(U/q+U/r+r^2h+qrh).
 \tag{1}
\]
The first factor controls structural output; the second is
construction work. Constants are uniform in the growing parameters.

The input is a demand multigraph \(J\) with distinct physical edge
IDs, and annotated ambient paths \(\Pi(e)\) with the same endpoints.
Write \(L_0=\max\{1,\max_e|\Pi(e)|\}\), let \(C_0\) be their
ambient vertex-occurrence congestion, and let
\(\Delta_0=\Delta(J)\). Endpoints and repeated occurrences are
included in \(C_0\).

First erase closed subwalks from each individual nonloop image.
This produces a normalized table \(\Pi'\) of simple paths, with
\[
                     L(\Pi')\leq L_0,\qquad C(\Pi')\leq C_0.
 \tag{2}
\]
The static routine returns this table, a subgraph
\(\widetilde J\subseteq J\), and explicit routes
\(\widehat\Pi:J\to\widetilde J\), with
\[
 \begin{aligned}
 |E(\widetilde J)|&\leq |V(J)|\Gamma\operatorname{poly}(U),\\
 L(\widehat\Pi)&\leq\Gamma,\\
 L(\Pi'\circ\widehat\Pi)&\leq\Gamma L_0,\\
 C(\Pi'\circ\widehat\Pi)&\leq\Gamma(C_0+\Delta_0).
 \end{aligned}
 \tag{3}
\]
Its work, including the normalization and full explicit ambient
route lists, is
\[
 |E(J)|F^{O(1)}\Gamma^{O(1)}(L_0+1)\operatorname{poly}(U),
 \tag{4}
\]
plus actual vertex bookkeeping. In particular \(F\) enters none
of the structural bounds in (3).

The last line of (3) is about the returned normalized table
\(\Pi'\), not the unchanged original walks \(\Pi\). This distinction
is necessary: an input walk could repeat an ambient vertex
arbitrarily often. The distance application permits normalization
and explicitly uses the correction circulation
\(e-\text{current normalized route of }e\). No gradient-preserving
static theorem for the old image is asserted.
All erasure compares IMMEDIATE ambient vertex lifetime IDs.
Equal eventual parent or physical images do not identify native
endpoints. In particular a path between different aliases of one
root, or an edge with zero eventual physical image, cannot be
discarded on that basis.
The exact circulation decomposition, gradient calculation, and
raw-lift compatibility are proved in
[normalized_route_cycle_comparison.md](normalized_route_cycle_comparison.md).

The proof of this interface has two new steps. In a fixed expander,
edge-threshold deletions and the original-volume pruning bound route
all degree-proportional token demands in \(O(\log M)\) fresh oracle
generations. Each token path has length
\(\Lambda=2^{O(qrh)}\), while aggregate edge congestion is
\(D\,2^{O(qrh)}\). There is one oracle per round, rather than \(D\)
separately initialized copies. Next, the deterministic weighted
selection lemma chooses one path for each witness edge. Simplicity
of each individual \(\Pi'(e)\) bounds a single choice's load at an
ambient vertex by \(O(\Lambda\Delta_0)\), independently of \(L_0\).
That is the step that removes \(L_0\) from ambient congestion.
The separate static note proves the degree-band, weighted-witness,
and reverse-embedding composition, including fractional witness
weights and parallel IDs.

## 2. Source ranges and actual-size base cases

The source dependencies in (1) are the parameterized
Chuzhoy--Saranurak decremental expander paths and
Chuzhoy et al. cut-player/decomposition algorithms, as reconstructed
in
[separated_static_sparsifier_parameters.md](separated_static_sparsifier_parameters.md)
and
[parameterized_expander_path_and_degree_bands.md](parameterized_expander_path_and_degree_bands.md).
The threshold router uses their original-volume pruning guarantee,
including its whole-host extension at deletion-quota exhaustion.

In a decomposition call on \(m'\) records, clip \(r\) to
\[
          r'=\min\{r,\lfloor\log(m'+2)/c_0\rfloor\},
 \tag{5}
\]
with a constant-size base. This improves conductance and keeps
construction work inside (1). In a path-oracle call with
\(\log(m'+2)<c_1qrh\), use ordinary pruning and direct BFS;
the query factor is \(2^{O(qrh)}\), with no larger padded graph.
Otherwise the smallest terminal set has sufficient logarithmic
size to meet the cut-player cutoff and the pruning slack. These
are the literal small-instance adapters in the source
reconstruction.

An additional tiny static case can use a spanning forest of \(J\).
For \(v\) nonisolated demand vertices with \(v^2\leq\Gamma\), route
each edge along its tree path. After input normalization, each
individual input image visits any ambient vertex at most once.
Thus the composed ambient congestion is at most
\[
              |E(J)|v\leq v^2\Delta_0
                         \leq\Gamma(C_0+\Delta_0),
 \tag{6}
\]
and its length is at most \(vL_0\). The actual construction work
is \(O(|E(J)|v(L_0+1))\), within (4).
This argument requires the simple normalized table; applying the
old nonsimple walks would reintroduce a length factor.

Loop demands retain their current endpoint annotations and
permitted empty geometric routes. They are kept outside nonloop
expander hosts. A later native split may awaken such a demand,
which is a change of its retained lifetime, not a new synthetic
edge insertion. Unrelated private native roots are never
published as a large zero-star child graph.

At a recursive cycle-backend level, inputs with at most \(24k\)
active records use the direct small-graph ratio solver on their
actual records and declared word sizes. Resident child isolates
remain counted for size bounds; only private tombstone metadata
is excluded. Source periods start from current active records
and retain newly isolated native slots until that period ends,
as in the existing isolate adapter.

## 3. Rounded parameters

Define
\[
 t=\max\left\{2,\left\lfloor(U/h)^{1/6}\right\rfloor\right\},
 \qquad q=r=t,\qquad K=t^2,
 \tag{7}
\]
\[
                    x=\lceil U/t\rceil,\qquad k=2^x.
 \tag{8}
\]
Integer-root comparisons compute \(t\); no real-valued
parameter advice is used. The static path-hierarchy depth \(q\),
cut-player parameter \(r\), touched-set repair depth \(K\),
and recursive size reduction \(k\) have distinct roles.

For sufficiently large \(U\),
\[
 t^6h\leq U,\qquad
 t=\Theta((U/h)^{1/6}),\qquad
 x=\Theta(U^{5/6}h^{1/6}).
 \tag{9}
\]
The literal source guards \(q,r\leq U\), \(K\leq U\), and
\(qrh=t^2h\leq U\) follow. They are checked, rather than presumed,
on finite exceptional inputs.

For the private touched-set schedule use
\[
             \rho=2^{\lceil8U/K\rceil},
             \qquad N_{\rm sched}=\rho^K.
 \tag{10}
\]
The latter is a counter of \(O(U)\) bits. It is never an allocated
vertex universe. The old restriction \(K^7\leq\log m\), belonging
to a different worst-case spanner instantiation, is not imposed
on this elementary static-repair schedule.

### 3.1 Explicit internal caps from the same constant index

The threshold router needs a numerical path cap in its threshold,
not just asymptotic notation for \(\Lambda\). No extra noncomputable
constant is supplied to the program. From the same positive integer
\(c_C\) enumerated in Section 9, compute
\[
 \begin{split}
 c_\phi&=\max\{1,\lfloor c_C^{1/4}\rfloor\},\\
 c_\Lambda&=\max\{1,\lfloor c_C^{1/2}\rfloor\},\\
 c_\Gamma&=\max\{1,\lfloor c_C^{3/4}\rfloor\}.
 \end{split}
 \tag{10a}
\]
Integer comparisons compute all three roots. Declare the dyadic
conductance and path caps
\[
 \phi_*=2^{-c_\phi rh},\qquad
 \Lambda_*=2^{c_\Lambda qrh},\qquad
 \Gamma_*=2^{c_\Gamma qrh}.
 \tag{10b}
\]
Use \(\phi_*\) as the conservative host/witness conductance
parameter, and \(\Lambda_*\) in the threshold router. For its
fixed explicit pruning constant \(c_{\rm prune}\), the threshold
is the integer ceiling of
\[
                    8c_{\rm prune}D\Lambda_*/\phi_*.
 \tag{10c}
\]
If a returned path exceeds \(\Lambda_*\), suspend that branch;
do not truncate the path. Likewise the static structural and
prefix counts are checked against their declared caps.

For a sufficiently large fixed \(c_C\), \(\phi_*\) is no greater
than the decomposition and witness expansion guarantees.
The source path bound has logarithm \(O(c_\phi qrh)\), so
\(\Lambda_*\) eventually dominates it. The threshold routing
and weighted selection output factors have logarithm
\(O((c_\Lambda+c_\phi)qrh)\), which is dominated by
\(\log\Gamma_*\) for sufficiently large fixed \(c_C\).
Finally the fixed polynomial powers of \(\Gamma_*\), \(\rho\),
and \(U\) required by selected-degree feedback fit the port
cap (14), because \(c_\Gamma=o(c_C)\) as the constant index
grows. Explicit powers of \(\Gamma_*\) may be used in the
native repair thresholds.

All coefficients in this paragraph are fixed after one favorable
\(c_C\) is chosen. They do not grow with the input. Consequently
they alter only the fixed constants in (1) and (22)--(26).
The independent \(c_E\) is then chosen large enough for all
work and quality bounds. On finite exceptional inputs the
parameter/bit guards may suspend the branch. This cap separation
makes the two-constant portfolio executable without knowing an
asymptotic path-bound constant in advance.

## 4. Dynamic repair and the improved local recurrence

Use
[the amortized static-base construction](amortized_static_base_distance_sparsifier.md).
Every selected projected edge contributes only its central original
core-edge ID. Its prefix and suffix already lie in lower repair
layers. Selected IDs are deduplicated across layer owners before
degree feedback. The static running time \(F\) is local work;
it does not multiply selected size or recourse.

Let \(A=\operatorname{poly}(U)\) cover native translation, stable
core forests, length buckets, and ordinary indexing. The
selected-degree and encoded child-edit factor is
\[
 R=(A\rho\Gamma)^{O(1)},\qquad
                 \log R=O(U/K+\log\Gamma+\log U).
 \tag{11}
\]
Through \(z\) parent edits the child transcript has the safe prefix
bound \(O(mR/k+Rz)\). Its additive credit may be spent late and is
not confused with actual child initialization. The alternative
one-time fresh-base normalization proves a pure \(O(Rz)\)
post-initialization prefix, but the recurrence below allows the
more conservative credit.

In a touched-set projection, a new endpoint is an occurrence on
an old route or a current native endpoint. Consequently the
projected input degree is bounded by a constant times old route
congestion plus the native degree envelope. This includes empty
loop endpoints. The literal normalized-route and endpoint-count
proof is in
[normalized_projected_route_composition.md](normalized_projected_route_composition.md).
In particular it bounds both projected degree and preliminary
ambient congestion without a factor \(L_j\).
The native envelope is
\(k\operatorname{poly}(U)\) in the degree-three parent interface.
Together with (3), the repair recurrence is therefore
\[
 L_{j+1}\leq O(\Gamma)L_j,\qquad
 C_{j+1}\leq O(\Gamma)
                  \bigl(C_j+k\operatorname{poly}(U)\bigr).
 \tag{12}
\]
It gives length \(\Gamma^{O(K)}\) and congestion
\(k\operatorname{poly}(U)\Gamma^{O(K)}\).
There is no multiplication by \(L_j\) in the second recurrence.
Freezing a settled base and then running another \(K\) repair
layers changes only the constant in \(O(K)\).

All normalized current routes receive new owner and inverse-
occurrence records. Old records are retired with their old
physical IDs before replacement; an erased unused subwalk
belongs to no current record. The raw-cycle corrections use
the new route, not an obsolete gradient identity.
The existing coalesced transaction and pool-retirement proofs
are still required; normalization does not cancel their actual
signed or absolute motion counters.

The resulting local work envelope is
\[
 W=k^{O(1)}\rho^{O(1)}F^{O(1)}
                      \Gamma^{O(K)}\operatorname{poly}(U).
 \tag{13}
\]
This is where \(\Gamma^{O(K)}\) replaces the previous
\(\Gamma^{O(K^2)}\). The improvement is insufficient by itself:
the multiplication of quality across recursive levels must
also be bounded.

## 5. Recursive pools, work, and quality

Apply the existing fixed port-fiber degree reset to each settled
selected graph. Each actual parent vertex lifetime has one
fiber; retained inactive fibers count in child size. Purely null
export over a retired parent lifetime is suppressed after all
real-edge retirement is complete. Stable core forests, frozen
gauges, physical provenance, and dormant motion counters retain
their existing lifetime interfaces.

For an enumerated positive integer \(c_C\), use the literal cap
\[
 C=2^{c_C(\lceil U/K\rceil+t^2h+h)},\qquad
                    P=C^{c_P},
 \tag{14}
\]
where \(c_P\) is the fixed polynomial encoding/pool exponent
of the chosen implementation. Increasing the fixed \(c_C\)
absorbs the source constants in (11). The port scale is
\[
 H_{\rm port}
       =2^{\lceil\log_2(4(\log_2C+1))\rceil}.
 \tag{15}
\]
Real child lengths and gradients are scaled by this value;
null fiber connectors have integer length one and gradient
zero. In particular \(\log H_{\rm port}=O(\log U)\).

Set
\[
                 d_*=\lceil8U/x\rceil+10=O(t).
 \tag{16}
\]
The actual child size is at most its parent size times \(P/k\),
up to the stated period credit. Since
\[
 \frac{\log P}{x}
      =O\!\left(\frac1t+\frac{t^3h}{U}\right)=o(1),
 \tag{17}
\]
every nonbase level shrinks by at least \(k^{1/2}\) eventually.
Thus the depth guard (16) has constant slack.

Let \(G_d\) bound occurrence and answer size, \(J_d\) be the
initial work allowance per actual record, and \(T_d\) be
amortized update work. The safe coupled recurrence is
\[
 \begin{aligned}
 G_d&\leq P(G_{d-1}+1),\\
 J_d&\leq W+P(G_{d-1}+1)
                  +(P/k)(J_{d-1}+T_{d-1}),\\
 T_d&\leq O(kW+kP(G_{d-1}+1))
                  +O(P)(J_{d-1}+T_{d-1}).
 \end{aligned}
 \tag{18}
\]
The \(T_{d-1}\) term in the initialization allowance pays for
late spending of additive child-update credit. With
\(\mathcal H_d=J_d+T_d/k\), (18) gives
\[
 \mathcal H_d\leq O(W+P(G_{d-1}+1))
                         +O(P)\mathcal H_{d-1}.
 \tag{19}
\]
Work, occurrence counts, and output-piece counts are bounded by
\[
                    k^{O(1)}W(cP)^{O(d_*)}.
 \tag{20}
\]
Actual initialization is actual size times this quantity.
There is one overall polynomial factor in \(k\), not a new
factor \(k\) on each recursive child edit.

The distance-spanner stretch in one level is
\(\Gamma^{O(K)}\). The raw-cycle inverse quality over all
levels is therefore bounded by
\[
            k^{O(1)}
             \exp O(d_*K\log\Gamma+d_*\log U).
 \tag{21}
\]
The factor involving \(d_*K\) must not be omitted. Local
correction circulations and same-tree loops are extracted
explicitly before recursion, with their actual lengths charged
to (13). Open edges use the established gauge correction;
zero-link contraction preserves circulation gradients.

## 6. The 5/6 balance

Substitution into (1) yields
\[
          \log\Gamma=O(t^2h),\qquad
          \log F=O(U/t+t^2h)=O(x).
 \tag{22}
\]
The local repair term is
\[
                  K\log\Gamma=O(t^4h)=O(x).
 \tag{23}
\]
The propagated occurrence/work term is
\[
 d_*\log P
    =O\!\left(t(U/t^2+t^2h+h)\right)
    =O(U/t+t^3h)=O(x).
 \tag{24}
\]
Finally the full quality loss is
\[
                  d_*K\log\Gamma=O(t^5h)\leq O(U/t)
                                                    =O(x).
 \tag{25}
\]
The last inequality uses precisely \(t^6h\leq U\).
It is the strongest of these parameter constraints.

Thus all quantities in (20)--(21) have a common logarithmic
envelope
\[
 \begin{split}
 O\!\left(
 x+\log F+K\log\Gamma+
 \frac Ux\left(\frac UK+\log\Gamma+K\log\Gamma\right)
 \right)
 &=O(U^{5/6}(\log(U+4))^{1/6}).
 \end{split}
 \tag{26}
\]
The construction-work factor has not been mistaken for
structural quality, and the hierarchy-wide quality term has
not been mistaken for a one-level cost.

## 7. Bits, guards, and root raw certificates

Retain the conservative finite-word envelope from the degree-reset
backend. A core stored length is at most a polynomial in its
level's graph size times the parent maximum length. Port scaling
contributes \(O(\log U)\) bits. Frozen potential sums and gradients
obey the same crude per-level bound. If root prices have at most
\(c_0U\) bits, declare
\[
                  b_*=(c_0+100)U(d_*+1)=O(Ut).
 \tag{27}
\]
All arithmetic is charged at this precision. On a nonbase input
\(\log m\geq x-O(1)\), and
\[
                 b_*/x^2=O(t^3/U)=o(1).
 \tag{28}
\]
The safe source guard \(b_*\leq(\log m)^2\) eventually holds.
Actual small bases use multiword arithmetic, not a false
\(O(\log m)\)-bit root-price assumption.

For an enumerated positive integer \(c_E\), declare
\[
                            E_*=2^{c_Ex}.
 \tag{29}
\]
For one fixed sufficiently large \(c_C\), followed by a fixed
sufficiently large \(c_E\), (29) bounds initialization per actual
record, update work, output pieces, route notifications, flat
multiplicity, and inverse raw quality. Check all declared degree,
size, transcript-prefix, bit, lifetime, and depth caps before
using an answer. The safe transcript guard includes its initial
credit unless the optional fresh-base proof has been invoked.

Deep abstract lengths need not be rounded into a short root
certificate. The root client sums physical root input lengths
along the exposed returned forest paths, counting every repeated
occurrence and unit signed piece. With at most \(E_*\) pieces and
root forest size at most \(ME_*\),
\[
 V\leq ME_*^2\max_e\ell_e,\qquad
 |N|\leq ME_*^2\max_e|g_e|.
 \tag{30}
\]
For a fixed favorable tuple, \(\log E_*=o(U)\), so both quantities
have \(O(U)\) root bits. Exact raw \(V\) is no greater than the
inherited upper certificate; replacing that certificate by \(V\)
only improves the ratio. Internal arithmetic is still charged
at (27).

The guards do not certify the imported mathematical contracts.
Their purpose is to make a single finite program and its
first-failure analysis explicit. Eventual fast correctness
uses the constructions in Sections 1--5.

## 8. Decoupled ledgers and numerical work

Let \(S=2^s\) bound the physical degree-three matching instance,
and use master \(U=2s\). The independent binary-ledger proof gives
\[
 a=s,\qquad C_{\rm ledger}=s+1,\qquad b_j=2^{s-j}.
 \tag{31}
\]
Set
\[
 D=2^{\lceil\log_2\max\{16,4E_*\}\rceil},
                     \qquad q_{\rm num}=1/(16D).
 \tag{32}
\]
The grid choices \(\delta=S^{-1000}\),
\(\epsilon=S^{-3000}\), and the existing root price scale remain
unchanged. Eventually \(D\leq S^2\) and
\(q_{\rm num}\geq S^{-1}\); the strict acceptance margin
\(1/(4D)>2q_{\rm num}\) holds literally.
The ledger base is two and need not dominate \(E_*\).

Use the actual nominal size
\[
              M=2^{\lceil\log_2(16(R_{\rm nom}+2))\rceil}.
 \tag{33}
\]
The top choice \(R_{\rm nom}=S(s+1)^{10}\) and the local choice
\(8192(P_{\rm debt}+1)\) are at most \(S^2=2^U\) eventually.
There is no rounding to a multiple of \(2a^2\).

The structural proof bounds the lower-ledger reset sum by
\(O(s^3S)\), global resets by \(O(s)\), and the number of gap
phases by \(O(s^2)\). The
[decoupled numerical client](decoupled_numerical_client.md)
has work
\[
              O(MD+QD+D^2J)\operatorname{poly}(s),
 \tag{34}
\]
where \(J\) counts accepted steps and \(Q\) includes client calls
and refreshes. Local and all-expanded exact recovery cost
\((P_{\rm debt}+1)D^4\operatorname{poly}(s)\); the top run costs
\(SD^4\operatorname{poly}(s)\). These recoveries round the
already conserved grid flow and use ordinary residual searches.
They do not call a new static max-flow routine.

After all resets and phases, a favorable complete branch costs
\[
 SE_*^4\operatorname{poly}(s)
    =S\exp O\!\left(s^{5/6}(\log(s+4))^{1/6}\right).
 \tag{35}
\]
The exact all-expanded recovery, binary-ledger budget,
persistent integral carrier, and general-gap driver are the
same previously proved interfaces. Before the first guard
failure, old states are valid and the physical/padded debt
bounds control the current attempted projection. Equations
(22)--(35) then show that the fixed favorable tuple cannot
reach a guard failure on sufficiently large inputs. This is
a mathematical consequence of the supplied contracts, not
of a final matching verifier.

## 9. One computable program, all graphs, and the optional kernel

Clean the input once: ignore self-loops for cardinality matching,
retain one representative of each parallel pair, and compact the
nonisolated vertices. In the usual integer-labeled graph input
model this costs \(O(n+m)\). Let \(m_s\) be the resulting
number of simple edges.

The exact odd-path degree-three gadget from
[general_graph_gap_reduction.md](general_graph_gap_reduction.md)
has size \(O(m_s)\), a known optimum offset, and a decoder for
arbitrary auxiliary maximum matchings. The gap phase is applied
without a perfect-matching promise; its LOW implication is the
general improvement-target statement. Thus the graph class has
not been restricted in the numerical composition.

Enumerate all positive integer pairs \((c_C,c_E)\). Give each
guarded branch a fixed positive geometrically decreasing share
of word instructions, and give one deterministic classical exact
matching branch a fixed positive share. Source algorithms,
allocation, callbacks, large-integer arithmetic, and verification
are charged within these instruction budgets; no long subroutine
is treated as an indivisible unit.

For each decoded proposal, validate that it is a matching on the
compact working graph, and run one exact deterministic
general-graph augmenting-path search. Accept only when no
augmenting path exists. This validation runs in that branch's
budget. The classical branch ensures termination and exact
output even if another branch makes an incorrect early LOW
claim or suspends.

One fixed pair has all the eventual fast-time bounds above.
Its budget share is a fixed positive constant, so it preserves
the asymptotic time. The same finite program handles the
finitely many exceptional smaller sizes, without knowing their
threshold or the favorable pair. The resulting all-graph
research bound is
\[
 \boxed{
 O(n+m)+(m_s+1)\exp O\!\left(
       (\log(m_s+2))^{5/6}
       (\log\log(m_s+4))^{1/6}
                         \right).
 }
 \tag{36}
\]

Optionally apply the exact matching-size kernel once, before
starting workers. A maximal matching gives a vertex cover \(C\).
Keep every edge inside \(C\), and for each \(v\in C\) keep
\(|C|+1\) arbitrary neighbors outside \(C\), or all of them if
there are fewer. An omitted matched neighbor can be replaced by
an unused retained one: at most \(|C|\) outside vertices are
occupied by the matching. Iterating this exchange preserves
the optimum. The kernel has
\[
                    m_c\leq\min\{m_s,O(\nu^2)\}.
 \tag{37}
\]
All workers, including the classical branch and every verifier,
then operate on this compact kernel. Only the winning matching
is mapped once to original edge IDs. This gives (36) with
\(m_s\) in its second term replaced by \(m_c\), while retaining
the one-time \(O(n+m)\) input term.

Exact output of this finite program and its fast-time proof are
separate statements. The first follows from the classical branch
and exact augmenting-path verification. The second depends on
the reconstructed source primitives, the new normalized-route
static sparsifier, dynamic lifetime and raw-cycle interfaces,
and the shared matching correctness proofs. Independent review
of these notes does not constitute external verification.
