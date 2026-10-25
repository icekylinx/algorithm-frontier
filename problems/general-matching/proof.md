# Proof map: Exact general-graph matching

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A conditional deterministic exact maximum-cardinality matching composition for arbitrary undirected graphs.

**Headline bound.** The explicit quantitative candidate is O(n+m)+(m_s+1) exp(O((log(m_s+2))^(4/5)(log log(m_s+4))^(1/5))); a separate uniform m^{1+o(1)} assembly is retained as a remark.

**Model and scope.** Arbitrary undirected graphs, loops/parallel records cleaned with original edge identifiers; exact output. The fast bound assumes the named external primitives and raw-backend Contract R.

## Complete proof source

[`sources/checkpoint-o/current_checkpoint/quantitative_matching_4_5_composition.md`](../../sources/checkpoint-o/current_checkpoint/quantitative_matching_4_5_composition.md)

## Proof outline from the source note

- ## 1. The additional primitive and its literal output type
- ### The static normalized-route interface
- ## 2. Actual-size hierarchy and finite local computation
- ## 3. Rounded master parameters and executable caps
- ## 4. Static-base repair and selected-edge recourse
- ## 5. Recursive work, occurrence pools, and full quality
- ## 6. The 4/5 balance

## Verification dependencies

- `sources/checkpoint-o/current_checkpoint/current_results_and_frontier.md`
- `sources/checkpoint-o/current_checkpoint/deterministic_maximum_matching_verifier.md`
- `sources/checkpoint-o/current_checkpoint/classical_matching_optimality_verifier.md`
- `sources/checkpoint-o/current_checkpoint/matching_size_kernel_corollary.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
