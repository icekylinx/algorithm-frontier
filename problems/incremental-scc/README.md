# Incremental strongly connected components

**Guarantee**

Exact strongly connected component labels after every settled directed-edge insertion.

**Objective and output**

Maintain one explicit component label per original vertex. The record does not include a topological ordering of the quotient or a path witness.

**Randomness**

Deterministic label-history construction and conditional SCC maintenance. The latter requires deterministic cycle search, exact flow maintenance and edge retirement under adaptive updates.

**Time**

Total work $`(n+m)E(N)^{O(1)}\mathrm{poly}(U)`$ under the raw minimum-ratio-cycle interface, with $`U=\log(N+4)`$ and $`E(N)=\exp(O(U^{4/5}(\log U)^{1/5}))`$; this is total incremental work, not a worst-case per-insertion claim.

**Space**

Polynomial in the maintained graph, label inventory, and raw-backend state; the client does not expand binary caps into unit arrays.

**Parameters**

$`n`$ is the original vertex count; $`m`$ bounds inserted edge records; $`N`$ is the power-of-two master cap; $`U`$ is its logarithmic scale. Parallel edges and self-loops are allowed.

**Model and representation**

Conditional incremental directed graph client using the named raw minimum-ratio-cycle interface, explicit endpoint retargeting, edge retirement, and exact component-label updates.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

**Ready for review in the stated scope.** The small-to-large persistent label history, historical equality queries, and first-coalescence queries in O(1+log log(n+2)) time via a binary search on the shared suffix.

**Conditions and remaining work.** The history layer assumes correct monotone component merges and permanently retired label identities. The faster SCC update algorithm still requires the cycle-search, exact flow and edge-retirement operations listed in sources.md.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Historical component queries

The same small-to-large labels store $`O(n\log(n+2))`$ historical records.
They answer SCC equality at a past settled update in
$`O(1+\log\log(n+2))`$ time and first coalescence in
$`O(1+\log\log(n+2))`$ time. The latter binary-searches their common
label suffix, as proved in Corollary 9.1. These representation
bounds are unconditional once the exact merge sequence is supplied.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
