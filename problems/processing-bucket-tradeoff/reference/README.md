# Exact bucket-label client

[buckets.py](buckets.py) implements the bucket thresholds, original-pair masks,
fixed-label plans and one-sided optimization of [Theorem AB](../proof.md).
It accepts the validated arbitrary-time `Instance` exported by this module.
The depth is a nonnegative integer, charged numerically as in the theorem.

```python
from fractions import Fraction
from buckets import BucketBackend, Instance

instance = Instance(
    ranks=((0, 1, 1, 1), (0, 1, 1, 1)),
    times=((Fraction(1, 4), 1), (Fraction(2, 3), 0)),
    costs=((0, 1), (1, 2)), budget=2,
)
schedule = BucketBackend(instance, depth=1).optimize()
```

Output tuples are in machine/type order. `target(T)` returns a legal schedule
within the depth's factor or soundly rejects the original full target with
`None`. `plan(T, labels)` exposes the exact disjoint groups for a fixed label
vector. Zero targets and original-budget infeasibility are tested exactly.

This is a thin client of the canonical
[general-processing joint solver](../../arbitrary-processing-scheduling/reference/profiles.py).
It imports that implementation's exact original-resource LP, cost-preserving
prefix/partition recovery and grid search, which in turn reuse the two-time
backend's rational LP and integer-count primitives. There is one implementation
of those common operations. Their explicit enumeration costs and vertex storage
remain charged; this reference does not attain the theorem's polynomial per-label
oracle time or overall polynomial workspace.

The [realization proof](../reference-realization.md) records the connection.

```sh
python3 problems/processing-bucket-tradeoff/verify/check_buckets.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
