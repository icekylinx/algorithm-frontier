# Two-scenario robust allocation hardness

**Guarantee**

Exact positive service on a common player basis is W[1]-hard in corank <code class="math">c</code>, even with two scenarios and free Boolean recipient resources.

**Objective and output**

Distinguish robust integer optimum one from zero, with the same selected basis in both scenarios and separate adaptive allocations.

**Randomness**

Deterministic parameter-preserving reduction from bounded-integer k-SUM. The stated hardness consequence concerns deterministic algorithms; no randomized reduction is needed.

**Time**

The reduction is polynomial and preserves the parameter as <code class="math">c=k</code>. Under <code class="math">\mathrm{FPT}\ne\mathrm{W}[1]</code>, no <code class="math">F(c)\mathrm{poly}(H)</code> finite-factor algorithm exists for this exact-budget positivity model.

**Space**

A polynomial-size explicit reduction; no algorithmic workspace upper bound is claimed.

**Parameters**

<code class="math">q</code> is the player count; <code class="math">r=q-k</code> is the selected uniform-matroid rank; <code class="math">A=\sum_i a_i</code>; <code class="math">L=A+1</code>. The two budgets are <code class="math">C_1=A-T</code> and <code class="math">C_2=rL-A+T</code>.

**Model and representation**

Two explicit scenarios, a uniform player matroid, unit values, free Boolean recipient ranks, nonnegative assignment costs, zero setup fees, and exact scenario budgets.

**Lower-bound scope**

The W[1] consequence concerns parameterized exact-budget positivity. It does not imply a whole-ground exponential lower bound or a lower bound with relaxed budgets.

**Review status**

**Ready for review.** The complete deterministic corank-parameterized finite-factor obstruction for optional common-basis selection under two exact scenario budgets, including positive-service equivalence to bounded nonnegative k-SUM, the always-feasible zero solution, binary encoding and parameter preservation.

**Dependencies and scope.** Uses the deterministic W[1]-hardness direction of Abboud, Lewi and Williams, Losing Weight by Gaining Edges, Definition 1.1, Theorem 1.3 and Section 4, and the assumption FPT differs from W[1]. The bounded nonnegative source avoids the separate randomized arbitrary-range reduction. The conclusion requires integer service, exact budgets and an optional common basis. It does not cover randomized algorithms, fractional service or relaxed budgets, and supplies no ETH or whole-ground exponential lower bound. Finite reduction checks do not certify the external hardness theorem.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The [finite reduction check](../../tools/verify_finite_reductions.py) verifies the two budget inequalities on small integer instances. The symbolic proof establishes the reduction for arbitrary input.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
