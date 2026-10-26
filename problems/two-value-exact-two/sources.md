# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Exact two for compulsory two-value allocation with arbitrary assignment costs](proof.md)

## Mathematical dependencies

- [Arbitrary-cost allocation near factor two with an adaptive residual budget](../../manuscripts/allocation-and-scheduling/arbitrary-cost-residual-budget-near-two-allocation.md)
- [Exact factor two for one-value allocation with arbitrary assignment costs](../one-value-exact-two/proof.md)
- [Corank omission with a changing residual budget](../whole-ground-allocation/adaptive-selection.md)
- [A polynomial-space conversion from corank gaps to global exponential time](../whole-ground-allocation/global-conversion.md)

## Related bounds and model comparisons

- [A value-oracle barrier below factor two for rank-parameterized allocation](../allocation-lower-bounds/proof.md)

## Primary references

- [*Cost Preserving Dependent Rounding for Allocation Problems*, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): The d=2 quota subcheck covers K=1,...,399: the exact one-unit gate for K<=2 and K/(K-ceil(K/2))<=3 for K>2. This is arithmetic evidence only; it does not execute support selection, branching or recovery.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
