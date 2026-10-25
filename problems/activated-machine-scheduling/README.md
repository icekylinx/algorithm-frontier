# Activated-machine scheduling

**Current curated result**

The Q scheme for scheduling with an activated actual machine basis and shared setup/assignment budget.

**Headline bound.** Makespan at most (1+epsilon)OPT in 2^{O(q/epsilon)} poly(H_epsilon), retaining original mandatory machine/job totals and exact scalar budget.

**Model and scope.** Activated actual machine basis, mandatory original jobs, machine-dependent processing, integral polymatroid constraints, and the initialization test in Q.

**Proof and verification.** `proof.md` is the selected Q proof note. The files in `verify/` are independent or root audits from the supplied checkpoints; they are not formal verification or peer review.

**Parameter note.** The Q schemes are accuracy-dependent exponential algorithms. Earlier P/O bounds remain available where their parameterization or comparator is incomparable.

**Source.** `sources/checkpoint-q/activated_machine_profile_scheduling.md` and the verification paths in `sources.md`.

---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
