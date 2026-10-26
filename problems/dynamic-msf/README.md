# Dynamic minimum spanning forest baseline

**Guarantee**

Maintains an exact minimum spanning forest in a fully dynamic weighted graph under the stated deterministic reduction.

**Objective and output**

Preserve the minimum spanning forest after each settled update; the source charges the update certificate and the forest reconstruction separately.

**Randomness**

Deterministic derived public baseline using deterministic decomposition and pruning in the stated worst-case MSF reduction.

**Time**

Worst-case per-update work is $`\exp(O(U^{2/3}h^{1/3}))`$, with $`U=\log(N+4)`$ and $`h=\log(U+4)`$. This is a derived public baseline, not a single-source theorem statement.

**Space**

Actual weighted-edge inventory, hierarchy certificates, retired records, and pruning state; no master-cap padding is materialized.

**Parameters**

$`n`$ is the vertex count; $`m`$ is the current edge count; $`N`$ bounds lifetime edge records; $`U`$ is log of $`N`$ plus a constant; $`h`$ is log of $`U`$ plus a constant.

**Model and representation**

Deterministic fully dynamic weighted multigraph, with the public decomposition, pruning, contraction, and child-forest certificate interfaces named by the source.

**Lower-bound scope**

No lower bound is claimed. The displayed point is a baseline and should not be advertised as an improvement over the cited public reduction.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
