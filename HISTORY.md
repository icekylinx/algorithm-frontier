# History

This is an append-only curation log. It records repository organization and presentation changes; it does not replace the source manifests or the mathematical review notes.

## 2026-10-25 — LaTeX overview and checkpoint X intake

- Replaced the generated overview with a reproducible four-page LaTeX article: `tools/overview.tex` is the source, `tools/make_overview_pdf.py` is the temporary-build compiler, and `overview.pdf` is the checked-in reading map.
- Imported checkpoint X as nine source payloads with an explicit draft manifest, family index, and proof/algorithm/source backlog. The payloads remain source-only; seven non-promoted draft cards expose their guarantees and review obligations without entering the stable catalogue.
- Added draft-source validation to CI and extended the review registry to distinguish draft intake from promoted result records.
- Published commits [`72e5459`](https://github.com/icekylinx/algorithm-frontier/commit/72e545947cf815d3e7e733563b390e411ec86092), [`ded564d`](https://github.com/icekylinx/algorithm-frontier/commit/ded564d50608f12bb9732c9cced32ecdf52b0576), [`28c3bb6`](https://github.com/icekylinx/algorithm-frontier/commit/28c3bb64b5a05a48b503b41f21cd49dc750be0ae), and [`fc25012`](https://github.com/icekylinx/algorithm-frontier/commit/fc2501290fe2c3f1946d5ef87aae23e853e13081); the final curation run is [green](https://github.com/icekylinx/algorithm-frontier/actions/runs/40214220579).

### Next review

Review checkpoint X payloads family by family. Promote a draft only after proof, algorithm, and source reports agree on its model, parameters, comparator, and lower-bound scope.

## 2026-10-25

- Reorganized the public reading path around `README.md`, `OVERVIEW.md`, and canonical `CONTENTS.md`.
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
