# Featured algorithm index

This page is the short reading path for the repository. The complete catalogue is in [`CONTENTS.md`](CONTENTS.md). Each linked record separates guarantee, objective, time, space, parameters, representation, lower-bound type, and review status.

## Headline records

| Problem | Why it is featured | Displayed bound or boundary |
|---|---|---|
| [Numeric-target frontier](problems/numeric-target-frontier/) | Newest R/S checkpoint family; combines exact target algorithms, support geometry, and lower-bound boundaries. | R: `2^(O((T + 1) log(T + 2)) * poly(H))`; S: `2^(O(T log(2 + Q/T)) * poly(H))` |
| [Weighted-prefix and sparse-quota frontier](problems/weighted-prefix-quota-frontier/) | T/U extension: ordered prefix quotas, laminar completion, sparse overlap, and deterministic ground kernels. | T/U: `2^O(B)`, `2^O(B log(B + 2))`, `2^O(B^2)`, and sparse `2^O(Delta B0 log(Delta B0 B + 2))` |
| [Faster Subset Sum](problems/subset-sum-fast-deterministic/) | A central exact exponential-time record with an explicit exponent. | `C + poly(n, L) * 2^(E n)`, `E < 0.4964618056` |
| [Low-space Subset Sum](problems/subset-sum-low-space-deterministic/) | Separates a space-sensitive algorithm from the faster-time record. | Time `poly(n, L) * 2^(n/2)`; space `poly(n, L) * 2^(E_S n)` |
| [General-graph matching](problems/general-matching/) | Exact matching with a conditional fast backend contract. | `O(n + m) + (m_s + 1) exp(O((log(m_s + 2))^(4/5) * (log log(m_s + 4))^(1/5)))` |
| [Dynamic graph frontier](problems/apsp-frontier/) | Collects update/stretch tradeoffs rather than one scalar optimum. | Multiple parameterized update/stretch points |
| [Allocation and scheduling boundaries](problems/allocation-lower-bounds/) | Keeps oracle barriers and approximation endpoints visible beside algorithms. | Model-specific query and factor barriers |

## How to read the catalogue

1. Start with a headline record and inspect its `README.md` result card.
2. Follow `proof.md` for the claim decomposition and `sources.md` for exact provenance.
3. Check `verify/` before treating a claim as formally verified or implementation-ready.
4. Use [`docs/PRIORITY.md`](docs/PRIORITY.md) to distinguish headline results, supporting extensions, boundary records, and archival source material.

## Presentation rule

The index uses plain-text complexity in code spans: `exp(...)`, `poly(...)`, `2^(...)`, `eps`, and `OPT`. This is intentional. It keeps GitHub rendering stable and makes copied tables readable in terminals, diffs, and search results. Original source notation is preserved under `sources/`.

## Neighbouring families

- **Graph algorithms:** matching, dynamic APSP, dynamic spanners, incremental SSSP/SCC, and decremental strong forests.
- **Allocation and flow:** selected flow, robust scenarios, setup budgets, polymatroids, matroid configurations, and lower bounds.
- **Scheduling:** activated machines, commitments, processing buckets, two-size/two-time models, and profile endpoints.
- **Robustness and barriers:** bounded certificates, unrelated values, width-two obstructions, and two-scenario hardness.

For every directory, the repository preserves the same compact record contract. The [repository map](docs/REPOSITORY_MAP.md) explains the source and checkpoint layout.
