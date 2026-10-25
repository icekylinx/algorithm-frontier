# Proof map: Dynamic spanners with recourse tradeoffs

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Two incomparable dynamic-spanner scopes are retained because their recourse guarantees differ.

**Headline bound.** Tracked-terminal flat spanner: 4/5-style envelope with ordinary recourse including insertions. Full-horizon low-recourse spanner: 5/6-style envelope with output recourse n+D and no dependence on insertion count. Both are amortized.

**Model and scope.** Use the exact terminal/recourse model in the selected source; do not compare the two ratios while dropping their different recourse assumptions.

## Complete proof source

[`sources/checkpoint-o/tracked_terminal_flat_spanner_four_fifths.md`](../../sources/checkpoint-o/tracked_terminal_flat_spanner_four_fifths.md)

## Proof outline from the source note

- ## 1. Retained hierarchy and forest family
- ## 2. Track only original-query pivot images
- ### 2.1 Boolean component aggregates
- ## 3. Marks in the flat witness forests
- ### 3.1 Mark-update work and stable lifted handles
- ## 4. Maintain marked Steiner subtrees and expose only short edges
- ## 5. Why every original edge is represented

## Verification dependencies

- `sources/checkpoint-o/tracked_terminal_flat_spanner_root_audit.md`
- `sources/checkpoint-o/tracked_terminal_flat_spanner_independent_audit.md`
- `sources/checkpoint-o/tracked_terminal_spanner_public_flat_comparator_audit.md`
- `sources/checkpoint-o/fully_dynamic_spanner_five_sixths.md`
- `sources/checkpoint-o/fully_dynamic_spanner_independent_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
