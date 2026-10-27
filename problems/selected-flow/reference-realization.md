# Exact concurrent-flow primitives and their certificates

This note completes the executable fixed-set optimization and nonnegative
separation interfaces of the [selected-flow theorem](proof.md), including
the [shared setup-budget model](../shared-setup-flow/proof.md). The shipped
[implementation](reference/concurrent.py) is a separate exact reference
baseline; its simplex and selected-set enumeration do not inherit the
research theorem's corank running time.

## Native model and faithful formulation

Fix a nonempty list of distinct original commodity IDs. Introduce one
nonnegative rate coordinate and one nonnegative variable for every selected
commodity and directed arc record. Encode each conservation equality by its
two opposite inequality rows. A directed physical record gets one capacity
row; an undirected record gets a single row summing both of its directional
variables over all commodities. Original parallel records stay distinct.
Routing-budget rows contain their actual nonnegative directional charges.

For the shared-budget model, subtract the sum of setup fees of this actual
selected set from the shared cap. A negative residual proves the set
unaffordable even at zero rate. Otherwise append its routing-charge row with
that residual as the right side. This subtraction is repeated for every
selected set; it is never reused from a cheaper set. Unselected commodities
have no variables and therefore no routing cost or capacity consumption.

All right sides are nonnegative, and the origin is feasible. Each directed
flow coordinate is bounded by its physical capacity. Source conservation
bounds the rate by total physical capacity divided by the smallest selected
demand scale. Add this redundant rate row explicitly. Thus the LP is bounded
and nonempty even with zero capacities, disconnected terminals, zero budgets,
zero shared residual, or no arcs. Its feasible solutions correspond exactly
to the native fixed-set routings, preserving rate and every budget. This
establishes the reduction independently of a particular LP optimizer.

## Exact pivoting and optimality certificates

Write the resulting LP in the following machine-readable convention:

```text
maximize c*x subject to A*x <= b and x >= 0, with b >= 0.
Introduce slack s: A*x + s = b.
```

The slack basis starts feasible. The tableau stores the transformed rows of
`[A I]` and `b`, and initially stores objective coefficients `[-c 0]` with
constant zero. Every pivot uses exact rational row operations. The entering
variable is the least indexed column with negative objective coefficient.
Among positive pivot entries, choose a minimum ratio, breaking ties by the
index of the leaving basic variable. Hence every new basic solution stays
nonnegative, and the objective equation remains an identity on the original
constraints. Degenerate pivots are permitted.

These are the least-index entering and leaving rules of Bland's finite
pivoting theorem. The rule terminates without revisiting a basis, even for
degenerate feasible LPs. This is an explicit published mathematical dependency:
[Bland, *New Finite Pivoting Rules for the Simplex Method*, Section 1, 1977](https://people.ohio.edu/melkonia/math4620/bland.pdf).
The flow LP is bounded, so an improving unbounded ray cannot occur.

At termination, let `y` be the objective row's coefficients on the original
slack columns. Row-operation invariance gives the identities

```text
objective coefficient on x_j = (A^T*y)_j - c_j;
objective coefficient on slack_i = y_i;
objective constant = b*y.
```

All terminal objective coefficients are nonnegative. Thus `y` is dual
feasible. Basic objective coefficients are zero and all nonbasic primal
coordinates are zero, so the returned basic solution has objective exactly
`b*y`. Weak duality proves its optimality. The search-free verifier checks
these same conditions on the original formulation, without trusting any
pivot history:

```text
x >= 0; A*x <= b; y >= 0; A^T*y >= c; c*x == b*y.
```

These equalities also explain why simply increasing a claimed rate or
replacing its dual with zero is rejected, including for disconnected
zero-optimum instances: dual feasibility still constrains the rate column.
The verifier establishes fixed-set optimality. It does not certify the
behavior of an arbitrary external selection predicate.

## Normalized Farkas rows

The separator implements Sections 3--4 of the main proof using one
nonnegative length per physical edge, one nonnegative multiplier per routing
budget, and positive/negative parts of every commodity potential. Its rows
are the directed potential inequalities, the nonnegative terminal gaps,
and a bound of one on the sum of all nonnegative coordinates. Every right
side is zero except this normalization row, so the same feasible-origin
simplex applies.

The objective is the queried service weighted by demand and terminal gap,
minus the capacity-weighted lengths and budget-weighted multipliers. The
zero vector is feasible. The existing Farkas argument proves that a positive
optimum is equivalent to infeasibility of the service query: negative terminal
gaps can be replaced by zero potentials because every effective arc charge
is nonnegative, and every strict certificate can be positively normalized.
An optimum of zero therefore means membership. No routing witness is claimed
from that return value alone.

For a positive optimum, decode lengths, multipliers and potentials. The
coefficient of a commodity is its demand times its terminal potential gap.
The row capacity is the capacity-weighted sum of lengths plus the
budget-weighted sum of multipliers. Telescoping conservation against the
potentials proves the resulting row valid for every feasible routing, and
the optimized positive excess proves strict violation at the queried service.
For undirected records, the same physical length occurs in both potential
inequalities and exactly once in the capacity sum. No independent directional
capacity is introduced.

This realizes the exact separation operation, but no polynomial-time claim
for this simplex implementation is inferred from the existence of a
polynomial-time rational LP algorithm in the theorem.

## Enumeration, arithmetic and storage

For fixed selected rank, iterate the original commodity combinations in
lexicographic order and apply the fixed permitted-family predicate. Skip
unaffordable sets; optimize every other set; retain an attaining maximum.
Finiteness and the fixed-set correspondence prove exact global optimality.
An empty affordable permitted family returns `None`, which is distinguished
from a legal zero-rate answer. Setup fees and capacities are never expanded
into unary copies or enumerated by numerical magnitude.

For a formulation with `N` original variables and `M` inequalities, the
slack tableau has `M*(N+M+1)` entries. There are at most
`binom(N+M,M)` bases; Bland termination gives this finite pivot bound.
Each pivot takes `O(M*(N+M))` rational operations. Determinant bounds on
basis inverses give polynomial bit length per exact tableau entry in the
explicit rational LP encoding; intermediate products in one pivot obey
the same polynomial bit bound up to a constant factor. Only one tableau
and one best certificate are kept. Therefore workspace is polynomial,
while the supplied running-time bound includes the potentially exponential
basis count. Selected enumeration multiplies that bound by at most
`binom(q,r)` and adds the paid predicate costs. These bounds are deliberately
separate from the corank approximation theorem, which uses a paid
polynomial-time LP primitive and a different selection recursion.

The independent verifier uses `O(M*N)` rational operations after rebuilding
the fixed-set matrix; input and certificate bit lengths are charged.
There is no dependency on the number of simplex pivots during verification.

## Review boundary and proof dependency audit

The selected-flow proof's nonnegative separator, zero-rate handling,
fixed-family denominator bound and exact returned-set reoptimization have
been checked together with the complete weighted first-crossing proof,
rational comparator lemma and streamed whole-ground conversion. The latter
uses the sharp algebraic constant only for fixed rational accuracy; the
public cards retain that qualification. An undirected source rate is bounded
by total physical capacity despite paired arc variables because their sum
has one shared capacity.

For shared setup fees, the minimum-setup restriction optimizer must attain
its cost on the very set returned. Along a protected optimum's branch its
minimum is at most that optimum's setup fee, leaving at least the optimum's
routing budget. This is the invariant that justifies applying a newly
computed separator after every omission. Unrelated extra selection budgets
cannot be silently added to that optimizer. Routing-only budgets are safe
because their rows remain fixed throughout.

The research proofs retain exact rational LP, Farkas duality and the specified
paid selection or minimum-setup oracle as mathematical dependencies. The
reference implementation removes a software gap for explicit fixed-set
optimization and separation; it does not replace those paid polynomial-time
primitives by a polynomial-time simplex theorem, implement the omission
recursion, or establish external peer review or formal verification.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
