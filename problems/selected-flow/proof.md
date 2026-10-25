# Proof map: Selected splittable concurrent flow

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** Corank-parameterized selected flow with exact capacities, routing budgets, and rational comparator recovery.

**Headline bound.** Rate at least (1-epsilon)OPT in Gamma(1/epsilon)^c poly(H), with exact permitted-set selection and exact routing constraints.

**Model and scope.** Directed or undirected splittable concurrent flow; restriction-selectable exact r-set, explicit nonnegative routing budgets, and rational input as specified.

## Complete proof source

[`sources/checkpoint-o/selected_multicommodity_flow_corank_scheme.md`](../../sources/checkpoint-o/selected_multicommodity_flow_corank_scheme.md)

## Proof outline from the source note

- ## 1. Model and comparators
- ## 2. A fixed downward service region
- ## 3. Nonnegative packing rows from arc potentials
- ## 4. Exact separation with a finite bounded LP
- ## 5. The fixed-target corank gap
- ## 6. Detecting zero optimum and constructing a positive scale
- ## 7. Rational comparator recovery gives the sharper exponent

## Verification dependencies

- `sources/checkpoint-o/selected_multicommodity_flow_independent_audit.md`
- `sources/checkpoint-o/rational_comparator_gap_independent_audit.md`
- `sources/checkpoint-o/selected_flow_and_global_conversion_root_audit.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
