# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Arbitrary-value allocation with setup fees: an exact-budget approximation scheme](proof.md)
- [Native exact-budget profile realization](reference-realization.md)

## Mathematical dependencies

- [Unrelated-value allocation with an exact budget and a fractional comparator](../unrelated-values-additive/proof.md)

## Primary references

- [Cost Preserving Dependent Rounding for Allocation Problems, ICALP 2025](https://doi.org/10.4230/LIPIcs.ICALP.2025.127)

## Executable evidence

- [Exact-table profile backend and API](reference/README.md) and [independent original-input checker](verify/check_scheme.py).
- Reuses canonical [intrinsic rank validation and base-coordinate elimination](../intrinsic-values-near-two/reference/README.md), [occupied scheduling profile iteration](../arbitrary-processing-scheduling/reference/README.md) and exact Gaussian elimination from the [two-time reference](../two-time-scheduling/reference/README.md).

The mathematical proof and repository document checks have separate roles.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
