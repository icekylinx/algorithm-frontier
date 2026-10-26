# Selected flow with scenario-adaptive routing

**Guarantee**

Selects one permitted commodity set and routes it in every explicit scenario at common rate at least $(1-\varepsilon)\mathrm{OPT}$.

**Objective and output**

Maximize robust selected concurrent rate; output the common set and a separate feasible splittable routing in each scenario.

**Randomness**

Deterministic for the explicit scenario list, with a paid exact selector. Scenario-dependent routing is recourse after selection, rather than randomized or adversarial input.

**Time**

$\Gamma(1/\varepsilon)^c\mathrm{poly}(H)$; for fixed rational $\varepsilon$, the whole-ground alternative is $\bigl(2-1/\Gamma(1/\varepsilon)\bigr)^q E(q)\mathrm{poly}(H)$.

**Space**

Polynomial in the full explicit scenario description, rational witnesses, selector state, and paid oracle workspace.

**Parameters**

$q$ is the commodity count; $r$ is the selected cardinality; $c=q-r$; $0<\varepsilon<1$ is rational. $\Gamma(R)=R^R/(R-1)^{R-1}$ and $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. Scenario count and routing-budget rows are charged in $H$.

**Model and representation**

Explicit rational networks and demand scales, one common selected set, exact capacities and nonnegative routing budgets, adaptive fractional flow, and an exact permitted-set restriction selector.

**Lower-bound scope**

Exact full-rate admission is W[2]-hard in the rejected count via Hitting Set, even on the stated forest instances with an unbounded explicit scenario list and no routing budgets. This does not imply the same hardness for the displayed approximate-rate output.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

Continuous scenario flows permit positive-rate approximation. The [integer robust-allocation obstruction](../robust-two-scenario-hardness/README.md) concerns a distinct positivity decision.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
