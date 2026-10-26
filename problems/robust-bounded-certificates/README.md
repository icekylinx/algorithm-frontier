# Robust unit allocation with bounded failure certificates

| Field | Result |
|---|---|
| **Guarantee** | For fixed integer $d\ge2$, returns at least $\lceil K_\star/d\rceil$ units on one common selected basis under every scenario budget, assuming all inclusion-minimal aggregate one-unit failures have width at most $w$. |
| **Objective and output** | Maximize robust minimum unit count with scenario-adaptive integral allocations; output a common basis and one allocation per scenario. |
| **Time** | Let $A=\max\{w,\Gamma((d+1)/(d-1))\}$. Time is $A^c\operatorname{poly}(H)$ or $(2-1/A)^q E(q)\operatorname{poly}(H)$. |
| **Space** | Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The complete explicit scenario list is part of the input. |
| **Parameters** | $q$ is the player count; $r$ is the common basis rank; $c=q-r$; $d\ge2$ is a fixed integer; $w$ bounds inclusion-minimal failure size; $K_\star$ is the robust optimum count. $\Gamma(R)=R^R/(R-1)^{R-1}$ and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. |
| **Model and representation** | One common actual player-matroid basis, explicit scenarios, scenario-specific recipient polymatroids and nonnegative exact assignment budgets, and one unit value. The width promise concerns the aggregate budget-feasible one-unit family, at least on player-independent sets. |
| **Lower-bound scope** | No universal corank-FPT finite-factor guarantee exists in the unrestricted two-scenario model unless $\mathrm{FPT}=\mathrm{W}[1]$; see the [hardness proof](../robust-two-scenario-hardness/README.md). The width promise is substantive. |
| **Review status** | The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed. |
| **Source** | [Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md). |

Outside the width promise the guarded algorithm may return a legal solution, a sound negative result, or an explicit inclusion-minimal failure wider than $w$. For $w\le6$, exact factor two retains base $27/4$; for $w\le4$, factor three retains base $4$. The [width-two gate](../robust-width-two-allocation/README.md) improves the positivity subroutine further.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
