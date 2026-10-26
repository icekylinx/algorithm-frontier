# Deterministic Subset Sum: time bound

**Objective and output**

Exact YES/NO decision and the selected input indices. Arbitrary signed binary integers, zeros and repeated weights are allowed.

**Randomness**

Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery and input-independent deterministic circuit construction; no probability of error.

**Time**

$C+\mathrm{poly}(n,L)2^{En}$, where $E=158153814247997/318927986919134\approx0.4958919277538907<0.495892$.

**Space**

No separate writable-space exponent is asserted for this algorithm.

**Parameters**

$n$ is the item count; $L$ is the complete binary input length; $C$ is a finite input-independent circuit-construction cost, with no practical bound claimed.

**Model and representation**

Uniform deterministic bit operations and indexed witness recovery. Polynomial degrees are fixed.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

Mathematical proof with computer-assisted numerical certification: all 44 continuous-domain branches pass exact rational verification, followed by 104 reflected-profile comparisons and the complete outer cost ledger. The circuit and reduction arguments are mathematical proofs; no machine-checked formalization is claimed.

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
$149809813343531/301754962128739<0.4964618056$ is retained as a background
conditional composition with its own historical contact premise. The refined
theorem above uses the newly reconstructed menu directly and does not depend
on an older contact receipt.

The time-focused algorithm and the [low-space algorithm](../subset-sum-low-space-deterministic/) are separate constructions with separate resource guarantees.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
