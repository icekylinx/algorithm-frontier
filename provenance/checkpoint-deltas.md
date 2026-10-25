# Incremental checkpoint storage

O is the complete baseline. P and Q contain only files whose bytes differ from the previous checkpoint, plus that checkpoint’s current summary, README, and manifest.

- O baseline files: 420
- P duplicate files removed: 417
- P retained files: 28
- Q duplicate files removed: 442
- Q retained files: 37

The original complete archives remain represented by SHA-256 entries in `provenance/archive-manifest.json`; their binary contents are ignored by Git. Problem source maps point to O/P/Q according to byte equality and checkpoint precedence.

**Attribution:** Yilin Liu  \  \n**AI contribution identifier:** GPT-6 Astra Pro
