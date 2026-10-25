# Degree-constrained subgraphs

| Field | Curated statement |
|---|---|
| **Guarantee** | Finds an exact feasible degree-constrained edge subset, or correctly reports that none exists, in the stated reduction scope. |
| **Objective and output** | Supports f-factors, interval degree bounds, and cardinality optimization; outputs original edge identifiers and treats each parallel edge record as a separate selectable item. |
| **Time** | Linear graph work plus the edge-record inventory multiplied by the four-fifths logarithmic backend factor, under the general-matching reduction contract. |
| **Space** | Polynomial in the explicit graph and reduction state; binary degree bounds are not expanded into unit copies. |
| **Parameters** | `n` is the vertex count; `m` is the explicit edge-record count; `g(v)` and `f(v)` are lower and upper degree bounds. |
| **Model and representation** | Loopless undirected multigraph with capacity one per edge record. The card does not extend the result to arbitrary weighted or binary-multiplicity variants. |
| **Lower-bound scope** | No new lower bound is claimed; this is a deterministic transfer from the matching backend. |
| **Review status** | Internal research record with a conditional backend. Finite audits are not formal verification; see the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [General degree-constrained subgraph source](../../sources/checkpoint-o/general_degree_constrained_subgraphs.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
