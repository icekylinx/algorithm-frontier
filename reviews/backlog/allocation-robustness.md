# Review backlog: allocation and robustness records

- **Last reviewed:** `2026-10-25`
- **Status:** `needs-follow-up`
- **Records:** recipient polymatroid allocation, arbitrary-value allocation, robust scenario flow, robust width-two allocation, bounded robust certificates, and allocation lower bounds.

## Scope

This pass replaces terse legacy cards with explicit guarantee, objective/output,
time, space, parameter, representation, lower-bound, and source rows. The
proof maps and checkpoint payloads remain authoritative; the card rewrite does
not alter imported mathematics.

## Proof review

The cards now expose the critical proof gates: selected rank and corank,
common versus scenario-adaptive choices, exact assignment or routing budgets,
certificate width, and oracle versus explicit-input boundaries. A complete
line-by-line proof review remains open, especially for approximation profile
counts, robust scenario separation, and whole-ground conversions.

## Algorithm review

The review separates end-to-end work from selector, rank-oracle, routing,
profile, and branching primitives. It also distinguishes algorithmic space
from a lower-bound record that has no algorithmic space claim. Any promoted
complexity must retain the exact additive terms, accuracy encoding, and output
reconstruction cost from its source.

## Source review

Each card points to its checkpoint payload, proof map, and verification
surface. Ranks, budgets, scenario lists, and certificate promises must remain
identical between the card and source after every checkpoint refresh.

## Finite checks and formal verification

Finite audit notes, source-hash checks, and bounded certificate replays are
evidence for individual components. They are not formal verification of the
full arbitrary-input algorithm or theorem. No proof-assistant artifact is
claimed here.

## Next review trigger

Reopen this backlog when a new allocation/robustness checkpoint arrives, a
model or comparator changes, a whole-ground conversion is promoted, or a
backend is replaced. Promote a record only after independent proof,
algorithm, and source reviews are recorded.
