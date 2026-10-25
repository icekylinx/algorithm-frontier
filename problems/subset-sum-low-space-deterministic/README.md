# Deterministic low-space Subset Sum

**Current curated result**

A separate uniform deterministic exact algorithm for the same arbitrary signed binary input model, with a proved writable-bit space bound and indexed witness recovery.

**Headline bound.** The bit running time and writable-bit space are

$$
\operatorname{poly}(n,L)2^{n/2}
\quad\text{and}\quad
\operatorname{poly}(n,L)2^{E_Sn},
\qquad E_S=\frac{18261635770550353}{10^{17}}<0.1826163578.
$$

**Model and scope.** The algorithm covers arbitrary signed binary weights, repeated and zero entries, exact decisions, and indexed witnesses. Its time and space guarantee is separate from the faster algorithm.

**Proof and verification.** The complete imported proof is preserved at the
source path in `proof.md`. `verify/` contains source-linked audit and program
pointers. The faster-time and low-space guarantees are separate executions.

**Source boundary.** The imported subset-sum source project is Apache-2.0 with
its original NOTICE and third-party attributions retained in
`sources/subset-sum/licenses/`.

---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
