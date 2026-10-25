# Selected splittable concurrent flow

| Field | Curated statement |
|---|---|
| **Guarantee** | Returns a feasible selected commodity set and splittable routing with common rate at least `(1-epsilon)` times the exact optimum. |
| **Objective and output** | Select exactly `r` of `q` commodities using the named restriction selector, then output the selected set and a routing that preserves every capacity and listed routing budget exactly. |
| **Time** | The exact selector base at inverse accuracy is raised to the rejection count `c = q - r`, times polynomial work in the full encoded input. The source defines the base as Gamma of inverse epsilon. |
| **Space** | Polynomial in the full binary input and paid selector, flow, and optimization work. |
| **Parameters** | `q` is the commodity count; `r` is the selected count; `c` is the rejected count; `s` is the number of optional routing-budget rows; `epsilon` is rational accuracy; `H` includes all binary data and paid primitive work. |
| **Model and representation** | Directed or undirected capacitated networks with rational data, fractional splittable flow, exact capacities, optional nonnegative routing budgets, and an exact selector such as a matroid basis or two common bases. |
| **Lower-bound scope** | No lower bound is claimed; the theorem is conditional on the restriction-selector interface. |
| **Review status** | Internal research record. The [backlog review](../../reviews/backlog/legacy-result-cards.md) keeps selector, flow, and finite-certificate assumptions separate from formal verification; see also the [review registry](../../reviews/README.md). |
| **Source** | [Selected multicommodity flow source](../../sources/checkpoint-o/selected_multicommodity_flow_corank_scheme.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
