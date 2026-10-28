# Exact-table arbitrary-value profile reference

[scheme.py](scheme.py) implements the actual original-basis profile scheme,
exact shared budget and original-value-grid optimization. Its
[realization proof](../reference-realization.md) accounts separately for
streamed active-system LP costs and the theorem's paid polynomial primitives.

```python
from fractions import Fraction
from scheme import Scheme

model = Scheme(
    player_rank=(0,1,1,1),
    resource_ranks=((0,2,2,2),),
    values=((1,),(3,)),
    costs=((1,),(2,)),
    setup=(0,1),
    budget=3,
    epsilon=Fraction(1,2),
)
answer = model.optimize()
assert model.verify(answer)
```

All rank tables use original owner-subset masks with the same power-of-two
length. The player table is a matroid rank and resources are integral
polymatroid ranks. Value and assignment-cost matrices are owner-major;
returned integer counts are original type-major owner vectors. Values,
costs, setup, budget and accuracy use `int` or `Fraction`. `None` values
forbid a pair. Data are nonnegative; accuracy lies in `(0,1]`. Unused
resources are allowed. Original IDs and loops are preserved; candidate bases are enumerated only
on original nonloop IDs.

`zero()` finds a minimum-setup original basis and returns it with zero
counts, or `None` if no basis is affordable even at zero utility.
`target(T)` streams every affordable original basis and its occupied
profiles. A returned allocation has actual original utility at least
`(1-epsilon)*T`; `None` proves that no original integer allocation meets
full target `T`. Weak successes need not be monotone. Capped fractional
target feasibility is deliberately not the comparator.

`optimize()` performs one-sided search on the original integer-utility
grid and returns at least `(1-epsilon)*OPT` against original integer
optimum, with no extra accuracy loss. An unaffordable model returns
`None`. Rank zero returns the empty allocation and `minimum` returns
`None` for its empty selection; a positive-rank zero optimum has value
zero. Empty type families are legal.

`grouping(basis,T)` reports only occupied bins with exact endpoint ties.
`plans(basis,T)` streams exactly the bounded PA count profiles using the
canonical pruned scheduling iterator. `fractional(plan)` solves the
actual joint LP with all original ranks, exact bin equalities and one
assignment budget after setup. `recover(plan,witness)` validates that
fractional witness, then optimizes actual cost on one integral
complement-prefix face, using a single disposal coordinate per resource.
Its original integer output preserves every lower prefix and never
increases assignment cost. It may change individual big-bin counts.

`verify(answer)` checks only actual original feasibility, masks, integer
counts and the shared setup-plus-assignment budget. It calls no producer
and certifies neither optimum nor a nominal target. `minimum(answer)`
evaluates actual uncapped original utility. `last_stats` reports the last
positive target's basis/profile/LP traversal counters and, after
optimization, its number of grid trials; these are observed work counts,
not asymptotic certificates.

Original complete rank tables and doubled disposal tables are charged
input/workspace. Each LP streams at most `binom(R,D)` active systems for
actual remaining row count `R` and free dimension `D<=m*q` after exact
fixed-coordinate substitutions, with polynomial exact work per system. That potentially exponential factor is additional to the theorem's
profile envelope. Recovery uses vertex optimization on the integral
face, never loops through binary supply counts. No table is indexed over
all numerical accuracy bins. Workspace and rational record lengths are
polynomial in the complete encoded input and full accuracy encoding.

Canonical rank validation, base-coordinate elimination, exact Gaussian
elimination and occupied-profile iteration are reused rather than copied.
The standard-library source is new Apache-2.0 code.

**Attribution:** icekylinx and GPT-6 Astra Pro.
