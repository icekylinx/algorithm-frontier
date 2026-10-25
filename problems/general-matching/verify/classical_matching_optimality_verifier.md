# Verification pointer

**Role:** independent/root audit or source comparison  
**Original audit source:** [`sources/checkpoint-o/current_checkpoint/classical_matching_optimality_verifier.md`](../../../sources/checkpoint-o/current_checkpoint/classical_matching_optimality_verifier.md)

The complete audit text is preserved at the linked source path. This file is a
short verification index so the problem directory does not duplicate the same
checkpoint note. The source is unchanged.

**Audit outline:**
- # A classical independent optimality verifier for general matching
- ## 1. Starting from an arbitrary proposed matching
- ## 2. A conservative near-linear implementation
- ## 3. Use after shared preprocessing

**Audit excerpt:** The final matching check can use a pre-2026 algorithm independently of the newer simplified implementation. The relevant primary source is Harold N. Gabow, [The Weighted Matching Approach to Maximum Cardinality Matching, arXiv:1703.03998v1](https://arxiv.org/abs/1703.03998v1), 2017. Figures 1–2 give the first search and its no-augmenting-path outcome; Sections 3 and 5 provide its correctness and implementation. Section 5 uses the incremental-tree set-union algorithm of Gabow and Tarjan, [A Linea


---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
