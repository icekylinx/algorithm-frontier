# Supplied-baseline arborescence reporting

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
negative auxiliary exchange cycle is defensively rejected. The reference
does not supply the initial optimum or an initialization bound. The
manuscript's ordinary minimum-cost-arborescence algorithm supplies that
separate step. Exhaustive enumeration in the finite checker only constructs
small independent baseline fixtures.

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
arborescence construction. It does not implement arbitrary oracle matroids,
valuated matroids, or multiple simultaneous failures.

The [realization argument](../manuscripts/reference-arborescence-reporting.md)
matches the source to the proved interfaces. Run its independent checker:

```sh
python3 problems/exact-failure-preservers/verify/check_arborescence_reporting.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
