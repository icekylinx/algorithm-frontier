# Proof map: Whole-ground allocation and scheduling transfers

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Exact factor 2 for one-value allocation and compulsory two-value allocation, plus the fixed-R intrinsic-value tradeoff, after whole-ground conversion.

**Headline bound.** For A=27/4, time T_A(q,H)=(50/27)^(q+o(q)) poly(H) and exact factor 2 in the one-value and compulsory two-value rows. For intrinsic values, factor 2R/(R-1) in Gamma(R)^(q+o(q)) poly(H).

**Model and scope.** Original player matroid, arbitrary assignment costs, one exact budget; the intrinsic-value row uses common value types and the exact scope in the proof.

## Complete proof source

[`sources/checkpoint-o/global_exponential_allocation_flow_transfers.md`](../../sources/checkpoint-o/global_exponential_allocation_flow_transfers.md)

## Proof outline from the source note

- ## 1. Models, time notation, and main guarantees
- ## 2. The precise forced-omission wrapper
- ## 3. One-value arbitrary-cost allocation: exact factor two
- ## 4. Compulsory two-value arbitrary-cost allocation: exact factor two
- ## 5. General intrinsic values and arbitrary costs: no support promise
- ## 6. Two-size scheduling: exact three halves on every instance
- ## 7. Selected concurrent flow and explicit robust scenarios

## Verification dependencies

- `sources/checkpoint-o/global_exponential_allocation_flow_independent_audit.md`
- `sources/checkpoint-o/polynomial_space_global_gap_independent_audit.md`
- `sources/checkpoint-o/selected_flow_and_global_conversion_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
