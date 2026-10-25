# Proof map: Unrelated-value additive allocation

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Player-dependent values with a precise additive guarantee and a one-budget extension.

**Headline bound.** Each selected player receives at least max(0,(1-epsilon)OPT-u_p) in Gamma(1/epsilon)^c poly(H); the exact-budget extension preserves one assignment budget.

**Model and scope.** Player-dependent values, recipient polymatroids, a selected original player basis; additive guarantee only. No unsupported multiplicative claim is made.

## Complete proof source

[`sources/checkpoint-o/unrelated_values_corank_additive_allocation.md`](../../sources/checkpoint-o/unrelated_values_corank_additive_allocation.md)

## Proof outline from the source note

- ## 1. Model, comparators and theorem
- ## 2. A fixed downward fractional utility polytope
- ## 3. Exact nonnegative separation through a small-dimensional LP
- ## 4. A rational service gap on genuine selected bases
- ## 5. Reconstructing the selected fractional allocation
- ## 6. Lower rounding with a different type order at each player
- ## 7. Integer-optimum search with the sharper runtime base

## Verification dependencies

- `sources/checkpoint-o/unrelated_values_corank_independent_audit.md`
- `sources/checkpoint-o/unrelated_values_exact_budget_independent_audit.md`
- `sources/checkpoint-o/unrelated_values_and_exact_budget_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
