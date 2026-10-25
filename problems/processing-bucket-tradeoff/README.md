# Processing-bucket scheduling tradeoff

**Current curated result**

A separate Pareto curve for arbitrary processing profiles, complementing the Q accuracy scheme and six-profile endpoint.

**Headline bound.** For gamma_k=(3*2^k-1)/(2^(k+1)-1), time is (k+1)^q poly(H+k): k=1 gives 5/3 in 2^q, k=2 gives 11/7 in 3^q, and the curve approaches 3/2 with the stated epsilon tradeoff.

**Model and scope.** Arbitrary processing profiles and the exact mandatory-job, budget, and profile assumptions in Q. This parameterized curve is not collapsed into the Q PTAS or six-profile theorem.

**Proof and verification.** The complete original proof remains in [`sources/checkpoint-q/arbitrary_processing_bucket_scheduling.md`](../../sources/checkpoint-q/arbitrary_processing_bucket_scheduling.md). The files in `verify/` are short pointers to unchanged audit notes. This directory records the exact scope and avoids duplicating checkpoint text.

---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
