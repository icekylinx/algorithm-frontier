# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Robust unrelated allocation with a common setup objective and additive loss](proof.md)
- [Exact common-basis reference for robust unrelated allocation](reference-realization.md)

## Mathematical dependencies

- [Unrelated-value allocation with an exact budget and a fractional comparator](../unrelated-values-additive/proof.md)
- [Rational comparator recovery without splitting the approximation error](../whole-ground-allocation/rational-optimization.md)
- [Single-exponential corank time for weighted packing through first-violation prefixes](../whole-ground-allocation/selection.md)
- [Streamed polynomial-space global conversion](../whole-ground-allocation/global-conversion.md)
- [Shared original-resource LP and signed prefix realization](../unrelated-values-joint-role/reference-realization.md)

## Related bounds and model comparisons

- [Robust integer unit allocation has a corank-parameter obstruction](../../manuscripts/mechanism-boundaries/robust-unit-allocation-corank-obstruction.md)
- [Two obstructions to lifting one-scenario roles into robust allocation](../../manuscripts/mechanism-boundaries/robust-unrelated-common-role-obstructions.md)

## Primary references

- [*Exact Algorithms via Monotone Local Search*](https://arxiv.org/abs/1512.01621)
- [*Cost Preserving Dependent Rounding for Allocation Problems*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127)

## Executable evidence

- [check_robust.py](verify/check_robust.py): Independently rebuilt original fixed-basis fractional LPs and integer comparators, forced/common-basis gaps, full-accuracy rational and global-cover optimization, scenario rounding, role-disagreement and zero/one obstruction bases, binary counts and producer-disabled original verification. The [native API](reference/README.md) charges its finite active-basis LP and support storage separately from the theorem's polynomial primitives.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
