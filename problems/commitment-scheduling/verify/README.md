# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Scheduling with local eligibility widths and collision thresholds](../eligibility-padding.md)
- [Safe machine contraction and residual large-job rank](../machine-contraction.md)

## Mathematical evidence

- An arbitrary independent commitment preserves a spanning residual promise. Resource restriction and zero extension are distinguished from player-matroid contraction, and the final singleton load is charged separately.
- The workload grid gives exact integer quotas; target search uses sound failures without assuming monotone success.
- Full-marginal contraction proves a dominated residual base, a unique threshold closure and an all-budget greedy bottleneck profile.
- Eligibility padding has an exact withdrawal rank inequality, a collision branch, a scalar refinement and integral recovery of all original job bases.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

All companions use common type sizes and no assignment or setup budget. Bottleneck terms are loads, with no implicit comparison to <code class="math">\mathrm{OPT}</code>. The sharper eligibility bound requires <code class="math">\mathrm{OPT}</code> below the collision threshold; the unrestricted guarantee retains the easy branch and additive smaller-job loss.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
