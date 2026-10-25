# Proof map: Processing-bucket scheduling tradeoff

A separate Pareto curve for arbitrary processing profiles, complementing the Q accuracy scheme and six-profile endpoint.

**Bound.** For gamma_k=(3*2^k-1)/(2^(k+1)-1), time is (k+1)^q poly(H+k): k=1 gives 5/3 in 2^q, k=2 gives 11/7 in 3^q, and the curve approaches 3/2 with the stated epsilon tradeoff.

**Scope.** Arbitrary processing profiles and the exact mandatory-job, budget, and profile assumptions in Q. This parameterized curve is not collapsed into the Q PTAS or six-profile theorem.

## Complete source

[`sources/checkpoint-q/arbitrary_processing_bucket_scheduling.md`](../../sources/checkpoint-q/arbitrary_processing_bucket_scheduling.md)

The source note is preserved verbatim. Its proof structure and assumptions are not rewritten here.

---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
