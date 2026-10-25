# Faster deterministic Subset Sum

| Item | Result |
|---|---|
| **Guarantee** | Exact witness recovery for arbitrary signed binary Subset Sum. |
| **Complexity** | $$C+\mathrm{poly}(n,L)2^{En}$$ with $$E<0.4964618056$$. |
| **Space** | No space exponent is claimed for this algorithm. |
| **Model** | The input is an arbitrary signed binary instance with total encoding length L. The theorem decides feasibility exactly and returns an indexed binary witness on YES instances. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** `sources/subset-sum/combined-proof.md`; verification scripts and reviews are listed in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
