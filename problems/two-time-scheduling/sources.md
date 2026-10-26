# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Two processing times per machine, with unrelated values across machines](proof.md)

## Mathematical dependencies

- [Unrelated two-size job scheduling with an exact assignment budget](../../manuscripts/allocation-and-scheduling/unrelated-two-size-costed-scheduling-tradeoff.md)
- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](../processing-bucket-tradeoff/proof.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Faster global time for coarser integer-quota approximation](../whole-ground-allocation/integer-quotas.md)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): Integer-quota arithmetic: d=2,...,30 and every d<K<=399 (11,107 cases) satisfy K/(K-ceil(K/d)) <= (d+1)/(d-1); every 1<=K<=d satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Target-dependent masks and zero-time feasibility are not tested.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
