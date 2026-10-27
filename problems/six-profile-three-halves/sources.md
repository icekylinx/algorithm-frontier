# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Six profiles suffice for exact factor three halves in arbitrary-time scheduling](proof.md)

## Mathematical dependencies

- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](../processing-bucket-tradeoff/proof.md)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal <code class="math">3/2</code>. General rational coverage, resource feasibility and exact-budget recovery remain symbolic.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
