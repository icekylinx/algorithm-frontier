# Exact rational concurrent-flow baseline

This dependency-free implementation supplies the continuous optimization and
separation interfaces used by the selected-flow and shared-setup-flow proofs.
It also provides an exact selected-set enumeration baseline. It uses Python
integers and `fractions.Fraction`; floating-point inputs are rejected.

```python
from concurrent import Network, optimize_selected, verify_fixed

network = Network(
    4,
    ((0, 1, 100), (2, 3, 100)),
    ((0, 1, 1), (2, 3, 1)),
)
# Rows are commodities; columns are directed arc positions.
shared = ((0, 80), ((100, 0), (0, 1)), 100)
answer = optimize_selected(network, 1, setup=shared)
assert answer.selected == (1,) and answer.rate == 20
assert verify_fixed(network, answer, setup=shared)
```

`Network.edges` lists explicit physical records, including parallel records.
Loops are rejected. `undirected=True` makes two directional arc coordinates
per physical edge, in forward/reverse order; both share its one capacity.
`Network.commodities` contains source, target and positive demand scale.
Endpoints must differ. Empty networks and zero capacities are supported.
A selected set must be nonempty; the rank-zero convention is left to callers.

`optimize_fixed` returns a `Certificate` with the selected IDs, primal vector
and dual vector. The primal's first coordinate is the common normalized rate;
remaining coordinates follow selected-commodity order, then directed-arc order.
A routing budget is a pair `(charges, cap)` with one nonnegative charge per
original commodity and directed arc. Several routing-only budgets are allowed.
The optional `setup=(fees, charges, cap)` adds one shared setup-plus-routing
budget. An unaffordable fixed set returns `None`; an affordable disconnected
set returns an exact zero-rate solution.

`optimize_selected` enumerates all sets of the requested size and applies the
supplied fixed-family predicate. Its default permits every such set. `None`
means no permitted affordable set exists. The callback must describe the same
family throughout execution and its work is additional. This does not provide
a polynomial matroid intersection implementation. Returned certificates prove
optimality of their fixed set; global optimality additionally uses exhaustive
enumeration, not a short certificate of the callback's behavior.

`verify_fixed` rebuilds the original flow rows and checks exact primal/dual
feasibility and equality of their objectives. It never invokes an optimizer.
Malformed and inexact certificate values are rejected. Its trusted model
translation is shared with the solver; independent path-formulation tests
check that translation separately.

`separate(network, rates, budgets)` executes the normalized Farkas LP. It
returns a `PackingRow` containing nonnegative physical lengths, routing-budget
multipliers, commodity potentials, the resulting nonnegative coefficients,
and the row capacity. This row is strictly violated by the query and valid
for the entire service region. `None` means membership, but does not itself
return a routing. For a shared-budget node, append its freshly computed
residual routing-budget row to the ordinary budgets before calling it.
The omission recursion and rational target search are not implemented here.

The [realization proof](../reference-realization.md) gives correspondence,
certificate soundness, finite termination and separate resource bounds.
The [independent checker](../verify/check_concurrent.py) compares against native
simple-path formulations and active-set vertex enumeration.

**Attribution:** icekylinx and GPT-6 Astra Pro.
