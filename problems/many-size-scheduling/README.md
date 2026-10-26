# Scheduling many common job sizes

**Guarantee**

For rational <code class="math">0&lt;\eta\le1</code>, returns <code class="math">C_{\max}\le\min\{2\mathrm{OPT},(2-1/(3+\eta))\mathrm{OPT}+u\}</code>.

**Objective and output**

Assign all mandatory job units and recover the original job-polymatroid bases from the workload construction.

**Randomness**

Deterministic workload aggregation, rank-based unit search, decomposition and additive rounding in both approximation variants.

**Time**

<code class="math">\mathrm{poly}(H)\min\{2^{O(h)},(h+1)^{O((1+\eta^{-1})\log(h+1))}\}</code>.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units.

**Parameters**

<code class="math">h</code> is the total rank of the largest positive size <code class="math">a</code>; <code class="math">u=\max\{p_j:p_j&lt;a,\ f_j(P)&gt;0\}</code>, or zero if no smaller jobs exist; <code class="math">\eta</code> is rational. <code class="math">H</code> includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Integral job polymatroids with common type processing sizes, arbitrary binary multiplicities, and mandatory totals. There is no arbitrary assignment-cost budget in this transfer.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

The largest smaller size contributes an explicit additive load term. The [commitment theorem](../commitment-scheduling/README.md) gives a separate computable residual-rank refinement.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
