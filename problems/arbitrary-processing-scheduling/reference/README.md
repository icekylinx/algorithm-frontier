# Occupied profiles and joint exact-table recovery

[profiles.py](profiles.py) implements the occupied-bin profile construction of
[Theorem PS](../proof.md). It accepts arbitrary finite complete recipient-rank
tables, nonnegative rational machine/type processing times and costs, `None`
eligibility masks, and one exact assignment budget. Integers and `Fraction`
values are accepted; floating point inputs are rejected.

```python
from fractions import Fraction
from profiles import Instance, ProfileBackend

instance = Instance(
    ranks=((0, 1, 1, 1), (0, 1, 1, 1)),
    times=((Fraction(1, 4), 1), (Fraction(2, 3), 0)),
    costs=((0, 1), (1, 2)),
    budget=2,
)
schedule = ProfileBackend(instance, epsilon=Fraction(1, 2)).optimize()
```

Schedules use machine-major, then type order. `target(T)` returns an integral
weak success within the requested factor or a sound full-target failure `None`.
`optimize()` detects original-total/budget infeasibility or optimizes by the
canonical one-sided rational-grid search. Zero targets are tested exactly.

Only actual occupied big bins are grouped. `profile_counts` keeps one binary
counter per occupied bin and prunes by both remaining count and remaining lower
load before descending. Both occupied-bin traversal and paused machine-family
iteration use explicit bounded stacks, with no language recursion-depth limit.
Their families are never cached in a Cartesian-product table. Even a binary
tiny accuracy creates no accuracy-sized array or full bin universe.

The joint `Plan` interface is shared with the
[bucket client](../../processing-bucket-tradeoff/reference/README.md). Its disjoint
integer count groups and fractional load groups partition the allowed original
pair coordinates. One LP retains all original resource bases and the budget;
one recovery keeps the integer caps and replaces the load groups by full
upper-prefix ceilings, minimizing actual cost on the original full-total face.

The module imports exact rational elimination, original-total coordinate
elimination, rank-table inequalities, integer-count enumeration, zero feasibility
and grid search from the canonical
[two-time backend](../../two-time-scheduling/reference/scheduling.py). A local
data adapter validates arbitrary times; the canonical two-time model is unchanged.
This reference retains the inherited LP-vertex and numeric integer-count
enumeration costs, including potentially exponential vertex storage. It does
not implement Theorem PS's polynomial oracle primitives or overall polynomial
workspace; the profile iterator itself has the proved binary-space contract.

The [realization proof](../reference-realization.md) gives the complete contract.
The slot-surplus companion is a separate mathematical algorithm and is not
implemented by this profile backend.

```sh
python3 problems/arbitrary-processing-scheduling/verify/check_profiles.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
