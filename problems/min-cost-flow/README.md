# Static and threshold min-cost flow

| Item | Result |
|---|---|
| **Guarantee** | Exact static min-cost flow and fixed-threshold witness recovery. |
| **Complexity** | $$O(n+m)+(m+1)\exp(O((\log(m+2))^{4/5}(\log\log(m+4))^{1/5}))$$, conditional on the raw backend; the proof also records the explicit $$E^4$$ numerical term. |
| **Model** | Static exact min-cost flow and fixed-threshold crossing with the explicit feasibility and numerical interfaces in the proof. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-o/moving_box_log_barrier_flow.md`](../../sources/checkpoint-o/moving_box_log_barrier_flow.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
