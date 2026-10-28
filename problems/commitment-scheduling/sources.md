# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Scheduling by bottleneck commitments and a reduced search rank](proof.md)
- [Scheduling with local eligibility widths and collision thresholds](eligibility-padding.md)
- [Safe machine contraction and residual large-job rank](machine-contraction.md)

## Mathematical dependencies

- [Unit quotas, a factor-three transfer, and the discrete time boundary](../../manuscripts/allocation-and-scheduling/unit-quota-three-transfer-and-discrete-time-gate.md)
- [Arbitrary small sizes through workload aggregation and per-machine rounding](../many-size-scheduling/proof.md)
- [Prefix normalization gives factor four for arbitrary recipient polymatroids](../recipient-polymatroid/proof.md)
- [Two-size polymatroid scheduling parameterized by the number of large units](../two-size-scheduling/rank-parameter.md)

## Primary references

- [Bamas et al., arXiv:2307.08453v1](https://arxiv.org/html/2307.08453v1)

## Executable evidence

- [Reference API](reference/README.md) and [realization proof](reference-realization.md): original-optimum workload/two-size clients, full-marginal machine contraction, actual dominated-base recovery/lifting, bottleneck positions and exact local eligibility/padding certificates.
- [Absorption checker](verify/check_absorption.py): all-order closures and original resource bases, collision thresholds, Boolean ranks and binary counts.
- [Structural profile checker](verify/check_commitment_profiles.py): exhaustive original matroid commitments and independent piecewise-affine minimax envelopes.
- [Original scheduling client checker](verify/check_commitment_client.py): original integer optima, exact quota modes, zero quota on commitments and actual fallback outputs.
- [Reused native workload decomposition and upper rounding](../many-size-scheduling/reference-realization.md): exact original types and separate streamed active-system costs.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
