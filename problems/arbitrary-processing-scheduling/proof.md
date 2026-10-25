# Proof map: Arbitrary processing-time scheduling

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Checkpoint Q gives an arbitrary-accuracy schedule for mandatory jobs with machine-dependent processing times and one exact assignment budget.

**Headline bound.** Makespan at most (1+epsilon)OPT in 2^{O(q/epsilon)} poly(H_epsilon) time, preserving all mandatory original totals and the budget exactly.

**Model and scope.** Every original job base is mandatory; processing times and job polymatroid constraints are arbitrary as specified in Q.

## Complete proof source

[`sources/checkpoint-q/arbitrary_processing_profile_approximation_scheme.md`](../../sources/checkpoint-q/arbitrary_processing_profile_approximation_scheme.md)

## Proof outline from the source note

- ## 1. Model and precise theorem
- ## 2. The one joint cost-preserving recovery primitive
- ## 3. The small-group upper-prefix inequality
- ## 4. Exact bins at a positive target
- ## 5. Machine profiles and the fixed-profile LP
- ## 6. One full-total rounding and the (1+epsilon) bound
- ## 7. Every full-T schedule supplies valid profiles

## Verification dependencies

- `sources/checkpoint-q/arbitrary_processing_profile_polymatroid_audit.md`
- `sources/checkpoint-q/arbitrary_processing_profile_transfer_audit.md`
- `sources/checkpoint-q/arbitrary_accuracy_and_robust_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
