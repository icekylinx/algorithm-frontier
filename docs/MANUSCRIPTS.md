# Manuscript formats and publication readiness

The problem pages are the reading index. Inline mathematical expressions are
literal code; displayed equations are checked-in SVG images with exact,
recoverable TeX source. They render without GitHub's mathematical interpreter.

## Incremental TeX migration

The first export set follows the homepage's three selected families:

| Family | Maintained proof | TeX source export | PDF status |
|---|---|---|---|
| Deterministic general-graph matching | [Proof](../problems/general-matching/proof.md) | [TeX](../problems/general-matching/proof.tex) | Source only; the fast cycle-search implementation is still incomplete. |
| Faster deterministic Subset Sum | [Proof](../problems/subset-sum-fast-deterministic/proof.md) | [TeX](../problems/subset-sum-fast-deterministic/proof.tex) | Source export; scoped typesetting and page review follow separately. |
| Matroid and submodular failure summaries | [Proof](../problems/matroid-failure-summaries/proof.md) | [TeX](../problems/matroid-failure-summaries/proof.tex) | Source export; scoped typesetting and page review follow separately. |

During this transition the Markdown proof owns the text; the adjacent TeX
file is generated from its recovered mathematical source. This avoids two
independently edited versions. The exports contain the complete main proof,
including its model limitations and links to the full companion proofs.
They are TeX body fragments ready for the eventual shared paper template.
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
review record. Missing algorithms and substantial proof gaps remain visible
in source-only manuscripts.

The visual reference is the original Subset Sum paper. Its
[import manifest](../provenance/imports/subset-sum/source-manifest.json)
identifies `paper/main.tex` and `paper/subset-sum.pdf` by exact hashes.
The supplied originals have been recovered and both hashes match that
manifest. The [shared paper style](../manuscripts/paper-style.tex) preserves
the original 11-point A4 article class, Latin Modern fonts, 25 mm margins,
microtype, 3-point paragraph spacing and blue links. This establishes the
typesetting reference; it does not by itself approve a manuscript for PDF.

When a package is ready, its PDF build uses the recovered shared style,
record the source revision, and pass visual review of the actual pages.
See [review and verification](../reviews/README.md) for the mathematical scope
of each package and [Contributing](../CONTRIBUTING.md) for updates.
