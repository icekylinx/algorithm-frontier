# Deterministic Subset Sum: time bound

**Objective and output**

Exact YES/NO decision and the selected input indices. Arbitrary signed binary integers, zeros and repeated weights are allowed.

**Randomness**

Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery and input-independent deterministic circuit construction; no probability of error.

**Time**

$`C+\mathrm{poly}(n,L)2^{En}`$, where $`E=158153814247997/318928754919134\approx0.4958907336157183<0.495891`$.

**Space**

No separate writable-space exponent is asserted for this algorithm.

**Parameters**

$`n`$ is the item count; $`L`$ is the complete binary input length; $`C`$ is a finite input-independent circuit-construction cost, with no practical bound claimed.

**Model and representation**

Uniform deterministic bit operations and indexed witness recovery. Polynomial degrees are fixed.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

**Ready for review in the stated scope.** The refined parameter and compiler-allowance update in Part II, Sections 6–7: the retyped initial difference-table bound, exact reflected-profile budget, and all nine outer cost rates. The new scalar tuple was independently recalculated against the existing compiler lemmas.

**Conditions and remaining work.** The arbitrary-input signed-circuit compiler and witness reduction remain mathematical manuscript proofs; the numerical certificates do not formalize them. The deterministic startup constant is finite and input-independent but has no practical numerical bound.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Theorems and complete composition proof](proof.md), [provenance and verification scope](sources.md).

## Numerical certificates

The [continuous-domain checker](../../tools/verify_subset_sum_contacts.py)
reconstructs every branch of the refined contact menu. Its complete run
accepted 188,227 rationally bounded leaves and proved the two empty recursive
domains. The [scalar checker](../../tools/verify_subset_sum_scalars.py)
then verifies the reflected profile and every outer running-time inequality.
The [verification note](verify/README.md) explains the acceptance proof,
the exact scopes of the three programs, and the [full-run receipt](verify/receipt.json).

The older baseline exponent
$`149809813343531/301754962128739<0.4964618056`$ is retained as a background
conditional composition with its own historical contact premise. The refined
theorem above uses the newly reconstructed menu directly and does not depend
on an older contact receipt.

The time-focused algorithm and the [low-space algorithm](../subset-sum-low-space-deterministic/) are separate constructions with separate resource guarantees.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
