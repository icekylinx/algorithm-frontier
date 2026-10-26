# Compulsory allocation with two common intrinsic values

| Field | Result |
|---|---|
| **Guarantee** | Returns utility at least $\operatorname{OPT}/2$ for every compulsory player under one exact assignment-cost budget. For fixed integer $d\ge2$, the same intrinsic-value model admits factor $d$. |
| **Objective and output** | Allocate integer counts with common positive resource values $u<a$, preserving each original recipient polymatroid and one budget. |
| **Time** | Exact factor two takes $(27/4)^{h_C}\operatorname{poly}(H)$ or $(50/27)^q E(q)\operatorname{poly}(H)$. For fixed integer $d\ge2$, replace $27/4$ by $A_d=\Gamma((d+1)/(d-1))$ and the global base by $2-1/A_d$. |
| **Space** | Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. |
| **Parameters** | $q$ is the compulsory-player count; $h_C$ is the maximum number of distinct recipients affordable with one large-value unit each. $\Gamma(R)=R^R/(R-1)^{R-1}$ and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. $H$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work. |
| **Model and representation** | Two common intrinsic resource values, arbitrary integral recipient polymatroids, nonnegative assignment costs, compulsory players, and one exact scalar budget. |
| **Lower-bound scope** | The [strict-below-two oracle obstruction](../allocation-lower-bounds/README.md) concerns the stated arbitrary recipient-rank model, not every explicit-item subclass. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md). |

The broader [J2 theorem](../unrelated-values-joint-role/proof.md#9-compulsory-two-valued-unrelated-instances-exact-factor-two) allows player-specific pair values in $\{0,u,a\}$, even within one shared resource type, with the same exact-two global base. Its [full integer tradeoff](../unrelated-values-joint-role/two-value-tradeoffs.md) requires compulsory players and does not obtain optional selection from a third-value dummy.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
