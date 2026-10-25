# Checkpoint X — reading guide and archive identity

**Status: draft.** **Curation: source-only; family-level non-promoted draft cards only.**

This directory maintains the complete uploaded X archive in one source tree. The revised payloads `01` and `02` replace their earlier X versions in place; payloads `03`–`09` are retained; payloads `10`–`38` add the new continuation. During curation, the proof/algorithm pass also edited `01`, `03`, `04`, `05`, `06`, `07`, `08`, and `09` in place to make proof, bit, oracle, and branch-accounting assumptions explicit. The archive README is preserved as the source context. `MANIFEST.json` records both the immutable upload hashes and the current hashes after those edits. No claim in this increment is a stable catalogue result.

## Payload by mathematical family

| Family | Payloads | Review priority | Current reading boundary |
|---|---|---:|---|
| Exact sensitivity, flow, and matching | `01`, `09`, `10`, `12`, `13`, `14`, `16` | A | Exact one-failure summaries and compact sensitivity compilers. Keep matroid, flow, matching, and nonnegative-sampling models separate. |
| Subset Sum | `02` | A | Deterministic signed-binary exponent `158153814247997/318927986919134 ≈ 0.4958919278`, conditional on the pinned compiler and proof contracts. |
| Correlated spectral, regression, and seminorm summaries | `03`, `11`, `15`, `17`, `18`, `19`, `26` | A | Uniform correlated-failure transfers, graded incidence lifts, and regression/norm consequences. Record field, label degree, rank, and probability model. |
| Matroid, packing, cuts, and whole blocks | `04`, `05`, `06`, `07`, `27`, `28`, `29` | B | Represented and oracle models, exact label annihilation, adaptive quotient resparsification, and whole-item extensions. |
| Boolean linear compiler | `08` | B | An interval/slack reduction whose numerical bound is conditional on the imported Subset Sum backend. |
| Group, subgroup, affine, and metric sparsification | `20`, `30`, `31`, `32`, `35`, `36`, `37` | A | Finite-group, affine-coset, Hilbert-metric, quotient-rank, and few-orbit claims. Compact and existential bounds are distinct. |
| Quantum, Pauli, qudit, and stabilizer blocks | `21`, `22`, `23`, `24`, `25`, `34` | A | Positive Pauli/Weyl/stabilizer block summaries with explicit local-dimension and locality assumptions. |
| Exact-separation and obstruction boundaries | `33`, `38` | B | coNP-completeness and the non-Fano counterexample delimit compact implementations and stronger conjectures. |

## Review boundary

Every payload remains a research draft for proof, algorithm, and source review. A finite script may check an exact identity or a bounded example; it does not verify a theorem. Draft cards are review handles, not promotions. In particular, existential support, randomized compact construction, deterministic construction, query time, and bit complexity must not be merged into one headline.

- Archive inventory: [`MANIFEST.json`](MANIFEST.json).
- Uploaded source context: [`README.md`](README.md).
- Review map: [`reviews/backlog/checkpoint-x-drafts.md`](../../reviews/backlog/checkpoint-x-drafts.md).
