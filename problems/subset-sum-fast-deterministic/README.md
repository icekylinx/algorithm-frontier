# Faster deterministic Subset Sum

**Current curated result**

A uniform deterministic exact algorithm for arbitrary signed binary Subset Sum inputs, including repeated, zero, and negative weights, with indexed witness recovery.

**Headline bound.** The bit running time is

$$
C+\operatorname{poly}(n,L)2^{En},
\qquad E=\frac{149809813343531}{301754962128739}<0.4964618056.
$$

No space exponent is claimed for this algorithm.

**Model and scope.** The input is an arbitrary signed binary instance with total encoding length L. The theorem decides feasibility exactly and returns an indexed binary witness on YES instances.

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
