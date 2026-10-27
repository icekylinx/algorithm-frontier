# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Executable finite exchange checks

Run the [exact exchange checker](../../../tools/verify_sensitivity_certificates.py) from the repository root:

~~~sh
python3 tools/verify_sensitivity_certificates.py
~~~

The exchange section enumerates every subgraph of <code class="math">K_{3,3}</code> under five integer cost profiles, including signed costs and an all-zero profile with ties. For each feasible prescribed rank from one through three, it finds the baseline and every failed-element optimum by direct enumeration, independently of the compressed exchange calculation.

| Finite domain or outcome | Count |
|---|---:|
| Unweighted bipartite graphs | 512 |
| Integer cost profiles | 5 |
| Feasible fixed-rank instances | 6,180 |
| Single-failure queries | 11,040 |
| Queries with a feasible exact repair | 7,530 |
| Infeasible queries | 3,510 |
| Simple compressed cycles examined | 10,804 |

The replay checks that cycle costs are nonnegative, repair existence agrees with direct feasibility, and minimum-cost/minimum-hop repairs have the exact optimum gap, distinct outside labels, and a literal feasible toggle. These are finite instances of two partition matroids. They do not establish the theorem for arbitrary matroids, valuated matroids, or the arborescence implementation.

## Exchange and oracle boundaries

The common-base convex decomposition includes multiplicities when outside labels repeat. The replacement-value identity first establishes the existence of a supported optimum. A separate minimum-hop argument establishes distinct labels and a literal feasible toggle; the value identity alone does not supply that conclusion.

The valuated extension requires initial finite-domain bases, or independence access that supplies them. A bare extended-value oracle may hide its only feasible basis and does not justify the initialization time. Exact arithmetic and the bit lengths of rational oracle answers remain part of the stated access model.

## Arborescence implementation

The sparse exchange representation has

<!-- math-display: 387008096a415eb2a5c95f1d
O(n)
-->
![Formula](../../../assets/math/387008096a415eb2a5c95f1d.svg)
 vertices and

<!-- math-display: 8349033980bbe479c40ba0e0
O(n+m\log^2 n)
-->
![Formula](../../../assets/math/8349033980bbe479c40ba0e0.svg)
 arcs. Heavy-light path intervals encode the graphic exchanges; the partition exchange is the unique baseline arc entering the outside arc's head. The lexicographic cost/hop lengths and feasible-potential transformation retain the shortest-path order and exclude nonpositive directed cycles.

The construction uses

<!-- math-display: b9d235996578dfc5ca86cac1
\widetilde O(mn)
-->
![Formula](../../../assets/math/b9d235996578dfc5ca86cac1.svg)
 arithmetic operations. The final original-arc and reporting storage is

<!-- math-display: 975ee40c8b70041b0eef8aa8
O(n^{3/2})
-->
![Formula](../../../assets/math/975ee40c8b70041b0eef8aa8.svg)
, and an explicit query report has

<!-- math-display: 387008096a415eb2a5c95f1d
O(n)
-->
![Formula](../../../assets/math/387008096a415eb2a5c95f1d.svg)
 size. Temporary workspace and rational bit complexity are distinct quantities.

## Executable supplied-baseline arborescence reporting

Run the [independent arborescence checker](check_arborescence_reporting.py):

```sh
python3 problems/exact-failure-preservers/verify/check_arborescence_reporting.py
```

The [reference backend](../reference/README.md) implements the actual
heavy-light/segment-tree auxiliary graph and deterministic phased short-path
and hub-tree reporting from a supplied optimum directed rooted baseline.
The [realization proposition](../manuscripts/reference-arborescence-reporting.md)
matches its transitions, lexicographic shortest paths and literal original-ID
updates to the companion's proved construction. It uses dense exact
Floyd–Warshall preprocessing. It does not claim the optimized arithmetic
preprocessing bound displayed above or compute the initial optimum baseline.

The checker enumerates all root-entering-arc-free loopless directed graphs
on four labeled vertices at a fixed root, under five nonnegative integer or
rational cost profiles. One profile is all zero. It enumerates rooted
directed spanning arborescences independently to supply baseline optima and
every failure optimum. Each HLD transition row is compared against a direct
graphic-forest exchange test; the partition endpoint is checked separately.
Reports must be spanning directed trees, avoid the failed original ID, attain
the independently enumerated value, use only retained support, and minimize
the number of added outside labels among optimal repairs.

Six bidirected-path fixtures on ten, twenty-five and sixty-five vertices,
with zero or rational outside costs, exercise actual hub-tree reports.
Their failure optima follow independently by forced root-to-failure paths;
they are not supplied by an exponential baseline search. Boundary fixtures
cover a single vertex, a nonzero root, parallel original arcs, ignored loops
and root-entering arcs. Nine malformed or suboptimal-baseline inputs are
rejected. Two additional checks delete the caller's input list and disable
all preprocessing functions before reporting.

| Finite domain or outcome | Count |
|---|---:|
| Four-vertex graph topologies | 512 |
| Cost profiles | 5 |
| Feasible four-vertex profile instances | 1,520 |
| Profile instances without a spanning baseline | 1,040 |
| Directly checked baseline transition rows | 4,754 |
| Ordinary query comparisons | 11,491 |
| Feasible ordinary queries | 9,090 |
| Infeasible ordinary queries | 2,401 |
| Queries using stored hub trees | 171 |
| Queries using stored explicit paths | 2,184 |
| Larger path fixtures | 6 |
| Other boundary fixtures | 2 |
| Largest auxiliary graph vertex count | 255 |

The executable scope is the named supplied-baseline arborescence backend.
Finite graph checks do not establish arbitrary-matroid or valuated exchange
theorems, the optimized preprocessing implementation, or lower-bound
reductions. Those retain the linked mathematical proofs and primary
dependencies. No proof-assistant verification is claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
