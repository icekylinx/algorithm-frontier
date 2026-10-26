# A 6/7 quantitative composition for deterministic general matching

**Research theorem candidate, 24 October 2026.** The two-parameter
STATIC sparsification interface used below is supplied by
[the separated static parameter reconstruction](separated-static-sparsifier-parameters.md)
and [the independent path/degree-band derivation](parameterized-expander-path-and-degree-bands.md).
This note proves its parameter balance, recursive composition,
numerical client bounds, and computable matching wrapper.
The result is a research proof assembly depending on the named
public-source and reconstruction proofs; it is not an externally
verified or implemented theorem. The earlier 14/15 construction
remains available separately.

The target problem is exact maximum-cardinality matching in an
arbitrary undirected graph. No perfect-matching promise, bipartiteness,
bounded-density promise, or approximation guarantee is assumed.

## 1. The precise additional primitive

Let $`U`$ be a common integer master parameter. The actual input size
of every call is at most $`2^{O(U)}`$, but a call must initialize only
its ACTUAL records. Let $`q_{\rm exp},r_{\rm cut}\geq1`$ be integer
parameters. The proposed primitive has two different envelopes:

```math
\log_2\Gamma
   =O\!\left(q_{\rm exp}r_{\rm cut}\log(U+4)\right),
 \tag{1}
```
```math
\log_2 F
   =O\!\left(
     \frac{U}{q_{\rm exp}}+\frac{U}{r_{\rm cut}}
     +r_{\rm cut}^2\log(U+4)
     +q_{\rm exp}r_{\rm cut}\log(U+4)
     \right).
 \tag{2}
```

All constants must be absolute for one finite family of constructive
algorithms, rather than constants depending arbitrarily on the two
growing parameters.

Given an ambient graph $`H'`$, a demand graph $`J`$, and explicit
annotated paths $`\Pi:J\to H'`$, the primitive must return a sparse
SUBGRAPH $`\widetilde J\subseteq J`$ and explicit demand routes with:

```math
\begin{split}
 |E(\widetilde J)|&\leq
       \Gamma\,\mathrm{poly}(U)|V(J)|,\\
 L(\Pi\circ\Pi_{J\to\widetilde J})&\leq \Gamma L(\Pi),\\
 C(\Pi\circ\Pi_{J\to\widetilde J})&\leq
       \Gamma L(\Pi)\bigl(C(\Pi)+\Delta(J)\bigr).
 \end{split}
 \tag{3}
```

The input-path-length factor in the last line is NOT removed.
Parallel IDs and repeated path occurrences are counted. Empty loop
routes retain current endpoint annotations. The work, including
explicit route indexing and notifications, is bounded by

```math
|E(J)|\,F^{O(1)}\Gamma^{O(1)}
                 (L(\Pi)+1)\mathrm{poly}(U),
 \tag{4}
```

plus ordinary actual-input vertex bookkeeping. The ambient graph for
a local call may be restricted to the used routes and their central
edges. Unrelated isolated native roots and the master scheduling
universe are not scanned or allocated.

The source reconstruction establishes (1)--(4) on the actual static
calls used below, including the parameter ranges and small input
cases recorded in Section 2. In particular, replacing a local input
by a master-sized padded graph is not permitted by (4). Running time
$`F`$ does not enter the sparsity, path length, congestion, selected
degree, or selected recourse factor $`\Gamma`$.

The intended source route separates the hierarchy parameter of the
decremental expander path construction from the cut-player parameter
in the deterministic decomposition. Its mathematical reconstruction
is in [the separated static parameter note](separated-static-sparsifier-parameters.md).
Equations (1)--(2), including that note's source and finite-word
dependencies, are the explicit imported mathematical interface of
this composition. The independent derivation identifies the terminal
cutoff, live-root deletion order, and loopless degree-band conventions
used in that interface.

## 2. Actual-size elementary cases

Write $`L_U=\lceil\log_2(U+4)\rceil`$, as in Section 3.
The source construction requires $`q_{\rm exp}\geq2`$,
$`r_{\rm cut}\geq1`$, both at most $`U`$, and
$`q_{\rm exp}r_{\rm cut}L_U\leq U`$. Its cut player has an
absolute terminal cutoff $`|T|^{1/r_{\rm cut}}\geq N_0`$.
The following actual-size adapters are part of its precise interface.

In a decomposition call on a cluster of size $`m'`$, clip
$`r_{\rm cut}`$ to
$`\min\{r_{\rm cut},\lfloor\log(m'+2)/c_0\rfloor\}`$, with a
constant-size base. This improves the output conductance; the
construction work remains within (2), because in the clipped regime
$`\log(m'+2)/r'=O(1)`$ and $`(r')^2\log\log(m'+4)\leq O(r_{\rm cut}^2L_U)`$.

For a path-oracle call of actual size $`m'`$, if
$`\log(m'+2)<c_1q_{\rm exp}r_{\rm cut}L_U`$, use ordinary expander
pruning and direct BFS queries. Its query work is
$`2^{O(q_{\rm exp}r_{\rm cut}L_U)}`$, and its initialization and all
pruning work are $`m'2^{O(q_{\rm exp}r_{\rm cut}L_U)}`$.
Otherwise the smallest hierarchy terminal set has logarithmic size
at least $`c_1r_{\rm cut}L_U`$. This meets the cut-player cutoff and
the polynomial-logarithmic pruning/degree slack for sufficiently
large fixed $`c_1`$. These are local actual-size cases, not padding
with $`2^U`$ dummy records.

The corresponding ordinary-pruning and hierarchy proofs are part
of the separated-parameter note's named source dependencies.

The interface does not require a sophisticated static call on every
tiny demand graph. For example, if $`J`$ has $`v`$ nonisolated vertices,
keep one spanning forest in each component and route each demand along
its tree path. This uses at most $`v-1`$ edges per component. If
$`L=L(\Pi)`$, then each composed route has length at most $`vL`$.
Its ambient congestion is at most
```math
|E(J)|vL\leq v^2L\,\Delta(J).
```
Thus, whenever $`v^2\leq\Gamma`$, this elementary construction satisfies
the safe structural bounds (3). Explicit construction costs
$`O(|E(J)|vL)`$, which fits the existing $`\Gamma`$-polynomial factor
in (4). Loops have their annotated empty routes.

This observation discharges an additional elementary small-static-call
regime. The actual path-oracle and cut-player restrictions are
discharged by the adapters just stated and their source
reconstruction; they are not inferred from this spanning-tree example.

At the recursive cycle-backend level, an actual degree-three input
of size at most $`24k`$ uses the direct small-graph ratio solver.
This solver handles its actual records and full declared word sizes;
it does not allocate $`k`$ records when the input is smaller.

## 3. Rounded parameters

Set
```math
L_U=\left\lceil\log_2(U+4)\right\rceil,\qquad
 t=\max\left\{2,\left\lfloor(U/L_U)^{1/7}\right\rfloor\right\},
 \tag{5}
```
where the integer root is computed by integer comparisons. Use
```math
q_{\rm exp}=r_{\rm cut}=t,\qquad K=t^2,\qquad
 x=\left\lceil U/t\right\rceil,\qquad k=2^x.
 \tag{6}
```
Here $`K`$ is the touched-set REPAIR depth, while $`k`$ is the
parent-to-child SIZE reduction parameter. They are different objects.
The numerical logarithmic-step accuracy parameter is introduced
later and is not $`q_{\rm exp}`$.

For all sufficiently large $`U`$,
```math
t^7L_U\leq U,\qquad
 t=\Theta((U/L_U)^{1/7}),\qquad
 x=\Theta(U^{6/7}L_U^{1/7}).
 \tag{7}
```
In particular $`K\leq U`$. For finite small values where the desired
size shrink or source guards do not hold, the guarded branch may
suspend and the unconditional classical branch remains available.
Check the literal static guard
$`q_{\rm exp}r_{\rm cut}L_U=t^2L_U\leq U`$ before invoking that
primitive. It holds eventually because
$`t^2L_U\leq t^7L_U\leq U`$; it also ensures that the primitive's
constructed witnesses have only $`2^{O(U)}`$ records.

For the native scheduling counter one may take
```math
\rho=2^{\lceil 8U/K\rceil},\qquad
 N_{\rm sched}=\rho^K.
 \tag{8}
```
This is a counter only. Its bit length is $`O(U)`$, and no graph
with $`N_{\rm sched}`$ vertices is constructed.

## 4. Static repair plus amortized selected-degree feedback

Apply
[the short-period alternative](amortized-static-base-distance-sparsifier.md),
using (3) for each static repair. Its proof requires the structural
factor $`\Gamma`$, while (4) is paid as local work. Its explicit
empty-loop convention, central-original-edge selection, layer
reference counts, and selected endpoint coalescing remain in force.

In particular, selecting a projected edge adds only its central
ORIGINAL core-edge ID. Its old route prefixes already lie in lower
layers. Expanding those prefixes into extra memberships would produce
an incorrect recourse bound.

Let $`A=\mathrm{poly}(U)`$ cover stable forests, buckets, native
translation, and ordinary indexing. The alternative supplies
```math
R=(A\rho\Gamma)^{O(1)},\qquad
       \log R=O(U/K+\log\Gamma+\log(U+4)).
 \tag{9}
```
Its initial selected graph has $`O(mR/k)`$ actual records. With the
explicit initial credit, its ordinary child transcript through $`h`$
parent edits has size $`O(mR/k+Rh)`$. Alternatively, its one-time
fresh-base normalization gives $`O(Rh)`$ post-initialization updates:
freeze the settled selected graph and all valid routes before child
publication, then reset only the private touched-set clock and
repair ownership lists.

The literal congestion recurrence is
```math
L_{j+1}\leq O(\Gamma)L_j,\qquad
 C_{j+1}\leq O(\Gamma)L_j C_j.
 \tag{10}
```
Hence route length is $`\Gamma^{O(K)}`$, and route congestion is
$`k\mathrm{poly}(U)\Gamma^{O(K^2)}`$.
The fresh-base normalization does not worsen the exponent: its initial
route length is already $`\Gamma^{O(K)}`$ and congestion is
$`k\Gamma^{O(K^2)}`$, and another $`K`$ levels of (10) still give
$`\Gamma^{O(K^2)}`$.

A common local work envelope is therefore
```math
W=k^{O(1)}\rho^{O(1)}F^{O(1)}
                    \Gamma^{O(K^2)}\mathrm{poly}(U).
 \tag{11}
```
No factor $`F`$ belongs in (9). The old restriction
$`K^7\leq\log m`$, used by a different worst-case spanner
instantiation, is not imported. The elementary repair clock only
requires $`K\leq O(U)`$; any restrictions of the new static primitive
must instead be verified directly under Section 1.

## 5. Recursive size, occurrence, and work bounds

Apply the existing fixed port-fiber degree reset to each settled
selected graph. Let $`P=R^{O(1)}\mathrm{poly}(U)`$ bound the
child size factor, its fully encoded ordinary edits, and its flat-pool
factor. Every actual parent vertex lifetime has one fixed fiber.
Inactive fibers remain counted in the child, and their purely null
parent export is suppressed after complete real-edge retirement.
The stable core forests and frozen gauges are unchanged.

A literal cap can be chosen, for an enumerated positive integer
$`c_C`$, as
```math
C=2^{c_C(\lceil U/K\rceil+t^2L_U+L_U)},\qquad P=C^{c_P},
 \tag{12}
```
where $`c_P`$ is one fixed sufficiently large integer for the stated
encoding and pool construction. The port scale is
```math
H_{\rm port}
   =2^{\lceil\log_2(4(\log_2 C+1))\rceil}.
 \tag{13}
```
Its logarithm is $`O(\log U)`$. It scales real child edges and
gradients; fiber connectors have integer length one and zero gradient.

Use the depth guard
```math
d_*=\left\lceil 8U/x\right\rceil+10=O(t).
 \tag{14}
```
Since
```math
\frac{\log P}{x}
   =O\!\left(\frac1t+\frac{t^3L_U}{U}\right)=o(1),
 \tag{15}
```
the actual nonbase size shrinks by at least $`k^{1/2}`$ eventually.
Thus (14) has constant slack.

For completeness, the safe recurrence includes late initial-credit
spending. Write $`G_d`$ for flat occurrence/answer size, $`J_d`$ for
the initial work ALLOWANCE per actual record, and $`T_d`$ for
amortized update work. Then
```math
\begin{aligned}
 G_d&\leq P(G_{d-1}+1),\\
 J_d&\leq W+P(G_{d-1}+1)
                 +(P/k)(J_{d-1}+T_{d-1}),\\
 T_d&\leq O(kW+kP(G_{d-1}+1))
                 +O(P)(J_{d-1}+T_{d-1}).
 \end{aligned}
 \tag{16}
```
The $`T_{d-1}`$ term in the second line is essential if the initial
child transcript credit is spent as updates later in an incomplete
parent period. It is not child initialization. Setting
$`\mathcal H_d=J_d+T_d/k`$ yields
```math
\mathcal H_d\leq
   O(W+P(G_{d-1}+1))+O(P)\mathcal H_{d-1}.
 \tag{17}
```
Thus all work, occurrences, and answer pieces fit in
```math
k^{O(1)}W(cP)^{O(d_*)}.
 \tag{18}
```
Actual initialization is bounded by the actual local size times
this envelope. There is one overall polynomial factor in $`k`$,
not one such factor multiplying each recursive update level.

## 6. Quantitative balance

Equations (1)--(2) and (5)--(7) give
```math
\log\Gamma=O(t^2L_U),\qquad
 \log F=O(U/t+t^2L_U)=O(x).
 \tag{19}
```
The crucial two remaining terms are
```math
K^2\log\Gamma=O(t^6L_U)\leq O(U/t)=O(x),
 \tag{20}
```
and
```math
d_*\log P
  =O\!\left(t(U/t^2+t^2L_U+L_U)\right)
  =O(U/t+t^3L_U)=O(x).
 \tag{21}
```
The inequalities use $`t^7L_U\leq U`$. The entire logarithmic
overhead is therefore
```math
O\!\left(
 x+\log F+K^2\log\Gamma+
       \frac Ux\left(\frac UK+\log\Gamma\right)
 \right)
 =O(U^{6/7}(\log(U+4))^{1/7}).
 \tag{22}
```
Polynomial factors in $`U`$ and the fixed source constants are
absorbed in this expression.

The spanner quality does not introduce a larger term. Across the
hierarchy it loses at most
$`\exp(O(d_*K\log\Gamma+d_*\log U))`$; terminal explicit
cycle extraction contributes $`k^{O(1)}`$. Since
```math
d_*K\log\Gamma=O(t^5L_U)\leq O(x),
 \tag{23}
```
the raw-cycle inverse quality also fits (22). Self-loops remain exact
local fundamental-cycle candidates, and all coefficients use the
unit signed piece/repeated-occurrence convention of the existing
raw lift.

## 7. Word sizes and executable guards

Retain the existing stable-forest metrics, positive port connectors,
exact gauge corrections, and immutable physical edge provenance.
A core edge length is at most a polynomial in its level's graph
size times the parent maximum length. Each port scaling contributes
only $`O(\log U)`$ additional bits. The same crude bound applies to
frozen potential sums and gradients. Hence, if root input lengths and
gradients have at most $`c_0U`$ bits, a sufficient declared bound is
```math
b_*=(c_0+100)U(d_*+1)=O(Ut).
 \tag{24}
```
All arithmetic is charged at this word size. At a nonbase input
$`\log m\geq x-O(1)`$, and
```math
\frac{b_*}{x^2}
       =O(t^3/U)=o(1).
 \tag{25}
```
Thus the existing safe finite-word check $`b_*\leq(\log m)^2`$
eventually passes. Tiny actual bases use the direct multiword solver;
they do not interpret the root prices as $`O(\log m)`$-bit prices.

For an enumerated positive integer $`c_E`$, declare
```math
E_*=2^{c_E x}.
 \tag{26}
```
For some fixed $`c_C`$, and then some fixed sufficiently large
$`c_E`$, this dominates (18), raw quality, all route notifications,
flat multiplicity, and all work factors. Check degree, resident size,
native-prefix counts, output pieces, bit sizes, depth, and complete
retirements against their declared caps before using an answer.
The initial-credit version checks $`A_0+Rh`$ once per parent period;
the fresh-base version may use the proved pure $`Rh`$ guard.

The root numerical client never needs a deep abstract denominator
to fit its root word size. It sums the actual root input lengths
along returned exposed forest paths, counting every occurrence.
With at most $`E_*`$ pieces and root forest size at most $`ME_*`$,
```math
V\leq ME_*^2\max_e\ell_e,\qquad
 |N|\leq ME_*^2\max_e|g_e|.
 \tag{27}
```
For a fixed favorable tuple $`E_*=2^{o(U)}`$, these quantities have
$`O(U)`$ root bits. Replacing an inherited upper denominator by the
exact raw $`V`$ only improves the ratio. Deep arithmetic remains
charged at (24).

No complete-source guarantee follows merely from passing these
runtime guards. Eventual fast correctness still requires the
Section 1 primitive and the stated raw/lifetime interfaces.

## 8. Binary ledgers and the numerical client

Let the physical matching instance have size at most $`S=2^s`$, and
use master $`U=2s`$. Apply the separately proved
[binary ledger hierarchy](binary-ledger-hierarchy-and-decoupled-parameters.md):
```math
a=s,\qquad C_{\rm ledger}=s+1,\qquad b_j=2^{s-j}.
 \tag{28}
```
Ledger scale is independent of backend approximation. Keep the exact
grids $`\delta=S^{-1000}`$, $`\epsilon=S^{-3000}`$, and the existing
price scale. For numerical steps set
```math
D=2^{\lceil\log_2\max\{16,4E_*\}\rceil},\qquad
                   q_{\rm num}=1/(16D).
 \tag{29}
```
For each fixed favorable tuple, eventually
$`D\leq S^2,\ q_{\rm num}\geq S^{-1}`$, and the strict acceptance
margin $`1/(4D)>2q_{\rm num}`$ holds. No ledger base $`B`$ is required
to dominate $`E_*`$, and no size exponent is rounded to a multiple
of $`2a^2`$.

Each actual numerical graph uses
$`M=2^{\lceil\log_2(16(R_{\rm nom}+2))\rceil}`$.
The top bound $`R_{\rm nom}=S(s+1)^{10}`$ and local bound
$`8192(P_{\rm debt}+1)`$ give $`M\leq S^2=2^U`$ eventually.
The lower-ledger reset sum is $`O(s^3S)`$, global resets are
$`O(s)`$, and the gap driver uses $`O(s^2)`$ phases.

The [decoupled priced client](decoupled-numerical-client.md) bounds
work by
```math
O(MD+QD+D^2J)\mathrm{poly}(s),
 \tag{30}
```
where $`J`$ counts accepted numerical steps separately from calls
and refreshes $`Q`$. The local/all-expanded exact recovery costs
$`(P_{\rm debt}+1)D^4\mathrm{poly}(s)`$, and the top run costs
$`SD^4\mathrm{poly}(s)`$. Therefore the complete favorable
matching branch has work
```math
SE_*^4\mathrm{poly}(s)
 =S\exp\!\left(
    O(s^{6/7}(\log(s+4))^{1/7})
   \right).
 \tag{31}
```
The exact rounding/recovery uses the already available conserved
grid flow, local cycle rounding, and ordinary residual searches.
It does not reintroduce a fresh static max-flow subroutine with a
larger quantitative exponent.

First-failure reasoning is unchanged. Before the first guard failure,
every old state is valid; the physical and padded debt bounds control
the current attempted projection, and the coarse finite-word bounds
remain available. Equations (19)--(31) then imply that, for a fixed
favorable tuple and sufficiently large $`S`$, the declared guards
are not reached. This implication uses the reconstructed primitive
and the mathematical interfaces in Section 1, rather than the
optimality verifier.

## 9. One finite program and arbitrary input graphs

Perform ordinary input cleanup once: ignore self-loops, coalesce
parallel copies for cardinality matching while retaining a physical
representative, and compact nonisolated vertices. Write $`m_s`$ for
the resulting number of simple edges. This costs $`O(n+m)`$ in the
chosen input model; the same compact input is shared by all workers.
Use the exact degree-three odd-path gadget and its decoder from
[the general-gap reduction](general-graph-gap-reduction.md).
The auxiliary size is $`O(m_s)`$, and the exact optimum offset and
decoder hold for arbitrary auxiliary maximum matchings.

Enumerate all positive integer pairs $`(c_C,c_E)`$ in a fixed
computable order. Give the corresponding guarded workers geometrically
decreasing instruction budgets, together with one deterministic
classical exact matching worker receiving a fixed positive share.
Every arithmetic operation, allocation, source call, and callback is
charged as word instructions. There is no uninterruptible source
subroutine treated as one scheduling step.

Validate each proposed decoded matching on the compact working
graph. Without the optional kernel this is the cleaned original
graph. Before accepting it, run one exact deterministic general-graph
augmenting-path search. Accept only if that search certifies that
there is no augmenting path. This adds only the ordinary near-linear
verification cost. The classical worker guarantees termination and
correctness even if a candidate worker suspends or produces an
incorrect early LOW conclusion.

Using the reconstructed primitive, one fixed pair has all the
eventual bounds proved above. Its budget share is a fixed positive
constant, so the portfolio has the same asymptotic time. A finite
set of exceptional smaller input sizes is handled by the same program;
no unknown size threshold or favorable pair is provided as advice.
The resulting all-graph research bound is
```math
\boxed{
 O(n+m)+(m_s+1)
  \exp\!\left(
    O\!\left(
      (\log(m_s+2))^{6/7}
      (\log\log(m_s+4))^{1/7}
    \right)
  \right).
 }
 \tag{32}
```

The same elementary matching-size kernel may be applied once before
the workers: a maximal matching yields a cover $`C`$, all edges
inside $`C`$ are kept, and for each cover vertex one keeps
$`|C|+1`$ arbitrary neighbors outside $`C`$. Replacing omitted
matched neighbors by unused kept ones proves that the optimum is
preserved. Thus (32) also holds with $`m_s`$ in its second term
replaced by $`m_c\leq\min\{m_s,O(\nu^2)\}`$, after the same
one-time input scan. This optional refinement does not restrict the
graph class.

When this kernel is used, it is the shared compact WORKING graph for
every branch, including the classical branch and every candidate's
matching validation and augmenting-path verification. The exact
exchange proof of kernel preservation is the mathematical bridge to
the original optimum; workers do not each rescan the larger original
graph to re-prove it. Map only the winning verified kernel matching
back to its retained original edge IDs, once. This preserves the
one-time $`O(n+m)`$ input term when $`m_c\ll m_s`$.

Output correctness of the finite program and its fast-time proof are
different statements. The former follows from exact verification and
the classical worker. The latter uses the supplied uniform static
primitive reconstruction, as well as the previously stated matching,
exact raw-cycle, and lifetime proofs. Their named public-source
dependencies remain part of this research theorem candidate.
Independent agreement on these mathematical notes is not external
verification of the assembled algorithm.
