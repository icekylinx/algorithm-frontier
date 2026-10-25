# Proof map: Static and threshold min-cost flow

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** An exact static min-cost flow/threshold feasibility construction with witness recovery and a fixed-threshold incremental client.

**Headline bound.** Conditional raw-backend bound with the E^4 numerical term and exact acceptance/recovery; it is not a generic dynamic maintenance theorem for every optimum.

**Model and scope.** Static exact min-cost flow and fixed-threshold crossing with the explicit feasibility and numerical interfaces in the proof.

## Complete proof source

[`sources/checkpoint-o/moving_box_log_barrier_flow.md`](../../sources/checkpoint-o/moving_box_log_barrier_flow.md)

## Proof outline from the source note

- ## 1. Statement and input conventions
- ### Raw backend assumption
- ## 2. Parameters and the expanded box
- ## 3. A pure logarithmic potential and a strong direction
- ## 4. Frozen cost gaps and coordinate anchors
- ## 5. Integer prices, ports, and the LOW test
- ## 6. Additional cost aggregates and atomic transactions

## Verification dependencies

- `sources/checkpoint-o/moving_box_log_barrier_independent_audit.md`
- `sources/checkpoint-o/moving_pad_min_cost_flow_audit.md`
- `sources/checkpoint-o/exact_flow_acceptance_and_reductions.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
