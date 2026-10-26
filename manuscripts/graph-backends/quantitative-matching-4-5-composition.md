# A 4/5 research composition from sequential expander routing

**Separate research theorem candidate, 24 October 2026.** This note gives
the complete quantitative composition using the sequential expander
router and static sparsifier constructed in the linked provider notes.
Their mathematical proofs, including the repaired half-matching entropy
lemma, have been assembled and independently reread within this research
session. That is not external certification. The parameter calculation
does not replace those component proofs. The existing 5/6 composition
and its threshold router are unchanged.

The target remains exact maximum-cardinality matching in arbitrary
undirected graphs, with no perfect-matching promise, approximation,
bipartiteness assumption, or density restriction. The proposed bound is
```math
O(n+m)+(m_s+1)\exp O\!\left(
    (\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5}\right),
 \tag{1}
```
where $`m_s`$ is the number of edges after one-time simplification and
compaction. Section 9 gives the optional exact matching-size kernel.
This is a research proof assembly with named dependencies, not an
externally verified implementation. Exact output verification and the
proof of the faster running time are separate claims.

## 1. The additional primitive and its literal output type

Let $`U\geq2`$ be an integer master bound and set
```math
h=\lceil\log_2(U+4)\rceil.
 \tag{2}
```
Local graphs, token inventories, explicit route lists, and their genuine
identifiers have at most $`2^{O(U)}`$ records. Every initialization is
proportional to its ACTUAL input inventory; this master bound does not
authorize padding by $`2^U`$.

The new parameters are integers $`1\leq p,r\leq U`$. The routing
parameter $`p`$, decomposition parameter $`r`$, dynamic-repair depth
$`K`$, and recursive size-reduction factor $`k`$ below are distinct.
The required additional construction has structural and work factors
```math
\log_2\Gamma=O((p+r)h),\qquad
 \log_2F=O(U/p+U/r+r^2h+(p+r)h),
 \tag{3}
```
with absolute constants uniform in the growing parameters. We impose
the conservative literal range
```math
(p+r)h\leq U.
 \tag{4}
```

The routing part of (3) is the following sequential interface. On a
loopless expander of $`m'`$ edge IDs and conductance
$`\phi\geq2^{-O(rh)}`$, preprocess once in
```math
m'\exp O(U/p+ph+\log\phi^{-1})\mathrm{poly}(U)
 \tag{5}
```
work. For token demands with at most $`D\deg(v)`$ starts and at most
$`D\deg(v)`$ destinations at every vertex, return explicit walks of
length at most $`2^{O((p+r)h)}`$ and edge congestion at most
$`D\,2^{O((p+r)h)}`$. Query work is allowed to be
```math
m'D\,2^{O((p+r)h)}\mathrm{poly}(U).
 \tag{6}
```
It is not claimed to be proportional only to the number of nonempty
demands. The two witness applications below pay this full volume.
The dedicated provider is
[sequential-expander-routing-tradeoff.md](sequential-expander-routing-tradeoff.md).

The separate sequential construction combines the following interfaces:

* [the virtual expander hierarchy](virtual-expander-hierarchy-reconstruction.md),
  with actual sparse cuts, identity child inclusions, and one physical
  root embedding;
* [the explicit coverage and balance wrapper](explicit-virtual-cut-balance-wrapper.md),
  whose weak leaves and internal successes both retain at least a
  1-beta fraction of their current host, for fixed beta=1/1000;
* [exact short-path packing](sequential-short-path-matching.md) and the
  [fresh-cut matching adapter](sequential-fresh-cut-matching-adapter.md);
* [half-matching entropy progress](half-matching-entropy-progress.md)
  at recursive balanced-cut threshold at most $`1/8`$;
* [the polynomial energy cut player](polynomial-energy-cut-player.md);
* [constructive leaf routing](sequential-leaf-routing-and-chs-work.md);
* [the direct full-router recursion](conditional-full-router-from-shufflers.md),
  which does not invoke the source's Task-2/Sort mutual recursion.

The interface in (5)--(6), including its aggregate precomputed path
family and degree-split adaptation, must be obtained by their explicit
composition. It cannot be inferred just from a distributed round bound.
The fixed inverse-conductance power in (5)--(6) is essential.

### The static normalized-route interface

The input is a demand multigraph $`J`$ with distinct native edge IDs and
annotated ambient walks $`\Pi(e)`$ with the same immediate endpoints.
Let $`L_0\geq1`$ bound their lengths, let $`C_0`$ be their ambient
vertex-occurrence congestion including endpoints, and let
$`\Delta_0=\Delta(J)`$. Erase closed subwalks of each individual image,
obtaining a table $`\Pi'`$ of simple paths. Thus
```math
L(\Pi')\leq L_0,\qquad C(\Pi')\leq C_0.
 \tag{7}
```
The additional static construction returns $`\Pi'`$, a subgraph
$`\widetilde J\subseteq J`$, and explicit routes
$`\widehat\Pi:J\to\widetilde J`$, satisfying
```math
\begin{aligned}
 |E(\widetilde J)|&\leq |V(J)|\Gamma\mathrm{poly}(U),\\
 L(\widehat\Pi)&\leq\Gamma,\\
 L(\Pi'\circ\widehat\Pi)&\leq\Gamma L_0,\\
 C(\Pi'\circ\widehat\Pi)&\leq\Gamma(C_0+\Delta_0).
 \end{aligned}
 \tag{8}
```
Its full work is
```math
|E(J)|F^{O(1)}\Gamma^{O(1)}(L_0+1)\mathrm{poly}(U)
 \tag{9}
```
plus actual vertex bookkeeping. In particular, the construction-work
factor $`F`$ enters neither selected size nor ambient congestion.

The precise new static provider is
[linear-parameter-static-sparsifier.md](linear-parameter-static-sparsifier.md).
It uses the degree bands and weighted witnesses of
[the length-free static construction](length-free-ambient-static-sparsifier.md),
with (5)--(6) substituted for its threshold router, and
[deterministic weighted path selection](deterministic-weighted-path-selection.md).
For the demand-band host, the port inventory and query load give
$`m'D\leq |E(J)|\,2^{O((p+r)h)}`$. For a witness of common weight
$`\rho`$, its reverse-embedding demand has load at most
$`\max\{1,\lceil\rho\rceil\}`$, and
```math
m_W\max\{1,\lceil\rho\rceil\}
                   =O(m_W+|E(J)|)\,2^{O((p+r)h)}.
 \tag{10}
```
These are required application-level estimates: repeatedly preprocessing
once per load unit, or ignoring the $`m'D`$ query volume, would not prove
(9). The dedicated static refinement supplies their precise degree and
weight bookkeeping.

There are TWO distinct path normalizations. Besides (7), erase closed
subwalks from every returned token candidate in its immediate host
before ambient composition and weighted selection. The latter operation
produces the simple $`J`$-paths needed by that selection proof. It
decreases every edge-occurrence load and costs the already charged
explicit list length.

All normalization uses IMMEDIATE ambient vertex lifetime IDs. Distinct
aliases with the same eventual physical image remain distinct vertices.
An edge whose eventual image is null is not deleted for that reason.
The conclusion is about the returned $`\Pi'`$, not the old $`\Pi`$.
The exact circulation identity, gradient correction, and raw-lift
compatibility are supplied by
[normalized-route-cycle-comparison.md](normalized-route-cycle-comparison.md).
The central original selected-edge ID remains separately recorded even
when normalization erases its geometric occurrence.

## 2. Actual-size hierarchy and finite local computation

For an expander host with actual $`n'`$ vertices, let
```math
v=\lceil\log_2(n'+2)\rceil,\quad
 k_{\rm route}=2^{\max\{5,\lceil v/p\rceil\}},\quad
 \lambda_{\rm cap}=C_\lambda(v+1)^2.
 \tag{11}
```
Here $`C_\lambda`$ is one fixed constant justified by the explicit energy
decrease. Use the actual-size leaf condition
```math
N\leq C_{\rm leaf}k_{\rm route}^5
                                         \lambda_{\rm cap}^2.
 \tag{12}
```
No graph of the right-hand size is allocated. Each genuine internal
part then has enough vertices for
```math
\min_i|Y_i|\geq8\lambda t_{\rm parts}^2,\qquad
                        n'_X\geq\lambda t_{\rm parts}^2,
 \tag{13}
```
where $`t_{\rm parts}\leq k_{\rm route}`$. The direct scatter proof uses
these inequalities, not a CHS distributed-$`\epsilon`$ range.
The hierarchy depth is $`O(p)`$; the fixed minimum
$`k_{\rm route}=32`$ only improves that bound.

All leaves have $`\mathrm{poly}(k_{\rm route},v)`$ vertices. The
exact PSD and moment procedures may have
$`\mathrm{poly}(k_{\rm route},v,\log\phi^{-1})`$-bit TEMPORARY
integers; leaf walk moments may additionally have a fixed polynomial
dependence on inverse expansion. Their complete bit operations are
charged in (5). They are not core lengths or gradient labels and need
not satisfy the backend label cap in Section 7. Only explicit graph
IDs and path lists leave these local preprocessing calls.

At every nonroot cut-player host the degree and cut threshold losses
are polylogarithmic. Root inverse conductance is paid once. Summing
local $`k_{\rm route}^{O(1)}`$ work over disjoint child mass, with only
polylogarithmic factors multiplying across $`O(p)`$ levels, yields
```math
n'\exp O(v/p+p\log(v+2)+\log\phi^{-1}).
 \tag{14}
```
The nonroot balanced-cut player uses threshold at most $`1/8`$.
The repaired entropy proof gives a literal
$`512\lceil\log_2(N+2)\rceil`$ round cap with half-matchings.
The source's incorrect per-round calculation at threshold $`1/2`$
is not used. This changes an absolute constant, not (14).
The aggregate precomputed shuffler, fold, and leaf-circuit family has
quality $`\phi^{-O(1)}\log^{O(p)}(n'+2)`$. Identity child inclusions let
one apply the physical root embedding only once. The full-router
recursion adds $`\lambda^{O(p)}`$ and no polynomial
$`k_{\rm route}`$ factor to output quality.

A decomposition call on a smaller actual graph clips its integer
parameter $`r`$ to the source's admissible range, with constant-size
base cases. Its work remains within $`F`$, while expansion improves.
The static tiny case can use an actual spanning forest after
normalization, as in the 5/6 construction. Loop demands keep their
current endpoint annotations and permitted empty routes outside
nonloop expander hosts. Awakening such a lifetime under a native split
is not billed as a new batch of synthetic edge insertions.

## 3. Rounded master parameters and executable caps

Compute
```math
t=\max\{2,\lfloor(U/h)^{1/5}\rfloor\},\qquad
 p=r=t,\qquad K=t^2,\qquad x=\lceil U/t\rceil,\qquad k=2^x.
 \tag{15}
```
Integer-root comparisons suffice. Eventually
```math
t^5h\leq U,\quad
 t=\Theta((U/h)^{1/5}),\quad
 x=\Theta(U^{4/5}h^{1/5}).
 \tag{16}
```
Thus (4), $`K\leq U`$, and $`p,r\leq U`$ eventually hold.
Check them explicitly on finite exceptional inputs.

Use the private touched-set schedule
```math
\rho_{\rm sched}=2^{\lceil8U/K\rceil},\qquad
                 N_{\rm sched}=\rho_{\rm sched}^{\,K}.
 \tag{17}
```
The latter is an $`O(U)`$-bit counter, never an allocated universe.
No $`K^7\leq\log m`$ condition from an older worst-case spanner is
imposed on the elementary static-base schedule.

For a positive integer constant index $`c_C`$, define
```math
c_\phi=\max\{1,\lfloor c_C^{1/4}\rfloor\},\quad
 c_\Lambda=\max\{1,\lfloor c_C^{1/2}\rfloor\},\quad
 c_\Gamma=\max\{1,\lfloor c_C^{3/4}\rfloor\}.
 \tag{18}
```
Declare dyadic caps
```math
\phi_*=2^{-c_\phi rh},\qquad
 \Lambda_*=2^{c_\Lambda(p+r)h},\qquad
 \Gamma_*=2^{c_\Gamma(p+r)h}.
 \tag{19}
```
These are conservative numerical parameters and checked output
envelopes. A path exceeding its declared cap suspends the branch;
it is never truncated. The explicit internal hierarchy constants may
be fixed from their proofs. The geometric cap indices in (18) cover
unknown fixed source constants without inserting them as advice.

For sufficiently large FIXED $`c_C`$, $`\phi_*`$ lies below all
required witness expansions. The router has logarithmic quality
$`O(ph+c_\phi rh)`$, which fits $`\Lambda_*`$. Weighted selection
and the static composition have logarithmic factors
$`O(c_\Lambda(p+r)h)`$, which fit $`\Gamma_*`$. Fixed polynomial
powers of those structural quantities fit the cap
```math
C=2^{c_C(\lceil U/K\rceil+(p+r)h+h)},\qquad P=C^{c_P},
 \tag{20}
```
where $`c_P`$ is the fixed encoding/pool exponent of the chosen
implementation. This order of constants is acyclic because
$`c_\phi=o(c_\Lambda)`$, $`c_\Lambda=o(c_\Gamma)`$, and
$`c_\Gamma=o(c_C)`$.
After $`c_C`$ is fixed, a separate constant $`c_E`$ bounds all work
and inverse quality. No index grows with the input in the favorable
branch.

## 4. Static-base repair and selected-edge recourse

Use
[the amortized static-base distance sparsifier](amortized-static-base-distance-sparsifier.md).
Each selected projected edge contributes only its central ORIGINAL
core-edge ID. Prefixes and suffixes lie in already retained lower
layers. Deduplicate selected IDs across owners before degree
feedback. The work factor $`F`$ remains local and does not multiply
selected size or recourse.

The selected-degree and encoded child-edit factor has
```math
\log R=O(U/K+\log\Gamma+\log U).
 \tag{21}
```
Its safe chronological prefix is $`O(mR/k+Rz)`$ through $`z`$
parent edits. Additive initial credit may be spent late. It is not
equated with actual child initialization.

The normalized projected-route proof bounds both projected degree
and preliminary ambient congestion by a constant times old route
congestion plus the native degree:
[normalized-projected-route-composition.md](normalized-projected-route-composition.md).
For a degree-three parent, that native degree is
$`k\mathrm{poly}(U)`$. The repaired length and congestion
therefore obey
```math
L_{j+1}\leq O(\Gamma)L_j,\qquad
 C_{j+1}\leq O(\Gamma)
                    (C_j+k\mathrm{poly}(U)).
 \tag{22}
```
There is no $`L_j`$ factor in the second recurrence. After $`K`$
layers, lengths are $`\Gamma^{O(K)}`$, and congestion is
$`k\mathrm{poly}(U)\Gamma^{O(K)}`$. An optional fresh-base
normalization changes only the absolute constant in $`O(K)`$.

The local work envelope is
```math
W=k^{O(1)}\rho_{\rm sched}^{O(1)}F^{O(1)}
                       \Gamma^{O(K)}\mathrm{poly}(U).
 \tag{23}
```
Route-owner replacement, inverse occurrence lists, current
correction scores, native endpoint annotations, and erased-path
retirement are charged here. Selected edges keep their genuine
labels and provenance. New normalized routes replace their own
correction circulation $`e-R(e)`$, not a child edge's gradient.
All raw-lifetime and no-query transaction requirements remain in
force; normalization does not reset signed or absolute motion.

## 5. Recursive work, occurrence pools, and full quality

Apply the fixed port-fiber degree reset, with one fiber per actual
parent vertex lifetime. Retained inactive fibers are counted in
child size. A parent lifetime is suppressed from exported null
components only after genuine edge retirement has completed.
Stable core forests, frozen potentials, parallel-edge provenance,
common path pools, and dormant motion counters use the existing
raw-lift interface.

The port scale is
```math
H_{\rm port}=
        2^{\lceil\log_2(4(\log_2C+1))\rceil},
 \tag{24}
```
with real child lengths and gradients scaled together, and null
fiber links assigned length one and gradient zero.
$`\log H_{\rm port}=O(\log U)`$.
Use the depth cap
```math
d_*=\lceil8U/x\rceil+10=O(t).
 \tag{25}
```
Since
```math
\frac{\log P}{x}
       =O\!\left(\frac1t+\frac{t^2h}{U}\right)=o(1),
 \tag{26}
```
the child size factor $`P/k`$ is at most $`k^{-1/2}`$ eventually.
The depth cap has fixed slack.

Let $`G_d`$ bound occurrences and answer pieces, $`J_d`$ the work
allowance per actual initialized record, and $`T_d`$ amortized
update work. The safe coupled recurrence is
```math
\begin{aligned}
 G_d&\leq P(G_{d-1}+1),\\
 J_d&\leq W+P(G_{d-1}+1)
                 +(P/k)(J_{d-1}+T_{d-1}),\\
 T_d&\leq O(kW+kP(G_{d-1}+1))
                 +O(P)(J_{d-1}+T_{d-1}).
 \end{aligned}
 \tag{27}
```
The $`T_{d-1}`$ term pays for late spending of initial child-update
credit. With $`\mathcal H_d=J_d+T_d/k`$, the recurrence closes as
```math
\mathcal H_d\leq O(W+P(G_{d-1}+1))+O(P)\mathcal H_{d-1}.
 \tag{28}
```
Thus initialization per ACTUAL record, amortized updates, and
occurrence/piece counts are at most
```math
k^{O(1)}W(cP)^{O(d_*)}.
 \tag{29}
```
There is one polynomial $`k`$ factor overall, not a $`k`$ factor
on every recursive child update.

The one-level distance quality is $`\Gamma^{O(K)}`$. The full
raw-cycle inverse quality includes its multiplication across
levels:
```math
k^{O(1)}
                 \exp O(d_*K\log\Gamma+d_*\log U).
 \tag{30}
```
Local correction circulations and same-tree loops are extracted
before recursion with their actual expansion work charged in
$`W`$. The exact native circulation identity and frozen-gauge
raw lift justify their comparison. Equation (30) is not replaced
by a one-level quality estimate.

## 6. The 4/5 balance

Substituting $`p=r=t`$ into (3) gives
```math
\log\Gamma=O(th),\qquad
            \log F=O(U/t+t^2h+th)=O(x).
 \tag{31}
```
The local repair term and propagated occurrence/work term are
```math
K\log\Gamma=O(t^3h)=O(x),
 \tag{32}
```
```math
d_*\log P
      =O\!\left(t(U/t^2+th+h)\right)
      =O(U/t+t^2h)=O(x).
 \tag{33}
```
Most importantly, the full quality term is
```math
d_*K\log\Gamma=O(t^4h)\leq O(U/t)=O(x),
 \tag{34}
```
using $`t^5h\leq U`$.
Consequently the common logarithmic envelope is
```math
\begin{split}
 O\!\left(x+\log F+K\log\Gamma+
       \frac Ux\left(\frac UK+\log\Gamma+K\log\Gamma\right)\right)
  &=O(U^{4/5}(\log(U+4))^{1/5}).
 \end{split}
 \tag{35}
```
Construction work, structural recourse, and full-depth quality
have each been counted separately.

## 7. Stored labels, guards, and root certificates

Retain the conservative degree-reset length/gradient bound:
one level increases maximum stored magnitude by at most a
polynomial in its graph size, followed by (24). Frozen potential
sums obey the same conservative bound. For root labels of at
most $`c_0U`$ bits, declare
```math
b_*=(c_0+100)U(d_*+1)=O(Ut).
 \tag{36}
```
Actual stored-label operations are charged at that precision.
On a nonbase graph $`\log m\geq x-O(1)`$, and
```math
b_*/x^2=O(t^3/U)=o(1).
 \tag{37}
```
Thus the conservative source guard
$`b_*\leq(\log m)^2`$ eventually holds. Actual small instances
use a direct multiword base; they do not assume root prices
have $`O(\log m)`$ bits. Temporary matrix/moment integers
from Section 2 remain separately charged local work.

Set the executable master envelope
```math
E_*=2^{c_Ex}.
 \tag{38}
```
For one fixed sufficiently large $`c_C`$, followed by one fixed
sufficiently large $`c_E`$, it bounds initialization per actual
record, update work, notifications, answer pieces, flat
multiplicity, and inverse raw quality. Every degree, prefix,
size, lifetime, bit, depth, and work cap is checked before
using an answer. A violation suspends that branch.

The root client computes the actual raw physical denominator
and numerator from returned paths, with repetitions and unit
signed pieces counted:
```math
V\leq ME_*^2\max_e\ell_e,\qquad
 |N|\leq ME_*^2\max_e|g_e|.
 \tag{39}
```
Root forest size is at most $`ME_*`$, and there are at most
$`E_*`$ pieces. For a fixed favorable tuple,
$`\log E_*=o(U)`$, so (39) has $`O(U)`$-bit root values.
The raw denominator does not exceed an inherited upper
certificate, so using it improves the ratio. Internal
arithmetic still pays (36).

These executable guards do not establish the imported mathematical
contracts. Eventual nonfailure and fast completion require the
supplied primitive and lifetime proofs.

## 8. Decoupled exact matching client

Let $`S=2^s`$ bound the physical degree-three matching instance,
and use master $`U=2s`$. The binary-ledger proof sets
```math
a=s,\quad C_{\rm ledger}=s+1,\quad b_j=2^{s-j}.
 \tag{40}
```
Choose
```math
D=2^{\lceil\log_2\max\{16,4E_*\}\rceil},\qquad
                     q_{\rm num}=1/(16D).
 \tag{41}
```
The grid $`\delta=S^{-1000}`$, $`\epsilon=S^{-3000}`$, and
the existing root price scale are unchanged. Eventually
$`D\leq S^2`$, $`q_{\rm num}\geq S^{-1}`$, and the strict
acceptance margin $`1/(4D)>2q_{\rm num}`$ holds literally.

For actual nominal size $`R_{\rm nom}`$, initialize with
```math
M=2^{\lceil\log_2(16(R_{\rm nom}+2))\rceil}.
 \tag{42}
```
The top choice $`R_{\rm nom}=S(s+1)^{10}`$ and the local
choice $`8192(P_{\rm debt}+1)`$ are at most $`2^U=S^2`$
eventually. No old $`2a^2`$ rounding condition is used.
The ledger base two need not dominate $`E_*`$.

The structural reset sum is $`O(s^3S)`$, the number of global
resets is $`O(s)`$, and the number of gap phases is $`O(s^2)`$.
The [decoupled client](decoupled-numerical-client.md) costs
```math
O(MD+QD+D^2J)\mathrm{poly}(s),
 \tag{43}
```
Here $`J`$ counts accepted steps and $`Q`$ counts external
requests from the owning client, including failed/LOW queries
and exact point requests. Internal numerical refreshes form
the separate $`O(DJ)`$ category already paid by $`D^2J`$;
they are not added to this $`Q`$.
Local and all-expanded exact recovery cost
$`(P_{\rm debt}+1)D^4\mathrm{poly}(s)`$. They round
the conserved grid circulation and use ordinary residual
searches; no fresh static max-flow call is hidden there.

The complete favorable branch therefore costs
```math
SE_*^4\mathrm{poly}(s)
       =S\exp O(s^{4/5}(\log(s+4))^{1/5}).
 \tag{44}
```
This uses the same persistent integral carrier, exact physical
matching representation, factor-critical contraction proof,
general-gap LOW implication, and reset/phase budget as the
existing construction.

For a first supposed failure on a favorable sufficiently large
input, all prior states satisfy those interfaces. Physical debt,
padded debt, and prefix estimates bound the attempted operation.
Equations (15)--(44) then place its work and state within the
declared caps, contradicting first failure. This argument is
conditional on the mathematical primitive, not on a verifier.

## 9. One finite program, all graphs, and an optional kernel

Simplify once: ignore self-loops for cardinality matching,
retain one representative per parallel pair, and compact
nonisolated vertices. In the ordinary integer-labeled input
model this costs $`O(n+m)`$; let $`m_s`$ be the surviving
simple edge count.

The exact odd-path degree-three reduction in
[general-graph-gap-reduction.md](general-graph-gap-reduction.md)
has size $`O(m_s)`$, a known optimum offset, and a decoder
for every auxiliary maximum matching. Gap phases use the
general improvement target and have no perfect-matching
promise. The numerical improvement does not restrict the
class of input graphs.

Enumerate positive integer pairs $`(c_C,c_E)`$. Give every
guarded branch a fixed positive geometrically decreasing
share of word instructions, and give one deterministic
classical exact matching branch a fixed positive share.
Charge all allocation, callbacks, local multiword arithmetic,
path materialization, and verification to those budgets.
No long subroutine is an indivisible scheduled unit.

Validate each decoded proposal on the compact working graph,
then perform one exact deterministic general-graph
augmenting-path search. Accept only if no augmenting path
exists. This verification runs in the proposing branch's
budget. The classical branch ensures termination and exact
output even when another branch suspends or makes an
incorrect early LOW claim.

Under the additional primitive theorem, one fixed pair has
the eventual fast bound (44), and its budget share is a
fixed positive constant. The same finite program handles
all finite exceptional sizes through the classical branch,
without knowing their threshold. This proves the conditional
time bound (1).

Optionally compute an exact matching-size kernel before
starting workers. A maximal matching gives a vertex cover
$`C_0`$. Keep all edges inside it; for each $`v\in C_0`$,
keep $`|C_0|+1`$ arbitrary outside neighbors, or all if fewer.
Any omitted maximum-matching edge can be replaced by an
unused retained outside neighbor, since at most $`|C_0|`$
outside vertices are occupied. Iterating preserves the
optimum and gives
```math
m_c\leq\min\{m_s,O(\nu^2)\}.
 \tag{45}
```
ALL workers, including the classical branch and every
augmenting-path verifier, then use this compact kernel.
Only the winning output is mapped once to original IDs.
Thus $`m_s`$ in the second term of (1) may be replaced by
$`m_c`$, while keeping the one-time $`O(n+m)`$ term.

The exact-output statement uses the verifier and classical
fallback. The fast-time statement additionally uses (3)--(10)
and their full sequential construction, together with all
shared dynamic, raw-cycle, numerical, and matching proofs.
This distinction remains necessary after an independent
mathematical review.
