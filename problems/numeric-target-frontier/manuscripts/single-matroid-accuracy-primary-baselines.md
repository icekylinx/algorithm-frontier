# Primary baselines for the single-matroid accuracy increment

**25 October 2026. New comparisons relative to checkpoint Q.**

This note supports the accuracy-exponent comparison for the seven
single-matroid linear-constraint variants. It is a bounded primary-source
audit. It does not establish publication priority or that every earlier
algorithm has been exhausted.

## 1. The directly compared unified bound

Ilan Doron-Arad, Hadas Shachnai and Gilad Shmerler,
[*Tight Approximation Results for Matroid Optimization with a Linear Constraint*, APPROX/RANDOM 2026, Article 18](https://drops.dagstuhl.de/storage/00lipics/lipics-vol392-approx-random2026/LIPIcs.APPROX-RANDOM.2026.18/LIPIcs.APPROX-RANDOM.2026.18.pdf).

The abstract and theorem framework give a unified EPTAS for the seven
nontrivial choices of objective direction, independent set versus basis,
and upper versus lower side constraint. The displayed dependence is
(1/epsilon^2)^{O(1/epsilon)} times a polynomial in the instance. Feasible
outputs retain the side constraint; the approximation is on the objective.
The bin-count enumeration in Section 2.1, Lemma 3 is the direct
counting comparison point.

The new SV theorem proves the same seven orientation choices by its own
integral recovery and obtains 2^{O(1/epsilon)} times polynomial work.
It also supports integral polymatroid counts in binary. The comparison
is a reduction of the identified displayed exponent from
O(epsilon^-1 log(1/epsilon)) to O(epsilon^-1). It is not a claim that
EPTAS existence or the seven-case formulation is new. The refined
constant manuscript further specifies the new upper bound.

## 2. Earlier EPTAS existence is explicitly credited

Refael Hassin and Asaf Levin,
[*An Efficient Polynomial Time Approximation Scheme for the Constrained Minimum Spanning Tree Problem Using Matroid Intersection*, SIAM Journal on Computing 33(2), 261--268 (2004)](https://epubs.siam.org/doi/abs/10.1137/S0097539703426775).
The primary abstract gives an exact-bound constrained spanning-tree
scheme with time (1/epsilon)^{O(1/epsilon)} n^4. Thus a constrained
tree EPTAS is longstanding public background. The new theorem does
not claim a better polynomial dependence on graph size or a first
scheme for that special case.

Ilan Doron-Arad, Ariel Kulik and Hadas Shachnai,
[*An EPTAS for Budgeted Matroid Independent Set*](https://arxiv.org/abs/2209.04654),
2022 preprint / SOSA 2023.
This is an earlier EPTAS for the maximum independent-set, upper-budget
member, based on a representative-set approach. Its existence is
credited independently of the newer unified comparison. No numerical
running-time formula is inferred here from an abstract that does not
display one.

## 3. The quantitative lower bound is a separate refinement

Ilan Doron-Arad, Ariel Kulik and Hadas Shachnai,
[*Lower Bounds for Matroid Optimization Problems with a Linear Constraint*, ICALP 2024](https://drops.dagstuhl.de/storage/00lipics/lipics-vol297-icalp2024/LIPIcs.ICALP.2024.56/LIPIcs.ICALP.2024.56.pdf),
[primary full version](https://arxiv.org/html/2307.07773v2).

The public theorem rules out randomized FPTASs for the seven nontrivial
oracle variants. Its equal-sum hidden-matroid construction is an
antecedent to the new quantitative analysis. Section 5 of the full
version also announces a modified inverse-error quarter-power
exponential lower bound, Omega(2^(epsilon^-1/4)), with details deferred.
This public quantitative observation is credited separately from
the equation-(5) reduction's literal error choice. The new lower-bound
manuscript separately changes the objective tie-breaks and tracks a
unit objective gap at an optimum of quadratic size. It proves
2^{Omega(epsilon^-1/2)} rank queries, including constant-success
randomization. That sharper displayed accuracy dependence is an
internal derivation, not attributed to the paper as its theorem.

A journal version, *Lower Bounds for Weighted Matroid Problems*,
appeared in ACM Transactions on Algorithms 22(2), Article 20 (2026),
DOI <https://doi.org/10.1145/3774814>. The publication metadata and
primary indexed statement were located. Direct access to its complete
publisher text was blocked during this check, so no additional
journal-only quantitative theorem is asserted here. The fully read
comparison above is explicitly to the public 2024 full version.

The resulting upper/lower comparison is therefore

    upper:  2^{O(epsilon^-1)} poly(H_epsilon),
    lower:  2^{Omega(epsilon^-1/2)} rank queries.

The gap is real. Neither the no-FPTAS theorem nor the new quantitative
argument proves an inverse-error linear lower exponent. These oracle
bounds do not automatically apply to explicitly represented graphic
or linear matroids.

## 4. Public OpenAI index check for this particular new target

The [public OpenAI math index](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)
was checked on 25 October 2026. Exact searches for "knapsack",
"linear constraint" and "budgeted matroid" returned no indexed text
matches. The earlier visible common-polymatroid-base entry concerns
randomized approximate counting rather than the optimization
guarantees proved here.

This establishes only the scope of that visible index check. It is
not evidence that no differently named or unpublished result exists,
and no indexed proof is treated as independently verified. The new
algorithm and lower bound do not depend on an OpenAI counting claim.

## 5. Reporting the improvement accurately

The concrete statement supported by this increment is that the
fully specified algorithms attain the new displayed accuracy bounds
for all seven exact-side-constraint variants, with polynomial binary
workspace and an integer comparator. Their proof covers a more general
integral-polymatroid representation as well.

The current primary comparison identifies a logarithmic factor removed
from an established published upper exponent. A claim of fastest-ever
complexity, first EPTAS, tight accuracy dependence, or polynomial
dependence on 1/epsilon would go beyond the evidence and is not made.
