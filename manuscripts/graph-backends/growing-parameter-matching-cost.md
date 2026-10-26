# Growing-parameter outer cost for deterministic general matching

**Status: conditional quantitative reconstruction, 24 October 2026.**
This note audits the dependence on the number of integral ledger levels.
It does not substitute a growing value into a fixed-parameter
`O_a` statement. It derives the counts from the explicit client proofs,
using a uniform, master-controlled raw-cycle backend stated below.
The accepted fixed-parameter construction is unchanged.

The conclusion is a deterministic general-graph matching running-time
candidate of the form

```math
O(n+m)+(m_s+1)\exp\!\left(
 O\left((\log(m_s+2))^{335/336}
          (\log\log(m_s+4))^3\right)\right),
```

where `m_s` is the number of distinct nonloop edges. The constant in
this display is absolute. Correctness still depends on the complete
structural, raw-cycle, and lifetime interfaces identified in the
referenced mathematical notes. In particular, this is a research proof
assembly, not a claim of an independently implemented matching solver.

The relevant component proofs are:

* [Priced logarithmic steps](priced-logarithmic-steps-from-raw-cycles.md).
* [Local exact projection](local-exact-projection-from-priced-steps.md).
* [Ledger algebra and phase budget](ledger-algebra-and-phase-budget.md).
* [Phase costs and finite guards](deterministic-phase-cost-and-guards.md).
* [Exact degree reduction and optimum-gap driver](general-graph-gap-reduction.md).
* [Growing-depth numerical aspect exploration](growing-depth-metric-recurrence.md).
* [Quantitative deterministic exact flow](quantitative-exact-flow-dependency.md).

The first five notes' algebraic arguments are used explicitly below.
Their former `O_a` running-time conclusions are not premises here.

## 1. Uniform numerical hypothesis and why a master parameter is needed

Let the physical subcubic graph have order `N`, and fix one power of two
`S=2^s` with `N<=S<2N` for all its phases. Put

```math
\alpha=335/336,\qquad
 E(s)=\exp\bigl(O(s^\alpha(\log(s+4))^2)\bigr).
```

The `O` in this definition denotes one absolute, uniform constant.
Assume the reconstructed primary raw-cycle backend can be run with
master logarithmic parameter `2s` on each numerical instance of actual
nominal size `M<=S^2`. Its required contract is:

1. Initialization, including exposed forest occurrences, costs at most
   `M E(s)`; each update/query and its complete representation log has
   amortized cost at most `E(s)`, with the corresponding prefix bound.
   No allocation or initialization of size `S` is made merely because
   an instance uses master parameter `s`.
2. Raw approximation loss, occurrence multiplicity, and returned path
   piece count are each at most `E(s)`. The ratio uses all mapped
   traversals before cancellation. Stable physical edge identities,
   null-edge semantics, dormant counters, and old-to-final callbacks
   are exactly those of
   [the numerical lifetime interface](numerical-backend-lifetime-and-loops.md).
3. Root integer lengths and gradients of `O(s)` bits are accepted;
   the fixed magnitude envelope `S^1200` is more than sufficient.
   Internal words have `O(s^(337/336))` bits. Arithmetic is charged
   by a fixed polynomial in the bit length, rather than unit cost on
   an arbitrarily large integer.
4. The contract holds uniformly over polynomial **master** lifetimes,
   for example at most `S^200` operations and explicitly logged records
   in one instance. Rebuild periods may depend on actual local size.
   A guarantee limited to a fixed polynomial in the smallest local
   size would not by itself meet this premise.

All recursive size and degree guards of that backend must be
executable and eventually adequate under this common master parameter.
Section 7 of the growing-depth backend note supplies the proposed
master-size construction and explicit recurrences for these assertions;
its named primitive and lift dependencies are retained. The outer
calculation does not reprove that backend. This note imposes no hypothesis
that a local numerical graph has size comparable to `S`.

### The literal local cap is insufficient for this uniform calculation

The fixed-parameter client used `D=M^(10/a)`. That choice cannot be
retained merely by replacing fixed `a` with the growing value below.
For a smallest instance, `u=log_2 M` is approximately `s/a`. The ratio
between the exponent `u^alpha(log u)^2` in its possible backend overhead
and `u/a` in the literal local cap is asymptotically

```math
\Theta\left(
 \frac{s^{1/112896}}{(\log s)^{1+3/336}}
 \right),
```

which tends to infinity. Moreover, the root prices still need `Theta(s)`
bits even in that small instance. These are concrete reasons to use the
master backend hypothesis and the master cap below. They do not affect
the fixed-parameter theorem.

## 2. Explicit outer parameters

For a completely integral parameter selection, set

```math
t=\lceil\log_2(s+4)\rceil,\qquad
 r=\lfloor s^{1/336}\rfloor,\qquad
 a=\lfloor r/t^3\rfloor.
```

The root is found by integer power comparisons. This is an executable
rounding of `s^(1/336)/(log_2(s+4))^3`, with the same asymptotics.
Suspend this fast branch unless `a>=1000` and the explicit initial
guards below hold. Define

```math
C=a+1,\quad v=\lceil s/a\rceil,\quad B=2^v,\quad
 q=B^{-100},\quad D_*=B^{10},
```

and retain

```math
\delta=S^{-1000},\qquad \varepsilon=S^{-3000},\qquad H=S^{100}.
```

As `s` tends to infinity,

```math
v=\Theta(s^\alpha(\log s)^3),\qquad
 a^2=o(v),\qquad v=o(s).
 \tag{1}
```

Every fixed polynomial in `a` and `s` is `2^{o(v)}`. Also

```math
E(s)=2^{o(v)}.
 \tag{2}
```

Consequently the master backend's costs, multiplicity, path-piece
count and inverse quality are eventually bounded by `D_*/4`, after
harmless constant slack. The client may use the computable cap `D_*`
without knowing the hidden constant in `E`. Guard failures remain
suspensions, never LOW certificates. The strong-direction margin is

```math
\frac{1}{4D_*}>2q,
 \tag{3}
```

which holds once `2^(90v)>8`. The numerical client can use the weaker
quality promise `D_*^{-1}` even if the actual backend is better.

The exact reset periods are

```math
b_j=B^{a-j}\quad (0\le j\le a),\qquad
 S\le b_0<2^a S.
 \tag{4}
```

The factor `2^a` is not declared constant. It is `2^{o(v)}` and will be
accounted for explicitly in the local nominal-size check.

## 3. Nominal sizes, rounding, and actual precision

Keep the old rule of choosing `M=2^u` by rounding `16(R+B)` upward
until `u` is divisible by `2a^2`. Then

```math
16(R+B)\le M<16(R+B)2^{2a^2}.
 \tag{5}
```

This is no longer a fixed constant-factor rounding. Its factor is
`2^{o(v)}` by (1), which is sufficient. Divisibility is unnecessary
for `D_*`, but retaining it is harmless and preserves the old size
format.

The top instance uses `R_top=SB`. Its actual physical births and
endpoint retargetings are `O(a S log S)`, as derived in Section 6;
these fit `SB` eventually. Equation (5) gives

```math
\log_2 M_{\rm top}
 \le s+v+2a^2+O(1)<2s.
 \tag{6}
```

At a local reset to level `j>1`, the parent debt satisfies

```math
P\le(C+2)b_{j-1}\le(C+2)b_1
 <(a+3)2^a S/B.
 \tag{7}
```

Thus `8192(P+1)+B<=S` eventually, since
`v-a-log_2(a+3)` tends to infinity. The local projection proof permits
nominal lifetime `R=8192(P+1)` or an absolute larger constant. Its
rounded `M` also has logarithm below `2s`. In particular both top and
local instances meet `R+B<=S^(1+2/a)` at all sufficiently large `S`.
No global scan is hidden in this nominal-size comparison.

The actual input magnitudes have absolute polynomial envelopes. For
all phases, `L<=10000(a+1)S+1`, `c<=a+1`, and integral debts are at
most `O(a^2 S)` by Section 6. Since `a` is a power of a logarithm,
all of these quantities have `O(s)` bits with absolute constants.
Logarithmic arguments on the epsilon grid, their at most two reciprocal
terms, integer prices and exact dyadic steps therefore have `O(s)`
root bits. In particular the priced-step proof's conservative price
envelope is below `S^1200`, independently of `a`.

The backend's longer internal words require a fixed polynomial in `s`
bit-operation overhead. This is absorbed using (1); it is not an
unaccounted `S^{o_a(1)}`. Dynamic-tree and persistent-memory addresses
have `O(s)` bits under the polynomial master guards. No arithmetic
operation here has a number of nested factors depending on `a`.

## 4. Uniform priced-step cost, including full copy sweeps

Use `D_*` in the occurrence bound, refresh thresholds, and copy-sweep
analysis of the priced-step proof. Its algebra is otherwise unchanged.
In particular:

* `lambda` is the sum of the absolute derivatives of the separate
  logarithms, so nearly canceling gradients do not harm accuracy.
* Every accepted list uses its exact raw denominator, one common
  dyadic step, and complete application before any reprice.
* A query's no-motion representation logs and consumption or discard
  of its answer form one atomic transaction.
* Signed retirement transfers preserve exact coordinates; absolute
  retirement transfers preserve refresh credit, including dormant
  copies.

Let `Q` count operations requested by the owning top or local client:
priced-step requests, point reads, logical edits, and explicit value or
descriptor settings. **Internal** anchor refreshes, their backend price
replacements, and their copy sweeps are not counted in `Q`; they are
the separate `O(D_* J)` category below. A price replacement caused by
an explicit client setting is charged once to that setting. Let `J<=Q`
be the number of accepted steps and `p_c<=D_*` the piece count.
Exact refresh and disable charging gives `O(D_* J)` genuine reports
caused by accumulated numerical motion. Full sweeps cost
`O(D_*^2 J)`, rather than constant cost per report. Substituting the
uniform backend bounds into the explicit four work categories yields

```math
\begin{split}
 T_{\rm price}
 &\le\bigl[M+Q+D_*J\bigr]D_*\mathrm{poly}(s)
       +(Q+D_*J)D_*\mathrm{poly}(s)\\
 &\hspace{1cm}+(Qp_c+D_*J)\mathrm{poly}(s)\\
 &\le (M+Q)D_*^2\mathrm{poly}(s).
 \end{split}
 \tag{8}
```

Here and below every polynomial has an absolute degree. The `Qp_c`
term includes raw sums for answers rejected as LOW. Combining (5)
and (8) gives the useful master-size form

```math
T_{\rm price}
 \le (R+B+Q)\,2^{2a^2} B^{20}\mathrm{poly}(s).
 \tag{9}
```

The drift thresholds and dyadic-grid checks remain valid. Eventually
`D_*<=S^2`, `q>=S^{-1}`, and `M<=S^2`. The total traversals in a list
are at most a constant times `M D_*^2<S^20`. Thus the old bounds
`V/H<=S^1044`, `mu>=S^{-1045}/400` and
`theta>=S^{-1030}` still leave ample room above `epsilon=S^{-3000}`.
No coordinatewise rounding is introduced.

The loose guard `Q<=S^100` allows at most `O(D_*Q)<=S^103` backend
edits and corresponding polynomially many logs before the sharper
counts are applied. The master lifetime premise `S^200` covers them.
Total signed and absolute motion remains bounded by the existing
`S^220` estimate; anchors and retirements do not duplicate motion.

## 5. Uniform local exact projection cost

The local proof uses absolute constants: scaled capacities are
multiplied by 16, return weight is `20000(P+1)`, represented ordinary
arcs number less than `1000(P+1)`, and the cumulative expanded weight
is less than `11(P+1)`. Its positive-deficit seed argument, optimistic
boundary domination, permanent sink locks, small-total-violation
integrality, and exact two-region union do not depend on `a`.

Every ordinary logarithm has `O(s)` width by Section 3. The return
weight is an absolute constant times `P+1`. The objective range and
the total insertion/lock loss are therefore bounded by
`c_0(P+1)s`, with one absolute `c_0`. Each accepted step gains an
absolute constant times `q^2`. A threshold test has at most

```math
J_{\rm loc}\le c_1(P+1)B^{200}s
 \tag{10}
```

accepted steps, plus one final query. Let `F_num` be the engine's genuine
motion-triggered notifications, so `F_num=O(D_* J_loc)`. The client
performs constantly many pad, queue or descriptor operations per such
notification. An explicit setting's acknowledgment is already handled
with that setting and is not recursively treated as a new report;
coalesced/stale flags are skipped. No-motion reanchoring cannot create
new absolute-motion credit. Seed and region work is
`O(P+1)` records with polynomial-in-`s` dictionary/physical costs.
Consequently `Q_loc` is bounded from the external requests
`O(P+1+J_loc+F_num)`, giving

```math
Q_{\rm loc}\le
 (P+1+D_*J_{\rm loc})\mathrm{poly}(s).
 \tag{11}
```

Equations (9)--(11) bound its numerical part by

```math
(P+B)\,2^{2a^2}B^{230}\mathrm{poly}(s).
 \tag{12}
```

This is a noncircular substitution: (8) treats `Q` as its client's
external requests, while (11) derives those requests from accepted
steps and a disjoint internal-refresh charge. It displays the full
`D_*^2` sweep cost and the additional `D_*` notification-response
factor. There is no product of one numerical
overhead for each ledger level inside a threshold test.

### Exact flow checks and recovery

The deterministic static-flow import must also have a uniform rate.
The constructive parameters of van den Brand et al.,
[*A Deterministic Almost-Linear Time Algorithm for Minimum-Cost Flow*,
arXiv:2309.16629v1](https://arxiv.org/abs/2309.16629v1), give the
rate

```math
Z\exp\bigl(O((\log Z)^{17/18}\log\log(Z+4))\bigr)
 \mathrm{poly}(\text{input bit length})
 \tag{13}
```

for the fixed polynomial-capacity exact-flow primitive used here.
This is the quantitative dependency being used; a bare `Z^{1+o(1)}`
statement would not suffice for the explicit conclusion of this note.
The parameter derivation uses Lemma 5.17's
`gamma_l,gamma_r=exp(O(log^(8/9)Z loglog Z))`, depth
`Theta(log^(1/18)Z)`, the Section 6.2 runtime expression, and the
polynomial inverse-quality iteration bound in Theorem 4.6. Exact
rounding and scaling are part of the same static-flow import;
the complete parameter derivation and arithmetic scope are recorded in
[the quantitative exact-flow note](quantitative-exact-flow-dependency.md).

For capacities with `O(s)` bits on a small region, the capacity-digit
reduction in the local-projection note uses `O(s)` rounds, each with
residual capacities truncated at the number of arcs. Pad the primitive
size to `Z+B`; never pad it to `S`. Since `Z=O(P+1)` and
`log(Z+B)<=O(s)`, (13) gives cost

```math
(P+B)\exp\bigl(O(s^{17/18}\log s)\bigr)\mathrm{poly}(s)
 \le (P+B)B
 \tag{14}
```

eventually. Exact threshold checks and the final union-flow recovery
are therefore smaller than (12). There are `O(log(beta+2))=O(s)`
threshold tests, including the constant number of repeated endpoint
tests. Using (1), a convenient conservative bound for a whole local
projection is

```math
T_{\rm proj}\le (P+B)B^{250}
 \tag{15}
```

for all sufficiently large `S`. The exponent 250 is an absolute
envelope, not a new optimized constant. The exact changed support is
still `O(P)`, and a peel has weight less than `P`.

## 6. Structural and top-objective counts with explicit `a`

For target gain `1<=K<=N`, set

```math
L=\lceil10000 C N/K\rceil,\qquad
 g_*=\max\{1,\lfloor K/(100C)\rfloor\}.
```

If `K>=100C`, then `L g_*<=101N`. If `K<100C`, then
`g_*=1` and `L<=10001 C N`. Thus in every case

```math
Lg_*\le10001 C N.
 \tag{16}
```

The exact debt identity pays total peel weight by
`2L(g_*-1)+S^{-800}`. Including erased gain regions, expansions,
contraction arities, successful pair materialization and tick count
are bounded by an absolute constant times `N+Lg_*`. Hence

```math
\tau=O(aS),\qquad
 T_{\rm structural}=a^2 S\mathrm{poly}(s).
 \tag{17}
```

The second factor `a` allows applying a physical batch to all integral
levels. Persistent sparse normalizations are charged by their changed
support; resets do not scan an old bottom ledger. The largest-bin
representative argument charges at most `O(log S)` physical moves per
stay, and there are `O(aS)` stays and row absorptions. These are
explicit linear dependences on `a`, not unspecified constants.

Each preserved integral ledger can acquire at most `C` debt per
expansion and `2L` per repaired gain. Equations (16)--(17) give an
absolute bound `O(a^2S)` on its debt. At the top, the sharper bound is
`2L(g_*-1)+S^{-800}=O(aS)`. With `O(S)` top coordinates, the top
objective range is `O(Ss)`. Structural touches number `O(aSs)` and
each loses at most `O(s)` objective, giving total loss `O(aSs^2)`.
The top positivity service creates only negligible loss and has no
no-motion repair cascade.

Therefore

```math
J_{\rm top}=O(aS B^{200}s^2).
 \tag{18}
```

Every notification causes constantly many point reads/settings and
eligibility changes; a high-degree bin residual is read from
`y=s-p+Cw`, without summing all its moving incidences. Thus

```math
Q_{\rm top}\le
 (aSs+D_*J_{\rm top})\mathrm{poly}(s).
 \tag{19}
```

Using `R_top=SB` in (9) bounds all top numerical work by
`S B^{240}` eventually, with an absolute exponent. This includes
initialization and the first final LOW or interrupted attempt.

## 7. Reset sum and phase cost

At a level `j>1` reset, the trigger crosses no `b_(j-1)` boundary.
The parent was reset within that same interval. An expansion adds
at most `C` debt and one tick; a repaired gain adds at most `2L`
debt and `L` ticks. Contractions preserve debt and peels decrease it.
This proves (7), including a gain that jumps over many finer periods.

There are at most `floor(tau/b_j)` triggers at level `j`. Hence

```math
\begin{split}
 \sum_{j=2}^{a}\frac{\tau}{b_j}
       [(C+2)b_{j-1}+B]
 &\le\tau[(a-1)(C+2)B+2B]\\
 &=O(a^3 S B).
 \end{split}
 \tag{20}
```

Multiplying this sum by the common factor in (15), rather than
compounding costs along the ledger hierarchy, gives at most
`O(a^3 S B^251)`. Sparse support application and carrier normalization
fit the same bound.

At level one, a global exact exchange flow and fresh carrier cost
`S exp(O(s^(17/18)log s)) poly(s)`. Because `b_0>=S`, the number
of these resets is at most `tau B/S=O(aB)`. Their total is at most
`S B^3` eventually. The top initialization and a possible final
materialization also fit the previously stated budgets.

Combining (15)--(20) and absorbing the displayed fixed polynomials
using (1), a deliberately loose per-phase bound is

```math
T_{\rm phase}\le S B^{300}.
 \tag{21}
```

It holds equally on no-instances and prefixes ending in LOW. No phase
count assumes that `K` equals the number of unmatched pairs.

## 8. First-failure and finite-word checks are uniform

The initial checks

```math
S\ge2^{100},\quad 100000C\le S^{1/20},\quad
 B\le S^{1/20},\quad q\ge S^{-1}
```

all hold eventually for the computable growing `a`. Retain the finite
caps `S^20` on main actions/threshold iterations and `S^100` on an
instance's external operations. A failed guard suspends, never LOW.

The first-failure proof uses the loose guards before using (21).
They bound the number of top positivity settings by a fixed polynomial
in `S`, and local pad settings by a fixed multiple of `S^100`.
Multiplication by `delta=S^-1000` leaves total positivity debt and
unpadded violation below `S^-800`. Their estimates have absolute
exponents: `a<S^(1/20)` is already checked, and each local response
has constant arity. These preliminary small-error bounds establish
the debt and locality arguments needed for the sharper counts.

Completed structural actions independently satisfy (16)--(17).
Through a first attempted failure, include one attempted physical
batch of size `O(S)`. Loads, debts, return weights and capacities
therefore fit the loose `S^20` argument envelope. The projection
volume bound is proved before expanding a newly triggered bin, so
it applies at a putative first nominal-size overflow. Equations
(6)--(7) discharge the size check uniformly.

The price/lifetime prefix bounds, followed by (10), (18), and (20),
give all sharply charged counts at most `S B^{O(1)}=S^{1+o(1)}`.
They are eventually strictly below the finite action and external
operation caps. The raw list length is likewise below its guard,
as verified in Section 4. No argument uses successful completion
to justify an earlier small-violation or magnitude premise.

The master backend's own eventual guards remain a separate necessary
premise. Their adequacy is not implied by the final matching verifier.
The finite exceptional input sizes may be handled by the previously
specified verified deterministic fallback. That wrapper ensures exact
output on exceptions but supplies no missing numerical speed bound.

## 9. Complete maximum matching and the final envelope

Keep the single value of `a` and the same `S` throughout the direct
optimum-gap driver. If its current upper bound on remaining improvement
is `U`, take `K=ceil(U/2)`. A valid LOW reduces the bound to at most
`K-1`; a successful phase gains `g_*` edges. For `U>=400C`,
`g_*>=U/(400C)`. Below that range, each success gains at least one
and each LOW strictly reduces the integer bound. Thus there are at
most `O(a(1+log(N+1)))` phases, with an absolute implied constant.

After multiplying (21) by this number and paying the exact final
matching check, a conservative bound is

```math
T_{\rm subcubic}\le S B^{320}
 =S\exp\bigl(O(s^{335/336}(\log s)^3)\bigr).
 \tag{22}
```

The elementary path-port degree reduction has `N=4m_s-r=O(m_s)`
and an exact optimum offset. Its linear-time decoder is valid for
every matching of the auxiliary graph, not only a canonical one.
Preprocessing arbitrary undirected input therefore gives the bound
stated at the beginning of this note. Loops, parallel input records,
odd order, disconnected graphs and arbitrarily many unmatched
vertices require no additional promise.

The uniform outer proof depends on two quantitative numerical facts:
the master-controlled raw flat-cycle/lifetime contract of Section 1,
and the explicit deterministic static-flow rate (13). Subject to
those facts, all remaining dependence on `a` has been exposed as
polynomials, `2^a`, `2^{2a^2}`, or a fixed power of `B`; each is
bounded in (1). No unquantified fixed-parameter convergence rate is
used to obtain (22).
