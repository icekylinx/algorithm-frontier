# Incremental directed SSSP with simple-path reporting

The construction maintains incremental directed shortest paths with explicit simple-path output.

**Guarantee**

Maintains one-source approximate distances under arbitrary online edge insertions and returns a simple directed path with original edge identifiers.

**Objective and output**

For every reachable vertex, the estimate is between the true distance and one plus epsilon times the true distance. Unreachable vertices return infinity. A reported path with **k** edges costs linear output work times a polynomial in log of the global size.

**Randomness**

Deterministic distance maintenance and simple-path reporting, using the realized detector and edge-retirement constructions. Zero-length handling and the exact numerical range are part of the proved reduction.

**Time**

Total work <code class="math">O(n+m)+(n+m)\exp\!\left(O(\log E(N)+\sqrt{U(h+\log(1/\epsilon))})\right)</code>, with <code class="math">\log E(N)=O(U^{4/5}h^{1/5})</code> from the constructed raw detector and retirement interface.

**Space**

Actual root vertices, inserted edges, and auxiliary copies over their lifetimes, with no graph padded to the master cap.

**Parameters**

**N** is the power-of-two cap; **U=log N**; **h=log(U+4)**; <code class="math">0&lt;\epsilon\le1/2</code> with <code class="math">\log(1/\epsilon)\le c_*U</code>; <code class="math">E(N)</code> is the raw-backend factor; **k** is the number of returned path edges.

**Model and representation**

Nonnegative integer root lengths in a polynomial range and parallel edges are allowed. The positive-length theorem extends to zero lengths by the fixed perturbation and exact flooring in Section 10.1. Arbitrary real or negative lengths are outside this statement. The frozen-detector raw interface must support exact retirement and callback accounting.

**Lower-bound scope**

This is a research upper bound with the explicitly identified local constructions and published theorem dependencies. No lower bound is claimed.

**Review status**

**Ready for review.** The complete frozen-detector incremental SSSP construction, its realized numerical interface, the simple-path reporting argument and nonnegative-integer perturbation adapter. Includes exact zero distances, clipped-tree intersections, loop removal and accuracy/bit accounting.

**Dependencies and scope.** The input, accuracy and polynomial numerical-range promises remain explicit. Reporting a path with k edges costs (k+1) poly(U). Finite path tests support the reporting lemmas and do not measure the asymptotic detector update time.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

Read the [proof](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the accuracy range, constructed interfaces and public dependencies.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
