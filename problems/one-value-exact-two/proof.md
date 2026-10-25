# Proof map: One-value exact-factor-two allocation

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Corank-parameterized exact factor-two allocation with arbitrary assignment costs and one exact budget.

**Headline bound.** Exact factor 2 in (27/4)^c poly(H) time and polynomial workspace, where c is the stated player-ground corank; the whole-ground wrapper gives a separate q-parameter result.

**Model and scope.** One common unit value, arbitrary integral recipient polymatroids, an original player-matroid basis, arbitrary assignment costs, one exact budget.

## Complete proof source

[`sources/checkpoint-o/one_value_exact_budget_corank_two_allocation.md`](../../sources/checkpoint-o/one_value_exact_budget_corank_two_allocation.md)

## Proof outline from the source note

- ## 1. Model and theorem
- ## 2. Why original loop deletion and free disposal are safe
- ## 3. The fixed budgeted count-service region
- ## 4. The integer-target service gap
- ## 5. No-loss quota recovery with the exact cost budget
- ## 6. The K=1 gate uses minimum-cost matroid intersection
- ## 7. Complete one-sided integer optimization

## Verification dependencies

- `sources/checkpoint-o/one_value_exact_budget_corank_two_independent_audit.md`
- `sources/checkpoint-o/arbitrary_cost_residual_budget_second_audit.md`
- `sources/checkpoint-o/corank_batch_allocation_scheduling_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
