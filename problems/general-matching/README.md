# Exact general-graph matching

| Item | Result |
|---|---|
| **Guarantee** | Exact maximum-cardinality matching in arbitrary undirected graphs with original edge identifiers. |
| **Complexity** | `O(n+m)+(m_s+1)exp(O((log(m_s+2))^(4/5)(loglog(m_s+4))^(1/5)))`, conditional on the named backend contract. |
| **Model** | Arbitrary undirected graphs, loops/parallel records cleaned with original edge identifiers; exact output. The fast bound assumes the named external primitives and raw-backend Contract R. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-o/current_checkpoint/quantitative_matching_4_5_composition.md`](../../sources/checkpoint-o/current_checkpoint/quantitative_matching_4_5_composition.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
