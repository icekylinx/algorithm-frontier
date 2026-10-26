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
   state exactly which finite or analytic claim it certifies. Missing modules,
   receipts or oracle implementations are unresolved dependencies.
4. Update the concise entry in `catalogue.json`, then regenerate both public
   indexes with `python3 tools/build_catalogue.py`. When a proof package is
   ready for review, record its exact scope, date and remaining conditions in
   `reviews/registry.json`, then run `python3 tools/build_reviews.py`. Use
   partial readiness when only named components of a family have been checked.
5. Run `python3 tools/check_repository.py`. Run the full continuous-domain
   Subset Sum certificate separately when changing its acceptance kernel,
   contact menu or circuit parameters.

## Proof and complexity conventions

Write formal statements followed by proofs. A summary may cite a separately
proved internal lemma or an identified external theorem, but must not replace
an unresolved step with an internal-review label. State a conditional
composition as a conditional theorem.

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

Use GitHub's protected inline notation, `` $`...`$ ``, and fenced `math`
blocks for displays. Ordinary dollar delimiters can let Markdown consume
TeX backslashes before the mathematical renderer sees them: set braces,
negative spacing and alignment rows can then render incorrectly. Keep inline
expressions on one physical line; give long bounds their own display instead
of placing them inside tables. For example:

````markdown
The kernel has $`O(c^2)`$ edges.

```math
m_H\leq\min\left\{m_s,\binom c2+c^2\right\}.
```
````

Use `\mathrm{poly}`, `\mathrm{rank}` and similar upright names in place of
`\operatorname`, which is rejected by some rendering surfaces. Place equation
tags after inner `aligned` or `split` environments. Code fences are for code,
input formats and exact commands; `math` fences contain rendered formulas.

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
then `python3 tools/build_catalogue.py` to refresh the generated indexes.
The standard check command verifies both are current and runs regression
cases for escaping, adjacent formulas, list indentation and protected code.
The syntax checker
catches delimiter, brace, macro and equation-tag errors; it does not prove
the mathematics. GitHub's [mathematical-expression guide](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
describes the supported Markdown delimiters.

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
