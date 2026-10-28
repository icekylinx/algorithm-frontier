# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Arbitrary small sizes through workload aggregation and per-machine rounding](proof.md)
- [Native binary workload realization and finite solver costs](reference-realization.md)

## Mathematical dependencies

- [Unit quotas, a factor-three transfer, and the discrete time boundary](../../manuscripts/allocation-and-scheduling/unit-quota-three-transfer-and-discrete-time-gate.md)
- [Two-size polymatroid scheduling parameterized by the number of large units](../two-size-scheduling/rank-parameter.md)
- [Workload private slack and exact finite-rank coefficient](../../manuscripts/allocation-and-scheduling/many-small-sizes-private-slack-deficiency.md)
- [Private-coordinate contraction and insertion](../../manuscripts/allocation-and-scheduling/two-size-makespan-private-slack-deficiency.md)
- [Binary recipient-count representation and integer comparator](../recipient-polymatroid/representation.md)
- [Normalized equal-unit quota construction](../recipient-polymatroid/proof.md)
- [Binary workload sum-decomposition lemma](../arbitrary-processing-scheduling/slot-surplus.md#8-reconstructing-every-original-job-and-bounding-the-load)

## Primary references

- [BLMRS23, Theorem 23 and its proof](https://arxiv.org/html/2307.08453v1)

## Executable evidence

- [Native workload reference](reference/workload.py): binary scaled decomposition,
  fixed full-machine dual, weak-basis selection, original upper rounding,
  equal-largest-type recovery and exact one-sided optimization. The private
  mode distinguishes cap rejection from original infeasibility.
- [Independent original-job checker](verify/check_workload.py): 16 instances,
  162 main targets and 32 optimizations, 486 private targets and 96 private
  optimizations, 144 scaled decompositions, 72 upper roundings, four binary
  checks and four cap rejections on originally feasible targets. Reference
  active-system/subset time is separate from the fast theorem's primitives.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
