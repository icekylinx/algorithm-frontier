# Incremental strongly connected components

**Guarantee**

Exact strongly connected component labels after every settled directed-edge insertion.

**Objective and output**

Maintain one explicit component label per original vertex. The record does not include a topological ordering of the quotient or a path witness.

**Randomness**

Deterministic exact SCC maintenance and label-history construction. The source map connects the detector, flow-maintenance and edge-retirement operations to their local realizations and named published prerequisites.

**Time**

Total work

<!-- math-display: 95f80374f1a65d983f052106
(n+m)\exp\!\left(O((\log_2 N)^{4/5}(\log\log_2 N)^{1/5})\right)\mathrm{poly}(\log_2 N)
-->
![Formula](../../assets/math/95f80374f1a65d983f052106.svg)

This expands the constructed raw minimum-ratio-cycle factor using the proof's exact convention <code class="math">N=2^U</code>. Its fixed powers are absorbed into the exponential constant. The bound is total incremental work, not a worst-case per-insertion claim.

**Space**

Polynomial in the maintained graph, label inventory, and raw-backend state; the client does not expand binary caps into unit arrays.

**Parameters**

<code class="math">n</code> is the original vertex count; <code class="math">m</code> bounds inserted edge records; <code class="math">N</code> is the power-of-two master cap; <code class="math">U=\log_2N</code> is its logarithmic scale. Parallel edges and self-loops are allowed.

**Model and representation**

Incremental directed graph construction using the raw minimum-ratio-cycle engine, exact base registers, atomic endpoint retargeting, edge retirement and explicit component-label updates. The source map identifies each constructed interface and its published inputs.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

**Ready for review.** The complete incremental SCC label theorem with the raw-cycle-to-frozen-detector realization, nonzero-base handling and retirement rules. The label-history extension proves historical equality and `O(1+log log(n+2))` first-coalescence queries using permanently retired identities.

**Dependencies and scope.** The theorem gives exact component labels under the stated insertion model and adaptive-history bounds. It does not include dynamic topological-order maintenance or within-component path output. The executable history checks cover that layer separately.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Historical component queries

The same small-to-large labels store

<!-- math-display: e428e7670593a88f1506f1db
O(n\log(n+2))
-->
![Formula](../../assets/math/e428e7670593a88f1506f1db.svg)
 historical records.
They answer SCC equality at a past settled update in
<!-- math-display: f11830ebe3dac2ffab24edf4
O(1+\log\log(n+2))
-->
![Formula](../../assets/math/f11830ebe3dac2ffab24edf4.svg)
 time and first coalescence in
<!-- math-display: f11830ebe3dac2ffab24edf4
O(1+\log\log(n+2))
-->
![Formula](../../assets/math/f11830ebe3dac2ffab24edf4.svg)
 time. The latter binary-searches their common
label suffix, as proved in Corollary 9.1. These representation
bounds are unconditional once the exact merge sequence is supplied.

**Attribution.** icekylinx · GPT-6 Astra Pro
