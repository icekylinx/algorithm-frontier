# Sources and proof dependencies: Packing and matching failure summaries

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Represented-resource packing transfer](manuscripts/represented-resource-packing-transfer.md) | Exterior features, product-space replacement, matching specializations, full resource rank, and rational bit accounting. |

The [rational implementation realization](manuscripts/reference-product-realization.md) proves that the shipped [backend](reference/README.md) instantiates this construction without a query-dependent resource truncation. The finite-field extension argument is supplied by Section 5.3 of the shared failure-feature manuscript, applied to a field large enough for both the padded support universe and the label codes. Published representative-family papers are credited antecedents; the local replacement proof is given in full.

## Shared proof dependencies

| Result | Role |
|---|---|
| [Polynomial failure features](../matroid-failure-summaries/manuscripts/sharp-represented-matroid-failure-summaries.md) | One failure-annihilating coefficient feature for each label system. |

## External inputs

- Fomin, Lokshtanov, Panolan, and Saurabh, [Efficient Computation of Representative Families with Applications in Parameterized and Exact Algorithms](https://sites.cs.ucsb.edu/~daniello/papers/efficientRepSetJ.pdf).
- van Bevern, Tsidulko, and Zschoche, [Representative Families for Matroid Intersections, with Applications to Location, Packing, and Covering Problems](https://arxiv.org/html/1806.11527v4).

The companion proves the combined packing, failure, and later-extension replacement statement and states exactly where a representation of the original resource matroid is required.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
