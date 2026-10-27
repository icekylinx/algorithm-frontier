# Verification and scope

[Result statements](../README.md) · [Main proof](../proof.md) · [Source dependencies](../sources.md)

## Reproduce the finite checks

Run from the repository root with Python 3 and its standard library:

```bash
python3 problems/matroid-failure-summaries/verify/check_summaries.py
python3 problems/matroid-failure-summaries/verify/check_weighted_obstruction.py
python3 problems/matroid-failure-summaries/verify/check_weighted_prefix.py
python3 problems/matroid-failure-summaries/verify/check_single_replacement.py
python3 problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py
```

All five scripts reject optimized Python mode. They implement independent
reference enumeration alongside the algorithms under test; they do not
merely check stored output hashes.

| Check | Evidence and finite scope |
|---|---|
| [Rank, one-failure weighted and integral-value summaries](check_summaries.py) | All 92 labeled matroids on at most four elements; 69,516 rank-summary instances, 202,415 failure-rank comparisons and 146,492 necessity witnesses. Also 23,172 one-failure weighted instances with 344,065 prefix comparisons, 27,144 integral-coverage instances with 88,910 value comparisons, and 18 sharp lower examples. |
| [Weighted obstruction](check_weighted_obstruction.py) | All 65 underlying bases and 8,448 basis-exchange conditions; all 386 parallel-extension bases and 405,558 exchange conditions; an independent 8,192-entry rank table; all 11 allowed failure sets; 13 exact optimum and prefix-necessity witnesses; and amplified examples for budgets two through six. |
| [Weighted prefix constructions and refined bounds](check_weighted_prefix.py) | Both the canonical-basis tree and retained-prefix algorithms agree on 86,340 instances over all 92 small matroids, 961,888 original-prefix rank comparisons and 179,293 necessity witnesses. Another 130 cases use 26 orders on the nonrepresentable example. Each algorithm's actual oracle calls are checked against its own bound. |
| [Sharp singleton replacement summaries](check_single_replacement.py) | 19,329 zero/single-extra algorithm instances with 191,962 actual independence calls and 53,100 scans. Includes 15,622 quotient equivalences, 2,259 potential steps, 32 sharp represented examples, and 8,366 graph-process states with 280,866 transitions through six vertices. |

The [rank-loss contraction checker](check_rank_loss_contraction.py) compares
the constructed minor against ranks of original subsets and prefixes.
The default suite enumerates every matroid, one-label partition and order
through three items, then runs 230 larger ordered instances. To include
the completed exhaustive four-item domain:

```bash
python3 problems/matroid-failure-summaries/verify/check_rank_loss_contraction.py --full
```

That full domain contains all 92 matroids through four items and 86,359
ordered/labelled instances, with 375,093 failure queries, 1,495,618 prefix
comparisons, 1,450,577 arbitrary-subset contraction-rank comparisons,
250,091 budget instances and 86,359 binary-large-budget cases. The larger
suite adds 4,680 failures, 42,512 prefixes, 196,560 contraction comparisons
and 1,051 budgets over binary matroids, the nonrepresentable obstruction
with private components, and sharp rank-one-minor families. Larger subset
tests use a fixed seed plus the empty and full surviving sets. The checks
cover loops, unlabelled items, repeated labels, rank drops, joint failed-block
independence, every canonical basis, the entire minimum prefix union,
actual oracle-query counts, and the <code class="math">T=0,1</code> endpoints. Both modes write no
repository files.

The prefix checker also contains independent suites for the new results:

- **Two-failure replacement profiles:** 18,521 degree-one instances,
  including loops, unlabelled basis items and rank drops; 83,618 rank-loss
  inequalities across all failure subsets, including sets larger than two.
- **Circuit extension and minimality:** 1,094 candidate basis families,
  70 valid extensions, 11,434 basis-exchange conditions and 3,784 complete
  rank-table entries. The missing-pair graph and 395 own-color cases are
  checked independently. All 6,656 coarsenings of the example into at most
  three labels or unlabelled items give 28,886 additional failure queries.
- **Integral-submodular basis trees:** 19,867 instances from 24 scaled
  matroid tables and 826 weighted-coverage tables; 231,334 prefix-value
  comparisons and 73,009 failure queries. Every case has a nonzero baseline,
  575 have zero range and 19,116 have a marginal larger than one. The
  115,595 actual value calls include the cached initial baseline.

Exact Bernoulli comparisons use all independently failed labels, even when
their number exceeds the requested failure budget. This matches the size
proof; the randomized measure is never used by either algorithm.

For the larger label-assignment sweep of the first program:

```bash
python3 problems/matroid-failure-summaries/verify/check_summaries.py --full-labels
```

That sweep checks 507,096 rank-summary instances and 1,809,935 failure-rank
comparisons, plus 169,032 one-failure weighted instances and 3,082,765
prefix comparisons. The counts describe these finite domains. They do not
establish universal theorems by exhaustive testing.

## What the written proofs establish

The represented theorem uses all monomials of degree at most <code class="math">h</code> in the
<code class="math">d</code> label-polynomial coefficients, of dimension <code class="math">\binom{h+d}{d}</code>.
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
sharp rank summary. A canonical-basis tree gives the unique smallest
prefix summary in at most `N` times the bounded tree size oracle calls;
the retained-prefix algorithm offers a separate one-pass tradeoff.
The original-basis probability calculation strengthens the general size
factor. Composing prefix compression and reverse deletion gives the sharp
rank bound with linear input dependence for fixed parameters. The
one-failure construction is the depth-one basis tree and has its own sharp
size guarantee.

The explicit counterexample rules out the sharp weighted binomial bound
for arbitrary oracle matroids from two failures onward, even when only
the exact optimum cost is required. It leaves the represented theorem and
the unweighted rank theorem intact. It is a support-size obstruction,
not an oracle-query hardness statement. The two-failure profile and circuit
proof gives the exact rank-four maximum of 13, the sharp three-rank bound
at ranks at most three, and minimum rank/label/ground size for the example.
The finite suites do not enumerate every rank-four matroid; that universal
upper bound is established by the written circuit argument.

When the union of one-failure replacements contains only one item, the
quotient and clique-block potential give the sharp bound <code class="math">r+2t</code> and
the faster profile-sensitive query algorithm. The new checker includes
repeated original-basis labels and failures of contracted items. These
cases exercise the flat-intersection step that a naive contraction would
leave unjustified. With no replacement item, the original basis suffices.

The fixed rank-loss contraction theorem proves that single-label rank
losses and unlabelled basis items can be removed once for all failure
queries. The argument establishes joint independence of failed contracted
blocks over the surviving ground, then derives the exact contraction/deletion
identity. It preserves the canonical basis and every original prefix, not
only the surviving total rank. Its adaptive bounds use one label per item
and one fixed total order. The finite checker supplies independent original
rank comparisons, while the written proof establishes the universal result.

For integral submodular functions, value-spanning sets replace bases in
the same witness search. The parameter <code class="math">R=f(E)-f(\varnothing)</code> is the
numerical range, not its bit length. Coverage examples exercise reverse
deletion, and the weighted-coverage and scaled-matroid suite independently
checks the new ordered value-basis tree and its query count. The general
corollary is proved for every integer-valued monotone submodular function.
The real-valued marginal and entropy inequalities require no integrality
and make no exact cardinality-summary claim.

## Review boundary

The local theorem statements, witness algorithms, one-failure endpoint,
weighted obstruction, ordered-prefix constructions and exact low-rank
two-failure results and fixed rank-loss contraction are ready for review
with their explicit models and evidence. This is a repository review
status; proof-assistant verification and external peer review are not
claimed. The best general weighted-oracle size beyond one failure remains
open outside the exact low-rank cases, between the recorded upper and
lower bounds. No unknown algorithm
is assumed to attain the represented bound in that model.

## Exact rank-two oracle construction and its lower bound

The [rank-two proof](../manuscripts/optimal-rank-two-prefix-oracle-construction.md)
has a separate [finite checker](check_rank_two_prefix.py). Its tested
algorithm sees only independence answers, while the reference answer
enumerates allowed failures and identifies canonical items by ranks of
the original complete prefixes. It verifies the exact union, every
retained item's failure witness, the capped-list query charges, the
sharp support bound, and the hidden-pair plus loop lower-bound families.

```sh
python3 problems/matroid-failure-summaries/verify/check_rank_two_prefix.py
python3 problems/matroid-failure-summaries/verify/check_rank_two_prefix.py --full
```

The completed full run covers 75 small matroids, 66,301 ordered-labelled
instances, 258,186 budget cases, 2,391,458 prefix comparisons and 554,073
retention witnesses. It also covers 250 larger instances, 72 lower-bound
oracle variants with 7,416 answer comparisons, and 102 higher-rank
all-label-budget instances. That last endpoint includes the nonrepresentable
13-item example and 1,192 enumerated failure states.

The exact lower bound applies for <code class="math">N\ge h+3</code> and concerns
computing the canonical union, not returning an arbitrary valid superset.
Query counts and ordinary running time are
separate: the rank-two upper algorithm uses <code class="math">O(N+(h+1)^2)</code> oracle calls
but <code class="math">O(N(h+1)+(h+1)^2)</code> ordinary work after indexing. The full proofs,
rather than the finite enumeration, establish the asymptotic bounds.

## Represented feature-rank construction

The shared [feature-construction checker](../../persistence-failure-certificates/verify/check_feature_construction.py)
compares a breadth-first row-module construction to explicit small tensor
matrices, then checks surviving prefix spans. Its source and proof scope
are recorded in the [persistence verification note](../../persistence-failure-certificates/verify/README.md).
It tests rational and prime-field arithmetic; the general extension-field
construction is proved separately.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
