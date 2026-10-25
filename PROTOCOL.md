# Stable citation protocol

This file is part of the repository's stable citation surface.

## Required attribution

Every citation, quotation, redistribution, or adaptation must retain:

- **Attribution:** Yilin Liu
- **AI contribution identifier:** GPT-6 Astra Pro
- **Repository:** Algorithm Frontier (`algorithm-frontier`)
- **License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

A citation must link the canonical license URL and identify the version or
commit used. If files are changed, the citing work must say that changes were
made. Adapted material must use CC BY-SA 4.0 or a Creative Commons compatible
share-alike license; no additional restriction may be added.

## Recommended citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25
> (2026). CC BY-SA 4.0. Cite the relevant `problems/<name>/` path as well.

For later releases, preserve the original version in citations to an older
result. A later release may add or correct material, but must not rewrite the
provenance of an earlier result. Each problem keeps its own README, proof map,
and verification notes so that a citation remains auditable after curation.

## Meaning of “verify”

`verify/` files are mathematical audit notes and source comparisons. They are
not a claim of formal machine verification, peer review, or implementation
certification. A conditional result must name every external primitive or
internal contract it assumes. An output verifier proves the returned object's
validity; it does not independently prove a fast running-time claim.
