# Finite verification and mathematical scope

[Statement](../README.md) · [Proof companion](../proof.md) · [Sources](../sources.md) · [Reference components](../reference/README.md)

The selected result is a complete mathematical draft composition with explicit cited source ingredients. The local programs check finite algebra and the exact numerical certificate. They do not implement the asymptotic matrix engine, the shared large-circuit constructor or the full streaming coefficient algorithm, and they do not certify the asymptotic theorem by experiment. No complete local proof-assistant verification or external peer review is claimed.

Run these checks from the repository root:

```sh
python3 -B problems/noncommutative-crossing/verify/check_schur_lattice.py
python3 -B problems/noncommutative-crossing/verify/check_integral_crossing.py
python3 -B problems/noncommutative-crossing/verify/check_numerical_bound.py
```

The current suites pass **10,825 exact checks**:

- The Schur-lattice suite has 10,270 checks: 210 Hall-pairing cases, 91 transform-coordinate checks, 7,920 mode-coordinate comparisons, 1,848 mode columns, 39 duality cases, 142 pieces and 20 complete crossings.
- The ordered crossing suite has 543 checks: nine complete integer crossings, 196 free-word coefficients, nine integrality checks, nine factor-count bounds, 288 evaluations at noncommuting two-by-two matrices, four reversal guards, 19 per-piece orientation equalities, eight malformed-input guards and one orientation-coverage check. Evaluations include the integers and residue moduli 2, 3, 4, 5, 6, 8 and 9, covering characteristic two and coefficient rings with zero divisors.
- The numerical suite has 12 exact checks for the selected rational padding, curved-branch prerequisites and the positive gap below exponent 1.719516. It uses rational arithmetic and integer squaring, not floating-point optimization.

The finite reference uses dense and memoized rational generation for small partitions. It is deliberately separate from the manuscript's streaming algorithm. Its tests compare actual ordered coefficients and noncommuting substitutions, so a correct commutative identity alone is insufficient to pass.

The retained [TeX manuscript](../manuscripts/crossing.tex) has closed local cross-references. With a TeX installation containing `pdflatex` and `bibtex`, build from `problems/noncommutative-crossing/manuscripts`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error crossing.tex
bibtex crossing
pdflatex -interaction=nonstopmode -halt-on-error crossing.tex
pdflatex -interaction=nonstopmode -halt-on-error crossing.tex
```

No generated TeX intermediates, historical formal receipts or checkpoint PDFs are needed to retain the mathematical argument. The initial curation environment lacked `pdflatex`/`latexmk`; source closure was checked, without claiming a local TeX compilation.

**Attribution:** Yilin Liu and GPT-6 Astra Pro. Apache-2.0.
