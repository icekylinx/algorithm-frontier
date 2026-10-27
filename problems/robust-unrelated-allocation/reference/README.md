# Robust unrelated exact reference

`Robust` accepts one complete original player-matroid table, a nonempty
explicit scenario list, and one common nonnegative setup vector. Each
scenario is `(ranks, type_major_values, type_major_costs, budget)`.
All counts, costs and values are exact integers or `Fraction` objects.

- `zero()` returns a common minimum-setup basis with no assignments, or
  `None` when no original basis can meet all budgets.
- `gap(full,weak,forced=(),global_base=None)` uses actual weighted
  first-crossing omission, minimum attained common setup, and independent
  scenario support separation on the original physical ground.
- `fractional(basis)` reoptimizes the original fixed-basis comparator.
  `optimize(epsilon,global_base=None)` performs the canonical full-accuracy
  rational search and independent scenario rounding on the same actual basis.
- `verify` checks original rank rows, integer counts, actual common basis and
  exact combined scenario budgets without any producer or LP.

The [realization proof](../reference-realization.md) distinguishes the
canonical fast theorem from the local finite active-basis LP reference.
The latter stores projected support vectors and may take exponential time
and memory; binary numerical supply is never expanded. There is no common
fractional dummy, common heavy/light role mask, scenario-specific setup
vector or common integer assignment requirement.

Run `python3 problems/robust-unrelated-allocation/verify/check_robust.py`
from the repository root.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. **License:** Apache-2.0.
