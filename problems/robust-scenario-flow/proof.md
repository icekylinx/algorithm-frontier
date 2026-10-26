# Adaptive selected flow under explicit network scenarios

A common permitted set of q-c commodities can be selected to obtain
nearly optimal concurrent service in every explicitly listed network
scenario. Each scenario has its own adaptive routing. All of its
capacities and all explicitly listed nonnegative routing budgets
are respected exactly. The deterministic time is

$$
\Gamma(1/\epsilon)^c\operatorname{poly}(H),
       \qquad \Gamma(R)=\frac{R^R}{(R-1)^{R-1}},
 \tag{S1}
$$

with polynomial space and common service at least
(1-epsilon)OPT. H includes the total explicit scenario description.
There is no exponent depending on the scenario count or the number
of routing-budget rows.

After proving this corollary, the note gives a parameter-preserving
Hitting Set reduction: exact full-demand admission is W[2]-hard in
c even without routing budgets, with unit demands and one shared
bottleneck in each scenario. Every positive-capacity scenario in
that construction has an underlying forest. This obstruction is
specific to arbitrarily many listed scenarios and exact admission.

## 1. Scenario model and adaptive comparator

Let P={1,...,q} be one common commodity ground and B a nonempty
family of r-element subsets, with r>=1 and c=q-r. B has a paid
polynomial restriction selector. Thus it can be an unrestricted
r-subset family, a matroid basis family, two common bases, or any
other fixed family meeting that exact selector interface.

There is a nonempty finite explicit list Omega of scenarios. For
each omega, specify a directed or undirected finite network,
finite nonnegative rational capacities, distinct terminals for
each commodity, positive rational demand scales d_i^omega, and
any explicitly listed collection of nonnegative routing-budget
rows. The network topology, terminals, demand scales and budget
data may vary by scenario. The common-topology failure model is
a special case, using zero capacities for unavailable edges.

Choose one I in B. After the scenario is known, its flows may be
computed specifically for that scenario. A common normalized rate
lambda is feasible when each omega admits routing
lambda*d_i^omega units for every i in I, obeying all capacities
and all budgets in that scenario. Define OPT as the largest such
lambda over permitted I.

Only the selected commodity set and common rate are shared across
scenarios. The result concerns adaptive routing and does not require
common path fractions or an oblivious routing template. All budgets
in this model constrain their own scenario's routing; there is no
additional unmodeled coupling of different scenarios' flow variables.

As in the single-scenario theorem, zero routing is feasible and
distinct terminals with finite capacities bound the common rate.
Empty selection families and the rank-zero selected family are
handled separately. The nontrivial statement assumes r>=1 and at
least one scenario.

## 2. Intersection of service regions preserves the packing interface

Let U_omega be the nonnegative normalized-service region of one
scenario, defined by its explicit arc-flow conservation, capacities
and routing budgets. The single-scenario proof in
[Near-optimal concurrent flow with few rejected commodities and exact selection constraints](../selected-flow/proof.md) shows that each
U_omega is bounded, convex and downward closed. It also gives an
exact polynomial separator returning a globally valid row

$$
\sum_{i\in P}a_i z_i\le h,
                         \qquad a_i\ge0,\quad h\ge0,
 \tag{S2}
$$

of polynomial binary length, whenever the queried z is outside
U_omega. The row follows from normalized arc-potential Farkas
certificates, including a nonnegative multiplier for every budget.

The robust service region is exactly

$$
U=\bigcap_{\omega\in\Omega}U_\omega.
 \tag{S3}
$$

It contains zero and is bounded, convex and downward closed. To
separate a nonnegative query z, check the scenarios in a fixed
order. If one rejects z, return its row (S2). That row is valid
for U because U is contained in the scenario region. If all
checks accept, z is feasible in every scenario; the corresponding
independent routing witnesses establish z in U.

The oracle work is polynomial in the total input H. There is no
need to combine the scenario rows into a smaller family or to
enumerate facets of their projection. Zero insertion outside a
current selected ground Q uses the same original q-coordinate
intersection throughout the omission recursion.

For a target T>0, apply the weighted prefix-free theorem to U with
t=T and b=(1-epsilon)T. It returns a permitted I with b*1_I in
every U_omega, or correctly reports that no permitted I can have
T*1_I in all scenarios. Its parameter is c=q-r, counted once.
Repeating the separator over scenarios changes only its polynomial
cost and does not multiply c by the number of scenarios.

## 3. Fixed-set reoptimization and the rational denominator bound

For a fixed I, maximize a variable lambda in the combined LP whose
variables are all scenario-specific arc flows and lambda. Impose
every scenario's own flow conservation with demands lambda*d_i^omega,
its capacities, and its routing budgets. Set flows of outside-I
commodities to zero. This LP has polynomially many variables and
constraints in the total explicit input. It is nonempty at zero.

A uniform finite upper bound is obtained from any one scenario
omega_0:

$$
V=\max_{i\in P}
          \frac{\sum_{e\text{ out of }s_i^{\omega_0}}u_e^{\omega_0}}
               {d_i^{\omega_0}}.
 \tag{S4}
$$

For an undirected network, use the sum of incident physical edge
capacities. Every common rate on a nonempty I is at most V.
Include 0<=lambda<=V explicitly. The other variables are bounded
by their scenario capacities, so the combined LP is bounded.

Its dimension and the binary lengths of its original rational
entries have known polynomial bounds. Clearing denominators row
by row and applying the determinant bound gives a uniform
computable integer D of polynomial binary length that bounds the
denominator of every fixed-I optimum lambda_I. The finite maximum
OPT=max_I lambda_I has the same bound. Lower-dimensional feasible
LPs are covered by the active-row argument in
[Rational comparator recovery without splitting the approximation error](../whole-ground-allocation/rational-optimization.md).

Apply that rational-comparator lemma with alpha=1-epsilon=A/B and
grid delta=1/(2BD^2). The one-sided search saves a set with
lambda_I>=alpha*L and finishes at L>OPT-delta. Exact optimization
of the original combined fixed-I LP then forces
lambda_I>=alpha*OPT: otherwise the positive rational gap would
be at least 1/(BD^2), contradicting the search bound. The returned
LP witness supplies the full list of adaptive scenario routings.

The family B, all scenario data and the fixed-set objective remain
independent of the target. This is why rational recovery applies.
There is no integral rounding, and consequently no additive error
or budget violation. The omission algorithm and each explicit LP
use polynomial workspace, proving (S1).

Equivalently, because the scenario routings have no cross-scenario
coupling, lambda_I is the minimum of the individual scenario
optima for that same I. This observation can simplify exact
reoptimization, but the combined LP already proves the required
uniform rational bound and constructive polynomial complexity.

## 4. Failure scenarios and the distinction between routing and selection budgets

An explicit list containing the intact network and every single-
edge-failure scenario has polynomial total size. Therefore the
theorem applies directly to selecting commodities whose nearly
optimal common throughput survives every one of those failures,
using a new feasible routing after the failed edge is known.
The statement remains valid when the optimum is zero because
some selected terminal pair cannot survive a listed failure.

Multiple nonnegative routing budgets are exact because they are
linear constraints inside each continuous scenario LP. They add
nonnegative Farkas multipliers and do not require rounding.
Extra constraints on I itself still need the stipulated exact
restriction selector. For example, two matroids and one fixed
linear selection-cost bound can be implemented by weighted
matroid intersection. This corollary does not assert a polynomial
selector for an arbitrary collection of additional selection budgets.

The scenario count must be polynomial in the stated total explicit
description. No claim is made for an exponentially large implicit
uncertainty family without a separately established polynomial
scenario/separation oracle and rational-description bound.

## 5. Exact unit admission encodes Hitting Set without routing budgets

The classical Hitting Set problem asks whether a universe P of
q elements has a subset D of size at most k intersecting every
set S in an explicitly listed family A. It is W[2]-complete when
parameterized by k; see the primary paper of Bart Jansen,
[On Structural Parameterizations of Hitting Set: Hitting Paths in
Graphs Using 2-SAT](https://jgaa.info/index.php/jgaa/article/view/paper413),
Journal of Graph Algorithms and Applications 21(2), 2017. The
following reduction is proved here.

Empty sets make a Hitting Set instance immediately NO. An empty
set family is immediately YES. If k>=q and there are no empty
sets, the answer is YES. These polynomially decidable cases may
be mapped to fixed YES or NO admission instances. Thus consider
at least one nonempty set, all sets nonempty, and 0<=k<q. Set
r=q-k>=1 and let B contain all r-element commodity sets, so its
restriction selector is trivial and its corank is exactly c=k.

Use pairwise distinct terminals s_i,t_i for each i in P and two
additional vertices x,y. The common directed topology contains

$$
s_i\longrightarrow t_i,\qquad
      s_i\longrightarrow x,\qquad
      y\longrightarrow t_i\quad(i\in P),
      \qquad x\longrightarrow y.
 \tag{S5}
$$

All commodities have demand scale one. There are no routing costs
or routing budgets. For each S in A create one scenario with
capacities

| Arc | Capacity when i is in S | Capacity when i is outside S |
|---|---:|---:|
| s_i to t_i | 0 | 1 |
| s_i to x | 1 | 0 |
| y to t_i | 1 | 0 |

The central arc x to y has capacity |S|-1. All capacities are
nonnegative integers at most q, and the entire construction is
polynomial in the Hitting Set input.

In scenario S, a commodity i outside S has its private unit arc.
A commodity i in S can reach its own sink only along
s_i,x,y,t_i. Flow cannot exit through another commodity's sink:
such a vertex has no outgoing arc and has zero prescribed balance
for commodity i. Thus every selected member of S must place its
entire flow on the central bottleneck.

For a selected set I, routing all selected commodities at unit rate
is consequently feasible in that scenario exactly when

$$
|I\cap S|\le |S|-1.
 \tag{S6}
$$

Necessity follows from the central capacity. Sufficiency follows
by using the private arcs outside S and the specified three-arc
paths inside S; every branch arc then carries at most one unit.
This argument allows fractional flow, but fractions cannot bypass
the unique required bottleneck.

Condition (S6) is equivalent to (P\I) intersection S being nonempty.
Therefore the same r=q-k commodities can be admitted at full unit
rate in every scenario if and only if the rejected k-set P\I hits
every S in A. A hitting set of size at most k can be extended to
size exactly k, because k<q; adding rejected elements preserves
the hitting property. This proves both directions of the reduction
with parameter c=k.

The common topology is acyclic: place sources before x, x before
y, and y before sinks. After zero-capacity arcs are removed, each
scenario's positive-capacity graph consists of one double-star
joined through the central bottleneck, together with disjoint
private edges. If the central capacity is zero, the joined piece
splits into two stars. In either case its underlying graph is a
forest. Thus exact admission remains W[2]-hard in c even under
these simple per-scenario routing structures.

## 6. The hardness statement has an exact and explicit scope

Every selected commodity in the construction has an outgoing
capacity-one branch, so any nonempty selected set has concurrent
rate at most one. A YES Hitting Set instance has robust optimum
exactly one. In a NO instance, each selected set contains some
S completely, and that scenario bounds its rate by
(|S|-1)/|S|<1. Hence the reduction also proves W[2]-hardness of
deciding whether robust optimum equals one.

The shortfall may be as small as 1/q. It is not a fixed constant
approximation gap. The reduction therefore does not contradict
the Gamma(1/epsilon)^c scheme or establish a lower bound against
that scheme at a fixed epsilon. It does not determine the optimal
exponential base or an optimal dependence on epsilon.

The construction uses an arbitrary explicit collection of scenarios.
It does not prove the same hardness for one scenario without
routing budgets, nor for the special family consisting only of
individual edge failures. A separate companion reduction can
encode Hitting Set in one scenario using many routing-budget rows;
that is a different stated scope.

The positive theorem is thus a parameterized approximation scheme
for adaptive robust selection, while the reduction excludes an
exact F(c)poly(H) full-admission algorithm in this broader scenario
model unless FPT=W[2]. No exhaustive publication-priority claim is
made for either formulation.

---

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
