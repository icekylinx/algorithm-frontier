# Maintaining the research catalogue

The repository keeps one canonical version of each proof. Result cards state
the strongest justified guarantees in their exact model; companion manuscripts
contain longer derivations and shared interfaces.

## Update a result

1. Edit its theorem and proof in `problems/<name>/proof.md`, or the relevant
   companion manuscript. Give every parameter, quantifier, input representation,
   oracle, comparator and output contract before using it.
2. Update `README.md` in that problem directory. Keep the required fields:
   objective/output, time, space, parameters, model/representation,
   lower-bound scope, review status and source.
3. Update its `sources.md` dependency map and `verify/README.md`. An executable check must
   state exactly which finite or analytic claim it certifies. Distinguish an
   unproved mathematical interface from a proved construction that has no
   executable implementation. Link the realizing theorem before classifying
   an interface as unresolved, and check earlier checkpoint provenance.
4. Update the concise entry in `catalogue.json`, then regenerate both public
   indexes with `python3 tools/build_catalogue.py`. When a proof package is
   ready for review, record its exact scope, date and remaining conditions in
   `reviews/registry.json`, then run `python3 tools/build_reviews.py`. Use
   partial readiness when only named components of a family have been checked.
5. Run `python3 tools/build_math_assets.py` after changing formulas, then
   `python3 tools/check_repository.py`. Run the full continuous-domain
   Subset Sum certificate separately when changing its acceptance kernel,
   contact menu or circuit parameters.

## Proof and complexity conventions

Write formal statements followed by proofs. A summary may cite a separately
proved internal lemma or an identified external theorem, but must not replace
an unresolved step with an internal-review label. State a conditional
composition as a conditional theorem.

A proved local construction discharges an abstract interface when its model,
parameters, initialization, updates and output bounds match the client. Cite
that realization explicitly. A named published theorem is an external proof
dependency; a stated oracle is part of the computational model. Neither a
missing software implementation nor missing proof-assistant formalization
turns a complete mathematical algorithm into an unresolved conditional claim.
Keep genuine promises and conjectural dependencies visible beside the result.

Retain incomparable bounds when their parameters, output guarantees or
computational models differ. Remove a weaker headline only when the stronger
result covers the same assumptions and output. A retained support bound is not
a construction-time bound. An original-ground kernel is not automatically a
parameter-only bit kernel. Rank-query lower bounds and readable-program ETH
consequences are different claims.

For binary capacities and rational inputs, charge bit length, oracle work,
stored records and witness output. A conceptual unit expansion in an existence
proof does not justify constructing an exponentially large ground. Mandatory
bases retain their original total after restrictions and lifts.

The [complexity guide](docs/COMPLEXITY.md) gives the full conventions.

## Files and notation

Use descriptive semantic paths. Current manuscripts belong with their problem;
proofs shared across families belong in `manuscripts/`. Keep import metadata
and license boundaries in `provenance/`, rather than maintaining copied
checkpoint trees or separate draft versions.

Choose the representation by **purpose**, not by inline/block position or
formula length. A formula presented as a headline bound, theorem conclusion,
comparison, or central derivation belongs in a source-bound SVG. A formula
used as a parameter, premise, explanation, program contract, exact certificate
value, or machine input remains literal, copyable text. A short headline can
be an SVG; a long parameter definition can remain text. Layout follows the
reading context and does not determine the role.

SVGs contain their own glyph paths and a white canvas; reading them needs no
JavaScript, external fonts or mathematical rendering service. Exact TeX is
retained in the adjacent `math-display` source comment and in the SVG title.
Literal mathematical text uses escaped `<code class="math">` elements or
ordinary code spans/blocks. Both retain machine-readable content. The legacy
`math-display` name records the SVG representation, not a rule that every
formula on a separate line must become an image.

TeX sources, programs, JSON catalogues, receipts, manifests and other
machine-readable records retain their literal formulas and data. Never
replace those values with images or rendered fragments. `catalogue.json`
records a `quantity_purposes` list for every result: one `showcase` or `literal`
entry per formula in `quantity`, in source order. The generator checks the
annotation count and uses these reviewed roles, without a length threshold.
Parameter definitions in other fields remain literal.

Public overviews, result cards, source maps and verification notes must not
leave symbolic formulas as ordinary prose. Use SVGs for showcased conclusions
and code for parameters, premises and exact data. `tools/check_public_math.py`
guards recognizable bare formulas on those surfaces; it cannot infer the role
of every isolated letter. Canonical manuscripts retain limited prose-notation
exceptions, and programs, TeX, JSON and other machine inputs keep their native
formats. Review generated catalogue and review-registry text at its source so
the next rebuild preserves the notation choices.

Edit the preserved mathematical source, not the SVG. Its digest determines
the image name and `assets/math/manifest.json` binds its exact bytes. During
authoring, select the SVG representation with a `math` fence or a display
source comment; select literal mathematical text with a code element. Dollar
delimiters are also accepted as legacy authoring input to the builder, but
are not a purpose classifier or a required published format. Review the
formula's role before choosing either representation.

```sh
npm ci --prefix tools/math-renderer
python3 tools/build_math_assets.py
```

Node and the pinned MathJax package are optional **authoring** dependencies.
The ordinary repository checks verify source/image bindings using only Python.
They also reject executable SVG content and external glyph references. See
[the manuscript migration guide](docs/MANUSCRIPTS.md) for the TeX sources and
the separate PDF publication boundary.

Use `\mathrm{poly}`, `\mathrm{rank}` and similar upright names consistently.
Place equation tags after inner `aligned` or `split` environments. Ordinary
code fences remain available for programs, input formats and exact commands.

The homepage contains a small selection of results and the complete problem
index. Full statements and model conditions belong on the problem cards. The nine standard card labels each introduce a separate
paragraph. Every method states its [randomness contract](docs/RANDOMNESS.md),
including confidence and backend assumptions when relevant. `catalogue.json`
owns the **Randomness** paragraphs synchronized with the selected homepage
entries and all problem cards. Keep small
comparison tables in technical manuscripts only when
their contents fit comfortably. Use `\lvert` and `\rvert` for mathematical
vertical bars in such tables.

Run `python3 tools/normalize_math.py` to normalize mathematical typography,
then regenerate the catalogue and review surfaces and build formula images.
The standard checks cover source recovery, escaping, adjacent expressions,
list indentation, unchanged ordinary code, image rebinding and exact formula
digests. The source checker catches grouping, macro and equation-tag errors;
none of these presentation checks proves the mathematics.

Prefer relative links to canonical files. Give a stable primary reference and
version for an imported theorem. Keep credits and applicable license/NOTICE
files when consolidating source material.

## Evidence and publication

The [review registry](reviews/README.md) records manuscript and executable
evidence for every result. Finite examples, exact numerical certificates,
output verifiers, complete asymptotic proofs and proof-assistant formalizations
are distinct forms of evidence.

Commits should explain the mathematical or organizational change and its
validation. Update [HISTORY.md](HISTORY.md) for changes to a theorem, comparator,
representation, leading bound or canonical path. Cite an exact commit when
referring to a historical statement.
