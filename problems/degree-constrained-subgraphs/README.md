# Degree-constrained subgraphs

**Guarantee**

Finds an exact feasible degree-constrained edge subset, or correctly reports that none exists, in the stated reduction scope.

**Objective and output**

Supports f-factors, interval degree bounds, exact or ranged cardinality constraints, and cardinality optimization; outputs original edge identifiers and treats each parallel edge record as a separate selectable item.

**Randomness**

Deterministic reductions using any correct deterministic exact matching solver. The faster bound additionally requires the cycle-search implementation and published prerequisites of the matching theorem.

**Time**

The unconditional reduction constructs an $`O(m\log(m+2))`$-size simple subcubic graph and uses one exact matching call for feasibility, including exact/ranged cardinality, or $`O(\log(m+2))`$ calls for optimization. Conditional on the faster matching theorem's cycle-search implementation, total time is $`O(n+m)+(m+1)\exp\!\left(O((\log(m+2))^{4/5}(\log\log(m+4))^{1/5})\right)`$.

**Space**

Polynomial in the explicit graph and reduction state; binary degree bounds are not expanded into unit copies.

**Parameters**

$`n`$ is the vertex count; $`m`$ is the explicit edge-record count; $`g(v)`$ and $`f(v)`$ are lower and upper degree bounds.

**Model and representation**

Loopless undirected multigraph with capacity one per edge record. The card does not extend the result to arbitrary weighted or binary-multiplicity variants.

**Lower-bound scope**

No new lower bound is claimed; this is a deterministic transfer from the matching backend.

**Review status**

**Ready for review.** Theorem 1.1: unconditional sparse deterministic reductions for prescribed degrees, degree intervals, and exact or ranged cardinality, with both extension and decoding directions. Cardinality feasibility uses one exact matching call.

**Conditions and remaining work.** The displayed fast running time requires the faster conditional general-matching implementation. Any correct exact maximum-matching solver, including the standard-library reference solver, suffices for the unconditional reduction theorem.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
