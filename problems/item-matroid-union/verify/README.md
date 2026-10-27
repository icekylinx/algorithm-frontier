# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Configuration-LP comparison for the player-matroid union reduction](../configuration-comparator.md)

## Mathematical evidence

- The current-star charge supplies the finite-rank factor <code class="math">4-3/r</code> using the strict separation condition.
- Heavy-item union supplies the small-resource promise and reconstructs an actual original basis, allowing only the justified recovery deletions.
- The configuration companion defines the player and recipient marginals and proves the fractional forward reduction without input configurations or a supplied LP solution.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

Items and liking incidences are explicit, values are intrinsic, and selected players form an original matroid basis. The factor approaches four with increasing rank; it is not a fixed improvement below four for all ranks. Rank one is handled exactly.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
