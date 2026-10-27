# A self-contained compact unit-flow reporting realization

This note proves the contract of [the exact-rational reference](../reference/unit_flow.py).
It supplies an executable realization of the residual-demand and compact
reporting interfaces in [the flow manuscript](exact-min-cost-flow-and-vertex-disjoint-paths.md),
Sections 3–5. The phased hub construction is the same elementary construction
proved in [the shared distance-preserver companion](../../exact-failure-preservers/manuscripts/exact-single-failure-arborescences-and-matroid-intersection.md#deterministic-construction-of-the-distance-preserver).
Its classical attribution is retained there. The proof below establishes
the reference's correctness directly; it needs no distance-preserver library.

## The public contract

Input consists of a finite loopless directed multigraph with explicit unit
arc records, nonnegative rational costs, two distinct supplied terminals,
and, for the fixed-value constructor, a nonnegative integer target value.
The input sequence gives each record its distinct integer ID. A query is an
independent deletion of one ID, or the no-failure query. Parallel and opposite
records remain distinct throughout. All arithmetic is exact.

**Theorem (reference realization).** The two public builders terminate and
return exact optimal flows or exact infeasibility under that contract.
`fixed_flow` returns an oracle at the requested value if originally feasible.
`MaximumFlowOracle` returns minimum-cost maximum-flow answers. Every feasible
query output uses only retained original records and avoids the failed ID.
The retained-record and reporting-record bound is precisely the
support-sensitive bound (F6) of the flow manuscript, with one baseline for
fixed value and at most two baselines for maximum flow. The original input
graph is not consulted or retained for queries. On simple input, the
acyclic-support proof gives the same uniform retained-size specialization
(F1); this implementation has its own slower preprocessing contract below.

The program's resource parameters and operation conventions are:

```text
n: number of input vertices, including isolated vertices
m: number of physical unit arc records
lambda: largest value actually reached by the augmenting-path builder
p: number of baseline support records for one fixed-value oracle
L: smallest positive integer with L^2 * phase_demand_count >= n^2

preprocessing, general loopless multigraph: O(n*(m+1)*(n+m+1)) operations
preprocessing, simple loopless digraph:     O(n^2*(m+1)) operations
temporary records, per constructed oracle: O(n^2+n*m+m)
retained/reporting records, fixed value:   O(p+n*sqrt(p)), or O(1) if p=0
difference report:                        O(n) hash-table/list operations
full report:                              O(p+n) hash-table/list operations
cost query:                               O(1) hash-table operations
```

These are unit arithmetic/record operation contracts. They do not assert
constant bit cost or deterministic worst-case Python hashing. The maximum
wrapper constructs at most two oracles and takes the union of their bounds.
The private constructor takes a prevalidated optimum produced by the public
builders; it does not verify an arbitrary supplied flow certificate.

## Computing an acyclic optimal baseline

Order flow objectives by original cost and then number of used records.
Initially the empty flow is optimal at value zero: original costs are
nonnegative, and the secondary objective is positive for any nonempty flow.
For a current support, each unused arc contributes its forward residual
record with signed count one; each used arc contributes its reverse with
negated cost and signed count minus one. Original IDs and direction signs
are stored explicitly, including when residual records become parallel.

Inductively the residual graph has no negative cycle in the ordered pair
of cost and signed count. Otherwise toggling a simple negative residual
cycle would give a feasible flow of the same value with a better objective.
For path computation `_shortest` adds a third coordinate counting residual
arcs. Every cycle with zero ordered-pair cost then becomes strictly positive.
Bellman–Ford strict relaxations compute these ordered-triple shortest
distances after at most `n-1` sweeps. Any shortest walk is simple, since
removing a cycle strictly improves its ordered-triple length. A further
relaxation detects a reachable negative cycle and is rejected.

The final predecessor records form simple shortest paths. For every final
predecessor arc its distance equality holds: a later strict improvement at
its tail would otherwise permit another relaxation at its head. A parent
cycle would sum these equalities to a zero ordered-triple cycle, which is
impossible. Thus following parents terminates at the supplied source for
every reachable target.

Take the shortest residual source-to-target path and toggle all its labels.
Unit capacities and conservation give a feasible flow of the next value.
For any competing integral next-value flow, its signed difference from the
current flow decomposes into a residual source-to-target path and residual
cycles. The cycles have nonnegative ordered-pair cost, and the chosen path
minimizes that ordered pair. Thus the next flow is optimal in cost and used
count. This proves the induction. If there is no residual path, any feasible
next-value flow would contradict that same decomposition. A larger-value
flow would contain a next-value subflow after decomposing into paths and
cycles, so the value is maximum.

Each augmentation increases value by one; the source has at most `m`
outgoing records, so the process terminates. A positive directed support
cycle could be cancelled to lower original cost or, for a zero-cost cycle,
lower used count. Baseline optimality excludes both cases. Hence its support
is acyclic. The topological-span proof in the flow manuscript, Section 2,
now applies when the original graph is simple.

## One residual graph suffices for every failure

For reporting, rebuild the residual graph using original signed costs and
secondary hop cost one on every residual record. Optimality of the baseline
excludes negative primary cycles; positive hop cost makes every cycle
strictly positive lexicographically. Primary-optimal paths of minimum hop
count are therefore simple.

If the failed ID is unused, the baseline remains feasible and optimal. For
a used arc from `u` to `v`, seek a shortest residual path from `u` to `v`.
A simple path of this orientation cannot use the failed arc's reverse:
that reverse would revisit the source or encounter the target before
finishing. Remove the failed baseline arc and toggle the path's signed
labels. This repairs exactly its endpoint imbalances and respects every
unit capacity. No original record occurs twice on a simple residual path.

Conversely the difference between any surviving equal-value flow and the
baseline is a residual circulation. Decompose it into simple cycles. One
contains the reverse of the failed record. Removing that reverse gives a
residual path of the required orientation. Every other cycle has nonnegative
cost, proving the exact cost identity (F5), including its infeasibility
convention. The implementation therefore issues precisely one demand per
baseline record in the same residual graph and stores the resulting cost
or infinity flag. There is no rebuilding of a residual graph at query time.

## Compact demand paths and original-record preservation

`CompactPaths` computes all-source shortest distances and predecessors as
temporary preprocessing data. For each reachable demand choose its fixed
simple shortest path. Unreachable demands receive a stored infinity flag.
Let a phase contain `q` still-unassigned reachable demands and choose `L`
by the exact integer contract above. Store each path of at most `L` arcs
explicitly. For the longer paths, repeatedly choose a vertex appearing on
the largest number of still-unhit paths. Store at most `ceil(n/L)` selected
vertices in this phase.

Each remaining long path has more than `L` distinct vertices. Summing
vertex incidences shows some vertex meets at least the fraction `L/n` of
the still-unhit paths. Thus after the allowed selections the remaining
long-demand count is at most its initial count times `exp(-1)`. A phase
therefore assigns a constant fraction of its demands; it always makes
progress. Each chosen vertex stores a shortest-path in-tree and out-tree,
and each hit demand stores the selected hub plus its two endpoints.
Reverse-graph shortest paths give the in-tree with original labels and
direction signs restored, not toggled.

For a hub on the fixed optimal demand path, subpath optimality shows that
the best source-to-hub path plus the best hub-to-target path has exactly
the optimal demand cost and hop count. This remains true for independently
selected in- and out-tree ties. Their concatenation cannot repeat a vertex:
removing the resulting strictly positive cycle would improve the demand
optimum. Hence the two tree traversals report a simple optimal path.

Explicit paths in this phase use at most `q*L` records. The hub trees use
at most `2*n*ceil(n/L)` vertex-pointer records. Their sum is bounded by a
constant times `q+n*sqrt(q)`. Demand descriptors add one record per demand,
including unreachable demands. The unassigned counts decrease geometrically,
so both their sums and the sums of their square roots are bounded by
constant multiples of the initial quantities. This proves the claimed
support-sensitive reporting bound. If there are no support demands, no
trees or lists are retained.

The reference retains the baseline records and every original record
labeling any stored explicit path or either kind of hub-tree arc. Their
number is no larger than baseline size plus reporting size, even when
different residual-tree records share one original ID. Every reported
residual path is contained in this retained labeled graph. The residual
identity then proves that the retained original subinstance contains an
optimum for every feasible failure.

A difference report comprises the failed arc and the simple path's labels,
so its length is at most `n`. Full output scans the stored baseline, skips
removed IDs and appends the added IDs. This requires no scan over the full
input ground. The cost table uses baseline IDs only; every other valid
original ID returns the stored baseline cost. Only the original record
count is needed to range-check an unused failure ID.

## Maximum value, work, and bit length

Deleting one unit-capacity arc from a path decomposition destroys at most
one unit path. Thus the new maximum value is the old maximum or one less.
The maximum wrapper keeps separate optimal baselines and separate compact
oracles at these two values. It first tests the upper oracle's stored cost
flag, then uses the lower oracle if necessary. The zero-maximum case uses
only its empty baseline. This proves the maximum-flow claim.

One Bellman–Ford call costs at most `O(n*(m+1))` arithmetic/record operations.
There are at most `lambda` successful baseline augmentations and one final
failed attempt for maximum flow. All-source residual preprocessing uses `n`
calls. The number of chosen hubs over geometrically shrinking phases is
`O(sqrt(p))`; each builds one reverse-graph shortest-path tree. A deliberately
simple greedy scan costs `O(n*q)` per hub in a phase, and its total is
`O(n*p^(3/2))`. The exact integer square-root calculation is charged at its
integer bit cost, or by a polynomial number of ordinary bit operations.
These quantities imply the conservative preprocessing contracts above,
using `p<=m`, and, for simple graphs, `m<n^2` and `lambda<n`. Paths and
all-source parent tables occupy the temporary-record contract. This does
not establish the manuscript's faster preprocessing implementation.

For completeness, suppose all input rational numerators and denominators
have at most `B` bits. Let `D` be the product of their denominators; it has
at most `m*B` bits. Every exact cost computed by the algorithm is an integer
multiple of `1/D`. A simple path has at most `n-1` terms; a flow has at most
`m` terms. Even intermediate in-place Bellman–Ford relaxation walks have
at most `n*m` terms within a call. Their numerators after multiplication
by `D` have `O(m*B+B+log(n*m+2))` bits. Signed-count and hop coordinates
have polynomially bounded integer magnitude. Fraction reduction, ordered
comparisons and integer arithmetic therefore have polynomial bit cost;
stored cost answers and output IDs are charged at their actual bit length.

## Review and executable boundaries

The theorem above is a complete local realization with a proved polynomial
preprocessing and exact output contract. The implementation does not claim
to execute the faster all-source/potential/heap construction, the
vertex-split path-packing wrapper, arbitrary signed-cost/general-balance
initialization, or matching and matroid clients. The latter are separate
mathematical and implementation scopes. Finite exhaustive checks compare
against independently enumerated original Boolean supports; they supplement
the proof and do not establish arbitrary-size correctness or asymptotics
on their own. No external peer review or proof-assistant verification is
claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
