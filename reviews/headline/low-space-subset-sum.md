# Review: Low-space Subset Sum

- **Record:** [`problems/subset-sum-low-space-deterministic`](../../problems/subset-sum-low-space-deterministic/)
- **Tier:** `A`
- **Last reviewed:** `2026-10-25`
- **Status:** `reviewed`

## Scope

This review covers the exact deterministic decision and indexed-witness result for signed binary Subset Sum, including its time bound, writable-space bound, representation, and proof-map links.

## Proof review

- **Checked:** The curated proof map states the theorem contract, the range/ownership/cover components, and the distinction between decision and witness reconstruction.
- **Evidence:** [`proof.md`](../../problems/subset-sum-low-space-deterministic/proof.md) and the low-space source review tree.
- **Open issue:** The repository does not formalize the full argument in a proof assistant.

## Algorithm review

- **Checked:** The card names `n` as the number of weights and `L` as the full binary encoding length, and separates time from writable bits.
- **Evidence:** The public contract records polynomial work times two to the power of `n/2`, and writable space polynomial in `n` and `L` times two to the power of `E_S n`, with `E_S = 18261635770550353 / 10^17 = 0.18261635770550353`.
- **Open issue:** A future machine-model change must restate whether counters, read-only input, and witness indices are charged as writable bits.

## Source review

- **Checked:** The source tree preserves the imported low-space payload and its verification scripts; the curated card points to the exact source boundary.
- **Evidence:** [`sources.md`](../../problems/subset-sum-low-space-deterministic/sources.md) and `sources/subset-sum/low-space/`.
- **Open issue:** Recheck relative links and source commit attribution when a new checkpoint replaces the current payload.

## Finite checks

The range, resource, structural, and proof-replay scripts can be run from the source verification directory. They check finite identities and declared resource expressions. They do not establish correctness for every input or constitute a formal verification of the complete algorithm.

## Formal-verification boundary

`not-claimed`. No proof-assistant development is included.

## Next review trigger

Reopen this report when the low-space source theorem, bit model, exact exponent, or witness interface changes.
