# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Near-optimal concurrent flow with few rejected commodities and exact selection constraints](proof.md)

## Mathematical dependencies

- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Rational comparator recovery without splitting the approximation error](../whole-ground-allocation/rational-optimization.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md)

- [Exact concurrent-flow primitive realization](../selected-flow/reference-realization.md)

## Primary references

- [Improved Throughput for All-or-Nothing Multicommodity Flows with Arbitrary Demands](https://arxiv.org/html/2005.04533v7)
- [The All-or-Nothing Multicommodity Flow Problem](https://chekuri.cs.illinois.edu/papers/anflow-sicomp.pdf)
- [Faster Approximation Schemes for Fractional Multicommodity Flow Problems via Dynamic Graph Algorithms](https://madry.mit.edu/docs/multiflow.pdf)

- [Bland, *New Finite Pivoting Rules for the Simplex Method*, Section 1 (1977)](https://people.ohio.edu/melkonia/math4620/bland.pdf): finite termination of the reference solver; no source code is imported.

## Executable evidence

[Exact concurrent-flow primitive realization](../selected-flow/reference-realization.md) proves the reference LP translation, certificate soundness and separate simplex bounds. [Independent executable check](../selected-flow/verify/check_concurrent.py) compares native path formulations and rational vertex optima. The mathematical research theorem and this baseline have different running times.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
