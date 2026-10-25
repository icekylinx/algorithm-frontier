# Continuous discovery and maintenance loop

The repository is maintained incrementally. Each pass should leave a small, reviewable commit and a clear next action.

## 1. Discover

- Check the connected Library at a moderate interval for new instruction files or checkpoint archives.
- Check the public repository state before editing: branch head, workflow result, and recent source additions.
- Treat an uploaded archive as a candidate increment until its manifest and parent are verified.

## 2. Ingest and identify

- Read the uploaded manifest and parent link before promoting a checkpoint.
- Keep one source tree with its original filenames and internal links under
  `sources/checkpoint-<letter>/`; do not create a review-side backup of the
  manuscript.
- Let the machine check use manifest metadata to catch accidental corruption,
  but keep hashes out of the reader-facing summary.
- Reject a child checkpoint whose parent or file inventory does not match.
- If the material is explicitly a rough or external-review draft, ingest it as
  a source-only checkpoint: add a `Status: draft` marker, leave it out of
  `problems/`, and record its family hints and next review actions in the
  optional `draft_sources` registry section. Run
  [`tools/check_draft_sources.py`](../tools/check_draft_sources.py) before any
  card is promoted.

## 3. Classify the result

For each new claim, compare the model, comparator, parameterization, guarantee, representation, lower-bound type, and review status with existing records. Assign a priority tier using [`PRIORITY.md`](PRIORITY.md): headline, supporting extension, boundary, or archive.

## 4. Promote carefully

Promote only the smallest useful curation layer: a display-first README, a proof map, an exact source map, and focused verification notes. Keep original manuscripts in the source boundary. Mark same-scope older records historical or superseded only after the replacement is actually comparable.

## 5. Normalize presentation

Use prose-first complexity on GitHub-facing pages. Keep time, space, update, query, approximation, and lower-bound fields separate. Reserve exact symbolic notation, TeX, and long derivations for the PDF overview, proof maps, source manuscripts, and checkpoint records.

## 6. Verify and publish

Run structural validation, the display-notation check, the result-card schema check, the finite Subset Sum and reduction replays, incremental-source verification, draft-source validation, review-registry validation, reviewed-link validation, and `git diff --check`. Proof, algorithm, and source review lanes can run in parallel; a result moves forward only when its open issues and finite-check boundary are recorded. Commit a coherent batch, push to `main`, inspect the workflow result, then record the commit in [`HISTORY.md`](../HISTORY.md).

No scheduled job is installed. The loop is re-entered during an active maintenance pass or after a new Library checkpoint is discovered, with the next review trigger recorded in the registry.

## 7. Re-audit

After a workflow failure, a new checkpoint, or a material correction, reopen the affected result card and its source map. Review links, parent links, complexity fields, and priority placement. Keep an explicit backlog in the next history entry when follow-up work remains. T/U are now imported; their first curation pass is the weighted-prefix and sparse-quota record.

## Current backlog

- Review the T/U weighted-prefix and sparse-quota record against the next checkpoint.
- Migrate the remaining legacy problem cards from raw TeX or dense code spans to the prose-first result-card schema.
- Add a machine-readable result index after the display schema stabilizes.
- Add targeted source-to-card link checks for each new checkpoint family.
- Review whether any Tier B record should be promoted after the next related checkpoint.
