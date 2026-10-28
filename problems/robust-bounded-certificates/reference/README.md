# Certified weighted unit tests and bounded common-basis gate

[bounded.py](bounded.py) supplies exact weighted matroid intersection,
original budgeted one-unit scenario tests, and the guarded local extension
algorithm. It uses only Python's standard library and exact `int`/`Fraction`
data. The [realization proof](../reference-realization.md) separates the
implemented unit interfaces from the main theorem's higher-quota algorithm.

`minimum_cost(independent1, independent2, costs, target)` uses the ground
`range(len(costs))`. Both predicates must be exact matroid independence
oracles on `frozenset` arguments. Signed rational costs are permitted.
The result is an `IntersectionCertificate` of minimum cost at the requested
cardinality, or at maximum smaller cardinality when the target cannot be
reached. Its fields are selected ground IDs, exact exchange potentials,
and an optional maximum-cardinality cut. Binary targets larger than the
ground are rejected by a cut without a numerical target loop.

`verify_intersection(...)` checks common independence and every exchange
potential inequality; an underfull answer also requires the rank cut.
It performs no optimization, shortest-path computation or negative-cycle
search. Validity of the supplied matroid oracles is an input-model
contract. `minimum_cost` uses shortest cheapest exchange augmentation,
with cost first and path length second; arbitrary cheapest walks do not
supply the required augmentation contract.

`UnitScenario(q, resource_independent, costs, budget)` builds one exact
budgeted unit test from the Boolean-cap matroid of each original resource.
`costs[player][type]` is a nonnegative rational or `None` for ineligibility.
Its resource predicates accept original owner sets, keeping all original
ranks and masks fixed. `table_scenario(ranks, costs, budget)` additionally
validates complete original integral polymatroid rank tables and supplies
those Boolean-cap predicates without expanding numerical capacities.
The complete tables are charged input; a rank-only client instead pays
for Boolean-cap independence/SFM as specified in the main proof.

- `scenario.optimize(selected)` returns a `UnitCertificate` even when the
  selected players cannot all receive a unit or their minimum cost exceeds
  the budget. The certificate records original owner/type assignments.
- `scenario.verify(certificate)` checks that minimum-cost or resource-
  infeasibility record without calling an optimizer.
- `scenario.affordable(certificate)` evaluates full coverage and its actual
  budget cost; it assumes the record was produced or verified first.
- `scenario(selected)` returns the actual unit certificate on success,
  otherwise `None`. This is directly usable by the bounded gate and the
  [Fibonacci width-two gate](../../robust-width-two-allocation/reference/README.md).

`gate(q, rank, rank_oracle, scenarios, width, forced=())` accepts exact
original player-rank queries and exact hereditary unit callbacks containing
the empty set. It returns a `GateOutcome` with `SUCCESS`, `INFEASIBLE`, or
`WIDTH VIOLATION`. Success includes one original common basis avoiding
`forced` and every scenario's actual witness. A width violation gives the
scenario and an original inclusion-minimal independent failed set larger
than `width`; it is never treated as robust infeasibility. Failure remains
sound outside the promise. Rank zero uses the empty-basis convention.
`nodes` counts every processed allowed ground, including rejected rank
nodes. Original ranks, required basis rank, budgets and resource data are
never recomputed from a smaller allowed ground.

Weighted intersection and each unit test have polynomial work in the
explicit pair ground and paid oracle work. The complete-table validator
is polynomial in the complete table encoding, which is exponentially
larger than a rank-only encoding. The bounded gate has the local corank
bound of the main proof and polynomial workspace. This reference does
not implement high-quota service LPs, integral polymatroid recovery,
integer target search or the streamed whole-ground wrapper. Source is
licensed under the repository Apache-2.0 license.

**Attribution:** icekylinx and GPT-6 Astra Pro.
