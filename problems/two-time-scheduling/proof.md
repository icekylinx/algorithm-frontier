# Proof map: Per-machine two-time scheduling

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** The special two-positive-processing-times-per-machine endpoint from Q.

**Headline bound.** Exact 3/2 in (50/27)^q E(q) poly(H), with the fixed-d base tradeoff stated in Q.

**Model and scope.** Each machine has its own two positive processing times; this is not a global two-value assumption.

## Complete proof source

[`sources/checkpoint-q/per_machine_two_time_costed_scheduling.md`](../../sources/checkpoint-q/per_machine_two_time_costed_scheduling.md)

## Proof outline from the source note

- ## 1. Model and statement
- ## 2. Original totals and fixed-target preprocessing
- ## 3. Easy and small-quota classes
- ## 4. The remaining role ground and its service region
- ## 5. Scaling unequal quotas preserves the omission inequality
- ## 6. One integral recovery for every machine class
- ## 7. All cardinalities, the global cover and optimization

## Verification dependencies

- `sources/checkpoint-q/per_machine_two_time_polymatroid_audit.md`
- `sources/checkpoint-q/unrelated_two_size_scheduling_polymatroid_audit.md`
- `sources/checkpoint-q/scheduling_and_profile_primary_baselines.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
