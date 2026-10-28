# Exact feature-rank reference constructions

[`feature_summary.py`](feature_summary.py) is a dependency-free Python
implementation of the
[evaluation-module and contraction proofs](../manuscripts/feature-rank-construction.md).
It uses exact `fractions.Fraction` values over the rationals, or integers
modulo a caller-supplied prime. All choices are deterministic.

## Represented matroids

```python
from feature_summary import represented_summary

answer = represented_summary(
    columns=[[1, 0], [1, 0], [0, 1], [0, 1], [1, 1]],
    labels=[{0}, {1}, {0}, {2}, set()],
    failures=1,
    order=[4, 0, 1, 2, 3],
)
print(answer["retained"])
```

The output IDs index the original `columns` list. `order` supplies the
single prefix order; a cost application sorts costs with a fixed ID tie
break first. `rank` is the actual rank of the formal tensor lift,
`formal_rows` is its ambient row count, and `candidates` counts the rows
processed by the module frontier. The algorithm never enumerates all
`formal_rows` rows when the accepted frontier is smaller.

## Simplicial persistence

```python
from feature_summary import persistence_summary

answer = persistence_summary(
    vertices=4,
    top_simplices=[(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
    labels=[{0}, {0, 1}, {1}, set()],
    failures=1,
    modulus=7,
)
print(answer["retained"], answer["feature_rank"])
```

Top simplices are distinct sorted vertex tuples of one dimension at least
one. Vertices use IDs from zero through `vertices - 1`. The complete
original lower skeleton is implicitly retained. This implementation covers
vertex labels with arbitrary overlaps and no additional top-simplex labels.
The `retained` IDs refer to the original top-simplex list. `feature_rows`,
`shifted_rows` and `selected_original_rows` expose the exact intermediate
data used by the independent checker.

The boundary row selection generates one oriented simplex column at a time
and stores at most one column plus a rank-sized echelon basis. The final
contraction pass likewise stores only its current column and retained
basis. Neither stage materializes a dense matrix across all top simplices.
The adapter builds a facet index from the top-simplex tuples; this
combinatorial index, the vertex labels and the supplied simplex list are
separate from the field-element workspace in the theorem.

With `modulus=None`, all arithmetic is rational. With a prime modulus, the
represented-matroid routine needs more field elements than input labels;
the persistence routine also needs more than the vertex count. The code
rejects fields too small for these explicit point/shift choices. General
finite-field extensions are proved in the manuscript and are not
implemented by this reference. The modulus is assumed prime.

## Verification scope

```sh
python3 problems/persistence-failure-certificates/verify/check_feature_construction.py
```

The checker compares small product frontiers against independently
enumerated monomial matrices, then checks every allowed small failure and
every ordered prefix against original column spans. Its larger structured
fixtures use several million formal feature rows but actual ranks three
and four. Exact arithmetic and finite examples check implementation
identities; the full parameter-dependent theorem and naturality of the
homology identifications are established by the manuscript proof.

## General incidence matrices and additional top labels

The separate [`incidence.py`](incidence.py) backend implements the
[general-incidence realization](../incidence-realization.md). Its input matrix
rows retain their original label sets; arbitrary row combinations are never
assigned old labels. Every nonzero incidence must have its row labels contained
in its column labels. It computes the actual lifted rank through independent
row products and avoids expanding the formal monomial universe.

```python
from incidence import incidence_summary, labeled_persistence_summary

summary = incidence_summary(
    rows=[[1, 1, 1]], row_labels=[{10}],
    column_labels=[{10, 20}, {10, 30}, {10, 40}], failures=1,
)
assert len(summary['retained']) == 2

summary = labeled_persistence_summary(
    vertices=4,
    top_simplices=[(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
    vertex_labels=[set(), {0}, {1}, set()],
    top_labels=[{2}, set(), {3}, set()], failures=1,
)
```

Both functions accept `modulus=None` for rationals, or a caller-supplied prime,
and one original-column permutation as `order`. Output `retained` contains
original IDs; `selected_original_rows` records the uncombined row projection.
`increment` is the maximum label difference on a nonzero incidence,
`original_rank` is the original matrix rank, and `rank` is the actual lifted
rank. `formal_rows` is an exact dimension counter, not an allocated row list.
Integer label IDs may be shared arbitrarily. Failure budgets remain binary.
A supplied finite field must have enough distinct nonzero label points; no
extension-field constructor is included.

The simplicial adapter retains the entire lower skeleton implicitly and
constructs a dense original boundary matrix. This is a separately charged
polynomial reference; the vertex-only adapter above retains its streaming
construction and sharper feature-rank contract. Neither adapter computes
worst-case failures, preserves top-degree homology or combines unrelated
filtration and cost orders in one bound.

```sh
python3 -B problems/persistence-failure-certificates/verify/check_incidence.py
```

**Attribution:** icekylinx and GPT-6 Astra Pro.
