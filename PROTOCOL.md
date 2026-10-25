# Stable citation protocol

This file is part of the repository's stable citation surface.

## Required attribution

Every citation, quotation, redistribution, or adaptation must retain:

- **Attribution:** Yilin Liu
- **AI contribution identifier:** GPT-6 Astra Pro
- **Repository:** Algorithm Frontier (`algorithm-frontier`)
- **License:** Apache License 2.0

A citation must identify the version or commit used. If files are changed, the
citing work should say that changes were made and must preserve the applicable
copyright, license, and NOTICE statements. The source directory of an imported
algorithm may carry additional licenses and notices; those files govern the
imported material's original boundary.

## Recommended citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25
> (2026). Apache License 2.0. Cite the relevant `problems/<name>/` path and
> commit as well.

For later releases, preserve the original version in citations to an older
result. A later release may add or correct material, but must not rewrite the
provenance of an earlier result. Each problem keeps its own README, proof map,
and verification notes so that a citation remains auditable after curation.

## Meaning of “verify”

`verify/` files are mathematical audit notes, source pointers, or executable
checks. They are not a claim of formal machine verification, peer review, or
implementation certification. A conditional result must name every external
primitive or internal contract it assumes. An output verifier proves the
returned object's validity; it does not independently prove a fast running-time
claim.
