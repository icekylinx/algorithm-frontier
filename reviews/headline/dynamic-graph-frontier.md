# Review: Dynamic graph frontier

- **Record:** [`problems/dynamic-spanners`](../../problems/dynamic-spanners/)
- **Tier:** `B`
- **Last reviewed:** `2026-10-25`
- **Status:** `conditional`

## Scope

This review covers dynamic spanner records and their adjacent dynamic-graph comparisons. The headline card must keep tracked-terminal and full-horizon regimes separate.

## Proof review

- **Checked:** The proof maps identify the update model, graph size, horizon, stretch, and recourse/path-reporting obligations for each regime.
- **Evidence:** The dynamic-spanners proof and verification notes.
- **Open issue:** A comparison is not a theorem transfer when it changes terminal coverage, horizon, or whether paths are explicitly reported.

## Algorithm review

- **Checked:** Update time, stretch, preprocessing/space, recourse, query or path-reporting time, and assumptions on `n`, `m`, `U`, `h`, and `D` are separate fields. Tracked-terminal and full-horizon rows are not merged.
- **Evidence:** `problems/dynamic-spanners/verify/` and the source checkpoint audits.
- **Open issue:** Recheck whether each row uses edge updates, vertex updates, or a mixed model before comparing exponents.

## Source review

- **Checked:** The current graph payload has independent audits for tracked-terminal and fully dynamic regimes.
- **Evidence:** The verification files linked from the dynamic-spanners record.
- **Open issue:** Preserve exact source attribution and checkpoint identity when graph records are refreshed.

## Finite checks

The independent audit notes replay finite parameter comparisons and identify model mismatches. They do not prove the dynamic data structure for all update sequences and are not formal verification.

## Formal-verification boundary

`not-claimed`.

## Next review trigger

Reopen on a new graph checkpoint, a changed update/horizon model, a new recourse guarantee, or a change in whether paths are explicitly reported.
