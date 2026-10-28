# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Two processing times per machine, with unrelated values across machines](proof.md)
- [Exact complete-table realization of the heterogeneous scheduling interfaces](reference-realization.md)

## Mathematical dependencies

- [Unrelated two-size job scheduling with an exact assignment budget](../../manuscripts/allocation-and-scheduling/unrelated-two-size-costed-scheduling-tradeoff.md)
- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](../processing-bucket-tradeoff/proof.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Faster global time for coarser integer-quota approximation](../whole-ground-allocation/integer-quotas.md)
- [Weighted first-violation prefix certificates and their complete time bound](../whole-ground-allocation/selection.md)
- [Changing-region protected-witness accounting](../whole-ground-allocation/adaptive-selection.md)

## Executable evidence

- [Exact complete-table backend](reference/scheduling.py) implements original-total
  target LPs, heterogeneous service support rows, joint minimum-cost integer
  recovery and one-sided grid optimization. Its explicit enumeration costs are
  proved in [the realization contract](reference-realization.md).
- [Independent scheduling checker](verify/check_scheduling.py) compares finite
  target and optimization results against independently enumerated original
  assignments, and checks every sampled weak-region vertex's recovery, support
  rows and protected omission inequalities. It includes rational inputs,
  zero-time costs, masks, nonmodular ranks and unequal quotas.

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. Target-dependent masks and zero-time feasibility are not tested.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
