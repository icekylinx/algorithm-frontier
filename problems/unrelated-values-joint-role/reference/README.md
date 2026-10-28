# Shared-role exact reference

`joint.py` accepts complete original rank tables and exact rational data.
Type-major arrays preserve unrelated player values and assignment costs.
No binary supply is expanded. The [realization proof](../reference-realization.md)
specifies the signed dummy, support LP, integer prefix face and runtime.

```python
instance = Joint((0, 1, 1, 2), ((0, 4, 1, 5),),
                 ((1, 10),), ((1, 0),), 3)
answer = instance.quota_target(3, factor=2)
assert instance.verify(answer)
```

- `zero()` returns a minimum-setup original basis with zero counts, or `None`.
- `gap(theta,k,full,weak,forced=(),global_base=None)` runs the actual adaptive
  weighted omission and returns a fractional `RoleWitness` or `None`.
- `near(epsilon,heavy_budget=None,global_base=None)` processes masks and exact
  omitted-light-role cardinalities, then rounds an actual original output.
  A restricted budget must include original corank and the promised heavy
  support. The default has no support promise.
- `exact_two()` streams every light-role set and returns an original
  exact-half solution. `quota_target(T,d)` is the stronger compulsory
  two-positive-value full-target gap, including its exact boundary gates.
- `verify` and `minimum` read only original data and canonical output records.

Complete-table validation, finite LP active-basis enumeration, temporary
projected support storage and exact rational power comparisons are charged
explicitly. This is not the polynomial-oracle implementation of the theorem.
The support list can use exponential memory. `quota_target` does not compute
the theorem's affordable-support parameter. No arbitrary negative original
costs, multiple exact budgets or common robust fractional dummy are accepted
by the model.

Run `python3 problems/unrelated-values-joint-role/verify/check_joint.py`
from the repository root.

**Attribution:** icekylinx and GPT-6 Astra Pro. **License:** Apache-2.0.
