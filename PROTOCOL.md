# Stable citation protocol

This file is part of the repository's stable citation surface.

## Required attribution

Every citation, quotation, redistribution, or adaptation must retain:

- **Attribution:** icekylinx
- **AI contribution identifier:** GPT-6 Astra Pro
- **Repository:** Algorithm Frontier (`algorithm-frontier`)
- **License:** Apache License 2.0

A citation must identify the version or commit used, say whether the curated layer changed, and preserve the applicable copyright, license, and NOTICE statements. The source directory of an imported algorithm may carry additional licenses and notices; those files govern the imported material's original boundary.

## Claim-status vocabulary

Use these labels consistently:

- **Internal review:** the repository records a complete internal mathematical review.
- **Formal verification:** a machine-checked derivation establishes the exact stated claim. An executable finite check alone is not a formalization of an asymptotic theorem.
- **External peer review:** an external review or publication record is actually available.
- **Conditional:** the result still assumes a mathematical claim or interface
  for which no applicable proof or realization is supplied. Identify that
  assumption. A stated oracle or representation defines a model; a proved
  local construction or named published theorem is a dependency, not an
  unresolved hypothesis. Record these categories separately.
- **Historical:** the result remains for provenance but is not the current strongest same-scope record.

Do not turn an audit note into a formal-verification claim. An output verifier proves the returned object's validity; it does not independently prove a fast running-time claim.

Before downgrading a result, trace its dependencies through the canonical
proofs and the checkpoint manifests. Generic conditional interface lemmas
may already have concrete instantiations elsewhere. Executable coverage and
formalization status are separate from mathematical proof readiness.

## Complexity discipline

Every public result should separate guarantee, objective, time, space, parameters, representation, lower-bound type, and review status. See [`docs/COMPLEXITY.md`](docs/COMPLEXITY.md). Unconditional rank-oracle query bounds and deterministic-ETH consequences must be displayed as different statements.

GitHub-facing pages choose formula presentation by purpose: showcased
results use checked-in SVGs; explanatory and machine-consumed expressions
remain literal text. Inline or block placement does not determine the choice.
Exact TeX source remains recoverable; no live GitHub math renderer is required. TeX migration and PDF readiness are tracked separately.
Machine-readable TeX, code, JSON and verification records retain their text;
the static-image convention applies only to presentation surfaces.
See [the maintenance guide](CONTRIBUTING.md).

## Recommended citation

> icekylinx and GPT-6 Astra Pro. *Algorithm Frontier*, version 2026.10.26 (2026). Apache License 2.0.

Cite the relevant `problems/<name>/` path and commit as well. For later releases, preserve the original version in citations to an older result. A later release may add or correct material, but must not rewrite the provenance of an earlier result.
