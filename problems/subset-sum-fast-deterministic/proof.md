# Proof map: faster deterministic Subset Sum

This page gives the public claim contract for the faster-time Subset Sum
algorithm and points to the preserved proof source.

## Theorem contract

- **Input:** arbitrary signed binary weights and a signed binary target.
- **Output:** exact YES/NO decision and indexed witness recovery on YES.
- **Time:** polynomial preprocessing plus polynomial work times two to the
  power of `E n`, with `E = 149809813343531 / 301754962128739`.
- **Space:** no independent exponent is asserted.
- **Parameters:** `n` counts weights, `L` is total binary input length, and
  `C` denotes the fixed polynomial preprocessing term in the source theorem.

## Source and review boundary

The complete argument remains in [combined-proof.md](../../sources/subset-sum/combined-proof.md).
The repository review distinguishes proof structure, algorithmic cost
accounting, source/provenance checks, and finite replay. A finite replay is
not formal verification of the full arbitrary-input algorithm.

See the [headline review](../../reviews/headline/faster-subset-sum.md) and the
[subset-sum review directory](../../sources/subset-sum/reviews/).

**Attribution.** Yilin Liu · GPT-6 Astra Pro
