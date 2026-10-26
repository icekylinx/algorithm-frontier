# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Exact factor two at the half-optimum derived corank](../exact-two-boundaries.md)
- [General-value near-two allocation with an arbitrary player matroid](../player-selection.md)

## Mathematical evidence

- All value splits are enumerated with equality on the heavy side; skipped over-budget splits are never declared infeasible.
- The optional-selection companion proves both directions of the dual-union adapter, including an original basis containing the retained light basis.
- Compressed light reconstruction pays one largest-light-unit loss; the optional-player fallback is proved separately.
- The exact-two companion uses the half-optimum threshold and proves XP time, polynomial corank zero and the quantified light-gap FPT regime.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

Values are common intrinsic values, recipient polymatroids are independent, unused resources are allowed, and no assignment or setup budget is included. Near-two and exact-two use different threshold parameters. Unquantified strict light-value slack does not establish exact-two FPT.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
