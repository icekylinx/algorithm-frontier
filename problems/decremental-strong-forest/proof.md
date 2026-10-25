# Proof map: Decremental strong forest and Gomory-Hu transfer

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A strong decremental forest construction substituted into a public Gomory-Hu reduction.

**Headline bound.** Research 6/7-style update envelope under the stated forest and reduction contracts; no first-publication or independently implemented near-linear Gomory-Hu claim.

**Model and scope.** The exact decremental metric/forest model, fixed-k reduction factors, and external assumptions in the proof.

## Complete proof source

[`sources/checkpoint-o/six_sevenths_strong_forest_and_gomory_hu_checkpoint.md`](../../sources/checkpoint-o/six_sevenths_strong_forest_and_gomory_hu_checkpoint.md)

## Proof outline from the source note

- ## 1. Current result and the fair comparison
- ## 2. Strong decremental SSSP contract
- ## 3. What changes in the construction
- ## 4. The parameter calculation with the necessary separation
- ## 5. Exact deterministic Gomory--Hu trees
- ## 6. Audit resolutions that matter to correctness
- ## 7. What remains open

## Verification dependencies

- `sources/checkpoint-o/separated_metric_forest_and_strong_sssp.md`
- `sources/checkpoint-o/gomory_hu_adapter_independent_audit.md`
- `sources/checkpoint-o/gomory_hu_external_factors_except_fixed_k.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
