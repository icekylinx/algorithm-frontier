# Proof map: Incremental SCC labels

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** An incremental SCC client with exact component labels under the log-barrier construction.

**Headline bound.** Conditional 4/5-style bound for exact component labels; no topological-order or path-witness claim is added.

**Model and scope.** The directed update model and exact-label interface in the proof; path/topological output is outside this module.

## Complete proof source

[`sources/checkpoint-o/log_barrier_incremental_scc.md`](../../sources/checkpoint-o/log_barrier_incremental_scc.md)

## Proof outline from the source note

- ## 1. Claimed interface and bound
- ## 2. Quotient graph, circulation, and slack offsets
- ## 3. Positive flow certifies a true SCC edge
- ## 4. Potential and the min-ratio query
- ## 5. Detecting a threshold crossing before flow becomes large
- ## 6. Every non-numerical operation is paid by the potential
- ## 7. Explicitly paid contraction implementation

## Verification dependencies

- `sources/checkpoint-o/log_barrier_scc_independent_audit.md`
- `sources/checkpoint-o/transfer_public_baselines.md`
- `sources/checkpoint-o/topological_order_transpose_interface_gap.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
