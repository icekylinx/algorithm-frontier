# Review backlog: scheduling profile records

- **Last reviewed:** `2026-10-25`
- **Status:** `needs-follow-up`
- **Records:** activated-machine scheduling, arbitrary-processing scheduling, commitment scheduling, many-size workload scheduling, two-size scheduling, per-machine two-time scheduling, processing-bucket tradeoff, and six-profile three-halves scheduling.

## Scope

This pass replaces compact complexity-only cards with explicit guarantees,
objectives, parameters, model boundaries, and output contracts. It keeps
accuracy schemes, commitment reductions, bucket curves, two-size endpoints,
many-size additive terms, six-profile enumeration, and per-machine two-time
assumptions separate.

## Proof review boundary

The proof maps retain the checkpoint notes and audit dependencies. A full
line-by-line proof review of profile coverage, integral recovery, and
additive-term accounting remains open. Finite audit notes are not formal
verification.

## Algorithm review boundary

The cards separate profile enumeration, compressed-rank search, rounding, and
output decomposition at the level exposed by the sources. The next review
must verify every additive polynomial factor and the exact definition of the
source's profile function.

## Source review boundary

The source maps and checkpoint payload names are unchanged. A new checkpoint,
changed processing model, or changed assignment-budget convention reopens all
three cards.

## Formal-verification boundary

`not-claimed`.

## Next review trigger

Promote a card after independent proof, algorithm-cost, and source-manifest
reviews have been recorded for its exact model.
