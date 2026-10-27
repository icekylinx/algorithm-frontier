# Binary-count recipient-polymatroid backend

[counts.py](counts.py) takes validated complete original-player rank tables.
It computes conceptual-copy ranks, whole-owner availability and actual
integral contracted comparator recovery without constructing any copy IDs.
The [realization proof](../reference-realization.md) gives contracts and costs.

```python
from counts import RankTable, minimal_bundle
from fractions import Fraction

# Two owner blocks with a shared capacity of 10**100.
capacity = 10**100
rank = RankTable(2, (0, capacity, capacity, capacity))
reserved = (capacity // 4, capacity // 4)
assert rank.rank(reserved) == capacity // 2
assert rank.availability(reserved) == (capacity // 2, capacity // 2)
retained = rank.recover_comparator(reserved, (0, capacity))
assert retained == (0, capacity // 2)
assert minimal_bundle((capacity, 5), (Fraction(1, 3), 0), Fraction(7, 3)) == (7, 0)
```

- `RankTable(n, values)` validates all original monotonicity and submodularity
  constraints. Table masks use original player indices.
- `rank(z)` evaluates the natural-matroid rank of a possibly dependent
  reserved set represented by its count vector.
- `contracted(z)` gives ranks of whole original owner blocks after contraction.
- `availability(z)` gives the maximal independent addition at each owner.
- `recover_comparator(z, original)` returns a maximum-total integral contracted
  vector bounded by the supplied original feasible allocation.
- `minimal_bundle(counts, values, threshold)` performs exact bulk deletion,
  preserving the threshold and making every remaining unit essential.

Complete tables and subset enumeration have explicit exponential dependence
on the number of original players. The implementation performs no loop
proportional to a capacity's numerical value. It does not provide a local
availability approximation oracle, full player-layer allocator or fractional
configuration optimizer.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
