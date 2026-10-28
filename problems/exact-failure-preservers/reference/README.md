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

**Attribution:** icekylinx and GPT-6 Astra Pro.


## Ordinary rank drops and certified valuated baselines

`matroid_reporting.build_maximum(costs,independent1,independent2)` initializes
maximum common cardinality and its exact minimum signed cost. It retains the
fixed-rank reporter at that cardinality and, when positive, one at the next
smaller cardinality. Its `query(failed)`, `optimum_cost(failed)` and
`rank_after(failed)` report the actual minimum-cost maximum-cardinality result.
A single deletion lowers ordinary common rank by at most one. Rank zero has
the empty optimum. The original cost table and callbacks are not retained.

```python
from fractions import Fraction
from valuated_reporting import build, certify, verify_optimality

first = {frozenset((0,1)): Fraction(0),
         frozenset((0,2)): Fraction(3),
         frozenset((1,2)): Fraction(1)}
second = {basis: Fraction(0) for basis in first}
certificate = certify(3,2,first.get,second.get,(0,1))
assert verify_optimality(3,2,first.get,second.get,certificate)
reporter = build(3,2,first.get,second.get,(0,1))
assert set(reporter.query(0)) == {1,2}
assert reporter.optimum_cost(0) == 1
```

`valuated_reporting.build(N,rank,value1,value2,baseline)` accepts two valid
fixed-rank minimization-convention valuated matroids. Value callbacks take
frozensets of original IDs, return exact `int`/`Fraction` on effective-domain
bases, and return `None` outside their domains. The supplied common baseline
is independently certified optimal through split prices. Nonoptimal or
non-common baselines raise `ValueError`; this is not original infeasibility.
No native valuated baseline search is implemented.

`certify` separately returns `BaselineCertificate(baseline,value,prices)` on
the original ground. `verify_optimality` checks the original baseline and all
finite single exchanges against its two opposite price inequalities, without
any optimizer, graph or producer. Validity of the valuated-matroid axioms is
an input-oracle promise; original tiny tables in the checker validate them
independently. The certificate is sufficient because priced local optimality
is global for each valuation and the prices cancel on common bases.

The compact valued reporter has the same query and stored-value methods as
the supplied-baseline ordinary reporter. Queries call no valuation or
independence oracle. Price certificates, original callbacks and exchange
tables are discarded during `build`; separately retaining certificate evidence
requires original-ground storage and is outside the compact bound. Rank zero
retains the two valuation constants on the empty basis. No objective on a
smaller-rank set is inferred from a fixed-rank valuation.

The [complete realization proof](../manuscripts/reference-valuated-and-rank-drop.md)
proves the price construction, signed exchange reporting, ordinary rank-drop
wrapper and costs. Valued baseline certification/compression uses `O(Nk)`
value evaluations and `O(Nk^2+k^3)` additional arithmetic work, with actual
rational/original-ID bit lengths charged. Ordinary maximum-cardinality
initialization retains the earlier conservative polynomial preprocessing.
The named polynomial valuated initializer is a mathematical dependency,
not native software in this interface. Lower-bound transfers and multiple
failures remain outside this incremental review.
