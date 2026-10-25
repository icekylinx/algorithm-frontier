# Review: Faster Subset Sum

- **Record:** [`problems/subset-sum-fast-deterministic`](../../problems/subset-sum-fast-deterministic/)
- **Tier:** `A`
- **Last reviewed:** `2026-10-25`
- **Status:** `reviewed`

## Scope

This review covers the exact deterministic indexed-witness algorithm for signed binary Subset Sum with a sub-half exponential time exponent.

## Proof review

- **Checked:** The proof map separates the profile construction, deterministic schedule, cost accounting, and witness extraction.
- **Evidence:** [`proof.md`](../../problems/subset-sum-fast-deterministic/proof.md) and the source verification scripts.
- **Open issue:** The public record does not claim a formal proof-assistant encoding.

## Algorithm review

- **Checked:** The card defines `n`, `L`, the target magnitude parameter `C`, and the exponent `E = 149809813343531 / 301754962128739` (approximately `0.4964618056`). It states exact decision plus indexed witness output and does not silently invent a space exponent.
- **Evidence:** [`README.md`](../../problems/subset-sum-fast-deterministic/README.md), `check_fast_costs.py`, and `check_profile.py`.
- **Open issue:** If a space bound is promoted later, it must receive its own row and model assumptions.

## Source review

- **Checked:** The source map identifies the imported fast-time payload and the verification artifacts used by the card.
- **Evidence:** [`sources.md`](../../problems/subset-sum-fast-deterministic/sources.md).
- **Open issue:** Recompute the rational exponent when a superseding checkpoint changes the schedule.

## Finite checks

The fast-cost and profile checks replay declared arithmetic identities and finite schedule data. They do not prove the algorithm on all instances and are not formal verification.

## Formal-verification boundary

`not-claimed`.

## Next review trigger

Reopen on a new fast-time checkpoint, a changed target model, a witness-interface change, or a newly claimed space bound.
