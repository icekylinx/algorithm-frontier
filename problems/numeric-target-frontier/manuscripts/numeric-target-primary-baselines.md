# Primary-source comparisons for the numeric-target increments

**25 October 2026. Increment relative to checkpoint Q.**
The companion algorithms and lower bounds have self-contained proofs.
This note identifies public antecedents and limits comparison claims.

## Exact vector-weight bases

Eisenbrand, Rohwedder and Wegrzycki, *Sensitivity, Proximity and FPT
Algorithms for Exact Matroid Problems*, FOCS 2024 /
[arXiv:2404.03747v2](https://arxiv.org/html/2404.03747v2), Theorem 3,
gives an FPT algorithm parameterized by coefficient magnitude and
dimension. Its introduction credits count-vector enumeration followed
by partition-matroid intersection.

The bounds proved here use nonnegative coefficients and the numeric
targets as parameters, while retaining scalar optimization and binary
polymatroids. Small coefficient magnitude can be useful even when
targets are large. No universal dominance or first count-profile
claim is made.

## Rank-parameterized matroid intersection

Doron-Arad, Kulik and Shachnai, *You (Almost) Can't Beat Brute Force
for 3-Matroid Intersection*,
[arXiv:2412.02217v2](https://arxiv.org/html/2412.02217v2), Theorem 1.3,
proves a k log k rank-exponent lower bound for general oracle
multi-matroid intersection. It also records the Huang--Ward rank-FPT
algorithm with a quadratic rank exponent.

Thus neither general rank-FPT existence nor a k log k oracle
obstruction is newly claimed here. VT directly treats one resource
rank, mixed numeric rows, total target T and rank-query access.

## Recent structured-intersection kernels

Huang, Kakimura, Kobayashi and Terao, *Polynomial Kernels with
Reachability for Weighted d-Matroid Intersection*,
[arXiv:2603.17345v1](https://arxiv.org/html/2603.17345v1), 18 March 2026,
Theorems 1--5, gives randomized polynomial-size reachable kernels
when one matroid is arbitrary and the others have specified
structured representations.

For a fixed number of partition constraints, enumerating rank-k
subsets of that kernel already gives k^{O(k)} time. This special
case is not a new rank-FPT breakthrough of the present checkpoint.
The present deterministic proofs establish their stated mixed
numeric-target, exact scalar, binary polymatroid and polynomial-space
interfaces.

## Recent group-label optimization

Liu, Oki and Xu, *Proximity Theorem and FPT Algorithm for Minimum
Group-labeled Matroid Bases*, posted 23 October 2026,
[primary article](https://optimization-online.org/2026/10/proximity-theorem-and-fpt-algorithm-for-minimum-group-labeled-matroid-bases/)
and [manuscript](https://optimization-online.org/wp-content/uploads/2026/10/Weighted_proximity.pdf),
studies a finite set of forbidden group labels. Its weighted time
bound is exponential in the square of that set's size.
This is a different parameterization; no first weighted exact-label
algorithm is claimed here.

## Nonlinear antecedents

Shioura, *Polynomial-Time Approximation Schemes for Maximizing Gross
Substitutes Utility Under Budget Constraints*, MOR 40(1), 192--225
(2015), [publisher](https://pubsonline.informs.org/doi/abs/10.1287/moor.2014.0668),
establishes PTAS results for broader discrete concave utility classes.
The nonlinear increments here use explicit marginal bands and
compatible curvature directions. They do not claim the first
nonlinear budgeted approximation scheme.

## Public OpenAI index check

The [public OpenAI mathematics index](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)
was reopened on 25 October 2026. Exact searches for "exact weight",
"linear constraint" and "numeric target" found no matching index
text. The visible common-polymatroid base entry describes randomized
approximate counting.

This is a literal check of one visible index, not evidence about
differently named or unpublished work. The indexed counting
manuscript is not used as a proof of an optimization theorem here.

## Reporting scope

The supported claims are the fully specified algorithms, their
precise input models and the independently derived lower
constructions. Numeric exponent orders are tight in the stated
oracle models. Publication priority, fastest-ever complexity across
all representations and an optimal inverse-accuracy exponent are
not established by this source check.
