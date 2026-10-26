# A slack-only matching client and its directed path interface

**Research continuation, 25 October 2026.** This note independently checks a
proposed change to the top numerical objective for arbitrary general-graph
matching. The mathematical reduction is sound. It exposes a specific
nonnegative directed shortest-path problem and a useful monotonicity property
under exact shortest-path steps. The required dynamic, path-reporting,
implicit-update interface has not been constructed. No improved matching
running-time exponent is claimed.

The comparison allocation and structural ledger equations are imported from
[general matching proof](../../problems/general-matching/proof.md). The old
numerical implementation is in
[priced-logarithmic-steps-from-raw-cycles.md](priced-logarithmic-steps-from-raw-cycles.md). This note
changes its top objective and motion charge; it does not silently apply the
old symmetric raw-cycle backend to the new asymmetric charge.

## 1. Remove allocation logarithms but retain the feasible allocation

At a fixed structural state, the top variables satisfy

```math
\sum_{e\ni r}x_e=L,
 \qquad \sum_{e\ni d}x_e+s_d=L+p_d-Cw_d.
```

For the first, conservative formulation, retain `x_e>0` and `s_d>0`, with
the existing tiny padding and guarded magnitude ranges. Change the objective
to

```math
\Phi(s)=\sum_d\log s_d.
```

For a logical circulation direction `h`, use the asymmetric charge

```math
\mathcal C_f(h)=
       \sum_{e\text{ allocation}}\frac{(-h_e)_+}{x_e}
       +\sum_d\frac{|h_{s_d}|}{s_d}.
```

The numerator is `G_f(h)=sum_d h_(s_d)/s_d`. Increasing an allocation is
uncharged, while decreasing it is charged against its available value. Both
slack directions remain charged. This is a directed residual quantity; its
value generally changes on reversing a circulation.

## 2. The actual matching comparator is still a constant-ratio witness

Suppose the phase has the improvement promised by its target and has reached
a settled state with no available structural action. The matching comparison
constructs a nonnegative alternative allocation and slack vector with the
same conservation equations. Its increase in contact slacks has positive
normalized mass `P>12N`.

The total negative slack mass is at most the number of bins, hence at most
`N`. The total one-sided allocation charge is at most the number of physical
row incidences, hence at most `3N`: each decreased coordinate contributes at
most one because the alternative remains nonnegative. Writing these two
quantities as `Q_s` and `Q_x`, respectively,

```math
\frac{G_f(h)}{\mathcal C_f(h)}
     =\frac{P-Q_s}{P+Q_s+Q_x}
     \ge\frac{P-N}{P+4N}
     >\frac{11}{16}>\frac12.
```

No allocation logarithm is used in this calculation. The gap-to-direction
proof therefore survives the changed objective with an absolute margin.

The objective range and charged structural losses do not increase: there are
fewer logarithmic terms, each still has polynomially bounded positive
argument, and the earlier explicitly changed slack terms retain their
`O(log S)` individual loss bound. Positivity repairs of allocation
coordinates can retain the existing debt accounting. Their old possible
loss from a donor allocation logarithm disappears.

## 3. One-sided safety and objective progress

For an explicit signed walk representation, charge every donor traversal
before cancellation, and every slack traversal in either direction. Let `V`
be this raw charge and `G` its exact slack numerator. Suppose

```math
G\ge\rho V>0.
```

Choose a common step `eta` so that

```math
\rho/128\le\eta V\le\rho/64.
```

Every negative partial motion on an allocation coordinate is at most
`eta V` times that coordinate's starting value. Every absolute partial slack
motion has the same bound. Thus all coordinates remain positive throughout
an atomic application, even when the representation repeats coordinates or
contains cancellation.

The absence of a charge on positive allocation motion does not permit
unbounded intermediate magnitudes. At every row the total positive raw
allocation motion equals the total negative raw allocation motion, because
the complete represented object is a circulation. Its negative absolute
mass is at most `eta V * L`. Hence intermediate values are bounded by
`(1+eta V)L`, well inside the existing polynomial envelope.

Only slacks contribute curvature. Put
`u_d=eta h_(s_d)/s_d` and `z=eta V<=rho/64`. Then
`sum_d |u_d|<=z`, and Taylor's inequality gives

```math
\Phi(s+\eta h_s)-\Phi(s)
  \ge \eta G-
             \frac{\sum_d u_d^2}{2(1-z)^2}
  \ge \rho z-\frac{z^2}{2(1-z)^2}
  =\Omega(\rho^2).
```

Thus a constant-ratio directed answer would give constant progress, while an
inverse-subpolynomial ratio gives the familiar quadratic dependence on that
inverse factor. There is no mathematical need to put back the allocation
logarithms for safety or progress.

## 4. Exact directed cycle formulation

Construct the residual directed graph on rows, bins, and an auxiliary vertex
`z`. For each allocation incidence `e=(r,d)`, create

```math
\begin{array}{c|c|c}
 \text{arc}&\text{charge}&\text{gradient}\\\hline
 r\to d&0&0\\
 d\to r&1/x_e&0.
 \end{array}
```

For every slack create

```math
\begin{array}{c|c|c}
 z\to d&\alpha_d&+\alpha_d\\
 d\to z&\alpha_d&-\alpha_d,
 \end{array}
 \qquad\alpha_d=1/s_d.
```

Every feasible direction is represented by a nonnegative directed
circulation in this graph with exactly its one-sided charge. Canceling a
pair of opposite allocation traversals only reduces charge. Decomposition
into directed simple cycles preserves the numerator and positive charge.
Cycles avoiding `z` have numerator zero. Hence a positive-ratio answer can be
chosen as a simple cycle through `z` exactly once.

Let `dist_x(a,b)` be directed distance in the ordinary row/bin graph, with
donor costs `1/x_e` and receiver costs zero. The best positive cycle through
bins `a,b` has ratio

```math
\frac{\alpha_a-\alpha_b}
             {\alpha_a+\alpha_b+\mathrm{dist}_x(a,b)}.
```

Its action transfers allocation along an alternating path from `a` to `b`,
increases `s_a`, and decreases `s_b`. Positive gain means `s_a<s_b`: it
balances slack from the larger-slack endpoint toward the smaller one.

This directed formula removes the ordinary nonconservative gradient
obstructions from the old top objective. It does not make the distance
problem undirected. The reverse of a zero-cost receiving arc is a positively
priced donor arc, and replacing both by one symmetric edge changes the
optimization problem.

## 5. One static threshold test is ordinary nonnegative SSSP

Fix `0<beta<1`, for example `beta=1/4`. Choose

```math
A\ge(1-\beta)\max_d\alpha_d.
```

In a new directed graph, scale ordinary donor costs by `beta`, keep receiving
costs zero, and add a new source `z_*` with an arc to every bin `d` of cost

```math
A-(1-\beta)\alpha_d.
```

All weights are nonnegative. Do not add any return arcs to `z_*`. Let `D(d)`
be the shortest distances from this source. A cycle of one-sided ratio
strictly greater than `beta` exists if and only if some bin `b` satisfies

```math
D(b)<A-(1+\beta)\alpha_b.
```

Indeed a source path begins at one bin `a` and has cost
`A-(1-beta)alpha_a + beta dist_x(a,b)`. Comparing it with the threshold is
exactly the inequality

```math
\alpha_a-\alpha_b
          >\beta(\alpha_a+\alpha_b+\mathrm{dist}_x(a,b)).
```

An ordinary static Dijkstra computation and path reconstruction therefore
give a complete deterministic threshold oracle in `O((m+n)log(n+2))`
scalar work. A returned path starts at a different bin from its endpoint,
since the direct source arc alone cannot pass the strict test.

This exact static oracle detects the comparator from Section 2 with a
constant margin and returns a constant-ratio direction. Repeating a full
computation after every numerical step is too expensive for the desired
matching bound; the statement is a closed static reduction, not a closed
dynamic algorithm. Section 6.1 below gives a conservative integer-priced
implementation, so the static claim need not be read only in a real-arithmetic
model.

## 6. A positive monotonicity lemma for exact shortest-path steps

There is additional structure beyond arbitrary mixed directed edge updates.
Suppose the source-path to the accepted endpoint `b` is an exact shortest
path, with first bin `a`, and let `D` be the exact distance labels immediately
before the step. Transfer a positive amount `eta` along its ordinary path,
increase `s_a` by `eta`, and decrease `s_b` by `eta`. Assume every relative
slack change and donor decrease is at most a small `z`, with

```math
z\le1/64,\qquad\beta=1/4.
```

Keep the source offset `A` fixed. After this step, all old labels remain
feasible lower distance labels for the new nonnegative graph. Consequently
the true shortest distances can only increase.

### Ordinary donor and receiving incidences

For a donor incidence on the path, `x_e` decreases and its directed donor
cost `beta/x_e` increases. This cannot violate an old shortest-distance
inequality.

For a receiving incidence on the path, `x_e` increases and the reverse donor
cost decreases. The receiving arc `r->d` itself has zero cost and lies on an
exact shortest path, so `D(r)=D(d)`. Its reverse arc therefore continues to
have nonnegative reduced cost after any positive new donor price. All other
ordinary arcs are unchanged.

### The initial source bin

The increase in `s_a` decreases `alpha_a`. The corresponding source-arc cost
`A-(1-beta)alpha_a` increases, so it also preserves feasibility.

### The terminal source arc

The decrease in `s_b` increases `alpha_b`. However the acceptance inequality
gives the old source arc to `b` a strict margin over its old distance:

```math
[A-(1-\beta)\alpha_b]-D(b)>2\beta\alpha_b.
```

The drop in that arc's cost after the step is at most

```math
(1-\beta)\alpha_b\frac{z}{1-z}
                         <2\beta\alpha_b.
```

It therefore remains at least `D(b)`. This is the only source-arc decrease.

### The offset remains valid

Acceptance also implies
`alpha_a>((1+beta)/(1-beta))alpha_b`. The small step ensures the new
`alpha_b` is still smaller than the old `alpha_a`. The starting reciprocal
decreases and all other reciprocals stay fixed. Thus the global maximum
slack reciprocal does not increase during this numerical step, and the same
`A` continues to make every source arc nonnegative.

### Exact scope

The lemma concerns one exact shortest-path step and unchanged structural
topology. Between successive steps, exact distances may need to be updated.
External expansions, contractions, debt changes, and numerical padding are
separate events and are not covered by this monotonicity claim.

An arbitrary approximate path need not have tight receiving arcs in the
maintained feasible potential. The reverse-price argument cannot be applied
to such a path without an additional potential/path guarantee. The lemma is
therefore a precise candidate update restriction for a future data structure,
not an automatic application of a generic approximate distance oracle.

### 6.1 A finite-word static oracle with the same monotonicity

Fix one sufficiently large polynomial integer scale `H` throughout the
structurally unchanged numerical interval. Use the guarded slack range to
ensure

```math
H\min_d\alpha_d\ge8(N+2).
```

For each allocation and slack, compute the conservative integers

```math
c_e=\left\lceil\frac{H}{4x_e}\right\rceil,
 \qquad \sigma_d=\left\lfloor\frac{3H}{4s_d}\right\rfloor,
 \qquad \tau_d=\left\lceil\frac{5H}{4s_d}\right\rceil.
```

Receiving arcs still have length zero. Give donor arcs length `c_e`, and
give the artificial source arc to bin `d` length `A-sigma_d`, where integer
`A>=max_d sigma_d`. Run exact integer Dijkstra and accept an endpoint `b`
precisely when

```math
D_{\rm int}(b)<A-\tau_b.
```

If the returned source path begins at `a`, this strict inequality implies

```math
\frac34H\alpha_a-\frac54H\alpha_b
       \ge\sigma_a-\tau_b
       >\sum_{e\text{ donor on path}}c_e
       \ge\frac H4\mathrm{len}_x(a\leadsto b).
```

Thus every accepted path has true one-sided ratio greater than `1/4`.
There is no false acceptance caused by rounding.

Conversely, a true path of ratio greater than `1/2` satisfies
`dist_x(a,b)<alpha_a-3alpha_b`. Its unrounded threshold margin at `beta=1/4`
is at least `H alpha_a/4` (in fact the preceding inequality gives more).
The source floor, terminal ceiling, and donor ceilings lose less than the
number of donor arcs plus two. A simple ordinary path has at most `N` donor
arcs. The condition on `H alpha_min` therefore leaves a strictly positive
integer threshold margin. Every strong comparator is still detected.

The monotonicity proof also holds for these integer labels. Donor costs
cannot decrease when their allocation decreases. A reverse donor cost can
decrease on a receiving incidence, but its zero-length receiving arc is
tight on the exact integer shortest path. At the starting bin the source
cost increases. At the terminal bin, the old acceptance gives source-arc
margin greater than

```math
\tau_b-\sigma_b\ge H\alpha_b/2.
```

For a relative slack decrease at most `z<=1/64`, the source-cost decrease is
at most

```math
\frac34H\alpha_b\frac{z}{1-z}+1
                                  <H\alpha_b/2.
```

Hence every old integer label remains feasible after the update. True
positive-ratio acceptance also guarantees that the maximum true slack
reciprocal does not increase. Since the floor is monotone, `max sigma_d`
does not increase either, and the same integer offset `A` stays valid.

All primal values have the existing common dyadic encoding and polynomial
magnitude bounds. Each displayed reciprocal floor or ceiling is one
`O(log S)`-bit integer division; all graph costs, distances, and path sums
have `O(log S)` bits up to the fixed precision constants. The static oracle
and its explicit shortest-path tree therefore use ordinary finite-word
operations. If a finite step size is needed, donor upper prices `4c_e/H`
and rounded upper slack prices give a common-denominator motion bound;
the two-endpoint slack numerator itself has only two reciprocal terms.

This resolves the static arithmetic issue. It does not resolve the dynamic
maintenance, path reporting, or lazy threshold-discovery obligations.

## 7. Positive allocation motion can be charged for repricing

Removing allocation logarithms from the objective does not make their
unpaid positive motion harmless to implementation. A large increase can
decrease `1/x_e` by many relative factors and invalidate a donor price.
Nevertheless the *number* of required price changes has a useful
history-wide bound.

Use `sum_e log x_e` only as an accounting potential, without optimizing it.
The active coordinates lie in a guarded polynomial range. A numerical step
with raw one-sided motion `z=eta V<=1/64` has total negative log variation at
most `2z`, since each net coordinate decrease is charged against its old
value. Total positive log variation over a run is at most total negative log
variation plus the initial/final potential range and the changes caused by
explicit coordinate births, deletions, or settings.

For `A_ext` explicitly edited allocation records and `J` numerical steps,
this gives an aggregate variation bound

```math
O((N+A_{\rm ext})\log S+\sum_{j=1}^J z_j).
```

A register reset only after a relative `tau` change can consequently occur
at most this quantity times `O(1/tau)`, provided resets use the actual new
value and the usual hysteresis. For `z_j=Theta(rho)` and `tau=Theta(rho)`,
the count is

```math
O\left(
                         J+\frac{(N+A_{\rm ext})\log S}{\rho}
                       \right).
```

This bound is an event-count argument. It does not by itself discover which
implicitly updated coordinates cross their thresholds. A new one-sided
forest/path watcher and complete occurrence/retirement protocol are still
required. The old symmetric absolute-motion watcher cannot simply be
assumed to report arbitrarily large free positive changes at the same cost.

## 8. Objective-neutral top normalization becomes possible

A transportation cycle pivot preserves every row sum and bin load. It
therefore preserves every slack and the new objective *exactly*. Unlike the
old top objective, the slack-only objective permits normalizing the actual
top allocation to a forest-supported carrier. This is a genuine additional
representation freedom.

There is nevertheless a separate numerical obstruction to using the old
carrier theorem as a complete solution. A large pivot can reduce many donor
allocations, make many of them zero, and change many `1/x_e` prices. Constant
carrier topology recourse does not imply a short directed-price update list.
Allowing zero allocations would also require removing their donor arcs while
keeping their zero-cost receiving arcs available.

One could instead try to search by carrier path minima and make bottleneck
pushes, avoiding reciprocal-price maintenance. Then a history-wide bound on
pivots, reinserted noncarrier incidences, and changing paths would be needed.
Neither that bound nor the required path-search interface follows from
objective neutrality alone.

## 9. The dynamic contract that remains missing

To improve the matching exponent through this route, a provider must support
the directed graph of Sections 4--5 with the following combined contract:

* actual-size initialization and charged structural edits;
* simultaneous donor-cost increases and reverse donor-cost decreases caused
  by a reported path step;
* changing slack source prices and a correctly maintained offset or equivalent
  normalization;
* detection of a constant-gap threshold violation and a current, explicit or
  valid implicit path witness;
* safe application of the whole circulation, including one-sided threshold
  discovery and complete value-transfer/lifetime metadata;
* total work sufficiently below the existing `4/5` envelope, rather than only
  monotonicity of a set of abstract numerical labels.

The exact monotonicity lemma may be useful in designing such a provider.
It does not make all edge updates decremental: some edge weights decrease.
Nor does the currently assembled undirected APSP or strong-forest machinery
apply to the asymmetric donor/receiver metric.

A relevant recent public result is Hanqing Li,
[*Almost-Linear Decremental Single-Source Distance Estimates in Directed
Graphs via Cut Balance*](https://arxiv.org/html/2610.07468v1), submitted
5 October 2026. Its stated output is simultaneous numerical distance
estimates under decremental updates; it explicitly excludes fast path
reporting. Those distinctions matter here. This note does not claim that
directed decremental numerical estimates are unknown, or that the result
already supports the mixed path-induced updates and witness contract above.

## 10. Result of this investigation

A further independently checked refinement is recorded in
[slack-potential-semantic-certificate.md](slack-potential-semantic-certificate.md). Any feasible old distance
potential gives a maintained scalar semantic LOW certificate, and current
threshold-passing paths in its original exact shortest-path tree preserve
that potential throughout a monotone fixed-tree epoch. The note explicitly
leaves the epoch refresh count open.

[coarse-directed-paths-for-slack-matching.md](coarse-directed-paths-for-slack-matching.md) gives a second refinement:
dyadic slack-price buckets turn a directed factor-$`\Gamma`$ path provider
into a direction of ratio at least $`1/(8+6\Gamma)`$. This relaxes the
required distance accuracy, while leaving dynamic path reporting and
potential-compatible receiving arcs as separate unproved obligations.

The slack-only change passes the matching comparison, safety, progress, and
static threshold-reduction checks. It also gives an exact positive
monotonicity lemma under shortest-path updates and a separate logarithmic
budget for positive allocation repricing. These properties are stronger than
the generic signed-gradient information used by the current raw-cycle
backend.

The unresolved work is algorithmic: maintain and report the required
directed paths, honor the one-sided update protocol, and bound the full
history cost. Until that interface is proved, the general matching theorem
remains at exponent `4/5`; this note is a concrete alternative direction,
not a new exponent obtained by rebalancing old parameters.
