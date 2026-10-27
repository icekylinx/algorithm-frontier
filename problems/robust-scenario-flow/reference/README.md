# Exact adaptive-scenario reference

[scenarios.py](scenarios.py) reuses the canonical
[selected-flow rational backend](../../selected-flow/reference/README.md).
It accepts an explicit nonempty tuple of `Scenario(network, budgets)`
records. Every network has the same positive commodity count and original
commodity IDs; topology, terminals, positive demand scales, directional
charges and budget counts may differ. Capacities, demands and costs are
exact `int` or `Fraction` values. Each budget is a commodity-by-directed-arc
charge matrix and its nonnegative cap. Physical undirected capacities remain
shared across both directional arc records.

- `optimize_fixed(scenarios, selected)` returns exact optimal certificates for
  the same nonempty distinct commodity tuple in every scenario. Its `rate`
  is their minimum. `routings()` scales each optimal routing down to this
  common rate, including legal zero routings at zero optimum.
- `verify_fixed(scenarios, certificate)` checks all original scenario
  primal/dual certificates and common commodity identity, without calling
  an optimizer. This establishes fixed-set robust optimality.
- `optimize_selected(scenarios, rank, permitted)` enumerates the original
  commodity combinations and returns an exact maximizing common set, or
  `None` for an empty permitted family. The predicate is fixed and paid.
- `separate(scenarios, rates)` returns the first rejecting scenario index
  and its normalized nonnegative packing row, or `None` for membership.
  Membership alone does not reconstruct routing.

The [realization proof](../reference-realization.md) proves these contracts.
The reference keeps one scenario list and polynomial-size certificates;
Bland simplex and explicit commodity-set enumeration have their own
potentially exponential time bounds. This reference does not implement
weighted omission, rational target search or the streamed global wrapper.
It is deterministic and has no third-party dependencies. Source is licensed
under the repository Apache-2.0 license.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
