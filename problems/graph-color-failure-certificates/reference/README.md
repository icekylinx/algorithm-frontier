# Exact graph-color certificate references

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

`vertex_colors.py` covers one color per vertex and arbitrary failure
allowance. Its query time includes the scan of retained records, vertex
initialization and output, with exact input-bit costs. The additional
mixed/list reference below supplies the broader activation interfaces.

## Mixed colors and overlapping lists

[`list_colors.py`](list_colors.py) accepts `Edge(u,v,weight,colors=())`
records and a distinct nonnegative color-ID list at every vertex. Original
IDs are input positions; weights remain signed exact integers/Fractions.
All vertex and edge color failures share one supplied budget.

```python
from list_colors import Edge, build, single_failure

vertex_lists = ((0,), (1,), (0, 2), ())
edges = (Edge(0, 1, -2, (2,)), Edge(1, 2, 0, (0,)),
         Edge(2, 3, 1), Edge(0, 3, 2, (1,)))
certificate = build(vertex_lists, edges, failures=1)
forest_ids = certificate.forest((2,))
differences = single_failure(vertex_lists, edges)
assert differences.forest(2) == forest_ids
```

`build` computes actual coefficient-evaluation spans using the canonical
module generator. No formal binomial monomial universe or failure family
is enumerated. Vertex lists use their computed componentwise actual feature rank and
symmetric-matrix saving. Mixed lists retain one shared activation column
per original edge; singleton vertex/edge colors also use the cubic saving.
The [realization proof](../manuscripts/reference-mixed-list-realization.md)
gives both-direction rowspace equivalence and exact prefix correctness.
`Component.feature_rank` counts vertex evaluations in vertex mode and
endpoint/edge evaluations in mixed modes; cubic vertex-rank savings use
their separate Vandermonde rank.

The default field is rational. An optional `modulus` is a caller-supplied
prime, with enough distinct nonzero points for each component's labels
and dummy zero. Composite-modulus validation and field extension are not
implemented. Query weights and sorting remain original rational data.

`Certificate.records` stores only retained original edges and their fixed
order. `forest(failed_colors,threshold=None)` optionally takes an exact
`(weight,original_ID)` prefix key and returns canonical IDs. Unknown colors
have no effect but spend failure allowance; repeated and excessive failure
sets are rejected. This forest report is not a standalone optimality proof
for an absent original graph. The independent checker retains the original
graph when verifying it.

## One-failure differences and the dynamic interface

`single_failure` builds the exact union of the baseline and individual-color
canonical forests. It collects nonbaseline forest edges through actual
reported insertions/deletions, using a dense original-ID linked list, and
enumerates only completed color-deletion batches. Intermediate forests are
never added. Every color has a `Difference(removed,added,value)` record;
unchanged colors have the baseline value and empty differences.

`indexed(i)` retrieves a record at a compact palette index. Raw original
color lookup `color(c)` additionally uses binary search. `forest(c)` scans
the stored retained union to write the canonical forest; its cost is
separate from compact indexed lookup. Neither query calls the feature or
dynamic producer. Sorting original/retained records and every extra list
is charged explicitly.

The default `ReferenceMSF` recomputes exact Kruskal by scanning the fixed
original record order after each individual update. Its finite polynomial
scan cost and hash/set work are separate from the published HDT update
bound. A paid backend can supply the same original-ID exchange interface;
the proof identifies its realization in HDT Theorem 8 and Section 5.1.
No fast dynamic-MSF code is shipped here.

```sh
python3 problems/graph-color-failure-certificates/verify/check_vertex_colors.py
python3 -B problems/graph-color-failure-certificates/verify/check_list_colors.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
