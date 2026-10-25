# Repository map

The repository separates public result records from imported source material.

| Path | Purpose |
|---|---|
| `README.md` | Display-first landing page with featured results and navigation. |
| `OVERVIEW.md` | Complete index of curated problem modules. |
| `problems/<name>/` | One curation record: README, proof map, verification notes, and exact source map. |
| `sources/checkpoint-o/` | Complete baseline source snapshot. |
| `sources/checkpoint-p/`, `sources/checkpoint-q/` | Incremental source checkpoints retained by byte identity. |
| `sources/checkpoint-r/`, `sources/checkpoint-s/` | New R and S incremental research payloads; S names R as its parent. |
| `provenance/` | Archive hashes, checkpoint manifests, delta accounting, and source-file identity. |
| `tools/` | Structural, delimiter, and incremental-source checks. |
| `.github/workflows/` | Reproducible repository checks for pushes and pull requests. |

## Curation flow

1. Preserve a new checkpoint under its own source directory.
2. Record its parent, archive hash, file hashes, exclusions, and review scope.
3. Add or update a compact problem record only after the model and comparator are explicit.
4. Keep raw manuscripts and imported licenses in `sources/`.
5. Run every check in `MAINTENANCE.md` before pushing.
6. Use the commit SHA in citations and release notes.

A source file may be long; a public result record should remain scan-friendly. Detailed proof prose belongs in the source path or the proof map, while the README exposes the guarantee and complexity first.
