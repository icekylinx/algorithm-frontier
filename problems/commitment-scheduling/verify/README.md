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

The [native modules](../reference/README.md) have a standalone
[realization proof](../reference-realization.md). Run the three independent
original-input checkers:

```sh
python3 -B problems/commitment-scheduling/verify/check_absorption.py
python3 -B problems/commitment-scheduling/verify/check_commitment_profiles.py
python3 -B problems/commitment-scheduling/verify/check_commitment_client.py
```

- Absorption: 109 original instances, 352 threshold closures, 1,317 reachable
  absorption sets across arbitrary legal orders, 369 rank-budget queries,
  1,553 dominated contracted bases and 839 lifts into original job schedules.
  The same fixtures compare 109 collision thresholds and 729 Boolean ranks
  with original assignments. Seven invalid/forged inputs are rejected.
- Structural profiles: 78 matroids, 606 bottleneck commitments, 1,419 original
  basis-image checks and 984 completions. Independent piecewise-affine envelope
  optimization checks 700 padding problems, including 18 strict improvements
  over the simpler certificate and an exact active-set endpoint. Six malformed
  profile inputs are rejected.
- Main clients: nine original job systems, 154 targets, 68 optimizations,
  58 actual commitment branches and 16 two-size configurations, with four
  malformed queries rejected. Independent original schedule enumeration checks
  every full base and original optimum bound. A separate fixture succeeds with
  zero quota on commitments even though the private-cap method rejects that
  originally feasible target. Noninteger size ratios and positive-slack exact
  quota arithmetic are exercised.

Additional guards cover decreasing marginal loads, full bottleneck plateaus,
zero-cost initial absorption and 100-digit capacities without unit expansion.
The exact original largest/smaller job decomposition is supplied by the
[canonical workload backend](../../many-size-scheduling/reference/README.md).

## Model and verification boundaries

All companions use common type sizes and no assignment or setup budget. Bottleneck terms are loads, with no implicit comparison to <code class="math">\mathrm{OPT}</code>. The sharper eligibility bound requires <code class="math">\mathrm{OPT}</code> below the collision threshold; the unrestricted guarantee retains the easy branch and additive smaller-job loss.

The native clients use streamed residual subset and LP active-system enumeration,
with their explicit costs separate from the fast theorem's rank-local search.
The structural preprocessing and scalar optimizer are implemented; the complete
heterogeneous-large padding allocator and external specialized two-size fallback
are not. The independent full proof audit covers all three canonical manuscripts,
including the actual original-optimum and capped-comparator distinctions.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** icekylinx and GPT-6 Astra Pro.
