# Proof map: deterministic low-space Subset Sum

This record organizes the complete low-space theorem without rewriting the
imported manuscript. The theorem is a uniform deterministic exact algorithm
for arbitrary signed binary inputs.

## Theorem contract

- **Input:** `n` signed binary weights and a signed binary target, with arbitrary
  repetitions and zero weights.
- **Output:** exact YES/NO decision and an indexed witness on YES instances.
- **Time:** polynomial in `n` and the full binary length `L`, times
  two to the power of `n/2`.
- **Writable space:** polynomial in `n` and `L`, times two to the power of
  `E_S n`, where `E_S = 18261635770550353 / 10^17`.
- **Model:** uniform deterministic bit operations; the space claim counts
  writable bits and keeps the input representation explicit.

## Proof components

The imported proof is split into ownership, linear-cover, biased-top, range,
resource, and simplification components. Each component is linked from the
[low-space source tree](../../sources/subset-sum/low-space/), while this page
records the public theorem contract and its claim boundary.

## Verification boundary

The repository runs finite identity, scalar, structural, and resource checks
where they are available. These checks replay bounded certificates and
arithmetic inequalities. They do **not** constitute formal verification of
the arbitrary-input algorithm, and the catalogue does not upgrade them to
that status.

See the [headline review](../../reviews/headline/low-space-subset-sum.md), the
[proof review source](../../sources/subset-sum/reviews/PROOF_REVIEW.md), and the
[verification notes](../../sources/subset-sum/low-space/current-review.md).

**Status:** internally reviewed research; no formal verification or external
peer review is claimed.

**Attribution.** Yilin Liu · GPT-6 Astra Pro
