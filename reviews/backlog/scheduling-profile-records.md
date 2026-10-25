# Review backlog: scheduling profile records

- **Last reviewed:** `2026-10-25`
- **Status:** `needs-follow-up`
- **Records:** many-size workload scheduling, six-profile three-halves scheduling, and per-machine two-time scheduling.

## Scope

This pass replaces compact complexity-only cards with explicit guarantees,
objectives, parameters, model boundaries, and output contracts. It checks that
the many-size additive term, the six-profile enumeration, and the per-machine
two-time assumption are not silently conflated.

## Proof review boundary

The proof maps retain the original checkpoint notes and audit dependencies.
A full line-by-line proof review of the profile coverage, integral recovery,
and additive-term accounting remains open. Finite audit notes are not formal
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
