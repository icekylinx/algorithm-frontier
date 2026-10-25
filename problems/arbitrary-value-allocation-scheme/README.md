# Arbitrary-value allocation scheme

| Item | Result |
|---|---|
| **Guarantee** | Value at least `(1-eps)OPT`. |
| **Complexity** | `binom(q, r)exp(O(r/eps)) poly(H_eps)` |
| **Model** | Optional actual player basis, arbitrary player-dependent values, integral recipient-polymatroid constraints, binary multiplicities, and one shared setup/assignment budget. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-q/arbitrary_value_profile_allocation_approximation_scheme.md`](../../sources/checkpoint-q/arbitrary_value_profile_allocation_approximation_scheme.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
