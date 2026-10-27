# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Exact factor two for one-value allocation with arbitrary assignment costs](proof.md)
- [One-value optional allocation with a shared setup and assignment budget](setup-tradeoffs.md)
- [Direct Boolean-cap and one-unit gate proof](one-unit-gate.md)
- [Native capped-service separator and exact shared-budget recovery](reference-realization.md)

## Mathematical dependencies

The main exact factor-two theorem has a complete local route through its
budgeted nonnegative support separator, the first-violation omission theorem,
no-loss quota recovery, one-unit gate and one-sided integer search. The
[gate note](one-unit-gate.md) proves Boolean-cap augmentation and the exact
assignment-pair correspondence directly, including zero capacities and costs.
All finite grounds are indexed by original players and types; binary resource
capacities are not expanded into copies.

Exact submodular minimization, rational linear optimization with separation,
and minimum-weight matroid or integral-polymatroid intersection remain the
explicit paid polynomial primitives in the theorem's model. The local proof
specifies their ranks, costs, feasibility separators and binary dimensions;
the finite checker does not purport to implement these general algorithms.
The full audit of 2026-10-27 also covers the setup companion's attaining
minimum-setup selector and protected original full witness, every small-target
gate for general fixed integer factors, and the original forced-omission
interface of the streamed whole-ground conversion. Setup fees and assignment
costs are one combined budget; the exact prescribed-basis problem retains its
separate polynomial endpoint.

The [native realization](reference-realization.md) proves a direct capped-service
primal/dual separator and dominant scalar minimum-cost recovery. The
[reference client](reference/README.md) reuses canonical weighted intersection,
weighted omission, streamed rational covers and exact Bland simplex. Native
finite LP time and the general-integer rational cover envelope are documented
separately from the paid polynomial primitives and sharp fixed-factor
algebraic cover theorem. Capacities and quotas remain binary throughout.

- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Faster global time for coarser integer-quota approximation](../whole-ground-allocation/integer-quotas.md)
- [Rational comparator recovery without splitting the approximation error](../whole-ground-allocation/rational-optimization.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md)

## Related bounds and model comparisons

- [Optional active machine bases: an oracle obstruction before approximation](../../manuscripts/mechanism-boundaries/optional-active-machine-basis-oracle-obstruction.md)
- [A value-oracle barrier below factor two for rank-parameterized allocation](../allocation-lower-bounds/proof.md)

## Primary references

- [*Cost Preserving Dependent Rounding for Allocation Problems*, ICALP 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.127/LIPIcs.ICALP.2025.127.html)

## Executable evidence

- [check_one_value.py](verify/check_one_value.py): 35 original-input instances,
  1,072 targets, 210 optional optimizations, 60 prescribed-basis exact optima
  and 300 exact quota tests. Independent original count vectors check the
  combined setup/assignment budget, actual selected basis, 286 packing rows
  and 292 protected setup nodes. There are 536 whole-ground calls, four
  binary-size guards and 13 malformed rejections. The reference implements
  actual allocation; finite tests do not prove its asymptotic bounds.
- [check_one_unit_gate.py](verify/check_one_unit_gate.py): 69 finite resource ranks, 2,495 augmentation pairs, and 285 exact-cost gate instances. Direct original unit assignments and independent pair-subset enumeration agree in 1,602 budget comparisons, including zero capacities, loops, zero costs, zero budgets and infeasible gates.
- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
