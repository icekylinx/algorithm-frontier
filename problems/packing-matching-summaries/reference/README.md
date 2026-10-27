# Exact rational packing-summary backend

[`packing_summary.py`](packing_summary.py) implements the product-feature
construction in the [realization proof](../manuscripts/reference-product-realization.md).
It uses only the Python standard library and exact rational arithmetic.

```python
from packing_summary import Item, summarize

items = [Item((i % 3,), i - 5, ((i % 2,),)) for i in range(12)]
answer = summarize(items, cardinality=2, label_failures=(1,))
print(answer.retained)
```

The returned IDs are positions in the original item list. Costs may be signed
integers or `fractions.Fraction` values; cost ties use those permanent positions.
Supports and label lists contain distinct nonnegative integer IDs. Empty
supports, empty label lists and parallel items are permitted. Each item supplies
one label list per entry of `label_failures`. `universe_failures` bounds failed
support IDs. Budgets are nonnegative integers, including binary huge integers;
only explicitly occurring IDs can affect the instance.

Pass `resource_columns` to require independence in an original rationally
represented resource matroid. Every original item has one equal-length column.
The backend computes its full original rank and performs a lossless row
compression. It never truncates the resource to the requested cardinality or
to a future background. Zero columns are loops; rank zero has no positive
feasible choice. Without resource columns there is no additional matroid.

For graph matching, make each nonloop edge an item whose support is its two
endpoints. Parallel edge records retain different positions. To support
individual edge failures, add a label system in which each item has its own
position as a singleton label, and pass that system's failure budget.

The result fields distinguish the identity branch from constructed features:

- `retained`: original item positions, in accepted cost order on the algebraic
  branch and input order on the identity branch.
- `dimension_bound`: product dimension saturated at the original item count,
  after clipping budgets to their effective explicit universes.
- `gated`: whether the original ground was returned before feature generation.
- `feature_rank`: actual lifted rank, or `None` on the identity branch.
- `resource_rank`: full original rational resource rank, or `None` without a
  resource constraint.

The public API constructs the restriction. It does not enumerate failure
queries or optimize a query's arbitrary later matroid extension. Rational
operations have their exact bit costs; the support count is not a workspace
bound. Finite-field extensions are covered by the mathematical construction
but are not implemented by this backend.

```sh
python3 problems/packing-matching-summaries/verify/check_product_summary.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
