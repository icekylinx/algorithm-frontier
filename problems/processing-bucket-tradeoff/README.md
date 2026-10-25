# Processing-bucket scheduling tradeoff

| Field | Curated statement |
|---|---|
| **Guarantee** | A discrete approximation curve approaches factor three-halves: the first points are two, five-thirds, and eleven-sevenths, followed by the exact bucket sequence in the source. |
| **Objective and output** | Minimize maximum load while keeping all original job bases mandatory and preserving the exact assignment-cost budget; output an integer schedule. |
| **Time** | For bucket depth `k`, the state factor is `(k + 1)` raised to the number of physical machines, times polynomial work in the encoded input and bucket depth. |
| **Space** | Polynomial in the full binary input and bucket state; no unit expansion of binary counts. |
| **Parameters** | `q` is the machine count; `k` is bucket depth; `epsilon` is optional rational accuracy for the limiting comparison; `H` is the complete encoded input plus paid optimization work; `C` is the exact assignment budget. |
| **Model and representation** | Arbitrary nonnegative rational processing times, mandatory recipient-polymatroid bases, eligibility masks, and one exact assignment-cost budget. This tradeoff is separate from the accuracy-scheme and six-profile records. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Internally reviewed research; no formal verification or external peer review is claimed. See the [backlog review](../../reviews/backlog/legacy-result-cards.md) and [review registry](../../reviews/README.md). |
| **Source** | [Arbitrary-processing bucket source](../../sources/checkpoint-q/arbitrary_processing_bucket_scheduling.md) and the verification paths in `sources.md`. |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
