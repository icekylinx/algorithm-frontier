# Dynamic spanners with recourse tradeoffs

Two dynamic-spanner constructions are retained because their recourse contracts differ. Their stretch exponents should not be compared while dropping those assumptions.

**Guarantee**

Maintains a spanner of an arbitrary-degree undirected graph with the stated stretch, size, amortized work, and output-recourse guarantee.

**Objective and output**

Maintain a sparse spanner and report its current edge set after settled updates.

**Randomness**

Both displayed spanner constructions are deterministic conditional on the stated deterministic hierarchy and forest interfaces. Randomized public baselines are comparisons only.

**Time**

Tracked-terminal construction: total initialization/update work $(n+m_0+I+D)\exp(O(U^{4/5}h^{1/5}))$; full-horizon construction: $(n+m_0+I+D)\exp(O(U^{5/6}h^{1/6}))$.

**Space**

The current spanner has the fixed vertex count multiplied by the chosen stretch factor in edges. The hierarchy pays actual initial edges and actual update history.

**Parameters**

**n** is the fixed vertex count; **m0** is the initial edge count; **I** and **D** count edge insertions and deletions; **N** is the declared polynomial history cap; **U** is log of N plus a constant; **h** is log of U plus a constant. **D** is also the deletion term in the full-horizon recourse bound.

**Model and representation**

Unweighted undirected graphs, with distinct identifiers for parallel edge lifetimes and settled external updates. Both constructions have amortized bounds. Self-loops are discarded.

**Lower-bound scope**

This page records two upper-bound constructions and their incomparable recourse assumptions. It does not claim an optimality lower bound.

**Review status**

The [verification note](verify/README.md) records the proof scope, executable evidence and remaining conditions. No proof-assistant verification or external peer review is claimed.

**Source**

[Complete theorem and proof](proof.md), [dependencies and primary sources](sources.md).

## Two recourse regimes

Write $M=n+m_0+I+D$ and $E_a=\exp(O(U^a h^{1-a}))$.

**Tracked original terminals**

**Stretch.** $E_{4/5}$

**Current edges.** $nE_{4/5}$

**Total work.** $ME_{4/5}$

**Total output recourse.** $ME_{4/5}$

**Full-horizon construction**

**Stretch.** $E_{5/6}$

**Current edges.** $nE_{5/6}$

**Total work.** $ME_{5/6}$

**Total output recourse.** $(n+D)E_{5/6}$

Both conclusions depend on the named flat-forest hierarchy. The full-horizon construction removes cumulative insertions from output recourse, so neither construction dominates the other in every displayed quantity.

Read the [proof](proof.md), [source map](sources.md), and [complexity guide](../../docs/COMPLEXITY.md) for the exact envelopes and recourse accounting.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
