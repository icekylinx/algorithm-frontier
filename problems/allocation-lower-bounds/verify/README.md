# Verification and scope

The evidence for this result consists of its [mathematical proof](../proof.md) and the following companion manuscripts:

- [Two integrality gaps for recipient-polymatroid configuration relaxations](../configuration-gaps.md)
- [The factor-two oracle obstruction persists at refined parameter zero](../refined-parameter-barrier.md)

## Mathematical evidence

- The hidden-set rank functions are proved normalized, monotone, integral and submodular; their oracle transcript distinguishes the unique hidden basis.
- Allocation below factor two and scheduling below three halves have separate constructions. The scheduling dual is verified as an independent rank function.
- The configuration companions distinguish the aggregate gap approaching r from the full residual gap exactly two. The refined-parameter companion specifies the threshold at which its parameter is zero.

## Executable evidence

No result-specific executable check is supplied. The argument above is a mathematical proof, not an executable certificate or a complete solver.

## Model and verification boundaries

These are rank-query lower bounds and explicitly defined relaxation gaps. They do not assert explicit-input NP-hardness, ETH bounds, or optimal approximation-algorithm exponential bases. No executable rank-family enumeration is supplied.

The [source map](../sources.md) identifies the actual proof dependencies. Repository checks validate the registry, links, notation and generated catalogue; those checks do not establish mathematical correctness. Proof-assistant verification and external peer review are not claimed.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
