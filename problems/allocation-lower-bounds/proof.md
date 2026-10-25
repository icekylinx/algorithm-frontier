# Proof map: Allocation and scheduling oracle barriers

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Value-oracle lower bounds and configuration-gap obstructions delimiting the positive results.

**Headline bound.** Strictly below factor 2 allocation and strictly below 3/2 two-size scheduling require the stated hidden-rank value-oracle queries; separate configuration relaxations retain a gap approaching two.

**Model and scope.** Full rank-value-oracle models and the exact aggregate configuration relaxations named in each source; no explicit-input hardness or optimal-base claim is inferred.

## Complete proof source

[`sources/checkpoint-o/recipient_polymatroid_below_two_oracle_barrier.md`](../../sources/checkpoint-o/recipient_polymatroid_below_two_oracle_barrier.md)

## Proof outline from the source note

- ## 1. The rank functions
- ## 2. The hidden basis is the only basis with value two
- ## 3. The oracle transcript lower bound
- ## 4. Scope of the obstruction
- ## 5. A corresponding scheduling barrier below factor three halves
- ## 6. The same bounds hold when parameterized by corank

## Verification dependencies

- `sources/checkpoint-o/recipient_polymatroid_oracle_barrier_independent_audit.md`
- `sources/checkpoint-o/near_two_refined_parameter_zero_oracle_barrier.md`
- `sources/checkpoint-o/full_residual_configuration_gap_two_independent_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
