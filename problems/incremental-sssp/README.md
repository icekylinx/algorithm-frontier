# Incremental directed SSSP with simple-path reporting

| Item | Result |
|---|---|
| **Guarantee** | Incremental directed SSSP with simple-path reporting. |
| **Complexity** | $$O(n+m)+(n+m)\exp(O(U^{4/5}h^{1/5}+\sqrt{U(h+\log(1/\varepsilon))}))$$ under the stated backend; reporting a path of k edges costs $$O((k+1)\,\mathrm{poly}(\log N))$$. |
| **Model** | Nonnegative incremental directed weights, epsilon<=1/2 and log(1/epsilon)<=cU as stated; candidate raw backend and simple-path reporting contract. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-o/frozen_detector_incremental_sssp.md`](../../sources/checkpoint-o/frozen_detector_incremental_sssp.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
