# Allocation with recipient matroids and a configuration comparator

**Guarantee**

Returns value at least $`T_{\mathrm{conf}}/d`$ with $`d=4-3/r`$. With a certified local factor-$`\lambda`$ oracle, use $`d=\lambda^{-1}+3-3/r`$. Factor $`d+\eta`$ has the rank-quasipolynomial alternative.

**Objective and output**

Select a player basis and integral resource bundles satisfying every recipient matroid and any supplied downward-closed local family.

**Randomness**

Deterministic current-blocker search with exact paid primitives. The optional factor-lambda availability oracle requires a certified per-call guarantee.

**Time**

$`2^{O(r)}\mathrm{poly}(H)`$ for factor $`d`$; $`\mathrm{poly}(H)\min\{2^{O(r)},(r+1)^{O((1+\eta^{-1})\log(r+1))}\}`$ for $`d+\eta`$.

**Space**

Polynomial in the original encoded matroid and resource input and paid oracle workspace. The exponentially many configurations are not input or stored.

**Parameters**

$`r\ge1`$ is the selected player rank; $`\eta>0`$ and the certified $`0<\lambda\le1`$ are rational; $`T_{\mathrm{conf}}`$ is the coupled configuration optimum. $`H`$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

One service per player-resource pair, common intrinsic resource values, arbitrary recipient matroids, an arbitrary player matroid, and a paid local availability oracle when local families are present.

**Lower-bound scope**

No lower bound is asserted. The coupled configuration comparator uses separate recipient-matroid columns; arbitrary polymatroid aggregation need not preserve it.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The manuscript defines the comparator explicitly and proves its reduction to the compact small-resource promise. No LP solution or configuration enumeration is required.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
