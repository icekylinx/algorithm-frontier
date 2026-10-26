# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [A three-halves algorithm for two-size polymatroid scheduling in the corank parameter](proof.md)
- [Two-size polymatroid scheduling parameterized by the number of large units](rank-parameter.md)

## Mathematical dependencies

- [Two-size scheduling with a private-slack rank deficit](../../manuscripts/allocation-and-scheduling/two-size-makespan-private-slack-deficiency.md)
- [Single-exponential corank time by branching on a required omission batch](../../manuscripts/allocation-and-scheduling/unit-quota-corank-batch-branching-improvement.md)
- [Unit-quota allocation by corank-bounded deficient-set branching](../../manuscripts/allocation-and-scheduling/unit-quota-corank-gap-branching.md)
- [Unit quotas, a factor-three transfer, and the discrete time boundary](../../manuscripts/allocation-and-scheduling/unit-quota-three-transfer-and-discrete-time-gate.md)
- [Prefix normalization gives factor four for arbitrary recipient polymatroids](../recipient-polymatroid/proof.md)

## Related bounds and model comparisons

- [A value-oracle barrier below factor two for rank-parameterized allocation](../allocation-lower-bounds/proof.md)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): The d=2 quota subcheck covers K=1,...,399: the exact one-unit gate for K<=2 and K/(K-ceil(K/2))<=3 for K>2. This is arithmetic evidence only; it does not execute support selection, branching or recovery. It does not test the separate five-thirds rank algorithm.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
