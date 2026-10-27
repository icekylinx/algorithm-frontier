# Exact-budget one-value reference

[one_value.py](one_value.py) implements actual original-basis allocation under
one shared nonnegative setup and assignment budget. It uses complete integral
resource-rank and player-matroid tables, original type-major assignment costs,
binary capacities and exact `int`/`Fraction` arithmetic. A positive common unit
value scales reported utility; it does not change the integer quota search.
Unused resources are allowed. Original player loops keep zero output counts.

`OneValue(player_rank, resource_ranks, costs, budget, setup=None, value=1)`
validates the complete original input. `Allocation` retains original player
IDs and original type-major integral vectors. `verify` checks every original
rank inequality, the actual selected basis and the combined budget.

| Interface | Contract |
| --- | --- |
| `zero()` | Attaining minimum-setup basis with zero counts, or `None` if even zero service is unaffordable. |
| `unit(allowed=None)` | Exact minimum-cost one-unit basis gate through actual weighted pair-matroid intersection. Each selected setup fee is paid once. |
| `fixed_quota(basis, quota)` | Exact shared-budget feasibility for a prescribed original basis and nonnegative integer quota. Returns exactly that quota at every selected player. |
| `optimize_fixed(basis)` | Exact optimum integer quota for the prescribed original basis, including its fixed setup cost. |
| `target(full, d=2, forced=(), whole_ground=False, cover_base=None, observe=None)` | Actual quota `ceil(full/d)` output or sound exclusion of the full integer target. Forced original IDs constrain selection only. |
| `optimize(d=2, whole_ground=False, cover_base=None)` | One-sided original integer search with actual saved outputs and exact combined budget. |
| `minimum(allocation)` | Actual minimum utility; `None` for an empty selected basis. |
| `service(rates, residual)` | Fractional original count-region membership with an explicitly supplied remaining assignment budget, or a strict nonnegative packing row. This analytical helper does not itself select or charge a setup basis. |

The small-target gate supplies one unit when `1 <= full <= d`; its success
does not certify the nominal full target. Larger targets run the actual
canonical weighted first-crossing omission recursion. Each node uses an
attaining minimum-setup original basis, retains its paired assignment budget,
and recovers on that same basis. Whole-ground mode runs the canonical streamed
logarithmic-block containment covers. Forced omissions and whole-ground mode
are mutually exclusive because the cover owns its omission seed.

The rational native cover defaults are `27/4` for `d=2` and `4` for `d=3`.
For larger or varying binary `d`, the native default is the certified envelope
`3*(d+1)/(d-1)`; a supplied rational base must be at least the corresponding
supported default. This avoids expanding powers with a numerical exponent
equal to a binary input. The manuscript's sharper fixed-integer algebraic
cover bases remain proved separately; the generic rational cover backend
does not implement their exact algebraic comparisons.

The [realization proof](../reference-realization.md) gives the capped-service
dual separator and the dominant scalar recovery objective. The cost row is
removed during integral recovery. No claim is made that adding a budget row
to an integral polytope preserves integrality. Numerical capacities and
quotas are never expanded into units or enumerated as count ranges.

The canonical exact Bland simplex has a finite, potentially exponential
basis bound. Its tableau and the omission/cover iterators use polynomial
workspace in the explicit complete-table input and numeric bit encodings.
This concrete LP time differs from the paid polynomial LP/intersection work
in the theorem. Weighted pair intersection and the actual omission recursion
are reused without duplicating their implementations.

Run the independent original-allocation comparison from the repository root:

```sh
python3 -B problems/one-value-exact-two/verify/check_one_value.py
```

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
