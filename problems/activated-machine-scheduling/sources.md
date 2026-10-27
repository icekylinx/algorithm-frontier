# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Scheduling on an activated matroid basis with one shared budget](proof.md)

## Mathematical dependencies

- [Arbitrary-processing polymatroid scheduling: an exact-budget approximation scheme](../arbitrary-processing-scheduling/proof.md)
- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](../processing-bucket-tradeoff/proof.md)
- [Six profiles suffice for exact factor three halves in arbitrary-time scheduling](../six-profile-three-halves/proof.md)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal <code class="math">3/2</code>. The <code class="math">k=0</code> factor-two endpoint, ordered bucket intervals for <code class="math">k=1,\ldots,13</code>, and all 91 exact bucket load identities <code class="math">b_i+2(1-b_{i-1})=\gamma_k</code>. Activation and shared-cost recovery are outside this check.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
