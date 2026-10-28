# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [A Fibonacci-base exact gate for width-two robust unit feasibility](proof.md)
- [Realization and scoped review of the width-two unit gate](reference-realization.md)

## Mathematical dependencies

- [Robust unit allocation with bounded minimal infeasibility certificates](../robust-bounded-certificates/proof.md)
- [Two exact scenario budgets already obstruct corank-FPT unit selection](../robust-two-scenario-hardness/proof.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)

## Primary reference

- [Bárász et al., Matroid Intersection under Minimum Rank Oracle, arXiv:2407.03229v2, Definition 2.2 and Algorithm 1](https://arxiv.org/html/2407.03229v2#S2). The reference uses the standard independence-oracle augmentation described there; it does not require the paper's minimum-rank-only machinery.

## Executable evidence

- [Local oracle gate and polynomial matching intersection](reference/README.md).
- [Independent exhaustive graph, matroid and width-guard comparisons](verify/check_width_two.py).

The mathematical proof and repository document checks have separate roles.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
