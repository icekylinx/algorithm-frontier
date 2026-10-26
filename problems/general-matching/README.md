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

```math
O(n+m)+(m_s+1)\exp\!\left(O((\log(m_s+2))^{4/5}(\log\log(m_s+4))^{1/5})\right).
```

**Space**

Polynomial in the actual graph and backend inventory; normalization does not require losing physical edge identifiers.

**Parameters**

**n** is the vertex count; **m** is the input edge-record count; **m_s** is the retained edge count after normalization; loops and parallel lifetimes are handled by the source contract.

**Model and representation**

Arbitrary undirected graphs, exact output, and the named raw-backend Contract R plus external primitives. The conditional backend assumptions are part of the claim.

**Lower-bound scope**

This card records a conditional upper bound and backend boundary. It does not claim a new unconditional matching lower bound.

**Review status**

**Ready for review in the stated scope.** The unconditional input reductions in Section 3: the sharp c-neighbor kernel, componentwise composition, the native mixed-failure kernel in the companion, and the subcubic reduction with its decoder.

**Conditions and remaining work.** The four-fifths running-time theorem remains conditional on Contract R and the deterministic primitives listed in sources.md. The mixed-failure kernel assumes a fixed simple graph; discarded parallel records and correlated labels are outside its scope.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Matching-size refinement

Let $`\nu(G)`$ be the maximum matching size. The exact-preserving kernel in the proof retains

```math
m_H\le\min\{m_s,O(\nu(G)^2)\}.
```

The second term of the running time may use $`m_H`$ in place of $`m_s`$, while input reading and normalization still cost $`O(n+m)`$. Original edge identifiers are restored after the exact solution is obtained.

For a computed vertex cover of size $`c`$, the explicit edge bound is
$`m_H\leq\min\{m_s,\binom c2+c^2\}`$. Processing connected components
separately replaces the solve term by the sum of the corresponding
component costs; no matching-size estimate is supplied as input.

For a fixed simple graph, the [mixed-failure extension](../../manuscripts/graph-backends/matching-size-kernel-corollary.md#4-one-kernel-for-mixed-vertex-and-edge-failures)
retains at most $`\binom c2+c(c+f)`$ edges and simultaneously preserves
the exact matching number after every mixture of at most $`f`$ native
vertex/edge deletions. This is an unconditional deterministic kernel;
each query still needs a matching solver.

Read the [proof](proof.md), [source map](sources.md), and [complete index](../../CONTENTS.md) for the backend contract and audit trail.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
