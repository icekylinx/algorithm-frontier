# Graph color-failure certificates — checkpoint X draft

**Status: Draft checkpoint X.** This is a source-linked candidate for correlated color failures.

| Field | Candidate statement |
|---|---|
| **Guarantee** | For an undirected graph with vertex color classes, retain at most `sum_C (n_C k_C - binom(k_C + 1, 2))` edges, where `k_C = min(h + 1, q_C)`, while preserving every surviving weighted prefix and its canonical minimum spanning forest after any failure of at most `h` colors. |
| **Objective and output** | Preserve the connected-component partition of every surviving edge prefix and therefore the canonical Kruskal forest, including signed edge weights and fixed edge-ID tie breaking. Mixed vertex/edge colors and overlapping color lists are separate extensions in the source. |
| **Time** | Deterministic polynomial preprocessing in the explicit graph and color representation, subject to the source activation-matrix construction. No near-linear or dynamic update bound is claimed. |
| **Space** | The displayed count is retained original-edge records. It is not a bound on auxiliary matrix or elimination workspace. |
| **Parameters** | `n_C` and `q_C` are the vertex and color counts in original component `C`; `h` is the number of failed colors; mixed and list variants introduce their own label multiplicities. |
| **Model and representation** | Explicit undirected graph, optionally with parallel edges; each vertex has a fixed color in the base model; signed rational weights and permanent edge IDs. Loops can be discarded. |
| **Lower-bound scope** | Ordinary individual-vertex sharpness is attributed to prior work. Correlated-color, mixed, and list lower bounds remain source-review items and are not promoted as new unconditional lower bounds. |
| **Review status** | Draft checkpoint X. Proof, algorithm, and source review are pending; formal verification is not claimed. |
| **Source** | [Colored graph and vertex-failure draft](../../sources/checkpoint-x/05_colored_graph_and_vertex_failure_certificates.md). |

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
