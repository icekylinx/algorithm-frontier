# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [A three-halves algorithm for two-size polymatroid scheduling in the corank parameter](proof.md)
- [Two-size polymatroid scheduling parameterized by the number of large units](rank-parameter.md)
- [Complete-table realization of the two-size corank construction](reference-realization.md)

## Mathematical dependencies

- [Two-size scheduling with a private-slack rank deficit](../../manuscripts/allocation-and-scheduling/two-size-makespan-private-slack-deficiency.md)
- [Single-exponential corank time by branching on a required omission batch](../../manuscripts/allocation-and-scheduling/unit-quota-corank-batch-branching-improvement.md)
- [Unit-quota allocation by corank-bounded deficient-set branching](../../manuscripts/allocation-and-scheduling/unit-quota-corank-gap-branching.md)
- [Unit quotas, a factor-three transfer, and the discrete time boundary](../../manuscripts/allocation-and-scheduling/unit-quota-three-transfer-and-discrete-time-gate.md)
- [Prefix normalization gives factor four for arbitrary recipient polymatroids](../recipient-polymatroid/proof.md)
- [Binary count representation and the integer comparator](../recipient-polymatroid/representation.md)
- [Prefix-normalized recipient-matroid invariants](../recipient-matroid-configuration/proof.md)
- [Earliest-layer player exchanges and the bounded signature](../../manuscripts/allocation-and-scheduling/matroid-allocation-current-blocker-quasipolynomial.md)
- [Integer-quota corank and whole-ground scheduling curve](../whole-ground-allocation/integer-quotas.md)
- [Streamed polynomial-space global conversion](../whole-ground-allocation/global-conversion.md)

## Related bounds and model comparisons

- [A value-oracle barrier below factor two for rank-parameterized allocation](../allocation-lower-bounds/proof.md)

## Executable evidence

- [Complete-table corank client](reference/corank.py) implements the actual
  hard-target Boolean rank, full-ground dual, exact one-unit gate, guarded batch
  recursion and binary base completion. Its high-target LP/recovery calls the
  canonical [two-time backend](../two-time-scheduling/reference/scheduling.py).
- [Independent original-base checker](verify/check_corank.py) checks 408 finite
  instances, 3,789 targets, 422 optimizations, 400 box-rank support values,
  2,390 dual-complement vectors, 295 base completions, 599 reached batch nodes,
  78 guards and one rejected-rank child. Six additional checks use an 81-bit
  forced count while disabling the shared high-target routine. The general
  oracle theorem and separate large-unit-rank local search are not executed.

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): The <code class="math">d=2</code> quota subcheck covers <code class="math">K=1,\ldots,399</code>: the exact one-unit gate for <code class="math">K\le2</code> and <code class="math">K/(K-\lceil K/2\rceil)\le3</code> for <code class="math">K&gt;2</code>. This is arithmetic evidence only; it does not execute support selection, branching or recovery. It does not test the separate five-thirds rank algorithm.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
