# Review backlog: matching certificates

- **Last reviewed:** `2026-10-25`
- **Status:** `needs-follow-up`
- **Records:** independent transversal and strong Haxell hypergraph matching.

## Scope

These two cards return either a combinatorial matching or a checkable
obstruction. The review must keep the promise, certificate semantics, and
output representation separate from the general-graph matching backend.

## Proof review

Check that the partition-relative domination/constellation certificate and the
strong-Haxell hitting-set certificate are sufficient for the stated branch,
and do not silently become a proof of global infeasibility outside the promise.

## Algorithm review

Recheck incidence volume, class count, claw or degree parameters, streamed
certificate construction, and the cost of validating both possible outputs.
Keep the explicit hypergraph and partition representations visible.

## Source review

Reconcile each card with its named checkpoint payload and verification surface
when the matching manuscripts are refreshed. No source is copied into this
report.

## Finite checks and formal verification

Finite certificate checks are evidence for the displayed component only. No
formal proof-assistant artifact is claimed.

## Next review trigger

Reopen when a matching source changes its promise, certificate, incidence
parameter, or backend composition.
