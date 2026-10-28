# Sources and mathematical dependency boundaries

[Statement](README.md) · [Proof companion](proof.md) · [Mathematical manuscript](manuscripts/crossing.tex) · [Finite verification](verify/README.md)

## Selected contribution

The selected construction combines normalization-one integral crossing pieces, simultaneous ordered insertion and shared matrix products with a full integral three-shape matrix theorem. The substantial transfer carries individual, unpaired character profiles through the integer spectrum and chooses one integer circuit before its target ring. The resulting circuit uses only <code class="math">0,1,-1</code> and computes the noncommutative identity polynomial in <code class="math">O(N^{1.719516})</code> arithmetic gates.

The real three-shape curve is established prior work over fields. Its shape, the underlying crossing idea and the degree-four output substitutions are not claimed as inventions of this package. The local construction preserves the integral and ordered interfaces required for a common circuit over all associative unital rings. The explicit numerical certificate supplies one strict upper bound, not a global optimum.

## Recent integral matrix source

Zhou and Wang, [*Shared-leg Rectangular Matrix Multiplication over Arbitrary Rings*](https://github.com/Hugin-Hilbert/rectangular-matmul-rings), is the additional recent mathematical source. The supplied checkpoint pins commit `285f513384dee8f933d941ed5e8770ddfbdcaae2`, dated October 14, 2026, and records source ZIP SHA-256 `27df86ba53c34df48630093b4b0cde0154af60811f3499e1567839ad8cc1bf96`.

The [full integral deduction](manuscripts/integral-three-shape.tex) states precisely the source ingredients used: the spectrum for zero and unit-admitting integer tensors; division-free integral convolution; coefficient-extraction monotonicity; unpaired shared-leg sector entropy; the unimodular determinant filtration; and integer tripling sectors. It does not assume an unconstructed evaluator. The source's symmetric-rectangular endpoint and its already stated weaker arbitrary-three-shape bound are distinguished from the stronger full-profile integral composition.

These ingredients remain cited mathematical premises. The checkpoint records internal source-interface reviews. The pinned source could not be fetched again through the browser tool during this curation, so its exact source assertions are attributed to the supplied checkpoint and its pinned source audit; this package makes no fresh independent certification of that repository or its formal endpoint. No formal build tree or historical build receipt is imported.

## Weighted profiles and the field-scope boundary

Amanov, van den Berg and Zuiddam, [*Multiplying Matrices via Polynomials: Exposition and Barriers*, arXiv:2610.30054v1](https://arxiv.org/html/2610.30054v1), states the complete rectangular curve over every field in Theorem 1.2. The primary text was checked on October 28, 2026. Its Sections 4.5–4.6, especially the weighted increment/profile arguments, supply the real-variable analysis used here.

The selected integer composition applies those profile arguments to the integral source interfaces before optional character pairing. The exact quadratic character bound then implies both branches of the matrix exponent. A bare all-field theorem would not supply a common integer circuit, and no inference of that form is made.

## Finite crossing and established reductions

The released [Claude / Anthropic manuscript](https://drive.google.com/file/d/1bSVC6mDHsOgAfXaXB1CEvWYwrmbHAOTB/view), dated October 26, 2026, is credited for the crossing-operator construction. The checkpoint records PDF SHA-256 `f0af035b6c87d04d3fcf07dae040df98029f4990c6493e3e9ab64c4ac714c0eb`. Its finite crossing and duality identities are independently derived in the retained [operator proof](manuscripts/finite-crossing.tex). The Drive PDF was unavailable to the browser tool during curation; this is not presented as a new full-source or formal rebuild. Neither released SAT theorem is a premise of the selected algebraic construction.

[Huang and Jing, *Lattice structure of modular vertex algebras*](https://arxiv.org/abs/2104.05223), provides the established integral-lattice context. The local [Schur argument](manuscripts/integral-pieces.tex) proves the particular normalization-one modes and integer factorizations needed here. The classical [Hardy–Ramanujan partition asymptotic](https://dlmf.nist.gov/27.14.E8) supplies the rank count for unequal dimensions. Both primary mathematical records were checked during this session.

[Hrubeš, *A subquadratic upper bound on Hurwitz's problem and related non-commutative polynomials*](https://users.math.cas.cz/~hrubes/PDFs/palindrome.pdf), primary author text checked October 28, supplies the earlier Hurwitz/circuit context and Proposition 26's integer reductions to the degree-four distinct-index polynomial. Its characteristic-two question is contextual evidence, not a publication-priority certificate. The retained manuscript gives the short integer identities explicitly and uses an upper-shift matrix substitution for the four-row output. It does not rely on a division-by-two transfer.

## Curated source map

The source is the supplied `sat_research_checkpoint.zip`, dated October 27, 2026. Repository-level import metadata records source identities and transformations.

| Retained text | Checkpoint member | Curation |
|---|---|---|
| [Finite crossing](manuscripts/finite-crossing.tex) | `paper/elementary_crossing_operator_lemma.tex` | Complete finite operator and duality proofs. |
| [Integral pieces](manuscripts/integral-pieces.tex) | `paper/integral_schur_extension.tex` | Complete integral theorem; unrelated field/sum-of-squares corollaries and duplicate streaming section omitted. |
| [Coefficient algorithm](manuscripts/coefficient-computation.tex) | `paper/algebraic_streaming_coefficients.tex` | Complete explicit coefficient proof. |
| [Ordered insertion](manuscripts/ordered-insertion.tex) | `paper/direct_mixed_crossing_transfer.tex` | First two complete lemmas; older numerical and field-only branches omitted. |
| [Full integral curve](manuscripts/integral-three-shape.tex) | `paper/integral_full_rectangular_transfer.tex` | Full mathematical deduction, locally expanded curve; formal-receipt statements and weaker numerical branches omitted. |
| [Shared products and selected exponent](manuscripts/shared-products.tex) | `paper/rectangular_hurwitz_transfer.tex`, `paper/direct_mixed_crossing_transfer.tex`, `paper/integral_full_rectangular_transfer.tex`, `paper/constant_free_crossing_circuits.tex` | Focused connective proof with exact rational certificate, constant construction and brief established degree-four identities. |
| [Finite reference](reference/README.md) | `experiments/weighted_integral_schur.py`, `experiments/integral_direct_crossing_checks.py` | Native adapted finite components; bounded coverage and implementation differences stated separately. |

The full proof chain is mathematical draft work with explicit source prerequisites. No complete local formal verification, external peer review or certified historical novelty is claimed. Older numerical substitutions, routine SAT consequences, incomplete permanent approaches and unrelated formal trees are outside the selected package.

**Attribution:** icekylinx and GPT-6 Astra Pro. Apache-2.0 under the repository [license](../../LICENSE); the mathematical sources retain their named attribution.
