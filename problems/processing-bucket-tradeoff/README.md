# A discrete scheduling tradeoff from processing buckets

**Guarantee**

For every integer $`k\ge0`$, returns makespan at most $`\gamma_k\mathrm{OPT}`$, where $`\gamma_k=\frac{3\cdot2^k-1}{2^{k+1}-1}=\frac{3}{2}+\frac{1}{2(2^{k+1}-1)}`$.

**Objective and output**

Assign all original job totals with exact recipient feasibility and one exact assignment-cost budget.

**Randomness**

Deterministic bucket enumeration and exact minimum-cost recovery, for every stated integer bucket depth.

**Time**

$`(k+1)^q\mathrm{poly}(H+k)`$. Choosing $`k=O(\log(1+1/\varepsilon))`$ gives factor $`3/2+\varepsilon`$ in $`[O(1+\log(1+1/\varepsilon))]^q\mathrm{poly}(H_\varepsilon)`$.

**Space**

Polynomial in the complete binary input and paid oracle workspace; numerical resource multiplicities are not expanded into individual units. Bucket depth is charged as stated in the time bound.

**Parameters**

$`q`$ is the physical-machine count; $`k`$ is an integer bucket depth. The first points are $`(\text{factor},\text{base})=(2,1),(5/3,2),(11/7,3),(23/15,4)`$. $`H`$ includes the explicit ground, all rational and integer encodings, and paid rank, submodular-minimization, LP, intersection, and decomposition work.

**Model and representation**

Arbitrary nonnegative rational processing times and assignment costs, integral job polymatroids, mandatory original totals, eligibility masks, and one exact scalar budget.

**Lower-bound scope**

No lower bound is claimed for this algorithm.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

For an exact $`3/2`$ guarantee at constant base, use the separate [six-profile construction](../six-profile-three-halves/README.md).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
