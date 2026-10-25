# Proof map: Many-size workload scheduling

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** An arbitrary-size workload construction with an additive smaller-job term.

**Headline bound.** max{max(3/2,2-1/D)OPT+u, a+lambda_k} under the stated compressed rank/commitment conditions; additive u is retained.

**Model and scope.** Many smaller sizes, large-unit profile and workload polymatroid assumptions in the proof.

## Complete proof source

[`sources/checkpoint-o/many_small_sizes_workload_makespan_transfer.md`](../../sources/checkpoint-o/many_small_sizes_workload_makespan_transfer.md)

## Proof outline from the source note

- ## 1. Model and guarantee
- ## 2. The per-machine form of the public rounding lemma
- ## 3. A fine workload unit with polynomial encoding
- ## 4. Target preprocessing and the rank-h player matroid
- ## 5. The target promise is a large integer quota
- ## 6. Fractional reconstruction followed by paid integral rounding
- ## 7. Optimization and bit complexity

## Verification dependencies

- `sources/checkpoint-o/many_small_sizes_workload_independent_audit.md`
- `sources/checkpoint-o/many_small_sizes_workload_second_audit.md`
- `sources/checkpoint-o/near_equal_large_sizes_bottleneck_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
