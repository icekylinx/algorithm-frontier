# Certified rational importance and supplied-response ridge realization

The [reference](../reference/README.md) realizes the exact algebraic core
of the [PSD importance manuscript](correlated-failure-spectral-and-regression-summaries.md)
and the unconstrained quadratic client of the
[weak convex-regression lemma](weak-convex-regression-under-correlated-failures.md).
The scope includes arbitrary-rank original PSD items, a fixed possibly
singular PSD background, original overlapping label sets and rational
coefficients. The software accepts supplied pools; it does not generate
random pools or a sampled sparse summary.

## 1. Rational generalized inverses certify the true trace scores

**Lemma 1.** Let `H` be a PSD matrix, and let a symmetric matrix `G`
satisfy `H G H=H`. For any symmetric matrix `B` supported on the range
of `H`, the trace `tr(BG)` equals `tr(B H^dagger)`.

**Proof.** In an orthonormal basis of the range and kernel, `H` is a
positive diagonal block and a zero block. The stated identity forces the
range-to-range block of `G` to be the inverse positive block. The range
support of `B` makes all its other blocks zero. Their trace product
therefore agrees with the Moore–Penrose trace, independently of the
remaining blocks of `G`. QED.

**Proposition 2.** `masses(items)` returns exactly the manuscript's
regularized importance traces on those original items, and
`verify_masses` verifies that fact without computing an inverse.

**Proof.** Exact symmetric Schur elimination validates every input item
and the background. A zero diagonal pivot must have zero residual row;
otherwise the matrix is not PSD. Positive pivot positions give a positive
definite original principal minor. The constructor inverts that minor
and embeds its inverse on those original coordinates, zero elsewhere.
Schur-complement elimination proves that this rational `G` satisfies
`H G H=H` for the background-plus-item sum `H`, including rank zero.

Each selected PSD item has range inside the range of `H`. Lemma 1 hence
identifies every returned trace with the true pseudoinverse importance.
The verifier reconstructs `H` from original item IDs, checks symmetry and
the exact identity, and checks the rational trace of every original item.
It rejects scores outside the selected set and invalid exact-number types.
It does not trust a claimed inverse, rank statistic or producer history.
Without a background their total is the exact rank. With a background it
is the exact restricted effective dimension, not rounded ambient rank.
All records use rational matrix products and polynomial determinant bit
bounds. QED.

Deletion monotonicity follows from the manuscript's inverse variational
identity on each item's range, also when rank drops. The total effective
dimension increases with the containing set. For positive definite
background this is operator monotonicity of `X(I+X)^(-1)` after background
congruence; a positive diagonal perturbation gives the singular-background
case. These statements do not assert a global pseudoinverse matrix order.

## 2. Exact one-failure and supplied-pool accounting

**Proposition 3.** The one-failure constructor computes the exact robust
maximum score of every original item, and its verifier proves the
data-dependent bound of the importance manuscript's Equation 9, replacing
rank by the fixed-background effective dimension where appropriate.
The supplied-pool constructor and verifier prove the estimator and its
deterministic mass bound on every supplied pool outcome.

**Proof.** The no-failure and each occurring single-label scenario are
explicit, so there are only linearly many covariance calculations. The
constructor takes each coordinate maximum; deleted items have trace zero.
For surviving items, deletion monotonicity gives nonnegative increments
above the baseline. Bounding a maximum by the sum of these nonnegative
increments and summing gives exactly the recorded data-dependent bound.
The scenario total statistic is monotone, so the bound is at most the
baseline effective dimension times one plus the largest item-label count.
The verifier reconstructs every original scenario and checks all traces,
the maxima and this accounting directly.

For an explicit pool, membership means that **all** labels of an original
item lie in that pool. Its certified total is at most the baseline
effective dimension. Summing the baseline plus the estimator's common
`2 Gamma / J` multiple of the pool scores gives the deterministic bound
`(1+2 Gamma)` times baseline dimension. This holds for bad pools too.
The verifier checks precisely that bound and the estimator's exact
original-ID coordinates.

For any particular item/failure pair separated by at least `J/(2 Gamma)`
supplied pools, every such pool contains the item and is contained in the
surviving set. Deletion monotonicity proves that its estimator dominates
that pair's true trace. The random construction's coverage event gives
this implication simultaneously. The executable accounting verifier does
not assert that event. A valid accounting certificate alone is therefore
not an all-failure importance certificate. QED.

The importance manuscript proves the all-pair coverage event by independent
Bernoulli label pools, followed by an independent item-sampling experiment
conditional on coverage. A union bound retains the explicit scenario-count
logarithm. This is a completed probability proof; the absence of those
sampling stages in the reference is a software boundary.

## 3. Planner gates and the concrete count envelope

`plan` computes the exact rational pool multiplier, clips the failure
degree at the explicit used-label count, and computes the scenario count
as a binomial sum. It does not list the scenarios. Its logarithmic
upper bound is at least one and at least the natural logarithm, using
exact numerator/denominator bit lengths and a power-of-two comparison.

If the full-input effective dimension is at most the requested embedding
error, every restricted whitened data matrix has norm at most that error.
Keeping only the fixed background is therefore already a valid relative
embedding for every failure. This proves the `EMPTY` weights. Otherwise
the planner compares its conservative sample-count envelope against the
number of original items and returns the original unit weights in
`FULL_INPUT` mode before calculating a positive pool-work count.

For the nontrivial branch the envelope is the ceiling of
`48 Gamma rho error^(-2)` times the integer logarithmic upper bound for
`4 n Q / failure_probability`, with `n` the original ambient dimension.
The pool count uses `8 Gamma` times the logarithmic upper bound for
`4 N Q / failure_probability`. The pool coverage calculation budgets at
most a quarter of the requested failure probability.

To check that the constant is conservative, condition on dominating scores
of total `T<=3 Gamma rho`. In each surviving range, a whitened importance
draw and its mean lie between zero and `T I`, while the mean is also at
most identity. The centered summand has norm at most `T` and variance at
most `T I`. Tropp, *User-friendly tail bounds for sums of random matrices*,
[arXiv:1004.4389v7, Theorem 6.1](https://arxiv.org/pdf/1004.4389),
applied to both signs gives the matrix-Bernstein exponent at least
`3 k error^2/(8T)` for `0<error<1`. The planner's sample envelope makes
that exponent at least six times its logarithmic upper bound, more than
needed for a union bound over the counted scenarios. The ceiling and
exact treatment of tiny effective dimension are included.

This count argument states the work needed by the mathematical sampling
construction. `POOLS_NEEDED` and `ORDINARY_SCORES` deliberately return
`weights=None`. When the nontrivial envelope is below item count and
effective dimension exceeds error, the pool multiplier and number of
pools are polynomially bounded by explicit input and accuracy. The
rational powers defining the multiplier and the binomial count have
polynomial bit length after clipping the degrees. The planner neither
tests a random code nor turns a supplied pool list into a random event.

## 4. Exact embeddings and the ridge query core

**Proposition 4.** `verify_embedding` proves the two fixed-background
PSD inequalities for the specified failure scenario and every real query
vector. `Regression.solve` returns a global minimizer of the supplied
unconstrained surviving ridge objective, and `verify_solution` certifies
that optimum without solving a system.

**Proof.** The embedding verifier reconstructs both surviving original
matrix sums. Exact symmetric PSD elimination checks their lower and upper
differences. These matrix inequalities quantify over all real vectors;
they are not tests of finitely many numerical query directions. They
concern the explicitly specified scenario, with no inferred all-failure
sampling event.

The regression core augments each original design row by its supplied
response coordinates. The fixed background is the base regularization
on design coordinates and zero on response coordinates. A query's
response transform produces the actual original response rows; labels
delete those rows as whole original items. Optional nonnegative sketch
weights remain original-ID indexed and the regularization is kept exact.

The returned coefficients solve the exact positive-semidefinite normal
equations. Their right-hand side is orthogonal to the Hessian kernel,
so the system is consistent even for singular designs. Gaussian
elimination may set free coordinates to zero; no minimum-Euclidean-norm
choice is required for objective optimality. Vanishing gradient is
necessary and sufficient for this convex quadratic. The verifier checks
that original equation directly. It retains the original regularization
and original response transform instead of treating a reduced selected
ground as a new problem. QED.

For a verified embedding at the fixed augmented background, every later
regularization at least its base and every supplied-subspace response
transform inherit the bilinear bound by adding background and applying
congruence. The companion's segment proof then gives weak solution loss
factor `1/(1-error^2)`. That proof also covers attained minimizers under
arbitrary convex constraints and nonnegative convex penalties; its
nonnegative penalty and attainment hypotheses are essential. The software
implements the unconstrained quadratic case only. Neither a ridge optimum
certificate nor arbitrary nonnegative sketch weights imply embedding
quality without checking the corresponding hypothesis.

The augmented effective dimension is the actual trace statistic; the
companion proves its upper bound by the design statistical dimension plus
the rank of the supplied response subspace. Dependent supplied response
coordinates are allowed by the reference and can be removed without
changing that subspace. The implementation does not replace the trace by
the number of response queries or by a full-rank assumption.

## 5. Review and evidence boundary

The inspected mathematical scope is the PSD importance/deletion argument,
the sharper one-failure accounting, the supplied-pool estimator and its
separate domination event, fixed-background concentration and gates,
and the weak convex-regression bilinear lemma with its stated hypotheses.
The executable scope is exact importance/certificates, supplied-pool
accounting, preflight gates, scenario PSD embeddings and the unconstrained
ridge core. The independent checker uses cofactor inverses and a separate
range-coordinate Moore–Penrose construction, not the producer's principal
generalized inverse. It includes a certified bad-pool accounting example
and the exact rank-two obstruction to a stronger random-order coupling.

Random pool generation, importance sampling, deterministic exponential
derandomization, RIP/coherence codes, graded incidence software, Lewis
weights and whole-seminorm backends are outside this implementation and
scoped readiness. Their mathematical theorems remain separately recorded
with their primary dependencies. Finite exact checks are not sampling
success experiments, external peer review or proof-assistant verification.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
