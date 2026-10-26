# Exact general-graph matching

This is a conditional composition theorem for exact maximum-cardinality matching in arbitrary undirected graphs.

**Guarantee**

Returns an exact maximum-cardinality matching while preserving the original identifier of every selected edge.

**Objective and output**

Maximize the number of matched edges and return the selected edge identifiers after loops and parallel records have been normalized.

**Randomness**

Deterministic conditional composition, requiring deterministic external primitives and a deterministic implementation of Contract R.

**Time**

Under Contract R,

$$
O(n+m)+(m_s+1)\exp\!\left(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5})\right).
$$

**Space**

Polynomial in the actual graph and backend inventory; normalization does not require losing physical edge identifiers.

**Parameters**

**n** is the vertex count; **m** is the input edge-record count; **m_s** is the retained edge count after normalization; loops and parallel lifetimes are handled by the source contract.

**Model and representation**

Arbitrary undirected graphs, exact output, and the named raw-backend Contract R plus external primitives. The conditional backend assumptions are part of the claim.

**Lower-bound scope**

This card records a conditional upper bound and backend boundary. It does not claim a new unconditional matching lower bound.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Matching-size refinement

Let $\nu(G)$ be the maximum matching size. The exact-preserving kernel in the proof retains

$$
m_H\le\min\{m_s,O(\nu(G)^2)\}.
$$

The second term of the running time may use $m_H$ in place of $m_s$, while input reading and normalization still cost $O(n+m)$. Original edge identifiers are restored after the exact solution is obtained.

Read the [proof](proof.md), [source map](sources.md), and [complete index](../../CONTENTS.md) for the backend contract and audit trail.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
