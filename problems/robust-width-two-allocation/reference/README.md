# Executable width-two unit gate

[width_two.py](width_two.py) implements the local exact one-unit gate using
original player-rank and exact scenario-unit callbacks. The standard-library
implementation performs polynomial matroid intersection at matching leaves;
it does not enumerate their endpoint choices.

`solve(q, rank, rank_oracle, scenarios, forced=())` accepts player IDs from
`range(q)`. `rank_oracle(C)` must be the exact rank of the original player
matroid on `C`; the supplied `rank` must equal its full rank. Each scenario
callback accepts a `frozenset` of original player IDs and returns either an
actual exact one-unit allocation witness or `None` for infeasibility. The
callback family must be hereditary, contain the empty set, and retain all
original resource and budget constraints. An empty witness tuple is a
success. These oracle contracts are paid assumptions, rather than tests of
arbitrary Python functions for mathematical validity.

The immutable `Outcome` has one of three statuses:

- `SUCCESS` supplies an original player basis, avoiding `forced`, and one
  actual callback witness per scenario.
- `INFEASIBLE` soundly excludes a robust unit basis avoiding `forced`.
- `WIDTH VIOLATION` gives the scenario index and an inclusion-minimal
  original infeasible set of size at least three. Another feasible basis
  might still exist; this outcome is not an infeasibility declaration.

`nodes` counts processed dual-cover nodes, including failed matching leaves.
Initial oracle preprocessing and rejected contraction attempts are separate
polynomial work. On the width-two class the third status cannot occur.
Rank zero uses the empty-basis convention, and matroid loops are harmless.

`intersection(ground, independent1, independent2)` is the polynomial
shortest-augmenting-exchange matroid intersection primitive. Its ground is
an ordered tuple of distinct integer IDs and both predicates must be valid
matroid independence oracles. It also works with loops; they cannot occur
on an augmenting path relevant to both matroids.

The [realization proof](../reference-realization.md) supplies the algorithm
mapping and exact complexity boundary. The reference realizes the local
Fibonacci gate in the paid oracle model. It does not implement general
budgeted polymatroid allocation, higher-quota optimization or the streamed
whole-ground wrapper. It uses deterministic arithmetic and no third-party
packages. Source is licensed under the repository Apache-2.0 license.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
