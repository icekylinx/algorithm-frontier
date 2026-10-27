# Exact mixed-target cover-chain reference

[targets.py](targets.py) implements the CC mixed-target construction on complete
original rank tables. The [realization and partial audit](../reference-realization.md)
separates its finite active-system LP cost from paid polynomial intersection
and from the broader numeric-target family.

```python
from fractions import Fraction
from targets import Targets

model = Targets(
    rank=(0,2,2,3),
    coefficients=((2,1),(1,2)),
    relations=('>=','>='),
    targets=(2,2),
    scalar=(Fraction(-1),Fraction(2)),
    mandatory=True,
)
answer = model.solve()             # exact minimum signed scalar
assert model.verify(answer)
maximum = model.solve(maximize=True)
```

The original rank table is indexed by subset masks. It must be a normalized
monotone integral polymatroid rank. Coefficients and targets are nonnegative
integers. Relations independently use `<=`, `=`, or `>=`. The one signed
scalar uses exact `int`/`Fraction` coefficients. `eligible` is an optional
original-coordinate boolean tuple; `mandatory` is a boolean selecting the
original full-total base, rather than optional independent counts.

`solve(maximize=False)` returns an attaining `Answer(counts,value)`, or `None`
exactly when the original problem is infeasible. Counts use original IDs,
including masked zeros. A bound on the same scalar can be decided by the
corresponding extremum; there is no separate additional unbounded scalar row
while optimizing another scalar.

`prepare()` exposes exact eligibility/zero-target masks, surviving original
row IDs, original support patterns and mandatory rank loss. `chains()` streams
CC covering-row permutations and shared copies; `profile_vectors(chain)`
streams bounded occupied-class multiplicities. `recover(chain,h,maximize)`
solves that exact resource/partition full-total face. Prepared chains are
internal constructed objects, not independently verified input certificates.
`profiles(vectors,caps,total)` is the reusable explicit-stack occupied-vector
iterator, with nonzero vectors and binary component/total caps.

`verify(answer)` uses only original rank inequalities, target rows, masks,
mandatory original total and the actual signed scalar. It calls no compiler,
profile iterator or LP, and certifies feasibility/value rather than optimality.
Zero-rank and empty-original-ground instances are legal. Zero-target rows do
not create negative cover intervals. Mandatory masks never redefine the base
total. Optional disposal is added only to the original optional model. Real
zero-column coordinates retain their resource mass and signed scalar weights.

The implementation keeps one shared original resource across every copied
coordinate. It aggregates original subset-rank rows directly and never builds
a subset table on the copied ground. One coordinate per prescribed class is
eliminated exactly; generic streamed active systems add an explicit
`binom(M,D)` reference factor for actual remaining rows and free dimension.
This may be exponential even when the mathematical recovery primitive has
paid polynomial cost. Workspace and rational record lengths are polynomial in
the complete original-table and binary input encoding. Numerical resource
units and target-sized coefficient universes are not materialized.

For covers the outer iterator retains the explicit factorial cover-permutation
factor. This is CC software, not the stronger UP original-support interval
compiler. No seven-scheme, nonlinear, global or robust client is implemented
here. Canonical exact rank validation and PA's generic rational active-system
primitive are reused, with new standard-library Apache-2.0 source.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
