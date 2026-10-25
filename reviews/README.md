# Review registry

This directory records the current review state of the curated result cards. A review entry describes what was checked, what remains open, and what evidence supports the displayed claim; it does not duplicate an imported manuscript.

## Review roles

- **Proof review** checks that the proof map exposes the theorem contract, reductions, parameter definitions, and logical gaps.
- **Algorithm review** checks that the public algorithm description separates preprocessing, update, query, output, recourse, and representation costs.
- **Source review** checks provenance, attribution, and whether the card points to the exact payload that supports it.
- **Finite checks** record executable identities or replayable certificates. They are useful evidence, but they are not formal verification of the full algorithm or proof.

A result is promoted only when its README, proof map, source map, and review entry agree about the same model and parameters. The registry is machine-checked by [`tools/validate_reviews.py`](../tools/validate_reviews.py), including the existence of every recorded finite-check path. Every problem card is checked against the shared field contract by [`tools/check_card_schema.py`](../tools/check_card_schema.py). Relative Markdown links in the curated layer and the low-space source tree are checked by [`tools/check_internal_links.py`](../tools/check_internal_links.py).

## Status vocabulary

| Status | Meaning |
|---|---|
| `reviewed` | The displayed claim has a current proof, algorithm, and source review; open issues are explicitly listed. |
| `conditional` | The claim depends on a named oracle, backend, conjecture, or representation contract. |
| `needs-follow-up` | A material issue remains before the card can be treated as a stable headline result. |
| `archival` | The record is preserved for provenance but is not a current headline result. |

The registry records the boundary between **internal mathematical review**, **finite certificate replay**, and **formal verification**. Unless a formal proof assistant artifact is named, the last category is `not-claimed`. Manifest metadata is used by automation only; it is not a second copy of a source.
