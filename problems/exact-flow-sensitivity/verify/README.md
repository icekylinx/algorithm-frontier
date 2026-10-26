# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Available executable evidence

The shared [exchange checker](../../../tools/verify_sensitivity_certificates.py) can be run from the repository root:

~~~sh
python3 tools/verify_sensitivity_certificates.py
~~~

Its minimum-hop section compares compressed exchange cycles with exhaustive optima on all subgraphs of $K_{3,3}$ under five integer cost profiles. This is finite evidence for the weighted exchange mechanism inherited by the exchange-based sensitivity arguments. It does not implement residual-flow repair, nonbipartite blossom augmentation, arbitrary matroid oracles, or a price sweep. There is no dedicated executable certificate for this family's flow, general-matching, or support-size theorems.

## Flow and support boundaries

For a used unit-flow arc $u\to v$, a simple residual $u$–$v$ path cannot use the reverse of that arc. Residual cycle decomposition therefore proves the exact replacement-cost identity in the same residual graph for every failure. A lexicographic hop coordinate makes the reported residual path simple.

The acyclic $O(n\sqrt{\lambda})$ support bound assumes a simple graph and nonnegative original costs. The support-sensitive theorem has the broader hypotheses stated in its companion; the acyclic specialization does not remove those extra assumptions by implication. Reporting the full flow scans the stored baseline support and the reported change.

Internally vertex-disjoint paths have $O(n)$ split support. Deleting a gate represents exactly one internal-vertex failure. Structures for two consecutive values handle the possible one-unit loss of maximum flow or packing size.

## Matching, matroid, and price boundaries

The general-matching support argument retains the odd-set constraints and uses a generic maximizing objective. A laminar optimal dual alone need not span the relevant face. Query repair uses one blossom-aware augmentation, not plain directed reachability.

The unweighted two-matroid proof uses tight-set lattice dimensions and integrality of the intersection of two matroid polytopes. No analogous three-matroid integrality is assumed.

The price structure retains one starter descriptor for each original element and preserves the same lexicographic cost/hop return distance used by the exact exchange proof. Insertion from a supplied catalog is a fixed-rank statement. These scope conditions and the classical algorithmic primitives are explicit mathematical dependencies, not properties certified by the finite bipartite replay.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
