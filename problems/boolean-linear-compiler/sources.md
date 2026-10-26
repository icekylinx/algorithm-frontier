# Sources and proof dependencies: Boolean linear optimization

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Signed interval compiler](manuscripts/boolean-linear-optimization-compiler.md) | Signed interval reduction, bounded slack, radix packing, exact optimization, and symbolic time–space composition. |

## Shared proof dependencies

| Result | Role |
|---|---|
| [Deterministic fast Subset Sum](../subset-sum-fast-deterministic/proof.md) | Baseline and refined time instantiations, each retaining its stated full-domain contact premise and indexed-witness interface. |
| [Deterministic low-space Subset Sum](../subset-sum-low-space-deterministic/proof.md) | The separate joint time/space backend; its space bound is not combined with the fast backend's time. |

## External inputs

- Nederlof, van Leeuwen, and van der Zwaan, [Reducing a Target Interval to a Few Exact Queries](https://arxiv.org/pdf/1208.4225), Theorems 1–2 and Corollary 1: the interval mechanism and Knapsack/Subset Sum transfer.
- Bansal, Garg, Nederlof, and Vyas, [Faster Space-Efficient Algorithms for Subset Sum, k-Sum and Related Problems](https://arxiv.org/pdf/1612.02788), Lemma 4.4 and the proof of Corollary 2: signed rows and exact-target enumeration. The local manuscript isolates the additional support-sensitive slack accounting.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
