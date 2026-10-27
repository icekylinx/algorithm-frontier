# Ordinary matroid and arborescence reporting

[`matroid_reporting.py`](matroid_reporting.py) supplies an initialized
fixed-rank exact reporting oracle for **two arbitrary ordinary matroid
independence callbacks**, with signed rational costs. It also supplies
automatic initialization for the rooted directed arborescence backend.
No optimum baseline needs to be supplied to these entry points.

```python
from fractions import Fraction
from matroid_reporting import build, build_arborescence
from arborescence_reporting import Arc

# Ordinary uniform matroids on original ground IDs 0,1,2.
independent = lambda chosen: len(chosen) <= 2
oracle = build((Fraction(-3), -2, 1), 2, independent, independent)
assert oracle.query() == (0, 1)
assert set(oracle.query(0)) == {1, 2}

graph_oracle = build_arborescence(
    3, 0, (Arc(0, 1, 0), Arc(1, 2, 0), Arc(0, 2, 1), Arc(2, 1, 1)),
)
assert set(graph_oracle.query(0)) == {2, 3}
```

`build(costs, rank, independent1, independent2)` uses original ground IDs
from zero through the cost-list length minus one. Costs are fixed signed
integers/Fractions. The rank is a nonnegative binary integer. Each callback
must be a valid ordinary matroid independence oracle on `frozenset`
arguments of original IDs. The mathematical validity of these callbacks
is a paid model assumption, not a property tested for arbitrary Python
functions. Rank zero has the empty optimum. If no initial common set of
the requested size exists, the constructor returns `None`; deletion can
never restore that size.

The initializer imports the canonical
[weighted intersection primitive](../../robust-bounded-certificates/reference/bounded.py).
It computes and verifies the exact optimum using exchange
potentials and, for an underfull answer, a maximum-cardinality rank cut.
It then discards those ground-sized initialization records. The compressed
graph keeps the cheapest original outside label for each ordered pair of
baseline elements, breaking ties by original ID. Its split graph has exactly
twice the requested rank many nodes. It uses the same exact lexicographic
Floyd–Warshall and phased hub reporter as the graph implementation below.

`build_arborescence(n, root, arcs)` validates the original nonnegative-cost
graph, initializes its optimum through graphic and incoming-partition
matroid oracles, and passes that baseline to the sparse HLD backend.
`None` means there is no initial rooted spanning arborescence. Original
parallel arc IDs remain distinct; loops and arcs entering the root are
loops of both initializer matroids. The graph entry point retains its
nonnegative cost model; the generic two-matroid entry point permits signed
costs. A one-vertex graph returns the empty oracle.

The generic initializer uses a conservative polynomial contract of
`O(N^5)` record/rational operations and `O(N^3)` independence calls on a
ground of size `N`, charging the callbacks' own work and rational bit costs.
After initialization, compression adds `O(Nk)` independence calls and
`O(Nk^2+k^3)` elementary/arithmetic work for requested rank `k`.
Temporary initialization and graph tables are polynomial, with quadratic
record storage in ground size for this implementation. The initialized
graph wrapper likewise has polynomial preprocessing; it does not attain
the manuscript's faster arborescence bound.

Both entry points return the canonical `Oracle` described below. It keeps
neither the original independence callbacks, the original cost list, an
initializer potential/cut vector, nor a full list of per-failure solutions.
Its final program contract is `O(k^(3/2))` original element IDs/records and
`O(k)` query/output work for `k>=1`; rank zero has constant reporting cost.
Record bounds charge original-ID and rational encoding lengths separately.
The [ordinary realization proof](../manuscripts/reference-ordinary-matroid-reporting.md)
identifies the initialization and literal-update dependencies. This is an
ordinary fixed-rank implementation; valuations, rank-drop objectives and
multiple simultaneous failures are outside its API.

```sh
python3 problems/exact-failure-preservers/verify/check_matroid_reporting.py
```

## Supplied-baseline arborescence entry point

[`arborescence_reporting.py`](arborescence_reporting.py) realizes the sparse
heavy-light exchange graph and phased deterministic reporting construction in
the [ordinary companion, Sections 4–6](../manuscripts/exact-single-failure-arborescences-and-matroid-intersection.md).
It uses the Python standard library and exact integer/Fraction costs.

```python
from fractions import Fraction
from arborescence_reporting import Arc, build

arcs = [Arc(0, 1, 0), Arc(1, 2, 0),
        Arc(0, 2, Fraction(2, 3)), Arc(2, 1, Fraction(1, 3))]
oracle = build(n=3, root=0, arcs=arcs, baseline=(0, 1))
assert oracle.query() == (0, 1)
assert oracle.query(failed=0) == (2, 3)
assert oracle.optimum_cost(failed=0) == 1
```

Vertices are zero-based integers; the root is arbitrary. An original arc ID
is its position in `arcs`. Parallel arcs remain distinct. All endpoints and
costs are validated; loops and arcs entering the root are then ignored.
Costs must be nonnegative integers or `fractions.Fraction` values. Floating
point inputs are rejected. The one-vertex graph has the empty baseline and
empty answer after every failure.

The caller supplies a **minimum-cost rooted spanning arborescence** under
the fixed original costs. `build` validates its identifiers, indegrees and
root reachability. Baseline optimality is an explicit input promise; a
negative auxiliary exchange cycle is defensively rejected. This lower-level
entry point retains that supply contract. The initialized wrapper above
discharges it using the canonical weighted-intersection primitive; exhaustive
tree enumeration remains only an independent small fixture comparator,
not the implemented initialization algorithm.

`query(failed)` returns optimum original arc IDs, or `None` if no surviving
spanning arborescence exists. Omitting `failed` requests the baseline. An ID
outside the baseline, including an unknown ID, returns the baseline.
`optimum_cost` reads a precomputed exact value or the infeasibility flag.
Queries traverse stored parent pointers or explicit paths, read the baseline,
and toggle original IDs. They make no optimization or graph-oracle calls.

The final `Oracle` keeps baseline IDs, retained `support` IDs, demand
descriptors, exact objective values, short paths, and the selected hubs'
in/out shortest-path trees. It keeps neither the original graph nor an
all-pairs distance matrix. `record_count` counts constant-size record copies,
including copies in different trees, rather than Python object bytes.
Rational bit lengths are charged separately.

Let `k=n-1`. The actual auxiliary dimensions are `A=4k-1` vertices when
`k>0` and `M=O(n+m log^2 n)` arcs. The reference uses exact lexicographic
Floyd–Warshall and a simple phased greedy scan. Its program contract is
`O(M+A^3)` arithmetic preprocessing after baseline supply, with
`O(M+A^2)` temporary records. The final record/support contract is
`O(n^(3/2))`; explicit reporting takes `O(n)` record operations, including
all output IDs. The empty one-vertex case takes `O(m+1)` validation and
constant reporting space/time. Rational additions and comparisons incur
their actual bit costs. This realizes the mathematical reporting interface
with a slower preprocessing implementation than the manuscript's optimized
arborescence construction. The generic ordinary-matroid entry point above
has its own initialization and compressed graph; neither implements valuated
matroids or multiple simultaneous failures.

The [realization argument](../manuscripts/reference-arborescence-reporting.md)
matches the source to the proved interfaces. Run its independent checker:

```sh
python3 problems/exact-failure-preservers/verify/check_arborescence_reporting.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
