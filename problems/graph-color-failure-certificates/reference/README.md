# Exact vertex-color certificate backend

[`vertex_colors.py`](vertex_colors.py) implements the rational activation
matrix for the sharp componentwise vertex-color theorem. It uses only the
Python standard library.

```python
from vertex_colors import Edge, build

certificate = build(
    colors=[0, 1, 1, 2],
    edges=[Edge(0, 1, -2), Edge(0, 2, 0), Edge(1, 2, 1),
           Edge(1, 3, 2), Edge(2, 3, 2)],
    failures=1,
)
print(certificate.records)
print(certificate.forest(failed_colors=[0]))
```

Colors are nonnegative integer IDs, one per vertex. Vertices are numbered
from zero. An edge's original ID is its position in the input list; ties in
signed integer or `fractions.Fraction` weights use that ID. Parallel edges
remain distinct. Loops are validated and then ignored because they never
belong to a forest. Isolated vertices remain in the stored color list.

`build` computes original connected components and the exact componentwise
activation basis. `records` contains retained `(original ID, Edge)` pairs
in the fixed weight order. `support_bound` is the sharp componentwise bound
from the theorem. The object stores these records, the original vertex
colors and the failure allowance. It does not keep discarded edge records.

`forest` rejects repeated failure IDs and failure sets exceeding the allowed
budget. Unknown nonnegative color IDs have no effect but count toward that
budget. A query filters the retained records and runs deterministic Kruskal;
it returns the exact original canonical minimum-spanning-forest IDs in
weight order. The construction also preserves every surviving ordered-prefix
connectivity partition, as proved in the
[realization note](../manuscripts/reference-vertex-color-realization.md).

This backend covers one color per vertex and arbitrary failure allowance.
It does not implement mixed edge colors, overlapping color lists, finite-field
arithmetic or the faster dynamic-MSF interface. Those theorem variants retain
their separate mathematical proofs. Query time includes the scan of retained
records, vertex initialization and output, with exact input-bit costs.

```sh
python3 problems/graph-color-failure-certificates/verify/check_vertex_colors.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
