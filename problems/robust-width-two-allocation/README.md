# Robust positivity with width-two failures

**Guarantee**

Under the width-two promise, exactly decides whether a common actual player basis can receive one unit in every explicit scenario and returns the corresponding scenario allocations.

**Objective and output**

Find a common basis in the aggregate budget-feasible one-unit family; detect and return an inclusion-minimal failure of size greater than two when needed outside the promise.

**Randomness**

Deterministic conflict enumeration, graph-cover branching and exact matroid intersection; the whole-ground alternative uses deterministic covers.

**Time**

<!-- math-display: ad15afaf2a049b5476f6efd5
\left(\frac{1+\sqrt5}{2}\right)^c\mathrm{poly}(H)
-->
![Formula](../../assets/math/ad15afaf2a049b5476f6efd5.svg)

Where <code class="math">\phi=(1+\sqrt{5})/2</code>. The whole-ground bound is

<!-- math-display: b7d5b8a89f9d1efd6368d08b
\left(\frac{5-\sqrt{5}}{2}\right)^q 2^{O(q\log\log(q+2)/\log(q+2))}\mathrm{poly}(H)
-->
![Formula](../../assets/math/b7d5b8a89f9d1efd6368d08b.svg)

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. Explicit singleton and pair tests and the current branching state are stored.

**Parameters**

<code class="math">q</code> is the player count; <code class="math">r</code> is the common basis rank; <code class="math">c=q-r</code>. All scenarios, costs, budgets, and paid one-unit intersection operations are included in <code class="math">H</code>.

**Model and representation**

One common player-matroid basis, integral recipient polymatroids, explicit scenarios, separate exact nonnegative assignment budgets, and aggregate inclusion-minimal one-unit failures of size at most two.

**Lower-bound scope**

The width restriction is essential. The separate whole-ground rank-oracle barrier does not establish an optimal base for explicit-input instances.

**Review status**

**Ready for review.** The complete width-two robust theorem: exact unit gate and Boolean optimization, original dual-rank forced omissions, polynomial matching intersection/completion, Fibonacci all-input accounting and guarded outcomes, plus the Section 8 higher-quota factor-d composition and both fixed-tradeoff whole-ground conversions. The precise unchanged positive-quota packing/recovery chain has been checked against the complete bounded-certificate theorem.

**Dependencies and scope.** Original rank and exact hereditary scenario unit tests retain their paid model contracts. General budgeted unit tests now have the certified weighted bounded-certificate realization, directly compatible with the Fibonacci client. The unit gate changes only the one-time exact positivity cost; fixed original bases/ranks/scenario data, saved small-target witnesses, larger-quota separator and integral scenario recovery remain identical to BW. Local costs add, and global conversion is applied separately, proving the maximum base. The sharper global expressions require fixed tradeoff parameters. Each quota comparison uses a fixed rational power, and the unit gate uses exact quadratic arithmetic; no arbitrary real-number oracle is assumed. The width-two software implements the local unit gate and polynomial matching terminal; higher-quota LPs/recovery, target search and the streamed wrapper remain separate complete mathematical algorithms, not implemented features. Width violation remains a third structural outcome.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

Outside the promise, the guarded output may still be a valid solution or a sound failure; otherwise it includes a concrete width violation. The Fibonacci recurrence comes from branching on a forbidden pair graph and completing the residual matching through matroid intersection.

**Attribution.** icekylinx · GPT-6 Astra Pro
