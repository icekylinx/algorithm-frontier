# Recipient-polymatroid count and fractional references

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
configuration optimizer by itself. The separate fractional backend below
supplies coordinate-box pricing and fractional generation.

## Coordinate-box fractional optimizer

[fractional.py](fractional.py) accepts complete original player and resource
rank tables, nonnegative exact profits and original owner-major coordinate
quotas. `values` may be one common value per type or an owner-major matrix;
the matrix extension concerns fractional optimization only. Arbitrary local
matroid, knapsack or downward-closed oracles are not accepted.

```python
from fractional import Residual
from fractions import Fraction

relaxation = Residual((0, 1, 1, 1), ((0, 2, 2, 2),), (1,), support=1)
point = relaxation.optimize(Fraction(1, 3))
assert relaxation.verify(point)
```

- `price(caps,profits,linear,hinges,budget,epsilon)` implements signed
  convex-cost pricing by nonpositive-prefix shifting, binary segment chunks
  and profit-scaled dynamic programming. Its scalar cost budget is exact.
- `strict_price` uses the exact rational cost grid, including negative
  thresholds, and returns a genuine weak-target violation or sound absence
  of a hard-target violation.
- `Residual(...,support=s)` retains exactly subsets of at most that size;
  the default retains all subsets. `cut_sets` instead supplies explicit
  distinct resource/subset IDs. All aggregate original rank rows remain.
- `aggregate_vertex` computes signed greedy support on the original
  player-base/resource product. `reserved_basis` represents a dependent
  reservation by a feasible spanning count vector without copy IDs.
- `weak_target(T,epsilon)` performs actual configuration/aggregate-vertex
  generation, using the canonical exact normalized Bland LP. `None` means
  original hard-target infeasibility. A `Point` is feasible for its declared
  weaker target; an accuracy above one half uses one half internally.
- `optimize(epsilon)` performs original-value-grid weak optimization.
  `verify` checks all original fractional rows and local configurations with
  every producer disabled. The output has fractional configuration masses,
  with no claimed common integer selected basis.

The [fractional realization proof](../fractional-realization.md) proves
pricing, strictness and direct LP-dual primal extraction, and records the
complete mathematical dependency audit. The native outer generation may
store exponentially many columns and vertices, with separately charged
finite Bland pivot and exact rational costs. It does not implement the
mathematical polynomial-cut ellipsoid algorithm or its workspace bound.
Binary unit counts remain numerical throughout.

Run both independent checkers from the repository root:

```sh
python3 -B problems/recipient-polymatroid/verify/check_counts.py
python3 -B problems/recipient-polymatroid/verify/check_fractional.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
