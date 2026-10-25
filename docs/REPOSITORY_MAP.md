# Repository map

The repository separates public result records from imported source material.

| Path | Purpose |
|---|---|
| `README.md` | Display-first landing page with featured results and navigation. |
| `OVERVIEW.md` | Short reading path for headline records. |
| `CONTENTS.md` | Canonical complete catalogue of all curated modules. |
| `problems/<name>/` | One curation record: README, proof map, verification notes, and exact source map. |
| `sources/checkpoint-o/` | Complete baseline source snapshot. |
| `sources/checkpoint-p/`, `sources/checkpoint-q/` | Incremental source checkpoints retained by byte identity. |
| `sources/checkpoint-r/`, `sources/checkpoint-s/`, `sources/checkpoint-t/`, `sources/checkpoint-u/` | Incremental research payloads with parent links and manifests. |
| `sources/checkpoint-x/` | Source-only rough drafts awaiting proof, algorithm, and source review; no promoted result cards. |
| `provenance/` | Machine-readable checkpoint manifests and source-file identity. |
| `tools/` | Structural, delimiter, incremental-source, and draft-source checks. |
| `.github/workflows/` | Reproducible repository checks for pushes and pull requests. |

## Curation flow

1. Preserve a new checkpoint under its own source directory.
2. Read its parent, manifest, exclusions, and review scope; keep machine metadata in the manifest rather than in a duplicate review file.
3. If the payload is a rough draft, mark it source-only and register its next review actions; do not create a result card yet.
4. Add or update a compact problem record only after the model and comparator are explicit.
5. Keep raw manuscripts and imported licenses in `sources/`.
6. Run every check in `MAINTENANCE.md` before pushing.
7. Use the commit SHA in citations and release notes.

A source file may be long; a public result record should remain scan-friendly. Detailed proof prose belongs in the source path or the proof map, while the README exposes the guarantee and complexity first.
