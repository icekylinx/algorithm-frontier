# Proof map: Selected flow with shared setup and routing budget

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Selected flow with one shared setup/routing budget and an attaining minimum-setup selector.

**Headline bound.** Rate at least (1-epsilon)OPT in Gamma(1/epsilon)^c poly(H), with the combined cost satisfied exactly under the stated optimizer interface.

**Model and scope.** Selected splittable flow, setup fees, one shared setup/routing budget, and an exact minimum-setup attaining restriction oracle.

## Complete proof source

[`sources/checkpoint-o/shared_setup_routing_budget_corank_flow.md`](../../sources/checkpoint-o/shared_setup_routing_budget_corank_flow.md)

## Proof outline from the source note

- ## 1. Network, selection and shared cost
- ## 2. The required exact minimum-setup restriction oracle
- ## 3. Comparator and theorem
- ## 4. Residual-budget service regions and their separator
- ## 5. The adaptive fixed-target algorithm
- ## 6. Why an optimal selected set survives
- ## 7. Rational optimization preserves the full accuracy parameter

## Verification dependencies

- `sources/checkpoint-o/shared_setup_routing_budget_independent_audit.md`
- `sources/checkpoint-o/shared_setup_routing_budget_second_audit.md`
- `sources/checkpoint-o/selected_flow_and_global_conversion_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
