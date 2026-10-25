# Proof map: Two-size makespan scheduling

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** The strongest two-size scheduling regimes are retained by parameter: global/corank exact 3/2 and large-unit 5/3 are incomparable.

**Headline bound.** Exact 3/2 in (27/4)^c poly(H) and in the whole-ground Q conversion; a separate 5/3 scheme uses 2^{O(h)} for h large units.

**Model and scope.** Arbitrary integral job polymatroids with two sizes; q/c/h are different parameters and no one regime is silently substituted for another.

## Complete proof source

[`sources/checkpoint-o/two_size_makespan_corank_three_halves_transfer.md`](../../sources/checkpoint-o/two_size_makespan_corank_three_halves_transfer.md)

## Proof outline from the source note

- ## 1. Scheduling model and parameter
- ## 2. Empty classes and the Boolean-rank failure branch
- ## 3. A one-sided target procedure
- ## 4. The integer quota supplied by a feasible target
- ## 5. Zero extension, base completion, and the exact load bound
- ## 6. Target search without a monotone success assumption
- ## 7. Total complexity and special cases

## Verification dependencies

- `sources/checkpoint-o/corank_quota_and_three_halves_independent_audit.md`
- `sources/checkpoint-o/corank_batch_allocation_scheduling_root_audit.md`
- `sources/checkpoint-o/two_size_makespan_large_rank_independent_audit.md`
- `sources/checkpoint-o/two_size_makespan_few_large_jobs_transfer.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
