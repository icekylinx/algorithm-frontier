# Native commitment and contraction backends

[absorption.py](absorption.py) supplies exact structural interfaces;
[commitment.py](commitment.py) supplies original-optimum workload and two-size
clients. The [realization proof](../reference-realization.md) states the
separate mathematical and finite-reference costs. All inputs use exact integers
or `Fraction` values, original physical IDs and complete original rank tables.

```python
from fractions import Fraction
from absorption import RankTable, Absorption, position_commitment, padding_scale
from commitment import CommitmentBackend

# Full-marginal absorption can remove many binary units at one machine.
capacity = 10**100
engine = Absorption((RankTable(2, (0, capacity, capacity, capacity)),), (1,), (0,))
closed = engine.for_budget(0)
assert closed.removed == (0, 1)  # Includes the complete bottleneck plateau.
assert engine.lift(closed, ()) == ((capacity,), (0,))

# Minimax scalar padding, with an exact strict-active-set endpoint.
assert padding_scale(((Fraction(1, 10), 1), (2, 2)), 2) == (1, 2)

# Exact original two-size commitment client, retaining both type bases.
solver = CommitmentBackend(2, ((0, 1, 1, 1), (0, 2, 2, 2)), (3, 1),
                           budget=1, mode='two-size')
schedule = solver.optimize()
assert solver.backend.verify(schedule)
```

`Absorption` takes validated `RankTable` objects, one positive common size per
original type and a nonempty tuple of distinguished original type IDs. It
records one greedy full order. `closure(threshold)` materializes its canonical
threshold closure; `for_budget(k)` selects the smallest closure threshold with
residual distinguished rank at most the binary budget. `dominated(closure,x)`
produces contracted bases dominated by a supplied original schedule, and
`lift(closure,y)` combines legal contracted bases with the recorded assignments.
These schedules are **machine-major** rows, including original type columns.

`position_commitment(rank, exposures, k)` instead chooses an ordinary player
independent set with minimum bottleneck exposure, contracts only that matroid,
and returns its original remaining nonloops. It supports residual rank zero.
`eligibility(engine)` computes original eligible size intervals, small workload
exposures, the exact two-large-unit collision threshold and the Boolean
large-recipient rank. `padding_scale(pairs, D)` returns the optimum overhead and
an attaining positive scale for its stated one-dimensional certificate.

`CommitmentBackend(q, ranks, sizes, budget, divisor=None, mode='workload')`
takes ordinary rank-table tuples, a positive residual-rank budget and common
sizes. Its `target(T)` returns original integer type bases or a sound target
failure. `optimize()` performs original-grid search and also returns the better
actual additive-largest-job fallback by default. Its schedules are
**type-major** rows, matching the reused workload API. `bound(T)` exposes the
corresponding commitment load estimate.

The workload mode defaults to the exact finite-rank divisor and accepts a
larger supplied divisor. The `two-size` mode requires at most two active sizes,
uses the exact integer floor quota and admits noninteger size ratios; it does
not take a divisor. Empty and one-size inputs have their exact branches. This
client requires positive rank budget; the zero-budget structural commitment is
available through `position_commitment` separately.

The clients import the canonical many-size workload decomposition, upper-prefix
rounding and binary box/base primitives. They stream residual candidate bases
and exact LP active systems with explicit finite costs. They do not implement
the fast rank-local unit search, the full heterogeneous-large padding allocator,
or the separate specialized public two-size approximation. The model has no
assignment or setup-cost budget.

**Attribution:** icekylinx and GPT-6 Astra Pro.
