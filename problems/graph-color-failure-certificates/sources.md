# Sources and proof dependencies: Exact colored-graph certificates

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Colored graph and vertex-failure certificates](manuscripts/colored-graph-and-vertex-failure-certificates.md) | Activation matrices, the sharp vertex-color envelope, mixed/list labels, canonical MSFs, and the one-color output-sensitive construction. |
| [Mixed/list feature and exchange realization](manuscripts/reference-mixed-list-realization.md) | Actual feature-span compression, cubic rank saving, original-prefix queries, completed-batch single-failure differences, lower examples, exact reference costs and primary dynamic interface. |

The [rational vertex-color realization](manuscripts/reference-vertex-color-realization.md) connects the componentwise activation proof to the shipped [reference backend](reference/README.md). It includes the exact prefix/Kruskal argument and polynomial rational arithmetic. The mixed/list theorems and the symmetric-cubic rank saving remain proved in the canonical manuscript. The near-linear one-color bound explicitly requires an exchange-reporting dynamic-MSF interface; the reference implementation uses static elimination instead.

The [mixed/list backend](reference/list_colors.py) separately reuses the
canonical evaluation-module primitive from the
[persistence feature module](../persistence-failure-certificates/reference/feature_summary.py).
It computes actual spans on vertex or endpoint/edge positions without
formal monomial enumeration. Its exact exchange wrapper and
[independent checker](verify/check_list_colors.py) retain their own cost
ledgers. No polylogarithmic dynamic-MSF implementation is shipped.

## Shared proof dependencies

| Result | Role |
|---|---|
| [Represented-matroid failure features](../matroid-failure-summaries/manuscripts/sharp-represented-matroid-failure-summaries.md) | The edge-color specialization and polynomial failure-annihilating features. |
| [Exact incidence summaries](../persistence-failure-certificates/manuscripts/correlated-fault-boundary-and-persistence-sparsifiers.md) | The incidence-lift framework and the simple-graph lower-bound antecedent. |

## External inputs

- Sorkin, Steger, and Zenklusen, [A Tight Bound on the Collection of Edges in MSTs of Induced Subgraphs](https://arxiv.org/pdf/0705.2439), for the induced-subgraph comparator and sharpness construction.
- Holm, de Lichtenberg, and Thorup, [Poly-logarithmic Deterministic Fully-Dynamic Algorithms](https://u.cs.biu.ac.il/~liamr/p723-holm.pdf), JACM 2001, Theorem 8 and Section 5.1. The original page-724 definition explicitly responds with maintained forest changes; the global insertion/deletion sites realize original-ID exchange reporting with constant extra work. Parallel pairs use a separate priority-queue adapter.
- The manuscript gives separate primary citations for colored connectivity, color-list spanners, and the hyperconnectivity matrix. Those comparisons do not replace the fixed-order prefix-span proof.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
