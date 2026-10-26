# Incremental directed SSSP with simple-path reporting

This is a conditional composition theorem for incremental directed shortest paths with explicit path output.

**Guarantee**

Maintains one-source approximate distances under arbitrary online edge insertions and returns a simple directed path with original edge identifiers.

**Objective and output**

For every reachable vertex, the estimate is between the true distance and one plus epsilon times the true distance. Unreachable vertices return infinity. A reported path with **k** edges costs linear output work times a polynomial in log of the global size.

**Randomness**

Deterministic path-reporting and integer zero-length reductions. The faster distance maintenance requires the deterministic cycle-search and edge-retirement guarantees listed in the source map.

**Time**

Total work $`O(n+m)+(n+m)\exp\!\left(O(\log E(N)+\sqrt{U(h+\log(1/\epsilon))})\right)`$, with $`\log E(N)=O(U^{4/5}h^{1/5})`$; conditional on the raw detector and retirement interface.

**Space**

Actual root vertices, inserted edges, and auxiliary copies over their lifetimes, with no graph padded to the master cap.

**Parameters**

**N** is the power-of-two cap; **U=log N**; **h=log(U+4)**; $`0<\epsilon\le1/2`$ with $`\log(1/\epsilon)\le c_*U`$; $`E(N)`$ is the raw-backend factor; **k** is the number of returned path edges.

**Model and representation**

Nonnegative integer root lengths in a polynomial range and parallel edges are allowed. The positive-length theorem extends to zero lengths by the fixed perturbation and exact flooring in Section 10.1. Arbitrary real or negative lengths are outside this statement. The frozen-detector raw interface must support exact retirement and callback accounting.

**Lower-bound scope**

This is an upper bound under the explicitly stated backend interfaces. It is not an unconditional published theorem and carries no new lower-bound claim.

**Review status**

**Ready for review in the stated scope.** The clipped-tree intersection and loop-removal reporting construction, including zero-length edges; the nonnegative-integer perturbation reduction and its accuracy/bit accounting.

**Conditions and remaining work.** The fast distance-maintenance theorem still requires the explicitly stated detector, cycle-search and edge-retirement data structures. The finite path tests do not validate their update time.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

Read the [proof](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact accuracy and backend hypotheses.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
