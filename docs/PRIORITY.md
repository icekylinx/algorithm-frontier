# Result priority and presentation tiers

Priority controls reading order and maintenance attention. It is not a ranking of mathematical truth, novelty, or author credit. Every record remains source-linked and retains its own review status.

| Tier | Presentation role | Current examples | Maintenance rule |
|---|---|---|---|
| **A — headline** | First-page results that define the current frontier or introduce a new parameter/representation boundary. | Numeric-target R/S, faster Subset Sum, low-space Subset Sum, general matching, dynamic APSP. | Keep the result card, proof map, source map, and focused audits synchronized. Review after every related checkpoint. |
| **B — supporting extension** | Strong constructive, transfer, or model-specific extensions that explain how a headline result is reused. | Flow, polymatroid, allocation, scheduling, dynamic spanner, and SCC records. | Update when a shared backend, parameter glossary, or model assumption changes. |
| **C — boundary and negative record** | Lower bounds, barriers, hardness, robustness limits, and endpoint tradeoffs. | Oracle barriers, robust width-two records, two-scenario hardness, profile endpoints. | Preserve the exact model and assumption; never collapse an oracle boundary into a universal lower bound. |
| **D — archive and provenance** | Imported manuscripts, checkpoint increments, manifests, licenses, and historical snapshots. | `sources/`, `provenance/`, and superseded records. | Preserve bytes and hashes; change only metadata or an explicit correction record. |

## Promotion criteria

A result may move toward Tier A only when its model, comparator, parameters, additive terms, representation, source path, and review status are explicit. A stronger displayed number alone is not enough. Same-scope replacement also requires a proof map and independent or root audit notes.

## Display consequences

Tier A and Tier B records use the compact result-card template and portable code-span complexity. Tier C cards lead with the boundary and assumption. Tier D pages prioritize provenance and byte identity over presentation.

The tier is recorded in a problem README when the distinction affects reading order. The underlying source remains discoverable from `sources.md` and the canonical contents map.
