# Proof map: Robust unrelated allocation with common setup

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A scenario-robust additive allocation guarantee for arbitrary unrelated values and a shared setup vector.

**Headline bound.** Robust utility at least max(0,(1-epsilon)FOPT-u) with every scenario budget exact; FOPT keeps a genuine common basis and relaxes only counts.

**Model and scope.** A common actual player basis across explicit scenarios, scenario-adaptive integer assignments, unrelated values, and common setup vector.

## Complete proof source

[`sources/checkpoint-q/robust_unrelated_common_setup_additive.md`](../../sources/checkpoint-q/robust_unrelated_common_setup_additive.md)

## Proof outline from the source note

- ## 1. Model, comparator and theorem
- ## 2. A common setup vector supplies a genuine zero initialization
- ## 3. Exact nonnegative separators for each scenario
- ## 4. Current minimum setup and the intersected region
- ## 5. The same protected basis survives every scenario and omission
- ## 6. All-input corank time and global conversion
- ## 7. A fixed-basis rational comparator removes target-search loss

## Verification dependencies

- `sources/checkpoint-q/robust_unrelated_common_setup_transfer_audit.md`
- `sources/checkpoint-q/robust_unrelated_common_role_obstructions.md`
- `sources/checkpoint-q/arbitrary_accuracy_and_robust_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
