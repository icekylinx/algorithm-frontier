# Degree-constrained subgraphs

**Guarantee**

Finds an exact feasible degree-constrained edge subset, or correctly reports that none exists, in the stated reduction scope.

**Objective and output**

Supports f-factors, interval degree bounds, and cardinality optimization; outputs original edge identifiers and treats each parallel edge record as a separate selectable item.

**Randomness**

Deterministic reductions conditional on the deterministic matching backend, including Contract R and its external primitives.

**Time**

Conditional on the matching backend Contract R: $O(n+m)+(m+1)\exp\!\left(O((\log(m+2))^{4/5}(\log\log(m+4))^{1/5})\right)$.

**Space**

Polynomial in the explicit graph and reduction state; binary degree bounds are not expanded into unit copies.

**Parameters**

$n$ is the vertex count; $m$ is the explicit edge-record count; $g(v)$ and $f(v)$ are lower and upper degree bounds.

**Model and representation**

Loopless undirected multigraph with capacity one per edge record. The card does not extend the result to arbitrary weighted or binary-multiplicity variants.

**Lower-bound scope**

No new lower bound is claimed; this is a deterministic transfer from the matching backend.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
