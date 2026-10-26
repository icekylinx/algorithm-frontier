# Unrelated-value allocation with exact cost and additive loss

| Field | Result |
|---|---|
| **Guarantee** | Returns utility at least $\max\{0,(1-\varepsilon)\operatorname{FOPT}-u_p\}$ at each selected player, and hence minimum utility at least $\max\{0,(1-\varepsilon)\operatorname{FOPT}-u\}$. One assignment-cost budget is exact. |
| **Objective and output** | Choose one permitted actual player set and allocate integral recipient counts; maximize the fractional fixed-set comparator before cost-preserving rounding. |
| **Time** | $\Gamma(1/\varepsilon)^c\operatorname{poly}(H)$ against $\operatorname{FOPT}$ itself. For fixed rational $\varepsilon$, also $\bigl(2-1/\Gamma(1/\varepsilon)\bigr)^q E(q)\operatorname{poly}(H)$. |
| **Space** | Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The full rational accuracy encoding is included. |
| **Parameters** | $c=q-r$; $u_p=\max_j v_{pj}$; $u=\max_p u_p$; $0<\varepsilon<1$ is rational. $\operatorname{FOPT}$ chooses an actual permitted set and relaxes only resource counts. $\Gamma(R)=R^R/(R-1)^{R-1}$ and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. |
| **Model and representation** | Arbitrary nonnegative player-type values and assignment costs, integral recipient polymatroids, unused resources allowed, one exact scalar assignment budget, and a fixed-cardinality family with an exact restriction selector; an original player-matroid basis is a principal case. |
| **Lower-bound scope** | No multiplicative constant follows without controlling the largest-unit term. The comparator does not fractionally mix selected bases. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md). |

Exact reoptimization of the returned fixed-set LP removes the target-search loss, so the old $\Gamma(2/\varepsilon)$ fractional-comparator base is unnecessary. Positive-cost pairs whose full-unit cost exceeds the budget remain eligible for the fractional comparator.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
