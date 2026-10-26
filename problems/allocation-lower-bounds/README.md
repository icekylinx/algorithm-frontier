# Oracle barriers and configuration gaps

**Guarantee**

Deterministic factors strictly below $2$ for allocation and strictly below $3/2$ for two-size scheduling require $\binom{q}{r}-1$ recipient-rank queries on the hidden-set instances. Separate configuration constructions give a gap approaching $r$ for the aggregate LP and an exact gap $2$ for the full residual LP.

**Objective and output**

Prove oracle-query lower bounds and exact integrality gaps; distinguish the integer optimum from each explicitly defined fractional comparator.

**Randomness**

Lower bounds for deterministic rank-query algorithms, together with explicit integrality-gap constructions. These query statements do not claim the same bound for randomized algorithms.

**Time**

The query lower bound is $\binom{q}{r}-1$. On balanced instances it is $2^{q-O(\log q)}$. The refined heavy-cover parameter can equal zero throughout the allocation lower-bound family.

**Space**

No running-time or workspace upper bound is asserted by a lower-bound construction.

**Parameters**

$q>r\ge1$ are the hidden ground size and rank. The refined-parameter construction uses $q=2r$. The residual-LP gap uses $r\ge3$.

**Model and representation**

Full rank-value oracles for the query lower bounds; explicit cardinality rank formulas for the two configuration gaps. The heavy threshold for the refined-parameter barrier is $\mathrm{OPT}/(2+\eta)$ with fixed $\eta>0$.

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
