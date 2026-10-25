# Activated-machine scheduling

| Item | Result |
|---|---|
| **Guarantee** | Makespan at most `(1+eps)OPT`. |
| **Complexity** | `2^(O(q/eps)) poly(H_eps)` |
| **Model** | Activated actual machine basis, mandatory original jobs, machine-dependent processing, integral polymatroid constraints, and the initialization test in Q. |
| **Status** | internally reviewed research; no formal verification or external peer review. |

The complete proof map, verification pointers, and exact source paths are
listed below. The original proof source is preserved without mathematical
rewriting.

**Source.** [`sources/checkpoint-q/activated_machine_profile_scheduling.md`](../../sources/checkpoint-q/activated_machine_profile_scheduling.md) and the verification paths in `sources.md`.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
