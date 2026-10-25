# Strong Haxell hypergraph matching

| Item | Result |
|---|---|
| **Guarantee** | Returns either a matching covering every vertex of A or a directly checkable hitting-set obstruction. |
| **Complexity** | $$O(|A|+|B|)+p\exp(O(U\log(2+s)/s))$$. |
| **Model** | Strong Haxell hypergraph input and the precise matching promise in the source; this is separate from general graph matching. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-o/explicit_hypergraph_matching_branching_improvement.md`](../../sources/checkpoint-o/explicit_hypergraph_matching_branching_improvement.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
