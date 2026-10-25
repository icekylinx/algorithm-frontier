# Incremental directed SSSP with simple-path reporting

**Current curated result**

A frozen-detector client for incremental directed SSSP with explicit simple-path output.

**Headline bound.** Conditional 4/5-style bound with the stated accuracy log(1/epsilon) term; a reported path of k edges costs O((k+1) poly(log N)).

**Model and scope.** Nonnegative incremental directed weights, epsilon<=1/2 and log(1/epsilon)<=cU as stated; candidate raw backend and simple-path reporting contract.

**Proof and verification.** `proof.md` is the selected proof note. `verify/` contains independent/root audits or a second incomparable source note. These are internal mathematical reviews, not formal verification or external peer review.

**Source.** `sources/checkpoint-q/frozen_detector_incremental_sssp.md` and the verification paths in `sources.md`.

---

**Curated by:** Yilin Liu  
**Signature:** GPT-6 Astra Pro  
**Date:** 2026-10-25  
**Status:** internally reviewed research; no formal verification or external peer review.
