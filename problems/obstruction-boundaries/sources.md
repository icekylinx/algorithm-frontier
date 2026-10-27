# Sources and proof dependencies: Exact membership and fixed-amplitude obstructions

[Result statements](README.md) · [Main proof](proof.md) · [Verification and scope](verify/README.md)

The main proof gives the family-level theorem composition. The following canonical manuscripts contain the detailed arguments and the hypotheses of each algorithmic interface.

## Canonical manuscripts

| Manuscript | Proof role |
|---|---|
| [Compact-code exact membership](manuscripts/exact-separation-for-compact-codes.md) | The weighted-Max-Cut reduction, coNP-completeness of membership, and the consequence for exact separation. |
| [Non-Fano fixed-amplitude obstruction](manuscripts/non-fano-obstruction-to-fixed-amplitude-bound.md) | The rank-three ternary representation, thirteen supports, fifteen valid signs, and direct sums. |

## Executable reduction and exact verification

The [local realization proof](manuscripts/reference-compact-membership.md)
records the weighted Max-Cut source's exact threshold direction and positive
integer convention, read at Karp's Problem 21 and Appendix I. The
[reference API](reference/README.md) constructs the body in linear record
work, checks strict nonmembership witnesses without search, and supplies a
separately exponential exhaustive oracle. No third-party code is imported.

## Related results and model distinctions

| Result | Role |
|---|---|
| [Gaussian subgroup comparison](../group-metric-constraints/manuscripts/optimal-whole-subgroup-constraints.md) | A different, unconditional Gaussian event. This comparison explains the model boundary; it is not a prerequisite of the finite counterexample. |

## External inputs

- Karp, [Reducibility Among Combinatorial Problems](https://doi.org/10.1007/978-1-4684-2001-2_9), supplies the Max-Cut complexity input.
- The non-Fano construction is proved directly from its displayed matrix and amplitudes, with the independent executable replay linked in [Verification and scope](verify/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
