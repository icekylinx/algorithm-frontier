# Source map

- `# Proof map: Deterministic low-space Subset Sum

A separate uniform deterministic exact algorithm for the same arbitrary signed binary input model, with a proved writable-bit space bound and indexed witness recovery.

**Headline bound.** The bit running time and writable-bit space are

$$
\operatorname{poly}(n,L)2^{n/2}
\quad\text{and}\quad
\operatorname{poly}(n,L)2^{E_Sn},
\qquad E_S=\frac{18261635770550353}{10^{17}}<0.1826163578.
$$

**Model and scope.** The algorithm covers arbitrary signed binary weights, repeated and zero entries, exact decisions, and indexed witnesses. Its time and space guarantee is separate from the faster algorithm.

## Complete proof source

[`sources/subset-sum/low-space/THEOREM.md`](../../sources/subset-sum/low-space/THEOREM.md)

The imported source text is preserved under `sources/subset-sum/`. This proof
map organizes the result and does not combine it with the other Subset Sum
algorithm.

## Verification sources

- `sources/subset-sum/low-space/RESOURCES.md`
- `sources/subset-sum/low-space/LINEAR_COVERS.md`
- `sources/subset-sum/low-space/OWNERSHIP.md`
- `sources/subset-sum/low-space/BIASED_TOP.md`
- `sources/subset-sum/low-space/SIMPLIFICATIONS.md`
- `sources/subset-sum/low-space/current-review.md`
- `sources/subset-sum/verification/check_resources.py`
- `sources/subset-sum/verification/check_structural.py`
- `sources/subset-sum/verification/check_range_identities.py`


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
`
- `sources/subset-sum/low-space/RESOURCES.md`
- `sources/subset-sum/low-space/LINEAR_COVERS.md`
- `sources/subset-sum/low-space/OWNERSHIP.md`
- `sources/subset-sum/low-space/BIASED_TOP.md`
- `sources/subset-sum/low-space/SIMPLIFICATIONS.md`
- `sources/subset-sum/low-space/current-review.md`
- `sources/subset-sum/verification/check_resources.py`
- `sources/subset-sum/verification/check_structural.py`
- `sources/subset-sum/verification/check_range_identities.py`


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
