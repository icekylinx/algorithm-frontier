# Weighted-prefix, laminar, and sparse-quota frontier

This is a Tier A record for ordered prefix geometry, laminar root caps, sparse mixed quotas, and deterministic ground kernels. It is kept separate from the numeric-target/support-pattern family because its controlling parameters are different.

| Field | Curated statement |
|---|---|
| **Guarantee** | Exact deterministic target feasibility and signed-scalar optimization for ordered quota systems, bounded-family weights, laminar caps, sparse mixed quotas, and the named deterministic kernel reductions. |
| **Objective and output** | Decide target feasibility or optimize the stated scalar objective under ordered prefixes, laminar caps, sparse mixed quotas, and kernel interfaces. |
| **Time** | One order: `2^(O(B))`; two orders: `2^(O(B log(B+2)))`; support count `C`: `2^(O(sqrt(B min{C,B})))` for one order and `2^(O(min{sqrt(BC), B log(2+min{C/B,B})}))` for two orders; `p` shared families: `2^(O(pB log(p+2)))`; laminar root cap: `2^(O(B^2 log(B+1)))`, all times `poly(H)`. |
| **End-to-end algorithms** | T retains one-order, two-order, multi-family, and laminar-cap algorithms. U retains sparse mixed-quota and laminar algorithms. Their complexity factors are reported against the binary caps rather than an expanded unit instance. |
| **Deterministic kernel outputs** | Separate ground-kernel rows retain sparse packing of order k to the power 2-delta-plus-1, coverable-matroid kernels of size k times d factorial times the d-th power of k times one plus the sum of the g-values, transversal kernels of order k to the power 2-d-plus-1, and graph-matching kernels of order k to the fourth power (or k to the fifth power for parallel-edge handling). |
| **Space** | Uniform polynomial binary workspace in the stated oracle or readable-program model. No binary cap is expanded into unit capacity. |
| **Model and representation** | One global normalized monotone integral polymatroid with exact rank access; optional or mandatory vectors are stated per row. |
| **Parameters** | **B** is the maximum target or root cap; **B0** is the distinguished root cap; **Delta** is at least 1 and bounds positive nonroot incidences per column; **p** counts shared weight families; **H** includes the full binary input and paid polynomial primitive work. The common coordinate order is shared across rows. A root cap is imposed by **B0**, the maximum cap is **B**, positive root charge is required where stated, and coordinates that are zero at the root are zero in every other row. The original completion oracle is retained. |
| **Lower-bound scope** | T records one-order, two-order, support-budget, multi-family, row-dependent, and laminar boundaries. U adds the frequency-one disjoint-row lower bound of 2 to the power Omega of B log B and separate deterministic ground-kernel boundaries. Oracle-query and readable-program ETH consequences remain distinct. |
| **Review status** | Internal proof, algorithm, and source review is tracked in the [headline review report](../../reviews/headline/weighted-prefix-quota-frontier.md). Finite replay checks are evidence for the listed statements; they are not formal verification. |

Read the [proof map](proof.md), [source map](sources.md), [complexity guide](../../docs/COMPLEXITY.md), and [complete index](../../CONTENTS.md) for the detailed rows and provenance.

| **Source** | [Checkpoint T](../../sources/checkpoint-t/CHECKPOINT_T_INCREMENT.md) and [Checkpoint U](../../sources/checkpoint-u/CHECKPOINT_U_INCREMENT.md). |

**Attribution.** Yilin Liu · GPT-6 Astra Pro
