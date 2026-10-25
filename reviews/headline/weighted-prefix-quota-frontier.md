# Review: Weighted-prefix and sparse-quota frontier

- **Record:** [`problems/weighted-prefix-quota-frontier`](../../problems/weighted-prefix-quota-frontier/)
- **Tier:** `A`
- **Last reviewed:** `2026-10-25`
- **Status:** `conditional`

## Scope

This review covers the T/U increments for ordered prefix quotas, laminar completion, sparse overlap, and deterministic kernel transfers.

## Proof review

- **Checked:** The card separates the common-coordinate assumptions, root cap `B0`, maximum cap `B`, shared weight families `p`, `Delta >= 1`, and the positive-root-charge condition from the resulting algorithms and kernels.
- **Evidence:** [`proof.md`](../../problems/weighted-prefix-quota-frontier/proof.md), `sources/checkpoint-t/`, and `sources/checkpoint-u/`.
- **Open issue:** Root-zero coordinates must remain zero in every other row, and the original completion oracle must be retained whenever a theorem uses it.

## Algorithm review

- **Checked:** End-to-end algorithms are separated from deterministic ground kernels. The current review records sparse packing `O_delta(k^(2 delta + 1))`, coverable-matroid `k d![k(1 + sum g_i)]^d`, transversal `O_d(k^(2d+1))`, and graph-matching `O(k^4)` or `O(k^5)` with parallel edges.
- **Evidence:** U payloads and the weighted-prefix verification notes.
- **Open issue:** Do not present a kernel size as an end-to-end running time until the completion, oracle, and reconstruction costs are stated.

## Source review

- **Checked:** T is parent-linked to S and U is parent-linked to T; manifests preserve payload names, byte counts, and hashes.
- **Evidence:** `sources/checkpoint-t/MANIFEST.json` and `sources/checkpoint-u/MANIFEST.json`.
- **Open issue:** Re-audit parent and payload hashes after every new increment.

## Finite checks

Kernel-scope and lower-bound notes provide finite certificate and parameter checks. They are not formal verification of the kernel transfer or of every end-to-end algorithm.

## Formal-verification boundary

`not-claimed`.

## Next review trigger

Reopen when a T/U successor changes the cap, coordinate, frequency, completion-oracle, or graph-matching assumptions, or when a kernel bound is promoted to an end-to-end claim.
