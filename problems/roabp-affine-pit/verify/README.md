# Verification and review scope

The general theorem is justified by the complete [core proof](../manuscripts/general-affine.tex) and [direction-grid proof](../manuscripts/direction-grids.tex). The programs below check exact finite identities, generator arithmetic, promised examples and publication-source bindings. None proves the arbitrary-input theorem by computation.

## Mathematical review

The research-session package contains separate internal reconstructions of the Artin-ring row-space induction, per-monomial box filtering, local Hasse pivots and augmented-interval rank descent. The [fresh-context report](../review/independent-core-audit.txt) was written without reading the earlier verdicts. It found no fatal flaw or exact missing mathematical assumption in the 845-line frozen core. The [second core report](../review/core-source-audit.txt) and [grid report](../review/direction-grid-audit.txt) identify their exact source hashes and checked interfaces.

The difficult reset step received a further [adversarial review](../review/artin-reset-audit.txt). Its examples allow zero divisors and future-dependent controls, and include a nonzero corrected passive response that the source terms cancel exactly. This guards against replacing the proved coefficient-span statement with a false assertion that the corrected passive product itself vanishes.

The [proof-reading guide](../review/artin-proof-reading-guide.txt) isolates the row-space definitions, the direction of coefficient-span inclusions, the source-restart cost and the zero-dimensional reset case. The [special-case scope audit](../review/special-case-scope-audit.txt) checks the five retained parameter regimes. The [cone dependency audit](../review/cone-dependency-audit.txt) verifies that the factorial-width affine result uses exactly the theorem proved in its included companion. This resolved dependency is not an unproved conditional hypothesis.

The [publication-facing audit](../review/publication-scope-audit.txt) checks the presentation and special-case ledger before static formula rendering. Audit files are historical records of the identified source versions, not claims of later review. In particular, the research-session external-preprint note predates this repository publication; its statement about no public posting refers to that earlier session.

These are model-assisted internal reviews, not independent external human peer review, proof-assistant certification, or priority verification. The [external-preprint review](../review/external-rigidity-review.txt) is a separate collection of explicit counterexamples and does not validate this theorem.

## Exact generator implementation

The standalone [general prototype](all_rank_affine_orbit.py) implements the moment-curve map, the explicit rank budgets, the globally smaller direction grid, extension-field arithmetic and lazy enumeration. It reports a nonzero witness as soon as one is found. A bounded partial run reports `incomplete`; only a completed traversal can report zero under the mathematical promise.

The executable arithmetic is specifically over the rationals in characteristic zero and over a constructed finite extension of the prime field in positive characteristic. It does not accept an arbitrary supplied base field or construct compatible embeddings for a supplied nonprime finite field. The arbitrary-field theorem has the broader oracle model stated in the proof. The command-line interface prints grid metadata or runs finite self-checks; an application supplies its oracle through the Python `HittingGrid.test(oracle, max_queries=...)` API.

```sh
python3 problems/roabp-affine-pit/verify/all_rank_affine_orbit.py --self-check
```

The exact cases cover rational arithmetic and fields of sizes 128, 243 and 125. They include actual width-four physical factors of ranks three and four, local degree two, an invertible input shear, Lagrange interpolation, refined-grid selection, complete univariate grids and interrupted traversals. The [stored evidence](all_rank_self_check.json) records the finite cases, and the [implementation audit](../review/prototype-audit.txt) states which changes were checked.

The general grid is far too large for practical traversal at moderate widths. The finite examples do not claim an exhaustive test of the general hitting set or a practical running time.

The separate [rank-one/full prototype](rank_one_full_affine_orbit.py) implements the all-characteristic special case with a derivative-separating curve and its smaller width budget. It has the same arithmetic and API limitations just described. It retains its own representation promise; these stronger bounds are not provided by the general prototype. Its [stored exact evidence](rank_one_full_self_check.json) covers rational and finite-field arithmetic, curve exponents and complete versus interrupted traversal.

```sh
python3 problems/roabp-affine-pit/verify/rank_one_full_affine_orbit.py --self-check
```

## Structural constructions

```sh
python3 problems/roabp-affine-pit/verify/check_palette_sharpness.py
python3 problems/roabp-affine-pit/verify/check_artin_reset.py
python3 problems/roabp-affine-pit/verify/check_quadratic_hasse.py
```

The palette program multiplies exact sparse integer-polynomial rows for every one of the 127 palettes through width seven. It verifies the single full-support scalar monomial and the elementary local-rank certificates. Those integer identities remain true after reduction to any field. This supports the separately proved sharpness construction; it is not an exhaustive proof of the upper-bound concentration theorem.

The reset program uses explicit monomial quotient rings over the rationals and the field with two elements. Its complete finite computation checks the claimed unit-rank minors, future-dependent cancellation, source reachability and the tight source-restart example. The output JSON is optional, so the normal check does not modify tracked files. [Stored palette evidence](palette_sharpness_checks.json) and [stored Artin evidence](artin_reset_checks.json) remain machine-readable.

The [quadratic Hasse obstruction](../manuscripts/quadratic-hasse-obstruction.md) has a separate [internal reconstruction](../review/quadratic-hasse-audit.txt). Its independently written verifier uses coefficient bases, fraction-free Bareiss determinants and prime-field elimination. Widths two through ten and three qualifying primes per width check the binomial determinant formula, middle-factor residual identity and scalar total degree. It imports no author verifier. The [stored JSON](quadratic_hasse_checks.json) binds the original research source and verifier; the canonical command changes only the source path and makes output optional. The complete symbolic proof covers every width. The result concerns the ordinary moment curve and does not claim a lower bound on PIT or on the number of SV pairs.

A [second mathematical review](../review/quadratic-publication-audit.txt) reconstructs the complete publication manuscript before static formula rendering. It separately confirms the determinant sign and unit conditions, the exact degree, the whole first component and the surviving one-pair SV coefficient; it does not claim a fresh execution of the finite checks.

## Source identity and native papers

```sh
python3 problems/roabp-affine-pit/verify/check_source_bindings.py
python3 problems/roabp-affine-pit/verify/build_native_papers.py --check
```

The first command verifies every canonical import hash and reverses each documented publication edit to the exact reviewed source hash. This establishes provenance. It does not infer correctness from the presence of an audit file.

The second checks the native-TeX sources, shared paper style, builder, PDF bytes and recorded visual review. The core has 12 pages and the grid addendum has 5. All 17 pages were rendered and inspected after publication layout changes. There were no layout warnings, missing-reference markers or clipping defects. The [build receipt](native-paper-builds.json) records the exact bindings.

To rebuild the two papers, with XeLaTeX and the authoring PDF parser installed:

```sh
python3 problems/roabp-affine-pit/verify/build_native_papers.py
```

A rebuild deliberately resets visual review to pending. Review all generated pages before changing that status. The ordinary repository checks use only the Python standard library and do not run TeX.

The [special-case ledger](../manuscripts/special-cases.md) supplies its own complete source dependencies. Distinct characteristic assumptions and curve choices are retained explicitly; their stronger bounds are not silently attributed to the general prototype.
