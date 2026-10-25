# Faster deterministic Subset Sum

| Field | Curated result |
|---|---|
| **Priority** | Tier A: headline time bound |
| **Guarantee** | Exact YES/NO decision and an indexed witness for arbitrary signed binary Subset Sum instances. |
| **Objective and output** | Decide whether a subset reaches the target; on YES, return the selected input indices. Repeated, zero, and negative weights are allowed. |
| **Time** | A polynomial additive term plus polynomial work times two to the power of `E n`, where `E = 149809813343531 / 301754962128739`, approximately `0.4964618056`. |
| **Space** | No separate space exponent is claimed for this record. |
| **Parameters** | `n` is the number of weights. `L` is the full binary encoding length. `C` is the fixed polynomial preprocessing term used by the source theorem. `E` is the exact time exponent. |
| **Representation** | Uniform deterministic bit algorithm over arbitrary signed binary inputs, with exact decision and indexed witness recovery. |
| **Lower-bound type** | No lower bound is claimed by this record. |
| **Review status** | Proof, algorithm, and source reviews are tracked in the [review report](../../reviews/headline/faster-subset-sum.md). Finite checks are evidence for proof components, not formal verification. |
| **Sources** | [Subset Sum proof source](../../sources/subset-sum/combined-proof.md), the [proof map](proof.md), and [verification/review notes](../../sources/subset-sum/reviews/). |

This is a separate time-focused record. It should not be combined with the
low-space card to infer a simultaneous time and writable-space guarantee.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
