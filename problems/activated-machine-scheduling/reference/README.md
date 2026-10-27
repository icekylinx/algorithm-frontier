# Exact activated-basis reference adapter

[activation.py](activation.py) implements the actual fixed-basis activation
adapter with one shared setup and assignment budget. Its positive-target
clients are the canonical occupied profiles, canonical bucket labels, and the
local reusable `SixBackend` implementing the six-profile theorem directly.

```python
from activation import ActivatedBackend, Instance

jobs = Instance(
    ranks=((0, 1, 1, 1),),
    times=((1,), (0,)),
    costs=((5,), (0,)),
    budget=4,
)
solver = ActivatedBackend(
    jobs, activation_rank=(0, 1, 1, 1), setup=(0, 4), method="six",
)
result = solver.optimize()
assert result.basis == (1,)
assert result.counts == (0, 1)
```

The job `Instance` is the canonical general-processing complete-table input:
one original recipient-rank table per type, machine/type rational times and
costs, `None` for forbidden pairs, and the original combined budget. The
activation table must be an ordinary matroid rank on the same positive number
of physical machines. Setup fees are exact nonnegative integers or `Fraction`
values. Floating point data are rejected. Rank zero and empty job classes
are supported; an empty job system still requires an affordable genuine basis.

`method="profiles"` takes rational `epsilon` in the scheme's domain;
`method="buckets"` takes nonnegative integer `depth`; `method="six"` gives
the exact three-halves profile factor. `feasible()` tests unbounded load
exactly, `target(0)` tests zero load exactly, and positive `target(T)` returns
a legal weak output or a sound full-target rejection. `optimize()` performs
one-sided search on the original rational load grid. Results retain both the
actual activated original-machine basis and original machine/type counts,
including zeros at inactive machines.

The exact feasibility gate streams actual bases, checks original job totals
under activation and eligibility, and uses binary rank increments in increasing
assignment-cost order. It charges the setup and assignment cost together.
After retained-rank checks, positive targets compress to exactly the active
machines before calling the profile solver. They do not generate duplicate
profiles at inactive positions. Counts are zero-extended on return.

`restricted` and `minimum_assignment` are internal helpers, rather than raw
original-instance scheduling entry points. The former requires a genuine
original activation basis; the latter requires valid tables already masked
with retained original totals, with every forbidden coordinate a rank loop.
Both helpers reject violations of these specific preconditions.

`SixBackend(jobs)` also provides a direct client of the original six-profile
scheduling model, without activation or setup. Its `plan(T, labels)` exposes
the exact big/small masks and caps for independent checking.

The [realization proof](../reference-realization.md) proves these contracts and
charges complete rank tables, inherited LP-vertex enumeration, numeric integer
recovery and vertex storage separately. Those reference costs do not realize
the fast theorems' polynomial per-profile primitives or total polynomial space.
No original job identities or unary job copies are constructed.

```sh
python3 problems/activated-machine-scheduling/verify/check_activation.py
python3 problems/activated-machine-scheduling/verify/check_six_profiles.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
