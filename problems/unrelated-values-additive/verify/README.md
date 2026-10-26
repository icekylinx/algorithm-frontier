# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- FOPT selects an actual permitted basis and then optimizes fractional assignments; selection is not fractional.
- Downward utility, clipped supports and normalized separation give a nonnegative polynomial-bit packing interface, including zero values.
- Disposal, complement duality and player-specific prefix orders give one simultaneous rounding; the maximum-total face and one actual cost objective preserve budget.
- Denominator bounds and exact reoptimization distinguish comparator recovery from approximate target search.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

The output pays a player-specific largest eligible value as additive loss. A common-value specialization does not remove it automatically. The profile and quota checker does not test this arbitrary-value rounding theorem, so no executable check is registered.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
