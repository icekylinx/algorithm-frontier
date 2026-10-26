# History

## 2026-10-26 — Scoped review readiness and exact graph reductions

- Ordered the homepage highlights as deterministic general-graph matching,
  faster deterministic Subset Sum, and sharp correlated-failure summaries.
  The matching backend conditions remain visible in its headline.
- Tightened the matching kernel cutoff from c+1 to c neighbors and proved
  its sharpness, componentwise cost refinement, and a c+f-neighbor kernel
  for native mixed edge/vertex failures on a fixed simple graph.
- Isolated the unconditional sparse degree-factor reduction and added exact
  and ranged cardinality with one feasibility call. Added independent finite
  checks for kernels, decoders, selectors, and cardinality gadgets.
- Introduced synchronized, scope-specific review statuses. A completed local
  proof does not promote an unresolved backend implementation; the evidence
  registry states remaining conditions beside each review invitation.

## 2026-10-26 — Compact problem index

- Reduced the homepage to three representative results and a complete grouped
  index of the 53 problem families. Detailed statements remain on each problem
  page; the 18 supporting results now have a dedicated proof-index section.
- Kept the selected results and all randomness paragraphs generated from the
  same catalogue, preserving model qualifications and deterministic scope.
- Repaired stray inline-code closing markers in the maintenance and complexity
  guides and corrected the evidence-note reading path.

## 2026-10-26 — Readable result pages and portable mathematics

- Replaced the homepage's four-column result tables with grouped, full-width
  entries, retaining all 53 result families and 18 supporting results.
- Replaced field and refinement tables in all 53 problem cards with stacked
  paragraphs. Long headline expressions have separate displays; model and
  scope conditions remain visible alongside each result.
- Replaced incompatible operator-name macros throughout the maintained
  mathematics, repaired undefined set-difference and arg-max commands, moved
  misplaced equation tags outside inner alignments, and joined multiline
  inline expressions. These are typography and syntax corrections, without
  changes to the stated mathematical guarantees.
- Added an idempotent notation normalizer and repository checks for unsupported
  macros, misplaced tags, multiline inline math and table-free result cards.
- Audited randomness across all 71 catalogue entries. Added synchronized
  per-result randomness contracts, variant-level Monte Carlo confidence and
  simultaneous-query scopes, explicit existence-only labels, and the
  distinction between deterministic and randomized oracle lower bounds.
- Recorded the bounded-trial partial-coloring confidence argument for explicit
  group/metric tables and its quantum composition, retaining numerical-access
  conditions and the deterministic stabilizer-witness algorithms.

## 2026-10-26 — Formal manuscripts and complete result catalogue

- Removed `overview.pdf` and its obsolete build sources in [93830a3](https://github.com/icekylinx/algorithm-frontier/commit/93830a3faa8c43e235e9cbb5b76162b0960bd318).
- Replaced proof-map placeholders with full theorem-and-proof manuscripts, promoted the former X-family drafts, and merged the faster Subset Sum refinement into its main problem record. There are now 53 canonical result families.
- Rebuilt the README from a validated catalogue containing every family and 18 additional supporting results. The complete proof index includes all companion and shared manuscripts.
- Consolidated the checkpoint trees into semantic manuscript paths, integrated superseded source copies, removed redundant review pointers and broken verification wrappers, and retained imported licenses and canonical provenance mappings.
- Preserved results that were absent from the old display, including the two-short-range Subset Sum branch, slot-surplus scheduling, optional-player intrinsic allocation, safe machine contraction, eligibility/collision refinements, exact-two parameter boundaries, and expander packing.
- Corrected allocation and scheduling scope and accounting: activated-basis enumeration, bucket bases, fixed-integer two-time parameters, exact fractional comparators, full original resource totals, and the separation between compulsory and optional players.
- Clarified graph backend assumptions, positive-length SSSP scope, the five-point APSP tradeoff, separate spanner recourse regimes, and the derived public MSF baseline. General matching retains its explicit Contract R condition.
- Formalized the laminar quadratic bound and the numeric-target budget classification; retained distinctions between oracle-query and explicit-input lower bounds, kernel size and construction time, and weighted versus rank-only interfaces.
- Reconstructed a self-contained exact continuous-domain Subset Sum checker. Its full refined menu passed all 44 branches with 188,227 accepted leaves. A separate exact scalar checker verifies 104 one-sided profile comparisons and the outer exponent ledger.
- Added scoped profile, sensitivity and quotient-rounding checks, retained the substantive low-space and energy certificates, and accelerated the exhaustive two-scenario reduction check without changing its finite coverage.
- Unified evidence notes and the machine-readable registry across all 53 families. Added one standard-library repository check command and a manual full-contact replay mode in CI.

The entries below describe the repository at their historical commits. Earlier
source paths and draft statuses in those entries are not the current layout.
This log does not replace the mathematical statements or import manifests.

## 2026-10-25 — complete checkpoint X review pass

- Replaced the earlier nine-payload X intake with the complete upload: 38 numbered drafts plus the archive README, maintained in one source tree and grouped by mathematical family.
- Updated `01` and `02` in place, added payloads `10`–`38`, and directly tightened proof, oracle, bit-complexity, and output-accounting details in the reviewed X files. The manifest records both upload hashes and current hashes after curation edits.
- Added six family-level non-promoted cards covering exact sensitivity, correlated spectral/regression summaries, finite-group and metric constraints, quantum/stabilizer blocks, label/block cuts, and separation/obstruction boundaries.
- Added proof-review notes for the arborescence, boundary, colored-graph, and valuated-intersection payloads; kept every X claim source-only and marked formal verification as not-claimed.
- Added an exhaustive finite replay for the seven-element non-Fano obstruction and extended the X Subset Sum rational ledger check. Both checks are evidence only.
- The source import is [`bffbeb2`](https://github.com/icekylinx/algorithm-frontier/commit/bffbeb2cbbdaa31fadedadc0d83f952464b636e5); the family-card and review-map pass is [`ac434c0`](https://github.com/icekylinx/algorithm-frontier/commit/ac434c07f78eeff01c537ace7ed4138ba12d35b4).
- The verification/PDF appendix is [`052995d`](https://github.com/icekylinx/algorithm-frontier/commit/052995d195e8d2787928ec8970ecc2f5f5ebfda5); the follow-up fixed source-path validation and restored the full 293,751-byte PDF blob in [`b1cf61f`](https://github.com/icekylinx/algorithm-frontier/commit/b1cf61fc103b43ec35d68fee07ff9d6c872d9bec). The resulting Actions run is [green](https://github.com/icekylinx/algorithm-frontier/actions/runs/40245182998).

## 2026-10-25 — LaTeX overview and checkpoint X intake

- Replaced the generated overview with a reproducible four-page LaTeX article: `tools/overview.tex` is the source, `tools/make_overview_pdf.py` is the temporary-build compiler, and `overview.pdf` is the checked-in reading map.
- Imported checkpoint X as nine source payloads with an explicit draft manifest, family index, and proof/algorithm/source backlog. The payloads remain source-only; seven non-promoted draft cards expose their guarantees and review obligations without entering the stable catalogue.
- Added draft-source validation to CI and extended the review registry to distinguish draft intake from promoted result records.
- Published commits [`72e5459`](https://github.com/icekylinx/algorithm-frontier/commit/72e545947cf815d3e7e733563b390e411ec86092), [`ded564d`](https://github.com/icekylinx/algorithm-frontier/commit/ded564d50608f12bb9732c9cced32ecdf52b0576), [`28c3bb6`](https://github.com/icekylinx/algorithm-frontier/commit/28c3bb64b5a05a48b503b41f21cd49dc750be0ae), and [`fc25012`](https://github.com/icekylinx/algorithm-frontier/commit/fc2501290fe2c3f1946d5ef87aae23e853e13081). The checkpoint-X constant replay is in [`4d0d9f0`](https://github.com/icekylinx/algorithm-frontier/commit/4d0d9f09f33f3dd853e93c33fe0ee387eeb53093); the final curation run is [green](https://github.com/icekylinx/algorithm-frontier/actions/runs/40214808514).

### Next review

Review checkpoint X payloads family by family. Promote a draft only after proof, algorithm, and source reports agree on its model, parameters, comparator, and lower-bound scope.

## 2026-10-25

- Reorganized the public reading path around `README.md`, [README.md](README.md), and canonical `CONTENTS.md`.
- Adopted portable plain-text complexity on GitHub-facing pages; source manuscripts retain original notation.
- Added result priority tiers and a continuous discovery/maintenance loop.
- Integrated the numeric-target frontier as a Tier A R/S incremental record, with parent-aware source directories and verification notes.
- Added a curation workflow and incremental-source checks.

### Next review

Migrate the remaining legacy problem cards, inspect the first workflow result after the R/S import, and reassess priority tiers when the next checkpoint arrives.

## 2026-10-25 — display migration

- Converted all curated problem result cards to portable code-span complexity notation.
- Added a display-notation check that excludes source manuscripts and detailed proof maps by design.


## 2026-10-25 — T/U checkpoint intake

- Imported T and U as parent-linked increments after validating archive hashes and payload manifests.
- Added the weighted-prefix, laminar, and sparse-quota Tier A extension record.
- Kept T/U separate from the R/S numeric-target card because the parameter geometry and kernel guarantees differ.

## 2026-10-25 — review and presentation pass

- Replaced the homepage and headline cards with prose-first result surfaces and added the root `overview.pdf` reading layer.
- Added explicit parameter, representation, lower-bound, and review-status rows for the R/S, T/U, Subset Sum, matching, APSP, spanner, and incremental SSSP records.
- Added a review registry that separates proof review, algorithm review, source review, finite certificate replay, and formal-verification status.
- Repaired the reviewed low-space source links and expanded the numeric-target source map to every R/S payload file.
- Added CI checks for the review registry and reviewed internal links.

## 2026-10-25 — second review pass

- Added a reading-order table that makes Tier A through Tier D roles visible from the homepage.
- Extended the result-card schema to incremental SCC, dynamic MSF, selected flow, min-cost flow, degree-constrained subgraphs, and five scheduling/profile records.
- Added a backlog review report for those migrated cards and registered the matching, APSP, and incremental SSSP cards under the dynamic-graph review surface.

## 2026-10-25 — third review pass

- Added prose-first cards and backlog reviews for scheduling profiles and allocation/robustness records.
- Expanded the registry to eleven review surfaces, including explicit finite-check paths and a stronger check that every recorded path exists.
- Added a CI whitespace gate and documented the no-schedule, checkpoint-triggered maintenance loop.

## 2026-10-25 — workflow repair

- The first whitespace-gate run exposed the checkout depth assumption; the workflow now fetches two commits before running `git diff --check`.

## 2026-10-25 — deep cost and proof review

- Corrected the APSP tradeoff card to match the source's equalized and fixed-constant amortized curves, query scope, and non-constant-stretch boundary.
- Expanded the R/S, T/U, and low-space proof maps with direct links to every promoted payload and proof component.

## 2026-10-25 — review-scope synchronization

- Extended the allocation/robustness backlog and dynamic-graph review scope to cover the newly migrated supporting cards without changing imported source bytes.

## 2026-10-25 — family index and finite verification pass

- Reorganized the public index around mathematical families, with Subset Sum, numeric targets and quotas, graph algorithms, matching, allocation, robust flow, scheduling, and lower-bound entry points.
- Rebuilt `overview.pdf` as a compact academic reading map with problem statements, explicit parameters, and separate time/space rows.
- Normalized all 41 curated cards to one display schema and removed redundant review prose that duplicated source material.
- Added exact-rational constant checks, exhaustive small Subset Sum contract replay, and a finite two-scenario reduction replay to the curation workflow.

## 2026-10-25 — card layout normalization

- Reordered the required result-card rows into one stable sequence: objective, time, space, parameters, model, lower-bound scope, review status, and source.
- Tightened the schema checker to reject both duplicate fields and future row-order drift.
