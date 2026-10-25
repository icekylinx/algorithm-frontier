# Proof map: Faster deterministic Subset Sum

A uniform deterministic exact algorithm for arbitrary signed binary Subset Sum inputs, including repeated, zero, and negative weights, with indexed witness recovery.

**Headline bound.** The bit running time is

$$
C+\operatorname{poly}(n,L)2^{En},
\qquad E=\frac{149809813343531}{301754962128739}<0.4964618056.
$$

No space exponent is claimed for this algorithm.

**Model and scope.** The input is an arbitrary signed binary instance with total encoding length L. The theorem decides feasibility exactly and returns an indexed binary witness on YES instances.

## Complete proof source

[`sources/subset-sum/combined-proof.md`](../../sources/subset-sum/combined-proof.md)

The imported source text is preserved under `sources/subset-sum/`. This proof
map organizes the result and does not combine it with the other Subset Sum
algorithm.

## Verification sources

- `sources/subset-sum/fast-time/frontier.md`
- `sources/subset-sum/reviews/PROOF_REVIEW.md`
- `sources/subset-sum/verification/check_profile.py`
- `sources/subset-sum/verification/check_fast_costs.py`
- `sources/subset-sum/verification/verify_proof.py`


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
