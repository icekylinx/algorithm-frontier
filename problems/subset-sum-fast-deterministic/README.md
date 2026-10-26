# Deterministic Subset Sum: time bound

**Objective and output**

Exact YES/NO decision and the selected input indices. Arbitrary signed binary integers, zeros and repeated weights are allowed.

**Randomness**

Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery and input-independent deterministic circuit construction; no probability of error.

**Time**

<code class="math">C+\mathrm{poly}(n,L)2^{0.495836n}</code> bit operations. The [proof](proof.md)
gives the slightly smaller exact rational exponent.

**Space**

No separate writable-space exponent is asserted for this algorithm.

**Parameters**

<code class="math">n</code> is the item count; <code class="math">L</code> is the complete binary input length; <code class="math">C</code> is a finite input-independent circuit-construction cost, with no practical bound claimed.

**Model and representation**

Uniform deterministic bit operations and indexed witness recovery. Polynomial degrees are fixed.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

**Ready for review in the stated scope.** Part II parameter composition: the generalized second lookup, its exact 62-branch replay and 44-branch compatibility, the finite-volume cone lemma and compiler allowance, the continuous reflected-profile envelope, and all nine outer cost rates. The scalar tuple was independently recalculated.

**Conditions and remaining work.** The arbitrary-input signed-circuit compiler and witness reduction remain mathematical manuscript proofs; the numerical certificates do not formalize them. The deterministic startup constant is finite and input-independent but has no practical numerical bound.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Theorems and complete composition proof](proof.md), [provenance and verification scope](sources.md).

## Numerical certificates

The [continuous-domain checker](../../tools/verify_subset_sum_contacts.py)
reconstructs all 62 branches of the refined contact menu, including the
new second-lookup fraction `14/25`. Its complete run
accepted 248,189 rationally bounded leaves and proved the two empty recursive
domains. The [scalar checker](../../tools/verify_subset_sum_scalars.py)
then checks all 160 endpoint comparisons for the continuous contact/chord/cone
envelope and every outer running-time inequality.
The [verification note](verify/README.md) explains the acceptance proof,
the exact scopes of the programs, and the [full-run receipt](verify/receipt.json).

The older baseline exponent
<code class="math">149809813343531/301754962128739&lt;0.4964618056</code> is retained as a background
conditional composition with its own historical contact premise. The refined
theorem above uses the newly reconstructed menu directly and does not depend
on an older contact receipt.

The time-focused algorithm and the [low-space algorithm](../subset-sum-low-space-deterministic/) are separate constructions with separate resource guarantees.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
