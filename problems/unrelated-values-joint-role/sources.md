# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Unrelated-value allocation near two through a joint light/heavy LP](proof.md)
- [The exact-factor-two endpoint for arbitrary unrelated allocation](exact-two.md)
- [Unrelated-value allocation with one shared setup and assignment budget](setup-budget.md)
- [Integer-quota time tradeoffs for compulsory unrelated two-value allocation](two-value-tradeoffs.md)
- [Exact original-input realization of shared resource roles](reference-realization.md)

## Mathematical dependencies

- [Unrelated-value allocation with an exact budget and a fractional comparator](../unrelated-values-additive/proof.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)
- [Faster global time for coarser integer-quota approximation](../whole-ground-allocation/integer-quotas.md)
- [Global exponential-time allocation, scheduling and selected-flow transfers](../whole-ground-allocation/proof.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md)

## Related bounds and model comparisons

- [Why arbitrary many exact assignment budgets cannot be added for free](../../manuscripts/mechanism-boundaries/multiple-exact-assignment-budgets-obstruction.md)

## Primary references

- [*Exact Algorithms via Monotone Local Search*](https://arxiv.org/abs/1512.01621)
- [*Cost Preserving Dependent Rounding for Allocation Problems*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127)

## Executable evidence

- [check_joint.py](verify/check_joint.py): Original-input integer optima, exact-half and near-two outputs, streamed covers, signed all-prefix recovery, compulsory quota target gaps, shared capacities, persistent setup credit, binary counts, original verifier independence and invalid-record rejection. The finite active-basis LP and temporary support list are separately charged in the [native API](reference/README.md).
- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): Integer-quota arithmetic: <code class="math">d=2,\ldots,30</code> and every <code class="math">d&lt;K\le399</code> (11,107 cases) satisfy <code class="math">K/(K-\lceil K/d\rceil)\le(d+1)/(d-1)</code>; every <code class="math">1\le K\le d</code> satisfies the one-unit gate. Selection, budgets, rank oracles and rounding are not executed. This applies only to the compulsory J2 and factor-<code class="math">d</code> quota arithmetic, not shared-resource or setup coupling.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
