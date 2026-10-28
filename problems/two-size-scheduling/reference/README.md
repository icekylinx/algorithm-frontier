# Complete-table corank client

[corank.py](corank.py) implements the hard-target construction in
[Theorem D](../proof.md) and its [integer-quota extension](../../whole-ground-allocation/integer-quotas.md):
Boolean box rank, small-job box rank, duality on the full physical-machine
ground, the exact one-unit gate, guarded omission-batch recursion, zero extension
and binary count augmentation to an original base. The client accepts two
complete integral rank tables and two positive common rational sizes.

The high-target branch loads the canonical
[two-time scheduling backend](../../two-time-scheduling/reference/scheduling.py)
for its joint LP and upper-prefix integer recovery. It does not copy that solver.
Its vertex and integer-count enumeration costs remain charged. The local
hard-target path never calls that numeric count enumerator and does not expand
a binary multiplicity into service copies.

```python
from corank import CorankBackend

solver = CorankBackend(
    small_rank=(0, 2, 2, 2),
    large_rank=(0, 1, 1, 1),
    small_size=1,
    large_size=3,
)
schedule = solver.optimize(d=2)
```

Rank tables use subset bit masks of the physical-machine IDs. Output tuples
contain small then large counts at each machine in order. `target` returns
`None` only on a sound full-target rejection; a returned schedule is a weak
success and may exceed its nominal target. `last_trace` records the most recent
target's branch, full and weak quotas, and the complete reached batch-node
count, including rank-rejected candidate children.

The [realization proof](../reference-realization.md) states the exact interface
and costs. This implements the corank client, not the distinct large-unit-rank
local-search algorithm or the streamed global wrapper.

```sh
python3 problems/two-size-scheduling/verify/check_corank.py
```

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0.
