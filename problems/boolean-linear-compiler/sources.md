# Sources and proof dependencies: Boolean linear optimization

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Cardinality and common-coefficient refinement](manuscripts/cardinality-and-modal-interval-compilation.md) | Complete guarded signed rounding, modal coefficient normalization, constant-row handling, original equalities/objectives, and uniform time–space interpolation. |
| [Signed interval compiler](manuscripts/boolean-linear-optimization-compiler.md) | Complete support-sized signed interval refinement, bounded slack, radix packing, exact optimization, and symbolic time–space composition. |

## Shared proof dependencies

| Result | Role |
|---|---|
| [Deterministic fast Subset Sum](../subset-sum-fast-deterministic/proof.md) | Baseline and refined time instantiations, retaining the full stated analytic and indexed-witness scope of the chosen theorem. |
| [Deterministic low-space Subset Sum](../subset-sum-low-space-deterministic/proof.md) | The separate joint time/space backend; its space bound is not combined with the fast backend's time. |

## External inputs

- Nederlof, van Leeuwen, and van der Zwaan, [Reducing a Target Interval to a Few Exact Queries](https://arxiv.org/pdf/1208.4225), Theorems 1–2 and Corollary 1: the interval mechanism and Knapsack/Subset Sum transfer.
- Bansal, Garg, Nederlof, and Vyas, [Faster Space-Efficient Algorithms for Subset Sum, `k`-Sum and Related Problems](https://arxiv.org/pdf/1612.02788), Lemma 4.4 and the proof of Corollary 2: signed rows and exact-target enumeration. The local manuscript proves its sharper boundary cap and the support-sensitive slack accounting directly. The cardinality and common-coefficient companion also proves its local refinements directly. These steps do not require another external theorem; the cited work supplies the historical method and comparison baseline.

## Local executable evidence

The [guarded compiler checker](verify/check_cardinality_compiler.py) verifies the stronger normalized construction and exact uniform-budget accounting. The [unconditioned compiler checker](verify/check_interval_compiler.py) uses exhaustive Boolean evaluation as its reference, including for the complete signed radix instances. The [verification note](verify/README.md) records exact counts and distinguishes these local checks from the separately supplied Subset Sum backend.

**Attribution:** icekylinx and GPT-6 Astra Pro.
