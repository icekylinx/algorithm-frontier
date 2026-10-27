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
| [Compact unit-flow reference realization](manuscripts/reference-unit-flow-realization.md) | Self-contained exact-rational augmenting-path baseline, single-failure residual identity, phased short-path/hub construction, original-record support and query reporting; includes a separate polynomial preprocessing and bit-cost contract. |

The [native vertex-path realization](manuscripts/reference-vertex-path-realization.md)
completes the internal unit-gate client, original-failure interpretation and
zero-cost-cycle-safe path recovery. It uses the exact unit-flow reference
and proves its own polynomial preprocessing bound.

The [independent flow certificate proof](manuscripts/independent-flow-certificates.md)
proves reduced-cost completeness, maximum and infeasibility cut certificates,
and a binary-input general-balance feasibility constructor. These arguments
are self-contained. The verifier scans the full surviving original graph;
its signed-cost scope does not extend compact minimum-cost initialization.

## Shared proof dependencies

| Result | Role |
|---|---|
| [Exchange and distance-preserver implementation](../exact-failure-preservers/manuscripts/exact-single-failure-arborescences-and-matroid-intersection.md) | Weighted exchange repairs, the minimum-hop distinction, and the classical pairwise-distance reporting primitive. |

## External inputs

The companions identify the classical residual-flow, matching-polytope, blossom-augmentation, and two-matroid-intersection inputs at the point of use. The shared distance-preserver input is [Bodwin's pairwise-distance theorem](https://arxiv.org/pdf/2001.07741). The local phased construction gives its complete elementary support/reporting argument and is implemented for the unit-flow client; the classical size theorem is not an unresolved interface. The flow reference has its own slower polynomial preprocessing bound. These primitives are mathematical dependencies; the finite exchange replay alone does not implement a general flow or blossom solver.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
