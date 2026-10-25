# Faster deterministic Subset Sum — checkpoint X draft

**Status: Draft checkpoint X.** This incremental candidate does not replace the reviewed Subset Sum card until the imported proof contract is rechecked.

| Field | Candidate statement |
|---|---|
| **Guarantee** | Exact decision and indexed witness recovery for arbitrary signed-binary Subset Sum with candidate deterministic time exponent `E_new = 158153814247997/318927986919134`, approximately `0.4958919278`. |
| **Objective and output** | Decide whether some subset reaches the target; on YES return the selected input indices. Repeated, zero, and negative weights remain in scope. |
| **Time** | `C_new + poly(n,L) * 2^(E_new*n)` bit operations under the repository Part I circuit compiler, representation lemmas, and exact signed-circuit contracts. The draft changes two circuit families and rebalances the complete cost profile. |
| **Space** | No simultaneous writable-space guarantee is claimed. The separate low-space Subset Sum theorem is not combined with this increment. |
| **Parameters** | `n` is the number of input weights; `L` is full binary encoding length; `C_new` is the finite input-independent circuit-construction cost; `E_new` is the displayed rational exponent. |
| **Model and representation** | Uniform deterministic bit model on arbitrary signed binary inputs with indexed witness recovery. The exact compiler and backend theorem contracts are imported from the pinned repository source. |
| **Lower-bound scope** | No lower bound is claimed. The draft does not advertise an improvement over the randomized `O(2^(0.49n))` catalogue entry; the comparison is to the pinned deterministic repository baseline. |
| **Review status** | Draft checkpoint X. Recompute all contact inequalities and outer cost lines for the revised circuit menu; verify the imported compiler and exact-witness contracts before promotion; formal verification is not claimed. |
| **Source** | [Checkpoint X increment](../../sources/checkpoint-x/02_deterministic_subset_sum_increment.md), with dependencies on the [pinned fast-time proof](../../sources/subset-sum/combined-proof.md). |

This candidate must remain separate from the reviewed faster-time card until the source commit and every changed profile line are re-pinned.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
