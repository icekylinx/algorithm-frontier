# Continuous discovery and maintenance loop

The repository is maintained incrementally. Each pass should leave a small, reviewable commit and a clear next action.

## 1. Discover

- Check the connected Library at a moderate interval for new instruction files or checkpoint archives.
- Check the public repository state before editing: branch head, workflow result, and recent source additions.
- Treat an uploaded archive as a candidate increment until its manifest and parent are verified.

## 2. Ingest and identify

- Copy known user uploads into the local working area without rewriting their payload.
- Record archive SHA-256, parent archive SHA-256, checkpoint letter, file count, and exclusions.
- Preserve original filenames and internal links under `sources/checkpoint-<letter>/`.
- Reject a child checkpoint whose parent hash or file inventory does not match.

## 3. Classify the result

For each new claim, compare the model, comparator, parameterization, guarantee, representation, lower-bound type, and review status with existing records. Assign a priority tier using [`PRIORITY.md`](PRIORITY.md): headline, supporting extension, boundary, or archive.

## 4. Promote carefully

Promote only the smallest useful curation layer: a display-first README, a proof map, an exact source map, and focused verification notes. Keep original manuscripts in the source boundary. Mark same-scope older records historical or superseded only after the replacement is actually comparable.

## 5. Normalize presentation

Use portable code-span complexity on GitHub-facing pages. Keep time, space, update, query, approximation, and lower-bound fields separate. Reserve TeX and long derivations for source manuscripts and checkpoint records.

## 6. Verify and publish

Run structural validation, the display-notation check, incremental-source verification, and `git diff --check`. Commit a coherent batch, push to `main`, inspect the workflow result, then record the commit in [`HISTORY.md`](../HISTORY.md).

## 7. Re-audit

After a workflow failure, a new checkpoint, or a material correction, reopen the affected result card and its source map. Review links, parent hashes, complexity fields, and priority placement. Keep an explicit backlog in the next history entry when follow-up work remains. T/U are now imported; their first curation pass is the weighted-prefix and sparse-quota record.

## Current backlog

- Review the T/U weighted-prefix and sparse-quota record against the next checkpoint.
- Migrate the remaining legacy problem cards from raw TeX to portable code-span complexity.
- Add a machine-readable result index after the display schema stabilizes.
- Add targeted source-to-card link checks for each new checkpoint family.
- Review whether any Tier B record should be promoted after the next related checkpoint.
