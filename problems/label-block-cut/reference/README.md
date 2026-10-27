# Exact rational whole-block label compiler

[`whole_blocks.py`](whole_blocks.py) implements the deterministic rational
incidence-label lift, original-row compression and common-scalar decoder.
It imports exact elimination primitives from the canonical
[feature module](../../persistence-failure-certificates/reference/feature_summary.py).
It does not implement quotient sampling or adaptive resparsification.

```python
from fractions import Fraction
from whole_blocks import compile_blocks

# Each item is a tuple of columns. Item IDs are original list positions.
blocks = [((1, 0), (0, 1))] * 10
compiled = compile_blocks(
    blocks, row_labels=({0}, {1}), item_labels=({0, 1},) * 10,
    failures=1, weights=(Fraction(1, 2),) * 10,
)
assert compiled.mode == "LIFT"
assert compiled.selected_rows == (0, 1)
assert compiled.value() == 5
assert compiled.value(failed=(0,)) == 0
assert compiled.scalars((0,)) == (0,) * 10
assert compiled.rank_on((0, 1)) == compiled.rank_on((0,))
```

`compile_blocks` accepts explicit columns of a common rational ambient
dimension, one label set per original row, one label set per entire item,
a nonnegative integer failure budget, and optional nonnegative rational
weights. Labels are original nonnegative integer IDs, including zero.
The compiler assigns distinct positive integer field points to used labels
and reserves point zero for its internal dummy. Original label IDs and
item IDs are preserved. Integers and `fractions.Fraction` are accepted;
floating point inputs are rejected. Empty blocks and zero columns are legal.

Every nonzero matrix entry must have its row's labels contained in its
item's labels. `deficit`, when supplied, bounds the missing-label count
on all such entries. After checking that bound, the compiler uses the
maximum actual deficit. It caps the effective failure degree at the number
of used labels. It selects independent **original rows** and keeps their
own label sets; `compression` reconstructs every original row from them.

The result has one of three modes:

- `LIFT` materializes ordinary homogeneous monomial coefficients for every
  column of every item. The ambient lift dimension is strictly smaller
  than the original item count. `decoder(failed)` constructs the exact
  original-dimensional linear map; `decode(failed)` applies it to every
  lifted column. `scalars(failed)` supplies the common scalar for each item.
- `FULL_INPUT` returns the original input when positive-rank lift dimension
  is at least the item count. It makes this decision before monomial
  enumeration or polynomial multiplication. It materializes no lift and
  rejects `decoder`, `decode`, and `rank_on` calls.
- `ZERO` represents total original rank zero. It has zero lift dimension,
  zero-length lifted columns and original-dimensional zero decoder images.

`value(subspace, failed, weights)` charges an item once when at least one
surviving original column lies outside the supplied rational subspace.
The subspace is given by column vectors. In `LIFT`/`ZERO` modes this is
computed from decoded columns; in `FULL_INPUT` mode it uses the exact
original input. Optional reweights remain indexed by original item ID and
are shared across all columns. This method certifies no approximation
property of arbitrary caller-supplied reweights. Unknown failed label IDs
have no effect but count toward the failure budget; duplicate failures
and over-budget queries are rejected.

`rank_on(item_ids)` is an exact integer rank oracle for the union of the
complete lifted blocks of the named original items. It supplies the
represented-polymatroid interface required by the published quotient
backend. It does not select or reweight items itself. A materialized
`Compilation` keeps all original blocks and all their lifted columns;
the compiler is not a sparse summary. `FULL_INPUT` is an exact fallback,
without a claim to have sampled the input.

If `r` is original rank, `L` is the used-label count, `h` is the effective
failure degree, and `k` is actual incidence deficit, the program computes
`K=binom(h+k,k)` and tests `r*K>=m` before constructing any of its `K`
monomial coordinates. Here `h,k<=L`; the bit length of that binomial
integer is polynomial in the explicit input even when its numerical value
is enormous. In `LIFT` mode the dimension is below `m`, so all materialized
matrices and the elimination, coefficient construction, rank queries and
decoder computations are polynomial in the explicit rational input and
queried subspace bit length. Exact rational bit costs are charged. There
is no finite-field or quantum implementation in this module.

See the [realization and composition audit](../manuscripts/reference-whole-block-decoder.md).
Run the independent checker from the repository root:

```sh
python3 problems/label-block-cut/verify/check_whole_blocks.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
