# Whole-ground selection and allocation transfers

**Guarantee**

Converts a forced-omission extension of cost <code class="math">A^{c-\lvert Z\rvert}\mathrm{poly}(H)</code> into a deterministic whole-ground algorithm while preserving the original approximation, exact constraints, and comparator.

**Objective and output**

Stream an inclusion cover of the omitted set, run the original extension from each seed, and retain an actual legal output.

**Randomness**

Deterministic streamed inclusion covers and fixed-order enumeration. Bernoulli measures in the analysis count branches; the procedure draws no random bits.

**Time**

<code class="math">T_A(q,H)=(2-1/A)^q E(q)\mathrm{poly}(H)</code>, where fixed <code class="math">A&gt;1</code> and <code class="math">E(q)=2^{O(q\log\log(q+2)/\log(q+2))}</code>. Exact-one-half quota cases use <code class="math">A=27/4</code> and base <code class="math">50/27</code>; factor-three count cases use <code class="math">A=4</code> and base <code class="math">7/4</code>.

**Space**

Polynomial in the explicit ground, binary input, streamed block cover, current recursion, and paid extension workspace.

**Parameters**

<code class="math">q</code> is the explicit nonloop ground; <code class="math">c</code> is the promised omission cardinality; <code class="math">Z</code> is a forced omitted seed; <code class="math">A</code> is a supplied admissible base. Sharp algebraic base displays use fixed rational tradeoff parameters.

**Model and representation**

An all-input extension bound, a full witness surviving every seed contained in its omitted set, and legal weak success. Allocation, scheduling, robust service, and splittable flow retain their separate models.

**Lower-bound scope**

No common lower bound or optimality of the transformed bases is asserted.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

## Shared proof components

**Weighted first-crossing omissions and the <code class="math">\Gamma</code> base**

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
