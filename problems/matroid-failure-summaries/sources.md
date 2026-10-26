# Sources and proof dependencies: Matroid and submodular failure summaries

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

## Complete local proof chain

| Result | Canonical argument | Required input |
|---|---|---|
| Sharp represented fixed-cost summary | [Polynomial label lift, prefix spans and field construction](manuscripts/sharp-represented-matroid-failure-summaries.md) | Rational or explicit finite-field columns, fixed additive costs and explicit label lists. |
| Sharp arbitrary-matroid rank summary | [Circuit-blocking inequality and complete witness branching](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md) | An independence oracle; rank, failure budget and label degree are parameters. |
| Sharp one-failure weighted oracle summary | [Union of the canonical basis and its relevant single-label replacements](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md#7-weighted-oracle-summaries-for-one-label-failure) | An independence oracle and one fixed item order; uniform polynomial preprocessing. |
| Arbitrary-budget weighted oracle summary | [Canonical-prefix necessity, the W–LF size proof and retained-prefix FPT construction](manuscripts/weighted-oracle-prefix-fpt-construction.md) | An independence oracle and fixed order; the nonsharp W–LF factor is an existing project baseline. |
| Weighted sharp-bound obstruction | [The 13-item construction, exact failure table and amplification](manuscripts/weighted-oracle-two-failure-obstruction.md) | An explicitly defined rank-four nonrepresentable matroid; no external algorithm. |
| Integral values, real marginals and entropy | [Diminishing returns and the circuit-blocking permutation argument](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md#9-monotone-submodular-functions) | A monotone submodular value oracle for constructions; finite joint entropy for the entropy inequality. |

The sharp rank and integral-value constructions no longer depend on a
separating-family generator or repeated-halving implementation. Their
bounded-depth search is specified and proved locally. The ordered-prefix
construction followed by reverse deletion also gives linear input
dependence for fixed parameters; see [main proof, Section 4.2](proof.md#42-linear-input-dependence-for-the-sharp-rank-construction).

Random permutations and independent label failures are used only to bound
the sizes of deterministic outputs. None of these constructions samples
queries or has a probability of error. Oracle-query bounds do not supply
a bit encoding or implementation of an arbitrary input oracle.

## Background and comparison sources

- [Variations on the Bollobás Set-Pair Theorem](https://arxiv.org/html/2307.14704v1) gives the classical set-pairs context and distinguishes strong from skew cross-intersection. The circuit-blocking and submodular inequalities used here have complete local proofs; they do not invoke an unsupported matroid version of the skew theorem.
- [Efficient Computation of Representative Families with Applications in Parameterized and Exact Algorithms](https://sites.cs.ucsb.edu/~daniello/papers/efficientRepSetJ.pdf), by Fomin, Lokshtanov, Panolan and Saurabh, and [Representative Families for Matroid Intersections](https://arxiv.org/html/1806.11527v4), by van Bevern, Tsidulko and Zschoche, provide the algebraic representative-family background. They are attribution and comparison sources, not missing implementations needed by the explicit lift.
- [Fault-Tolerant Matroid Bases](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.83) studies minimum-cardinality full-rank protection under individual failures. Here the allowed queries delete correlated label classes and may decrease the surviving rank; the local size theorem does not optimize the restriction size on each individual instance.
- [Equivariant Kazhdan–Lusztig theory of paving matroids](https://pages.uoregon.edu/njp/eq-relax.pdf), by Karn, Nasr, Proudfoot and Vecchi, Section 5, records the classical Vámos matroid used as the underlying obstruction. The local manuscript proves the needed basis exchange and nonrepresentability facts and supplies its own ordered colored parallel extension and necessity witnesses.

The W–LF factor and its direct XP construction were already recorded in
the project's canonical comparison sections. The new weighted manuscript
reproves the factor and supplies the FPT implementation; it makes no
priority claim for the factor or its probabilistic proof. The exact best
universal weighted-oracle size for two or more failures is not determined
by the displayed upper and lower bounds.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
