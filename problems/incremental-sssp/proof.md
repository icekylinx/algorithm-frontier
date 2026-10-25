# Proof map: Incremental directed SSSP with simple-path reporting

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A frozen-detector client for incremental directed SSSP with explicit simple-path output.

**Headline bound.** Conditional 4/5-style bound with the stated accuracy log(1/epsilon) term; a reported path of k edges costs O((k+1) poly(log N)).

**Model and scope.** Nonnegative incremental directed weights, epsilon<=1/2 and log(1/epsilon)<=cU as stated; candidate raw backend and simple-path reporting contract.

## Complete proof source

[`sources/checkpoint-o/frozen_detector_incremental_sssp.md`](../../sources/checkpoint-o/frozen_detector_incremental_sssp.md)

## Proof outline from the source note

- ## 1. Quantitative statement
- ## 2. The single-lifetime detector interface
- ## 3. Root reachability and the meaning of a local graph
- ## 4. Normalized detectors, degree weights, and births
- ## 5. The projected child and its accuracy
- ## 6. A child-size quota pays edges inserted after promotions
- ## 7. Sound-stop phase counts with changing degree demands

## Verification dependencies

- `sources/checkpoint-o/frozen_sssp_outer_independent_audit.md`
- `sources/checkpoint-o/frozen_barrier_detector_independent_audit.md`
- `sources/checkpoint-o/simple_path_reporting_from_tree_segments.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
