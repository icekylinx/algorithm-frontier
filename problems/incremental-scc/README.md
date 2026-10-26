# Incremental strongly connected components

**Guarantee**

Exact strongly connected component labels after every settled directed-edge insertion.

**Objective and output**

Maintain one explicit component label per original vertex. The record does not include a topological ordering of the quotient or a path witness.

**Randomness**

Deterministic conditional composition using the deterministic raw-cycle backend and exact nonzero-base, flow-maintenance and retirement interfaces; no randomized error allowance is stated.

**Time**

Total work $(n+m)E(N)^{O(1)}\mathrm{poly}(U)$ under the raw minimum-ratio-cycle interface, with $U=\log(N+4)$ and $E(N)=\exp(O(U^{4/5}(\log U)^{1/5}))$; this is total incremental work, not a worst-case per-insertion claim.

**Space**

Polynomial in the maintained graph, label inventory, and raw-backend state; the client does not expand binary caps into unit arrays.

**Parameters**

$n$ is the original vertex count; $m$ bounds inserted edge records; $N$ is the power-of-two master cap; $U$ is its logarithmic scale. Parallel edges and self-loops are allowed.

**Model and representation**

Conditional incremental directed graph client using the named raw minimum-ratio-cycle interface, explicit endpoint retargeting, edge retirement, and exact component-label updates.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
