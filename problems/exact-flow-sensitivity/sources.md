# Sources and proof dependencies: Exact flow, matching, and price sensitivity

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Flow and vertex-disjoint paths](manuscripts/exact-min-cost-flow-and-vertex-disjoint-paths.md) | Residual replacement identity, support-sensitive and acyclic bounds, path reporting, and vertex-failure gates. |
| [General matching certificates](manuscripts/linear-single-fault-general-matching.md) | Odd-set support argument, maximum-cardinality and fixed-size variants, and blossom-aware repair. |
| [Unweighted two-matroid certificate](manuscripts/linear-unweighted-two-matroid-certificate.md) | Tight-set dimension argument and a linear rank-only single-failure summary. |
| [One-element price sensitivity](manuscripts/compact-one-element-price-sensitivity.md) | Forced-element identities, price-query reports, and fixed-rank insertion from a supplied catalog. |

## Shared proof dependencies

| Result | Role |
|---|---|
| [Exchange and distance-preserver implementation](../exact-failure-preservers/manuscripts/exact-single-failure-arborescences-and-matroid-intersection.md) | Weighted exchange repairs, the minimum-hop distinction, and the classical pairwise-distance reporting primitive. |

## External inputs

The companions identify the classical residual-flow, matching-polytope, blossom-augmentation, and two-matroid-intersection inputs at the point of use. The shared distance-preserver input is [Bodwin's pairwise-distance theorem](https://arxiv.org/pdf/2001.07741). These algorithmic primitives are mathematical dependencies; the finite exchange replay does not implement a general flow or blossom solver.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
