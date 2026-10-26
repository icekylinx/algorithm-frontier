# Proof dependencies and source map

## Two separate guarantees

[Theorem 2](proof.md#abstract-and-theorem) gives the general deterministic
time bound <code class="math">\mathrm{poly}(n,L)2^{n/2}</code> and writable-space exponent
<code class="math">18261635770550353/10^{17}</code>. Its input may contain arbitrary signed,
zero or repeated binary integers.

The [short-range theorem](range-branch.md) gives a stronger space bound
for a supplied three-block partition whose first two normalized sum
ranges are short. That input promise belongs to the theorem; it is not
asserted for arbitrary Subset Sum instances. Its arithmetic proof
is identified below.

## General theorem: internal proof obligations

- **Support extraction and trace inequalities:** Sections II.1–II.2
  prove canonical projection injectivity, the nonlinear deficiency
  potential, the fixed-layer trace inequality, deterministic linear
  translate covers and balanced-cell families.
- **Ownership and common moduli:** Sections II.3–II.4 prove exact
  original-coefficient representations, weighted owner covers,
  finite prime families and universal weighted residue covers. The
  common-good path serves all three required images simultaneously.
- **Physical images and space allocation:** Section II.5 proves the
  projection and background reserves, whole-complement compression,
  atomic leaf bounds and finite rounding allowances. Support bounds
  refer to actual integer images before modular reduction.
- **Compatibility and bounded storage:** Section II.6 constructs
  assignment containers and separators and proves the ordered child
  streams, buffered interval join and independent parent streams.
  Original keys are restored before deduplication across local signings.
- **Complete resource ledger and witnesses:** Sections II.7–II.9
  charge each modulus lift, raw occurrence, restart, signing, cache,
  output incidence and live array. The final algorithm includes the
  high-deficiency fallback and indexed witness recovery.

The elementary prime bounds, deterministic sieve, Walsh identities,
quadratic cyclic convolution, fixed-dimensional polynomial arithmetic
and entropy estimates are supplied in the proof. The general theorem
does not leave an external algorithmic oracle or an unavailable verifier
as a hypothesis. It does not use quasi-linear multiplication of
exponentially long integers: its residue convolutions are charged
quadratically, with polynomial-bit entries.

## Short-range theorem: arithmetic proof

The [exact Boolean convolution lemma](convolution.md) supplies
<code class="math">C\,\mathrm{poly}(\log(C+2))</code> bit time and writable space. It proves
the radix-two transform identity, constructs roots with rational
arctangent and Taylor sums, bounds all fixed-point errors below <code class="math">1/4</code>,
and charges schoolbook arithmetic on <code class="math">O(\log C)</code>-bit words. Thus the
range theorem's arithmetic requirement is proved internally, without an
imported fast multiplication theorem or a transcendental-number oracle.

The previous packed-product route could use Harvey and van der Hoeven,
*Integer multiplication in time <code class="math">O(n\log n)</code>*,
[Annals of Mathematics 193(2), 563–617 (2021)](https://annals.math.princeton.edu/2021/193-2/p04).
That published result is not needed by the current proof. The packed
identity remains useful in the finite range check, whose role is to
exercise control flow rather than certify Python's multiplication cost.
The independent [fixed-point check](verify/check_exact_convolution.py)
implements the internally proved arithmetic route.

## Randomness and evidence

Both algorithms are deterministic and exact. Random partitions,
translations and separators are averaging arguments: their choices are
made by exact enumeration or conditional expectation. There is no
input-distribution assumption, Monte Carlo error or Las Vegas runtime
claim.

The [verification note](verify/README.md) identifies the separate
resource, structural and range checks. Exact numerical inequalities
support the ledger; finite examples support the named identities.
Arbitrary-input correctness, the storage schedule and the asymptotic
costs are mathematical proofs in the manuscripts, rather than conclusions
of finite enumeration.

## Source lineage

The bibliography in [proof.md](proof.md#references) retains the classical
Horowitz–Sahni and Schroeppel–Shamir algorithms, the circuit papers and
the [source low-space preprint](https://github.com/openai/math/tree/main/preprints/A-Low-Space-Algorithm-for-Worst-Case-Subset-Sum-September-26-2026).
The imported representation, stream and separator arguments needed for
the current theorem are written out in Sections II.3–II.7.

The entropy/projection discussion is related to Madiman, Marcus and
Tetali, *Entropy and Set Cardinality Inequalities for Partition-Determined
Functions*, [DOI](https://doi.org/10.1002/rsa.20385). Section II.5.1
proves its required projection inequality directly by the chain rule;
the full external sumset theorem is not assumed. The multi-prime
selection method is related to Jin, Park, Saha and Xu,
[ICALP 2026, Article 119](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.119);
Section II.4 supplies the exact finite selection argument used here.

The [import record](../../provenance/README.md) and
[notice](NOTICE.md) preserve revisions, source paths, attribution and
applicable licenses.

**Attribution:** Yilin Liu · GPT-6 Astra Pro.
