# Proof map: Robust selected flow across scenarios

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** The selected-flow guarantee with adaptive routing in every explicit scenario.

**Headline bound.** Rate at least (1-epsilon)OPT in every listed scenario in Gamma(1/epsilon)^c poly(H), under the scenario and selection interfaces in the proof.

**Model and scope.** A common selected set, explicit scenarios, scenario-dependent routes, exact capacities and the stated routing constraints. Exact full-rate admission hardness is a separate negative result.

## Complete proof source

[`sources/checkpoint-o/robust_scenario_selected_flow_corank.md`](../../sources/checkpoint-o/robust_scenario_selected_flow_corank.md)

## Proof outline from the source note

- ## 1. Scenario model and adaptive comparator
- ## 2. Intersection of service regions preserves the packing interface
- ## 3. Fixed-set reoptimization and the rational denominator bound
- ## 4. Failure scenarios and the distinction between routing and selection budgets
- ## 5. Exact unit admission encodes Hitting Set without routing budgets
- ## 6. The hardness statement has an exact and explicit scope

## Verification dependencies

- `sources/checkpoint-o/robust_selected_flow_and_hitting_set_independent_audit.md`
- `sources/checkpoint-o/selected_multicommodity_flow_independent_audit.md`
- `sources/checkpoint-o/selected_flow_and_global_conversion_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
