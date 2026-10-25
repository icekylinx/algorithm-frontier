# Review backlog: legacy result-card migration

- **Last reviewed:** `2026-10-25`
- **Status:** `needs-follow-up`
- **Records:** incremental SCC, dynamic MSF, selected flow, min-cost flow, degree-constrained subgraphs, and five scheduling/profile records.

## Scope

This first pass migrates the cards to the common prose-first schema. It checks
that each card names its guarantee, objective/output, time or update resource,
space convention, local parameters, model/representation, lower-bound scope,
and source boundary. It is a display and model audit; it does not replace a
full proof review for each theorem.

## Checked in this pass

- `incremental-scc` separates component labels from path or topological output and names the raw minimum-ratio-cycle backend.
- `dynamic-msf` labels its two-thirds baseline as a derived conditional composition rather than an unconditional improvement.
- `selected-flow` defines selected and rejected commodities, accuracy, routing budgets, and the selector interface.
- `min-cost-flow` separates exact flow output, threshold feasibility, edge identifiers, and lifetime edge parameters.
- `degree-constrained-subgraphs` limits the transfer to loopless multigraph edge records and makes the matching backend explicit.
- The scheduling cards define physical machine count, accuracy or bucket parameters, mandatory totals, assignment budgets, and integral output.

## Proof review boundary

The proof maps and imported checkpoint sources remain authoritative. A full
line-by-line proof review is still open for each record, especially where a
public card composes a backend, a decomposition primitive, or an oracle
operation. No finite audit in this pass is formal verification.

## Algorithm review boundary

The cards now separate end-to-end time, preprocessing or update work, output
cost, and writable-space conventions where the source provides them. The next
pass should verify every additive term and distinguish a backend bound from a
complete implementation guarantee.

## Source review boundary

Each card points to the named checkpoint payload and retains the existing
`proof.md`, `sources.md`, and `verify/` files. Source manifests and attribution
remain unchanged. A refreshed checkpoint or changed backend must reopen the
card and this report.

## Formal-verification boundary

`not-claimed`. The repository has no proof-assistant formalization for these
records. Finite certificate replay and manifest validation are evidence for
specific checks only.

## Next review trigger

Promote a record out of this backlog after an independent proof review, an
algorithm cost audit, and a source-manifest check have all been recorded.
Reopen immediately when a checkpoint, model, comparator, backend, or output
interface changes.
