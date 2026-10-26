# A binary ledger hierarchy independent of numerical accuracy

**Separate mathematical refinement, 24 October 2026.** This note changes
the parameterization of the matching phase, leaving all frozen
quantitative constructions unchanged. The ledger hierarchy needs only
a geometric sequence of reset periods and adjacent residual floors
differing by one. Its branching ratio need not bound the numerical
backend's cost, multiplicity, or inverse approximation quality.

We prove the structural and allocation statements directly, with
explicit dependence on the number of levels. We then combine them with
the independently specified [decoupled numerical client](decoupled-numerical-client.md).
The resulting conclusion remains conditional on the complete raw-cycle
backend, persistent-carrier, local-pair, and physical-lifetime interfaces.
An eventual fast-time bound is not inferred from final output verification.

The underlying matching-state equations and local projection are from
[OAI Sections 3--5](https://github.com/openai/math/tree/main/preprints/Almost-Linear-Time-Maximum-Cardinality-Matching-in-Sparse-General-Graphs-September-24-2026).
The explicit component proofs used here are
[ledger algebra](ledger-algebra-and-phase-budget.md),
[local exact projection](local-exact-projection-from-priced-steps.md),
[near-feasible rounding and exact recovery](near-feasible-rounding-and-exact-projection.md),
[persistent integral carriers](persistent-integral-ledger-carrier.md),
and [the general-graph gap driver](general-graph-gap-reduction.md).
Their former fixed-parameter running-time conclusions are not premises
of this calculation.

## 1. Parameters and conditional numerical contract

Let a subcubic physical graph have order $N$, and choose the one
master size $S=2^s$ with $N\le S<2N$, outside bounded empty
cases. For every phase use

$$
a=s,\qquad C=s+1,\qquad B_{\rm ledger}=2,\qquad
 c_j=C-j,\qquad b_j=2^{s-j}\quad(0\le j\le s).
 \tag{1}
$$

Thus $b_0=S$, $b_1=S/2$, $b_s=1$, and the bottom
floor is $c_s=1$. There are $s+1$ ledgers. All these
integers have $O(s)$ bits and are computed exactly. Retain

$$
\delta=S^{-1000},\qquad \varepsilon=S^{-3000},
 \qquad H_{\rm price}=S^{100}.
 \tag{2}
$$

Let a complete master-controlled raw backend have a computable cap
$E_*\ge1$ for initialization per actual input record, update/query
cost, complete logs, occurrence multiplicity, pieces, and inverse raw
quality. It accepts the specified $O(s)$-bit root prices, actual
nominal sizes at most $S^2$, and polynomial master lifetimes.
Its full numerical-lifetime contract is retained. Define

$$
D=2^{\lceil\log_2\max\{16,4E_*\}\rceil},
 \qquad q=\frac1{16D}.
 \tag{3}
$$

The explicit cap may be rounded upward before (3). Both $D$ and
$q^{-1}$ are powers of two. Check $q\ge S^{-1}$,
$D\le S^2$, and all remaining numerical prerequisites. For any
favorable fixed backend constants with $E_*=S^{o(1)}$, these
checks eventually hold. In particular

$$
q<1/100,\qquad \frac1{4D}>2q,
 \qquad E_*\le D/4.
 \tag{4}
$$

For an actual numerical lifetime $R$, use only ordinary
power-of-two rounding

$$
M=2^{\lceil\log_2(16(R+2))\rceil},
 \qquad 16(R+2)\le M<32(R+2).
 \tag{5}
$$

There is no divisibility requirement by $2a^2$. The root integer
price cap is stated in the master form $S^{1200}$, rather than
deduced from a local power $M^{1200a}$. The backend is run at
master logarithmic parameter $2s$; this does not allocate an
$S$-sized array for a small local instance.

The decoupled client proves the following useful uniform cost form.
If $J$ is the number of accepted steps and $Q$ counts requests
from its owning client, including failed and LOW queries but excluding
internal refresh work, then

$$
T_{\rm priced}
 \le O(MD+QD+D^2J)\operatorname{poly}(s).
 \tag{6}
$$

The $D^2J$ term includes full copy sweeps. The polynomial has a
fixed exponent. Longer internal backend words are charged in its cap
and in this polynomial; unbounded-word unit-cost arithmetic is not used.

## 2. Exact state invariants do not require a small number of levels

For a phase target $1\le K\le N$, define

$$
L=\left\lceil\frac{10000CN}{K}\right\rceil,
 \qquad g_* =\max\left\{1,
                 \left\lfloor\frac K{100C}\right\rfloor\right\}.
 \tag{7}
$$

The impossible-target precheck in the gap driver may return LOW before
initialization. Every initialized phase satisfies $L>C$, so its
singleton top slacks are positive. Integral levels satisfy

$$
\sum_{e\text{ at row }r}x^j_e=L,\qquad
 y^j_d=L-\operatorname{load}^j(d),\qquad
 y^j_d+p^j_d\ge c_jw_d,
 \qquad x^j,p^j\ge0.
 \tag{8}
$$

The bottom has zero debt at settled states. These are coordinatewise
algebraic statements for every $j$; they do not contain $B$,
$q$, or a requirement that $a$ be fixed. A tight contraction
adds bin weights, residuals and debts. An expansion adds debt at most
$c_j\le C$ at each integral level. A preserving deletion of bins
$R$, under the fixed injection for that event, changes the total
debt of a floor-$c$ ledger by at most

$$
Lh(R)-cw(R).
 \tag{9}
$$

A projection from floor $c+1$ to floor $c$ either produces
a zero-debt child or a full residual peel satisfying
$Lh(R)<cw(R)$. Equation (9) then decreases the debt of every
preserved coarser ledger by at least $w(R)$. The adjacent-floor
difference is exactly one in (1), as required. The target floor is
always positive, including the last projection with $c=1$.

Persistent transportation pivots preserve row sums and column loads.
They therefore preserve (8)--(9), independently at all $s$ integral
levels. A projection reads one immutable parent, writes a separate
child, and then normalizes that child. Sharing its roots with deeper
fresh ledgers does not scan the old bottom allocation. Applying one
structural batch to all preserved levels contributes a factor at most
$s$, not a product of costs across levels.

The frozen injection/overlay is retained throughout each deletion,
contraction and its projection transactions. A later canonical
assignment switch uses the existing carrier construction. Increasing
the number of ledgers changes neither that transaction order nor the
factor-critical physical witnesses.

## 3. Uniform structural, debt, and physical-size bounds

The choice (7) gives the explicit inequality

$$
Lg_*\le10001CN.
 \tag{10}
$$

If $K\ge100C$, use $g_*\le K/(100C)$ and the ceiling
bound for $L$; in fact $Lg_*\le101N$. If $K<100C$,
then $g_*=1$ and $L\le10000CN+1$. Thus small targets do
not require a separate unproved progress rule. There is no repaired
gain or positive-weight peel before the one terminal gain in that case.

Before the terminal gain, the top debt pays all peeled weight:

$$
\sum_{\rm peels}w(R)
       \le2L(g_*-1)+S^{-800}.
 \tag{11}
$$

The strict blocker inequality and integrality give at most
$2C(g_*-1)$ blockers, provided the checked inequality
$CS^{-800}/L<1$ holds. It holds with very large slack when
$C=s+1$. No fixed-$a$ constant is used in this rounding.

The materialized physical volume of a peel is at most $2w(R)$,
and the two bins of a gain have total weight at most $2L$.
Counting initial physical vertices, reentries from the paired remainder,
expansions and contraction arities therefore gives absolute bounds

$$
\text{physical erasures, expansions, total contraction arity}
                 =O(CN),\qquad \tau=O(CN)=O(sS).
 \tag{12}
$$

Here expansions and contractions add one tick, repaired gains add
$L$, and peels add none. The terminal gain ends the phase without
repairing obsolete ledgers. Local pair work is charged to the returned
tight-set arity or to the two $O(L)$ selected components immediately
consumed by a gain. It is included in (10)--(12).

Retaining the largest bin at contraction moves a physical vertex at
most $O(\log S)$ times in each stay. There are $O(CN)$
stays and row absorptions. Since physical degree is at most three,
total changed physical incidence records are $O(CNs)$. Processing
them at all integral levels, including persistent normalization, costs

$$
S\operatorname{poly}(s).
 \tag{13}
$$

Every integral ledger receives at most $C$ debt per expansion
and $2L$ per repaired gain. Its debt is consequently
$O(C^2N)=O(s^2S)$. The top has the sharper bound
$2L(g_*-1)+S^{-800}=O(sS)$. All weights, allocations, column
loads, debts and exchange capacities have $O(s)$ bits with fixed
absolute constants. For example $L=O(sS)$ and a column load is
at most $LN=O(sS^2)$. These quantities fit the existing loose
$S^{20}$ client magnitude envelope eventually.

## 4. Binary reset periods and the exact additive sum

For an event with positive tick increase, select the smallest
$j\in\{1,\ldots,s\}$ for which
$\lfloor\tau/b_j\rfloor$ increases across that event. Such
a $j$ exists because $b_s=1$. Reset this level and all
deeper levels by the existing projection rule.

If $j>1$, no $b_{j-1}$ boundary is crossed. The parent
$(j-1)$-ledger was last reset within the same coarser interval.
Per tick, expansions add at most $C$ debt and repaired gains add
at most twice their $L$-tick increase. Contractions preserve debt
and peels decrease it. Thus its input debt obeys

$$
P\le(C+2)b_{j-1}
      \le(s+3)S/2.
 \tag{14}
$$

This proof covers arbitrarily large $L$-tick jumps. If such an
event crosses a coarser boundary, the coarser level is selected instead.
No proof assumes a unit tick increment or one reset for each boundary
skipped inside one event.

There are at most $\lfloor\tau/b_j\rfloor$ events selecting
level $j$. With $b_{j-1}=2b_j$,

$$
\begin{split}
 \sum_{j=2}^{s}\frac{\tau}{b_j}
                    [(C+2)b_{j-1}+2]
 &\le 2(s-1)(s+3)\tau+
                2\tau\sum_{j=2}^{s}\frac1{b_j}\\
 &< [2(s-1)(s+3)+4]\tau
   =O(s^3S).
\end{split}
\tag{15}
$$

The additive 2 pays even a zero-debt invocation's fixed local overhead.
Level one uses an all-expanded exact exchange recovery and a fresh
integral carrier. The number of such resets is at most
$1+\tau/b_1=1+2\tau/S=O(s)$, where the additive one may also
cover initialization. Its graph has $O(S)$ actual records. The
exact recovery from near-feasible rounding applies even if its initial
assignment-supported allocation does not meet the target residual
floor; it does not call the old static exact-flow algorithm.

## 5. Local nominal sizes and objective bounds

Use nominal top lifetime

$$
R_{\rm top}=S(s+1)^{10}.
 \tag{16}
$$

This covers the $O(CNs)$ logical births and incidence retargetings
from Section 3, plus one attempted physical-size batch before a first
guard failure. Numerical price replacements on retained endpoint slots
do not consume new topological lifetime. Equations (5) and (16) imply
$M_{\rm top}<S^2$ eventually.

A higher-level local projection uses nominal lifetime
$R_{\rm loc}=8192(P+1)$, or an absolute larger constant. The
seed-weight, boundary-lock, region-size and exact union-cut proofs
give this bound with constants independent of $c$, $a$ or
$B_{\rm ledger}$. They use the one-unit stronger parent floor,
$\beta\le P$, integral $u_d\ge1$, and polynomial
capacity magnitudes. They do not require $P\le S$.
By (14), (5) now gives $M_{\rm loc}=O(sS)<S^2$ eventually.
The new numerical interface accepts this bound directly.

The original restriction
$R+B\le S^{1+2/a}$ would equal $R+2\le4S$ at
$a=s$, and need not hold. It is deliberately removed: it was
used to obtain the original local power and price caps, not in the
allocation, locality, lock, or residual-cut proofs. Reimposing it would
be an invalid application of that old packaged numerical theorem.
Similarly, retaining exponent rounding by $2a^2$ would introduce
an unnecessary enormous nominal size and is not part of this construction.

Each local threshold has $O(P+1)$ represented logarithmic terms,
return weight $20000(P+1)$, and argument logarithmic width
$O(s)$. Its objective range plus all insertion/lock losses is
$O((P+1)s)$. The binary search has $O(s)$ threshold tests.
With $q^{-2}=256D^2$, the numerical-client and exact-rounding
proofs give

$$
T_{\rm local}\le(P+1)D^4\operatorname{poly}(s).
 \tag{17}
$$

All-expanded recovery on a graph of $Z$ records has the same
bound with $P+1$ replaced by $Z+1$. Return-arc locking,
ordinary-residual search, common-grid rounding, and exact cut checking
are unchanged. Their proofs use a fixed constant tolerance margin and
total unpadded violation below one; no comparison with the ledger
period ratio occurs.

The top has $O(S)$ terms and objective range $O(Ss)$.
Its $O(CNs)$ structural term changes lose $O(s)$ each.
Hence

$$
J_{\rm top}=O(sS s^2D^2),\qquad
 Q_{\rm top}\le[O(sSs)+O(DJ_{\rm top})]
                                       \operatorname{poly}(s).
 \tag{18}
$$

The second expression counts genuine motion-triggered notifications
and constantly many client services per notification. It does not
relabel all explicit settings as fresh numerical motion. Substitution
in (6), with (16), yields
$T_{\rm top}\le SD^4\operatorname{poly}(s)$.

## 6. Phase cost, direct maximum matching, and finite guards

Multiplying (15) by the common cost in (17), adding $O(s)$
all-expanded resets, and then adding the top, structural and
materialization work gives

$$
T_{\rm phase}\le SD^4\operatorname{poly}(s).
 \tag{19}
$$

The multiplications in this expression are a fixed number of numerical
factors. There is no $D$-factor for each of the $s$ ledger
levels; their input volumes were summed in (15).

The direct gap driver retains its integer upper bound on the possible
improvement. For a large bound, a successful phase reduces it by a
$\Theta(1/C)$ fraction and LOW approximately halves it. For a
bound below a constant multiple of $C$, every successful phase
gains at least one and every LOW strictly reduces the bound. Therefore
there are $O(C(1+\log N))=O(s^2)$ phases. This reasoning uses
the arbitrary-comparison-matching no-false-LOW proof, not a perfect-
matching promise. The complete branch cost is

$$
SD^4\operatorname{poly}(s).
 \tag{20}
$$

All guard adequacy is uniform. Check, for example,
$s\ge1000$, $100000(s+1)\le S^{1/20}$, the numerical
conditions in Section 1, and the ordinary magnitude/record caps.
Retain the $S^{20}$ main-action and threshold-iteration caps and
the $S^{100}$ instance-operation cap. Before a first putative
overflow those loose caps already bound all $O(\delta)$ positivity
and pad changes by a fixed polynomial in $S$, leaving total added
debt/violation below $S^{-800}$. They establish the algebra and
locality needed for the sharper counts; the reasoning is not circular.

Equations (10)--(18), applied to prefixes and one final attempted
batch, then give $S^{1+o(1)}$ total charged work whenever the
favorable cap satisfies $D=S^{o(1)}$. They are far below the
fixed loose guards. The actual values retain the same fixed
$O(s)$-bit root envelope. Persistent memory addresses and all
charged arithmetic likewise fit polynomial master histories. A backend
prerequisite failure still suspends the branch, never supplies LOW.

No allocation-side proof requires $a\ll\sqrt{s}$,
$B_{\rm ledger}\ge E_*$, or an old local exponent
$M^{10/a}$. The required conditions are the explicit floor,
period, magnitude, and numerical contracts stated above.

## 7. Consequence for the 14/15 backend and a finite program

Use the computable degree-reset backend of
[the separate 14/15 construction](distance-degree-reset-candidate.md),
at master $2s$. Its adequate fixed constants $(c_C,c_E)$
give

$$
E_*=
 \exp O\!\left(s^{14/15}(\log(s+4))^{1/5}\right).
 \tag{21}
$$

Since $D=O(E_*+1)$, (20) is
$SE_*^4\operatorname{poly}(s)$, with a constant factor for
the fixed cap rounding. The same rate follows for all general graphs
after the exact subcubic reduction and decoder:

$$
O(n+m)+(m_s+1)
 \exp O\!\left((\log(m_s+2))^{14/15}
                 (\log\log(m_s+4))^{1/5}\right).
 \tag{22}
$$

Only the two backend constant choices are enumerated. The outer
level count $a=s$, period ratio 2, and (3) are explicit; there
is no third parameter chosen to make a separate ledger $B$
dominate the backend. A weighted instruction portfolio runs these
guarded fixed-constant branches and a classical exact fallback. Before
accepting any branch, it validates the original matching and performs
one exact deterministic augmenting-path search. Original input cleanup
is shared once; final original-ID translation is done for the winner.

Every branch has a finite executable parameter rule and charged word
simulation. Some fixed favorable pair has constant scheduling share;
its polynomial scheduling overhead is absorbed in the polynomial of
(20), and therefore in (22). If desired, since the explicit adequate
$E_*$ dominates every fixed polynomial in $s$, a coarser
eventual bound $SE_*^5$ includes that polynomial overhead.
The verifier ensures accepted-output correctness, while existence of
the favorable pair and the mathematical interfaces above are what
establish the conditional fast-time conclusion.

The cover-kernel optional preprocessing from the complete composition
is unaffected: it preserves the optimum and can replace $m_s$
by $m'\le\min\{m_s,O(\nu(G)^2)\}$ in the second term.
All graph classes, densities, and no-perfect-matching inputs remain in
scope.
