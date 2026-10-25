# Selected splittable concurrent flow

| Item | Result |
|---|---|
| **Guarantee** | Rate at least `(1-eps)OPT` with exact routing constraints. |
| **Complexity** | `Gamma(1/eps)^c poly(H)` |
| **Model** | Directed or undirected splittable concurrent flow; restriction-selectable exact r-set, explicit nonnegative routing budgets, and rational input as specified. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-o/selected_multicommodity_flow_corank_scheme.md`](../../sources/checkpoint-o/selected_multicommodity_flow_corank_scheme.md) and the verification paths named in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
