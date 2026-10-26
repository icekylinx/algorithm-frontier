# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md).

## Mathematical evidence

- The selection interface returns an attaining minimum-setup permitted set in every restriction; feasibility alone is insufficient.
- The residual routing budget changes with setup cost while one original promised set and routing remain protected.
- Nonnegative polynomial-bit support separation and exact reoptimization preserve the shared budget and full requested relative rate.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

There is one combined setup-plus-routing budget, alongside the separately stated routing-only constraints. The fixed-comparator proof does not permit arbitrary unrelated selection costs or changing the permitted family across nodes. No full selected-flow implementation is supplied.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
