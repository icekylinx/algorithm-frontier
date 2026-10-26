# Sources and proof dependencies: Finite-group, affine, and metric sparsification

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Weighted Cayley sparsification](manuscripts/arbitrary-group-cayley-sparsification.md) | Arbitrary generator weights, universal actions, and correlated generator failures. |
| [Whole subgroup constraints](manuscripts/optimal-whole-subgroup-constraints.md) | Hereditary Gaussian comparison, symmetrization, and optimal support. |
| [Affine finite-group constraints](manuscripts/affine-constraints-over-arbitrary-finite-groups.md) | Coset compilation, group-derived Mal'tsev constraints, and arbitrary-center group codes. |
| [Transitive Hilbert metrics](manuscripts/transitive-metrics-and-group-alignment.md) | Group alignment, Bernstein transforms, and permutation examples. |
| [Rational quotient ranks](manuscripts/rational-quotient-ranks-from-weak-oracles.md) | Closure-preserving exact rationalization of deterministic approximate rank access. |
| [Affine modular blocks](manuscripts/affine-modular-blocks-and-sharp-modulus-dependence.md) | Optimal support, factorization-free compact construction, and the modulus lower bound. |
| [Few-orbit Hilbert metrics](manuscripts/hilbert-metric-sums-with-few-orbits.md) | Metric completion, original-table implementation, and orbit-dependent lower bounds. |

## Shared proof dependencies

| Result | Role |
|---|---|
| [Adaptive quotient resparsification](../label-block-cut/manuscripts/adaptive-quotient-resparsification.md) | The compact modular and rank-oracle constructions, with summable error and failure budgets. |
| [Direct cut lower bound](../label-block-cut/manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md) | The cut-support obstruction used in the modular valuation-layer lower bound. |
| [Correlated importance pools](../correlated-spectral-regression/manuscripts/correlated-failure-spectral-and-regression-summaries.md) | The correlated generator-failure extension of the ordinary Cayley theorem. |

## External inputs

- Quanrud, *Quotient Sparsification for Submodular Functions*, Theorem 1.1 and the entropy application: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>. The theorem permits real-valued normalized submodular ranks with positive marginals at least one.
- Reis and Rothvoss, *Linear-size l1 Sparsifiers*, Theorem 7: <https://arxiv.org/html/2606.28147v2>. The partial coloring lies in a constant dilation of the error body; that dilation is charged in the proof.
- Slepian, *The One-Sided Barrier Problem for Gaussian Noise*: <https://doi.org/10.1002/j.1538-7305.1962.tb02419.x>. The comparison is used at zero after equal-variance normalization.
- Royen, Gaussian correlation inequality: <https://arxiv.org/abs/1408.1028>. Prékopa log-concavity and matrix concentration are identified where used.
- Basu et al., *Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms*, Theorem 1.2: <https://arxiv.org/pdf/2609.20238>. This supplies only the unrestricted metric comparison branch; the symmetry proof is internal.
- Integer normal forms are the Kannan–Bachem polynomial-bit input: <https://doi.org/10.1137/0208040>. Full comparator citations are retained in each manuscript.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
