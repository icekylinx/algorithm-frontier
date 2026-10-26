# A conditional 14/15 quantitative bound for deterministic general matching

**Separate complete mathematical candidate, 24 October 2026.** This note
composes the degree-reset distance backend with exact recovery from
near-feasible circulations. It leaves all frozen 335/336, 209/210, and
167/168 constructions unchanged. Under the named constructive interfaces,
one uniform deterministic program finds an explicit maximum-cardinality
matching in every undirected general graph in time

$$
O(n+m)+(m_s+1)\exp\!\left(
 O\!\left((\log(m_s+2))^{14/15}
             (\log\log(m_s+4))^{1/5}\right)\right).
 \tag{1}
$$

Here $m$ counts input edge records and $m_s$ counts distinct
nonloop edges. The bound has no perfect-matching promise, density
restriction, or approximation error. It is a research proof assembly
with explicit public primitive dependencies, not an implementation or
external certification. The independent final verifier proves accepted
output correctness; the improved time additionally requires the
fast-branch proof given here.

## 1. Complete dependency boundary

The matching state and reduction are specified in:

* [Exact general-graph gap reduction](general-graph-gap-reduction.md).
* [Algorithm and transaction outline](matching-algorithm-specification.md).
* [Factor-critical contraction witnesses](factor-critical-contractions.md).
* [Ledger algebra and physical phase budget](ledger-algebra-and-phase-budget.md).
* [Persistent actual integral carriers](persistent-integral-ledger-carrier.md).
* [Deterministic small tight-set discovery](deterministic-local-tight-discovery.md),
  [local balanced pair queries](balanced-forest-pair-oracle.md), and
  [descending-level exchanges](static-pair-exchange.md).

The complete numerical route used in THIS composition is:

* [Degree-three reset between distance levels](distance-degree-reset-candidate.md).
* [Distance raw lifting and retained-edge gauge correction](distance-oracle-raw-lift.md).
* [Disconnected-component routing](disconnected-component-backend-wrapper.md).
* [Numerical occurrence lifetime and query transactions](numerical-backend-lifetime-and-loops.md).
* [Priced logarithmic client](priced-logarithmic-steps-from-raw-cycles.md).
* [Near-feasible rounding and exact projection](near-feasible-rounding-and-exact-projection.md).

The region and lock construction is the one in
[local exact projection](local-exact-projection-from-priced-steps.md),
but ALL its static exact-flow checks and recovery calls are replaced
by the new rounding construction. Level-one global exchange uses the
all-expanded version of that construction. Consequently this composition
has no separate exact-flow factor with logarithmic exponent 17/18.

The source-specific numerical primitives remain the constructive local
KMPG and DO26 interfaces, including their selected-edge transcript,
weighted future-path forests, native split processing, and deterministic
spanner. Their primary references and exact scope are recorded in the
degree-reset note. The full DO26 growing-depth theorem is not being
substituted for the recurrences below. Its old squared maximum-degree
recurrence is avoided by a genuine degree-three input between levels.

## 2. Literal master parameters for a numerical branch

Let $S_b=2^U$, with integer $U$, be a backend master bound.
An actual root has at most $S_b^2$ records and root integer
lengths/gradients of at most $c_0U$ bits for one fixed absolute
$c_0$, for example $c_0=1200$. Use positive integer branch
constants $c_C,c_E$. Define

$$
\begin{split}
 L_U&=\lceil\log_2(U+4)\rceil,\qquad r_U=\lceil L_U^{1/5}\rceil,\\
 K&=\max\left\{1,
       \left\lfloor\frac{\lfloor U^{2/15}\rfloor}{r_U^2}
       \right\rfloor\right\},\\
 h_k&=\lceil U^{14/15}\rceil r_U,\qquad k=2^{h_k},\\
 h_C&=c_C\left(\left\lceil\frac UK\right\rceil
       +\lceil U^{2/3}\rceil L_U+L_U\right),\qquad C_p=2^{h_C},\\
 \gamma_*&=2^{c_C\lceil U^{2/3}\rceil L_U},\qquad P_*=C_p^{16},\\
 H_p&=2^{\lceil\log_2(4(h_C+1))\rceil},\\
 d_*&=\left\lceil\frac{8U}{h_k}\right\rceil+10,\qquad
 b_*=(c_0+100)U(d_*+1).
 \end{split}
 \tag{2}
$$

Rational powers are rounded by integer power comparisons. The
numerical port symbols $C_p,H_p$ are separate from the matching
floor $C=a+1$. Use the computable common backend cap

$$
E_*=k^{c_E}\gamma_*^{c_EK^2}
       C_p^{c_E(d_*+1)}(U+4)^{c_E(d_*+1)}.
 \tag{3}
$$

An adequate fixed $c_C$, followed by an adequate fixed $c_E$,
bounds the source and reset construction. The program checks selected
degrees, emitted-record prefixes, resident sizes, stored bit lengths,
and charged operations against these declared caps. A failure suspends
the branch. Resource checks are not finite-size quality certificates.

The bit cap $b_*$ is fixed for each source invocation's whole
life and for its length/radius buckets. It is not increased after an
observed edge becomes longer. An active instance of size at most
$24k$ uses the direct base solver. Before nonbase recursion,
let $e_0$ be its initial ACTIVE edge count and
$v_0=\lfloor\log_2\max\{2,e_0\}\rfloor$, and check

$$
K\ge2,\qquad K^7\le v_0,\qquad b_*\le v_0^2,
 \qquad P_*^2\le k/16.
 \tag{4}
$$

The active-isolate adapter of the degree-reset note is part of this
contract. Private physical isolates are initialized once and touched
only on their own events; they are not counted as fictitious edges
and are not rescanned on active-source restarts. Actual port trees,
including inactive resident ghost trees, remain counted child input.
A temporary source activation generation does not create a second
external port fiber for the same actual parent vertex lifetime. More
precisely, each source period starts on the maintained nonisolated
endpoint list, keeps newly isolated native slots until that period is
discarded, and reuses the SAME source generation and external fiber on
reactivation. No mid-period source-vertex deletion is needed. An actual
parent-lifetime deletion leaves only a counted inactive tombstone after
real-record retirement and export suppression; a new actual lifetime
gets a different identity. The period's elementary-edit allowance
$Q\le m_{\rm act}/(12k)$ bounds the additional resident slots and
the change in edge count, so its resident size remains within a constant
factor of its initial active size. Disposal scans only this bounded
period history and its descendant records, never the private historical
isolate inventory.

### The smaller selected-edge envelope

For a degree-three parent, the selected degree, fully encoded
birth/recourse, and STABLE CORE forest F_i change envelopes have logarithm

$$
O\!\left(U/K+U^{2/3}L_U\right).
 \tag{5}
$$

Adequate fixed $c_C$ makes $C_p$ cover them. The port trees,
per-occurrence pool indices and their explicit metadata add fixed
powers, covered by $P_*=C_p^{16}$ as in the reset lemma.

The source's $\gamma^{O(K^2)}$ demand-route re-embedding work is
LOCAL work. It does not replace unchanged retained child edges.
A retained child edge uses its own physical core-edge provenance and
corrected root-leg gradient. Genuine endpoint/price/provenance changes
are in the smaller selected-edge transcript. Forwarding every changed
demand route as a recursive edge edit would invalidate this separation
and the exponent proved below.
The separate nearest-pivot shortest-path forest can have
$\widetilde O(k)$ changes per input edit; its local candidate work
is included in $W$, not in this smaller recursive envelope.

## 3. Recursion, aspect and the backend contract

Let $G_r$ be occurrence multiplicity, $J_r$ initialization
work per active nominal record, and $T_r$ amortized work per
external edit/query with $r$ remaining levels. The reset gives

$$
\begin{split}
 G_r&\le P(G_{r-1}+1),\\
 J_r&\le W+P(G_{r-1}+1)+(P/k)J_{r-1},\\
 T_r&\le P T_{r-1}
       +O\!\left(kW+kP(G_{r-1}+1)+P J_{r-1}\right),
 \end{split}
 \tag{6}
$$

where $P\le P_*$ eventually and
$W=k^{O(1)}C_p^{O(1)}\gamma_*^{O(K^2)}\operatorname{poly}(U)$.
The exponents denoted $O(1)$ are absolute implementation constants,
independent of depth and $K$; an adequate $c_E$ covers them.

At active nonbase size $m>24k$, the period is
$\lfloor m/(12k)\rfloor$. Degree three implies
$m=n+e\le5n/2$, so this is within the literal $n/k$ source
horizon. Active edges and vertices are comparable up to constants
through the period; this is supplied by the isolate adapter. Current
level initialization AND complete retirement are included in (6).

The child-input size, including ghost slots and all born port trees,
is at most $mP/k$. Equation (4) gives shrink by at least
$\sqrt{k}$ up to the absorbed constant. A root of size
$m\le S_b^2$ therefore has depth

$$
d=O(U/h_k)=O(U^{1/15}L_U^{-1/5})<d_*.
 \tag{7}
$$

The flat lift assigns a distinct same-index parent-tree copy to EACH
child occurrence over ANY port of a logical root. Its factor is
$\lambda C_p(G+1)$, within $P(G+1)$. A child forest-edge
log changes one attachment and does not rebuild its long parent
tree. Common observed capacity doubling charges dormant pool copies
to initialization/restarts. No extra $k$ multiplies each recursive
edit. Private isolates likewise have no repeated active-restart scan.

Solving (6), including polynomial direct base queries, gives

$$
\log E=O(h_k+K^2\log\gamma_*+d\log C_p).
 \tag{8}
$$

The large local $\gamma_*^{O(K^2)}$ factor occurs once in this
bound; it is not raised to depth. Raw quality and piece count obey the
same envelope. Their per-level $\gamma_*^{O(K)}$ factor fits a
fixed power of $C_p$, since $K^2U^{2/3}L_U=o(U)$.

The rounded parameters satisfy

$$
\begin{split}
 K&=\Theta(U^{2/15}L_U^{-2/5}),\qquad
 h_k=\Theta(U^{14/15}L_U^{1/5}),\\
 K^2\log\gamma_*&=O_{c_C}(U^{14/15}L_U^{1/5}),\\
 d\log C_p&=O_{c_C}(U^{14/15}L_U^{1/5}).
 \end{split}
 \tag{9}
$$

The dominant term in the last line is $(U/h_k)(U/K)$.
Thus (3) covers the complete backend with

$$
E\le E_*=
 \exp\!\left(O_{c_C,c_E}(U^{14/15}L_U^{1/5})\right).
 \tag{10}
$$

This includes actual-size initialization, amortized edits/queries and
logs, inverse raw quality, pieces, occurrences and full retirement.
No initialization allocates $k$ or $S_b$ records for a tiny
root. Charged local restarts support a polynomial master history,
such as $S_b^{200}$, rather than requiring one tiny primitive
instance to endure that entire history.

### Internal length and gradient bits

The integer stable-core labels and the port scale give

$$
L_{i+1}\le O(n_i\log^2(n_i+2))H_p L_i.
 \tag{11}
$$

Each level adds $O(U)$ bits. Frozen gradient potentials and the
corrected retained-edge gradients have the same additive bound.
Consequently

$$
b_{\rm internal}=O(U(d_*+1))
       =O(U^{16/15}L_U^{-1/5}+U).
 \tag{12}
$$

The declared $b_*$ covers this eventually. Every nonbase source
has $b_*\le v_0^2$, a literal quasipolynomial aspect in its
OWN edge count. Its future-path forest count is
$O(\log m+\log k+b_*)$, polynomial in $U$; no
polynomial-length shorthand is used. Moreover

$$
K^7/h_k=O(L_U^{-3})\longrightarrow0.
 \tag{13}
$$

The active-size adapter gives $v_0=\log_2m-O(1)$, so (4)
holds eventually at the smallest nonbase size. Since
$K^7\le\log m$ implies
$K\log\log m/(\log m)^{1/6}\to0$, the source's spanner
parameter condition is checked at every local scale.

### Root certificates have O(log S) bits

An inherited abstract upper certificate need not have short encoding.
Instead evaluate the returned list on the exposed ROOT occurrence
forest. Each of its edges maps to one root input edge or true null.
Path aggregates give the exact root gradient and literal root length
$V$. Pieces have unit signed coefficients; repeated traversals
are counted with their multiplicity, before any cancellation. There are at most $E_*$
pieces and $ME_*$ root forest records, hence

$$
V\le M E_*^2\max_e\ell_e.
 \tag{14}
$$

The root numerator $\Gamma$ satisfies the analogous
$\lvert\Gamma\rvert\le ME_*^2\max_e\lvert g_e\rvert$.
The length is no larger than the inherited raw certificate, so quality only
improves. Under the outer caps below it has polynomial master magnitude
and $O(s)$ bits. Internal metric arithmetic still has the charged
multiword cost (12); no unbounded real or integer operation is unit cost.

## 4. The outer parameter and uniform absorptions

Let the subcubic physical graph have order at most $S=2^s$, with
one fixed $s$ throughout the gap driver. Invoke the backend with
$U=2s$. For a third positive integer branch constant $c_B$, put

$$
\begin{split}
 L_s&=\lceil\log_2(s+4)\rceil,\qquad r_s=\lceil L_s^{1/5}\rceil,\\
 a&=\left\lfloor\frac{\lfloor s^{1/15}\rfloor}{c_Br_s}\right\rfloor,\\
 v&=\lceil s/a\rceil,\qquad B=2^v,\qquad
 q=B^{-100},\qquad D_*=B^{10}.
 \end{split}
 \tag{15}
$$

Suspend before dividing by $a$ if $a<1000$. For any fixed
$c_B$, eventually

$$
a=\Theta_{c_B}(s^{1/15}L_s^{-1/5}),\qquad
 v=\Theta(c_Bs^{14/15}L_s^{1/5}).
 \tag{16}
$$

After fixing adequate $c_C,c_E$, a sufficiently large FIXED
$c_B$ makes (10), including $U=2s$, imply

$$
E_*\le B/4.
 \tag{17}
$$

The branch checks this literal inequality using (3). It need not know
an analytical leading constant. It is stronger than the priced
client's slack requirement between raw pieces/occurrences/inverse
quality and $D_*$.

All remaining outer overheads are strictly smaller:

$$
a=o(v),\qquad a^2=o(v),\qquad
 \operatorname{poly}(a,s)=2^{o(v)},\qquad v=o(s).
 \tag{18}
$$

In particular $B^a\in[S,2^aS)$. Rounding nominal numerical
sizes to the prescribed $2^{2a^2}$ grid costs only $2^{o(v)}$.
For a higher reset, its parent-debt bound gives local lifetime
$R+B\le O((a+3)2^aS/B)=o(S)$ in the worst case. Top nominal
size $SB$, all smaller actual local instances, and their rounded
capacities have $M\le S^2$ eventually. Thus master $U=2s$
has ample size and history headroom without a master-sized allocation.

Numerical root prices have $O(s)$ bits under the existing explicit
$S^{1122}$ price bound. Equation (14), with $M\le S^2$ and
$E_*\le B/4=S^{o(1)}$, gives polynomial root certificate
magnitude. Internal fields in (12) use only $\operatorname{poly}(s)$
ordinary $\Theta(s)$-bit words. Their fixed polynomial arithmetic
cost is absorbed by (18).

The dyadic grids, step sizes, pad sizes and positivity services are
unchanged. The executable guards $q\ge S^{-1}$,
$D_*\le S^2$, and the stronger initial size conditions hold
eventually since $v=o(s)$. The master bound is used in these
caps; a tiny local instance is not assigned a separate local
$M^{10/a}$ occurrence cap.

## 5. Local and global exact recovery

The local threshold proof has absolute constants: ordinary capacities
are scaled by 16, $W=20000(P+1)$, and fewer than $1000(P+1)$
ordinary arcs are ever represented. Objective range and all
insertion/lock losses are $O((P+1)s)$, so

$$
J_{\rm local}=O((P+1)B^{200}s).
 \tag{19}
$$

Genuine motion notifications are $O(D_*J_{\rm local})$.
Their client responses and the separately counted external requests
do not recursively create new motion credit. The priced proof pays
full occurrence sweeps and their $D_*^2$ cost. Substitution of
(17) into its explicit counts bounds numerical work by

$$
(P+B)2^{2a^2}B^{230}\operatorname{poly}(s).
$$

Near-feasible rounding adds $O(P)$ exact coordinate reads and
$\widetilde O(P)$ dynamic-tree work per completed recovery.
The $O(s)$ threshold count is absorbed by (18). A complete local
projection therefore has the safe bound

$$
T_{\rm local}\le(P+B)B^{250}.
 \tag{20}
$$

Exact recovery does not solve a fresh max-flow problem on the union.
A true success rounds to an integral flow of exactly its threshold
value. At the final optimistic LOW threshold $v+1$, the return
coordinate is greater than $16v-8$. Dropping locks and dividing
by 16 leaves total integral-bound violation below one. Penalty-based
rounding yields an exact optimistic maximum $v$ and a checked
minimum cut. The true flow and that cut certify the full maximum;
ordinary residual search on the deduplicated union gives the COMPLETE
full peel. Intermediate LOW answers are provisional. Wrong ones
cannot pass the final exact flow/cut checks. All residual graphs
omit the numerical return arc.

At level one, use the all-expanded version on the $O(S)$-record
exchange graph with $W=20000(M+1)$. It has the same
$(M+B)B^{250}$ bound. For a general directed invocation, first
remove ordinary arcs entering the source, leaving the sink, and loops;
this ensures the return lower bound and preserves maximum value.
The matching exchange network already has this terminal orientation.

All capacities and threshold arguments lie in the fixed master
envelope of the priced client. Arbitrarily encoded general capacities
can instead use the separate capacity-digit reduction. The matching
composition needs only its polynomial-master capacities.

There is no $s^{17/18}$ overhead to absorb into (16): every reset
uses this priced client, explicit integral rounding, and residual
reachability.

## 6. Phase counts, reset sum and complete matching time

The combinatorial/debt proof has explicit dependence on $a$.
For $C=a+1$, target $1\le K\le N$,
$L=\lceil10000CN/K\rceil$, and
$g_*=\max\{1,\lfloor K/(100C)\rfloor\}$,

$$
Lg_*\le10001CN,\qquad \tau=O(aS),\qquad
 T_{\rm structural}=a^2S\operatorname{poly}(s).
 \tag{21}
$$

One frozen injection plus a sparse overlay is used throughout each
structural/reset transaction. A new canonical carrier assignment is
published only after settlement. Physical erased volume, contractions
and sparse supports are charged without a global explicit assignment
rewrite after every carrier pivot.

At the top, structural objective losses and bounded range give
$J_{\rm top}=O(aSB^{200}s^2)$. Notifications, exact cached
residual access and complete sweeps bound all top numerical work by
$SB^{240}$ eventually.

Put $b_j=B^{a-j}$. For a higher reset, including a gain that
jumps many finer periods, the unreset parent's debt is at most
$(C+2)b_{j-1}$. Hence

$$
\sum_{j=2}^{a}\frac{\tau}{b_j}
       [(C+2)b_{j-1}+B]=O(a^3SB).
 \tag{22}
$$

Multiply this sum once by $B^{250}$. Costs are added over
levels, not compounded through the ledger hierarchy. Sparse support
application and persistent normalization fit
$O(a^3SB^{251})$.

At level one, $b_1=B^{a-1}\ge S/B$. There are at most
$O(aB+1)$ global resets. The NEW all-expanded flow cost gives

$$
O(aB+1)(S+B)B^{250}\le SB^{252}
 \tag{23}
$$

eventually. Initialization, last incomplete attempts and phase
materialization remain within these envelopes. From (18)--(23),

$$
T_{\rm phase}\le SB^{300}.
 \tag{24}
$$

The bound holds on every input and every valid prefix, including LOW
exits. No perfect-matching hypothesis enters the cost accounting.

The direct gap driver maintains
$\nu(J)-|Q|\le U_0\le\lfloor N/2\rfloor-|Q|$, chooses
$K=\lceil U_0/2\rceil$, and updates this bound after gains or
the generalized LOW conclusion. There are $O(a\log(N+2))$
phases, including the final $O(a)$ small-gap steps. Equation (18)
absorbs that count. A complete favorable branch has time

$$
SB^{320}
 =S\exp\!\left(O_{c_C,c_E,c_B}(s^{14/15}L_s^{1/5})\right).
 \tag{25}
$$

## 7. First-failure proof and one uniform program

Retain the explicit initial, magnitude and history guards of the
priced client and phase proof. A failed guard suspends the branch;
it never returns an optimum certificate. They include $a\ge1000$,
$100000(a+1)\le S^{1/20}$, $B\le S^{1/20}$,
$q\ge S^{-1}$, $S^{20}$ main-action/threshold caps, and
$S^{100}$ external-operation caps, together with (4), (17) and
the literal recursive degree/bit/size budgets.

Argue at the first attempted guard violation. The loose prefix guards
first bound positivity and pad changes, before using a sharp time
theorem. They give small total violation and valid region bounds.
These give (19), the notification count, rounding prerequisites and
(20). Structural/debt identities then give (21)--(23), and (24)
applies to the prefix INCLUDING its last attempted operation. All
these quantities are $S^{1+o(1)}$ or smaller and lie below their
loose polynomial guards eventually. Recursive source caps follow
independently from (6)--(13). An adequate fixed branch therefore
cannot have a first guard failure beyond one fixed input-size threshold.

Internal arithmetic, memory allocation, pool growth, dynamic trees,
coordinate reads and rounding are charged physical-word instructions.
Memory addresses have polynomial master magnitude on guarded histories.
Large integer operations use ordinary digit arithmetic. No branch
can monopolize execution through a nominally single unbounded-cost
operation.

Enumerate all positive integer triples $(c_C,c_E,c_B)$, for
example by sum and then lexicographic order. Give one classical
deterministic exact general-matching algorithm a fixed positive
instruction share. Give branch number $j$ a share at least a
fixed multiple of $2^{-j}$, using a computable binary-counter
interleaving. Instantiate a branch only when it first receives work.
Branches have private mutable state and share the compact immutable
input.

Decode every proposal, check it as a matching of that compact original
graph, and perform one deterministic exact augmenting-path search
before acceptance, using
[classical matching verification](classical-matching-optimality-verifier.md).
All verification work is charged WITHIN the proposing branch's share.
A rejected or malformed proposal suspends that branch. The classical
branch supplies termination on every finite input.

There exist an adequate fixed $c_C$, then an adequate fixed
$c_E$, then an adequate fixed $c_B$, for which all displayed
source and client bounds hold eventually. Their triple has one finite
index $j_*$, independent of input. Its share penalty
$2^{j_*}$ is a constant. Counter/interleaving overhead is
polynomial in logarithms and is absorbed by (25). Finitely many
exceptional compact sizes are covered by enlarging the final absolute
constant for the always-running classical branch. The program does
not need to know that threshold.

The verifier and classical branch prove sound output and termination
even for an inadequate numerical tuple. The improved time uses the
existence and correctness of a favorable branch; verification is not
a substitute for that proof.

## 8. Arbitrary graphs and the optional matching-size kernel

One linear input scan removes loops, coalesces parallel copies while
retaining original IDs, drops isolates and compacts the graph. The
odd-path reduction replaces each degree-d vertex by $2d-1$
vertices, producing a subcubic graph with
$N=4m_s-r=O(m_s)$ and optimum offset $A=2m_s-r$.
Every maximum auxiliary matching, including noncanonical gadget
matchings, decodes linearly to an original maximum matching. The
decoder is the arbitrary-matching proof in the gap-reduction note;
it does not assume one external port per gadget.

Choose $S$ as the next power of two above a fixed constant and
this $N$. The empty-edge case returns immediately. Then
$S=\Theta(m_s+1)$, so (25) gives (1). All portfolio branches
and verifiers operate on compact records. The original $O(n+m)$
scan and winning original-ID translation are not repeated per branch.

Optionally apply the exact
[vertex-cover matching kernel](matching-size-kernel-corollary.md).
If $\nu$ is the original matching number, its computable greedy
cover keeps a graph with

$$
m'\le\min\{m_s,O(\nu^2)\}.
$$

Apply the SAME algorithm and parameter choice to its actual compact
size. This gives

$$
O(n+m)+(m'+1)\exp\!\left(
 O\!\left((\log(m'+2))^{14/15}
             (\log\log(m'+4))^{1/5}\right)\right).
 \tag{26}
$$

No knowledge of $\nu$ is needed to build the kernel. No special
graph family is introduced. Both conclusions remain conditional on
the complete constructive numerical and state interfaces in Section 1.
