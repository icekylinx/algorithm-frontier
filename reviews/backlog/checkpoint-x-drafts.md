# Checkpoint X draft intake and review backlog

**Status: draft intake only.** No checkpoint X claim has been promoted to a stable result card. The complete source tree is under [`sources/checkpoint-x/`](../../sources/checkpoint-x/); its uploaded ZIP identity and 39-file inventory are recorded in [`MANIFEST.json`](../../sources/checkpoint-x/MANIFEST.json).

## Provenance

- Archive: `checkpoint_X_incremental_drafts_2026-10-25(1).zip` (297,808 bytes; see the manifest for the SHA-256 digest)
- Stated repository reference: `icekylinx/algorithm-frontier` at `37b31138bf102a83d9efb2cbe44437eec45ae3c2`
- Stated attribution: Yilin Liu and GPT-6 Astra Pro
- Source maturity: research drafts for external proof, algorithm, and source review; no formal verification, exhaustive priority clearance, or external peer review
- Parent archive: not declared in the upload; no inherited manuscript or backup copy is inferred

## Family review matrix

| Family | Payloads | Candidate headline (still draft) | Highest-priority gates |
|---|---|---|---|
| Exact sensitivity, flow, and matching | `01`, `09`, `10`, `12`, `13`, `14`, `16` | One-failure summaries for matroid intersection, arborescences, min-cost flow, matching, and price sensitivity; displayed supports range from `O(k^(3/2))` to `O(n^(3/2) lambda^(1/4))` and `O(N+r sqrt(min{N,r^2}))`. | Reproduce exchange/residual reductions; separate rank, flow, matching, and sampling models; charge oracle calls, rational arithmetic, output, and workspace. |
| Subset Sum | `02` | Conditional deterministic signed-binary exponent `158153814247997/318927986919134 ≈ 0.4958919278`, with indexed witness recovery. | Recompute every contact inequality and outer ledger; pin the compiler and witness contract; keep the no-space-combination caveat. |
| Correlated spectral, regression, and seminorm summaries | `03`, `11`, `15`, `17`, `18`, `19`, `26` | Uniform correlated-failure spectral/PSD, weak-regression, graded-incidence, and seminorm transfers. | Check label degree, rank/field dependence, effective dimension, uniform versus per-query probability, and existential versus constructive status. |
| Matroid, packing, cuts, and whole blocks | `04`, `05`, `06`, `07`, `27`, `28`, `29` | Represented and oracle rank summaries, exact label cuts, adaptive quotient resparsification, and whole-item extensions. | Keep represented and arbitrary-oracle claims separate; verify exact decoders, failure labels, filtration/order, rank clipping, and bit bounds. |
| Boolean linear compiler | `08` | Support-sensitive interval/slack compiler conditional on an imported Subset Sum backend. | Recheck interval exactness, branch count, slack parameter, equality handling, witness recovery, and backend space. |
| Group, affine, metric, quotient-rank, and obstruction boundaries | `20`, `30`, `31`, `32`, `33`, `35`, `36`, `37`, `38` | Arbitrary-group Cayley, subgroup/coset, Hilbert metric, modular, quotient-rank, exact-separation, few-orbit, and non-Fano boundary results. | Check finite-group access, compact input model, exact-rational oracle, transitivity, coNP reduction, and the precise scope of lower/obstruction claims. |
| Quantum, Pauli, qudit, and stabilizer blocks | `21`, `22`, `23`, `24`, `25`, `34` | Locality-independent positive-Pauli, prime/composite-qudit, commuting-surrogate, and arbitrary-dimension stabilizer-block summaries. | Keep local dimension, factorization, locality, commutation, whole-block semantics, Hilbert dimension, and compact versus exponential construction explicit. |

## Review protocol

Each family receives separate proof, algorithm, and source notes. A headline may be promoted only after all three roles have addressed the gates above and the card records the exact model and parameters. Until then, any card must say `Draft checkpoint X`, link the payloads, and state `formal verification: not claimed`.

Finite scripts are evidence only. The current X-specific script, [`tools/verify_checkpoint_x_constants.py`](../../tools/verify_checkpoint_x_constants.py), checks the exact Subset Sum exponent and outer-ledger rational identities, together with the strict comparison to the pinned deterministic baseline. Future scripts may check bounded group, non-Fano, or rational examples only when the domain and expected identity are explicit.

The first detailed proof pass for payloads \`01\`, \`03\`, \`05\`, and \`09\` is recorded in [\`checkpoint-x-proof-review-01.md\`](checkpoint-x-proof-review-01.md). The note separates applied wording repairs from unresolved theorem gates; it does not promote any result.

## Next passes

1. Reproduce each displayed proof lemma in a short reviewer note and mark every missing quantifier or rank assumption.
2. Charge preprocessing, query, output, workspace, and exact-arithmetic costs separately.
3. Re-open primary comparators and retain only claims supported by the cited source and stated model.
4. Promote no family from source-only status until its three review roles and finite evidence (if any) are recorded in the registry.
