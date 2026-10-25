# Checkpoint X — reading guide and archive identity

**Status: draft.** **Curation: source-only; no promoted result card.**

This directory preserves the nine mathematical drafts and the original archive README uploaded as checkpoint X. Every payload below is copied byte-for-byte from `checkpoint_X_incremental_drafts_2026-10-25.zip`; the manifest records the supplied archive inventory. The drafts are English research material for proof, algorithm, and source review. No result in this increment is treated as verified or publication-ready. The repository adds non-promoted draft cards only as review handles; they remain outside the stable catalogue.

## Payload by mathematical family

| Family | Drafts | Current interpretation |
|---|---|---|
| Exact sensitivity preservation | `01_exact_single_failure_arborescences_and_matroid_intersection.md`; `09_valuated_matroid_intersection.md` | Candidate `O(k^(3/2))`-record single-element-failure summaries for two-matroid and valuated-matroid intersection; arborescence specialization is stated separately. Fixed-rank and oracle/valuation assumptions must remain explicit. |
| Subset Sum | `02_deterministic_subset_sum_increment.md` | Incremental deterministic signed-binary exponent `149809813343531/301825962128739` (approximately `0.4963450204`), conditional on the pinned repository compiler and proof contracts. |
| Boundary and graph certificates | `03_correlated_fault_boundary_and_persistence_sparsifiers.md`; `05_colored_graph_and_vertex_failure_certificates.md` | Candidate correlated-failure certificates for persistent boundary spaces and exact weighted-prefix connectivity/MSF. Filtration order, cost order, field, and label model are separate parameters. |
| Matroid failure summaries | `04_sharp_represented_matroid_failure_summaries.md`; `06_arbitrary_matroid_and_submodular_failure_summaries.md` | Represented-matroid polynomial lift versus arbitrary-matroid rank-only FPT summary. The arbitrary-oracle construction does not inherit represented-matroid cost-prefix guarantees. |
| Packing and matching summaries | `07_represented_resource_packing_transfer.md` | Candidate represented-resource transfer with explicit packing/failure parameters; arbitrary-oracle resource comparisons remain out of scope. |
| Boolean linear optimisation | `08_boolean_linear_optimization_compiler.md` | Parameterised interval/slack compiler built on a supplied Subset Sum backend; no universal dominance claim. |

## Review boundary

The README in the original archive records the author's baseline scope and limitations. The repository keeps those caveats. The present increment is source-only until the external reviewer checks the reduction, model, complexity accounting, and literature boundary for each family. The non-promoted draft cards link back to the exact payload and keep the `Draft` label until all three review roles (proof, algorithm, source) have reports.

- Archive inventory: [`MANIFEST.json`](MANIFEST.json).
- Repository reference: `icekylinx/algorithm-frontier` at commit `37b31138bf102a83d9efb2cbe44437eec45ae3c2`.
- Original archive overview: [`README.md`](README.md).
- Provenance/review inventory: [`reviews/backlog/checkpoint-x-drafts.md`](../../reviews/backlog/checkpoint-x-drafts.md).
