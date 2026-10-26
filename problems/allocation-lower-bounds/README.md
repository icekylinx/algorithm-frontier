# Oracle barriers and configuration gaps

**Guarantee**

Deterministic factors strictly below <code class="math">2</code> for allocation and strictly below <code class="math">3/2</code> for two-size scheduling require <code class="math">\binom{q}{r}-1</code> recipient-rank queries on the hidden-set instances. Separate configuration constructions give a gap approaching <code class="math">r</code> for the aggregate LP and an exact gap <code class="math">2</code> for the full residual LP.

**Objective and output**

Prove oracle-query lower bounds and exact integrality gaps; distinguish the integer optimum from each explicitly defined fractional comparator.

**Randomness**

Lower bounds for deterministic rank-query algorithms, together with explicit integrality-gap constructions. These query statements do not claim the same bound for randomized algorithms.

**Time**

The query lower bound is <code class="math">\binom{q}{r}-1</code>. On balanced instances it is <code class="math">2^{q-O(\log q)}</code>. The refined heavy-cover parameter can equal zero throughout the allocation lower-bound family.

**Space**

No running-time or workspace upper bound is asserted by a lower-bound construction.

**Parameters**

<code class="math">q&gt;r\ge1</code> are the hidden ground size and rank. The refined-parameter construction uses <code class="math">q=2r</code>. The residual-LP gap uses <code class="math">r\ge3</code>.

**Model and representation**

Full rank-value oracles for the query lower bounds; explicit cardinality rank formulas for the two configuration gaps. The heavy threshold for the refined-parameter barrier is <code class="math">\mathrm{OPT}/(2+\eta)</code> with fixed <code class="math">\eta&gt;0</code>.

**Lower-bound scope**

This record contains oracle-query and relaxation-gap results. It does not assert explicit-input NP-hardness, ETH lower bounds, or optimal exponential bases for the approximation upper bounds.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Manuscript and proof](proof.md), with [dependencies and verification sources](sources.md).

## Results

**Hidden-rank allocation and scheduling query barriers**

[Main proof](proof.md)

**Strictly-below-two allocation remains hard at refined heavy parameter zero**

[Refined-parameter proof](refined-parameter-barrier.md)

**Aggregate configuration gap approaching rank; full residual configuration gap exactly two**

[Configuration-gap proofs](configuration-gaps.md)

**Attribution.** Yilin Liu · GPT-6 Astra Pro
