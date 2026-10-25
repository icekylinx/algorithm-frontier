# Deterministic low-space Subset Sum

| Item | Result |
|---|---|
| **Guarantee** | Exact witness recovery for arbitrary signed binary Subset Sum. |
| **Complexity** | Time `poly(n,L)2^(n/2)` and writable space `poly(n,L)2^(E_Sn)` with `E_S<0.1826163578`. |
| **Scope** | This time/space guarantee is a separate algorithm and is not claimed simultaneously with the faster-time result. |
| **Model** | The algorithm covers arbitrary signed binary weights, repeated and zero entries, exact decisions, and indexed witnesses. Its time and space guarantee is separate from the faster algorithm. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/subset-sum/low-space/THEOREM.md`](../../sources/subset-sum/low-space/THEOREM.md); verification scripts and reviews are listed in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
