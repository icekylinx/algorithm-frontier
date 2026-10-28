# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Adaptive selected flow under explicit network scenarios](proof.md)
- [Exact realization and review of adaptive scenario flow](reference-realization.md)

## Mathematical dependencies

- [Near-optimal concurrent flow with few rejected commodities and exact selection constraints](../selected-flow/proof.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Rational comparator recovery without splitting the approximation error](../whole-ground-allocation/rational-optimization.md)

## Primary references

- [On Structural Parameterizations of Hitting Set: Hitting Paths in Graphs Using 2-SAT](https://jgaa.info/index.php/jgaa/article/view/paper413)

## Executable evidence

- [Exact adaptive-scenario reference](reference/README.md) and [implementation](reference/scenarios.py).
- [Independent scenario path, separator, witness and finite reduction checker](verify/check_scenarios.py).

The mathematical proof and repository document checks have separate roles.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
