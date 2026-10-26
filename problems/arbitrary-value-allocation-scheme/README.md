# An approximation scheme for arbitrary-value allocation

| Field | Result |
|---|---|
| **Guarantee** | Returns an actual selected basis and an integer allocation of utility at least $(1-\varepsilon)\operatorname{OPT}$ under the exact combined setup and assignment budget. |
| **Objective and output** | Maximize minimum player-specific utility; detect whether any selected basis is affordable even at zero utility. |
| **Time** | Put $\delta=\varepsilon/3$, $J=\lfloor1/\delta\rfloor$, $K=\lceil1/\delta\rceil$, $L=\left\lceil(1-\delta)/\delta^2\right\rceil$, and $C_\delta=\binom{L+K}{K}$. Time is $\binom{q}{r}\min\{C_\delta^r,\exp(4r(J+1))\}\operatorname{poly}(H_\varepsilon)$, hence $\binom{q}{r}\exp(O(r/\varepsilon))\operatorname{poly}(H_\varepsilon)$. |
| **Space** | Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. Space includes the full rational accuracy encoding. |
| **Parameters** | $q$ is the nonloop player count; $r$ is the selected matroid rank; $0<\varepsilon\le1$ is rational; $H_\varepsilon=H+\operatorname{size}(\varepsilon)$. $H$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work. |
| **Model and representation** | Arbitrary nonnegative player-type values, integral recipient polymatroids, an actual original player basis, nonnegative setup and assignment costs, eligibility masks, and one shared scalar budget. Unused resources are allowed. |
| **Lower-bound scope** | No lower bound is claimed for this algorithm. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
