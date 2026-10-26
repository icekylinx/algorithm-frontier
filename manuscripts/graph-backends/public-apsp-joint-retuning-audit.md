# Joint retuning of the public deterministic APSP construction

**Primary-source derivation and audit, 25 October 2026.**

The derivation tracks work and quality separately, including the conservative local cutoff, domain adapters and work-budget substitution.

This note separates the construction time of the public static metric
sparsifier from its output quality, and then jointly retunes that provider,
the public repair hierarchy, and the recursive APSP hierarchy. The resulting
public composite has the following quantitative point:

$$
\boxed{\begin{aligned}
 \text{amortized update factor}
    &\le \exp O(U^{6/7}h^{1/7}),\\
 \text{distance stretch}
    &\le \exp O(U^{5/7}h^{2/7}),\\
 \text{distance query time}&\le\operatorname{polylog}N,
 \qquad U=\log_2(N+4),\quad h=\lceil\log_2(U+4)\rceil.
\end{aligned}}                                                    \tag{P1}
$$

Initialization plus an update sequence costs its initial inventory plus
its number of elementary edits, multiplied by the factor in (P1). The
input is an arbitrary-degree undirected graph with positive integer
lengths at most a fixed polynomial in the history bound $N$.

**Classification.** This is a derived public baseline, obtained by reading
and composing the actual algorithms and recurrences in the sources below.
It is not a theorem printed with these parameters in any of those papers.
In particular, it does not invoke the printed KMG Theorem 3.1 beyond its
declared parameter range: Section 4 rederives the needed local envelope
from the public repair algorithm. It also does not use the new sequential
router or the new length-free ambient normalization in the research
checkpoint.

At the permitted stretch scale $\exp O(U^{6/7}h)$, (P1) strengthens
the previously recorded derived public $59/63$ update comparison. It
still has a larger update exponent than the new $11/14$ point. The
present result does not establish that $6/7$ is optimal over every
public APSP framework.

## 1. Source inventory and what is imported

All algorithmic inputs to this derivation are primary sources.

1. **CGLNPS20**, *A Deterministic Algorithm for Balanced Cut with
   Applications to Dynamic Connectivity, Flows, and Beyond*,
   [arXiv:1910.08025v2](https://arxiv.org/html/1910.08025v2).
   Theorem 1.6 is the parameterized deterministic cut player. Theorem 5.1
   is the slower balanced-cut/pruning routine with output conductance
   loss $(\log m)^{O(r)}$, as opposed to the bundled quadratic
   exponent in some later corollaries. Theorem 2.4 supplies fixed-degree
   auxiliary expanders, and Theorem 2.5 bounds the cut-matching rounds.

2. **CS21**, *Deterministic Algorithms for Decremental Shortest Paths
   via Layered Core Decomposition*,
   [arXiv:2009.08479v1](https://arxiv.org/html/2009.08479v1).
   Theorem B.9 is deterministic terminal matching in an expander with
   short paths and bounded congestion. Section 3.2, especially Lemmas
   3.10 and 3.11, gives the separate stage-count and path-length
   recurrences of the decremental expander path oracle. Theorem 3.7
   is the expander-pruning interface used in those recurrences.

3. **vdB et al.23**, *A Deterministic Almost-Linear Time Algorithm for
   Minimum-Cost Flow*,
   [arXiv:2309.16629v1](https://arxiv.org/html/2309.16629v1).
   Theorem 8.1 and Algorithm 4 give the deterministic static sparsifier
   with an ambient embedding. Theorem 8.2 explicitly imports the public
   CKL repair reduction. Theorems 8.4--8.6 and Appendix B describe the
   weighted witnesses, degree bands, and expander path dependency. Some
   subsequent citations use an earlier section number 7 for this material.

4. **CKL et al.22**, *Maximum Flow and Minimum-Cost Flow in Almost-Linear
   Time*,
   [arXiv:2203.00671v1](https://arxiv.org/pdf/2203.00671v1).
   Section 5.1, Algorithm 1, Claims 5.7--5.8, and Lemma 5.9 supply the
   touched-set repair hierarchy and its recourse/work analysis. Its own
   static sparsifier is randomized; this derivation uses the deterministic
   replacement from item 3, exactly as that replacement paper prescribes.

5. **KMG23**, *A Dynamic Shortest Paths Toolbox*,
   [arXiv:2311.06402v1](https://arxiv.org/pdf/2311.06402v1).
   The local pivot/ball/core construction is Section 3.2. Theorem 3.7 and
   the preceding paragraphs specify weighted bucketing, insertions,
   forwarded vertex splits, and the standard deamortization of the public
   spanner. Claims 3.17--3.18 and the proof of Theorem 3.1 separate
   selected-edge recourse from the cost of maintaining the embedding.
   Algorithm 6 and Claim 4.4 give the numerical query algorithm and its
   exact-base-table implementation.

The binary-tree degree reduction used at recursive boundaries is the
standard dynamic degree reduction, also explicitly described in Section
2.6 of the public ESA 2025 paper *A Simple and Faster Algorithm for
Fully Dynamic Approximate Shortest Paths*. Its full version is
[arXiv:2408.11375v1](https://arxiv.org/html/2408.11375v1).
Section 6 below states the complete version needed here, including
positive lengths and current inventory, so no path-output strengthening
is hidden in that citation.

## 2. The public static provider has two independent parameters

Let $r\ge1$ be the CGLNPS cut-player parameter and $q\ge2$ the
number of CS21 expander-path levels. Take

$$
\phi^{-1}=2^{O(rh)},\qquad
 F_r=2^{O(U/r+r^2h)}.                                      \tag{P2}
$$

The hidden constants are uniform constants of the named constructive
algorithms. They do not depend on the input or on the selected growing
parameters. We only need $r,q\le U$ and $q^2rh=o(U)$ for the
conservative small-instance implementation used below.

### 2.1 The cut player and decomposition

CGLNPS Theorem 1.6 constructs an expanding large terminal subset with
sparsity $(\log n)^{-O(r)}$ in time
$n^{1+O(1/r)}(\log n)^{O(r^2)}$. Its cutoff is
$n^{1/r}\ge N_0$ for a fixed constant $N_0$. Theorem 5.1 gives
a balanced cut or a constant-volume expander side with conductance
$\theta/(\log m)^{O(r)}$, in time

$$
m^{1+O(1/r)}(\log m)^{O(r^2)}/\theta^2.                  \tag{P3}
$$

The ordinary balanced-cluster recursion, with
$\theta=\epsilon/(C\log(m+2))$, gives an expander decomposition
with crossing-edge budget $\epsilon m$, conductance
$\epsilon 2^{-O(rh)}$, and total construction work
$mF_r\operatorname{poly}(U)/\epsilon^2$. The recursion has
logarithmically many edge-disjoint levels. The quadratic $r^2h$
term pays for constructing the cut certificate; it need not be inserted
into the output conductance.

For a too-small call, replace $r$ by
$\min\{r,\lfloor\log(m+2)/C_0\rfloor\}$, with a constant-size
base case. This improves output conductance and keeps the work within
the master bound (P3). No small graph is padded to size $N$.

### 2.2 The terminal expander and the actual CS21 stage count

CS21 Theorem B.9 routes one terminal matching in a $\phi$-expander
using paths of length $O(U/\phi)$, edge congestion
$O(U^2/\phi^2)$, and work $m\operatorname{poly}(U)/\phi^3$.
Using CGLNPS Theorem 1.6 as the cut player in the public cut-matching
construction yields an embedded terminal expander with

$$
\text{conductance}\ge2^{-O(rh)},\quad
 \ell=\operatorname{poly}(U)/\phi,
 \quad\eta=\operatorname{poly}(U)/\phi^2,                 \tag{P4}
$$

and work $mF_r\operatorname{poly}(U,\phi^{-1})$. In (P4), the
congestion includes all $O(U)$ matching rounds; using a safe
$O(U^3/\phi^2)$ bound also agrees with the proof in CS21 B.4.3.
The factor $F_r$ controls construction, not output length or
congestion.

Use the CS21 hierarchy with nominal sizes $m^{i/q}$. Inspection of
Lemma 3.10, rather than substituting into its bundled $\gamma$, gives:

* work for one level-$i$ stage, excluding recursive lower stages:
  $m^{(i+1)/q}F_r\,2^{O(rh)}$;
* number of level-$i$ stages contained in a level-$(i+1)$ stage:
  $m^{1/q}2^{O(rh)}$.

The second assertion follows by charging child restarts to deletions,
amplified by the embedding congestion and pruning loss in (P4). It does
not contain the work used to construct the terminal expander. Multiplying
stage work by the number of stages, and summing, therefore gives

$$
mF_{\rm path},\qquad
 \log F_{\rm path}
      =O(U/q+U/r+r^2h+qrh).                               \tag{P5}
$$

In Lemma 3.11 the path-length recurrence is instead

$$
L_i\le O(U/\phi)(1+L_{i-1}).                            \tag{P6}
$$

Consequently returned simple paths have length and explicit-query work
$2^{O(qrh)}$. The final simplification of a walk takes its explicit
length and only removes occurrences.

For a fully explicit size cutoff, only run the hierarchy when
$\log(m+2)\ge Cq^2rh$, for a sufficiently large absolute constant
$C$. Then every nominal consecutive-size ratio obeys

$$
m^{1/q}\ge2^{Cqrh}\ge\Gamma^{C_1},                     \tag{P5a}
$$

after choosing constants in the prescribed order. This stronger-than-needed
gap dominates immediate embedding lengths and congestion, all
polylogarithmic maximum degrees, pruning losses, and the cut-player cutoff
on the smallest terminal set. In particular the smallest nonbase stage
has a positive allowed deletion budget. A surviving intermediate expander
has a constant fraction of its initial edge volume and maximum degree
$O(U)$, so it has enough surviving vertices to choose the next terminal
set. At the top level, the source's subdivision-edge terminals give the
same conclusion even for an initially high-degree graph. Ceilings in sizes
and integer budgets change fixed factors only.

For smaller actual instances, use expander pruning and a direct BFS for
each query. The BFS path length is still $O(U/\phi)$, since the
surviving graph is a strong $\phi/O(1)$-expander. Its query work,
however, can be as large as $2^{O(q^2rh)}$. This extra term is a
construction/work allowance, not an output-quality allowance. The
static sparsifier below makes only $m\Gamma^{O(1)}\operatorname{poly}(U)$
path calls, so it pays this fallback with one extra factor
$2^{O(q^2rh)}$. No small component is replaced by a master-sized graph.

The public pruning guarantee is used only within each generation's
allowed deletion quota. On the first request exceeding that quota,
retire all remaining vertices of that generation and stop answering
queries there. If the quota is a fixed multiple of $\phi m$, then
at that first excess request $m=O(t/\phi)$, so the entire remaining
original volume fits the same $O(t/\phi)$ pruning charge. This also
handles a quota below one. It gives the all-deletion convention needed
by the static congestion rounds, including the direct-BFS fallback;
it does not assert expansion after arbitrary uncharged deletions.

The settled implementation uses the current surviving child terminals as
the roots of each ES tree. A pruned child terminal deletes its super-source
edge, and bottom-level deletions perform pruning before recomputing the
base tree. Retired-generation callbacks are ignored. These bookkeeping
completions are required to read the source's abbreviated procedures as
a valid query interface. They add at most the already charged root and
edge deletions in a stage, and do not alter (P5)--(P6).

### 2.3 A loopless implementation of the public degree-band reduction

The statement of vdB et al.23 Theorem 8.5 is the required degree-band
interface. Its Appendix B Algorithm 5, read literally, adds $2^i$
self-loops at every vertex and starts at a maximum-degree scale.
CGLNPS Section 2 explicitly permits parallel edges but excludes
self-loops. Moreover, explicitly allocating all those artificial loops
could cost $n\Delta$ rather than $m$. The following elementary
implementation supplies the needed interface using only the public
loopless decomposition and pruning primitives. It is stated explicitly
rather than silently applying Algorithm 5 outside a source domain.

Let $n$ count the nonisolated vertices of the loopless demand graph.
Start with

$$
\ell=\max\{0,\lceil\log_2(2m/n)\rceil\},\qquad G_\ell=J.
$$

Maintain $|E(G_i)|\le2^in$. For $i>0$, decompose $G_i$
using Section 2.1 with crossing-edge budget $|E(G_i)|/4$. Initialize
public expander pruning in each nontrivial component. While a surviving
vertex has positive current degree below
$\delta_i=\phi2^i/C_b$, explicitly delete all its current incident
edges and settle the pruning output. A chosen vertex becomes isolated
and is chosen at most once in this band. Thus the number $t_i$ of
explicit deletion requests is less than $\delta_i n$.

Put every explicitly deleted edge and every initial component edge
incident to a pruned vertex into the next residual graph. Public pruning
bounds that removed initial volume by $c_{\rm pr}t_i/\phi$, for
a fixed constant $c_{\rm pr}$. If the next request would exceed a
component's allowed deletion quota, count that first excess request and
move the entire component to the residual graph. Its edge count is then
at most a fixed multiple of $t_C/\phi$, so the same charge applies.
This convention also handles a component whose positive quota is below
one. Each original edge is moved only once within this band.

Consequently, for an absolute constant $c_b$,

$$
|E(G_{i-1})|
   \le |E(G_i)|/4+c_bt_i/\phi
   \le2^in(1/4+c_b/C_b)
   \le2^{i-1}n,                                          \tag{P5b}
$$

on choosing $C_b\ge4c_b$. The retained graph $J_i$ has
nontrivial components of conductance $\Omega(\phi)$, and every
nonisolated vertex in those components has degree at least
$\phi2^i/C_b$. The residual $J_0=G_0$ has at most $n$
edges and is retained directly. Replacing $\phi$ by a smaller fixed
multiple makes the degree and conductance lower bounds use the same
parameter, as in the published interface.

The total size charged to bands is at most
$\sum_i2^in=O(m)$. Their decomposition, adjacency scanning, and
pruning therefore cost $mF_r\operatorname{poly}(U,\phi^{-1})$.
In particular there is no maximum-degree padding factor. Pruning and
path queries on a loopless multigraph may use the source's one-subdivision
representation: it is simple, has constant-factor size and conductance
loss, and retains original edge IDs when paths are projected back.

The weighted witness needed for a retained component can likewise be
constructed within the public domains. Its weights are
$w_v=\deg_{J_i}(v)/(\phi2^i)\ge1$. Because the component is
loopless, $w_v\le\sum_{u\ne v}w_u$. Put
$p_v=\lceil w_v\rceil$, create $p_v$ ports for $v$, and
apply CGLNPS Theorem 2.4 to all ports. Contract each vertex's port fiber,
discard internal edges, and replicate the remaining edges a sufficiently
large fixed number of times. Every fiber contains at most half the
ports, so its boundary gives a degree lower bound $w_v$, while the
fixed port degree gives an upper bound $O(w_v)$. The same argument
for a union of fibers gives constant conductance. Construction work is
$O(\sum_vw_v)=O(|E(J_i)|/(\phi2^i))$.

This derives the weighted-witness contract of Theorem 8.4 without
self-loop assumptions or a higher-degree allocation. It introduces no
independent $U/q$ output-quality term.

### 2.4 Feeding the oracle into the public static sparsifier

Algorithm 4 has two routing passes: witness edges into the demand graph,
and demand edges into the witness. In each pass it uses fresh expander
path structures for logarithmically many congestion-threshold rounds.
Each round's initialization and adaptive deletions cost its actual graph
size times (P5). The source's constant-progress charging uses output
path length and pruning loss, not construction time. Thus both static
passes preserve the separation in (P5).

Writing

$$
\Gamma=2^{g},\quad
 g=O(qrh),\quad
 F=2^f,\quad
 f=O(U/q+U/r+r^2h+q^2rh),                                \tag{P7}
$$

the reparameterized form of the public Theorem 8.1 is as follows.
Given an actual demand graph $J$ and an explicit ambient embedding
$\Pi:J\to H'$ with maximum path cardinality $L_0\ge1$ and
vertex congestion $C_0$, it returns $\widetilde J\subseteq J$ and
an explicit routing $\widehat\Pi:J\to\widetilde J$ with

$$
\begin{aligned}
 |E(\widetilde J)|&\le |V(J)|\Gamma\operatorname{poly}(U),\\
 \operatorname{length}(\widehat\Pi)&\le\Gamma,\\
 \operatorname{length}(\Pi\circ\widehat\Pi)&\le\Gamma L_0,\\
 \operatorname{vcong}(\Pi\circ\widehat\Pi)
    &\le\Gamma L_0\bigl(C_0+\Delta(J)\bigr).
\end{aligned}                                                   \tag{P8}
$$

Its safe work bound is

$$
|E(J)|\,F\,\Gamma^{O(1)}(L_0+1)\operatorname{poly}(U).  \tag{P9}
$$

For example, the published two-pass composition has congestion factor
$O(\gamma_{\rm ExpPath}^2\gamma_{\rm del}^2 U^2/\phi^2)$, which
fits $\Gamma$. The static proof's explicit path enumeration contributes
only fixed powers of that output factor. The conservative BFS fallback
contributes the separately charged $q^2rh$ term in (P7). It does not
raise $F$ to the number of routing rounds.

**The ambient factor $L_0$ in (P8) is retained.** Removing it is one of
the changes made by the new checkpoint provider. No such removal is used
to obtain (P1).

Parallel demand IDs and loop demands are retained as identities. A loop
has an empty route in its own demand graph and needs no metric edge in
the selected graph. For expander path calls, the standard one-subdivision
representation handles a loopless multigraph using a simple graph with
constant-factor conductance loss. Weighted witness quotas can be rounded
to ports and Theorem 2.4 applied to the ports; contracting their fibers
retains the needed constant-factor degree and conductance inequalities.
These are representation conventions, not a faster routing primitive.

## 3. Why the speculative public 5/6 calculation is not justified

The tempting substitution

$$
g=O(rh),\qquad f=O(U/r+r^2h)
$$

is valid for a cut certificate. It is not the output interface of the
public metric provider just audited. The public path oracle has a second
depth parameter $q$. Its recurrence (P6) contributes $q$ to the
quality exponent, while (P5) contributes $U/q$ to construction work.
Taking $q$ constant to remove its growing quality cost leaves a
polynomial construction overhead.

Accordingly, the claimed public 5/6 balance obtained by putting a cut
quality directly into a metric sparsifier has not been established. The
source-supported interface for this composition is (P7), and the joint
balance below gives 6/7. This audit does not rule out other public routers
or a stronger future reconstruction; it identifies the exact missing
interface in that particular 5/6 argument.

## 4. Retuning the public repair depth without a hidden work multiplier

Let $K$ be the number of touched-set repair levels in CKL Section 5.1.
Use the deterministic primitive (P8)--(P9) in place of its randomized
static primitive. This is the replacement explicitly prescribed before
vdB et al.23 Theorem 8.2.

Let $\mathcal L_j$ and $\mathcal C_j$ bound the maximum explicit
path length and vertex congestion after repairing through level $j$.
The construction and Claim 5.8 give

$$
\mathcal L_j\le O(\Gamma)(\mathcal L_{j-1}+1),
       \qquad \mathcal L_j\le\Gamma^{O(j+1)}.             \tag{P10}
$$

For congestion, follow Claim 5.7 but keep the public deterministic
ambient-path factor. The new middle route has input length at most
$\mathcal L_{j-1}+1$; the two surviving legs only add the previous
congestion. The degree of the projected demand graph is bounded by the
previous embedding congestion. Hence

$$
\mathcal C_j
   \le O(\Gamma)(\mathcal L_{j-1}+1)
                 (\mathcal C_{j-1}+\Delta),
 \qquad
 \mathcal C_j\le\Delta\,\Gamma^{O((j+1)^2)}.             \tag{P11}
$$

This is the precise source of the old $K^2g$ loss. It has not been
replaced by the new checkpoint's $Kg$ maintenance loss.

At a level-$j$ rebuilding event, the projected demand graph has vertex
set equal to the touched set $S_{j-1}$, and at most
$O(|S_{j-1}|\mathcal C_{j-1})$ demand edges. Equations (P9)--(P11)
bound the entire job by

$$
|S_{j-1}|\,\Delta F\Gamma^{O(K^2)}\operatorname{poly}(U).
                                                               \tag{P12}
$$

The number of selected edges created by the job is only
$|S_{j-1}|\Gamma\operatorname{poly}(U)$. The public clock charges
one such touched-set job to its interval of updates. Thus, with
$\rho=2^{O(U/K)}$, the selected-edge recourse is

$$
\rho\Gamma\operatorname{poly}(U),              \tag{P13}
$$

while the update work has the additional multiplier
$F\Gamma^{O(K^2)}$, and powers of input degree. **The static
construction factor $F$ occurs once in (P12).** It does not occur in
the number of touched vertices, the output edge count, or the path and
congestion recurrences.

### What happens to the printed restriction on K

The deterministic spanner theorem prints
$K=o((\log m)^{1/6}/\log\log m)$ with its fixed
$g_0=O((\log m)^{2/3}\log\log m)$. Its use guarantees that
the quantities $\Gamma^{O(K^2)}$ are subpolynomial in that input
size. The algorithms and proofs just cited impose no additional
correctness inequality involving the number $1/6$.

For the reparameterized primitive, (P10)--(P13) prove the replacement
envelope directly. It is sufficient here that $K^2g=o(U)$, where
$U$ is the global logarithmic inventory bound. At the smallest
nonbase local calls one need not claim that every overhead is
subpolynomial in that call's smaller size. It is bounded by the stated
global envelope and is explicitly paid. All actual record counts remain
polynomial in $N$.

An integer implementation uses a geometric clock with ratio
$b=\max\{2,\lceil n^{1/K}\rceil\}$, and only as many powers of
$b$ as the actual phase needs. The effective depth is at most $K$
up to an absolute endpoint convention, and the adjacent clock ratio is
$O(1+n^{1/K})$. If the nominal depth exceeds the actual logarithmic
size, this simply gives a binary clock with fewer levels. It does not
pad a small clock to $N$ updates. The changes preserve (P12)--(P13)
up to fixed factors and polynomial logarithms.

### Deamortization, lengths, and insertions

The paragraphs preceding KMG Theorem 3.7 explicitly apply the standard
batching deamortization, forward native vertex splits, add newly inserted
edges directly to the selected graph, and use length buckets. Those
operations depend on the job's output bound (P13), its repair deadline,
and its work budget (P12), separately. Multiplying the budget for a static
job by $F$ changes its allotted computation per update, not its
number of selected edges. Consequently the public selected-edge
recourse guarantee remains (P13). No deamortization of the entire APSP
composition is claimed here.

More explicitly, treat each static call in the public batching scheduler
as a job on its fixed input snapshot. Its output is buffered until the
job completes; the active routing structure never uses a partially
computed candidate. Replace its declared construction budget
$T_{\rm out}$ by $FT_{\rm out}$, and multiply the computational
budget assigned to every logical update by the same master factor $F$.
Every job then completes by the same logical-update deadline. The same
argument applies to processing a candidate's backlog: its component
operations have slowed by at most $F$, and its allotted work has
increased by $F$. Induction over job completions gives exactly the
same bound on the number of pending logical edits as in the public
schedule. The number of retained old/candidate structures, the lifetime
of old support measured in input edits, and the number of selected edges
published at a handoff are consequently unchanged.

Equivalently, simulate each unit of the original job budget by $F$
units of actual computation. A static call whose result is ready early
may keep that result buffered until the scheduled release, so no earlier
completion forces an extra handoff or an earlier new job. Only input and
completed output cross a static-call boundary in CKL Algorithm 1. This
permits the simulation even when the substituted static routine has a
different internal implementation and private intermediate graph sizes.

This is a work-budget substitution, not an assertion that the old
deadline survives after slowing only the implementation. All static
intermediate records stay private to their job. Neither they nor its
construction work are forwarded as recursive graph edits. The source
import used for the scheduler is precisely KMG's public strengthening
preceding Theorem 3.7; the $F$-budget substitution above explains why
its output-recourse analysis is unaffected by separating the two
parameters. Overall work is still charged amortized in (P18).

Weighted bucketing uses only a polynomial logarithmic number of buckets
for the length range in Section 7. Zero-length core identifications are
handled in their separate zero bucket and quotient, as in KMG; all
external and inter-level port graphs below have strictly positive
integer lengths. Insertions retained directly in a spanner are cleared
at its next full phase rebuild; their output inventory is charged to
the number of input insertions in that phase.

## 5. KMG's selected-degree repair does not multiply F into recourse

KMG's local vertex sparsifier maintains exact nearest pivots, small
strict balls, their exact distances, and the public low-stretch core
forests. Those operations cost $k^{O(1)}$ per local edit and do not
use the static metric provider. The provider only sparsifies the direct
sum of core graphs.

Claims 3.17--3.18 analyze selected-degree repair using two quantities:
the number of selected edges introduced by a spanner update, and the
degree of the original graph. The potential decrease and pile-splitting
argument use (P13), not the time needed to produce those edges. The
subsequent simulation of a vertex split by edge edits introduces another
fixed power of that selected-degree bound. With input degree fixed by
the public adapter in the next section, the complete local transcript
therefore has

$$
\log P=O(U/K+g+h),                                       \tag{P14}
$$

where $P$ bounds both the child inventory multiplier and the number
of child edits per native edit. A safe local work allowance is

$$
k^{O(1)} F\Gamma^{O(K^2)}P^{O(1)}\operatorname{poly}(U).
                                                               \tag{P15}
$$

During initialization, the cleanup potential can cause further
spanner updates. Paying all of them with the larger bound (P15) remains
valid; there is no need to reuse the particularly economical printed
initialization expression after changing its static provider.

The local pivot-to-child metric stretch is
$\Gamma^{O(K)}$. A selected child edge retains its actual parent
core-edge identity and a parent path no longer than its label. This is
the public KMG metric interface. No lifted arbitrary forest or stronger
path-output contract is needed for the numerical APSP theorem.

## 6. Public degree reduction at every recursive boundary

For every native vertex lifetime $v$, retain a permanent query handle
$q_v$. The current incidences at $v$ form the leaves of a balanced
binary tree attached to this handle. Leaves retain their incidence
identity through rotations. All connectors have length one; a native
edge of length $\ell$ becomes one leaf-to-leaf edge of length
$H\ell$, for a fixed power of two $H\ge C\log N$.

The resulting graph has maximum degree three. A native edit causes
$O(\log N)$ connector/edge edits, using only the current incidences.
Rotations allocate no new vertices; incidence insertions allocate a
constant number. Total vertex births are proportional to actual native
vertex and incidence births, and total connector lifetimes are larger
by only $O(\log N)$. Delete old connectors before inserting their
replacement so every intermediate step satisfies the degree bound.

For distinct connected vertices,

$$
d_G(u,v)\le H^{-1}d_{G'}(q_u,q_v)\le2d_G(u,v).           \tag{P16}
$$

The first inequality drops connector edges and divides real lengths
by $H$. A simple native shortest path with $b\ge1$ edges uses
$O(b\log N)$ connectors in its lift. Since native lengths are
positive integers, its native length is at least $b$, proving the
second inequality. Disconnected pairs stay disconnected, and equal
endpoints are returned as zero directly.

Use this adapter at every child boundary, not just the external graph.
Thus local selected-degree bounds do not compound as a physical input
degree through all recursive levels. Its extra logarithmic edits are
absorbed by $h$ in (P14). The native handles are fixed for their
lifetimes; when an entire recursive instance is rebuilt its private
handles are replaced atomically along with the current pivot maps.
Queries never retain a reference to a retired instance generation.

## 7. Recursive work, query cost, and arithmetic

Set $x=\log_2 k$ with $x$ larger than a sufficiently large
constant times $\log P$. Stop in an exact base case once the actual
inventory is $k^{O(1)}$. Rebuild a local instance after a constant
multiple of its current initial inventory divided by $k$ native
edits. Over that interval, its selected child has size at most
$P$ times the parent inventory divided by $k$. The size shrinks
by a factor $k/P$, so the recursive depth is

$$
d=O(U/x).                       \tag{P17}
$$

The total work to initialize a child is paid when that child is created.
On a full local replacement, creating and retiring its entire selected
inventory introduces $O(P)$ child records per native update after
amortization over the local interval. This includes initial child
records; it does not merely count later child edits.

Consequently the update recurrence has local term (P15) and multiplies
recursive work by $P^{O(1)}$, yielding

$$
\boxed{\begin{aligned}
 B_{\rm pub}
   &=O\bigl(x+f+K^2g+d(U/K+g+h)+h\bigr),\\
 a_{\rm pub}:=\log\gamma
   &=O(dKg+dh).
\end{aligned}}                                                   \tag{P18}
$$

This is an amortized public composite. It deliberately avoids the
larger $d^2$ degree multiplication in the unmodified printed KMG
hierarchy by applying the standard degree adapter at every boundary.
It does not replace any static routing primitive by a new one.

### Numerical queries

The query is the public Algorithm 6. At each recursive level it stores
one current pair of endpoints. It either reads the stored exact strict-ball
distance and finishes, or reads the two stored exact nearest-pivot legs
and passes the current pivot pair to the child. Divide the child's
answer by its stored reset scale $H$ before adding native legs.
The endpoint maps are those of the currently settled instance.

The exact base graph recomputes its distance table after each settled
update; its $k^{O(1)}$ cost belongs to (P15). A query reads one
entry of that table. It never performs a size-$k$ shortest-path
computation. Deterministic dictionaries and polynomial logarithmic
arithmetic therefore give $O(d\operatorname{poly}(U))$ query time.
The source's pivot-detour proof multiplies approximation by
$\Gamma^{O(K)}$ per level; (P16) adds a constant per reset,
giving the second line of (P18).

### Finite arithmetic and history

Each core projection multiplies the permitted largest label by at most
the local vertex bound, and each degree reset multiplies labels by
the fixed polynomial scale $H$. Thus all structural length labels
have $O(Ud)$ bits. At every nonbase invocation this is a fixed
polynomial in its logarithmic size; exact arithmetic and the number of
weighted buckets contribute only polynomial logarithms in $N$.
The static provider uses a dyadic $\phi$, integer quotas, and explicit
path occurrence lists, with the same polynomial logarithmic bit cost.

For the parameters below, all recourse, work, path, and degree factors
are $N^{o(1)}$. The internal elementary history can therefore use
a fixed polynomially larger cap such as $N^C$; its logarithm remains
$\Theta(U)$. Graphs are always allocated at their actual current
sizes. Long sequences may be handled by the usual doubling/restarting
of the master bound, charging each replacement to the elapsed history.

## 8. The joint 6/7 balance

Let

$$
t=\Theta((U/h)^{1/7}),\qquad
 q=r=\Theta(t),\qquad K=\Theta(t^2),
 \qquad x=\Theta(U/t),\quad d=O(t).                      \tag{P19}
$$

Round parameters to integers and choose the fixed constant in $x$
large enough for shrink. For the finitely many small values of $N$,
use the exact base algorithm. Since $U=t^7h$ up to fixed factors,

$$
\begin{array}{c|c}
\text{quantity}&\text{logarithmic bound}\\ \hline
g& O(t^2h)\\
f& O(U/t+t^3h)\\
K^2g& O(t^6h)=O(U/t)\\
dU/K& O(U/t)\\
dg& O(t^3h)\\
dKg& O(t^5h).
\end{array}                                                    \tag{P20}
$$

It follows that

$$
B_{\rm pub}=O(U/t)=O(U^{6/7}h^{1/7}),\qquad
 a_{\rm pub}=O(t^5h)=O(U^{5/7}h^{2/7}),                  \tag{P21}
$$

as claimed. Moreover
$x/(U/K)=\Theta(t)\to\infty$,
$x/g=\Theta(t^4)\to\infty$,
$q^2rh=o(U)$, and $K^2g=o(U)$, verifying the conditions used
above. The proposed $K$ exceeds the fixed-$g_0$ theorem's printed
range, which is why Section 4's source-level rederivation is essential.

For orientation, within the fixed-power envelope (P18), ignoring
polylogarithmic factors, a budget $B=U^\sigma$ forces
$q,r,d\ge U^{1-\sigma}$, and $dU/K\le B$ forces
$K\ge U^{2(1-\sigma)}$. Therefore $K^2qr\le B$ forces
$6(1-\sigma)\le\sigma$, or $\sigma\ge6/7$.
This only explains the balance inside this particular charged envelope;
it is not a lower bound for deterministic APSP.

## 9. Consequences for the current comparisons

The previous derived public comparison used KMG's fixed static output
factor $g_0=O(U^{2/3}h)$, then retuned only the outer parameters and
degree adapter. That yielded $59/63$ update exponent at the displayed
$6/7$ stretch scale. The present source-level joint retuning is stronger
and should replace that value in a comparison claiming to include the
currently checked joint public composition.

The new research APSP point remains
$\exp O(U^{11/14})$ amortized update work at stretch
$\exp O(U^{6/7}h)$. Compared at this allowed stretch scale, the
checked public composite is now (P1), not merely the printed
$\exp O(U^{20/21}h)$ theorem or the earlier $59/63$ composite.
The difference comes from two substantive changes in the research engine:
its new static router has $g=O((p+r)h)$, and its normalized ambient
repair changes the local quadratic depth loss into a linear one.

An equal-stretch comparison is also available. The public point (P1)
has stretch exponent $U^{5/7}h^{2/7}$. Set
$t_{\rm new}=\Theta((U/h)^{5/28})$ in the new curve
$B_{\rm new}=O(U/t_{\rm new}+t_{\rm new}^3h)$,
$a_{\rm new}=O(t_{\rm new}^4h)$. This gives

$$
B_{\rm new}=O(U^{23/28}h^{5/28}),\qquad
 a_{\rm new}=O(U^{5/7}h^{2/7}),                           \tag{P22}
$$

so the new construction also improves the checked public update envelope
at that finer allowed stretch. More generally, the public balanced family
has $B_{\rm pub}=O(U/t+t^6h)$, $a_{\rm pub}=O(t^5h)$, while
the research family has $B_{\rm new}=O(U/t+t^3h)$,
$a_{\rm new}=O(t^4h)$. These are separate time/stretch curves; their
parameters should not be equated when claiming equal approximation.

This audit makes no automatic change to the strong-forest or Gomory--Hu
comparison. Those interfaces require additional forest lifting, stable
canonical maps, cover/hopset recourse, and an outer scale constraint.
They need their own joint rederivation. It also makes no ordinary
output-sensitive simple-path claim and no new exact-matching exponent.

No already delivered immutable checkpoint archive is modified by this
baseline correction.
