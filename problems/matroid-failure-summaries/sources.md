# Sources and proof dependencies: Matroid and submodular failure summaries

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

## Complete local proof chain

| Result | Canonical argument | Required input |
|---|---|---|
| Sharp represented fixed-cost summary | [Polynomial label lift, prefix spans and field construction](manuscripts/sharp-represented-matroid-failure-summaries.md) | Rational or explicit finite-field columns, fixed additive costs and explicit label lists. |
| Sharp arbitrary-matroid rank summary | [Circuit-blocking inequality and complete witness branching](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md) | An independence oracle; rank, failure budget and label degree are parameters. |
| Sharp one-failure weighted oracle summary | [Union of the canonical basis and its relevant single-label replacements](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md#7-weighted-oracle-summaries-for-one-label-failure) | An independence oracle and one fixed item order; uniform polynomial preprocessing. |
| Arbitrary-budget weighted oracle summary | [Canonical-basis tree, original-basis size refinement and one-pass alternative](manuscripts/weighted-oracle-prefix-fpt-construction.md) | An independence oracle, fixed order and explicit labels; no external summary implementation. |
| Exact two-failure rank-four maximum and minimality | [Replacement profiles, the circuit missing-pair graph and few-label bound](manuscripts/two-failure-oracle-prefix-bounds.md) | An arbitrary independence oracle; two failures and at most one label per item. All arguments follow from the matroid axioms. |
| Fixed rank-loss contraction and rank-adaptive prefix summaries | [Private rank directions, joint failed-block independence and the exact canonical-basis decomposition](manuscripts/rank-loss-contraction-for-prefix-summaries.md) | An independence oracle, one fixed order, and at most one label per item; no representation or additional external theorem. |
| Weighted sharp-bound obstruction | [The 13-item construction, exact failure table and amplification](manuscripts/weighted-oracle-two-failure-obstruction.md) | An explicitly defined rank-four nonrepresentable matroid; no external algorithm. |
| Integral values, real marginals and entropy | [Diminishing returns and the circuit-blocking permutation argument](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md#9-monotone-submodular-functions) | A monotone submodular value oracle for constructions; finite joint entropy for the entropy inequality. |

The sharp rank and integral-value constructions no longer depend on a
separating-family generator or repeated-halving implementation. Their
bounded-depth search is specified and proved locally. The canonical-basis
tree followed by reverse deletion also gives linear input
dependence for fixed parameters; see [main proof, Section 4.2](proof.md#42-linear-input-dependence-for-the-sharp-rank-construction).

Random permutations and independent label failures are used only to bound
the sizes of deterministic outputs. None of these constructions samples
queries or has a probability of error. Oracle-query bounds do not supply
a bit encoding or implementation of an arbitrary input oracle.

The fixed-contraction theorem removes the directions accounted for by
single-label rank losses and unlabelled original-basis items. Its effective
rank is the total number of single-failure replacement appearances. The
proof uses only the matroid rank axioms and greedy order, then invokes the
locally proved prefix bounds on that lower-rank minor. It does not extend
the contraction statement to overlapping label lists or to one set that
works for all cost orders.

## Background and comparison sources

- [Variations on the Bollobás Set-Pair Theorem](https://arxiv.org/html/2307.14704v1) gives the classical set-pairs context and distinguishes strong from skew cross-intersection. The circuit-blocking and submodular inequalities used here have complete local proofs; they do not invoke an unsupported matroid version of the skew theorem.
- [Efficient Computation of Representative Families with Applications in Parameterized and Exact Algorithms](https://sites.cs.ucsb.edu/~daniello/papers/efficientRepSetJ.pdf), by Fomin, Lokshtanov, Panolan and Saurabh, and [Representative Families for Matroid Intersections](https://arxiv.org/html/1806.11527v4), by van Bevern, Tsidulko and Zschoche, provide the algebraic representative-family background. They are attribution and comparison sources, not missing implementations needed by the explicit lift.
- [Fault-Tolerant Matroid Bases](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.83) studies minimum-cardinality full-rank protection under individual failures. Here the allowed queries delete correlated label classes and may decrease the surviving rank; the local size theorem does not optimize the restriction size on each individual instance.
- [Equivariant Kazhdan–Lusztig theory of paving matroids](https://pages.uoregon.edu/njp/eq-relax.pdf), by Karn, Nasr, Proudfoot and Vecchi, Section 5, records the classical Vámos matroid used as the underlying obstruction. The local manuscript proves the needed basis exchange and nonrepresentability facts and supplies its own ordered colored parallel extension and necessity witnesses.

The original Bernoulli prefix factor and its direct XP construction were
already recorded in the project's canonical comparison sections. The
weighted manuscript supplies the faster canonical-basis tree and proves
the stronger original-basis bound, with a complete local derivation of
every size inequality. No priority claim is made for the earlier factor
or its probabilistic proof.

For two failures and one label per item, the low-rank bounds are now
exact: three times the rank through rank three, and 13 items at rank
four. The 13-item obstruction is minimal in rank, number of labels and
ground size for exceeding three times the rank. Outside those cases the
best universal weighted-oracle size remains open between the recorded
upper and lower bounds; the constructions do not assume an algorithm
attaining the represented binomial bound.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
