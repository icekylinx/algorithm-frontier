# Sources and proof dependencies: Exact-label quotient and whole-block summaries

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Adaptive quotient resparsification](manuscripts/adaptive-quotient-resparsification.md) | Repeated restriction removes the ambient item-count logarithm, with explicit error, probability, and rational bit accounting. |
| [Exact-label cuts and matroid quotients](manuscripts/exact-label-cut-and-matroid-quotient-sparsification.md) | The column decoder, graph-cut specialization, and direct cut lower bound. |
| [Exact-label whole blocks](manuscripts/exact-label-whole-blocks-and-hyperedges.md) | Common-scalar block decoding, atomic hyperedges, hedge partitions, and globally commuting stabilizer blocks. |

## Shared proof dependencies

| Result | Role |
|---|---|
| [Rational quotient ranks](../group-metric-constraints/manuscripts/rational-quotient-ranks-from-weak-oracles.md) | Used when the adaptive backend is instantiated with logarithmic subgroup ranks; explicit linear-rank applications use exact field rank directly. |

## External inputs

- Quanrud, *Quotient Sparsification for Submodular Functions*, Theorem 1.1 and restriction Lemma 2.1: <https://kentq.s3.amazonaws.com/submodular-sparsification.pdf>. Adaptive calls are an internal consequence with an explicit error and probability proof.
- Chandrasekaran, Chekuri, Wang, and Zhu, *Hedgegraph Polymatroids*, Theorem 7: <https://arxiv.org/html/2510.25043v1>. Ordinary hedge partition sparsification is an antecedent.
- The support lower bounds are proved from cut inequalities and the classical L1 Khintchine inequality; no spectral lower bound is substituted for a cut lower bound.
- The prime-dimensional commuting-block representation uses standard Weyl/stabilizer algebra: <https://arxiv.org/abs/quant-ph/0408190>.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
