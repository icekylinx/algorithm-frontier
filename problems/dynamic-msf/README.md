# Dynamic minimum spanning forest baseline

**Guarantee**

Maintains an exact minimum spanning forest in a fully dynamic weighted graph under the stated deterministic reduction.

**Objective and output**

Maintain the exact forest with original edge identifiers and publish its changes after each settled update. Enumerating the whole forest additionally costs its output size; connectivity queries use the maintained forest.

**Randomness**

Deterministic derived public baseline using deterministic decomposition and pruning in the stated worst-case MSF reduction.

**Time**

Worst-case per-update work is $`\exp(O(U^{2/3}h^{1/3}))`$, with $`U=\log(N+4)`$ and $`h=\log(U+4)`$. This is a derived public baseline, not a single-source theorem statement.

Initialization costs $`(n+m_0)\exp(O(U^{2/3}h^{1/3}))`$, where $`m_0`$ is the initial edge count. Connectivity queries cost a polynomial logarithm.

**Space**

Actual weighted-edge inventory, hierarchy certificates, retired records, and pruning state; no master-cap padding is materialized.

**Parameters**

$`n`$ is the fixed vertex count; $`m`$ is the current edge count; $`N`$ bounds vertices, initial edges and subsequent update records; $`U`$ is log of $`N`$ plus a constant; $`h`$ is log of $`U`$ plus a constant.

**Model and representation**

Deterministic fully dynamic weighted multigraph with adaptive edge updates and immutable edge-ID tie breaking. The public decomposition, pruning, contraction and child-forest certificate interfaces are named in the source map. Weight comparison is constant-time in the comparison model, or uses polynomially many bits in $`\log N`$.

**Lower-bound scope**

No lower bound is claimed. The displayed point is a baseline and should not be advertised as an improvement over the cited public reduction.

**Review status**

**Ready for review in the stated scope.** The formal weighted MSF certificate and pruning substitution: local exchange/contraction proofs, literal connectivity adapter, finite pruning horizons, deterministic decomposition parameters and the NSW recursive cost calculation.

**Conditions and remaining work.** This is a derived public baseline using Chuzhoy–Gao–Li–Nanongkai–Peng–Saranurak Corollary 6.1, Meierhans–Probst Gutenberg–Saranurak Theorem 6.4, and Nanongkai–Saranurak–Wulff-Nilsen Theorem 7.1 and Section 9. It is not an executable implementation or a consequence of the research matching router.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
