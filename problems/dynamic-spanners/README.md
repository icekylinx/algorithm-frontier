# Dynamic spanners with recourse tradeoffs

| Item | Result |
|---|---|
| **Guarantee** | Dynamic spanner stretch and recourse guarantees. |
| **Complexity** | Tracked-terminal scope: `exp(O(U^(4/5)h^(1/5)))` stretch, work, and recourse envelope; full-horizon low-recourse scope: `exp(O(U^(5/6)h^(1/6)))` stretch/work, with output recourse `(n+D)exp(O(U^(5/6)h^(1/6)))`. |
| **Model** | Use the exact terminal/recourse model in the selected source; do not compare the two ratios while dropping their different recourse assumptions. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-o/tracked_terminal_flat_spanner_four_fifths.md`](../../sources/checkpoint-o/tracked_terminal_flat_spanner_four_fifths.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
