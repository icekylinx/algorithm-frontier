# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The family is supported by the activation identities, rank bounds and prefix-span arguments in the proof and companion. The [rational vertex-color backend](../reference/README.md) now realizes the sharp componentwise theorem, with an explicit [implementation proof](../manuscripts/reference-vertex-color-realization.md).

```sh
python3 problems/graph-color-failure-certificates/verify/check_vertex_colors.py
```

The independent checker passes 371 graph/color/budget instances, 2,099 failure queries and 24,388 ordered-prefix connectivity comparisons. Thirty-five classical sharpness examples meet the bound exactly; seven malformed-input or over-budget cases are rejected. It uses independent reachability flood fills and a partition-based canonical forest scan, with exhaustive small simple graphs, seeded multigraphs, parallel records, loops, isolates and signed rational ties.

The executable covers one color per vertex. Mixed edge colors, overlapping lists, finite fields and the near-linear dynamic-MSF construction remain separate mathematical constructions. No full dynamic-MSF backend is claimed. Runtime and support claims are mathematical bounds, not empirical measurements. Literature comparisons retain their stated source-check limits and are not a historical-priority certification.

## Activation and rank

The query map sends every lifted edge <code class="math">uv</code> to a scalar multiple of its ordinary incidence column. That scalar is nonzero exactly when both endpoints survive. Symmetric matrix row dependencies have dimension

<!-- math-display: 9cae79263ac8b219dbe824a4
\binom{t+1}{2}
-->
![Formula](../../../assets/math/9cae79263ac8b219dbe824a4.svg)
 when the vertex feature vectors span dimension <code class="math">t</code>. The cancellation argument remains valid in characteristic two.

Mixed edge/vertex labels use an edge-dependent block feature and a separate symmetric-trilinear refinement. For overlapping vertex lists, the actual feature rank can be used only when that feature matrix is constructed. The full-input gate claims the parameter envelope rather than an uncomputed actual-rank bound.

## Fixed-order prefixes and MSFs

Equality of every surviving ordered incidence-prefix span means that canonical Kruskal accepts exactly the same original edges. This covers signed weights with fixed edge-ID tie breaking. It does not assert preservation under arbitrary later recosting or preservation of shortest-path distances.

For one failed color, every surviving baseline MSF edge remains accepted. Across all color queries, the replacement lists have total size at most

<!-- math-display: 08fd74b9b38e01cc5a51262c
(2d_v+d_e)r
-->
![Formula](../../../assets/math/08fd74b9b38e01cc5a51262c.svg)
. The near-linear construction requires a dynamic MSF interface that reports exchanged forest edges and enumerates the nonbaseline forest only after each color-deletion batch is complete. This amortized output accounting is a separate construction from the general all-<code class="math">h</code> matrix lift.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
