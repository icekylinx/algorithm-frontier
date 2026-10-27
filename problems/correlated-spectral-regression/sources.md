# Sources and proof dependencies: Correlated spectral and regression summaries

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Importance pools and spectral summaries](manuscripts/correlated-failure-spectral-and-regression-summaries.md) | Robust scores, PSD sampling, Lewis-weight summaries, fixed background, and the separate one-label deterministic construction. |
| [Nonnegative sensitivity compiler](manuscripts/general-nonnegative-sensitivity-compiler.md) | The common pool estimator for nonnegative loss families and its all-scenario total-mass bound. |
| [Weak convex regression](manuscripts/weak-convex-regression-under-correlated-failures.md) | The bilinear-error argument, effective dimension, fixed response subspaces, and nonnegative convex penalties. |
| [Label-vector PSD and norm lifts](manuscripts/label-vector-spectral-and-norm-lifts.md) | Common-weight decoding, RIP and deterministic code choices, and the distinction between arithmetic and polynomial-bit sparsification. |
| [Graph incidence lifts](manuscripts/correlated-vertex-and-edge-failure-spectral-graphs.md) | Vertex/edge label geometry, graded exterior features, and graph lower bounds. |
| [Graded and simplicial incidence lifts](manuscripts/graded-incidence-and-simplicial-spectral-sparsification.md) | Rank-sensitive incidence decoding, repeated labels, rational implementation, and simplicial applications. |
| [Whole seminorm summaries](manuscripts/arbitrary-seminorms-under-correlated-failures.md) | The common projector theorem; separate optimal-support existence and constructive lifted-oracle interfaces. |
| [Rational importance and ridge realization](manuscripts/reference-rational-importance-regression.md) | Exact generalized-inverse trace certificates, one-failure and supplied-pool accounting, preflight gates, scenario PSD embeddings, and the unconstrained supplied-response ridge core with explicit software boundary. |

## External inputs

The companion manuscripts state the exact theorem, input representation, accuracy, and probability interface used from each ordinary backend. Principal inputs are:

- de Carli Silva, Harvey, and Sato, [Sparse Sums of Positive Semidefinite Matrices](https://www.math.uwaterloo.ca/~harvey/Publications/SparsifierMMWUM/SparsifierMMWUM.pdf), Theorem 3, for arbitrary-rank PSD sparsification.
- Baraniuk, Davenport, DeVore, and Wakin, [A Simple Proof of the Restricted Isometry Property for Random Matrices](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/2/436/files/2011/04/baraniuk08si.pdf), for the random code event.
- Cohen and Peng, [Row Sampling by Lewis Weights](https://arxiv.org/pdf/1412.0588), together with the corrected Appendix A of Woodruff and Yasuda, [Online Lewis Weight Sampling](https://arxiv.org/pdf/2207.08268), for ordinary norm sampling.
- Wigderson and Xiao, [Derandomizing the Ahlswede–Winter Matrix-Valued Chernoff Bound](https://theoryofcomputing.org/articles/v004a003/v004a003.pdf), for the stated deterministic finite-scenario alternatives.
- Basu et al., [Optimal Sparsifiers for Minkowski Sums and Sums of Seminorms](https://arxiv.org/pdf/2609.20238), for the optimal ordinary seminorm existence theorem. The constructive branch separately requires the lifted sum evaluation and roundedness access stated in its manuscript.
- Feldman and Langberg, [A Unified Framework for Approximating and Clustering Data](https://arxiv.org/abs/1106.1379), and In, Li, Woodruff, and Wu, [Robust Sparsification via Sensitivity](https://proceedings.mlr.press/v267/in25a.html), for the sensitivity framework and the ordinary separation-pool antecedent.
- Tropp, [User-friendly tail bounds for sums of random matrices](https://arxiv.org/pdf/1004.4389), arXiv version seven, Theorem 6.1, for the centered matrix-Bernstein inequality used to quantify the reference planner's conservative count envelope.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
