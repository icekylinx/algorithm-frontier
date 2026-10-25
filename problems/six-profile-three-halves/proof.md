# Proof map: Six-profile exact three-halves scheduling

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** The current six-profile endpoint for arbitrary unrelated processing profiles.

**Headline bound.** Exact makespan at most 3/2 OPT in 6^q poly(H) time; the base six is not claimed optimal.

**Model and scope.** Arbitrary processing profiles with mandatory original job totals and the exact budget accounting stated in Q.

## Complete proof source

[`sources/checkpoint-q/arbitrary_processing_six_profile_three_halves.md`](../../sources/checkpoint-q/arbitrary_processing_six_profile_three_halves.md)

## Proof outline from the source note

- ## 1. Model and statement
- ## 2. The common cost-preserving rounding interface
- ## 3. Six exact target-T profiles
- ## 4. Every feasible profile LP gives a three-halves schedule
- ## 5. Complete coverage of every full target schedule
- ### 5.1 No additional job above T/4
- ### 5.2 Exactly one additional job above T/4

## Verification dependencies

- `sources/checkpoint-q/arbitrary_processing_six_profile_polymatroid_audit.md`
- `sources/checkpoint-q/arbitrary_processing_scheduling_transfer_audit.md`
- `sources/checkpoint-q/scheduling_and_profile_primary_baselines.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
