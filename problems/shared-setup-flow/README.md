# Selected flow with a shared setup and routing budget

**Guarantee**

Returns a permitted $`r`$-commodity set and common rate at least $`(1-\varepsilon)\mathrm{OPT}`$, with one shared setup and routing budget and all routing-only budgets exact.

**Objective and output**

Maximize selected concurrent rate; output the actual selected set and its splittable flow.

**Randomness**

Deterministic, conditional on the paid exact minimum-setup restriction optimizer and exact rational flow-LP primitives.

**Time**

$`\Gamma(1/\varepsilon)^c\mathrm{poly}(H)`$; for fixed rational $`\varepsilon`$, the whole-ground bound is $`\bigl(2-1/\Gamma(1/\varepsilon)\bigr)^q E(q)\mathrm{poly}(H)`$.

**Space**

Polynomial in the explicit network, selected-set state, rational flow witnesses, and paid oracle workspace.

**Parameters**

$`c=q-r`$; $`0<\varepsilon<1`$ is rational; setup fees and routing charges are nonnegative; $`\Gamma(R)=R^R/(R-1)^{R-1}`$; $`E(q)=2^{O(q\log\log(q+2)/\log(q+2))}`$. $`H`$ includes the exact minimum-setup restriction optimizer.

**Model and representation**

A fixed family of permitted $`r`$-sets with an attained exact minimum setup cost on every restriction, a rational directed network, splittable flows, and one combined exact budget.

**Lower-bound scope**

No lower bound is claimed; an ordinary existence-only restriction selector does not provide the required minimum-setup optimizer.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The exact returned set must attain the setup cost used to compute the residual routing budget. The proof maintains one protected full-rate witness through the changing budget.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
