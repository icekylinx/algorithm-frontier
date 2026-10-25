# Curation and release policy

The repository is intentionally staged. A new checkpoint is first copied into
`sources/` and recorded in `provenance/archive-manifest.json`. Checkpoint storage
is incremental: O is the complete baseline, P stores only P minus O, and Q stores
only Q minus P (with each current summary/README/manifest retained). The exact
byte-level counts are in `provenance/checkpoint-deltas.md`. Then one problem
at a time is promoted under `problems/`. Each promotion is a separate commit
with a complete README/proof/verify set.

During the private phase, redundant source notes and older checkpoints may stay
in the snapshot to make comparison auditable. Before a public release, remove
only files that are redundant after their hashes, source paths, and supersession
status have been recorded. Never delete a source needed to reproduce a cited
claim without leaving a provenance pointer.

A claim can replace an older claim only when all of these are explicit:

- same problem model and comparator;
- at least as strong guarantee in every relevant parameter regime;
- no hidden loss of additive terms, input assumptions, or exactness;
- proof and independent/root audits available;
- old claim marked historical or superseded in the curation index.

Run `python3 tools/validate_curation.py` before each commit. The script checks
structure and attribution; it does not prove mathematics.
