# Native workload decomposition and upper rounding

[workload.py](workload.py) implements the full-machine workload construction,
binary scaled-base decomposition and joint per-machine upper-prefix rounding.
The input has an explicit nonnegative machine count, complete integral job-rank
tables and positive common sizes given by integers or `Fraction` values.
Original mandatory bases remain exact. This model has no assignment budget.

```python
from fractions import Fraction
from workload import WorkloadBackend

model = WorkloadBackend(
    2,
    ranks=((0, 1, 1, 1),) * 3,
    sizes=(Fraction(1, 2), 1, Fraction(3, 2)),
    eta=Fraction(1, 3),
)
schedule = model.optimize()
assert model.verify(schedule)
```

Schedules are tuples of original type-major integer machine vectors.
`verify` checks all original bases, and `load` evaluates actual makespan.
`target(T)` returns an `Outcome`: `counts` is an actual complete schedule on
success; otherwise `failure="infeasible"` is a sound original full-target
rejection. The output bound includes the largest smaller-job size as an
explicit additive term. Positive rational targets are rounded down to the
working grid, which contains every original integer schedule load.

`target(T, budget=k, divisor=D)` implements the private-slack refinement.
It distinguishes `failure="cap"`, which is not original infeasibility.
`threshold(k,D)` computes the attained cap threshold; private optimization
compares against the larger of that threshold and the original optimum.
The divisor must satisfy the finite-rank condition in the companion theorem.
`optimize` compares its actual workload output with a separate additive-largest-
job fallback by default. `with_fallback=False` isolates the workload/cap output.

The reusable native interfaces are:

- `decompose(ranks, multipliers, workload)` returns integer bases of the
  scaled original ranks with exactly that machine workload. Multipliers and
  counts are binary; the routine creates no multiplier or resource copies.
- `upper_round(ranks, sizes, fractional, q)` restores every original base
  jointly, with per-machine added load at most the largest active input size.
  Zero-rank types do not enlarge that bound.
- `state(T, quantum)` forms the capped workload and fixed full-machine dual.
  A missing state indicates genuine rank loss. The quantum must divide the
  original sizes and target.
- `reconstruct(state, lower, large_counts)` completes an independent integral
  full-machine dual lower vector, restores original smaller types and splits
  the fixed largest-class base among its original types. Committed machines
  may have lower quota zero; no private insertion is implicitly required.

Generic mandatory-base LP/streamed-vertex primitives are imported from the
canonical intrinsic reference. Its optional-allocation, disposal and lower-
rounding model is not used here. The two-size complete-table box and binary
base-augmentation helpers are also reused. This reference selects weak bases
by explicit subset enumeration, rather than the rank-dependent local search.
It charges that enumeration and streamed LP active systems separately from
the fast theorem. It keeps polynomial rational workspace in the full explicit
table/input encoding, without numeric count enumeration or storing all LP
vertices. See the [realization proof](../reference-realization.md).

```sh
python3 problems/many-size-scheduling/verify/check_workload.py
```

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
