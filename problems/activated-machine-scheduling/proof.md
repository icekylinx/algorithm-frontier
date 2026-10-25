# Proof map: Activated-machine scheduling

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** The Q scheme for scheduling with an activated actual machine basis and shared setup/assignment budget.

**Headline bound.** Makespan at most (1+epsilon)OPT in 2^{O(q/epsilon)} poly(H_epsilon), retaining original mandatory machine/job totals and exact scalar budget.

**Model and scope.** Activated actual machine basis, mandatory original jobs, machine-dependent processing, integral polymatroid constraints, and the initialization test in Q.

## Complete proof source

[`sources/checkpoint-q/activated_machine_profile_scheduling.md`](../../sources/checkpoint-q/activated_machine_profile_scheduling.md)

## Proof outline from the source note

- ## 1. Exact model and guarantee
- ## 2. Feasibility cannot be initialized by setup cost alone
- ## 3. Add one inactive label and fix the selected set before rounding
- ## 4. Target search and scope

## Verification dependencies

- `sources/checkpoint-q/activated_machine_profile_allocation_four_audit.md`
- `sources/checkpoint-q/arbitrary_processing_scheduling_transfer_audit.md`
- `sources/checkpoint-q/arbitrary_accuracy_and_robust_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
