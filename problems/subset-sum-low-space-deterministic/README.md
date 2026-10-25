# Deterministic low-space Subset Sum

| Field | Curated result |
|---|---|
| **Priority** | Tier A: headline resource tradeoff |
| **Guarantee** | Exact YES/NO decision and an indexed witness for arbitrary signed binary Subset Sum instances. |
| **Objective and output** | Decide whether a subset reaches the target; on YES, return the selected input indices. Repeated, zero, and negative weights are allowed. |
| **Time** | Polynomial in the input bit length, multiplied by two to the power of one half of the item count. |
| **Space** | Writable space is polynomial in `L` times `2^(E_S n)`; read-only input storage is excluded. |
| **Writable space** | Polynomial in the input bit length, multiplied by two to the power of `E_S` times the item count. The exact exponent is `E_S = 18261635770550353 / 10^17 = 0.18261635770550353`; the older `137/750` value is a weaker implied bound. |
| **Parameters** | `n` is the number of weights. `L` is the full binary encoding length of all weights and the target, including signs and delimiters. `E_S` is the writable-space exponent. |
| **Model and representation** | Uniform deterministic bit model; the space row counts writable bits only. |
| **Lower-bound scope** | No lower bound is claimed. |
| **Review status** | Proof, algorithm, and source reviews are tracked in the [review report](../../reviews/headline/low-space-subset-sum.md). Finite certificate replay is recorded separately and is not formal verification. |
| **Source** | [Curated proof map](proof.md), [low-space theorem source](../../sources/subset-sum/low-space/THEOREM.md), and the [source map](sources.md). |

**Finite contract check.** [`tools/verify_subset_sum_certificates.py`](../../tools/verify_subset_sum_certificates.py) exhaustively replays small signed instances and indexed witnesses; it does not verify the asymptotic algorithm.

This result is a separate time/space point from the faster-time Subset Sum
record. The two cards should not be read as a simultaneous combined bound.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
