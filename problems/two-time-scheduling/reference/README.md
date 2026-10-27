# Exact complete-table baseline

[scheduling.py](scheduling.py) implements the original-total LP, heterogeneous role
queries, normalized support separation, joint integer recovery and one-sided target
search from [Theorem HT](../proof.md). It accepts any finite physical-machine set
through complete integral recipient-rank tables. Times, costs and the budget must
be Python integers or `Fraction` values; `None` marks a forbidden pair.

This is an executable explicit-table baseline. It enumerates LP active sets,
all role subsets and bounded integer count vectors. Those costs differ from the
polynomial oracle primitives and fast omission/global-cover algorithm in Theorem HT.
The [realization proof](../reference-realization.md) states the contract and charges
these enumerations. It does not infer a new running-time bound for Theorem HT.

```python
from scheduling import Backend, Instance

instance = Instance(
    ranks=((0, 2, 2, 2), (0, 1, 1, 1)),
    times=((1, 5), (2, 6)),
    costs=((0, 1), (1, 0)),
    budget=2,
)
schedule = Backend(instance).optimize(d=2)
```

The output is a tuple in machine-major, then type order. Every type retains its
original full rank, including after eligibility and target masks. `None` returned
by `optimize` certifies infeasibility of the original totals or budget. `target`
may return a weak success above its nominal load target. `separator` separately
rejects an empty underlying joint region with `ValueError`; otherwise it returns
a normalized nonnegative separating row or `None` for service membership.

Run the independent finite checker from the repository root:

```sh
python3 problems/two-time-scheduling/verify/check_scheduling.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
