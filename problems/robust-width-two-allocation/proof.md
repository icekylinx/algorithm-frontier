# Proof map: Robust width-two allocation

This file is the concise proof index for the curated result. It keeps the
problem directory readable while preserving the complete original proof note
at the source path below. The original source text is not rewritten.

**Claim summary.** A sharper exact robust positivity gate under width-two minimal obstructions.

**Headline bound.** phi^c poly(H) time, with phi=(1+sqrt(5))/2, and whole-ground base ((5-sqrt(5))/2)^q E(q) under the stated promise; outside the promise the algorithm returns an explicit violation.

**Model and scope.** One common actual player basis across explicit scenarios; all inclusion-minimal one-unit obstructions have width at most two.

## Complete proof source

[`sources/checkpoint-q/robust_unit_width_two_fibonacci_gate.md`](../../sources/checkpoint-q/robust_unit_width_two_fibonacci_gate.md)

## Proof outline from the source note

- ## 1. Model, promise and guarantees
- ## 2. Building the complete singleton/pair conflict graph
- ## 3. Passing to the dual basis and forced omissions
- ## 4. The matching terminal case is polynomial
- ## 5. Degree branching with matroid constraints retained
- ## 6. Full Fibonacci running time and polynomial space
- ## 7. Final unit recovery and the all-input guard

## Verification dependencies

- `sources/checkpoint-q/robust_unit_width_two_fibonacci_transfer_audit.md`
- `sources/checkpoint-q/robust_unit_bounded_certificate_transfer_audit.md`
- `sources/checkpoint-q/robust_unit_allocation_whole_ground_oracle_barrier.md`

The verification files in this directory point to the unchanged audit notes in
`sources/`. They are audit pointers and summaries, not formal proof checkers.


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
