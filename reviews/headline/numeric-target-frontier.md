# Review: Numeric-target frontier

- **Record:** [`problems/numeric-target-frontier`](../../problems/numeric-target-frontier/)
- **Tier:** `A`
- **Last reviewed:** `2026-10-25`
- **Status:** `conditional`

## Scope

This review covers the R/S numeric-target catalogue: exact target decisions, scalar optimization, mixed and support-sensitive variants, approximation accuracy, and encoded lower-bound boundaries.

## Proof review

- **Checked:** The record distinguishes exact schemes, approximation schemes, single-matroid variants, and lower-bound audits rather than merging them into one theorem.
- **Evidence:** [`proof.md`](../../problems/numeric-target-frontier/proof.md) and the R/S checkpoint payloads.
- **Open issue:** Preserve the refined accuracy statement `(1/epsilon) times exp(141/(50 epsilon) + 7) times polynomial in H_epsilon` with its scope and direction; do not shorten it to an unqualified approximation claim.

## Algorithm review

- **Checked:** The card separates end-to-end procedures, oracle representations, readable-program representations, and fixed-dimension or single-matroid parameter regimes. It records the square-root-in-`T` and square-root-in-`OPT` variants separately.
- **Evidence:** The numeric-target verification notes and the promoted R/S payload files.
- **Open issue:** Every promoted row must define support, dimension, target, accuracy, and representation parameters locally or link to an unambiguous definition.

## Source review

- **Checked:** R and S are chained increments with manifest hashes and parent references. The source map should enumerate all payload files, not only representative manuscripts.
- **Evidence:** `sources/checkpoint-r/`, `sources/checkpoint-s/`, and their manifests.
- **Open issue:** Reconcile any new R/S payload with the registry before promotion.

## Finite checks

The scope and lower-bound audit notes are finite review artifacts. They help detect mismatched parameter ranges and provenance errors; they do not establish the full mathematical theorems or formal verification.

## Formal-verification boundary

`not-claimed`. Conditional lower bounds retain their named oracle, readable-program, or deterministic-ETH assumptions.

## Next review trigger

Reopen when a new numeric-target checkpoint arrives, an accuracy constant changes, a representation changes, or a lower-bound scope is broadened.
