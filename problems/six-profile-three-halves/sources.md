# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Six profiles suffice for exact factor three halves in arbitrary-time scheduling](proof.md)

## Mathematical dependencies

- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](../processing-bucket-tradeoff/proof.md)

- [General-processing joint recovery and its explicit reference costs](../arbitrary-processing-scheduling/reference-realization.md)

## Executable evidence

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal <code class="math">3/2</code>. This scalar check covers geometry only.

- [Direct original-input six-profile checker](../activated-machine-scheduling/verify/check_six_profiles.py) exercises the reusable `SixBackend`, all six labels, exact interval boundaries and joint recovery against independent original count enumeration.
- [Shared reference and realization proof](../activated-machine-scheduling/reference-realization.md) distinguish the direct six-profile implementation from its activation client and from the fast theorem's paid primitives.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** icekylinx and GPT-6 Astra Pro.
