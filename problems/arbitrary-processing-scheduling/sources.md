# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Arbitrary-processing polymatroid scheduling: an exact-budget approximation scheme](proof.md)
- [Compressed large-job slots and corank scheduling with arbitrary smaller sizes](slot-surplus.md)
- [Exact occupied-profile and joint recovery realization](reference-realization.md)

## Mathematical dependencies

- [Arbitrary small sizes through workload aggregation and per-machine rounding](../many-size-scheduling/proof.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md)
- [Bucket thresholds and original-total upper-prefix recovery](../processing-bucket-tradeoff/proof.md)
- [Canonical exact-table LP and integer-count primitives](../two-time-scheduling/reference-realization.md)

## Primary references

- [arXiv:2307.08453v1, Theorem 23](https://arxiv.org/html/2307.08453v1)

## Executable evidence

- [Profile client and shared joint plan solver](reference/profiles.py): Exact
  occupied-bin grouping, binary count/load pruning, streamed global profiles,
  original-total LPs, one joint minimum-cost prefix recovery and grid search.
- [Independent profile checker](verify/check_profiles.py): 25 instances, 250
  targets, 50 optimizations, 345 exact profile families with 2,154 profile vectors,
  558 fixed plans, 581 joint recoveries including 221 fractional witnesses,
  158 protected profiles, 40 boundaries, five binary-accuracy checks and four
  deep-stream checks on 1,100 occupied coordinates or physical machines.
  The [original-pair oracle](verify/original_schedule_oracle.py) imports no
  scheduling implementation. The inherited LP/count enumeration costs and
  the unimplemented slot-surplus client retain their separate scope.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
