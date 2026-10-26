# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Executable finite exchange checks

Run the [exact exchange checker](../../../tools/verify_sensitivity_certificates.py) from the repository root:

~~~sh
python3 tools/verify_sensitivity_certificates.py
~~~

The exchange section enumerates every subgraph of $`K_{3,3}`$ under five integer cost profiles, including signed costs and an all-zero profile with ties. For each feasible prescribed rank from one through three, it finds the baseline and every failed-element optimum by direct enumeration, independently of the compressed exchange calculation.

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

The sparse exchange representation has $`O(n)`$ vertices and $`O(n+m\log^2 n)`$ arcs. Heavy-light path intervals encode the graphic exchanges; the partition exchange is the unique baseline arc entering the outside arc's head. The lexicographic cost/hop lengths and feasible-potential transformation retain the shortest-path order and exclude nonpositive directed cycles.

The construction uses $`\widetilde O(mn)`$ arithmetic operations. The final original-arc and reporting storage is $`O(n^{3/2})`$, and an explicit query report has $`O(n)`$ size. Temporary workspace and rational bit complexity are distinct quantities. The finite checker above does not implement this sparse exchange graph or the classical pairwise-distance-preserver primitive; those claims rely on the linked mathematical arguments and external algorithmic interfaces.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
