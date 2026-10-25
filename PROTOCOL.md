# Stable citation protocol

This file is part of the repository's stable citation surface.

## Required attribution

Every citation, quotation, redistribution, or adaptation must retain:

- **Attribution:** Yilin Liu
- **AI contribution identifier:** GPT-6 Astra Pro
- **Repository:** Algorithm Frontier (`algorithm-frontier`)
- **License:** Apache License 2.0

A citation must identify the version or commit used, say whether the curated layer changed, and preserve the applicable copyright, license, and NOTICE statements. The source directory of an imported algorithm may carry additional licenses and notices; those files govern the imported material's original boundary.

## Claim-status vocabulary

Use these labels consistently:

- **Internal review:** the repository records a complete internal mathematical review.
- **Formal verification:** a machine-checked proof or executable checker is actually present.
- **External peer review:** an external review or publication record is actually available.
- **Conditional:** the result depends on a named backend, oracle, representation, or complexity assumption.
- **Historical:** the result remains for provenance but is not the current strongest same-scope record.

Do not turn an audit note into a formal-verification claim. An output verifier proves the returned object's validity; it does not independently prove a fast running-time claim.

## Complexity discipline

Every public result should separate guarantee, objective, time, space, parameters, representation, lower-bound type, and review status. See [`docs/COMPLEXITY.md`](docs/COMPLEXITY.md). Unconditional rank-oracle query bounds and deterministic-ETH consequences must be displayed as different statements.

GitHub-facing pages use plain-text code spans. Source manuscripts may retain TeX and other original notation.

## Recommended citation

> Yilin Liu and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.25 (2026). Apache License 2.0.

Cite the relevant `problems/<name>/` path and commit as well. For later releases, preserve the original version in citations to an older result. A later release may add or correct material, but must not rewrite the provenance of an earlier result.
