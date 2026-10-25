# Arbitrary processing-time scheduling

**Current curated result**

Checkpoint Q gives an arbitrary-accuracy schedule for mandatory jobs with machine-dependent processing times and one exact assignment budget.

**Headline bound.** Makespan at most (1+epsilon)OPT in 2^{O(q/epsilon)} poly(H_epsilon) time, preserving all mandatory original totals and the budget exactly.

**Model and scope.** Every original job base is mandatory; processing times and job polymatroid constraints are arbitrary as specified in Q.

**Proof and verification.** `proof.md` is the selected Q proof note. The files in `verify/` are independent or root audits from the supplied checkpoints; they are not formal verification or peer review.

**Parameter note.** The Q schemes are accuracy-dependent exponential algorithms. Earlier P/O bounds remain available where their parameterization or comparator is incomparable.

**Source.** `sources/checkpoint-q/arbitrary_processing_profile_approximation_scheme.md` and the verification paths in `sources.md`.

---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
