# Selected splittable concurrent flow

**Guarantee**

Returns one permitted set of commodities and a feasible splittable routing of common rate at least $(1-\varepsilon)\mathrm{OPT}$.

**Objective and output**

Select exactly $r$ of $q$ commodities while preserving every edge capacity and every listed routing budget exactly.

**Randomness**

Deterministic branching and exact rational flow-LP optimization, conditional on the paid exact restriction selector; both time alternatives are deterministic.

**Time**

$\Gamma(1/\varepsilon)^c\mathrm{poly}(H)$; for fixed rational $\varepsilon$, also $\bigl(2-1/\Gamma(1/\varepsilon)\bigr)^q E(q)\mathrm{poly}(H)$.

**Space**

Polynomial in the explicit network, rational flow data, selector state, and paid optimization workspace.

**Parameters**

$c=q-r$; $0<\varepsilon<1$ is rational; $\Gamma(R)=R^R/(R-1)^{R-1}$; $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. $H$ includes all routing-budget rows and the exact restriction-selector cost.

**Model and representation**

Directed networks, or undirected networks with one shared capacity per edge, rational capacities and positive demand scales, splittable flow, nonnegative routing budgets, and a fixed-cardinality family with an exact restriction selector.

**Lower-bound scope**

No lower bound is claimed; the result requires the stated permitted-set selector. Examples include a matroid basis and suitable common-basis families.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [rational-comparator lemma](../whole-ground-allocation/rational-optimization.md) uses exact optimization of the returned selected-set LP to retain the full $\Gamma(1/\varepsilon)$ base.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
