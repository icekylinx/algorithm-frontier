# Complete-table intrinsic-value allocation reference

[intrinsic.py](intrinsic.py) implements the derived light-player adapter,
original heavy-type recovery, actual weighted light omission and exact-half
basis enumeration. Its light realization and joint lower rounding use streamed
exact rational LP vertices. The [realization proof](../reference-realization.md)
keeps that potentially exponential reference LP cost separate from the research
theorem's paid polynomial primitives.

```python
from fractions import Fraction
from intrinsic import Intrinsic

model = Intrinsic(
    player_rank=(0, 1, 1, 1),
    resource_ranks=((0, 2, 2, 2), (0, 1, 1, 1)),
    values=(1, 3),
)
answer = model.near(epsilon=Fraction(1, 3), budget=1)
assert model.verify(answer)
exact_half = model.exact_two(budget=1)
assert model.verify(exact_half)
```

Rank tables use original owner-subset bit masks, with equal power-of-two
length. The player table must be a matroid rank; each resource table must be
a normalized monotone integral submodular rank. Values are common nonnegative
intrinsic `int`/`Fraction` data. Zero-value/zero-rank types are ignored for
search and retain zero output counts. All original IDs are retained, including
original player loops. No assignment budget, setup charge or extra constraint
coupling resource types is accepted.

`geometry(heavy)` accepts positive original type IDs and returns the Boolean
heavy-cover, union and dual light-matroid tables, its original nonloop IDs,
rank and loop-deleted corank. `splits()` enumerates all threshold value-class
partitions, with equality on the heavy side. These records are constructed
internal geometry, not independently verified input certificates.

`completion(geometry, light_basis)` executes actual matroid-union decomposition
through the canonical certified weighted intersection. It extends the dual
component **inside the light complement**, then returns an original player
basis containing that light basis and actual one-unit assignments to original
heavy types. Binary supplies are not copied into individual resource units.

`near(epsilon,budget,fallback=None)` processes every affordable derived-corank
split and every pure-heavy split. It calls the canonical real first-crossing
omission and full-accuracy rational search on original workload rows, not an
exhaustive selected-basis substitute. Exact original light fractions are
realized by an active-basis LP and rounded jointly through original complement
resources and player-prefix caps. It returns a valid original allocation on
every input, and has the stated near-two guarantee under its exact threshold
parameter promise. The same call with the supplied light-separation margin
as accuracy gives the quantified exact-half endpoint. `last_trace` records
processed/skipped/pure-heavy splits and actual gap calls/nodes. A skipped
split is not an infeasibility declaration.

`exact_two(budget,fallback=None)` enumerates derived-basis complements only on
splits within the supplied half-threshold corank budget, reoptimizes each
fixed light basis exactly and applies the same original recovery. This
realizes the XP/zero-corank exact-half endpoint with its separate reference
LP cost. It does not establish the unresolved unrestricted exact-half FPT
claim.

`Allocation.basis` contains original owner IDs and `counts` contains original
type-major integer owner vectors, zero outside that basis. `verify` checks
actual original basis membership and every original resource inequality
without using any derived geometry, LP, union or search. It certifies
feasibility, not optimum or a parameter promise. `minimum` evaluates actual
value; it returns `None` for empty original rank to avoid assigning a finite
minimum to an empty selection. Empty/zero-resource cases are legal.

The default backend does **not** implement the published polynomial
`8+zeta` fallback. A supplied `fallback(model)` callback may return an original
allocation, whose feasibility is checked and whose actual value is compared
with the native candidates. A guaranteed public fallback must be supplied
under its own paid algorithm contract to obtain that unconditional software
guarantee. The mathematical theorem's named fallback and explicit dummy-dual
transfer remain complete independently of this software boundary.

Complete rank-table construction and weighted intersection have polynomial
cost in the charged complete-table encoding and oracle work. LP recovery
streams active systems and may take exponential time in its dimension,
while retaining polynomial rational workspace. No loop ranges over a binary
capacity, unit count or denominator's numerical value. The source is a new
standard-library implementation under Apache-2.0, with canonical neighboring
primitives imported rather than copied.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
