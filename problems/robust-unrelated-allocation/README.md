# Robust unrelated allocation with common setup costs

**Guarantee**

Returns per-player, per-scenario utility at least $`\max\{0,(1-\varepsilon)\mathrm{FOPT}-u_{\omega,p}\}`$ on one common actual basis. Hence robust minimum utility is at least $`\max\{0,(1-\varepsilon)\mathrm{FOPT}-u\}`$. Every scenario's combined setup and assignment budget remains exact.

**Objective and output**

Maximize robust common utility while choosing a single basis before the scenario and allowing integral assignments to adapt afterward.

**Randomness**

Deterministic common-basis selection and exact-budget rounding in each listed scenario; whole-ground selection also uses deterministic covers.

**Time**

$`\Gamma(1/\varepsilon)^c\mathrm{poly}(H)`$. For fixed rational $`\varepsilon`$, the whole-ground alternative is $`\bigl(2-1/\Gamma(1/\varepsilon)\bigr)^q E(q)\mathrm{poly}(H)`$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. All scenarios are explicit.

**Parameters**

$`c=q-r`$; $`0<\varepsilon<1`$ is rational; $`u_{\omega,p}=\max_j v_{\omega,p,j}`$; $`u=\max_{\omega,p}u_{\omega,p}`$. $`\mathrm{FOPT}`$ maximizes over one actual common basis and relaxes only scenario assignment counts. $`\Gamma(R)=R^R/(R-1)^{R-1}`$ and $`E(q)=2^{O(q\log\log(q+2)/\log(q+2))}`$.

**Model and representation**

Player-specific scenario values, integral recipient polymatroids, a common nonnegative setup vector, scenario-specific exact scalar budgets and assignment costs, one common actual player-matroid basis, and unused resources allowed.

**Lower-bound scope**

This additive guarantee does not imply a finite multiplicative guarantee when the largest-unit loss dominates. Distinct scenario setup vectors and one common integer allocation require separate arguments.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

$`\mathrm{FOPT}`$ is one comparator name, not a product of an unspecified factor and integer $`\mathrm{OPT}`$. The proof retains all fractional coordinates needed by that comparator, including pairs whose full-unit cost exceeds a positive budget.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
