# Two-scenario robust allocation hardness

**Guarantee**

Exact positive service on a common player basis is W[1]-hard in corank $c$, even with two scenarios and free Boolean recipient resources.

**Objective and output**

Distinguish robust integer optimum one from zero, with the same selected basis in both scenarios and separate adaptive allocations.

**Randomness**

Deterministic parameter-preserving reduction from bounded-integer k-SUM. The stated hardness consequence concerns deterministic algorithms; no randomized reduction is needed.

**Time**

The reduction is polynomial and preserves the parameter as $c=k$. Under $\mathrm{FPT}\ne\mathrm{W}[1]$, no $F(c)\mathrm{poly}(H)$ finite-factor algorithm exists for this exact-budget positivity model.

**Space**

A polynomial-size explicit reduction; no algorithmic workspace upper bound is claimed.

**Parameters**

$q$ is the player count; $r=q-k$ is the selected uniform-matroid rank; $A=\sum_i a_i$; $L=A+1$. The two budgets are $C_1=A-T$ and $C_2=rL-A+T$.

**Model and representation**

Two explicit scenarios, a uniform player matroid, unit values, free Boolean recipient ranks, nonnegative assignment costs, zero setup fees, and exact scenario budgets.

**Lower-bound scope**

The W[1] consequence concerns parameterized exact-budget positivity. It does not imply a whole-ground exponential lower bound or a lower bound with relaxed budgets.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [finite reduction check](../../tools/verify_finite_reductions.py) verifies the two budget inequalities on small integer instances. The symbolic proof establishes the reduction for arbitrary input.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
