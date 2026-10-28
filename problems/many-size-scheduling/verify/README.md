# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).
The [private-slack finite-rank companion](../../../manuscripts/allocation-and-scheduling/many-small-sizes-private-slack-deficiency.md)
and [native realization proof](../reference-realization.md) record the distinct
cap comparator and reference implementation contracts.

## Mathematical evidence

- The pair-ground upper-prefix argument proves a per-machine additive rounding bound.
- Workload scaling, coordinate caps, duality and decomposition have polynomial binary encoding and restore every original type base.
- The hard-target integer quota, Boolean-rank-loss branch and one-sided target search cover all inputs.
- The final schedule still pays the largest-smaller-job error after refining the artificial workload grid.

## Executable evidence

[check_workload.py](check_workload.py) compares actual native outputs and target
failures with independently enumerated original job bases and loads. It covers
16 instances, 162 main target calls, 32 main optimizations, 486 private target
calls and 96 private optimizations. Four cap rejections occur at originally
feasible targets, explicitly testing that cap failure is not original
infeasibility.

Separate independent scaled-base comparisons check 144 actual decompositions
and 72 joint upper-prefix roundings, including original type totals and
per-machine bounds. Four binary tests use 81-bit original counts or multipliers
and an 81-bit accuracy denominator, executing actual scaled decomposition,
fractional intermediate original bases, rounding and optimization without
numeric count enumeration or unit copies.

```sh
python3 problems/many-size-scheduling/verify/check_workload.py
```

The native reference enumerates weak selected bases and streams exact LP active
systems. It has polynomial rational workspace in its explicit table encoding,
while its local time is charged separately from the fast theorem's polynomial
LP/intersection and rank-dependent local-search algorithms. It does not
mechanically verify those general mathematical proofs.

## Model and verification boundaries

The parameter counts mandatory units of the largest common type size, with arbitrary smaller common sizes and no assignment budget. A near-five-thirds multiplicative consequence needs the stated size-gap condition. The native workload implementation supplies its semantic reconstruction, while the rank-dependent local search retains its separate mathematical proof. The private mode keeps the attained cap threshold and additive largest-small-job term in its comparator.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
