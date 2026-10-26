# Whole-ground selection and allocation transfers

**Guarantee**

Converts a forced-omission extension of cost $`A^{c-\lvert Z\rvert}\mathrm{poly}(H)`$ into a deterministic whole-ground algorithm while preserving the original approximation, exact constraints, and comparator.

**Objective and output**

Stream an inclusion cover of the omitted set, run the original extension from each seed, and retain an actual legal output.

**Randomness**

Deterministic streamed inclusion covers and fixed-order enumeration. Bernoulli measures in the analysis count branches; the procedure draws no random bits.

**Time**

$`T_A(q,H)=(2-1/A)^q E(q)\mathrm{poly}(H)`$, where fixed $`A>1`$ and $`E(q)=2^{O(q\log\log(q+2)/\log(q+2))}`$. Exact-one-half quota cases use $`A=27/4`$ and base $`50/27`$; factor-three count cases use $`A=4`$ and base $`7/4`$.

**Space**

Polynomial in the explicit ground, binary input, streamed block cover, current recursion, and paid extension workspace.

**Parameters**

$`q`$ is the explicit nonloop ground; $`c`$ is the promised omission cardinality; $`Z`$ is a forced omitted seed; $`A`$ is a supplied admissible base. Sharp algebraic base displays use fixed rational tradeoff parameters.

**Model and representation**

An all-input extension bound, a full witness surviving every seed contained in its omitted set, and legal weak success. Allocation, scheduling, robust service, and splittable flow retain their separate models.

**Lower-bound scope**

No common lower bound or optimality of the transformed bases is asserted.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

## Shared proof components

**Weighted first-crossing omissions and the $`\Gamma`$ base**

[Selection theorem](selection.md)

**Attained residual budgets and a protected full witness**

[Adaptive selection](adaptive-selection.md)

**Streamed logarithmic-block inclusion covers**

[Polynomial-space conversion](global-conversion.md)

**Exact fixed-set rational reoptimization without splitting accuracy**

[Rational comparator recovery](rational-optimization.md)

**Exact integer quota and scheduling tradeoffs**

[Integer quotas](integer-quotas.md)

**Model-specific consequences and oracle boundaries**

[Transfer theorem](proof.md)

The [arbitrary-value joint-role record](../unrelated-values-joint-role/README.md) adds the setup extension, J2, and the exact-factor-two enumeration endpoint. None is obtained by treating binary numerical counts as an explicit ground.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
