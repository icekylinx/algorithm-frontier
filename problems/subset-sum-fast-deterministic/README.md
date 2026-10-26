# Deterministic Subset Sum: time bound

**Objective and output**

Exact YES/NO decision and the selected input indices. Arbitrary signed binary integers, zeros and repeated weights are allowed.

**Randomness**

Deterministic exact algorithm in the uniform bit model, including indexed-witness recovery and input-independent deterministic circuit construction; no probability of error.

**Time**

<code class="math">C+\mathrm{poly}(n,L)2^{0.495748n}</code> bit operations. The exact
exponent is `E_3=158153814247997/319021177919134`; [Theorem F3](proof.md#theorem-and-proof-structure)
proves this bound. A
[deterministic baseline cap](proof.md#a-deterministic-baseline-cap) also
bounds each instance by ordinary meet-in-the-middle time.

**Space**

No separate writable-space exponent is asserted for this algorithm.

**Parameters**

<code class="math">n</code> is the item count; <code class="math">L</code> is the complete binary input length; <code class="math">C</code> is a finite input-independent circuit-construction cost, with no practical bound claimed.

**Model and representation**

Uniform deterministic bit operations and indexed witness recovery. Polynomial degrees are fixed.

**Lower-bound scope**

No lower bound is claimed.

**Review status**

**Ready for review.** The complete uniform deterministic integer Subset Sum and indexed-witness construction in Parts I–III: signed circuit compilation, finite exact seed search, trace aggregation, all inherited reductions, the preserved two-level result and the third-lookup extension. The final-source 62-branch and 16-branch evidence, finite contact-cone lemma, exact reflected envelope and all nine outer cost rates are separately accounted for.

**Conditions and remaining work.** The finite input-independent startup constant has no practical numerical bound. Mathematical compiler proofs and exact continuous certificates have different scopes; neither is described as proof-assistant formalization or as a practical implementation of the compiled algorithm. The historical 18-contact presentation retains its explicitly stated numerical evidence boundary. The current 62-plus-16-branch theorem uses its own complete contact evidence and does not depend on that historical receipt.

The [verification note](verify/README.md) identifies executable coverage. This status does not claim external peer review or proof-assistant verification.

**Source**

[Theorems and complete composition proof](proof.md), [provenance and verification scope](sources.md).

## Numerical certificates

The [third-lookup checker](../../tools/verify_subset_sum_third_contacts.py)
has a source-bound [16-branch receipt](verify/third_receipt.json): 317,138
accepted leaves and four empty leaves in the completed resumable replay.
The [base checker](../../tools/verify_subset_sum_contacts.py) retains all 62
branches and its separate [receipt](verify/receipt.json), with 248,189
accepted leaves and two empty recursive domains. The
[scalar checker](../../tools/verify_subset_sum_scalars.py) combines both
menus, checks 112 reflected-profile comparisons and every outer cost.
Its `--base-two-level` mode independently preserves the 160-comparison F2
ledger and `E_2=158153814247997/318964058919134`.
The [verification note](verify/README.md) explains the acceptance proof,
the scope of each program, and clean replay versus stored-receipt binding.

The older baseline exponent
<code class="math">149809813343531/301754962128739&lt;0.4964618056</code> is retained as a background
conditional composition with its own historical contact premise. The refined
theorem above uses the newly reconstructed menu directly and does not depend
on an older contact receipt.

The time-focused algorithm and the [low-space algorithm](../subset-sum-low-space-deterministic/) are separate constructions with separate resource guarantees.

**Attribution:** Yilin Liu and GPT-6 Astra Pro.
