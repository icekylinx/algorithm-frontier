# Proof map: Fully dynamic APSP tradeoff frontier

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A Pareto set of fully dynamic APSP update/stretch points.

**Headline bound.** Retains incomparable research points: update exp(O(U^(11/14))) at stretch exp(O(U^(6/7)h)); update exp(O(U^(3/4)h^(1/2))) at stretch exp(O(U/h)); same-stretch comparison points are recorded separately.

**Model and scope.** The graph update model, stretch definition, and parameter h/U restrictions in the source. No single point is advertised as globally best.

## Complete proof source

[`sources/checkpoint-o/fully_dynamic_apsp_time_stretch_curve.md`](../../sources/checkpoint-o/fully_dynamic_apsp_time_stretch_curve.md)

## Proof outline from the source note

- ## 1. The audited local envelope
- ## 2. A one-parameter tradeoff
- ## 3. Subpolynomial stretch with a 3/4 leading work power
- ## 4. Query paths and finite arithmetic
- ## 5. General physical degrees for a distance oracle
- ## 6. Scope and remaining comparison

## Verification dependencies

- `sources/checkpoint-o/apsp_tradeoff_independent_audit.md`
- `sources/checkpoint-o/same_stretch_apsp_comparison_and_root_audit.md`
- `sources/checkpoint-o/public_apsp_joint_retuning_independent_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
