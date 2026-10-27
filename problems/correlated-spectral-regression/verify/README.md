# Verification and scope

[Main proof](../proof.md) · [Source dependencies](../sources.md)

## Evidence status

The family rests on the written probability, positive-operator, and optimization arguments and on the ordinary sparsification theorems named in the sources.
The [rational reference](../reference/README.md) now supplies exact importance
and supplied-pool accounting certificates, scenario PSD embedding checks,
preflight gates and the unconstrained supplied-response ridge core. It does
not sample a summary or certify a random all-failure event. A finite numerical
code experiment does not verify every RIP subset, failure query, or regression
objective.

Run the independent exact checker:

```sh
python3 problems/correlated-spectral-regression/verify/check_importance_regression.py
```

The comparator computes range-coordinate Moore–Penrose inverses by independent
cofactor determinants. The producer instead uses a principal-minor generalized
inverse whose trace values have a separate exact certificate. Ridge optima
are compared using the independent inverse and original quadratic objective.

| Finite mechanism or outcome | Count |
|---|---:|
| Rational arbitrary-rank PSD instances | 24 |
| Independent subset mass certificates | 384 |
| Exact deletion-monotonicity comparisons | 2,592 |
| Exact single-failure item maxima | 96 |
| Supplied pool outcomes with deterministic accounting | 216 |
| Protected-pair domination implications | 1,536 |
| Certified bad-pool accounting without domination | 1 |
| Exact rank-two coupling-obstruction marginals | 4 |
| Supplied-response regression instances | 12 |
| Augmented effective-dimension bounds | 12 |
| Exact scenario all-vector embedding checks | 84 |
| Independent ridge/weak-solution comparisons | 504 |
| Degenerate regression queries | 5 |
| Planner modes exercised | 4 |
| Producer-disabled certificate verifiers | 4 |
| Forged certificate rejections | 8 |
| Malformed input rejections | 13 |

Fixtures include singular backgrounds, changing ranks, zero PSD items,
overlapping and empty labels, rational costs, singular/zero-variable designs,
zero response spaces, multiple response columns, huge encoded failure budgets,
and background values with hundreds of bits. The full-input planner returns
before positive pool work when the formal multiplier is enormous. Verified
PSD inequalities quantify over all vectors for the **specified** scenario;
they are not finite direction tests. The supplied-pool checker separately
tests an accounting-valid pool list whose scores fail domination, keeping the
probabilistic coverage condition visible.

The [realization note](../manuscripts/reference-rational-importance-regression.md)
states the inspected mathematical composition and the precise executable scope.

## Probability and construction interfaces

The pool estimator has a deterministic total-mass bound even on a bad pool outcome. Simultaneous domination is a separate high-probability event; the second sampling stage is independent and is analyzed conditional on that event. The factor <code class="math">\log Q</code>, for the number of allowed failure scenarios, remains explicit. With one failed label, exact all-scenario scores support the separately stated deterministic finite-scenario construction.

The code route uses one successful RIP event and one PSD inequality to cover every later failure query. The random code is Monte Carlo; the algorithm does not efficiently certify the full RIP event. The optimal-support arithmetic PSD theorem and the explicit polynomial-bit construction with logarithmic overhead remain different guarantees.

Whole-seminorm construction requires evaluation and roundedness access for the lifted sum. Access only to the original sum does not automatically provide those interfaces. The optimal ordinary seminorm existence theorem is distinct from this constructive model.

## Positive decoding and incidence

Congruence followed by partial trace preserves PSD order. The decoded item scalar is zero on failed items and lies in the common interval <code class="math">[1-\kappa,1]</code> on survivors. The scalar sandwich uses nonnegative output weights, and those weights are fixed before every query.

Graph and simplicial incidence lifts use graded exterior deficits, including degree zero when labels repeat. Rank compression selects original rows. Reconstruction of the full matrix continues to hold after deletions that lower rank; it does not assume a separately chosen full-rank surviving matrix.

## Weak regression

The weak regression conclusion assumes an attained sketched minimizer, convex feasibility, and a nonnegative convex penalty. The response subspace and base regularization are supplied before preprocessing; later choices are restricted to the stated response and regularization family.

The bilinear argument converts embedding error <code class="math">\eta</code> into relative solution error <code class="math">\eta^2/(1-\eta^2)</code>. This is a mathematical optimization statement under the listed hypotheses, not a claim that the repository implements a solver for every permitted convex objective.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
