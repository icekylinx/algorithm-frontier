# Exact rational importance and ridge-query core

[`importance.py`](importance.py) implements exact arbitrary-rank PSD
importance, singular-background certificates, one-failure scores and
supplied-pool score accounting. [`regression.py`](regression.py) implements
the unconstrained quadratic/ridge query core for a supplied response
subspace. Both use the Python standard library and exact integers/Fractions.
They do not generate random pools, sample a sparsifier, build label codes,
or solve arbitrary constrained convex regression.

```python
from fractions import Fraction
from importance import PSDInstance
from regression import Regression

instance = PSDInstance(
    matrices=(((1, 1), (1, 1)), ((1, 0), (0, 0))),
    labels=({0}, set()),
)
certificate = instance.masses()
assert instance.verify_masses(certificate)
assert certificate.total == 2
assert instance.verify_one_failure(instance.one_failure())
scores = instance.pool_scores(1, (set(), {0}))
assert instance.verify_pool_scores(scores)

model = Regression(((1,), (2,)), ((1,), (0,)), ({0}, set()))
x = model.solve(transform=((1,),), regularization=Fraction(1, 2))
assert model.verify_solution(x, ((1,),), Fraction(1, 2))
```

An item's original ID is its input position. Every item is a whole explicit
symmetric PSD matrix of the same dimension. Nonnegative weights may already
be absorbed into those matrices. Background is one fixed explicit PSD
matrix, zero by default. Nonnegative integer label IDs may overlap and may
include zero. Floating point data, indefinite/asymmetric matrices, malformed
dimensions and negative labels are rejected. Zero matrices, zero ambient
dimension and singular backgrounds are legal.

`masses(item_ids)` returns a `MassCertificate` with original selected IDs,
a rational generalized inverse of background plus their sum, and one exact
importance value per original item, zero outside the selected set. These
are the pseudoinverse trace scores in the manuscript even though the
certificate matrix need not equal the Moore–Penrose inverse. Its total is
the actual background effective dimension of that restriction; without a
background it is the actual rank. `verify_masses` reconstructs the original
sum, checks the generalized-inverse identity and checks every trace value.
It calls neither a matrix inverse producer nor an optimizer.

`one_failure()` explicitly processes the no-failure and each occurring
single-label scenario, computes exact per-item maxima and the sharper
data-dependent total-mass bound. `verify_one_failure` verifies all those
records. This is polynomially many scenarios; no arbitrary-failure family
is enumerated. Unknown failed label IDs have no effect in query methods.

`pool_scores(h, pools)` accepts an **explicit supplied list of label pools**.
It forms each pool's original items by containment of their whole label
sets, then computes the averaged estimator, including the baseline term.
`verify_pool_scores` checks the original pool memberships, every mass
certificate, the exact estimator and its deterministic total-mass bound.
This certificate does not certify the probabilistic coverage event or
universal domination. A bad pool list can pass this accounting check and
fail domination; the independent checker includes exactly such an example.
The original IDs and one common score per whole item remain fixed.

`plan(h, error, failure_probability)` performs exact rational preflight.
It clips the failure budget to the used-label universe, computes the
scenario **count** and the pool multiplier without listing failures, and
uses a conservative integer upper bound on the logarithms. The four modes
are `EMPTY`, `FULL_INPUT`, `POOLS_NEEDED` and `ORDINARY_SCORES`. Only the
first two return completed weights, respectively zero or one on original
items. The empty gate uses the actual effective dimension. The full-input
gate runs before oversized pool work and returns pool count zero. The two
nontrivial modes return required counts with `weights=None`; they do not
claim to have sampled anything. Actual rational data lengths, matrix
dimensions and explicit supplied pool counts are charged.

`verify_embedding(weights, failed, error)` checks both PSD inequalities on
the original surviving sum plus fixed background. It proves an all-vector
embedding for that **specified scenario** by exact PSD elimination. It
does not enumerate or certify a random all-scenario event.

`Regression(design, response_basis, labels, base_regularization)` keeps
the supplied response coordinates and constructs their augmented PSD
items and fixed base background. Its `psd` property exposes the importance
and embedding interfaces. A query gives a rational response transform,
regularization at least the supplied base, failed labels, and optional
nonnegative original-row weights. `solve` returns an exact unconstrained
ridge minimizer, setting free coordinates to zero in singular normal
equations. `verify_solution` checks those original normal equations without
solving them. `objective` evaluates the original or supplied-weight
surviving quadratic objective exactly. Multiple responses, dependent
response coordinates, singular designs, zero variables and zero response
space are supported. The objective guarantee of a supplied sketch still
requires the appropriate embedding; arbitrary weights get no approximation
certificate merely because their ridge problem is solved exactly.

All matrix operations and verifiers are polynomial in explicit rational
input and certificate encoding length. A certificate contains full matrix
and score records, rather than a sparse summary. The
[realization argument](../manuscripts/reference-rational-importance-regression.md)
states the exact proof and software boundary. Run:

```sh
python3 problems/correlated-spectral-regression/verify/check_importance_regression.py
```

**Attribution:** icekylinx and GPT-6 Astra Pro.
