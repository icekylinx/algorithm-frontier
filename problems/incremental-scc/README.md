# Incremental SCC labels

| Item | Result |
|---|---|
| **Guarantee** | Exact incremental strongly connected component labels. |
| **Complexity** | $$(n+m)E(N)^{O(1)}\,\mathrm{poly}(U)$$ with $$E(N)=\exp(O(U^{4/5}(\log U)^{1/5}))$$. |
| **Model** | The directed update model and exact-label interface in the proof; path/topological output is outside this module. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** `sources/checkpoint-o/log_barrier_incremental_scc.md` and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
