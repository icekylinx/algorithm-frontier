# Proof map: Scheduling bottleneck commitment

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A commitment/rank-reduction tradeoff for arbitrary-size scheduling.

**Headline bound.** min{2OPT, max{beta(D)OPT+u, a+lambda_k}} with exact D_k and the two-size specialization as stated.

**Model and scope.** The selectable independent commitment, workload bottleneck, and target-cap branches in the proof.

## Complete proof source

[`sources/checkpoint-o/scheduling_bottleneck_commitment_rank_reduction.md`](../../sources/checkpoint-o/scheduling_bottleneck_commitment_rank_reduction.md)

## Proof outline from the source note

- ## 1. Model and a computable bottleneck profile
- ## 2. The contraction promise does not require private units
- ## 3. Committed machines have a separate final load bound
- ## 4. Arbitrarily many smaller sizes
- ## 5. Exactly two sizes: no additive rounding loss
- ## 6. Target search, rank loss and exceptional cases
- ## 7. Relation to the private-slack comparator

## Verification dependencies

- `sources/checkpoint-o/scheduling_bottleneck_commitment_independent_audit.md`
- `sources/checkpoint-o/scheduling_bottleneck_commitment_second_audit.md`
- `sources/checkpoint-o/committed_machine_scheduling_independent_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
