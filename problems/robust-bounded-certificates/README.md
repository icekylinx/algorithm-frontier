# Robust unit allocation with bounded failure certificates

**Guarantee**

For fixed integer <code class="math">d\ge2</code>, returns at least <code class="math">\lceil K_\star/d\rceil</code> units on one common selected basis under every scenario budget, assuming all inclusion-minimal aggregate one-unit failures have width at most <code class="math">w</code>.

**Objective and output**

Maximize robust minimum unit count with scenario-adaptive integral allocations; output a common basis and one allocation per scenario.

**Randomness**

Deterministic width-guarded branching and exact unit tests. A width-violation certificate reports a failed promise, rather than a probabilistic failure.

**Time**

Let <code class="math">A=\max\{w,\Gamma((d+1)/(d-1))\}</code>. Time is <code class="math">A^c\mathrm{poly}(H)</code> or <code class="math">(2-1/A)^q E(q)\mathrm{poly}(H)</code>.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. The complete explicit scenario list is part of the input.

**Parameters**

<code class="math">q</code> is the player count; <code class="math">r</code> is the common basis rank; <code class="math">c=q-r</code>; <code class="math">d\ge2</code> is a fixed integer; <code class="math">w</code> bounds inclusion-minimal failure size; <code class="math">K_\star</code> is the robust optimum count. <code class="math">\Gamma(R)=R^R/(R-1)^{R-1}</code> and <code class="math">E(q)=2^{O(q\log\log(q+2)/\log(q+2))}</code>.

**Model and representation**

One common actual player-matroid basis, explicit scenarios, scenario-specific recipient polymatroids and nonnegative exact assignment budgets, and one unit value. The width promise concerns the aggregate budget-feasible one-unit family, at least on player-independent sets.

**Lower-bound scope**

No universal corank-FPT finite-factor guarantee exists in the unrestricted two-scenario model unless <code class="math">\mathrm{FPT}=\mathrm{W}[1]</code>; see the [hardness proof](../robust-two-scenario-hardness/README.md). The width promise is substantive.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

Outside the width promise the guarded algorithm may return a legal solution, a sound negative result, or an explicit inclusion-minimal failure wider than <code class="math">w</code>. For <code class="math">w\le6</code>, exact factor two retains base <code class="math">27/4</code>; for <code class="math">w\le4</code>, factor three retains base <code class="math">4</code>. The [width-two gate](../robust-width-two-allocation/README.md) improves the positivity subroutine further.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
