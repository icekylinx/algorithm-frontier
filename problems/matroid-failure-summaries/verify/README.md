# Verification and scope

[Result statements](../README.md) · [Main proof](../proof.md) · [Source dependencies](../sources.md)

## Reproduce the finite checks

Run from the repository root with Python 3 and its standard library:

```bash
python3 problems/matroid-failure-summaries/verify/check_summaries.py
python3 problems/matroid-failure-summaries/verify/check_weighted_obstruction.py
python3 problems/matroid-failure-summaries/verify/check_weighted_prefix.py
```

All three scripts reject optimized Python mode. They implement independent
reference enumeration alongside the algorithms under test; they do not
merely check stored output hashes.

| Check | Evidence and finite scope |
|---|---|
| [Rank, one-failure weighted and integral-value summaries](check_summaries.py) | All 92 labeled matroids on at most four elements; 69,516 rank-summary instances, 202,415 failure-rank comparisons and 146,492 necessity witnesses. Also 23,172 one-failure weighted instances with 344,065 prefix comparisons, 27,144 integral-coverage instances with 88,910 value comparisons, and 18 sharp lower examples. |
| [Weighted obstruction](check_weighted_obstruction.py) | All 65 underlying bases and 8,448 basis-exchange conditions; all 386 parallel-extension bases and 405,558 exchange conditions; an independent 8,192-entry rank table; all 11 allowed failure sets; 13 exact optimum and prefix-necessity witnesses; and amplified examples for budgets two through six. |
| [Weighted prefix construction](check_weighted_prefix.py) | 86,340 instances over all 92 small matroids, 961,888 original-prefix rank comparisons and 179,293 necessity witnesses; explicit query-count bounds. A further 130 instances use 26 orders on the nonrepresentable 13-item example. Exact Bernoulli checks include failures larger than the requested budget, as required by the size proof. |

For the larger label-assignment sweep of the first program:

```bash
python3 problems/matroid-failure-summaries/verify/check_summaries.py --full-labels
```

That sweep checks 507,096 rank-summary instances and 1,809,935 failure-rank
comparisons, plus 169,032 one-failure weighted instances and 3,082,765
prefix comparisons. The counts describe these finite domains. They do not
establish universal theorems by exhaustive testing.

## What the written proofs establish

The represented theorem uses all monomials of degree at most $h$ in the
$d$ label-polynomial coefficients, of dimension $\binom{h+d}{d}$.
A query functional annihilates exactly the failed items. Applying it to
the greedy relation with earlier retained columns proves every surviving
prefix span, including ties, signed costs and rank drops. The dimension
gate runs before feature enumeration; the field extension and rational
bit accounting are part of the construction. The finite programs above
do not implement that complete algebraic lift or certify its universal
arithmetic complexity.

For arbitrary matroids, the sharp rank bound uses a coloop witness in the
entire surviving restriction. A cheaper-prefix witness is a different
condition. The bounded-depth search explicitly decides both conditions
when supplied the appropriate current ground. Reverse deletion gives the
sharp rank summary; a forward ordered scan gives the unique smallest
prefix summary, whose general bound is the larger W–LF factor. Composing
the two gives the sharp rank bound with linear input dependence for fixed
rank, failure budget and label degree. The one-failure construction has
its own sharper uniform polynomial bound.

The explicit counterexample rules out the sharp weighted binomial bound
for arbitrary oracle matroids from two failures onward, even when only
the exact optimum cost is required. It leaves the represented theorem and
the unweighted rank theorem intact. It is a support-size obstruction,
not an oracle-query hardness statement.

For integral submodular functions, value-spanning sets replace bases in
the same witness search. The parameter $R=f(E)-f(\varnothing)$ is the
numerical range, not its bit length. Coverage examples exercise the
reverse-deletion construction; the general ordered-value corollary is
proved in the manuscript and is outside the executable checker scope.
The real-valued marginal and entropy inequalities require no integrality
and make no exact cardinality-summary claim.

## Review boundary

The local theorem statements, witness algorithms, one-failure endpoint,
weighted obstruction and ordered-prefix construction are ready for review
with their explicit models and evidence. This is a repository review
status; proof-assistant verification and external peer review are not
claimed. The best general weighted-oracle size beyond one failure remains
open between the recorded upper and lower bounds. No unknown algorithm
is assumed to attain the represented bound in that model.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
