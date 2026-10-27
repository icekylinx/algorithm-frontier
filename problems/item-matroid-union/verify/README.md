# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Configuration-LP comparison for the player-matroid union reduction](../configuration-comparator.md)

## Mathematical evidence

- The current-star charge supplies the finite-rank factor <code class="math">4-3/r</code> using the strict separation condition.
- Heavy-item union supplies the small-resource promise and reconstructs an actual original basis, allowing only the justified recovery deletions.
- The configuration companion defines the player and recipient marginals and proves the fractional forward reduction without input configurations or a supplied LP solution.

## Executable evidence

Run the finite reduction check:

```sh
python3 problems/item-matroid-union/verify/check_union_reduction.py
```

The exact small-instance suite covers 285 matroid pairs, 2,156 union-rank
identities, 681 dual-basis recovery extensions, 1,768 fractional points and
13,820 fractional rank constraints. It includes loops, zero ranks and full
ranks. Union ranks come from explicit disjoint decompositions, independently
of the rank-minimization formula under test. Fractional sums use rational
arithmetic throughout.

The checker enumerates small binary-represented families plus the free matroid;
it is neither an implementation of the polynomial union algorithm nor a full
allocation solver. Base-polytope domination and configuration-row scaling
remain supported by their written general proofs.

## Model and verification boundaries

Items and liking incidences are explicit, values are intrinsic, and selected players form an original matroid basis. The factor approaches four with increasing rank; it is not a fixed improvement below four for all ranks. Rank one is handled exactly.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
