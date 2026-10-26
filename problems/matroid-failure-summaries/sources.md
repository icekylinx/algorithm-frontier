# Sources and proof dependencies: Matroid and submodular failure summaries

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Represented fixed-cost summaries](manuscripts/sharp-represented-matroid-failure-summaries.md) | The polynomial label lift, canonical prefix spans, field extensions, mergeability, and extension contexts. |
| [Oracle rank and submodular summaries](manuscripts/arbitrary-matroid-and-submodular-failure-summaries.md) | The coloop-witness bound, separating pools, fixed-parameter rank construction, integral-submodular summaries, and real/entropy inequalities. |

## External inputs

- The arbitrary-matroid proof uses the classical Bollobás set-pairs permutation method. [Variations on the Bollobás Set-Pair Theorem](https://arxiv.org/html/2307.14704v1) records the distinction between its strong and skew forms.
- [Efficient Computation of Representative Families with Applications in Parameterized and Exact Algorithms](https://sites.cs.ucsb.edu/~daniello/papers/efficientRepSetJ.pdf) and [Representative Families for Matroid Intersections](https://arxiv.org/html/1806.11527v4) supply the representative-family background.
- [Fault-Tolerant Matroid Bases](https://drops.dagstuhl.de/storage/00lipics/lipics-vol351-esa2025/html/LIPIcs.ESA.2025.83/LIPIcs.ESA.2025.83.html) is a comparison for minimum-cardinality full-rank protection under individual failures. The local theorem instead allows correlated label failures and rank drops; its final oracle deletion theorem is rank-only.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
