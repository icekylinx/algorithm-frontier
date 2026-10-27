# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Available executable evidence

The shared [exchange checker](../../../tools/verify_sensitivity_certificates.py) can be run from the repository root:

~~~sh
python3 tools/verify_sensitivity_certificates.py
~~~

Its minimum-hop section compares compressed exchange cycles with exhaustive optima on all subgraphs of <code class="math">K_{3,3}</code> under five integer cost profiles. This is finite evidence for the weighted exchange mechanism inherited by the exchange-based sensitivity arguments. It does not implement residual-flow repair, nonbipartite blossom augmentation, arbitrary matroid oracles, or a price sweep.

The dedicated [unit-flow reference](../reference/README.md) now implements
exact rational minimum-cost fixed-value flows, independent single-record
residual repair, a sparse original-record preserver with compact short-path
and hub-tree reports, and the two-consecutive-value maximum-flow wrapper.
Its [self-contained realization proof](../manuscripts/reference-unit-flow-realization.md)
establishes the support-sensitive record contract and its own polynomial
preprocessing bound. It does not implement the faster preprocessing ledger
of the main theorem.

```sh
python3 problems/exact-flow-sensitivity/verify/check_unit_flow.py
```

The checker independently enumerates all Boolean original-arc supports,
without residual searches, to determine feasible flow values and exact
optimal costs. It checks all 4,096 loopless directed graphs on four labeled
vertices under both an all-zero cost profile and a nonnegative rational
profile: 8,192 graph/profile instances. Another 150 fixed-seed instances
have up to seven vertices and twelve explicitly listed arcs, including
parallel records. Together they check 127,254 fixed-value failure/no-failure
queries and 58,423 maximum-flow queries. These include 12,994 infeasible
fixed-value queries and corresponding one-unit maximum-value drops, and
1,882 repairs reversing another baseline arc. Every feasible output is
independently checked for original IDs, distinctness, unit capacities,
conservation, exact cost, failure avoidance and membership in the retained
subinstance. Baseline cost/used-count optimality and acyclicity are also
checked.

A separate 96-vertex bidirected-chain fixture uses signed rational lengths
obtained by a potential transformation. It forces the hub-tree branch for
38 demands, checks simple minimum-hop reports against the known chain
distances, phase reduction and the concrete stored-record envelope. It
stores one hub and 230 counted descriptors/list entries/tree pointers.
Twenty query calls are also exercised after disabling shortest-path,
augmentation and residual-construction routines and clearing the caller's
input list. Twelve malformed input/query/negative-cycle cases are rejected.
The checker uses explicit exceptions, so optimized Python does not disable
its validations.

This finite evidence supports the implemented residual and compact-reporting
mechanisms. It does not prove arbitrary-size correctness or asymptotic size
by enumeration. The local written proof establishes those guarantees under
the exact public contract. General-balance/signed-cost initialization, blossom clients, arbitrary
matroid clients and price sweeps remain outside these reference interfaces.

## Flow and support boundaries

For a used unit-flow arc <code class="math">u\to v</code>, a simple residual <code class="math">u</code>–<code class="math">v</code> path cannot use the reverse of that arc. Residual cycle decomposition therefore proves the exact replacement-cost identity in the same residual graph for every failure. A lexicographic hop coordinate makes the reported residual path simple.

The acyclic

<!-- math-display: 58df2e79a68a8cf86014b14a
O(n\sqrt{\lambda})
-->
![Formula](../../../assets/math/58df2e79a68a8cf86014b14a.svg)
 support bound assumes a simple graph and nonnegative original costs. The support-sensitive theorem has the broader hypotheses stated in its companion; the acyclic specialization does not remove those extra assumptions by implication. Reporting the full flow scans the stored baseline support and the reported change.

Internally vertex-disjoint paths have

<!-- math-display: 387008096a415eb2a5c95f1d
O(n)
-->
![Formula](../../../assets/math/387008096a415eb2a5c95f1d.svg)
 split support. Deleting a gate represents exactly one internal-vertex failure. Structures for two consecutive values handle the possible one-unit loss of maximum flow or packing size.

## Matching, matroid, and price boundaries

The general-matching support argument retains the odd-set constraints and uses a generic maximizing objective. A laminar optimal dual alone need not span the relevant face. Query repair uses one blossom-aware augmentation, not plain directed reachability.

The unweighted two-matroid proof uses tight-set lattice dimensions and integrality of the intersection of two matroid polytopes. No analogous three-matroid integrality is assumed.

The price structure retains one starter descriptor for each original element and preserves the same lexicographic cost/hop return distance used by the exact exchange proof. Insertion from a supplied catalog is a fixed-rank statement. These scope conditions and the classical algorithmic primitives are explicit mathematical dependencies, not properties certified by the finite bipartite replay.


## Native internally vertex-disjoint path packings

The [path wrapper](../reference/vertex_paths.py) uses one unit gate per internal
vertex and maps original arc/vertex failures back to compact flow queries.
Its [local proof](../manuscripts/reference-vertex-path-realization.md) establishes
exact native costs, packing recovery, linear full output and the stated
support bound. Queries are independent single failures in a simple directed
graph; terminal deletions, parallel original arcs and simultaneous failures
are rejected.

```sh
python3 -B problems/exact-flow-sensitivity/verify/check_vertex_paths.py
```

The checker independently enumerates native simple paths and compatible
internal-vertex masks. Across 8,428 graph/profile instances it compares
161,804 fixed-value and 75,557 maximum-packing queries, including 18,238
infeasible fixed queries and one-path maximum drops. It rejects 8,428
infeasible original target values and 33 malformed cases. A forced zero-cost
circulation checks cycle removal during recovery; ten queries run after the
caller input is cleared and all optimization routines are disabled. The
written proof supplies the arbitrary-size argument; these finite comparisons
do not certify the faster research preprocessing or the other family clients.

## Independent original-input certificates and general balance feasibility

The [verifier](../reference/flow_certificates.py) imports no optimizer and
checks every surviving original record. The
[producer and balance backend](../reference/certify_flow.py) have separate
polynomial contracts proved in the
[certificate note](../manuscripts/independent-flow-certificates.md). Costs may
be signed; original loops and parallel records are allowed. General-balance
feasibility is cost-blind and never expands binary supplies into units.

```sh
python3 -B problems/exact-flow-sensitivity/verify/check_flow_certificates.py
```

Independent Boolean-support enumeration covers 789 graph/cost instances,
193,862 supports and 101,364 optimal certificates. It checks 5,389 maximum
certificates and 141,605 balance-feasibility decisions, including 65,138
infeasibility cuts. Every decision is compared with the constructive balance
backend. Another 1,157 existing compact-oracle answers are certified against
the full original graph. Twenty-five hostile witnesses/requests, a binary
supply with 101 decimal digits and a disconnected negative loop exercise
rejection and model boundaries. A fresh interpreter checks verification
with both solver and producer imports disabled.

Finite comparisons support the written arbitrary-size arguments. No
signed-cost minimum-cost solver, fast preprocessing, or constant-time
certificate verification is claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
