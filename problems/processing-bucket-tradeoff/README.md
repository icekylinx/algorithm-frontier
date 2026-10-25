# Processing-bucket scheduling tradeoff

| Item | Result |
|---|---|
| **Guarantee** | The profile curve includes 5/3, 11/7, and the approach to 3/2. |
| **Complexity** | $$ (k+1)^q\,\mathrm{poly}(H+k) $$ with $$\gamma_k=(3\cdot2^k-1)/(2^{k+1}-1)$$. |
| **Model** | Arbitrary processing profiles and the exact mandatory-job, budget, and profile assumptions in Q. This parameterized curve is not collapsed into the Q PTAS or six-profile theorem. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-q/arbitrary_processing_bucket_scheduling.md`](../../sources/checkpoint-q/arbitrary_processing_bucket_scheduling.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
