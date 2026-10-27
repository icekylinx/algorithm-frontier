# Ordered recipient-matroid reservations

[reservations.py](reservations.py) implements the resource-side state transitions
in Sections 2–5 of the [proof](../proof.md). It is a reusable exact backend,
not a complete player-basis allocator or an implementation of the configuration
LP. Its [realization proof](../resource-backend.md) gives the contract and costs.

```python
from reservations import Bundle, Reservations

# Uniform rank two on four recipients, for one resource.
def rank(owners):
    return min(2, len(owners))

state = Reservations(4, [rank], [Bundle(0, frozenset({0}))])
candidate = Bundle(1, frozenset({0}))
assert state.complete(candidate) == frozenset()  # Fresh strongly free center.
state.exchange(candidate, outgoing=None, keep=0)
assert len(state.matching) == 2
```

Original matching records receive permanent integer IDs. A replacement gets a
fresh ID and inherits no blocker designation. Public snapshots consist of
immutable tuples and frozen records. Ordinary invalid operations raise
`ValueError` before changing the state. Supplied rank functions must obey the
matroid axioms; checking all those axioms is not part of the backend.

- `available(owner)` performs the current closure test for each resource.
- `complete(bundle)` appends a dependency-filtered blocked center, or returns an
  empty set without storing a fresh strongly free candidate.
- `releasable(index)` tests the center against its current earlier prefix and
  current designated group. A nonempty group can pass.
- `exchange(incoming, outgoing, keep)` verifies strong resource freedom,
  replaces the named matching record and retains the requested ordered prefix.
  Augmentation uses `outgoing=None` and `keep=0`.

The caller certifies player-matroid independence, earliest-layer exchange,
local bundle feasibility, minimality and value thresholds. It normalizes all
stored centers before completing a growth test. The backend deliberately
contains neither a player-layer search nor a numerical approximation claim.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
