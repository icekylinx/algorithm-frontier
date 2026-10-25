# Incremental checkpoint storage

O is the complete baseline. P and Q contain only files whose bytes differ from the previous checkpoint, plus that checkpoint’s current summary, README, and manifest.

- O baseline files: 420
- P duplicate files removed: 417
- P retained files: 28
- Q duplicate files removed: 442
- Q retained files: 37

The original complete archives remain represented by SHA-256 entries in `provenance/archive-manifest.json`; their binary contents are ignored by Git. Problem source maps point to O/P/Q according to byte equality and checkpoint precedence.

**Attribution:** Yilin Liu  \  \n**AI contribution identifier:** GPT-6 Astra Pro

## R increment

- Parent: Q archive `8ff7b58aafa78cf67747fcd58433f98d8968a11d03ee61c3041497b3b7fc96e5`.
- R archive: `deterministic_related_problems_increment_20261025_R.zip`, SHA-256 `c5a0cacff1e0ab9283da4e6214d7f80ced7fc46cc3b15e5700dc9098bf7e3bf4`, 110,748 bytes.
- Retained payload: 17 files; no Lean, PDF, executable, or test bundle.
