# Proofs and dependencies

The canonical manuscripts below contain the mathematical arguments. Computational evidence and its limits are recorded separately in [Verification](verify/README.md).

## Canonical manuscripts

- [Scheduling on an activated matroid basis with one shared budget](proof.md)
- [Activation, binary feasibility and exact six-profile realization](reference-realization.md)

## Mathematical dependencies

- [Arbitrary-processing polymatroid scheduling: an exact-budget approximation scheme](../arbitrary-processing-scheduling/proof.md)
- [Arbitrary unrelated processing times: a bucket-label scheduling tradeoff](../processing-bucket-tradeoff/proof.md)
- [Six profiles suffice for exact factor three halves in arbitrary-time scheduling](../six-profile-three-halves/proof.md)
- [Canonical joint plan and original-total reference realization](../arbitrary-processing-scheduling/reference-realization.md)

## Executable evidence

- [Activated adapter and direct six-profile client](reference/activation.py)
  reuse the canonical general-processing joint solver. The activation gate
  itself uses exact binary greedy minimum-cost bases.
- [Independent activation checker](verify/check_activation.py): 72 finite
  instances, 216 exact feasibility checks, 216 optimizations, 1,080 target checks,
  483 active-coordinate solver checks and nine 81-bit-count greedy checks with
  positive-target solvers disabled. The independent oracle uses original
  activation bases, original job schedules and combined setup/assignment costs.
- [Independent direct six-profile checker](verify/check_six_profiles.py): 29
  original SX instances, 145 targets, 29 optimizations, 4,176 fixed profiles,
  2,713 joint recoveries including 857 fractional witnesses, 106 protected
  full-target profile vectors, six unique-profile fixtures and 24 endpoint cases.
  Activation is not used in this direct SX check.

- [verify_profile_certificates.py](../../tools/verify_profile_certificates.py): All 915 nondecreasing positive integer load multisets of total at most 16, including the empty multiset, normalized by 16, fit at least one of the six profiles; the five nontrivial rounded-load sums equal <code class="math">3/2</code>. The <code class="math">k=0</code> factor-two endpoint, ordered bucket intervals for <code class="math">k=1,\ldots,13</code>, and all 91 exact bucket load identities <code class="math">b_i+2(1-b_{i-1})=\gamma_k</code>. Activation and shared-cost recovery are outside this check.

The [verification note](verify/README.md) states which obligations remain symbolic. Import origins and retained notices are recorded in [provenance](../../provenance/README.md).

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
