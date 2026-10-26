# A distance-decrease detector with frozen auxiliary barriers

**Research theorem candidate, 25 October 2026.** This note proposes a
modification of the detector in Yang P. Liu's *Incremental Shortest Paths
in Almost Linear Time via a Modified Interior Point Method*,
arXiv:2506.19207v1, Sections 2--3. The proposed change is to freeze an
auxiliary coordinate when it becomes dangerous, retain its flow and cost
as constants, and delete its positive barrier. This potentially removes
the minimum-ratio oracle's approximation factor from the *cumulative
reporting bound*. It does not remove that factor from the running time.

Primary source: <https://arxiv.org/html/2506.19207v1>.

The construction remains conditional on a correct raw-cycle and
flow-maintenance interface. In particular, it must support retirement
of a logical edge at its exact current value, not only insertion of
zero-flow edges. All claims below concern a single detector lifetime.
The separate outer-recursion note will account for rebuilding.

## 1. Input, numerical scope, and required oracle

Fix a global master size $`N=2^U\geq64`$. Let $`1\leq M\leq N`$ bound the total number of actual ordinary edge records,
auxiliary copies, and vertex records that can be born during this
lifetime. Increasing this bound by a fixed constant to cover all these
categories is harmless. It is an accounting bound; no dummy vertices
or edges are allocated. The cost of this detector is proportional to
its local inventory allowance $`M`$, while arithmetic uses the common
master precision $`U`$. In particular, a small recursive graph is not
padded to size $`N`$.

Here $`M`$ counts logical flow coordinates and their linear-size
degree-three port lift. It does **not** count the
$`M E^{O(1)}`$ internal flat-forest occurrences of the raw backend.
Those occurrences are charged only in running time and raw movement.
In particular, neither the potential coefficient $`AM`$ nor the
reporting bound below is enlarged by the flat-copy multiplicity.

The directed ordinary graph has a source $`s`$. Every current vertex is
reachable from $`s`$, and all current source distances lie in $`[1,2]`$.
Ordinary edges have positive rational costs in $`[N^{-c},2]`$, for a
fixed constant $`c`$. Edges longer than 2 are irrelevant for this
normalized problem and may be omitted. All supplied costs share a
polynomial-bit grid. Vertices and ordinary edges can be inserted.

Each vertex $`v\ne s`$ receives one or more *auxiliary units*. Unit
$`j`$ belongs to a vertex $`v(j)`$, has a fixed anchor cost
$`a_j\in[1,2]`$, and stores an available source-to-vertex walk of cost
$`a_j`$. Thus $`a_j\geq d(s,v(j))`$ whenever the unit is inserted,
and this remains true as ordinary edges are inserted. In the application,
all units belonging to one vertex during a phase have the same anchor.
New units may arrive later in the lifetime. Let

```math
b_v=|\{j:v(j)=v\}|,\qquad F=\sum_{j\text{ born}}a_j.
```

The full flow routes $`b_v`$ units to each $`v\ne s`$, with balancing
source demand. It initially sends one unit on every auxiliary edge
$`j=(s,v(j))`$, and zero on ordinary edges. A new auxiliary unit is
inserted at flow one. A new ordinary edge is inserted at flow zero.
These are explicit demand changes. All subsequent numerical changes
are exact circulations in the currently active graph.

Fix detector accuracy $`\sigma\in(0,1/100]`$, a phase threshold
$`0<\alpha\leq\sigma/10^6`$, and assume
$`\alpha\geq N^{-1/100}`$. The last condition is an eventual
parameter restriction for the growing-depth application, not a claim
for arbitrarily small $`\alpha`$. Let

```math
p=\lceil20U\rceil,\quad A=1000,\quad
K=\frac{\sigma}{100\alpha},\quad F_*=(1-\alpha)F.
\tag{1}
```

The oracle loss is $`\rho\geq1`$, with numerical parameter
$`\beta=1/(C\rho)`$, where $`C`$ is a sufficiently large absolute
constant. Assume $`\beta\geq N^{-1/100}`$ eventually. Its time,
flat-copy multiplicity, raw answer size, and notification factors are
bounded by a common factor $`E=N^{o(1)}`$, with
$`\rho\leq E^{O(1)}`$.

For current positive weights $`w`$ and signed gradient $`g`$, the
interface must do one of the following after settlement:

* certify that every circulation has ratio greater than $`-1/4`$; or
* return a circulation $`z`$, together with an explicit raw forest-path
  representation and its positive raw weighted length $`R`$, such that
  $`\|Wz\|_1\leq R`$, $`g^Tz\leq-\beta R`$, and the representation
  can be applied at a dyadic scale $`\eta`$ with
  $`\eta R\in[\beta/(C_1p),2\beta/(C_1p)]`$.

Constant-factor slack permits approximate prices and a common positive
rescaling of the gradient. The true guarantees just stated are what
the potential proof uses. They must be derived from the raw backend,
not from a ratio computed after cancellation. All logarithmic and
power terms below can be differentiated by rational arithmetic; the
algorithm need not evaluate logarithms.

## 2. Active and frozen coordinates

Let $`J`$ be the auxiliary units that are still active. For a frozen
unit $`j`$, write $`z_j`$ for its immutable frozen flow. The full cost
is

```math
P=c^Tf_{\mathrm{ordinary}}+
  \sum_{j\in J}a_jf_j+
  \sum_{j\text{ frozen}}a_jz_j.
\tag{2}
```

The last sum is an exactly maintained scalar offset. It is part of
the cost and the logarithmic gap throughout the detector lifetime.

The potential is

```math
\Phi(f)=AM\log(P-F_*)
-\sum_{e\text{ ordinary}}\log(f_e+\delta_e)
+\sum_{j\in J}V_p(f_j),
\tag{3}
```
where

```math
V_p(x)=\begin{cases}x^{-p}/p,&0<x\leq1,\\
1/p-\log x,&x\geq1.
\end{cases}
\tag{4}
```

Set $`r=P-F_*`$. On active coordinates define

```math
w_e=(f_e+\delta_e)^{-1}\quad(e\text{ ordinary}),\qquad
w_j=-V_p'(f_j)\quad(j\in J),
```
```math
g=\frac{AM}{r}c-w.
\tag{5}
```

Initially $`\delta_e=\delta_0=N^{-B}`$, where $`B`$ is a sufficiently
large fixed constant depending only on the input cost-bit envelope.
When an ordinary slack approaches $`\delta_0`$, increase its
$`\delta_e`$ by $`\delta_0`$ and reprice it. Use two separated
thresholds, for example rearm below $`5\delta_0/4`$ and reset above
$`2\delta_0`$, to charge each such event to a constant amount of
weighted absolute motion. This change lowers $`\Phi`$ and does not
change $`P`$, $`F`$, or the flow. The event and lifetime guards below
ensure $`\sum_e\delta_e\leq N^{-20}`$. Any desired larger fixed
polynomial separation can be obtained by choosing $`B`$ larger.
An ordinary edge is born with slack $`\delta_0`$, so its first
rearming event receives one constant birth credit. Only subsequent
rearming events are charged to separated-threshold motion.

### The freezing operation

Whenever an active auxiliary copy is reported by the stale-flow
maintenance structure as having weight at least $`K`$, read its exact
current value and freeze it if its true weight is at least $`K/2`$.
Set $`z_j=f_j`$, move $`a_jf_j`$ to the constant offset in (2), and
retire the edge from the active raw graph. Its old coordinate value,
price, endpoint correspondence, and copy counters remain available
until all retirement callbacks are complete.

Because $`K/2>1`$, an edge frozen this way satisfies

```math
0<z_j<1.
\tag{6}
```

Thus no negative auxiliary flow and no auxiliary flow greater than one
is ever frozen. The active demand at $`v`$ becomes

```math
b_v-\sum_{j\text{ frozen},\ v(j)=v}z_j\geq0.
\tag{7}
```

The operation does not change the *full* flow, its full divergence, or
its full cost. The remaining active flow has precisely the residual
demand (7). Future numerical increments are circulations on the
remaining active graph and preserve it.

The positive potential term $`V_p(z_j)`$ is deleted. No other term of
$`\Phi`$ changes. Freezing is therefore a potential decrease of
exactly $`V_p(z_j)`$.

For a vertex $`v`$, report it once all auxiliary units currently
belonging to it have been frozen. Reports are permanent for this
detector lifetime. New units belonging to an already reported vertex
may still be maintained, but do not cause a second vertex report.

## 3. Termination without an external min-cost-flow instance

Use the explicit stopping threshold

```math
P\leq(1-3\alpha/4)F.
\tag{8}
```

If a proposed complete numerical step would reach this threshold,
the detector may terminate before applying it. The proposed complete
flow is already known to preserve the full demand and all coordinate
lower bounds, so it is an existence certificate for the stopping
argument. No claim about the objective is evaluated between the
individual forest-path operations of a numerical transaction.

Let $`d(v)`$ be current true source distances. A shortest-path potential
has $`d(s)=0`$, $`d(v)\in[1,2]`$, and
$`c_e-(d(v)-d(u))\geq0`$ on every ordinary edge. This reduced cost is
at most 4, because ordinary costs are at most 2. Auxiliary edges also
have nonnegative reduced cost and nonnegative flow. Conservation gives

```math
P\geq\sum_v b_vd(v)-4\sum_e\delta_e.
\tag{9}
```

Choose the slack envelope so that
$`4\sum_e\delta_e\leq\alpha F/8`$. Then (8) implies

```math
\sum_vb_vd(v)\leq(1-5\alpha/8)F<(1-\alpha/2)F.
\tag{10}
```

Thus termination is justified by a real decrease in the weighted
shortest-path objective. This removes the fixed-demand restriction
that would arise if the detector called a black-box incremental
min-cost-flow solver while vertices and demand units were being born.

At all settled nonterminal states,

```math
r=P-F_*>\alpha F/4.
\tag{11}
```

## 4. Why freezing preserves the strong comparison direction

Suppose $`P>(1+5\alpha)F`$. Construct a conceptual comparison flow
$`f^*`$ as follows.

* Keep each frozen unit at exactly $`z_j`$.
* For every active auxiliary unit set $`f_j^*=\min\{f_j,1\}`$.
* For each auxiliary unit, route its remaining amount
  $`1-z_j`$ or $`1-f_j^*`$ along a current ordinary shortest path to
  its owner.

All remaining amounts are nonnegative by (6). Consequently this is a
feasible full flow of the same demand, with nonnegative ordinary flow.
For each unit its fixed/active auxiliary portion uses cost $`a_j`$,
while its remaining portion uses current distance at most $`a_j`$.
Therefore

```math
c^Tf^*\leq\sum_j a_j=F.
\tag{12}
```

The difference $`\Delta=f^*-f`$ is an active-graph circulation: it is
zero on every frozen coordinate. For any ordinary edge, positivity of
$`f_e+\delta_e`$ and $`f_e^*\geq0`$ give

```math
-w_e\Delta_e\leq2-w_e|\Delta_e|.
```

The same inequality holds for an active auxiliary edge. If $`f_j\leq1`$
then $`\Delta_j=0`$; if $`f_j>1`$, its weight is $`1/f_j`$.
There are at most $`M`$ active coordinates. Combining with
$`(P-F)/(P-F_*)>5/6`$,

```math
g^T\Delta\leq-\frac56 AM+2M-\|W\Delta\|_1
\leq-\|W\Delta\|_1.
\tag{13}
```

Thus a sound LOW certificate is impossible when
$`P>(1+5\alpha)F`$, even after arbitrarily many valid freezes.
At a settled LOW state,

```math
P\leq(1+5\alpha)F,\qquad r\leq6\alpha F.
\tag{14}
```

## 5. LOW still certifies all unreported vertices

By the circulation/gradient duality used in Liu25 Lemma 3.7, a sound
LOW statement yields a potential $`\pi`$ on the active graph satisfying
$`|g-B\pi|\leq w/4`$. This uses one consistent incidence convention;
the absolute value in the printed *negative-ratio premise* is not used.

Set $`\phi=(r/(AM))\pi`$ and normalize $`\phi(s)=0`$. On every
ordinary edge and every remaining auxiliary edge,

```math
\frac{3r}{4AM}w_e\leq c_e-(\phi(v)-\phi(u))
\leq\frac{5r}{4AM}w_e.
\tag{15}
```

All ordinary edges remain present, so $`\phi(v)\leq d(s,v)`$ in the
current ordinary graph, regardless of which auxiliary edges were
frozen. If $`v`$ is unreported, it has at least one remaining auxiliary
copy $`j`$. Settle all heavy-copy notifications before returning LOW.
With the stated constant-factor price accuracy, such a remaining
copy has true weight less than $`2K`$. Equations (14)--(15),
$`F\leq2M`$, and (1) imply

```math
a_j-d(s,v)\leq a_j-\phi(v)
\leq\frac{12\alpha F}{AM}\,2K
\leq\frac{48\alpha K}{A}<\sigma.
\tag{16}
```

Since $`a_j\geq1`$, this gives
$`d(s,v)\geq(1-\sigma)a_j`$. When all units of $`v`$ use one anchor,
this is exactly the required per-vertex certificate.

The argument uses only *one remaining auxiliary copy*. It does not
require a dual constraint on a frozen copy. When a vertex's distance
has genuinely decreased, all of its remaining copies must therefore
be removed before a sound LOW state can be returned.

## 6. Potential accounting and a reporting bound independent of rho

At initialization $`P=F`$, all auxiliary flows are one, ordinary flows
are zero, and $`|\Phi|=O(MU)`$. An ordinary-edge insertion adds
$`-\log\delta_0=O(U)`$.

Inserting an auxiliary unit of anchor $`a\in[1,2]`$ adds $`a`$ to
both $`P`$ and $`F`$, hence adds $`\alpha a`$ to $`r`$. By (11),
its potential increase is at most

```math
AM\log(1+\alpha a/r)+1/p
\leq4AM\,a/F+1/p.
\tag{17}
```

As $`F`$ grows by these same anchors, the sum of $`a/F`$ is
$`O(U)`$. The empty case is skipped until the first unit is
born. Therefore the *total positive potential injection* from all
births is $`O(MU)`$. Rearming ordinary slacks lowers the
potential; freezing lowers it; accepted numerical steps lower it.

For completeness, the potential has a polynomial-state lower bound.
Ordinary negative flow contributes at most
$`2\sum_e\delta_e`$ negative cost. Because all costs are at least
$`N^{-c}`$, any nonnegative coordinate is at most
$`N^c(P+1)`$. If $`P`$ is large, the positive term
$`AM\log(P-F_*)`$ dominates the at most $`M`$ negative logarithmic
barrier terms. The upper bound on $`\Phi`$ consequently gives
$`P\leq N^{C_2}`$ for one fixed constant $`C_2`$. Together with
(11), this proves

```math
\Phi\geq-C_3MU
\tag{18}
```

for another fixed constant. This proof does not count a frozen barrier
in the potential. Thus deleting such a barrier does not invalidate
the lower bound.

At a freeze, $`w_j\geq K/2>1`$, so

```math
V_p(z_j)=\frac{w_j^{p/(p+1)}}p
\geq\frac{(K/2)^{p/(p+1)}}p
=\Omega(K/p).
\tag{19}
```

The last equality uses $`p\geq\log K`$, which follows from the
parameter range in Section 1. Potential injections, (18), and the
nonnegativity of every other accounted decrease now give

```math
\#\{\text{frozen auxiliary copies}\}
\leq O\!\left(\frac{MpU}{K}\right)
=O\!\left(\frac{\alpha M U^2}{\sigma}\right).
\tag{20}
```

There is **no factor involving $`\rho`$, $`\beta^{-1}`$, or $`E`$**
in (20). This is the proposed improvement over charging each dangerous
copy to the total numerical motion.

The argument does not assert that every true decrease in the weighted
distance sum forces immediate termination. A detector may continue
after that condition becomes true. It must only terminate soundly,
return sound nonterminal certificates, and obey (20). Frozen auxiliary
flow can delay termination without violating any of these properties.

## 7. Why each numerical step and the total work remain controlled

The piecewise barrier (4) is continuously differentiable. On a step
whose raw weighted motion is at most $`1/(C_1p)`$, its second-order
remainder is at most a constant times
$`p\|W\eta z\|_1^2`$; ordinary logarithmic barriers satisfy the same
bound with a smaller constant. Concavity bounds the global
$`AM\log r`$ term by its first-order change whenever the final gap is
positive. Consequently the oracle guarantees in Section 1 imply

```math
\Phi(f+\eta z)-\Phi(f)\leq-\Omega(\beta^2/p).
\tag{21}
```

If the proposed final gap is too small, Section 3 terminates the
detector instead. Coordinate positivity holds even during the raw
forest-path transaction, since every partial coordinate change is
bounded by the full raw weighted motion. The global affine cost and
the potential are read only after the transaction is complete.

By the same potential budget, the number of accepted steps is

```math
T=O(Mp\beta^{-2}U)=M E^{O(1)}\mathrm{poly}(U).
\tag{22}
```

Total raw motion is at most $`O(T\beta/p)`$. Together with one
constant birth credit per ordinary edge, this pays all separated
ordinary-slack rearming events. For sufficiently large master $`N`$, the
total event count is polynomial in $`N`$; choosing $`B`$ larger
than that fixed horizon keeps $`\sum_e\delta_e\leq N^{-20}`$.
This is an acyclic guard: fix the polynomial event horizon first,
then choose the slack exponent. Rearm counters are not reset by
representation changes.

Maintain an anchor $`\widehat r`$ within relative $`O(\beta)`$ of
$`r`$, and flow anchors accurately enough that every weight changes
by only $`O(\beta)`$ between refreshes. For auxiliary powers this
requires relative flow accuracy $`O(\beta/p)`$. The scaled-gradient
identity

```math
\widehat g-\frac r{\widehat r}g
=\frac r{\widehat r}w-\widehat w
\tag{23}
```

pays for the global cost term without requiring an additive bound on
its potentially large coordinates.

A numerical step with negative gradient has positive relative gap
increase at most $`O(\beta/(Mp))`$. Auxiliary births contribute a
total $`O(U)`$ positive logarithmic increase by (17).
The polynomial upper/lower gap bounds imply that the total negative
logarithmic variation is at most the total positive variation plus
$`O(U)`$. Hence full gradient repricing occurs at most
$`E^{O(1)}\mathrm{poly}(U)`$ times. Each such pass costs
$`M E^{O(1)}`$, within the lifetime work bound.

All remaining coordinate refreshes, exact point reads, auxiliary
retirements, and edge births are charged by the raw flow-maintenance
interface. The detector's total time is therefore

```math
M E^{O(1)}\mathrm{poly}(U).
\tag{24}
```

Power evaluation at integer exponent $`p=O(U)`$ uses polynomially
many bits. Stored prices are rounded to a common integer scale after
evaluation. Their *values* remain polynomially bounded: the potential
bound prevents an active auxiliary flow from becoming so small that
$`f^{-p}`$ exceeds a fixed polynomial; ordinary slacks are rearmed.
The backend must pay the resulting exact arithmetic or a proved
relative-rounding implementation. No irrational comparisons are
required by (1), (8), the freezing rule, or the update rules.

### 7.1 A common-grid implementation of this particular detector

Here is a more explicit finite-arithmetic choice. Take the master
$`N=2^U`$; let costs and anchors have a common dyadic denominator at
most $`N^{c_0}`$. Round $`\alpha`$, $`\sigma`$, and $`\beta`$ down
to powers of two within fixed constant factors, and retain the slack
in the numerical inequalities above. The power $`p`$ is an integer.

The potential upper/lower argument gives fixed constants bounding
$`|f_e|`$, $`r^{-1}`$, $`w_e`$, $`w_e^{-1}`$, and $`|g_e|`$ by
polynomials in $`N`$, while the ordinary-slack rule bounds all its
negative excursions. These constants may depend on the fixed input
bit envelope and slack exponent, but not on the input size or on a
recursion level. The auxiliary upper-weight bound follows directly
from $`V_p(f)=f^{-p}/p`$ and the potential budget, so it is still
polynomial when $`p=\Theta(U)`$.

Choose one price scale $`H=N^{C_H}`$ larger than these fixed exponents.
After evaluating the rational weights and gradients at their anchors,
send the raw backend
$`\ell_e=\lceil H\widehat w_e\rceil`$ and
$`\gamma_e=\mathrm{round}(H\widehat g_e)`$.
The rounding error is at most $`1/H`$, which can be made less than
$`\beta w_e/10^6`$ uniformly. The exported integers still have
$`O(U)`$ bits. The exact evaluation of a power at exponent $`p`$
can use $`O(U^2)`$-bit temporary integers; their polynomial bit cost
is paid locally and is not an exported edge-label magnitude.

The raw backend supplies at most $`E^{O(1)}`$ signed pieces in a flat
forest of at most $`M E^{O(1)}`$ records. With polynomially bounded
root integer prices, its complete raw integer denominator satisfies
$`1\leq V\leq N^{C_V}`$ for one fixed constant $`C_V`$. The usual
degree-three port lift puts zero gradient and sufficiently negligible
priced length on connectors; its linear-size physical port records
and their retired lifetimes are included in the logical allowance.
Internal raw-forest copies are instead paid by $`E^{O(1)}`$, without
enlarging the potential or reporting count. Logical raw weighted
motion is bounded by a fixed multiple of $`V/H`$.

Choose a power-of-two step $`\eta`$ by integer comparisons so that
$`\eta V/H`$ is between two fixed constant multiples of
$`\beta/p`$. Since $`\beta\geq N^{-1/100}`$, this step has
$`\eta\geq N^{-C_\eta}`$ for one fixed constant. Taking a common
flow grid $`N^{-C_f}`$, with fixed
$`C_f>\max\{B,C_\eta+c_0+10\}`$, makes
every accepted step an exact grid circulation. All initial values,
ordinary slack offsets, and auxiliary frozen values lie on that grid.
No coordinatewise rounding of a circulation is performed.

The maintained cost, frozen-cost offset, $`F`$, and the affine gap
$`r`$ then have one fixed polynomial-bit dyadic denominator. Their
tests are exact. A frozen edge is retired only after its exact grid
value has been read and its cost moved to the offset. A point check
of the auxiliary threshold evaluates a positive integer power and
uses cross multiplication. It does not approximate a logarithm or
an irrational root.

All price refreshes and affine-cost reads are postponed until a
numerical transaction settles. An intermediate forest-path update
need not preserve the final circulation or keep the *affine cost gap*
positive. The individual coordinate barriers remain positive by raw
absolute-motion control, and the complete proposed update either
passes the positive final-gap test or triggers sound termination.
The Taylor/concavity proof is applied to the straight segment between
the two complete flows, where a positive final gap is enough.

## 8. Degree-weighted units and vertex birth

For an arbitrary directed parent graph, assign

```math
b_v=1+\deg_{\mathrm{in}}(v)+\deg_{\mathrm{out}}(v)
\qquad(v\ne s).
\tag{25}
```

Implement this with separate auxiliary copies, not a large integral
coefficient hidden in the running time. Each parent edge insertion
creates at most two new copies. A vertex birth creates its base copy.
All copies of a vertex share its current phase anchor. The source
itself is never a reported target.

At the moment $`v`$ is first reported, all its current copies have
been frozen. Different reported vertices own disjoint copies.
Therefore (20) implies

```math
\sum_{v\text{ reported}}
 \bigl(1+\deg_{\mathrm{in}}^{\mathrm{report}}(v)
          +\deg_{\mathrm{out}}^{\mathrm{report}}(v)\bigr)
\leq O\!\left(\frac{\alpha M U^2}{\sigma}\right).
\tag{26}
```

This pays both incoming edges and pending outgoing edges when a
reported vertex is inserted into a recursively maintained graph.
Edges born *after* that report are charged to their ordinary input
insertions. An outer child-size cap handles that separate category.

No bounded-degree assumption and no uncharged degree-reduction
gadget is used in (26). The normalized detector permits new demand
units because their potential injection was paid explicitly in (17).

## 9. Precise remaining review obligations

The mathematical proposal above still requires an independent audit of
its imported raw interface, finite-precision settlement, and its outer
recursive use. In particular:

* frozen values must remain immutable constants until a full phase
  restart, and their cost must remain in (2);
* a full restart runs Dijkstra, rebuilds phase anchors, reinitializes
  unit auxiliary flows, and pays a new $`O(MU)`$ potential
  budget; no freeze credit is transferred across that restart;
* each LOW answer is issued only after all refreshes, freezes,
  retirements, and demand bookkeeping have settled;
* the right-hand side of (20) counts cumulative frozen copies, not
  only the copies currently deleted;
* arbitrary fresh edge insertions into already reported vertices
  need the separate outer accounting stated after (26).

The note makes no claim about decremental SSSP, negative input lengths,
or a path-query bound proportional to a loop-erased output's length.
