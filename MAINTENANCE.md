# Curation and release policy

The repository is public and is maintained as a source-linked research index. Public-facing records must remain concise, explicit about scope, and reproducible from their cited source paths.

## Checkpoint storage

Checkpoint O is the complete baseline. P and Q retain only byte-level increments after their parent, together with current summaries and manifests. Checkpoints R, S, T, and U follow the same rule:

- R is an increment since Q;
- S is an increment since R;
- T is an increment since S;
- U is an increment since T;
- Each child does not copy the parent payload and names the parent through its archive hash;
- each increment keeps its own README, checkpoint summary, and machine-readable manifest.

The original complete archives remain represented by SHA-256 entries in `provenance/archive-manifest.json`; binary archives are not committed. `provenance/checkpoint-files.json` and the per-increment manifests verify retained source bytes.

## Promotion policy

A new theorem is promoted under `problems/` only after its model, comparator, parameters, additive terms, representation, and review status are explicit. Each promoted record keeps a README, proof map, exact source map, and at least two focused verification notes.

A claim can replace an older claim only when all of these are explicit:

- same problem model and comparator;
- at least as strong a guarantee in every relevant parameter regime;
- no hidden loss of additive terms, input assumptions, or exactness;
- proof and independent/root audits available;
- old claim marked historical or superseded in the curation index.

## Required checks

Run the following before each commit:

```sh
python3 tools/validate_curation.py
python3 tools/check_latex_delimiters.py
python3 tools/verify_incremental_sources.py
```

These checks cover structure, attribution, display delimiters, and source hashes; they do not prove the mathematics.
