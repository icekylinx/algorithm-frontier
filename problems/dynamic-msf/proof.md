# Proof map: Dynamic minimum spanning forest baseline

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A public-framework-derived dynamic MSF result retained as a baseline.

**Headline bound.** 2/3 worst-case update envelope under the public pruning/substitution framework; it is not derived from the matching router.

**Model and scope.** The public dynamic MSF model and all pruning assumptions in the source.

## Complete proof source

[`sources/checkpoint-o/dynamic_msf_public_two_thirds_baseline.md`](../../sources/checkpoint-o/dynamic_msf_public_two_thirds_baseline.md)

## Proof outline from the source note

- ## 1. Primary sources and current versions
- ## 2. The formal public reduction separates pruning from decomposition
- ## 3. Modern pruning, isolated vertices, and a short supported period
- ## 4. Deterministic decomposition with the required gamma
- ## 5. Solving the worst-case recurrence
- ## 6. What the October 2026 deamortization reference does and does not supply
- ## 7. Consequences for further work

## Verification dependencies

- `sources/checkpoint-o/dynamic_msf_formal_pruning_substitution_audit.md`
- `sources/checkpoint-o/dynamic_msf_public_baseline_root_audit.md`
- `sources/checkpoint-o/dynamic_spanner_public_baseline_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
