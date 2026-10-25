# Proof map: Arbitrary-value allocation scheme

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Checkpoint Q gives an arbitrary-accuracy integer allocation scheme for player-dependent values with an optional actual player basis and one shared setup/assignment budget.

**Headline bound.** Value at least (1-epsilon)OPT in binom(q,r) exp(O(r/epsilon)) poly(H_epsilon) time and polynomial workspace, with the scalar budget exact.

**Model and scope.** Optional actual player basis, arbitrary player-dependent values, integral recipient-polymatroid constraints, binary multiplicities, and one shared setup/assignment budget.

## Complete proof source

[`sources/checkpoint-q/arbitrary_value_profile_allocation_approximation_scheme.md`](../../sources/checkpoint-q/arbitrary_value_profile_allocation_approximation_scheme.md)

## Proof outline from the source note

- ## 1. Original model and accuracy encoding
- ## 2. The theorem and state parameters
- ## 3. Target capping and occupied bins
- ## 4. Profiles and the fixed-basis LP
- ## 5. Full integer targets supply enumerated profiles
- ## 6. Cost-preserving lower-prefix rounding
- ## 7. Big-bin boundaries eliminate the large-value loss

## Verification dependencies

- `sources/checkpoint-q/arbitrary_value_profile_polymatroid_audit.md`
- `sources/checkpoint-q/arbitrary_value_profile_transfer_audit.md`
- `sources/checkpoint-q/arbitrary_accuracy_and_robust_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
