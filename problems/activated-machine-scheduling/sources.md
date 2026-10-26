# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Scheduling on an activated matroid basis with one shared budget](proof.md)

## Mathematical dependencies

- [Arbitrary-processing polymatroid scheduling: an exact-budget approximation scheme](../arbitrary-processing-scheduling/proof.md)
- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](../processing-bucket-tradeoff/proof.md)
- [Six profiles suffice for exact factor three halves in arbitrary-time scheduling](../six-profile-three-halves/proof.md)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal 3/2. The k=0 factor-two endpoint, ordered bucket intervals for k=1,...,13, and all 91 exact bucket load identities b_i+2(1-b_(i-1))=gamma_k. Activation and shared-cost recovery are outside this check.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
