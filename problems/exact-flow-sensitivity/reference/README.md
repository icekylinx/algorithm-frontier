# Exact unit-flow reference realization

[Implementation](unit_flow.py) · [Proof and resource contract](../manuscripts/reference-unit-flow-realization.md) · [Independent checks](../verify/check_unit_flow.py)

This standard-library implementation constructs a sparse original-record
preserver and a self-contained reporting oracle for independent single-arc
deletions. It computes exact rational minimum-cost unit flows, stores phased
short-path lists and hub trees, and reports either a difference or a full
surviving flow. The maximum-flow wrapper stores the last two feasible values.
Preprocessing has a conservative polynomial bound, distinct from the faster
preprocessing in the research theorem.

Import `unit_flow` from this directory:

```python
from fractions import Fraction
from unit_flow import Arc, MaximumFlowOracle, fixed_flow

arcs = (Arc(0, 1, Fraction(1, 3)), Arc(1, 3, 0),
        Arc(0, 2, 1), Arc(2, 3, 0))
fixed = fixed_flow(4, arcs, 0, 3, 1)
assert fixed.cost() == Fraction(1, 3)
assert fixed.cost(0) == 1
assert fixed.flow(0) == (2, 3)
assert fixed.difference(0).removed == (0, 1)

maximum = MaximumFlowOracle(4, arcs, 0, 3)
assert maximum.query(0) == (1, Fraction(1), (2, 3))
```

Vertices are integers from zero through `n-1`. Original arc IDs are their
positions in the supplied sequence. Costs must be nonnegative Python integers
or `Fraction` values; floats and negative costs are rejected. Loops are
rejected, and parallel and opposite arcs retain distinct original IDs. The
uniform simple-graph support exponent requires simplicity; the reference
accepts parallel records under the broader support-sensitive contract.

`fixed_flow(n, arcs, source, target, value)` returns `None` if the requested
original flow value is infeasible, including when it exceeds maximum flow.
Zero is permitted. A fixed oracle's `cost(failed)`, `difference(failed)` and
`flow(failed)` return `None` precisely when that value becomes infeasible.
Otherwise the difference has exact cost and original `removed`/`added` IDs;
the flow is a tuple of used original IDs with capacity one each. Omit `failed`
or pass `None` for no failure. Queries name one original ID and always refer
to the original input; they do not accumulate deletions. Out-of-range IDs,
Boolean IDs and collections of failures are rejected.

`MaximumFlowOracle(...).query(failed)` returns `(value, exact_cost, used_ids)`
for a minimum-cost maximum flow. The selected full support is feasible in
the oracle's `upper.retained` or `lower.retained` original-arc dictionary.
These dictionaries and the compact path structures contain the retained
subinstance; neither oracle retains the full input graph or all-pairs
preprocessing tables. Private `_FixedFlowOracle` construction assumes an
already proved optimal baseline and is used only by the validating builders;
it is not an adversarial certificate verifier.

Python dictionaries and sets are used for IDs. Query operation counts in the
companion proof count these as hash-table operations; this implementation
does not certify deterministic worst-case Python lookup time. Sorted
deterministic dictionaries give the manuscript's logarithmic ID lookup
alternative. Exact integers and fractions are charged at their actual bit
length. Output cost also depends on encoding the returned IDs and rationals.

The separate [native path wrapper](vertex_paths.py), proved in its
[realization note](../manuscripts/reference-vertex-path-realization.md), supplies
minimum-cost internally vertex-disjoint path packings under an original-arc
or internal-vertex failure. It restores both original vertex lists and arc
IDs, including after zero-cost-cycle removal. It supports fixed cardinality
and maximum cardinality on simple directed nonnegative-rational inputs.

The preceding `unit_flow` and path interfaces retain their nonnegative-cost
contracts. The separate signed interface below handles general balances;
matroid and blossom clients remain outside these flow interfaces.

The separate [certificate verifier](flow_certificates.py) accepts signed
rational costs, arbitrary integral outward balances, loops and parallel
original records. It checks original-input feasibility, exact reduced-cost
optimality, a maximum-flow cut or a strict infeasibility cut. It imports no
optimizer. The [certificate producer](certify_flow.py) builds potentials for
a supplied optimal support and rejects nonoptimal supports; its
`balance_feasibility` routine constructs a cost-blind feasible flow or a
violated cut without expanding binary supplies. See the
[self-contained proof](../manuscripts/independent-flow-certificates.md).
Certificate production and full-input verification are charged separately
from the compact oracle's query bounds.

```python
from certify_flow import balance_feasibility, certify_maximum
from flow_certificates import verify_maximum, verify_infeasible

value, cost, used = maximum.query(0)
certificate = certify_maximum(4, arcs, 0, 3, used, failed=0)
assert verify_maximum(4, arcs, 0, 3, certificate, failed=0)
support, cut = balance_feasibility(4, arcs, (2, 0, 0, -2), failed=0)
assert support is None
assert verify_infeasible(4, arcs, (2, 0, 0, -2), cut, failed=0)
```
`CompactPaths` is the internal reusable reporting component for a residual
graph with no negative cycles and a positive hop coordinate. It is exercised
separately by the checker, including signed primary lengths and hub routes.

Run from the repository root:

```sh
python3 problems/exact-flow-sensitivity/verify/check_unit_flow.py
```

The checker independently enumerates original Boolean arc supports. It
compares optimal values, exact costs, differences and full outputs before
and after each single failure. Its finite domain and exclusions are stated
in [the verification note](../verify/README.md).

## Signed costs, general balances and compact deletion queries

The [signed flow backend](signed_flow.py), with its
[self-contained proof](../manuscripts/reference-signed-balance-flow.md), accepts
signed exact rational costs, loops and parallel original arcs. It computes its
own optimum, including negative cycles in disconnected components.

```python
from signed_flow import minimum_balance, minimum_maximum
from signed_flow import build_balance_oracle, MaximumBalanceOracle

signed_arcs = (Arc(0, 1, -2), Arc(1, 1, -3))
certificate, cut = minimum_balance(2, signed_arcs, (1, -1))
assert cut is None and certificate.cost == -5
fixed_signed, cut = build_balance_oracle(2, signed_arcs, (1, -1))
assert fixed_signed.query(0) is None
assert fixed_signed.value(1) == -2
signed_maximum = MaximumBalanceOracle(2, signed_arcs, 0, 1)
assert signed_maximum.query(0) == (0, -3, (1,))
assert signed_maximum.query(1) == (1, -2, (0,))
```

`minimum_balance` returns an independently verified optimum certificate or an
original violated balance cut. `minimum_maximum` returns a combined optimum
and maximum-cut certificate. `build_balance_oracle` returns an initialized
oracle or an infeasibility cut. Its `query` returns original selected IDs or
`None`; `value` returns the exact cost or `None`. The maximum wrapper returns
`(value, exact_cost, used_ids)` using two consecutive initialized levels.
Queries are independent; absent integer IDs have no effect, while Boolean
and noninteger IDs are rejected. Neither compact interface retains the full
original graph. Final bounds use actual baseline support sizes, including
negative cycles, rather than source flow value. Decoding uses deterministic
binary search and dense removal arrays; exact rational bit work is separate.
Native polynomial preprocessing is distinct from the fast research theorem.

```sh
python3 -B problems/exact-flow-sensitivity/verify/check_signed_flow.py
```

## Ordinary one-element prices and supplied-catalog insertion

The [price backend](price.py), proved in the
[native realization](../reference-price-realization.md), initializes an exact
ordinary two-matroid optimum and supports independent rational cost changes.
Its all-pairs path representation has a quadratic baseline-rank term, as
specified by the canonical manuscript's simpler storage alternative.

```python
from fractions import Fraction
from price import build_price

at_most_one = lambda chosen: len(chosen) <= 1
oracle = build_price((2, -7, 5), 1, at_most_one, at_most_one, active=(0, 2))
assert oracle.query(0, 10) == (5, (2,))
assert oracle.query(1) == (-7, (1,))
assert oracle.query(1, Fraction(20)) == (2, (0,))
```

`build_price(costs, rank, independent1, independent2, active=None)` uses original
catalog IDs from zero through the cost-list length minus one. With no active
list, every catalog element is initially available. `None` means the prescribed
rank is infeasible on the active restriction. The predicates must be valid
ordinary matroid independence oracles on the complete catalog; they receive
sets of original IDs. Costs are signed integers or exact `Fraction` values.

`query(element, delta=0)` returns `(exact_cost, original_ids)`. For an active
element it changes that original cost by the increment. For an inactive
catalog element it activates only that element at its specified cost plus the
increment. Every query is relative to the original active set and costs.
Unknown IDs, Boolean IDs and floating-point increments are rejected. Ties
return the original baseline. Rank-zero queries return the empty set.

The final structure retains only original-ID descriptors, a baseline and its
cost, and a first-edge path matrix. It retains no original independence oracle
or cost list and performs no optimization, sorting or hash lookup during
queries. Insertion that increases maximum common cardinality, arbitrary
uncatalogued insertions, valuated price objectives and cumulative updates
are outside this executable contract.

```sh
python3 -B problems/exact-flow-sensitivity/verify/check_price.py
```

**Attribution:** icekylinx and GPT-6 Astra Pro.
