# Manuscript formats and publication readiness

The problem pages are the reading index. Inline mathematical expressions are
literal code; displayed equations are checked-in SVG images with exact,
recoverable TeX source. They render without GitHub's mathematical interpreter.

## Incremental TeX migration

The source-bound export set covers the original selected families and also
includes complete degree, quota, flow-adapter and Boolean-compiler proofs,
the four restored static graph packages, rank-sensitive Haxell analysis,
optimal rank-two oracle construction, universal mixed-failure matching
compression and constructive persistence feature ranks. There are 32
source-bound exports:

| Family | Maintained proof | TeX source export | PDF status |
|---|---|---|---|
| Deterministic general-graph matching | [Proof](../problems/general-matching/proof.md) | [TeX](../problems/general-matching/proof.tex) | The complete research manuscript has a [PDF](../problems/general-matching/paper.pdf); its [reference implementation paper](../problems/general-matching/reference/paper.pdf) has a separate scope. |
| Faster deterministic Subset Sum | [Proof](../problems/subset-sum-fast-deterministic/proof.md) | [TeX](../problems/subset-sum-fast-deterministic/proof.tex) | Complete Parts I–III, including the stronger third-lookup theorem, have a [PDF](../problems/subset-sum-fast-deterministic/paper.pdf). |
| Matroid and submodular failure summaries | [Proof](../problems/matroid-failure-summaries/proof.md) | [TeX](../problems/matroid-failure-summaries/proof.tex) | Complete [two-failure](../problems/matroid-failure-summaries/two-failure-paper.pdf) and [rank-adaptive contraction with optimal rank-two queries](../problems/matroid-failure-summaries/rank-adaptive-paper.pdf) packages have PDFs; the wider family remains source only. |
| Persistent-homology failure certificates | [Proof](../problems/persistence-failure-certificates/proof.md) | [TeX](../problems/persistence-failure-certificates/proof.tex) | The complete [actual feature-rank construction](../problems/persistence-failure-certificates/manuscripts/feature-rank-construction.tex) is available as editable source. |

During this transition the Markdown proof owns the text; the adjacent TeX
file is generated from its recovered mathematical source. This avoids two
independently edited versions. The exports contain the complete main proof,
including its model limitations and links to the full companion proofs.
They are TeX body fragments that can be included in the recovered shared
paper style. The [export manifest](../manuscripts/tex-exports.json) lists
every maintained source, output and exact mathematical-source hash.
The [source/image builder](../tools/build_math_assets.py) also accepts formulas
written conventionally during editing and converts them before publication.

```sh
python3 tools/build_manuscripts.py
python3 tools/build_manuscripts.py --check
```

Export authoring uses Pandoc. The ordinary check verifies the recorded input,
tool and output hashes with Python and does not invoke a document compiler.

## PDF boundary

A source file or a successful typesetting run does not make a theorem
complete. A PDF is published only for a defined proof package that has a
complete statement, justified proof, explicit external theorems, and a scoped
review record. Substantial unproved steps remain visible in source-only manuscripts.
A complete mathematical algorithm does not require a software implementation
to qualify; its software coverage is stated separately.

The visual reference is the original Subset Sum paper. Its
[import manifest](../provenance/imports/subset-sum/source-manifest.json)
identifies `paper/main.tex` and `paper/subset-sum.pdf` by exact hashes.
The supplied originals have been recovered and both hashes match that
manifest. The [shared paper style](../manuscripts/paper-style.tex) preserves
the original 11-point A4 article class, Latin Modern fonts, 25 mm margins,
microtype, 3-point paragraph spacing and blue links. This establishes the
typesetting reference; it does not by itself approve a manuscript for PDF.

The five selected paper packages are:

- **[Deterministic Exact General Matching](../problems/general-matching/paper.pdf):** the complete four-fifths research manuscript, including the local cycle-search realization, parameter balance and uniform finite program. Named companion and published proofs remain explicit dependencies. [TeX wrapper](../problems/general-matching/paper.tex).
- **[Deterministic Subset Sum through Signed Circuits and Trace Bounds](../problems/subset-sum-fast-deterministic/paper.pdf):** the complete compiler and witness proof, preserved two-level theorem and third-lookup refinement. Historical and current numerical evidence are distinguished. [TeX wrapper](../problems/subset-sum-fast-deterministic/paper.tex).
- **[Certificates and Cover Compression for Deterministic Matching](../problems/general-matching/reference/paper.pdf):** the independent optimality certificate, refined three-times-matching-number compression, complete nonrecursive bipartite phase proof, and universal mixed-failure kernels with matching/cover certificates. The classical blossom method and known fault-tolerant asymptotic size are attributed to their precise sources. [TeX wrapper](../problems/general-matching/reference/paper.tex).
- **[Two-Failure Prefix Summaries in Oracle Matroids](../problems/matroid-failure-summaries/two-failure-paper.pdf):** profile bounds, the sharp singleton replacement case, exact maxima through rank four, and the explicit 13-item obstruction with its amplification. [TeX wrapper](../problems/matroid-failure-summaries/two-failure-paper.tex).
- **[Rank-Adaptive Failure Summaries in Oracle Matroids](../problems/matroid-failure-summaries/rank-adaptive-paper.pdf):** one fixed contraction for every one-label failure query, exact original-prefix identities, optimal rank-two oracle complexity and its exact-output lower bound, sharp residual-rank endpoints and the all-label-budget construction. [TeX wrapper](../problems/matroid-failure-summaries/rank-adaptive-paper.tex).

Every PDF build uses the recovered shared style, records exact source and
artifact hashes, and requires visual review of the actual pages. Rebuilding
resets that review to pending unless the entire PDF is byte-identical to an
already reviewed artifact, or an exact byte comparison proves that only its
two nonvisual trailer file identifiers changed. The latter comparison accepts
only the engine's expected single identifier field and records the previous
reviewed PDF hash. The ordinary check rejects stale inputs, unreviewed output
or recorded layout warnings. A fixed source timestamp and source-derived
file identifiers make repeated builds reproducible in the same toolchain;
the manifest binds the actual generated bytes. Identifier injection uses
the documented first-page special in the [dvipdfmx manual](https://tug.org/dvipdfmx/doc/dvipdfmx/dvipdfmx.pdf).

```sh
python3 tools/build_papers.py
python3 tools/build_papers.py --check
```

PDF authoring uses Pandoc and XeLaTeX with the packages listed in
[paper-style.tex](../manuscripts/paper-style.tex), including Latin Modern and
microtype. The source-to-TeX conversion compares every mathematical AST node
with the original source. The two main research papers retain the source
section labels, so their internal cross-references are unchanged. XeLaTeX runs with shell escape disabled. Ordinary
repository verification uses Python only and does not install or run TeX.
The [paper configuration](../manuscripts/papers.json) defines each package;
the [build manifest](../manuscripts/paper-builds.json) records its evidence.

See [review and verification](../reviews/README.md) for the mathematical scope
of each package and [Contributing](../CONTRIBUTING.md) for updates.

## Native algebraic-complexity manuscripts

The [affine ROABP PIT package](../problems/roabp-affine-pit/) has two complete
native-TeX papers: the [general theorem](../problems/roabp-affine-pit/paper.pdf)
and the [finite direction-grid refinement](../problems/roabp-affine-pit/direction-grids.pdf).
Their native sources are canonical; they are not independently maintained
exports of a second Markdown proof. Both import the same shared paper style.
The reading companion and static formula pages point to those complete sources.

```sh
python3 problems/roabp-affine-pit/verify/build_native_papers.py
python3 problems/roabp-affine-pit/verify/build_native_papers.py --check
```

The [native build receipt](../problems/roabp-affine-pit/verify/native-paper-builds.json)
binds the sources, style, builder and PDF bytes. All 17 pages were rendered
and inspected after the publication layout changes. Rebuilding resets
visual review to pending. The ordinary repository runner checks these
Python-only bindings alongside the five Markdown-derived paper packages;
no TeX installation is needed in CI. Internal mathematical review remains
distinct from presentation checks and external peer review.
