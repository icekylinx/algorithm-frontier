# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The family is supported by the activation identities, rank bounds, and prefix-span arguments in the proof and companion. No dedicated executable currently checks all color-failure queries or implements the dynamic-MSF construction. Runtime and support claims are mathematical bounds, not empirical measurements.

## Activation and rank

The query map sends every lifted edge <code class="math">uv</code> to a scalar multiple of its ordinary incidence column. That scalar is nonzero exactly when both endpoints survive. Symmetric matrix row dependencies have dimension <code class="math">\binom{t+1}{2}</code> when the vertex feature vectors span dimension <code class="math">t</code>. The cancellation argument remains valid in characteristic two.

Mixed edge/vertex labels use an edge-dependent block feature and a separate symmetric-trilinear refinement. For overlapping vertex lists, the actual feature rank can be used only when that feature matrix is constructed. The full-input gate claims the parameter envelope rather than an uncomputed actual-rank bound.

## Fixed-order prefixes and MSFs

Equality of every surviving ordered incidence-prefix span means that canonical Kruskal accepts exactly the same original edges. This covers signed weights with fixed edge-ID tie breaking. It does not assert preservation under arbitrary later recosting or preservation of shortest-path distances.

For one failed color, every surviving baseline MSF edge remains accepted. Across all color queries, the replacement lists have total size at most <code class="math">(2d_v+d_e)r</code>. The near-linear construction requires a dynamic MSF interface that reports exchanged forest edges and enumerates the nonbaseline forest only after each color-deletion batch is complete. This amortized output accounting is a separate construction from the general all-<code class="math">h</code> matrix lift.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
