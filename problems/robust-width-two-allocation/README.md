# Robust positivity with width-two failures

**Guarantee**

Under the width-two promise, exactly decides whether a common actual player basis can receive one unit in every explicit scenario and returns the corresponding scenario allocations.

**Objective and output**

Find a common basis in the aggregate budget-feasible one-unit family; detect and return an inclusion-minimal failure of size greater than two when needed outside the promise.

**Randomness**

Deterministic conflict enumeration, graph-cover branching and exact matroid intersection; the whole-ground alternative uses deterministic covers.

**Time**

$\phi^c\mathrm{poly}(H)$, where $\phi=(1+\sqrt{5})/2$. The whole-ground bound is $\left(\frac{5-\sqrt{5}}{2}\right)^q E(q)\mathrm{poly}(H)$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. Explicit singleton and pair tests and the current branching state are stored.

**Parameters**

$q$ is the player count; $r$ is the common basis rank; $c=q-r$. $E(q)=2^{O(q\log\log(q+2)/\log(q+2))}$. All scenarios, costs, budgets, and paid one-unit intersection operations are included in $H$.

**Model and representation**

One common player-matroid basis, integral recipient polymatroids, explicit scenarios, separate exact nonnegative assignment budgets, and aggregate inclusion-minimal one-unit failures of size at most two.

**Lower-bound scope**

The width restriction is essential. The separate whole-ground rank-oracle barrier does not establish an optimal base for explicit-input instances.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

Outside the promise, the guarded output may still be a valid solution or a sound failure; otherwise it includes a concrete width violation. The Fibonacci recurrence comes from branching on a forbidden pair graph and completing the residual matching through matroid intersection.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
