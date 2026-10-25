# Exact general-graph matching

This is a Tier A conditional algorithm record for exact maximum-cardinality matching in arbitrary undirected graphs.

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns an exact maximum-cardinality matching while preserving the original identifier of every selected edge. |
| **Objective and output** | Maximize the number of matched edges and return the selected edge identifiers after loops and parallel records have been normalized. |
| **Time** | `O(n+m) + (m_s+1) exp(O((log(m_s+2))^(4/5) (log log(m_s+4))^(1/5)))`; a separate `m^(1+o(1))` assembly point remains only a comparison. |
| **Space** | Polynomial in the actual graph and backend inventory; normalization does not require losing physical edge identifiers. |
| **Parameters** | **n** is the vertex count; **m** is the input edge-record count; **m_s** is the retained edge count after normalization; loops and parallel lifetimes are handled by the source contract. |
| **Model and representation** | Arbitrary undirected graphs, exact output, and the named raw-backend Contract R plus external primitives. The conditional backend assumptions are part of the claim. |
| **Lower-bound scope** | This card records a conditional upper bound and backend boundary. It does not claim a new unconditional matching lower bound. |
| **Review status** | Internal proof, algorithm, and source review is tracked in the [headline review report](../../reviews/headline/dynamic-graph-frontier.md). Finite audit notes are evidence for the stated composition; they are not formal verification. |
| **Source** | [Quantitative matching composition](../../sources/checkpoint-o/current_checkpoint/quantitative_matching_4_5_composition.md). |

Read the [proof map](proof.md), [source map](sources.md), and [complete index](../../CONTENTS.md) for the backend contract and audit trail.


**Attribution.** Yilin Liu · GPT-6 Astra Pro
