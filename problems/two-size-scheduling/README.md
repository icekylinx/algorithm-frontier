# Scheduling two common job sizes

| Field | Result |
|---|---|
| **Guarantee** | One branch gives exact factor $3/2$ in the surplus-large-position parameter; a separate branch gives factor $5/3$ in the number of mandatory large units. Fixed integer $d\ge2$ also gives factor $2-1/d$. |
| **Objective and output** | Assign all large and small units and recover the original job-polymatroid bases. |
| **Time** | Exact $3/2$ takes $(27/4)^c\operatorname{poly}(H)$ or $(50/27)^q E(q)\operatorname{poly}(H)$. Exact $5/3$ also takes $2^{O(h)}\operatorname{poly}(H)$. More generally use $A_d^c\operatorname{poly}(H)$ or $(2-1/A_d)^q E(q)\operatorname{poly}(H)$ with $A_d=\Gamma((d+1)/(d-1))$. |
| **Space** | Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. |
| **Parameters** | $h=f_b(P)$ is the mandatory large-unit total; $q$ is the number of nonloop Boolean-cap large positions when their rank is $h$; $c=q-h$; positive sizes are $u<a$; $\Gamma(R)=R^R/(R-1)^{R-1}$ and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. |
| **Model and representation** | Two common positive job sizes, arbitrary integral job polymatroids, binary ranks, and mandatory original bases. This transfer has no assignment-cost budget. Boolean-rank loss and one-size cases are handled separately. |
| **Lower-bound scope** | The [strict-below-three-halves value-oracle barrier](../allocation-lower-bounds/proof.md) applies to the named general recipient-rank model; no broader explicit-input hardness is inferred. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md). |

The [large-unit-rank proof](rank-parameter.md) establishes the separate $h$ branch. The [integer-quota transfer](../whole-ground-allocation/integer-quotas.md) gives the full $d$ curve. For machine-specific times and exact assignment costs, see the distinct [two-time theorem](../two-time-scheduling/README.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
